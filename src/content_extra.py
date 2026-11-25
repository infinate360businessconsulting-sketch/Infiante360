"""Extra academy pages built from the owner-supplied Career Accelerator material (2026-11-25).
Rewritten to the site pattern; flagged sitemap3 so they are listed in sitemap3.xml. No dates, hours, counts, reviews or outcome claims."""
import html
from content_cases import pills, REGISTER, WHATSAPP_MSG, LI_GROUP

e = html.escape
DATE = "2026-11-25"
EL = "https://experienceleague.adobe.com/en/docs"
SRC = [("Adobe Experience Platform documentation", f"{EL}/experience-platform"), ("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer"),
       ("Customer Journey Analytics documentation", f"{EL}/analytics-platform/using/cja-landing"), ("Adobe Experience Platform Web SDK", f"{EL}/experience-platform/web-sdk/home")]


def _table(head, rows):
    return ('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


PHASES = [("Days 1-15", "AEP core", "XDM, datasets, ingestion, Profile, Identity, governance, segmentation and Query Service.", "A Customer 360 data model"),
          ("Days 16-30", "Web SDK, CJA and AJO", "Datastreams, Web SDK, CJA connections and data views, AJO profiles and events, real-time journeys.", "A working event journey and a data view"),
          ("Days 31-45", "Real-Time CDP and activation", "Audiences, destinations, decisioning, personalisation and production validation.", "An audience and destination blueprint"),
          ("Days 46-60", "Architect patterns", "APIs, integration, security, environments, QA, monitoring and troubleshooting.", "An integration and QA checklist"),
          ("Days 61-75", "Agentic AI and MCP", "AI agents, tools, governed data access and MarTech automation scenarios.", "A governed MarTech agent design"),
          ("Days 76-90", "Capstone and positioning", "Capstone, interview scenarios, resume and LinkedIn positioning, certification strategy.", "A capstone write-up and an architecture story")]
PLAN = [("Days 1-2", "Career baseline and target role"), ("Days 3-4", "XDM and data modelling"), ("Days 5-6", "Datasets and ingestion"), ("Day 7", "Identity namespaces"),
        ("Days 8-9", "Profile and merge-policy thinking"), ("Day 10", "Segmentation validation"), ("Days 11-12", "Query Service and SQL"), ("Days 13-14", "Architecture and interview story")]
FOCUS = [("AEP and XDM", "Architecture", "High", "Customer 360 schema and ingestion"), ("Identity and Profile", "Enterprise", "High", "Identity graph and merge policies"),
         ("Real-Time CDP", "Activation", "High", "Audience and destination blueprint"), ("Adobe Journey Optimizer", "Production patterns", "High", "Event journey and QA checklist"),
         ("CJA and Analytics", "Business architecture", "Medium", "Executive journey dashboard"), ("Web SDK", "Implementation", "High", "Data layer and datastream"),
         ("APIs and data", "Enterprise integration", "High", "API and ETL design"), ("Agentic AI and MCP", "Applied architecture", "High", "Governed MarTech agent")]

ROADMAP = dict(
    path="academy/career-accelerator-roadmap.html", title="Adobe MarTech Career Accelerator: 90-Day Learning Roadmap",
    desc="A six-phase, 90-day roadmap for learning Adobe MarTech and Agentic AI, with a 14-day starter plan and a table of where to focus first.",
    h1="90-day Adobe MarTech and Agentic AI learning roadmap", kicker="Academy · Roadmap", nav="90-day roadmap", schema="Article", category="Academy", date=DATE,
    keywords=["adobe martech learning roadmap", "aep learning path 90 days", "adobe experience platform study plan", "agentic ai martech roadmap", "martech career roadmap"],
    answer="This roadmap splits Adobe MarTech and Agentic AI learning into six 15-day phases: AEP core, Web SDK with CJA and AJO, Real-Time CDP, architect patterns, Agentic AI with MCP, and a capstone. Each phase ends with a piece of evidence you can show. A 14-day starter plan and a focus table help you decide what to learn first. It is a study plan, not a guarantee of any job or certification.",
    sections=[
        ("Six phases, each with an output", _table(["Days", "Phase", "What you cover", "Evidence you produce"], PHASES)),
        ("14-day starter plan", _table(["Days", "Focus"], PLAN)),
        ("Where to focus first", '<p>The emphasis column is our suggested ordering for architecture-focused roles. Adjust it to the role you are targeting.</p>' + _table(["Capability", "Target", "Suggested emphasis", "Evidence to build"], FOCUS)),
        ("What this roadmap does not promise", '<p class="note">It does not guarantee a job, a salary or a certification. Outcomes depend on your background, practice and the market. Practice happens on sandbox or simulated environments with synthetic data.</p>'),
        ("Next steps", "<p>See the <a href=\"portfolio-projects-and-interview-scenarios.html\">portfolio projects and interview scenarios</a>, the <a href=\"hands-on-projects.html\">hands-on projects</a> and the <a href=\"../adobe-experience-platform/interview-questions.html\">AEP interview questions</a>.</p>"
         + pills(("Career Accelerator", "../training/index.html"), ("Register", REGISTER), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Is 90 days enough to learn Adobe MarTech?", "It is enough to build a structured foundation and a portfolio. Depth in any one product takes longer and depends on hands-on practice."),
          ("Do I need Adobe licences to follow the roadmap?", "Not to start. Early phases use documentation, simulators and synthetic data; check what any live programme provides before you enrol.")],
    related=["academy/hands-on-projects.html", "academy/community-tracks.html", "academy/event-calendar.html", "training/index.html", "academy/index.html"], sources=SRC)

PROJECTS = [("Enterprise Customer 360", "Sources, XDM, identity, profile, audiences, activation"), ("Real-time transaction journey", "Streaming event, profile, AJO trigger, immediate communication"),
            ("RTCDP activation", "Segment strategy, qualification, destinations, activation QA"), ("CJA executive intelligence", "Cross-channel journey analysis and KPI storytelling"),
            ("Web SDK modernisation", "Data layer, Alloy.js, datastream, AEP event flow"), ("Enterprise data pipeline", "ETL, APIs, cloud storage, validation, monitoring"),
            ("MarTech integration hub", "Adobe, CRM, commerce and data-platform integration"), ("Production readiness", "Security, deployment, observability, QA, go-live controls"),
            ("Agentic AI marketing assistant", "Agent, governed tools, customer context, workflow automation"), ("AI and Adobe MarTech capstone", "AEP, RTCDP, AJO, CJA, Web SDK and MCP together")]
SCEN = [("Identity failure", "Diagnose namespaces, identity fields, graphs and merge policies"), ("Streaming delay", "Trace schema, datastream, ingestion, profile and journey conditions"),
        ("Audience mismatch", "Diagnose qualification logic, events, attributes and evaluation"), ("Web SDK migration", "Design a safe migration without breaking measurement"),
        ("CJA architecture", "Design connections and data views for cross-channel executive reporting"), ("Enterprise integration", "Design Adobe, CRM, commerce and data-lake integration"),
        ("AJO governance", "Explain suppression, frequency, testing, approvals and monitoring"), ("Agentic AI", "Expose customer context and actions to AI through governed tools"),
        ("Career positioning", "Turn projects into concise architecture stories")]

PROJ2 = dict(
    path="academy/portfolio-projects-and-interview-scenarios.html", title="Adobe MarTech Portfolio Projects and Interview Scenarios",
    desc="Ten enterprise-style Adobe MarTech portfolio project briefs and nine interview scenarios to practise, from identity failures to governed Agentic AI.",
    h1="Adobe MarTech portfolio projects and interview scenarios", kicker="Academy · Portfolio", nav="Projects and scenarios", schema="Article", category="Academy", date=DATE,
    keywords=["adobe martech portfolio projects", "aep interview scenarios", "customer 360 project brief", "ajo interview scenario", "agentic ai portfolio project"],
    answer="This page lists ten enterprise-style project briefs, from Customer 360 to an Agentic AI assistant, and nine interview scenarios such as identity failure, streaming delay and AJO governance. Each is a practice brief to build or explain with synthetic data on sandbox or simulated environments. They create evidence of skill. They do not guarantee a job.",
    sections=[
        ("Ten project briefs", _table(["#", "Project", "Flow you build"], [(str(i + 1), n, f) for i, (n, f) in enumerate(PROJECTS)])),
        ("Nine interview scenarios", _table(["Scenario", "What you should be able to explain"], SCEN)),
        ("How to use this page", '<ul class="checklist"><li>Pick one project and write a one-page design before building</li><li>Use synthetic data only; never real customer data</li><li>For each scenario, practise a two-minute explanation and a diagram</li><li>Keep the write-ups: they become your architecture stories</li></ul>'),
        ("Related", "<p>The <a href=\"hands-on-projects.html\">hands-on projects page</a> describes the six projects used in the programme, and the <a href=\"career-accelerator-roadmap.html\">90-day roadmap</a> shows when each fits.</p>"
         + pills(("Career Accelerator", "../training/index.html"), ("Register", REGISTER), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Are these projects client work?", "No. They are practice briefs using synthetic data. None describes a delivered client engagement."),
          ("Can I use these in a portfolio?", "Yes, as your own build and write-up, clearly labelled as practice projects on synthetic data.")],
    related=["academy/career-accelerator-roadmap.html", "academy/hands-on-projects.html", "adobe-experience-platform/interview-questions.html", "training/index.html"], sources=SRC)


PHONE = "+91 82968 93895"
TRACKS = [("Adobe Experience Platform and AI", "AEP architecture, XDM, ingestion and AI use", "workshops.html"),
          ("CDP Knowledge Bytes", "Short weekly CDP technical notes and questions", "../learn/index.html"),
          ("Real-Time CDP", "Audiences, identity resolution, destinations and activation", "workshops.html"),
          ("Adobe Journey Optimizer", "Journey design, events, suppression and QA", "workshops.html"),
          ("Customer Journey Analytics", "Connections, data views and cross-channel analysis", "workshops.html"),
          ("Adobe Web SDK and data collection", "Datastreams, data layer and event validation", "hands-on-projects.html"),
          ("MarTech architects", "Reference architectures and integration patterns", "../services/index.html"),
          ("Customer 360 engineers", "Data modelling, identity and profile design", "hands-on-projects.html"),
          ("Agentic AI builders", "Agents, tools and governed MarTech automation", "../services/agentic-ai-mcp.html"),
          ("MCP developers", "Model Context Protocol servers and safe tool access", "../guides/what-is-mcp.html")]


def _links(rows):
    return ('<div class="table-wrap"><table><thead><tr><th>Track</th><th>What members discuss</th><th>Related page</th></tr></thead><tbody>'
            + "".join(f'<tr><td>{e(a)}</td><td>{e(b)}</td><td><a href="{c}">Open</a></td></tr>' for a, b, c in rows) + "</tbody></table></div>")


COMMUNITY2 = dict(
    path="academy/community-tracks.html", title="Adobe MarTech Community Tracks: Topics You Can Join",
    desc="Ten Adobe MarTech and Agentic AI community topics, from AEP and Real-Time CDP to MCP, and how to join and ask questions in the Infiante360 community.",
    h1="Adobe MarTech community tracks", kicker="Academy · Community", nav="Community tracks", schema="WebPage", category="Academy", date=DATE,
    keywords=["adobe martech community topics", "aep community", "agentic ai mcp community", "cdp knowledge community", "martech architects network"],
    answer="Ten topic tracks organise the Infiante360 community: AEP and AI, CDP Knowledge Bytes, Real-Time CDP, AJO, CJA, Web SDK, MarTech architects, Customer 360, Agentic AI and MCP. They are discussion topics, not separate member-run groups yet. Join through the LinkedIn group or WhatsApp and say which track you want. The community is independent and is not an official Adobe user group.",
    sections=[
        ("Ten topic tracks", _links(TRACKS)),
        ("How to join", "<p>Use the LinkedIn group for discussion and WhatsApp to tell us which tracks you want. Consent is separate for each channel, and you can leave at any time.</p>"
         + pills(("LinkedIn group", LI_GROUP), ("Tell us your track on WhatsApp " + PHONE, WHATSAPP_MSG), ("Community guidelines", "community.html"))),
        ("How the community will grow", '<ul class="checklist"><li>We start with tracks that have active members and add more only when people ask</li><li>No member counts or activity figures are published until they are real</li><li>Never post passwords, keys or customer data</li><li>Administrator-written posts are labelled as such</li></ul>'),
        ("Independence", '<p class="note">This is an independent learning community. It is not sponsored by, or an official user group of, Adobe or any other vendor named on this page.</p>'),
    ],
    faqs=[("Is the community free to join?", "Joining the LinkedIn group is free. Check any programme page for fees before you enrol in training."),
          ("Can I suggest a new track?", "Yes. Message us on WhatsApp with the topic and why it needs its own space.")],
    related=["academy/community.html", "academy/event-calendar.html", "academy/career-accelerator-roadmap.html", "academy/index.html"])

SLOTS = [("Tuesday", "Adobe MarTech masterclass", "Adobe and CDP professionals", "8:00 PM IST"),
         ("Wednesday", "Agentic AI and MCP workshop", "AI engineers and MarTech developers", "8:00 PM IST"),
         ("Sunday", "Executive and research roundtable", "Senior leaders and architects", "6:00 PM IST")]
CONCEPTS = [("Enterprise MarTech and Agentic AI live demo", "../lp/martech-sme-accelerator.html"), ("Adobe Experience Platform architecture masterclass", "workshops.html"),
            ("Real-Time CDP implementation workshop", "workshops.html"), ("Adobe Journey Optimizer live lab", "workshops.html"),
            ("Customer Journey Analytics masterclass", "workshops.html"), ("Adobe Web SDK implementation challenge", "hands-on-projects.html"),
            ("Customer 360 architecture summit", "hands-on-projects.html"), ("XDM data modelling bootcamp", "aep-launchpad-bootcamp.html"),
            ("Identity graph troubleshooting workshop", "workshops.html"), ("MarTech architecture career summit", "career-accelerator-roadmap.html")]

EVENTS2 = dict(
    path="academy/event-calendar.html", title="Proposed Weekly Event Calendar for Adobe MarTech and AI",
    desc="Three proposed weekly event slots and ten event concepts for Adobe MarTech and Agentic AI. Nothing is scheduled yet; register interest to be told first.",
    h1="Proposed weekly events for Adobe MarTech and AI", kicker="Academy · Events", nav="Event calendar", schema="WebPage", category="Academy", date=DATE,
    keywords=["adobe martech webinar", "aep masterclass event", "agentic ai mcp workshop", "martech architecture summit", "adobe live lab"],
    answer="This page lists three proposed weekly slots, on Tuesday, Wednesday and Sunday, and ten event concepts from an AEP architecture masterclass to an identity graph troubleshooting workshop. None is scheduled yet: no dates, speakers or registration links are confirmed. Register your interest and we will contact you when a session is confirmed. Existing workshops and the bootcamp are listed separately.",
    sections=[
        ("Proposed weekly slots", _table(["Day", "Theme", "Audience", "Proposed time"], SLOTS) + '<p class="note">Proposed only. Slots start when speakers and dates are confirmed.</p>'),
        ("Ten event concepts", '<div class="table-wrap"><table><thead><tr><th>#</th><th>Concept</th><th>Related learning</th></tr></thead><tbody>'
         + "".join(f'<tr><td>{i + 1}</td><td>{e(n)}</td><td><a href="{u}">Open</a></td></tr>' for i, (n, u) in enumerate(CONCEPTS)) + "</tbody></table></div>"),
        ("Already available", "<p>See the <a href=\"workshops.html\">workshops</a> and the <a href=\"aep-launchpad-bootcamp.html\">AEP Launchpad bootcamp</a> for sessions with their own details.</p>"
         + pills(("Register interest", REGISTER), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("Join the community", "community-tracks.html"))),
        ("What every confirmed event will show", '<ul class="checklist"><li>Date, start and end time, and time zone</li><li>Confirmed speaker and short biography</li><li>Agenda and delivery format</li><li>Price, or free, stated up front</li><li>Registration with consent kept separate from marketing</li></ul>'),
    ],
    faqs=[("Are these events happening?", "Not yet. They are proposals. A session is announced only after the date and speaker are confirmed."),
          ("Will sessions be recorded?", "Only with the speaker's agreement. Each event page will say whether a recording is offered.")],
    related=["academy/community-tracks.html", "academy/workshops.html", "academy/aep-launchpad-bootcamp.html", "academy/index.html"])

for _p in (ROADMAP, PROJ2, COMMUNITY2, EVENTS2):
    _p["sitemap3"] = True
EXTRA_PAGES = [ROADMAP, PROJ2, COMMUNITY2, EVENTS2]
