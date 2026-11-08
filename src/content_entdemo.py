"""Enterprise MarTech demo registration landing page (Meta ads destination). Links come from content/sme-accelerator.json."""
import json, os, html
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = json.load(open(os.path.join(_ROOT, "content", "sme-accelerator.json"), encoding="utf-8"))
e = html.escape
PATH = "lp/enterprise-martech-demo.html"
REG = S["register_url"]
LNK = 'rel="noopener" target="_blank"'
WA = "https://wa.me/918296893895"

topics = [
 ("Adobe Experience Platform", "XDM schema design, datasets, ingestion, Identity Service and Real-Time Customer Profile."),
 ("Real-Time CDP and Customer 360", "Unified profiles, identity resolution, segmentation, governance and audience activation."),
 ("Journey Optimizer and CJA", "Journey orchestration, decisioning, cross-channel messaging, analytics and measurement."),
 ("Adobe Analytics and Web SDK", "Event design, data collection, validation and the path into AEP."),
 ("Enterprise MarTech architecture", "Reference architecture, integration patterns, migration and delivery risk."),
 ("Agentic AI and MCP", "Governed AI agents, MCP tools and intelligent marketing workflows with human approval points."),
]
cases = [
 ("Banking and insurance", "Identity resolution and governed customer profiles that support personalization within consent rules."),
 ("Retail and e-commerce", "Real-time audiences and journey orchestration for browse, cart and loyalty moments."),
 ("Telecommunications", "Retention journeys and cross-channel measurement with Customer Journey Analytics."),
 ("Healthcare and life sciences", "Governed customer data and responsible personalization with strict consent handling."),
 ("Technology and SaaS", "Enterprise data architecture, CDP design and AI integration across product and marketing data."),
 ("Systems integrators", "Specialist Adobe MarTech capability for delivery teams and practice leads."),
]
audience = ["Chief Digital, Technology, Information and Marketing Officers", "VPs, heads and directors of MarTech, data and CDP", "Enterprise and solution architects", "Digital transformation and delivery leaders at enterprises and systems integrators", "Enterprise L&D and capability leaders"]

PAGES_ENTDEMO = [dict(
 path=PATH, nav="Enterprise MarTech demo",
 title="Exclusive Live Enterprise MarTech & Agentic AI Demo | Infinite360",
 desc="Register for a live demo of Adobe Experience Platform, Real-Time CDP, Journey Optimizer, CJA and Agentic AI architecture, led by Pavan Babu Gandla.",
 h1="See the Future of Enterprise MarTech and Agentic AI",
 kicker="Exclusive live demo · Infinite360 Business Consulting",
 keywords=["enterprise martech demo", "adobe experience platform demo", "real-time cdp demo", "agentic ai martech", "adobe experience cloud consulting"],
 answer="Join Infinite360 for an exclusive live demonstration of Adobe Experience Cloud, customer data platforms and Agentic AI architecture, presented by Pavan Babu Gandla. The session covers AEP, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, identity resolution and governed AI workflows. Register to reserve your place.",
 schema="WebPage", landing=True, interest="entdemo", bands=True, hero_cta=("Register for the exclusive live demo", REG),
 sections=[
  ("Reserve your demo session", f'''<p>Are you transforming your enterprise customer-data and MarTech ecosystem? Explore enterprise architecture, identity resolution, personalization, customer journeys and intelligent AI-driven marketing workflows, and see practical approaches to common enterprise MarTech challenges.</p>
<p class="cta-row"><a class="btn btn-primary" href="{e(REG)}" {LNK}>Register for the exclusive live demo &rarr;</a><a class="btn btn-ghost" href="#enquire-form">Book an enterprise architecture discussion</a><a class="btn btn-ghost" href="../assets/sme-accelerator.ics" download>Add sessions to calendar (.ics)</a></p>
<p class="small muted">Live sessions run 10:00 to 11:00 PM IST. The current live series is 10 to 15 November 2026; see the <a href="martech-sme-accelerator.html">six-day schedule</a>. Join details are confirmed after registration.</p>''', "plain", "Register"),
  ("What the demo covers", '<div class="grid-3">' + "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in topics) + '</div>', "alt", "Topics"),
  ("Enterprise scenarios", '<p>These are illustrative scenarios used in the demo, not client case studies.</p><div class="grid-3">' + "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in cases) + '</div>', "plain", "Use cases"),
  ("Who should attend", '<ul class="checklist">' + "".join(f"<li>{e(x)}</li>" for x in audience) + '</ul><p class="small muted">Organisations typically with an existing or planned Adobe Experience Cloud investment or a customer-data modernisation roadmap.</p>', "alt", "Audience"),
  ("Your presenter", f'''<div class="card"><h3>Pavan Babu Gandla</h3><p>Digital transformation and enterprise MarTech leader with 15+ years of experience, specialising in Adobe Experience Cloud, customer data platforms, analytics, architecture and Agentic AI. Founder of Infinite360, an architecture-led consulting and capability-building firm.</p>
<p><a href="https://www.martechconsultant.tech/Pavan.html" {LNK}>Portfolio</a> · <a href="https://linkedin.com/in/pavanbabu1" {LNK}>LinkedIn</a></p></div>
<p class="small muted">Infinite360 is independent and not affiliated with or endorsed by Adobe. No results or outcomes are guaranteed.</p>''', "plain", "Presenter"),
  ("Join the community and next steps", f'<ol class="steps"><li><a href="{e(REG)}" {LNK}>Complete the registration form</a> (mandatory).</li><li><a href="{e(S["platform_url"])}" {LNK}>Register on the learning platform</a>.</li><li><a href="{e(S["community_url"])}" {LNK}>Join the WhatsApp community</a>.</li><li>Add the sessions to your calendar.</li></ol><p>Senior leaders can also explore <a href="../academy/programs/executive-architecture-leadership.html">CXO Hive</a>. Delivery partners and systems integrators can use the form below to start a partnership conversation.</p>', "alt", "Next steps"),
  ("Book an enterprise architecture discussion", f'<p>Prefer a conversation first? Send the form below with your company, role, Adobe products in use and main challenge, or message <a href="{WA}" {LNK}>+91 82968 93895</a>.</p><div class="form-card" id="enquire-form">@@LP_FORM@@</div><p class="small muted">Privacy and consent: we use your details only to respond to your enquiry and to send demo information you asked for. We contact you by email, phone or WhatsApp only where you have agreed, and you can opt out at any time. See the <a href="../privacy-policy.html">privacy policy</a>.</p>', "plain", "Contact us"),
 ],
 faqs=[("Who is this demo for?", "Enterprise and mid-market leaders, architects and delivery teams working on Adobe Experience Cloud, customer data or AI-enabled MarTech."),
       ("Is registration required?", "Yes. Complete the registration form to receive session details."),
       ("Will you share the presentation?", "Approved resources are shared after the session to registered attendees."),
       ("Is this a sales pitch?", "No. It is a technical demonstration. You can book a separate architecture discussion afterwards if useful."),
       ("Does this guarantee results?", "No. The demo shows approaches and architecture; outcomes depend on your context and implementation.")],
 related=["lp/martech-sme-accelerator.html", "academy/programs/executive-architecture-leadership.html"],
)]
