import pg from "pg";
import type { Code, Entitlement, Session, Store } from "./store.js";

export class PgStore implements Store {
  constructor(private pool: pg.Pool) {}
  async addCodes(codes: Code[]) {
    for (const c of codes) await this.pool.query("INSERT INTO activation_codes(code,plan,batch,expires_at) VALUES($1,$2,$3,$4)", [c.code, c.plan, c.batch, c.expiresAt]);
  }
  async redeem(code: string, email: string, now: Date) {
    const client = await this.pool.connect();
    try {
      await client.query("BEGIN");
      const r = await client.query("SELECT * FROM activation_codes WHERE code=$1 FOR UPDATE", [code]);
      const row = r.rows[0];
      if (!row) { await client.query("ROLLBACK"); return "invalid" as const; }
      if (row.redeemed_by) { await client.query("ROLLBACK"); return "used" as const; }
      if (row.expires_at && new Date(row.expires_at) < now) { await client.query("ROLLBACK"); return "expired" as const; }
      await client.query("UPDATE activation_codes SET redeemed_by=$2, redeemed_at=$3 WHERE code=$1", [code, email, now]);
      await client.query("INSERT INTO entitlements(email,plan,batch,expires_at) VALUES($1,$2,$3,$4) ON CONFLICT DO NOTHING", [email, row.plan, row.batch, row.expires_at]);
      await client.query("COMMIT");
      return { email, plan: row.plan, batch: row.batch, expiresAt: row.expires_at ? new Date(row.expires_at) : null } as Entitlement;
    } catch (err) { await client.query("ROLLBACK"); throw err; } finally { client.release(); }
  }
  async entitlementsFor(email: string, now: Date) {
    const r = await this.pool.query("SELECT * FROM entitlements WHERE email=$1 AND (expires_at IS NULL OR expires_at>$2)", [email, now]);
    return r.rows.map(x => ({ email: x.email, plan: x.plan, batch: x.batch, expiresAt: x.expires_at ? new Date(x.expires_at) : null }));
  }
  async addSession(s: Session) {
    await this.pool.query("INSERT INTO live_sessions(id,title,plan,batch,webinar_id,scheduled_at,duration_minutes,status) VALUES($1,$2,$3,$4,$5,$6,$7,$8)", [s.id, s.title, s.plan, s.batch, s.webinarId, s.scheduledAt, s.durationMinutes, s.status]);
  }
  private map(x: any): Session { return { id: x.id, title: x.title, plan: x.plan, batch: x.batch, webinarId: x.webinar_id, scheduledAt: new Date(x.scheduled_at), durationMinutes: x.duration_minutes, status: x.status }; }
  async getSession(id: string) { const r = await this.pool.query("SELECT * FROM live_sessions WHERE id=$1", [id]); return r.rows[0] ? this.map(r.rows[0]) : null; }
  async listSessions(plans: string[]) { const r = await this.pool.query("SELECT * FROM live_sessions WHERE plan = ANY($1) ORDER BY scheduled_at", [plans]); return r.rows.map(x => this.map(x)); }
}
