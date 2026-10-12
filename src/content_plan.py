"""Lesson/webinar topic library (planned topics) and press page. Nothing here claims results or videos that do not exist."""
import html as _h
from content_cases import pills, WHATSAPP_MSG, REGISTER
e = _h.escape
EL = "https://experienceleague.adobe.com/en/docs"
EMAIL = "infinate360businessconsulting@gmail.com"

T = {  # section -> rows (title, keyword, format, audience, leads_to)
"AEP data, schemas and identity": [
("What is Adobe Experience Platform? Explained in 3 minutes", "what is adobe experience platform", "3-min", "Beginners", "AEP Launchpad"),
("AEP vs Real-Time CDP: the difference in 3 minutes", "aep vs real-time cdp", "3-min", "Beginners, buyers", "Foundations batch"),
("XDM schemas explained: classes, field groups, data types", "xdm schema explained", "3-min", "Beginners", "Friday workshop"),
("How to design an XDM schema for a retail customer", "xdm schema design", "45-min", "Practitioners", "Career Accelerator"),
("Datasets, batches and ingestion in AEP: what happens to your data", "aep data ingestion", "3-min", "Beginners", "AEP Launchpad"),
("Batch vs streaming ingestion in AEP: which to choose", "aep streaming vs batch ingestion", "3-min", "Practitioners", "Foundation + Advanced"),
("How the AEP identity graph works", "aep identity graph", "3-min", "Practitioners", "Friday workshop"),
("ECID, hashed email and CRM IDs: choosing identity namespaces", "aep identity namespace", "3-min", "Practitioners", "Foundation + Advanced"),
("Merge policies in Real-Time Customer Profile", "aep merge policy", "3-min", "Practitioners", "Friday workshop"),
("Record schema vs XDM Individual Profile: when to use each", "xdm individual profile vs record", "3-min", "Practitioners", "Foundation + Advanced"),
],
"Real-Time CDP and Journey Optimizer": [
("Real-Time CDP audiences in 3 minutes", "real-time cdp audience", "3-min", "Beginners", "Friday workshop"),
("RTCDP destinations and activation: a walkthrough", "rtcdp destinations activation", "45-min", "Practitioners", "Career Accelerator"),
("Edge, streaming and batch segmentation: what each is for", "aep segmentation types", "3-min", "Practitioners", "Foundation + Advanced"),
("Suppression audiences: stop wasting ad spend on buyers", "rtcdp suppression audience", "3-min", "Marketers", "Live Customised"),
("Adobe Journey Optimizer: your first journey in 3 minutes", "adobe journey optimizer tutorial", "3-min", "Beginners", "Friday workshop"),
("AJO campaigns vs journeys: which to use", "ajo campaigns vs journeys", "3-min", "Practitioners", "Foundation + Advanced"),
("AJO implementation best practices for enterprises", "ajo implementation best practices", "45-min", "Leaders, architects", "CXO Hive"),
("Abandoned cart journey in AJO: trigger to measurement", "abandoned cart journey ajo", "45-min", "Practitioners", "Career Accelerator"),
("AJO event triggers and conditions explained", "ajo event trigger", "3-min", "Beginners", "Friday workshop"),
("Consent and frequency caps in AJO journeys", "ajo consent frequency capping", "3-min", "Practitioners", "Live Customised"),
],
"CJA, Adobe Analytics, Web SDK and governance": [
("Customer Journey Analytics in 3 minutes", "what is customer journey analytics", "3-min", "Beginners", "Foundations batch"),
("CJA vs Adobe Analytics: use cases and trade-offs", "cja vs adobe analytics", "45-min", "Analysts", "Career Accelerator"),
("CJA connections, datasets and data views explained", "cja data view", "3-min", "Practitioners", "Friday workshop"),
("Backfill months from AEP to CJA: what to expect", "cja backfill", "3-min", "Practitioners", "Foundation + Advanced"),
("Adobe Analytics eVars vs props vs events", "adobe analytics evars vs props", "3-min", "Beginners", "Single-tool course"),
("Adobe Analytics source connector in AEP: set-up checklist", "adobe analytics source connector aep", "3-min", "Practitioners", "Foundation + Advanced"),
("Adobe Web SDK in 3 minutes: how events reach AEP", "adobe web sdk", "3-min", "Beginners", "Friday workshop"),
("Web SDK troubleshooting: five errors and fixes", "adobe web sdk troubleshooting", "3-min", "Practitioners", "Single-tool course"),
("Datastreams and the Edge Network explained", "adobe datastream edge network", "3-min", "Practitioners", "Foundation + Advanced"),
("Migrating from AppMeasurement to Web SDK", "appmeasurement to web sdk migration", "45-min", "Practitioners", "Live Customised"),
("Data elements best practices in Adobe Tags", "adobe tags data elements", "3-min", "Practitioners", "Single-tool course"),
("ECID in Adobe Tags: set-up and validation", "ecid data element adobe tags", "3-min", "Practitioners", "Single-tool course"),
("Consent in AEP: OneTrust and the consent standard", "onetrust aep consent", "3-min", "Practitioners", "Live Customised"),
("AEP data governance: labels, policies and enforcement", "aep data governance", "45-min", "Leaders, architects", "CXO Hive"),
],
"Agentic AI and MCP": [
("What is MCP? Explained for MarTech teams", "what is mcp", "3-min", "All", "Agentic AI course"),
("Agentic AI in enterprise MarTech: use cases and limits", "agentic ai martech", "45-min", "Leaders", "CXO Hive"),
("Build a safe AI agent with one approved tool", "build ai agent mcp", "90-min", "Developers", "Career Accelerator"),
],
"Career pathways and interview preparation": [
("How to move from software developer to AEP developer", "software developer to aep developer", "45-min", "Developers", "Career Accelerator"),
("Data engineer to customer data engineer: the AEP path", "data engineer aep career", "45-min", "Data engineers", "Career Accelerator"),
("Data analyst to CJA analyst: a skills map", "cja analyst career", "45-min", "Analysts", "Career Accelerator"),
("QA tester to MarTech QA specialist: what to learn", "martech qa specialist", "3-min", "QA", "Friday workshop"),
("Fresher's roadmap to an Adobe MarTech career", "adobe martech career roadmap", "45-min", "Freshers", "AEP Launchpad"),
("Ten AEP interview questions and how to answer them", "aep interview questions", "45-min", "Job seekers", "Career Accelerator"),
("AEP architect whiteboard interview: a worked example", "aep architect interview", "90-min", "Architects", "Career Accelerator"),
("Your AEP portfolio: five projects hiring managers ask about", "aep portfolio projects", "45-min", "Job seekers", "Career Accelerator"),
],
"Architecture, buyers and teams": [
("MarTech stack map: where AEP sits with CRM, CDP and analytics", "martech stack architecture", "45-min", "Architects", "Live Customised"),
("Customer 360 on AEP: sources to activation", "customer 360 aep", "45-min", "Architects", "CXO Hive"),
("How to evaluate a MarTech consulting engagement", "martech consulting engagement", "45-min", "Buyers", "Architecture review"),
("Training your MarTech team: a capability plan for L&D leaders", "martech team training", "45-min", "L&D leaders", "Live Customised"),
("50 real-time MarTech use cases: pick one to build", "real-time martech use cases", "45-min", "All", "Use-case library"),
],
}
assert sum(len(v) for v in T.values()) == 50

def _table(rows, start):
    h = '<div class="table-wrap"><table><thead><tr><th>#</th><th>Topic</th><th>Search phrase</th><th>Format</th><th>Audience</th><th>Next step</th></tr></thead><tbody>'
    for i, (t, k, f, a, l) in enumerate(rows, start):
        h += f"<tr><td>{i}</td><td>{e(t)}</td><td>{e(k)}</td><td>{f}</td><td>{e(a)}</td><td>{e(l)}</td></tr>"
    return h + "</tbody></table></div>"

_secs, n = [], 1
for name, rows in T.items():
    _secs.append((name, _table(rows, n))); n += len(rows)

TOPIC_PAGE = dict(
    path="academy/lesson-topics.html",
    title="50 Adobe MarTech Lesson & Webinar Topics | AEP, AJO, CJA",
    desc="Planned 3-minute lessons, 45-minute webinars and 90-minute workshops on AEP, RTCDP, AJO, CJA, Web SDK and Agentic AI, with search phrases and audiences.",
    h1="50 Adobe MarTech lesson and webinar topics",
    kicker="Academy topics", nav="Lesson topics", schema="Article", category="Academy", date="2026-10-12",
    keywords=["adobe experience platform tutorial", "aep webinar topics", "xdm schema explained", "aep identity graph", "cja vs adobe analytics", "what is mcp"],
    answer="This is the planned topic list for Infinite360 Tech Academy lessons: 50 topics across AEP, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Web SDK, governance, Agentic AI, career pathways and architecture, in 3-minute, 45-minute and 90-minute formats. Topics are planned, not all published yet. Titles describe teaching, never guaranteed jobs or results.",
    sections=[("Read this first", '<p>These are <strong>planned</strong> sessions. Published recordings are on the <a href="videos.html">videos page</a> and the <a href="youtube-playlists.html">YouTube playlists</a>. Live dates are on the <a href="workshops.html">workshops page</a>.</p>')] + _secs + [
        ("Join a session", pills(("Friday workshops", "workshops.html"), ("Free resources", "free-resources.html"), ("Register", REGISTER), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Are all 50 topics available as videos now?", "No. This is the planned list. Check the videos page and playlists for what is published."),
          ("Do these sessions guarantee a job?", "No. They teach skills. Hiring depends on your experience and the market.")],
    related=["academy/index.html", "academy/workshops.html", "academy/videos.html", "academy/free-resources.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform"), ("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer")],
)

PRESS_PAGE = dict(
    path="press.html",
    title="Press & Media: Infinite360 Tech Academy Founder & Facts",
    desc="Press contact, founder profile and programme facts for Infinite360 Tech Academy, plus story angles on Adobe MarTech skills, Agentic AI and hands-on training.",
    h1="Press and media",
    kicker="Press", nav="Press", schema="WebPage", category="Company", date="2026-10-12",
    keywords=["infinite360 tech academy press", "adobe martech training news", "pavan babu gandla"],
    answer="Infinite360 Tech Academy is an online academy for Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics and Agentic AI skills, founded by Pavan Babu Gandla in Bengaluru, India. Journalists and podcast hosts can contact the team by email or WhatsApp for interviews, commentary and event information.",
    sections=[
        ("Contact", f'<p>Email: <a href="mailto:{EMAIL}">{EMAIL}</a></p>' + pills(("WhatsApp", WHATSAPP_MSG), ("LinkedIn company page", "https://www.linkedin.com/company/30928383"), ("Founder on LinkedIn", "https://linkedin.com/in/pavanbabu1"))),
        ("Founder", "<p>Pavan Babu Gandla founded Infinite360 Business Consulting and Infinite360 Tech Academy. He works as a fractional chief data architect on Adobe Experience Cloud, Agentic AI and enterprise data architecture, and is based in Bengaluru. Experience figures are as stated by the founder.</p>"),
        ("Programme facts", '<ul class="checklist"><li>Live and recorded programmes on AEP, RTCDP, AJO, CJA, Web SDK and Agentic AI</li><li>Hands-on Friday workshops from 16 October 2026</li><li>Live Foundations batch from 15 October 2026</li><li>Career outcomes are described as target pathways; no job, salary or certification is guaranteed</li></ul><p>See the <a href="academy/index.html">Academy</a> and <a href="academy/workshops.html">workshops</a> pages for current dates and fees.</p>'),
        ("Story angles", '<ul class="checklist"><li>Why AEP, AJO and CJA skills are scarce, with cited job-market data</li><li>Moving from a developer, data engineer, analyst or QA role into Adobe MarTech</li><li>Agentic AI and MCP in enterprise MarTech: safe patterns and limits</li><li>Free weekly hands-on AEP workshops</li></ul>'),
        ("Media kit", "<p>Logos, a founder photo and a short biography are available on request by email. We do not claim any Adobe partnership or certified-partner status on this page.</p>"),
    ],
    faqs=[("Who can I speak to for an interview?", "Email or message the team and we will arrange a time with the founder."),
          ("Does the Academy claim an Adobe partnership?", "Not on this page. Partner status is shown only where it can be documented.")],
    related=["academy/index.html", "academy/workshops.html", "academy/lesson-topics.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
)
PLAN_ALL = [TOPIC_PAGE, PRESS_PAGE]
