export type Code = { code: string; plan: string; batch: string; expiresAt: Date | null; redeemedBy: string | null };
export type Entitlement = { email: string; plan: string; batch: string; expiresAt: Date | null };
export type Session = { id: string; title: string; plan: string; batch: string; webinarId: string; scheduledAt: Date; durationMinutes: number; status: string };

export interface Store {
  addCodes(codes: Code[]): Promise<void>;
  redeem(code: string, email: string, now: Date): Promise<Entitlement | "invalid" | "used" | "expired">;
  entitlementsFor(email: string, now: Date): Promise<Entitlement[]>;
  addSession(s: Session): Promise<void>;
  getSession(id: string): Promise<Session | null>;
  listSessions(plans: string[]): Promise<Session[]>;
}

export class MemoryStore implements Store {
  codes = new Map<string, Code>();
  ents: Entitlement[] = [];
  sessions = new Map<string, Session>();
  async addCodes(c: Code[]) { for (const x of c) this.codes.set(x.code, x); }
  async redeem(code: string, email: string, now: Date) {
    const c = this.codes.get(code);
    if (!c) return "invalid" as const;
    if (c.redeemedBy) return "used" as const;
    if (c.expiresAt && c.expiresAt < now) return "expired" as const;
    c.redeemedBy = email;
    const ent = { email, plan: c.plan, batch: c.batch, expiresAt: c.expiresAt };
    this.ents.push(ent);
    return ent;
  }
  async entitlementsFor(email: string, now: Date) { return this.ents.filter(e => e.email === email && (!e.expiresAt || e.expiresAt > now)); }
  async addSession(s: Session) { this.sessions.set(s.id, s); }
  async getSession(id: string) { return this.sessions.get(id) ?? null; }
  async listSessions(plans: string[]) { return [...this.sessions.values()].filter(s => plans.includes(s.plan)); }
}
