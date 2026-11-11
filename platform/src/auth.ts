import { createHmac, timingSafeEqual } from "node:crypto";
const b64 = (b: Buffer) => b.toString("base64url");
export function sign(payload: object, secret: string, ttlSec = 3600, now = Date.now()) {
  const body = b64(Buffer.from(JSON.stringify({ ...payload, exp: Math.floor(now / 1000) + ttlSec })));
  return `${body}.${b64(createHmac("sha256", secret).update(body).digest())}`;
}
export function verify<T = any>(token: string | undefined, secret: string, now = Date.now()): T | null {
  if (!token) return null;
  const [body, sig] = token.split(".");
  if (!body || !sig) return null;
  const good = createHmac("sha256", secret).update(body).digest();
  const given = Buffer.from(sig, "base64url");
  if (given.length !== good.length || !timingSafeEqual(given, good)) return null;
  const p = JSON.parse(Buffer.from(body, "base64url").toString());
  return p.exp * 1000 > now ? (p as T) : null;
}
export const safeEqual = (a: string, b: string) => { const x = Buffer.from(a), y = Buffer.from(b); return x.length === y.length && timingSafeEqual(x, y); };
