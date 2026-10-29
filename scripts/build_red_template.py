#!/usr/bin/env python3
"""Red-theme resource email (ESP-ready). Output: docs/outreach/email-html/red-resources.html. Merge tags: {{FirstName}} {{UnsubscribeURL}} {{postal_address}}."""
import os, html, urllib.parse
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(R, "docs", "outreach", "email-html", "red-resources.html")
S = "https://infiante360techacademy.com/"
ACAD = "https://techacademy.infinate360.in/"
DRIVE = "https://drive.google.com/file/d/11hkOjfB7a8z7V8ZJJVOyX9mSSlUxvMxQ/view?usp=sharing"
IMG = "https://appbox12.mail250.com/uploadimages/infinate360businessconsulting/image/"
LOGO, HERO, CARD = IMG + "81349-Infinite360-Tech-Academy-Logo_youtube-.png", IMG + "88154-Adobe-Resized.png", IMG + "71991-Adobe-Infinite360-Business-Card-Mockup.png"
WA, MAIL = "https://wa.me/918296893895", "infinate360businessconsulting@gmail.com"
RED, DRED, DEEP, TINT, INK, MUT = "#D91E36", "#B3122A", "#1A0A0F", "#FFF1F2", "#1F1315", "#5B4A4D"
e = html.escape
def u(url, c):  # UTM-tag every link
    sep = "&" if "?" in url else "?"
    return e(f"{url}{sep}utm_source=email&utm_medium=campaign&utm_campaign=martech_resources&utm_content={c}")

def button(label, url, c, bg=RED, fg="#FFFFFF"):
    href = u(url, c)
    return (f'<!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{href}" style="height:52px;v-text-anchor:middle;width:340px" arcsize="20%" stroke="f" fillcolor="{bg}"><w:anchorlock/><center style="color:{fg};font-family:Arial,sans-serif;font-size:16px;font-weight:bold">{e(label)} &rarr;</center></v:roundrect><![endif]-->'
            f'<!--[if !mso]><!--><a href="{href}" target="_blank" style="display:inline-block;background:{bg};color:{fg};font:800 16px/20px Arial,Helvetica,sans-serif;text-decoration:none;padding:16px 30px;border-radius:10px;box-shadow:0 6px 16px rgba(217,30,54,.28)">{e(label)} &rarr;</a><!--<![endif]-->')

RES = [("The AEP guide", "Schemas to activation, step by step.", S + "learn/index.html", "guide-aep"),
       ("AEP vs Real-Time CDP", "What is the difference?", S + "guides/aep-vs-real-time-cdp.html", "guide-aep-vs-rtcdp"),
       ("CJA vs Adobe Analytics", "Use cases and trade-offs.", S + "guides/cja-vs-adobe-analytics.html", "guide-cja-vs-aa"),
       ("What is MCP?", "Safe agentic AI for enterprise MarTech.", S + "guides/what-is-mcp.html", "guide-mcp"),
       ("Marketo Engage and AEP", "Lead lifecycle, scoring and integration.", S + "guides/marketo-engage-aep.html", "guide-marketo"),
       ("Free learning resources", "Guides, roles explained and more.", S + "academy/free-resources.html", "free-resources")]
PATHS = [("Career accelerator", "Live online, six phases, projects and interview prep. ₹60,000.", S + "lp/career-accelerator-admission.html", "career", "FOR PROFESSIONALS"),
         ("CXO Hive", "10-week live program for C-level leaders. ₹1,30,000.", S + "academy/programs/executive-architecture-leadership.html", "cxo", "FOR C-LEVEL"),
         ("Corporate training", "Role-based tracks, labs and assessments for teams.", S + "training/corporate-training.html", "corporate", "FOR TEAMS"),
         ("Architecture review", "Prioritised findings and a 30/60/90-day plan.", S + "lp/aep-architecture-review.html", "review", "FOR ENTERPRISES")]
LIB = ["Adobe Experience Platform", "XDM and data modeling", "Identity resolution and Customer 360", "Real-Time CDP", "Adobe Journey Optimizer", "Customer Journey Analytics", "Adobe Analytics", "Adobe Web SDK", "Agentic AI and MCP"]

def res_cell(t, d, url, c):
    return (f'<td valign="top" width="50%" style="padding:6px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="border:1px solid #F3C9CE;border-radius:10px;background:#fff"><tr><td style="padding:14px 16px">'
            f'<a href="{u(url, c)}" target="_blank" style="font:800 15px/20px Arial,Helvetica,sans-serif;color:{DRED};text-decoration:none">{e(t)} &rarr;</a><br><span style="font:13px/19px Arial,Helvetica,sans-serif;color:{MUT}">{e(d)}</span></td></tr></table></td>')
res_rows = "".join(f"<tr>{res_cell(*RES[i])}{res_cell(*RES[i+1])}</tr>" for i in range(0, len(RES), 2))
path_rows = "".join(f'<tr><td style="padding:0 0 10px"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#fff;border-left:4px solid {RED};border-radius:8px"><tr><td style="padding:14px 18px">'
                    f'<span style="font:800 11px/16px Arial;letter-spacing:1.4px;color:{RED}">{k}</span><br><a href="{u(url, c)}" target="_blank" style="font:800 17px/24px Arial,Helvetica,sans-serif;color:{DEEP};text-decoration:none">{e(t)} &rarr;</a><br><span style="font:13px/19px Arial;color:{MUT}">{e(d)}</span></td></tr></table></td></tr>' for t, d, url, c, k in PATHS)
lib = "".join(f'<tr><td style="padding:6px 0;font:14px/20px Arial,Helvetica,sans-serif;color:{INK}"><span style="color:{RED};font-weight:800">{i:02d}</span>&nbsp;&nbsp;{e(x)}</td></tr>' for i, x in enumerate(LIB, 1))

H = f"""<!doctype html>
<html lang="en" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light only"><meta name="x-apple-disable-message-reformatting">
<title>Your complete Adobe MarTech resource library | Infinite360 Tech Academy</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>body{{margin:0;padding:0}}img{{border:0;display:block}}a{{color:{DRED}}}@media only screen and (max-width:640px){{.w{{width:100%!important}}.p{{padding:24px 18px!important}}.h{{font-size:28px!important;line-height:33px!important}}.c{{display:block!important;width:100%!important}}}}</style></head>
<body style="margin:0;padding:0;background:#FBEEF0">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:#FBEEF0">Course resources for AEP, XDM, identity, RTCDP, AJO, CJA, Web SDK and Agentic AI, plus free guides.&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#FBEEF0"><tr><td align="center" style="padding:24px 10px">
<table role="presentation" class="w" width="680" cellpadding="0" cellspacing="0" border="0" style="width:680px;max-width:100%;background:#fff;border-radius:18px;overflow:hidden">
<tr><td align="center" bgcolor="{DEEP}" style="padding:22px 28px;border-bottom:4px solid {RED}"><a href="{u(ACAD, 'logo')}" target="_blank"><img src="{LOGO}" alt="Infinite360 Tech Academy" width="230" style="margin:0 auto;max-width:100%"></a></td></tr>
<tr><td bgcolor="{DEEP}"><a href="{u(ACAD, 'hero')}" target="_blank"><img src="{HERO}" alt="Infinite360 Adobe MarTech and Agentic AI Career Accelerator" width="680" style="width:100%;max-width:680px"></a></td></tr>
<tr><td class="p" style="padding:36px 38px 10px"><p style="margin:0 0 8px;font:800 13px/18px Arial;letter-spacing:1.6px;color:{RED}">INFINITE360 TECH ACADEMY</p>
<h1 class="h" style="margin:0 0 16px;font:800 34px/39px Arial,Helvetica,sans-serif;color:{DEEP}">Your complete Adobe MarTech learning path starts here.</h1>
<p style="margin:0;font:17px/27px Arial,Helvetica,sans-serif;color:{MUT}">Hi {{{{FirstName}}}},<br><br>If you want to strengthen your Adobe MarTech skills, or move from a technology, data, analytics, cloud or consulting background into enterprise MarTech, we have put the learning path in one place.</p></td></tr>
<tr><td align="center" class="p" style="padding:18px 38px 12px">{button("Access the complete course resources", DRIVE, "drive-primary")}<p style="margin:12px 0 0;font:12px/18px Arial;color:#8A787B">Course and architecture resources &bull; opens online</p></td></tr>
<tr><td class="p" style="padding:20px 38px;background:{TINT}"><h2 style="margin:0 0 6px;font:800 24px/30px Arial;color:{DEEP}">What the library covers</h2><p style="margin:0 0 12px;font:14px/22px Arial;color:{MUT}">Nine focused learning paths across customer data, analytics, orchestration and agentic AI, taught as Learn &rarr; Build &rarr; Implement &rarr; Deploy.</p>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{lib}</table></td></tr>
<tr><td class="p" style="padding:30px 32px 14px"><h2 style="margin:0 0 4px 6px;font:800 24px/30px Arial;color:{DEEP}">Free guides to read first</h2><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{res_rows}</table></td></tr>
<tr><td class="p" style="padding:24px 38px;background:{DEEP}"><p style="margin:0 0 8px;font:800 13px/18px Arial;letter-spacing:1.4px;color:#FF8A98">CAREER ACCELERATION</p><h2 style="margin:0 0 12px;font:800 27px/33px Arial;color:#fff">Don&#39;t restart your career. Redirect it.</h2>
<p style="margin:0;font:15px/25px Arial;color:#F6D3D8">Use your existing engineering, data, analytics, cloud, consulting or business experience as the foundation for Adobe MarTech capability. Six learning phases, simulators and an enterprise-style project, with interview preparation. Outcomes depend on your participation; no job, salary or certification is guaranteed.</p></td></tr>
<tr><td class="p" style="padding:30px 38px 10px"><h2 style="margin:0 0 14px;font:800 24px/30px Arial;color:{DEEP}">Choose your path</h2><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{path_rows}</table></td></tr>
<tr><td align="center" class="p" style="padding:20px 38px 30px;background:{TINT}"><h2 style="margin:0 0 10px;font:800 26px/32px Arial;color:{DEEP}">Ready to build your MarTech skill stack?</h2><p style="margin:0 0 20px;font:15px/24px Arial;color:{MUT}">Start with the resources, pick a track, or ask me anything on WhatsApp.</p>
{button("Get the course resources", DRIVE, "drive-final")}<p style="margin:16px 0 0;font:14px/22px Arial"><a href="{u(ACAD, 'explore')}" target="_blank" style="color:{DRED};font-weight:bold">Explore Infinite360 Tech Academy</a> &nbsp;|&nbsp; <a href="{e(WA)}" target="_blank" style="color:{DRED};font-weight:bold">WhatsApp +91 82968 93895</a></p>
<a href="{u(ACAD, 'card')}" target="_blank"><img src="{CARD}" alt="Infinite360 contact card" width="560" style="width:100%;max-width:560px;margin:20px auto 0;border-radius:10px"></a></td></tr>
<tr><td align="center" bgcolor="{DEEP}" style="padding:26px 30px;font:13px/20px Arial,Helvetica,sans-serif;color:#E8C4C9;border-top:4px solid {RED}"><img src="{LOGO}" alt="Infinite360 Tech Academy" width="180" style="margin:0 auto 14px"><strong style="color:#fff;font-size:14px">Infinite360 Tech Academy</strong><br>Practical Adobe MarTech &bull; Customer Data &bull; Analytics &bull; Agentic AI &bull; Enterprise Transformation<br>
<a href="{e(WA)}" style="color:#FF8A98;text-decoration:none">+91 82968 93895</a> &nbsp;|&nbsp; <a href="mailto:{MAIL}" style="color:#FF8A98;text-decoration:none">{MAIL}</a>
<p style="margin:14px 0 0;font-size:11px;line-height:17px;color:#B79DA1">Training outcomes depend on participation and practice; no job, salary, certification or business outcome is guaranteed. Infinite360 is independent and not affiliated with or endorsed by Adobe. Adobe product names are trademarks of Adobe.<br>
You are receiving this because you requested or are being contacted about Infinite360 MarTech learning resources. <a href="{{{{UnsubscribeURL}}}}" style="color:#D9B8BD;text-decoration:underline">Unsubscribe</a> or reply STOP.<br>{{{{postal_address}}}}</p></td></tr>
</table></td></tr></table></body></html>
"""
open(OUT, "w", encoding="utf-8").write(H); print(len(H), "bytes ->", OUT)
