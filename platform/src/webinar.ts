// Webinar.gg adapter. Authentication (Bearer account token, premium plan required, join tokens mandatory for iframe embeds) matches https://webinar.gg/docs/authentication (updated 2026-11-06).
// Other endpoint details follow the docs supplied by the owner; confirm with the vendor before production.
export type CreateWebinarInput = { title: string; date: string; time: string; meridiem: "AM" | "PM"; durationMinutes: number };
export type Fetcher = typeof fetch;

export class WebinarGg {
  constructor(private base: string, private token: string, private f: Fetcher = fetch) {}
  private async call(path: string, body: unknown) {
    const res = await this.f(`${this.base}${path}`, { method: "POST", headers: { Authorization: `Bearer ${this.token}`, "Content-Type": "application/json" }, body: JSON.stringify(body) });
    if (res.status === 401) throw new Error("Webinar.gg rejected the token (missing, malformed or revoked)");
    if (res.status === 403) throw new Error("Webinar.gg refused the call: the account needs an active premium plan, or the resource belongs to another account");
    if (!res.ok) throw new Error(`Webinar.gg ${path} failed with ${res.status}`);
    return (await res.json()) as Record<string, unknown>;
  }
  async createWebinar(i: CreateWebinarInput) {
    const r = await this.call("/webinar/", { ...i, timezone: "Asia/Kolkata", authentication: true, requireLogin: true, recordingEnabled: true, watermarkEnabled: true, requireApproval: true });
    const id = (r.webinarId ?? r.id ?? (r.data as any)?.id) as string | undefined;
    if (!id) throw new Error("Webinar.gg response had no webinar id");
    return { webinarId: String(id) };
  }
  async createJoinToken(webinarId: string, p: { firstName: string; lastName: string; email: string }) {
    const r = await this.call("/webinar/join-token", { webinarId, ...p, phone: "", passcode: "" });
    const token = (r.token ?? (r.data as any)?.token) as string | undefined;
    if (!token) throw new Error("Webinar.gg response had no join token");
    return { token };
  }
}

// Recording export is NOT confirmed by the vendor documentation. Keep this behind an adapter and leave publishing off until confirmed.
export interface RecordingProvider { getCompletedRecording(webinarId: string): Promise<{ downloadUrl: string } | null>; }
export class UnconfirmedRecordingProvider implements RecordingProvider {
  async getCompletedRecording(): Promise<null> { return null; }
}
