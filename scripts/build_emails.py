#!/usr/bin/env python3
"""Generate cold-email HTML + plain-text templates for four segments into docs/outreach/email-html/.
Dynamic values (fee, cohort, WhatsApp) come from content/cxo-hive.json. Merge tags are left as {{first}}, {{company}}, {{signal}}, {{postal_address}}, {{unsubscribe_mailto}}.
Send only after human review; B2B only; honour STOP. No client, result or certification claims."""
import json, os, datetime, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(R, "content", "cxo-hive.json"), encoding="utf-8"))
BASE = "https://infiante360techacademy.com/"
LP = BASE + "lp/adobe-martech-conversation.html"
CAL = "https://calendar.app.google/5CHbD1hmQBHxcJyy5"
EMAIL = "infinate360businessconsulting@gmail.com"
OUT = os.path.join(R, "docs", "outreach", "email-html")
os.makedirs(OUT, exist_ok=True)
c = next((x for x in CFG["cohorts"] if x["status"] == "open"), None)
kick = datetime.date.fromisoformat(c["kickoff"]).strftime("%-d %B %Y") if c else "dates to be announced"

SEGS = {
 "enterprise": dict(subject="{{company}} and customer data: a 30-minute architecture check", pre="An independent view on identity, schemas and activation, before the architecture gets locked.",
   kicker="ENTERPRISE ADOBE TEAMS", head="Is your customer-data architecture ready for what comes next?",
   lead="I noticed {{signal}}. Most MarTech programs do not stall on tools; they stall on identity, data quality and decision rights. I advise enterprise teams on Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics.",
   bullets=["Schemas, identity and Profile configuration reviewed against your use cases", "Ingestion, consent and governance gaps surfaced early", "Prioritised findings and a 30/60/90-day plan you can act on"],
   cta="Book a 30-minute review call", utm="enterprise", ps="If an independent one-page checklist is more useful than a call, reply 'checklist' and I will send it."),
 "cxo": dict(subject="CXO Hive: a 10-week live program for C-level leaders", pre=f"Architecture, AI governance and an investment case, built on your own organisation. Fee {CFG['fee_label']}.",
   kicker="C-LEVEL ONLY", head="From MarTech and AI pilots to a board-ready plan in ten weekends",
   lead="I noticed {{signal}}. CXO Hive is a live program I run for C-level leaders who sponsor MarTech, customer data and AI transformation. It is strategy and architecture led, not a tools course.",
   bullets=["Live every Saturday and Sunday plus two short midweek checkpoints", "Six deliverables you keep: investment case, target architecture, operating model, AI backlog, 90-day roadmap, board briefing", f"Fee {CFG['fee_label']}; first cohort kick-off {kick}. No business result is guaranteed"],
   cta="See CXO Hive and apply", utm="cxo", ps="If your leadership team would join together, ask about a private in-house cohort."),
 "training": dict(subject="Adobe MarTech training for {{company}}'s team", pre="Role-based tracks, hands-on labs and assessments built on your own use cases.",
   kicker="CORPORATE TRAINING", head="Build the Adobe MarTech skills your team actually needs",
   lead="I noticed {{signal}}. We run tailored Adobe MarTech training for engineers, analysts, architects and managers, with labs, projects and assessments rather than slide-only sessions.",
   bullets=["Skills baseline for your team before the plan is set", "Labs and projects on your use cases, not generic demos", "Live, recorded or blended delivery with progress reporting"],
   cta="Request a training proposal", utm="training", ps="I can share a sample syllabus and lab outline first so you can judge fit."),
 "capacity": dict(subject="Specialist Adobe capacity for your delivery team", pre="Architects and engineers for AEP, RTCDP, AJO, CJA and Web SDK work, scoped per project.",
   kicker="DELIVERY PARTNERS", head="A gap on an Adobe project? Add specialist capacity quickly",
   lead="I noticed {{signal}}. Infinate360 provides specialist Adobe architects and engineers to delivery teams, scoped per project rather than a long commitment.",
   bullets=["AEP, Real-Time CDP, Journey Optimizer, CJA and Web SDK skills", "Contract, contract-to-hire or managed pod", "Scenario-based readiness check and onboarding prepared before day one"],
   cta="Tell us about the gap", utm="capacity", ps="If useful, I can outline the roles we cover and how engagements are structured."),

 "career": dict(subject="Move into Adobe MarTech: live career accelerator, six phases", pre="Live online training in AEP, RTCDP, AJO, CJA, Web SDK and Agentic AI, with projects and interview preparation. Fee ₹60,000.",
   kicker="CAREER ACCELERATOR", head="Don't restart your career. Redirect it into Adobe MarTech.",
   lead="You asked about, or showed interest in, Adobe MarTech learning, so I am sharing how the Infinite360 Tech Academy career accelerator works. It builds on your current engineering, data, analytics, cloud or consulting experience.",
   bullets=["Live online classes with recordings, in six phases across AEP, Real-Time CDP, Journey Optimizer, CJA, Web SDK and Agentic AI", "Simulators, an enterprise-style project, troubleshooting scenarios and interview preparation", "Program fee ₹60,000. Training outcomes depend on your participation; no job, salary or certification is guaranteed"],
   cta="See the program and apply", utm="career", ps="Not ready to commit? Ask about the free guides and demo sessions first.", warm=True),
}
INK, MUT, IND, VIO = "#0F172A", "#64748B", "#4F46E5", "#7C3AED"


def link(seg):
    return f"{LP}?utm_source=cold-email&utm_medium=email&utm_campaign=martech-outreach&utm_content={seg['utm']}"


def build(key, s):
    e = html.escape
    reason = 'You are receiving this because you enquired about or showed interest in Infinite360 programs.' if s.get('warm') else 'You are receiving this one-to-one business email because of your role at {{company}}.'
    lis = "".join(f'<tr><td valign="top" style="padding:0 10px 10px 0;color:{IND};font-size:16px;line-height:22px">&#10003;</td><td style="padding:0 0 10px 0;font:15px/22px Arial,Helvetica,sans-serif;color:{INK}">{e(b)}</td></tr>' for b in s["bullets"])
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><meta name="x-apple-disable-message-reformatting">
<title>{e(s['subject'])}</title>
<!--[if mso]><style>td,p,a{{font-family:Arial,sans-serif!important}}</style><![endif]-->
<style>@media only screen and (max-width:620px){{.w{{width:100%!important}}.p{{padding:22px 18px!important}}.h{{font-size:22px!important;line-height:28px!important}}.btn a{{display:block!important}}}}</style></head>
<body style="margin:0;padding:0;background:#F1F5F9">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:#F1F5F9">{e(s['pre'])}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<!-- Subject: {e(s['subject'])} -->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#F1F5F9"><tr><td align="center" style="padding:24px 12px">
<table role="presentation" class="w" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:100%;background:#FFFFFF;border-radius:14px;overflow:hidden;border:1px solid #E2E8F0">
<tr><td bgcolor="{IND}" style="background:{IND};background-image:linear-gradient(135deg,{IND},{VIO});padding:26px 30px">
<div style="font:700 12px/16px Arial,Helvetica,sans-serif;letter-spacing:1.5px;color:#C7D2FE">{s['kicker']}</div>
<div class="h" style="font:700 26px/32px Arial,Helvetica,sans-serif;color:#FFFFFF;padding-top:8px">{e(s['head'])}</div></td></tr>
<tr><td class="p" style="padding:28px 30px 8px 30px;font:15px/24px Arial,Helvetica,sans-serif;color:{INK}">
<p style="margin:0 0 14px 0">Hi {{{{first}}}},</p><p style="margin:0 0 18px 0">{e(s['lead'])}</p>
<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 6px 0">{lis}</table></td></tr>
<tr><td class="p btn" align="left" style="padding:8px 30px 8px 30px"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{IND}" style="border-radius:8px;background:{IND}">
<a href="{link(s)}" style="display:inline-block;padding:14px 26px;font:700 15px/20px Arial,Helvetica,sans-serif;color:#FFFFFF;text-decoration:none;border-radius:8px">{e(s['cta'])} &rarr;</a></td></tr></table>
<p style="margin:12px 0 0 0;font:13px/20px Arial,Helvetica,sans-serif;color:{MUT}">Prefer to pick a time directly? <a href="{CAL}" style="color:{IND}">Open my calendar</a> or WhatsApp <a href="{CFG['whatsapp']}" style="color:{IND}">+91 82968 93895</a>.</p></td></tr>
<tr><td class="p" style="padding:18px 30px 6px 30px;font:15px/24px Arial,Helvetica,sans-serif;color:{INK}"><p style="margin:0 0 14px 0;color:{MUT}">P.S. {e(s['ps'])}</p>
<p style="margin:0">Regards,<br><strong>Pavan Babu Gandla</strong><br><span style="color:{MUT};font-size:13px">Founder, Infinate360 &middot; Adobe MarTech, customer data and agentic AI</span></p></td></tr>
<tr><td style="padding:18px 30px 24px 30px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="border-top:1px solid #E2E8F0;padding-top:14px;font:11px/17px Arial,Helvetica,sans-serif;color:{MUT}">
Infinate360 is independent and not affiliated with or endorsed by Adobe. Training and advisory outcomes depend on participation and execution; no job, salary, certification or business result is guaranteed.<br>
{e(reason)} If this is not relevant, reply STOP or <a href="mailto:{EMAIL}?subject=STOP" style="color:{MUT}">click here</a> and I will not contact you again.<br>{{{{postal_address}}}}</td></tr></table></td></tr>
</table></td></tr></table></body></html>
"""


def text(key, s):
    return "\n".join([f"Subject: {s['subject']}", "", "Hi {{first}},", "", s["lead"], ""] + [f"- {b}" for b in s["bullets"]] + ["", f"{s['cta']}: {link(s)}", f"Calendar: {CAL}", f"WhatsApp: {CFG['whatsapp']}", "", f"P.S. {s['ps']}", "", "Regards,", "Pavan Babu Gandla", "Founder, Infinate360", "",
                  "Independent; not affiliated with Adobe. No job, salary, certification or business result is guaranteed.",
                  "If this is not relevant, reply STOP and I will not contact you again. {{postal_address}}", ""])


for k, s in SEGS.items():
    open(os.path.join(OUT, f"{k}.html"), "w", encoding="utf-8").write(build(k, s))
    open(os.path.join(OUT, f"{k}.txt"), "w", encoding="utf-8").write(text(k, s))
idx = "<!doctype html><meta charset=utf-8><title>Email previews</title><body style='font-family:Arial;padding:20px;background:#eee'>" + "".join(f"<h3>{k}: {html.escape(s['subject'])}</h3><iframe src='{k}.html' style='width:660px;height:760px;border:1px solid #ccc;background:#fff'></iframe>" for k, s in SEGS.items())
open(os.path.join(OUT, "preview.html"), "w", encoding="utf-8").write(idx)
print("Wrote", len(SEGS), "segments to", OUT)
