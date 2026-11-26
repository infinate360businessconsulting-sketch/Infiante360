// POST {email, code}: checks the invite and sets a 12-hour HttpOnly session cookie. Needs LAB_SECRET.
const { checkInvite, makeSession } = require("./_labauth");
const hits = new Map();
module.exports = async (req, res) => {
  if (req.method !== "POST") { res.status(405).json({ ok: false }); return; }
  const secret = process.env.LAB_SECRET;
  if (!secret) { res.status(503).json({ ok: false, error: "Labs are not open yet." }); return; }
  const ip = (req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "unknown";
  const now = Date.now();
  const recent = (hits.get(ip) || []).filter((t) => now - t < 600000);
  if (recent.length >= 10) { res.status(429).json({ ok: false, error: "Too many tries. Wait a few minutes." }); return; }
  hits.set(ip, recent.concat(now));
  let body = req.body || {};
  if (typeof body === "string") { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  if (!body.email || !checkInvite(secret, body.email, body.code, now)) { res.status(401).json({ ok: false, error: "Email or invite code not recognised." }); return; }
  res.setHeader("Set-Cookie", "lab_session=" + makeSession(secret, body.email, now, 12) + "; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=43200");
  res.status(200).json({ ok: true, next: "/lab" });
};
