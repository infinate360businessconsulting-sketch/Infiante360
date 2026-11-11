// Webinar.gg adapter. Endpoints follow the vendor documentation supplied by the owner; confirm with the vendor before production.
export type CreateWebinarInput = { title: string; date: string; time: string; meridiem: "AM" | "PM"; durationMinutes: number };
export type Fetcher = typeof fetch;

export class WebinarGg {
  constructor(private base: string, private token: string, private f: Fetcher = fetch) {}
  private async call(path: string, body: unknown) {
    const res = await this.f(`${this.base}${path}`, { method: "POST", headers: { Authorization: `Bearer ${this.token}`, "Content-Type": "application/json" }, body: JSON.stringify(body) });
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
