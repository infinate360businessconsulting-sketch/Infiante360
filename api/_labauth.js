// Stateless invite and session tokens for the practice lab (no database). Secret: LAB_SECRET (Vercel env var only).
const crypto = require("crypto");
const b64 = (s) => Buffer.from(s).toString("base64url");
const hmac = (secret, msg) => crypto.createHmac("sha256", secret).update(msg).digest("hex");
const safeEq = (a, b) => { const x = Buffer.from(String(a)), y = Buffer.from(String(b)); return x.length === y.length && crypto.timingSafeEqual(x, y); };
const norm = (e) => String(e || "").trim().toLowerCase();

// invite code = "<expiryDays since epoch>.<20 hex chars>"
function makeInvite(secret, email, expiryDay) { return expiryDay + "." + hmac(secret, "invite|" + norm(email) + "|" + expiryDay).slice(0, 20); }
function checkInvite(secret, email, code, nowMs) {
  const m = /^(\d{4,6})\.([0-9a-f]{20})$/.exec(String(code || "").trim());
  if (!m || !secret) return false;
  if (Math.floor((nowMs || Date.now()) / 86400000) > Number(m[1])) return false;
  return safeEq(makeInvite(secret, email, m[1]), m[0]);
}
function makeSession(secret, email, nowMs, hours) {
  const exp = (nowMs || Date.now()) + (hours || 12) * 3600000;
  const body = b64(norm(email) + "|" + exp);
  return body + "." + hmac(secret, "session|" + body);
}
function checkSession(secret, token, nowMs) {
  const parts = String(token || "").split(".");
  if (parts.length !== 2 || !secret) return null;
  if (!safeEq(hmac(secret, "session|" + parts[0]), parts[1])) return null;
  const [email, exp] = Buffer.from(parts[0], "base64url").toString().split("|");
  return Number(exp) > (nowMs || Date.now()) ? email : null;
}
const cookieOf = (req, name) => ((req.headers.cookie || "").split(/;\s*/).map((c) => c.split("=")).find((p) => p[0] === name) || [])[1];
module.exports = { makeInvite, checkInvite, makeSession, checkSession, cookieOf, norm };
