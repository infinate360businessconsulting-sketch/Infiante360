#!/usr/bin/env python3
"""Career-accelerator learner campaign (3 emails) styled from the owner's ESP template. Opted-in / enquiring learners only.
Merge tags (ESP style): {{FirstName}} {{UnsubscribeURL}} {{postal_address}}. Output: docs/outreach/campaign-career-library/"""
import os, html
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(R, "docs", "outreach", "campaign-career-library"); os.makedirs(OUT, exist_ok=True)
B = "https://infiante360techacademy.com/"
LP = B + "lp/adobe-martech-conversation.html?utm_source=email&utm_medium=campaign&utm_campaign=career_library&utm_content=career"
DRIVE = "https://drive.google.com/file/d/11hkOjfB7a8z7V8ZJJVOyX9mSSlUxvMxQ/view?usp=sharing&utm_source=email&utm_medium=campaign&utm_campaign=career_library"
LOGO = "https://appbox12.mail250.com/uploadimages/infinate360businessconsulting/image/81349-Infinite360-Tech-Academy-Logo_youtube-.png"
HERO = "https://appbox12.mail250.com/uploadimages/infinate360businessconsulting/image/88154-Adobe-Resized.png"
WA = "https://wa.me/918296893895"; MAIL = "infinate360businessconsulting@gmail.com"
NAVY, CY, INK, MUT = "#06132f", "#00a8e8", "#071a36", "#526274"
e = html.escape


def btn(label, href, color="#ff1744"):
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td bgcolor="{color}" style="border-radius:10px"><a href="{href}" style="display:inline-block;padding:16px 28px;font:800 16px/20px Arial,Helvetica,sans-serif;color:#fff;text-decoration:none;border-radius:10px" target="_blank">{e(label)} &rarr;</a></td></tr></table>'


def rows(items, mark="&#10003;"):
    return "".join(f'<tr><td valign="top" style="padding:7px 10px 7px 0;color:{CY};font:700 15px/22px Arial">{mark}</td><td style="padding:7px 0;font:14px/21px Arial,Helvetica,sans-serif;color:#1f2937"><strong>{e(a)}</strong>{(" &mdash; " + e(b)) if b else ""}</td></tr>' for a, b in items)


def wrap(pre, kicker, h1, body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><title>{e(h1)}</title>
<style>@media only screen and (max-width:640px){{.w{{width:100%!important}}.p{{padding:24px 18px!important}}.h{{font-size:26px!important;line-height:31px!important}}}}</style></head>
<body style="margin:0;padding:0;background:#eef3f8"><div style="display:none;max-height:0;overflow:hidden;opacity:0;color:#eef3f8">{e(pre)}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#eef3f8"><tr><td align="center" style="padding:24px 10px">
<table role="presentation" class="w" width="680" cellpadding="0" cellspacing="0" border="0" style="width:680px;max-width:100%;background:#fff;border-radius:18px;overflow:hidden">
<tr><td align="center" bgcolor="{NAVY}" style="padding:22px 28px"><a href="{B}"><img src="{LOGO}" alt="Infinite360 Tech Academy" width="230" style="display:block;border:0;max-width:100%"></a></td></tr>
<tr><td bgcolor="#071a36"><img src="{HERO}" alt="Infinite360 Adobe MarTech and Agentic AI Career Accelerator" width="680" style="display:block;width:100%;max-width:680px;border:0"></td></tr>
<tr><td class="p" style="padding:34px 38px 8px"><p style="margin:0 0 8px;font:bold 13px/18px Arial;letter-spacing:1.5px;color:#009fe3">{kicker}</p>
<h1 class="h" style="margin:0 0 16px;font:800 32px/37px Arial,Helvetica,sans-serif;color:{INK}">{e(h1)}</h1>{body}
<tr><td align="center" bgcolor="{NAVY}" style="padding:26px 30px;font:13px/20px Arial,Helvetica,sans-serif;color:#cbd5e1"><strong style="color:#fff;font-size:14px">Infinite360 Tech Academy</strong><br>Practical Adobe MarTech &bull; Customer Data &bull; Analytics &bull; Agentic AI<br>
WhatsApp <a href="{WA}" style="color:#22d3ee;text-decoration:none">+91 82968 93895</a> | <a href="mailto:{MAIL}" style="color:#22d3ee;text-decoration:none">{MAIL}</a>
<p style="margin:12px 0 0;font-size:11px;line-height:17px;color:#94a3b8">Training outcomes depend on participation and practice; no job, salary, certification or business outcome is guaranteed. Infinite360 is independent and not affiliated with or endorsed by Adobe.<br>
You are receiving this because you enquired about or showed interest in Infinite360 MarTech learning. <a href="{{{{UnsubscribeURL}}}}" style="color:#94a3b8">Unsubscribe</a> or reply STOP.<br>{{{{postal_address}}}}</p></td></tr>
</table></td></tr></table></body></html>"""


def block(inner, bg="#fff"):
    return f'<tr><td class="p" style="padding:0 38px 28px;background:{bg}">{inner}</td></tr>'


LIB = [("Adobe Experience Platform", "architecture, datasets, ingestion, Profile, governance, segmentation, activation"), ("XDM and data modeling", "schemas, experience events, field groups"),
       ("Identity resolution and Customer 360", "namespaces, graphs, profile stitching"), ("Real-Time CDP", "audiences, destinations, activation workflows"),
       ("Adobe Journey Optimizer", "journeys, triggers, orchestration, decisioning"), ("Customer Journey Analytics", "connections, data views, attribution, dashboards"),
       ("Adobe Analytics", "implementation, tracking, reporting"), ("Adobe Web SDK", "data layers, datastreams, Edge Network"), ("Agentic AI and MCP", "agents, tool calling, governed data access")]
PROJ = [("Customer 360", "sources, XDM, identity, profile, audiences, activation"), ("Real-time transaction journey", "streaming event, profile, AJO trigger, communication"),
        ("RTCDP activation", "segment strategy, destinations, activation QA"), ("CJA executive intelligence", "cross-channel analysis and KPI storytelling"),
        ("Web SDK modernization", "data layer, Alloy.js, datastream, AEP event flow"), ("Agentic AI marketing assistant", "agent, governed tools, customer context, workflow automation")]
PATHS = "AEP Developer, AEP Data Engineer, Customer Data Engineer, CJA Analyst, MarTech Integration Engineer, AEP Architect, MarTech Architect, Adobe MarTech Consultant, MarTech Business Analyst, MarTech Program Manager"

E = []
E.append(("1-resources", "Your complete Adobe MarTech learning path, in one place", "Course resources for AEP, XDM, identity, RTCDP, AJO, CJA, Web SDK and Agentic AI.", "INFINITE360 TECH ACADEMY", "Your complete Adobe MarTech learning path starts here.", 0,
 f'<p style="margin:0 0 18px;font:17px/27px Arial,Helvetica,sans-serif;color:#40516a">Hi {{{{FirstName}}}},<br><br>If you want to strengthen your Adobe MarTech skills, or move from a technology, data, analytics, cloud or consulting background into enterprise MarTech, we have put the learning path in one place.</p></td></tr>'
 + block(btn("Open the course resources", DRIVE), "#fff")
 + block(f'<h2 style="margin:0 0 6px;font:800 22px/28px Arial;color:{INK}">What the library covers</h2><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows(LIB)}</table>', "#f8fafc")
 + block(f'<p style="margin:0;font:15px/24px Arial;color:{MUT}">Learn &rarr; Build &rarr; Implement &rarr; Deploy: platform knowledge connected to enterprise-style use cases. Reply to this email with your background and I will suggest where to start.</p>')))
E.append(("2-projects-pathways", "Build the projects employers ask about", "Six enterprise-style projects and the career pathways they point to.", "BUILD, DON'T JUST WATCH", "Don't restart your career. Redirect it.", 3,
 f'<p style="margin:0 0 18px;font:17px/27px Arial,Helvetica,sans-serif;color:#40516a">Hi {{{{FirstName}}}},<br><br>Your engineering, data, analytics, cloud or consulting experience is the foundation. The accelerator turns it into practised Adobe MarTech skill through enterprise-style projects, run on simulators with synthetic data.</p></td></tr>'
 + block(f'<h2 style="margin:0 0 6px;font:800 22px/28px Arial;color:{INK}">Six projects you build</h2><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows(PROJ)}</table>', "#f8fafc")
 + f'<tr><td class="p" style="padding:26px 38px;background:{NAVY};font:15px/24px Arial;color:#dbeafe"><strong style="color:#22d3ee;letter-spacing:1.4px;font-size:13px">TARGET PATHWAYS</strong><br>{e(PATHS)}.<br><span style="font-size:12px;color:#94a3b8">Pathways are directions, not job promises.</span></td></tr>'
 + block('<div style="height:20px"></div>' + btn("See the program and apply", LP, CY))))
E.append(("3-admission", "Admissions: Adobe MarTech career accelerator, Rs 60,000", "Live online, six phases, projects and interview preparation. Ask me anything before you decide.", "ADMISSIONS OPEN", "Ready to start? Here is exactly what you get.", 7,
 f'<p style="margin:0 0 18px;font:17px/27px Arial,Helvetica,sans-serif;color:#40516a">Hi {{{{FirstName}}}},<br><br>A clear summary, so you can decide without guesswork.</p></td></tr>'
 + block(f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows([("Live online classes", "with recordings on the learner app"), ("Six learning phases", "AEP, RTCDP, AJO, CJA, Web SDK, Agentic AI"), ("Simulators and an enterprise-style project", ""), ("Mentor doubt resolution and interview preparation", ""), ("Program fee", chr(8377) + "60,000; corporate pricing on request")])}</table>', "#f8fafc")
 + block(f'<p style="margin:0 0 18px;font:14px/22px Arial;color:{MUT}"><strong>Honest note:</strong> your results depend on your participation and practice. There is no job, salary or certification guarantee. Prefer to talk first? WhatsApp <a href="{WA}" style="color:#0069a6">+91 82968 93895</a>.</p>' + btn("Apply or ask a question", LP, "#ff1744"))))
rowsmd = ["# Career accelerator learner campaign (3 emails)", "Audience: people who enquired, attended a demo or opted in. Not for scraped or purchased lists. Check deliverability.md first.", "",
          "| Email | Send | Subject | Goal | CTA |", "|---|---|---|---|---|"]
for fn, subj, pre, kick, h1, day, body in E:
    open(os.path.join(OUT, fn + ".html"), "w", encoding="utf-8").write(wrap(pre, kick, h1, body))
    rowsmd.append(f"| {fn} | day {day} | {subj.replace('Rs ', chr(8377))} | {pre} | {'Drive resources' if day == 0 else 'Landing page (utm_content=career)'} |")
rowsmd += ["", "Rules: send 1 only to opted-in learners; skip anyone who replied, enrolled or unsubscribed before email 2 and 3; pause below 1% reply or click after 200 sends; weekly review of opens, clicks, replies, enrolments, unsubscribes.",
           "Removed from your original template: '60+ learning hours' and '10+ projects' (not stated on the website; add back only if true) and the misspelled reply address (now " + MAIL + ").",
           "Subject lines are in the HTML <title> and above; set A/B variants in your ESP."]
open(os.path.join(OUT, "campaign.md"), "w", encoding="utf-8").write("\n".join(rowsmd) + "\n")
print("ok", len(E))
