import express from "express";
import { randomBytes, randomUUID } from "node:crypto";
import { z } from "zod";
import type { Config } from "./config.js";
import type { Store } from "./store.js";
import { WebinarGg } from "./webinar.js";
import { sign, verify, safeEqual } from "./auth.js";
import { ask, retrieve, type Chunk } from "./assistant.js";

export function makeApp(deps: { cfg: Config; store: Store; webinar?: WebinarGg; chunks: Chunk[]; assistantFetch?: typeof fetch; now?: () => Date }) {
  const { cfg, store, chunks } = deps;
  const now = deps.now ?? (() => new Date());
  const app = express();
  app.disable("x-powered-by");
  app.use(express.json({ limit: "20kb" }));
  app.use((req, res, next) => {
    res.setHeader("Access-Control-Allow-Origin", cfg.PUBLIC_ORIGIN);
    res.setHeader("Access-Control-Allow-Headers", "authorization, content-type");
    res.setHeader("Vary", "Origin");
    res.setHeader("X-Content-Type-Options", "nosniff");
    if (req.method === "OPTIONS") return res.sendStatus(204);
    next();
  });
  const hits = new Map<string, { n: number; t: number }>();
  const limit = (max: number, windowMs: number) => (req: express.Request, res: express.Response, next: express.NextFunction) => {
    const k = `${req.path}:${req.ip}`, t = Date.now(), h = hits.get(k);
    if (!h || t - h.t > windowMs) { hits.set(k, { n: 1, t }); return next(); }
    if (++h.n > max) return res.status(429).json({ error: "Too many requests" });
    next();
  };
  const admin: express.RequestHandler = (req, res, next) => {
    const k = String(req.headers["x-admin-key"] ?? "");
    return safeEqual(k, cfg.ADMIN_API_KEY) ? next() : res.status(401).json({ error: "Unauthorized" });
  };
  const learner = (req: express.Request) => verify<{ email: string }>(String(req.headers.authorization ?? "").replace(/^Bearer /, ""), cfg.SESSION_SECRET, now().getTime());

  app.get("/healthz", (_q, r) => r.json({ ok: true }));

  app.post("/v1/admin/codes", admin, async (req, res) => {
    const b = z.object({ plan: z.string().min(2), batch: z.string().min(2), count: z.number().int().min(1).max(1000), expiresAt: z.string().datetime().optional() }).safeParse(req.body);
    if (!b.success) return res.status(400).json({ error: "Invalid request" });
    const codes = Array.from({ length: b.data.count }, () => ({ code: randomBytes(6).toString("hex").toUpperCase(), plan: b.data.plan, batch: b.data.batch, expiresAt: b.data.expiresAt ? new Date(b.data.expiresAt) : null, redeemedBy: null }));
    await store.addCodes(codes);
    res.status(201).json({ codes: codes.map(c => c.code) });
  });

  app.post("/v1/redeem", limit(10, 60_000), async (req, res) => {
    const b = z.object({ email: z.string().email(), code: z.string().min(6).max(40) }).safeParse(req.body);
    if (!b.success) return res.status(400).json({ error: "Invalid request" });
    const email = b.data.email.toLowerCase();
    const r = await store.redeem(b.data.code.trim().toUpperCase(), email, now());
    if (r === "invalid" || r === "used" || r === "expired") return res.status(400).json({ error: "This code cannot be used" });
    res.json({ token: sign({ email }, cfg.SESSION_SECRET, 8 * 3600, now().getTime()), plan: r.plan });
  });

  app.post("/v1/admin/sessions", admin, async (req, res) => {
    if (!deps.webinar) return res.status(503).json({ error: "Webinar.gg is not configured" });
    const b = z.object({ title: z.string().min(3), plan: z.string(), batch: z.string(), date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/), time: z.string().regex(/^\d{2}:\d{2}$/), meridiem: z.enum(["AM", "PM"]), durationMinutes: z.number().int().min(15).max(480) }).safeParse(req.body);
    if (!b.success) return res.status(400).json({ error: "Invalid request" });
    const { webinarId } = await deps.webinar.createWebinar(b.data);
    const [h, m] = b.data.time.split(":").map(Number);
    const hh = (h % 12) + (b.data.meridiem === "PM" ? 12 : 0);
    const scheduledAt = new Date(`${b.data.date}T${String(hh).padStart(2, "0")}:${String(m).padStart(2, "0")}:00+05:30`);
    const s = { id: randomUUID(), title: b.data.title, plan: b.data.plan, batch: b.data.batch, webinarId, scheduledAt, durationMinutes: b.data.durationMinutes, status: "scheduled" };
    await store.addSession(s);
    res.status(201).json({ id: s.id });
  });

  app.get("/v1/sessions", async (req, res) => {
    const u = learner(req); if (!u) return res.status(401).json({ error: "Sign in" });
    const ents = await store.entitlementsFor(u.email, now());
    const list = (await store.listSessions(ents.map(e => e.plan))).filter(s => ents.some(e => e.plan === s.plan && e.batch === s.batch));
    res.json({ sessions: list.map(s => ({ id: s.id, title: s.title, scheduledAt: s.scheduledAt, durationMinutes: s.durationMinutes, status: s.status })) });
  });

  app.post("/v1/sessions/:id/join-token", limit(30, 60_000), async (req, res) => {
    const u = learner(req); if (!u) return res.status(401).json({ error: "Sign in" });
    if (!deps.webinar) return res.status(503).json({ error: "Webinar.gg is not configured" });
    const s = await store.getSession(req.params.id);
    if (!s || s.status === "cancelled") return res.status(404).json({ error: "Session unavailable" });
    const ents = await store.entitlementsFor(u.email, now());
    if (!ents.some(e => e.plan === s.plan && e.batch === s.batch)) return res.status(403).json({ error: "Not enrolled" });
    const t = now().getTime(), start = s.scheduledAt.getTime();
    if (t < start - 30 * 60_000 || t > start + (s.durationMinutes + 120) * 60_000) return res.status(403).json({ error: "Outside the class window" });
    const first = u.email.split("@")[0].slice(0, 40);
    const { token } = await deps.webinar.createJoinToken(s.webinarId, { firstName: first, lastName: "Learner", email: u.email });
    res.json({ webinarId: s.webinarId, token });
  });

  app.post("/v1/assistant", limit(10, 60_000), async (req, res) => {
    const u = learner(req); if (!u) return res.status(401).json({ error: "Sign in" });
    if (!cfg.ANTHROPIC_API_KEY || !cfg.ANTHROPIC_MODEL) return res.status(503).json({ error: "Assistant is not configured" });
    const b = z.object({ question: z.string().min(3).max(1000) }).safeParse(req.body);
    if (!b.success) return res.status(400).json({ error: "Invalid request" });
    const ctx = retrieve(chunks, b.data.question);
    if (!ctx.length) return res.json({ answer: "I could not find this in the course material. Please ask your trainer.", grounded: false });
    const answer = await ask({ apiKey: cfg.ANTHROPIC_API_KEY, model: cfg.ANTHROPIC_MODEL, question: b.data.question, chunks: ctx, f: deps.assistantFetch });
    res.json({ answer, grounded: true });
  });

  app.use(express.static(new URL("../public", import.meta.url).pathname));
  app.use((err: unknown, _q: express.Request, res: express.Response, _n: express.NextFunction) => { console.error(err instanceof Error ? err.message : "error"); res.status(500).json({ error: "Server error" }); });
  return app;
}
