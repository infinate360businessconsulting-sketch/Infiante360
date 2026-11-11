import test from "node:test";
import assert from "node:assert/strict";
import type { AddressInfo } from "node:net";
import { makeApp } from "../src/app.js";
import { MemoryStore } from "../src/store.js";
import { WebinarGg } from "../src/webinar.js";
import { retrieve, loadKnowledge } from "../src/assistant.js";
import { sign, verify } from "../src/auth.js";

const cfg: any = { PORT: 0, PUBLIC_ORIGIN: "https://example.com", ADMIN_API_KEY: "a".repeat(30), SESSION_SECRET: "s".repeat(30), WEBINAR_GG_API_TOKEN: "t", WEBINAR_GG_API_BASE: "https://w.test/api/v1", ANTHROPIC_API_KEY: "k", ANTHROPIC_MODEL: "m" };
const calls: string[] = [];
const wf: any = async (url: string) => { calls.push(url); return { ok: true, status: 200, json: async () => (url.endsWith("/webinar/") ? { webinarId: "W1" } : { token: "TOK" }) }; };
const af: any = async () => ({ ok: true, status: 200, json: async () => ({ content: [{ text: "grounded answer" }] }) });

async function boot(nowIso = "2026-11-20T09:00:00+05:30") {
  const store = new MemoryStore();
  const app = makeApp({ cfg, store, webinar: new WebinarGg(cfg.WEBINAR_GG_API_BASE, "t", wf), chunks: loadKnowledge(new URL("../knowledge", import.meta.url).pathname), assistantFetch: af, now: () => new Date(nowIso) });
  const srv = app.listen(0); const base = `http://127.0.0.1:${(srv.address() as AddressInfo).port}`;
  const req = (p: string, o: any = {}) => fetch(base + p, { ...o, headers: { "content-type": "application/json", ...(o.headers || {}) }, body: o.body ? JSON.stringify(o.body) : undefined });
  return { srv, req };
}
const A = { "x-admin-key": "a".repeat(30) };

test("admin endpoints reject missing key", async () => {
  const { srv, req } = await boot();
  assert.equal((await req("/v1/admin/codes", { method: "POST", body: { plan: "aep", batch: "b1", count: 1 } })).status, 401);
  srv.closeAllConnections(); srv.close();
});

test("code redeem is single-use and unlocks join only for enrolled batch in window", async () => {
  const { srv, req } = await boot();
  const codes = (await (await req("/v1/admin/codes", { method: "POST", headers: A, body: { plan: "aep", batch: "b1", count: 2 } })).json()).codes;
  assert.equal(codes.length, 2);
  const r1 = await req("/v1/redeem", { method: "POST", body: { email: "L@x.com", code: codes[0] } });
  assert.equal(r1.status, 200);
  const { token } = await r1.json();
  assert.equal((await req("/v1/redeem", { method: "POST", body: { email: "o@x.com", code: codes[0] } })).status, 400);
  const sid = (await (await req("/v1/admin/sessions", { method: "POST", headers: A, body: { title: "AEP class", plan: "aep", batch: "b1", date: "2026-11-20", time: "09:00", meridiem: "AM", durationMinutes: 120 } })).json()).id;
  const auth = { authorization: `Bearer ${token}` };
  const list = await (await req("/v1/sessions", { headers: auth })).json();
  assert.equal(list.sessions.length, 1);
  const j = await req(`/v1/sessions/${sid}/join-token`, { method: "POST", headers: auth });
  assert.equal(j.status, 200);
  assert.equal((await j.json()).token, "TOK");
  assert.equal((await req(`/v1/sessions/${sid}/join-token`, { method: "POST" })).status, 401);
  srv.closeAllConnections(); srv.close();
});

test("other plan cannot join; outside window denied", async () => {
  const { srv, req } = await boot("2026-11-25T09:00:00+05:30");
  const codes = (await (await req("/v1/admin/codes", { method: "POST", headers: A, body: { plan: "other", batch: "zz", count: 1 } })).json()).codes;
  const { token } = await (await req("/v1/redeem", { method: "POST", body: { email: "a@x.com", code: codes[0] } })).json();
  const sid = (await (await req("/v1/admin/sessions", { method: "POST", headers: A, body: { title: "AEP class", plan: "aep", batch: "b1", date: "2026-11-20", time: "09:00", meridiem: "AM", durationMinutes: 120 } })).json()).id;
  assert.equal((await req(`/v1/sessions/${sid}/join-token`, { method: "POST", headers: { authorization: `Bearer ${token}` } })).status, 403);
  srv.closeAllConnections(); srv.close();
});

test("assistant is grounded and requires sign-in", async () => {
  const { srv, req } = await boot();
  assert.equal((await req("/v1/assistant", { method: "POST", body: { question: "What is XDM?" } })).status, 401);
  const codes = (await (await req("/v1/admin/codes", { method: "POST", headers: A, body: { plan: "aep", batch: "b1", count: 1 } })).json()).codes;
  const { token } = await (await req("/v1/redeem", { method: "POST", body: { email: "a@x.com", code: codes[0] } })).json();
  const ok = await (await req("/v1/assistant", { method: "POST", headers: { authorization: `Bearer ${token}` }, body: { question: "What is an XDM schema?" } })).json();
  assert.equal(ok.grounded, true);
  const none = await (await req("/v1/assistant", { method: "POST", headers: { authorization: `Bearer ${token}` }, body: { question: "zzzz qqqq unrelated" } })).json();
  assert.equal(none.grounded, false);
  srv.closeAllConnections(); srv.close();
});

test("tokens expire and tampering fails; retrieval ranks relevant chunk", () => {
  const t = sign({ email: "a" }, "s".repeat(30), 10, 0);
  assert.ok(verify(t, "s".repeat(30), 5000));
  assert.equal(verify(t, "s".repeat(30), 20000), null);
  assert.equal(verify(t + "x", "s".repeat(30), 5000), null);
  assert.ok(retrieve(loadKnowledge(new URL("../knowledge", import.meta.url).pathname), "identity graph namespaces")[0].text.includes("Identity"));
});
