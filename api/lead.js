// Lead webhook relay. The browser posts form data here (in addition to FormSubmit email);
// this function forwards it to LEAD_WEBHOOK_URL (n8n / Make / Zapier / CRM) kept in Vercel env vars.
// Optional: LEAD_WEBHOOK_SECRET is sent as the X-Webhook-Secret header so the receiver can verify the source.
const ALLOWED = ["first_name", "last_name", "name", "email", "phone", "company", "job_title", "country", "interest", "program", "tool",
  "preferred_contact", "message", "source_page", "form_type", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "referrer"];
const hits = new Map();

module.exports = async (req, res) => {
  if (req.method !== "POST") { res.status(405).json({ ok: false }); return; }
  const ip = (req.headers["x-forwarded-for"] || "").split(",")[0].trim() || "unknown";
  const now = Date.now();
  const recent = (hits.get(ip) || []).filter((t) => now - t < 60000);
  if (recent.length >= 5) { res.status(429).json({ ok: false }); return; }
  hits.set(ip, recent.concat(now));

  let body = req.body || {};
  if (typeof body === "string") { try { body = JSON.parse(body); } catch (e) { body = {}; } }
  if (body._honey) { res.status(200).json({ ok: true }); return; }
  const lead = {};
  for (const k of ALLOWED) if (typeof body[k] === "string") lead[k] = body[k].slice(0, 4000);
  if (!lead.email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(lead.email)) { res.status(400).json({ ok: false }); return; }
  lead.received_at = new Date().toISOString();

  const url = process.env.LEAD_WEBHOOK_URL;
  if (!url) { res.status(202).json({ ok: true, forwarded: false }); return; }
  try {
    const headers = { "Content-Type": "application/json" };
    if (process.env.LEAD_WEBHOOK_SECRET) headers["X-Webhook-Secret"] = process.env.LEAD_WEBHOOK_SECRET;
    const r = await fetch(url, { method: "POST", headers, body: JSON.stringify(lead) });
    res.status(200).json({ ok: r.ok, forwarded: true });
  } catch (err) {
    res.status(200).json({ ok: false, forwarded: false });
  }
};
