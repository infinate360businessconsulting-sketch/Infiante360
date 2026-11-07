"""MarTech SME Accelerator 6-day demo series + WhatsApp community pages. Data: content/sme-accelerator.json."""
import json, os, datetime, html
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(_ROOT, "content", "sme-accelerator.json"), encoding="utf-8"))
e = html.escape
PATH = "lp/martech-sme-accelerator.html"
COMM_PATH = "academy/community.html"
CXO_MAIN = "academy/programs/executive-architecture-leadership.html"
first, last = (datetime.date.fromisoformat(D["days"][0]["date"]), datetime.date.fromisoformat(D["days"][-1]["date"]))
SPAN = f'{first.day}–{last.day} {last.strftime("%B")}'
fmt = lambda x: datetime.date.fromisoformat(x["date"]).strftime("%A %-d %B")
days_json = e(json.dumps([{"n": x["n"], "start": f'{x["date"]}T{D["start_hour"]}:00+05:30', "end": f'{x["date"]}T{D["end_hour"]}:00+05:30'} for x in D["days"]]))
LNK = 'rel="noopener" target="_blank"'

SCRIPT = """<script>(function(){try{var b=document.getElementById("sme-status");var d=JSON.parse(b.getAttribute("data-days")),n=Date.now();
var s=d.map(function(x){return[new Date(x.start).getTime(),new Date(x.end).getTime()]});var m="";
if(n<s[0][0]){var k=Math.ceil((s[0][0]-n)/86400000);m="Starts in "+k+(k===1?" day":" days")+". Complete the three registration steps before Day 1."}
else if(n<=s[s.length-1][1]){var c=0;for(var i=0;i<s.length;i++){if(n<=s[i][1]){c=i;break}}m=(n>=s[c][0]&&n<=s[c][1])?"Day "+(c+1)+" is live now.":"The series is in progress. Next session: Day "+(c+1)+"."}
else{m="This series has ended. Join the community to hear about the next run."}
b.textContent=m}catch(x){}})();</script>"""


def ics():
    desc = f'Infinite360 MarTech SME Accelerator live demo. Classroom: {D["classroom_url"]} Community: {D["community_url"]} Questions: +91 82968 93895.'
    z = lambda t: t.strftime("%Y%m%dT%H%M%SZ")
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Infinite360//SME Accelerator//EN", "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:MarTech SME Accelerator (Infinite360)"]
    for x in D["days"]:
        st = datetime.datetime.fromisoformat(f'{x["date"]}T{D["start_hour"]}:00+05:30').astimezone(datetime.timezone.utc)
        en = datetime.datetime.fromisoformat(f'{x["date"]}T{D["end_hour"]}:00+05:30').astimezone(datetime.timezone.utc)
        out += ["BEGIN:VEVENT", f'UID:sme-accelerator-day{x["n"]}-{x["date"]}@infiante360techacademy.com', "DTSTAMP:20261107T000000Z", f"DTSTART:{z(st)}", f"DTEND:{z(en)}",
                f'SUMMARY:MarTech SME Accelerator Day {x["n"]}: {x["title"].replace(",", " ")}', "DESCRIPTION:" + desc.replace(",", " "), "LOCATION:" + D["classroom_url"],
                "BEGIN:VALARM", "TRIGGER:-PT15M", "ACTION:DISPLAY", "DESCRIPTION:Session starts in 15 minutes", "END:VALARM", "END:VEVENT"]
    return "\r\n".join(out + ["END:VCALENDAR", ""])


steps = f'''<ol class="steps">
<li><strong>Complete the registration form.</strong> It is mandatory. <a href="{e(D["register_url"])}" {LNK}>Open the registration form</a>.</li>
<li><strong>Register on the Infinite360 learning platform.</strong> <a href="{e(D["platform_url"])}" {LNK}>techacademy.infinate360.in</a>.</li>
<li><strong>Join the MarTech SME WhatsApp Community.</strong> <a href="{e(D["community_url"])}" {LNK}>Join on WhatsApp</a>, then pick the specialist groups that fit you.</li>
<li><strong>Add the six sessions to your calendar.</strong> <a href="../assets/sme-accelerator.ics" download>Download the calendar file (.ics)</a>.</li></ol>
<p class="small muted">Joining the WhatsApp community alone does not confirm your registration. The form confirms registration, WhatsApp gives community access and the platform gives learning access.</p>'''

groups_html = '<div class="grid-3">' + "".join(f'<div class="card"><h3>{g[0]} {e(g[1])}</h3><p>{e(g[2])}</p></div>' for g in D["groups"]) + "</div>"

PAGES_SME = [
 dict(path=PATH, nav="6-day MarTech SME Accelerator",
  title=f"MarTech SME Accelerator: 6-Day Live Demo, {SPAN} Nov",
  desc=f"Six live evenings on AEP, Real-Time CDP, AJO, CJA, architecture and Agentic AI: {SPAN} {last.year}, 10-11 PM IST. Register and join the community.",
  h1="MarTech SME Accelerator: 6-day live demo series", kicker=f"Live online · {SPAN} {last.year} · {D['time_label']}",
  keywords=["martech sme accelerator", "adobe experience platform live demo", "aep demo series india", "martech community whatsapp", "agentic ai martech demo"],
  answer=(f"The MarTech SME Accelerator is a six-day live online demo series from {SPAN} {last.year}, 10:00 to 11:00 PM IST each night. It covers Adobe Experience Platform, XDM, identity resolution, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, enterprise architecture and Agentic AI through practical demonstrations. Registration is mandatory."),
  schema="WebPage", landing=True, interest="sme", bands=True, hero_cta=("Register now", D["register_url"]),
  sections=[
   ("Register in four steps", f'<p id="sme-status" role="status" aria-live="polite" class="small" style="font-weight:600" data-days="{days_json}">Complete the registration steps before Day 1.</p>' + steps +
    f'<p class="cta-row" style="margin-top:14px"><a class="btn btn-primary" href="{e(D["register_url"])}" {LNK}>Register now &rarr;</a><a class="btn btn-ghost" href="{e(D["community_url"])}" {LNK}>Join the community</a><a class="btn btn-ghost" href="{e(D["classroom_url"])}" {LNK}>Live classroom</a></p>', "plain", "Registration"),
   ("Six-day calendar", '<div class="grid-3">' + "".join(f'<div class="card"><span class="tag">Day {x["n"]} · {e(fmt(x))}</span><h3>{e(x["title"])}</h3><p class="small muted">{e(D["time_label"])}</p></div>' for x in D["days"]) + '</div><p class="cta-row" style="margin-top:14px"><a class="btn btn-ghost" href="../assets/sme-accelerator.ics" download>Add all six to calendar (.ics)</a></p>', "alt", "Agenda"),
   ("What you will see", '<ul class="checklist"><li>Practical platform demonstrations</li><li>Enterprise architecture discussions</li><li>Real-world implementation scenarios</li><li>AEP, RTCDP, AJO and CJA working together</li><li>Data engineering and identity resolution</li><li>Agentic AI and MCP applications</li><li>SME, architect and consultant career preparation</li></ul>', "plain", "Content"),
   ("Seven specialist WhatsApp groups", '<p>Inside the community you can join the groups that match your interests. See the <a href="../academy/community.html">community page</a> for the full list and house rules.</p>' + groups_html, "alt", "Community"),
   ("Looking for the executive program?", f'<p>Senior leaders have a separate program and community. See <a href="../{CXO_MAIN}">CXO Hive</a>.</p><p class="small muted">Infinite360 is independent and not affiliated with or endorsed by Adobe. A demo is not a certification, and jobs, salaries and certifications are not guaranteed.</p>', "plain", "Executives"),
   ("Missed my call? Talk to us", '<p>If you missed our call or want to understand the program before registering, send the form below or message <a href="https://wa.me/918296893895" rel="noopener" target="_blank">+91 82968 93895</a> with the word CALL and a convenient time.</p><div class="form-card" id="enquire-form">@@LP_FORM@@</div>' + SCRIPT, "plain", "Contact us"),
  ],
  faqs=[("When is the series?", f"{first.strftime('%A %-d %B')} to {last.strftime('%A %-d %B %Y')}, 10:00 PM to 11:00 PM IST each night, live online."),
        ("Is registration required?", "Yes. Complete the registration form, register on the learning platform and join the WhatsApp community before the first session."),
        ("Does joining WhatsApp count as registration?", "No. The form confirms registration; WhatsApp is for community access."),
        ("Is there a job or certification guarantee?", "No. The sessions show the work and how we teach; outcomes depend on your own practice."),
        ("Is there a separate program for executives?", "Yes. CXO Hive has its own program, community and enquiry route.")],
  related=[CXO_MAIN, "academy/workshops.html"]),
 dict(path=COMM_PATH, nav="Learning communities",
  title="Infinite360 Learning Communities: MarTech SME and CXO Hive",
  desc="Join the Infinite360 MarTech SME community with seven specialist WhatsApp groups, or the separate CXO Hive community for senior leaders.",
  h1="Infinite360 learning communities", kicker="Academy · Community",
  keywords=["martech whatsapp community", "adobe experience platform community india", "cxo hive community"],
  answer="Infinite360 runs two separate WhatsApp communities: the MarTech SME Accelerator community with seven specialist groups for practitioners, and CXO Hive for C-level and senior leaders. Each has its own purpose and joining route.",
  schema="WebPage", landing=False, interest="sme",
  sections=[
   ("MarTech SME Accelerator community", f'<p>For developers, data engineers, consultants, architects and technical leads. Focus: AEP, Real-Time CDP, AJO, CJA, data engineering, Agentic AI, labs and careers.</p><p class="cta-row"><a class="btn btn-primary" href="{e(D["community_url"])}" {LNK}>Join the SME community</a><a class="btn btn-ghost" href="../{PATH}">6-day demo series</a></p>' + groups_html, "plain", "SME community"),
   ("Group guidelines", '<ul class="checklist"><li>Announcements is admin-only; schedules, links and recordings are posted there.</li><li>Groups 2 to 6 are open for technical questions and discussion.</li><li>The careers group is for career conversations and relevant opportunities only.</li><li>No spam, no confidential client data and no unsolicited promotion.</li></ul>', "alt", "Guidelines"),
   ("CXO Hive community", f'<p>A separate community for C-level and senior leaders: enterprise MarTech strategy, architecture, AI governance, operating models and business value. It is separate from the SME community and from the paid program.</p><p class="cta-row"><a class="btn btn-primary" href="{e(D["cxo_community_url"])}" {LNK}>Join CXO Hive community</a><a class="btn btn-ghost" href="../{CXO_MAIN}">CXO Hive program</a></p>', "plain", "Executives"),
   ("Follow Infinite360", f'<p><a href="{e(D["linkedin_url"])}" {LNK}>LinkedIn</a> · <a href="{e(D["youtube_url"])}" {LNK}>YouTube demo sessions</a> · <a href="https://wa.me/918296893895" {LNK}>WhatsApp +91 82968 93895</a></p><p class="small muted">Infinite360 is independent and not affiliated with or endorsed by Adobe.</p>', "alt", "Links"),
  ],
  faqs=[("Which community should I join?", "Practitioners and career switchers: the SME community. C-level and senior leaders: CXO Hive."),
        ("Is the community free?", "Joining the WhatsApp community is by invite link. Paid programs are priced on their own pages.")],
  related=[PATH, CXO_MAIN]),
]
