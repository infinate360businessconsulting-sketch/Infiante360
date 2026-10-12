"""Long-form program pages: weekend CDP+Agentic AI, 30-hour advanced lab series, 4-week Agentic AI + MCP bootcamp,
MarTech SME batch, AJO live learning, weekday morning batch and career paths by background.
No calendar dates are shown. The accelerator fee stays at Rs 60,000 (owner decision)."""
import html as _h
from content_academy import program_page, PROGRAMS, REG_FORM, CHALLENGE, DEMO_AEP, DEMO_AI
e = _h.escape
EL = "https://experienceleague.adobe.com/en/docs"
NOTE = '<p class="small muted">Tool and product names (including Adobe AI features and MCP-based integrations) change quickly. We verify them against current Adobe documentation before each cohort, and training does not guarantee jobs, salary or certification.</p>'
FEE = ('<p>Paid program fees are confirmed in writing before payment. The flagship <a href="../../training/">Career Accelerator is ₹60,000</a> '
       'and, as stated by the founder, includes Adobe sandbox access and mentoring. Pricing for this track is shared on request.</p>')


def table(head, rows):
    return ('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


WEEKEND = [
 ("1","Sat","Foundations","Agentic AI basics, MCP, agents, Adobe Experience Cloud overview","Draw an AI + CDP architecture","Architecture diagram"),
 ("1","Sun","AEP setup","AEP UI, XDM, datasets, ingestion, identity","Create a customer schema and dataset","Schema and dataset"),
 ("2","Sat","Identity and profile","Identity graph, profile merge, RTCDP","Build a Customer 360 profile","Unified profile"),
 ("2","Sun","Segmentation","Real-time audience creation, behavioural segmentation","Create a high-value and a churn segment","Segments ready"),
 ("3","Sat","Web SDK and Tags","Datastream, Web SDK sendEvent implementation","Track page, product and cart events","Tracking validated"),
 ("3","Sun","Data layer and AI","ACDL JSON design, AI-assisted schema drafting","Build an ecommerce data layer","Data layer JSON"),
 ("4","Sat","Agentic AI and MCP","MCP, agents, AI coding assistants","Build an AI coding assistant","AI assistant"),
 ("4","Sun","AI debugging and automation","AI-assisted debugging, refactoring, automation","Fix tracking issues using AI","Resolved issues"),
 ("5","Sat","Dynamic datastreams","Routing to Analytics, AEP and Target","Configure multi-destination routing","Routing configuration"),
 ("5","Sun","Data Distiller","Data transformation and enrichment logic","Transform event data","Transformed dataset"),
 ("6","Sat","AJO journeys","Cart abandonment and loyalty journeys","Build a journey","Journey built"),
 ("6","Sun","CJA analytics","Funnels, attribution, dashboards","Create a dashboard","Dashboard ready"),
 ("7","Sat","AI + MarTech integration","AI-generated schemas, journeys and payloads","End-to-end AI automation","Working system"),
 ("7","Sun","Capstone","Retail and banking implementation","Full implementation","End-to-end system"),
 ("8","Sat","Governance and performance","Privacy, consent, optimisation","Create a governance model","Governance document"),
 ("8","Sun","Final assessment","Portfolio review, interview preparation","Present your project","Portfolio-ready"),
]
ADV = [
 (1,"Agentic AI in Adobe","Experience Platform agents and orchestrator","Automate journey optimisation","Explore AI agents","Agent workflow document"),
 (2,"Journey agent","AI-driven journey orchestration","Cart abandonment automation","Create a journey using AI","Journey flow"),
 (3,"Brand governance agent","Automated compliance and governance","Consent and GDPR automation","Define governance rules","Governance model"),
 (4,"Product support agent","AI troubleshooting automation","Debug AEP and AJO issues","Resolve an issue using AI","Debug report"),
 (5,"Marketing copilot","AI insights via a copilot","Marketing decision automation","Query insights","Insights report"),
 (6,"Mini project 1","AI agent setup","End-to-end agent workflow","Build an agent flow","Working agent system"),
 (7,"MCP deep integration","Agent orchestration via MCP","Multi-agent CDP workflows","Create an MCP pipeline","MCP system"),
 (8,"Multi-agent systems","Agent collaboration","Journey and analytics automation","Build a multi-agent flow","Agent system"),
 (9,"AI decisioning","Real-time decision engine","Next best offer engine","Build a decision model","Decision engine"),
 (10,"AI personalisation","Hyper-personalisation","Dynamic content targeting","Create a personalisation flow","Personalised journey"),
 (11,"Experimentation agent","AI-driven experimentation","A/B testing automation","Run an experiment","Experiment result"),
 (12,"Mini project 2","AI personalisation system","End-to-end personalisation","Build a personalisation engine","Working system"),
 (13,"Data Distiller","Advanced data transformation","Data enrichment pipelines","Transform a dataset","Enriched dataset"),
 (14,"Dynamic datastreams","Multi-destination routing","Analytics, Target and AEP routing","Configure routing","Routing configuration"),
 (15,"Real-Time CDP advanced","Identity stitching at scale","Unified customer view","Build an identity graph","Unified profile"),
 (16,"AI data layer","Auto-generate a data layer","Schema automation","Generate JSON","Data layer JSON"),
 (17,"sendEvent optimisation","Payload optimisation","Performance tuning","Optimise a payload","Optimised payload"),
 (18,"Mini project 3","AI data pipeline","End-to-end pipeline","Build a pipeline","Working pipeline"),
 (19,"CJA advanced analytics","Attribution and pathing","Multi-touch attribution","Build an attribution model","Attribution report"),
 (20,"Predictive analytics","ML models on AEP data","Churn prediction","Train a model","Prediction output"),
 (21,"AI segmentation","Real-time predictive segments","High-value user prediction","Create a segment","Segment output"),
 (22,"Customer journey intelligence","Full lifecycle tracking","Banking lifecycle","Map the lifecycle","Journey map"),
 (23,"Mini project 4","AI analytics system","End-to-end analytics","Build an analytics system","Analytics dashboard"),
 (24,"Validation","Debug analytics","Fix attribution issues","Validate reports","Validation document"),
 (25,"AI governance","Data privacy and compliance","GDPR consent automation","Implement governance","Governance document"),
 (26,"AI security","Secure AI workflows","Access control","Define policies","Security model"),
 (27,"Performance scaling","Optimise large systems","High-traffic system","Optimise a system","Performance report"),
 (28,"Cost optimisation","Token and infrastructure optimisation","Reduce AI cost","Optimise cost","Cost report"),
 (29,"Capstone project","End-to-end AI CDP system","BFSI and retail implementation","Build the full system","Working architecture"),
 (30,"Final assessment","Interview and portfolio","Scenario solving","Solve scenarios","Assessment result"),
]
PATHS = [
 ("Software developers","JavaScript, APIs and application development","AEP developer, MarTech engineer, Adobe integration developer"),
 ("Data engineers","ETL, databases, pipelines and cloud","AEP data engineer, customer data engineer, CDP engineer"),
 ("Data analysts","Analytics and reporting","CJA analyst, customer analytics specialist, MarTech analyst"),
 ("Cloud and DevOps professionals","Cloud, automation, deployment and APIs","MarTech integration engineer, platform engineer, automation specialist"),
 ("Architects and technical leads","Solution and platform design","AEP architect, MarTech architect, customer data architect"),
 ("Business and systems analysts","Requirements, process and stakeholders","MarTech business analyst, CX analyst, solution consultant"),
 ("Consultants and IT professionals","Enterprise consulting","Adobe MarTech consultant, AEP consultant, technical consultant"),
 ("Project and programme managers","Delivery and transformation leadership","MarTech programme manager, delivery manager, transformation manager"),
 ("QA, testing and support","Testing and production support","MarTech QA specialist, implementation specialist, support consultant"),
 ("Sales, presales and account professionals","Customer-facing and solutioning skills","MarTech solution consultant, presales consultant, solution advisor"),
 ("Security and governance professionals","Compliance, privacy and security","MarTech governance specialist, customer data governance consultant"),
 ("Students and freshers","Foundational technology skills","Junior MarTech engineer, AEP associate, MarTech analyst"),
]

def _tl(items):
    return '<div class="timeline">' + "".join(f'<div class="step"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in items) + "</div>"

P = []
P.append(program_page(
 "academy/programs/agentic-ai-cdp-weekend-batch.html", "Agentic AI + Adobe CDP Weekend Batch",
 "Agentic AI + Adobe CDP Weekend Batch: 16 Sessions",
 "Weekend program for working professionals: AEP, RTCDP, AJO, CJA, Agentic AI and MCP in 16 two-hour sessions with BFSI and retail projects.",
 "Academy · Weekend batch",
 ["agentic ai adobe cdp course", "weekend aep training", "rtcdp ajo cja weekend batch", "mcp for martech course", "adobe cdp portfolio projects"],
 "The Agentic AI + Adobe CDP Weekend Batch is a program for working professionals that runs on Saturdays and Sundays, two hours a day, across 16 sessions. It combines Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics with Agentic AI and MCP, using BFSI and retail projects, and ends with a portfolio review and interview preparation.",
 "Beginner to intermediate", "Live · weekends · 2 hours a day", "On request", None,
 ["16 live sessions, Saturday and Sunday", "Real BFSI and retail MarTech projects", "A deliverable after every session", "Portfolio review and interview preparation", "Designed for working professionals"],
 ["Draw an AI and CDP reference architecture", "Design XDM schemas, datasets and ingestion", "Build identity graphs and a Customer 360 profile", "Create real-time and behavioural audiences", "Implement Web SDK, datastreams and a data layer", "Use AI assistants and MCP to speed up debugging and automation", "Build AJO journeys and CJA dashboards", "Deliver a retail and banking capstone with a governance model"],
 [("Weeks 1-2: platform foundations", ["Foundations and architecture", "AEP setup, XDM, datasets and identity", "Profile merge and segmentation"]),
  ("Weeks 3-4: collection and AI", ["Web SDK and Tags", "Data layer design with AI assistance", "Agentic AI, MCP and AI debugging"]),
  ("Weeks 5-6: pipelines, journeys, analytics", ["Dynamic datastreams and Data Distiller", "AJO journeys", "CJA funnels, attribution and dashboards"]),
  ("Weeks 7-8: integration and capstone", ["AI plus MarTech integration", "Retail and banking capstone", "Governance, performance and final assessment"])],
 [("Working professionals", "Engineers, analysts and consultants who can only study at weekends."), ("Career switchers", "Professionals moving into Adobe MarTech from data, cloud or development."), ("MarTech practitioners", "People adding Agentic AI to an Adobe skill set.")],
 [("Session-by-session plan", table(["Week", "Day", "Module", "Topics", "Hands-on project", "Deliverable"], WEEKEND), "plain", "Schedule"),
  ("Fees and enquiry", FEE + NOTE, "alt", "Fees")],
 [("Do I need prior Adobe experience?", "No. The batch starts with architecture and AEP basics before moving to identity, journeys and AI."),
  ("What will I have at the end?", "A set of deliverables, one per session, and a retail and banking capstone you can present in interviews. These are training projects, not client work."),
  ("Is employment guaranteed?", "No. We provide portfolio and interview preparation; hiring decisions rest with employers.")],
 ["academy/programs/agentic-ai-advanced-30-hour.html", "training/index.html", "academy/programs/agentic-ai-mcp-track.html"]))

P.append(program_page(
 "academy/programs/agentic-ai-advanced-30-hour.html", "Advanced Agentic AI + AEP: 30-Hour Lab Series",
 "Advanced Agentic AI + AEP: 30-Hour Lab Series",
 "Thirty one-hour labs on Agentic AI with Adobe Experience Platform: journey agents, MCP pipelines, decisioning, CJA attribution, governance and a CDP capstone.",
 "Academy · Advanced lab series",
 ["agentic ai aep advanced", "mcp pipeline training", "ai journey agent ajo", "ai decisioning adobe", "advanced rtcdp cja course"],
 "The Advanced Agentic AI + AEP lab series is 30 one-hour hands-on sessions for people who already know the basics of Adobe Experience Platform. Each hour pairs a use case with a task and a deliverable, covering agents, MCP pipelines, multi-agent flows, AI decisioning, personalisation, Data Distiller, predictive analytics, governance, security and a BFSI and retail capstone.",
 "Intermediate to advanced", "Live labs · 30 hours", "On request", None,
 ["30 one-hour hands-on labs", "Four mini projects and a capstone", "A deliverable per lab", "Governance, security and cost modules", "Final assessment with interview and portfolio review"],
 ["Design agent workflows for journey optimisation and troubleshooting", "Build MCP pipelines and multi-agent flows", "Create decisioning and personalisation flows", "Apply Data Distiller and dynamic datastreams", "Build attribution and predictive analytics", "Apply AI governance, security, scaling and cost control"],
 [("Hours 1-6: agents and mini project 1", ["Agentic AI in Adobe", "Journey, governance and support agents", "Marketing copilot"]),
  ("Hours 7-12: MCP, decisioning, personalisation", ["MCP integration and multi-agent systems", "AI decisioning and next best offer", "Experimentation and mini project 2"]),
  ("Hours 13-18: data and collection", ["Data Distiller and datastreams", "Identity stitching at scale", "AI data layer, sendEvent optimisation, mini project 3"]),
  ("Hours 19-24: analytics", ["CJA attribution and pathing", "Predictive analytics and segments", "Lifecycle intelligence, mini project 4, validation"]),
  ("Hours 25-30: governance and capstone", ["Governance and security", "Performance and cost optimisation", "Capstone and final assessment"])],
 [("AEP practitioners", "People who have used AEP and want to add AI-assisted delivery."), ("Architects", "Architects designing governed AI on customer data."), ("Consultants", "Delivery consultants preparing for AI-heavy Adobe engagements.")],
 [("Hour-by-hour plan", table(["Hour", "Module", "Advanced topic", "Use case", "Hands-on task", "Deliverable"], [(str(a), b, c, d, f, g) for a, b, c, d, f, g in ADV]), "plain", "Schedule"),
  ("Fees and enquiry", FEE + NOTE, "alt", "Fees")],
 [("What should I know first?", "AEP basics: XDM, datasets, profiles and audiences. If you are new, start with the weekend batch or the Career Accelerator."),
  ("Are the AI tools specified?", "Labs name the tools used per hour, such as Claude-based assistants alongside AEP and AJO. Tool availability and licences depend on your own accounts and are verified before the cohort.")],
 ["academy/programs/agentic-ai-cdp-weekend-batch.html", "guides/what-is-mcp.html", "training/index.html"]))

P.append(program_page(
 "academy/programs/adobe-cx-enterprise-agentic-ai-bootcamp.html", "Adobe CX Enterprise Agentic AI Bootcamp",
 "Adobe CX Enterprise Agentic AI Bootcamp: 4 Weeks",
 "Four-week bootcamp on Claude Desktop, MCP and Adobe Experience Platform: agentic AI, AEP data context, journeys and an AI copilot capstone.",
 "Academy · Agentic AI bootcamp",
 ["adobe agentic ai bootcamp", "claude desktop mcp aep", "adobe mcp gateway training", "enterprise marketing ai copilot", "adobe ai assistant agents course"],
 "The Adobe CX Enterprise Agentic AI Bootcamp is a four-week hands-on program on Agentic AI with Adobe Experience Cloud. Week one covers agents, MCP and responsible AI, week two connects AEP data through developer authentication, XDM, datasets and identity, week three covers audience and journey intelligence with AJO, CJA and Analytics, and week four is a capstone concept for an enterprise marketing AI copilot.",
 "Intermediate", "Live · 4 weeks", "On request", None,
 ["Four weeks of live, hands-on sessions", "Claude Desktop and MCP labs", "AEP data context: XDM, datasets, identity and profile", "Audience, journey and analytics intelligence", "Enterprise marketing copilot capstone"],
 ["Explain agentic AI, agent orchestration and MCP architecture", "Apply responsible-AI and governance concepts", "Set up developer-console and OAuth access concepts for AEP", "Use XDM, datasets, identity and profile as agent context", "Qualify audiences and validate journeys with AI support", "Design an enterprise marketing AI copilot"],
 [("Week 1: Agentic AI foundations", ["Agentic AI and agent patterns", "Adobe AI Assistant, agent orchestrator and platform agents (as currently documented)", "Claude Desktop and MCP architecture", "Responsible AI"]),
  ("Week 2: AEP + MCP", ["Adobe Developer Console and OAuth", "MCP gateway concepts", "XDM and datasets", "Identity Service and Real-Time Customer Profile"]),
  ("Week 3: audience and journey intelligence", ["Audience agent and qualification", "AJO and journey validation", "CJA and Adobe Analytics", "Data insights with AI"]),
  ("Week 4: enterprise AI copilot", ["Work with audiences", "Validate journeys", "Generate analytics insights", "Recommend CX improvements and automate workflows", "Apply enterprise governance"])],
 [("MarTech engineers and architects", "People designing AI automation on customer data."), ("Analysts and consultants", "Professionals who want AI-assisted analysis."), ("Technology leaders", "Leaders evaluating governed agentic AI for marketing.")],
 [("What the capstone builds", _tl([("Audiences", "Work with Adobe audiences."), ("Journeys", "Validate customer journeys."), ("Insights", "Generate analytics insights and recommend CX improvements."), ("Governance", "Automate workflows under enterprise controls.")]) + "<p>The capstone is a concept and prototype built in a training environment, not a production deployment.</p>", "dark", "Capstone"),
  ("Fees and enquiry", FEE + NOTE, "alt", "Fees")],
 [("Do I need to code?", "Basic scripting helps, but labs provide starter material and the capstone can be design-led."),
  ("Which Adobe features are used?", "Adobe's AI and MCP-related capabilities evolve. We confirm what is generally available against Adobe's documentation before each cohort and do not imply an official partnership.")],
 ["academy/programs/agentic-ai-mcp-track.html", "guides/what-is-mcp.html", "academy/programs/agentic-ai-advanced-30-hour.html"]))

P.append(program_page(
 "academy/programs/martech-sme-batch.html", "Adobe MarTech SME Batch",
 "Adobe MarTech SME Batch: AEP, RTCDP, AJO, CJA",
 "Live batch for SME depth across AEP, RTCDP, AJO, CJA, Web SDK, XDM, APIs and MarTech architecture, from strategy to optimisation.",
 "Academy · MarTech SME",
 ["adobe martech sme training", "aep rtcdp ajo cja sme batch", "martech architect training", "customer 360 training", "web sdk xdm apis course"],
 "The Adobe MarTech SME Batch builds practical subject-matter-expert depth across Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Adobe Analytics, Web SDK, XDM and APIs. It follows a Strategy, Architecture, Implementation, Optimisation arc through enterprise scenarios, troubleshooting and architect concepts, including AI and agentic AI.",
 "Intermediate", "Live · instructor-led", "On request", None,
 ["Live instructor-led sessions", "Enterprise implementation scenarios", "Troubleshooting and real-world cases", "Architect and SME concepts", "Career and interview guidance"],
 ["Explain end-to-end MarTech architecture", "Design XDM, identity and Customer 360", "Implement and validate Web SDK collection", "Orchestrate journeys in AJO", "Analyse behaviour in CJA and Adobe Analytics", "Work with APIs and integrations", "Troubleshoot enterprise scenarios"],
 [("Strategy", ["MarTech strategy and use-case selection", "Customer 360 and data strategy"]), ("Architecture", ["AEP, XDM and identity", "RTCDP audiences and activation", "Integrations and APIs"]), ("Implementation", ["Web SDK and datastreams", "AJO journeys", "CJA and Adobe Analytics"]), ("Optimisation", ["Troubleshooting", "AI and agentic AI additions", "Governance and consent"])],
 [("Aspiring SMEs", "Practitioners who want depth across the Adobe stack."), ("Consultants", "People supporting enterprise implementations."), ("Architects", "Architects adding Adobe-specific depth.")],
 [("Strategy to optimisation", _tl([("Strategy", "Choose use cases and measures."), ("Architecture", "Design data, identity and activation."), ("Implementation", "Build collection, audiences and journeys."), ("Optimisation", "Measure, troubleshoot and improve.")]), "dark", "Approach"),
  ("Fees and enquiry", FEE + NOTE, "alt", "Fees")],
 [("How is the SME batch different from the Career Accelerator?", "The SME batch focuses on depth and architect concepts. The Career Accelerator adds a longer project path and career preparation; see the accelerator page for its fee and format.")],
 ["training/index.html", "academy/programs/agentic-ai-cdp-weekend-batch.html", "academy/index.html"]))

P.append(program_page(
 "academy/programs/ajo-live-learning.html", "Adobe Journey Optimizer Live Learning",
 "Adobe Journey Optimizer Live Learning: Morning Batch",
 "Live morning sessions on Adobe Journey Optimizer: orchestration, audience qualification, activation, personalisation, validation and measurement.",
 "Academy · AJO",
 ["ajo live training", "adobe journey optimizer morning batch", "journey orchestration course", "ajo validation", "ajo analytics measurement"],
 "Adobe Journey Optimizer Live Learning teaches AJO through practical enterprise scenarios in a live morning session, typically 6:45 to 8:15 AM IST. Topics are journey orchestration, audience qualification, customer journeys, data and activation, personalisation concepts, journey validation, and analytics and measurement. Timings are confirmed when you register.",
 "Intermediate", "Live · morning session", "On request", None,
 ["Live morning sessions, about 90 minutes", "Enterprise implementation scenarios", "Selected recorded AEP learning videos", "Hands-on and sandbox learning opportunities", "Career and interview guidance"],
 ["Design journeys from entry to exit", "Qualify audiences for journeys", "Connect data and activation", "Apply personalisation concepts", "Validate journeys before launch", "Measure results in analytics"],
 [("Orchestration", ["Journey building blocks", "Events, conditions and actions", "Entry, exit and timing rules"]), ("Data and audiences", ["Audience qualification", "Data and activation", "Consent and channels"]), ("Quality and measurement", ["Personalisation concepts", "Journey validation", "Analytics and measurement"])],
 [("Marketing technologists", "Practitioners who build or run journeys."), ("AEP professionals", "People extending from the platform into orchestration."), ("Consultants", "Delivery staff preparing for AJO projects.")],
 [("Fees and enquiry", FEE + NOTE, "alt", "Fees")],
 [("When are the sessions?", "The morning slot is usually 6:45 to 8:15 AM IST. Final timings are shared when you register."),
  ("Is AJO taught in the Career Accelerator too?", "Yes. AJO is one of the platforms in the accelerator.")],
 ["academy/courses/ajo-training.html", "training/index.html", "academy/programs/martech-sme-batch.html"]))

P.append(program_page(
 "academy/programs/weekday-morning-batch.html", "Weekday Morning Live Batch",
 "Weekday Morning Batch: Adobe MarTech + Agentic AI",
 "Monday to Friday morning batch (6:45-8:30 AM IST): Adobe MarTech and Agentic AI, a free architect challenge, demos and weekly community calls.",
 "Academy · Weekday batch",
 ["adobe martech morning batch", "weekday aep training", "enterprise architect challenge", "adobe martech agentic ai batch", "friday community call adobe"],
 "The Weekday Morning Batch is a Monday to Friday live program, usually 6:45 to 8:30 AM IST, with day-by-day practical learning in Adobe MarTech and Agentic AI. It begins with foundations before moving to enterprise implementations. Registration gives access to the learning path, a free Enterprise Architect Challenge, demo recordings, a roadmap, weekly Friday community calls and career guidance. Training is paid; it is not free.",
 "Beginner to advanced", "Live · Monday to Friday", "On request", None,
 ["Monday to Friday live sessions", "Adobe MarTech learning path and roadmap", "Free Enterprise Architect Challenge (test series)", "Demo session recordings", "Weekly Friday community calls", "Career guidance"],
 ["Foundations first, then enterprise implementations", "AEP, AJO, CJA, RTCDP, Agentic AI and Edge Delivery Services", "Identity resolution and XDM schema design", "Enterprise architecture thinking", "Interview preparation and resume guidance"],
 [("What the free challenge tests", ["Adobe Experience Platform (AEP)", "Adobe Journey Optimizer (AJO) and Customer Journey Analytics (CJA)", "RTCDP, Agentic AI and Edge Delivery Services", "Identity resolution", "XDM schema design", "Enterprise architecture"])],
 [("Working professionals", "Data engineers, software engineers, solution architects and Adobe professionals."), ("Marketing and CRM professionals", "Marketers, CRM specialists, digital marketers and business analysts."), ("Career switchers and graduates", "AI enthusiasts, career switchers and fresh graduates.")],
 [("Free starting points", f'<ul class="checklist"><li><a href="{CHALLENGE}" rel="noopener" target="_blank">Take the free Enterprise Architect Challenge</a></li><li><a href="{DEMO_AEP}" rel="noopener" target="_blank">Watch the AEP, AJO and CJA demo</a></li><li><a href="{DEMO_AI}" rel="noopener" target="_blank">Watch the Agentic AI and MCP demo</a></li><li><a href="../community.html">Join the community and Friday calls</a></li></ul>', "alt", "Free"),
  ("Fees and enquiry", FEE + NOTE, "plain", "Fees"),
  ("Corporate training too", '<p>The Academy also runs <a href="../../training/corporate-training.html">corporate training</a>: team upskilling, enterprise workshops, AI workshops, architecture reviews and implementation guidance.</p>', "alt", "Teams")],
 [("Is this batch free?", "No. The challenge, demos and community are free; the live batch is paid and fees are confirmed in writing before payment."),
  ("Will it get me a job?", "It builds skills, a portfolio and interview readiness. We do not promise employment or salary outcomes.")],
 ["academy/free-resources.html", "training/index.html", "academy/community.html"]))

PATHS_PAGE = dict(
 path="academy/career-paths-by-background.html", title="Adobe MarTech Career Paths by Background | Infinite360",
 desc="Move into Adobe MarTech and Agentic AI from developer, data, cloud, analytics, QA, consulting, management or fresher backgrounds: roles and skills to build.",
 h1="Adobe MarTech career paths by background", kicker="Academy · Career transition",
 keywords=["career change to adobe martech", "aep developer career", "cja analyst career", "martech architect path", "adobe martech roles for freshers"],
 schema="Article", category="Academy", nav="Career paths",
 answer="Your existing technology, data, cloud, analytics, consulting or management experience can be the base for an Adobe MarTech career. The usual route is to keep your core skill, add the MarTech layer (AEP, XDM, identity, RTCDP, Web SDK, Analytics, AJO, CJA, APIs, Agentic AI and MCP), build project evidence and then prepare for interviews. Roles listed here are what learners prepare for, not guaranteed outcomes.",
 sections=[
  ("Do not restart, redirect", "<p>Most Adobe MarTech roles value what you already know: APIs, data pipelines, analytics, cloud, testing, delivery or customer-facing skills. The gap is usually the Adobe and customer-data layer, which you can build with structured learning and projects.</p>", ),
  ("Roles by starting background", table(["Your background", "Skills you carry", "Roles to prepare for"], PATHS) + "<p class='small muted'>These are roles learners commonly prepare for. We do not guarantee interviews, placement or salary.</p>"),
  ("One program, several entry points", _tl([("1. Your experience", "Engineering, data, cloud, analytics, IT, consulting or business."), ("2. The MarTech layer", "AEP, XDM, identity, RTCDP, Web SDK, Analytics, AJO, CJA, Agentic AI."), ("3. Project evidence", "Customer 360, ingestion, identity, segmentation, journeys, analytics, personalisation, AI."), ("4. Role preparation", "Resume, LinkedIn, mock interviews and role mapping.")])),
  ("What you will build", '<ul class="checklist cols-2"><li>Customer 360</li><li>AEP data and XDM architecture</li><li>Identity resolution</li><li>Real-Time Customer Profiles</li><li>Audience segmentation</li><li>Web SDK implementation</li><li>Journey Optimizer journeys</li><li>Customer Journey Analytics</li><li>Enterprise APIs and integrations</li><li>Agentic AI and MCP workflows</li></ul><p>These are training projects, not client work.</p>'),
  ("Ways to learn", '<ul class="checklist"><li><strong>Weekend mentorship batch:</strong> live sessions, labs, scenarios and Q&amp;A (<a href="programs/agentic-ai-cdp-weekend-batch.html">weekend batch</a>).</li><li><strong>Intensive batch:</strong> accelerated, project-based training with mentor support (<a href="../training/">Career Accelerator</a>).</li><li><strong>Career support:</strong> resume and LinkedIn guidance, role mapping, interview preparation and ongoing mentorship.</li></ul>'),
  ("Next steps", '<p class="cta-row"><a class="btn btn-primary" href="../training/">Career Accelerator · ₹60,000</a><a class="btn btn-ghost" href="index.html">All programs</a><a class="btn btn-ghost" href="../training/career-transition.html">Career transition guide</a></p>'),
 ],
 faqs=[("Can a fresher join?", "Yes. Freshers start from foundations and work towards junior MarTech engineer, AEP associate or analyst roles. Outcomes are not guaranteed."),
       ("Do I need Adobe experience?", "No. Foundational Adobe concepts are taught from the start.")],
 related=["academy/index.html", "training/index.html", "training/career-transition.html"],
)

# register in the program catalogue so cards and hub link to the new pages
for _p, _n, _c, _l, _f, _s in [
    ("academy/programs/agentic-ai-cdp-weekend-batch.html", "Agentic AI + Adobe CDP Weekend Batch", "Weekend batch", "Beginner to intermediate", "Live · 16 weekend sessions", "Agents, AEP, RTCDP, AJO and CJA with BFSI and retail projects."),
    ("academy/programs/agentic-ai-advanced-30-hour.html", "Advanced Agentic AI + AEP: 30-Hour Lab Series", "Advanced labs", "Intermediate to advanced", "Live · 30 one-hour labs", "MCP pipelines, multi-agent flows, decisioning, governance and a CDP capstone."),
    ("academy/programs/adobe-cx-enterprise-agentic-ai-bootcamp.html", "Adobe CX Enterprise Agentic AI Bootcamp", "Agentic AI", "Intermediate", "Live · 4 weeks", "Claude Desktop, MCP and AEP data context, ending in an enterprise copilot capstone."),
    ("academy/programs/martech-sme-batch.html", "Adobe MarTech SME Batch", "Adobe Experience Cloud", "Intermediate", "Live · instructor-led", "SME-level depth across AEP, RTCDP, AJO, CJA, Web SDK and APIs."),
    ("academy/programs/ajo-live-learning.html", "Adobe Journey Optimizer Live Learning", "Adobe Experience Cloud", "Intermediate", "Live · morning session", "Journey orchestration, validation and measurement in AJO."),
    ("academy/programs/weekday-morning-batch.html", "Weekday Morning Live Batch", "Adobe Experience Cloud", "Beginner to advanced", "Live · Monday to Friday", "Day-by-day Adobe MarTech and Agentic AI with a free architect challenge."),
]:
    PROGRAMS.append((_p, _n, _c, _l, _f, "On request", None, _s))

PROG_ALL = P + [PATHS_PAGE]
