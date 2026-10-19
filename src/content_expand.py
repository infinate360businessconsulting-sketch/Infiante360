"""Expansion pages: promo video, AEP multi-region course, AI Engineering Bootcamp, AEP implementation track (modules),
agentic engagement architecture guide and a sports and entertainment cart use case.
Source material was supplied by the owner. Unverified figures from the supplied decks (case-study percentages, old phone number) are intentionally not published."""
import html as _h
from content_academy import program_page
from content_programs import table, NOTE, FEE
from content_growth import use_case
from visuals import flow_svg, figure
e = _h.escape

import datetime as _dt
def _next_mon_tue(today=None):
    t = today or _dt.date.today()
    d = ((1 - t.weekday() - 1) % 7) or 7  # python Monday=0; days until next Monday strictly after today
    m = t + _dt.timedelta(days=((0 - t.weekday()) % 7) or 7)
    return m, m + _dt.timedelta(days=1)
def _fmt(d): return d.strftime("%a ") + str(d.day) + d.strftime(" %b %Y")
def batch_block():
    m, tu = _next_mon_tue()
    return ('<p><strong>Next batch sessions: <span id="nb">' + _fmt(m) + " and " + _fmt(tu) + '</span></strong>. New batches run every Monday and Tuesday, and these dates roll forward automatically each week. Session time is confirmed on WhatsApp when you enrol.</p>'
            '<script>(function(){try{var t=new Date();t.setHours(0,0,0,0);var a=((8-t.getDay())%7)||7;var m=new Date(t);m.setDate(t.getDate()+a);var u=new Date(m);u.setDate(m.getDate()+1);'
            'var f=function(d){return d.toLocaleDateString("en-GB",{weekday:"short",day:"numeric",month:"short",year:"numeric"}).replace(",","")};'
            'document.getElementById("nb").textContent=f(m)+" and "+f(u)}catch(e){}})();</script>')
CXO_BLOCK = '<p><strong>CXO Hive batch:</strong> starts 2 November 2026, live sessions every Saturday and Sunday, with a 100% live, instructor-led approach.</p>'
EL = "https://experienceleague.adobe.com/en/docs"
WA = "https://wa.me/918296893895"

# ---------- Promo video ----------
PROMO = dict(
    path="academy/promo-video.html", nav="Promo video",
    title="Infinite360 Tech Academy Promo Video | Adobe MarTech & AI",
    desc="Watch the 10-second Infinite360 Tech Academy promo video, then explore Adobe MarTech programs, free demo sessions and AI engineering tracks.",
    h1="Infinite360 Tech Academy promo video", kicker="Academy · Video",
    keywords=["infinite360 tech academy video", "adobe martech academy promo", "aep training video"],
    answer="This is the 10-second promo for Infinite360 Tech Academy, which teaches Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Agentic AI and AI engineering. Watch it, then open the free demo sessions, the program pages or ask on WhatsApp.",
    schema="WebPage",
    sections=[
        ("Watch the promo", '<figure class="promo-fig"><video controls preload="none" playsinline width="1280" height="720" poster="../assets/media/infinate360-promo-poster.jpg" style="width:100%;height:auto;border-radius:16px;background:#0e1d3b">'
         '<source src="../assets/media/infinate360-promo.mp4" type="video/mp4">Your browser cannot play this video. <a href="../assets/media/infinate360-promo.mp4">Download the MP4</a>.</video>'
         '<figcaption class="small muted">This promotional video was created with AI tools. Scenes are illustrative and do not show real learners, certificates or results.</figcaption></figure>', "plain", "Video"),
        ("Where to go next", '<div class="link-pills"><a href="videos.html">Free demo sessions</a><a href="../academy/index.html">All programs</a><a href="programs/ai-engineering-bootcamp.html">AI Engineering Bootcamp</a><a href="programs/aep-multi-region-multi-brand-architecture.html">AEP at scale across regions and brands</a><a href="aep-implementation-track/index.html">AEP implementation track</a>'
         f'<a href="{WA}">WhatsApp +91 82968 93895</a></div>', "alt", "Next steps"),
    ],
    faqs=[("Is the video a real classroom recording?", "No. It is an AI-generated promotional video. For real recorded sessions, open the free demo sessions page.")],
    related=["academy/videos.html", "academy/index.html", "training/index.html"],
)

# ---------- AEP across regions and brands ----------
REGION = program_page(
 "academy/programs/aep-multi-region-multi-brand-architecture.html", "Architecting AEP for Scale Across Regions and Brands",
 "Architecting Adobe Experience Platform Across Regions & Brands",
 "30-hour course with 1-on-1 mentorship on multi-region, multi-brand Adobe Experience Platform architecture, identity, consent, governance and activation.",
 "Academy · Architecture course",
 ["aep multi region architecture", "aep multi brand architecture", "aep sandboxes governance course", "customer identity architecture training", "cdp architecture course"],
 "Architecting AEP for Scale Across Regions and Brands is a 30-hour course with 1-on-1 mentorship. It teaches how to design Adobe Experience Platform for several regions and brands: a shared XDM model, identity and consent, governance by region and brand, role-based access, cross-brand audiences and integration with CRM, CIAM and ad-tech systems.",
 "Intermediate to advanced", "Live · 30 hours · 1-on-1 mentorship", "On request", None,
 ["30 hours of learning built around real-world use cases", "1-on-1 mentorship for your own platform challenges", "Identity, consent and governance design", "Integration patterns for CRM, CIAM and ad-tech"],
 ["Design customer identity frameworks aligned to compliance needs", "Plan SSO, MFA and consent management across platforms", "Model data in XDM so profiles are consistent across brands", "Decide where data residency and privacy rules shape the architecture", "Separate brands and regions with sandboxes, role-based access and data usage policies", "Build cross-brand audiences and unified reporting", "Work with marketing, legal, compliance and analytics on shared goals", "Prepare for evolving privacy regulation and responsible AI use"],
 [("Core modules 1-6", ["Introduction to AEP and its key components", "Data ingestion: batch and streaming methods", "Data modelling with XDM and schema management", "Identity service setup and resolution", "Building real-time customer profiles", "Audience segmentation strategies"]),
  ("Advanced modules 7-12", ["Data Science Workspace and ML model deployment", "Activation and third-party integrations", "Consent management and preferences", "Data governance, privacy and compliance", "Journey orchestration for personalisation", "Reporting and customer insights analytics"])],
 [("Platform architects", "Design for several brands, regions and legal regimes."), ("CDP and data leads", "Unify data while keeping governance and consent intact."), ("Consultants", "Bring a repeatable multi-brand pattern to client programs.")],
 [("Why scaling AEP is hard", '<ul class="checklist"><li><strong>Data silos:</strong> fragmented data gives inconsistent customer views across brands and regions.</li><li><strong>Compliance complexity:</strong> regulations such as GDPR and CCPA, and data residency limits, shape what you can centralise.</li><li><strong>One scalable model:</strong> unified insight needs a governed, compliant architecture rather than separate stacks.</li></ul>', "plain", "The challenge"),
  ("Architecture topics covered", '<div class="grid-2"><div class="card"><h3>Regional considerations</h3><p>Data residency and privacy, localised data collection, multi-tenant isolation per region or brand, and processing near the user to reduce latency.</p></div><div class="card"><h3>Multi-brand design</h3><p>Brand-specific governance, role-based access control, cross-brand segmentation on unified profiles and aggregated reporting.</p></div><div class="card"><h3>Scalability components</h3><p>Data lake, Real-Time CDP, AI and ML, and Adobe Journey Optimizer for multi-channel orchestration.</p></div><div class="card"><h3>Emerging trends</h3><p>Generative AI for insights, agentic personalisation, cloud transformation, stronger privacy focus and ethical AI deployment.</p></div></div>', "alt", "Content"),
  ("Learning roadmap", table(["Stage", "Focus"], [("Week 1", "CDP basics, identity management and data governance"), ("Week 2", "Hands-on projects on Adobe Experience Platform and analytics tools"), ("Week 3", "Real-time profiles and universal identifiers"), ("Week 4", "Working with cross-functional teams"), ("Week 5", "Certification preparation and specialisation"), ("Ongoing", "Continuous improvement and mentorship")]) + '<p class="small muted">The roadmap is a guide; pace is agreed with your mentor.</p>', "plain", "Roadmap"),
  ("Fees and enquiry", batch_block() + '<p><strong>Program fee: ₹60,000.</strong> Fees are confirmed in writing before payment, and enrolled learners receive a sandbox for labs and mentoring, as stated by the founder.</p>' + NOTE + f'<p><a class="btn btn-primary" href="{WA}">Enrol or ask on WhatsApp</a> <a class="btn btn-ghost" href="../../contact-us.html">Book a demo via the form</a></p>', "alt", "Fees")],
 [("Is this for beginners?", "It assumes some familiarity with data platforms or marketing technology. Start with the AEP Launchpad Bootcamp if you are new."),
  ("Does it guarantee certification or a job?", "No. It prepares you for certification study and architecture work, but outcomes depend on you and on employers."),
  ("How is mentorship delivered?", "As 1-on-1 support on your own challenges and goals; the format is confirmed when you enquire.")],
 ["adobe-experience-platform/architecture.html", "academy/aep-launchpad-bootcamp.html", "guides/agentic-customer-engagement-architecture.html"])

# ---------- AI Engineering Bootcamp ----------
BOOT = [
 ("1", "AI, LLMs and prompt engineering", "AI vs ML vs DL, LLMs, tokens, context windows, hallucinations, model choice, zero-shot, few-shot, chain of thought, structured outputs, prompt chaining", "AI research assistant, resume builder, study assistant"),
 ("2", "n8n foundations", "Nodes, triggers, expressions, loops, error handling, scheduling, Gmail, Google Sheets, Slack, human approval", "AI email assistant, resume parser, daily news workflow"),
 ("3", "Advanced n8n and AI agents", "AI agent node, memory, tool usage, webhooks, APIs, multi-step workflows", "AI CRM, customer support agent, meeting scheduler, sales agent, recruiting assistant"),
 ("4", "Python and APIs", "Python basics, HTTP, REST, JSON, authentication, SDKs, Claude Code, virtual environments, Postman", "Weather API, AI chat script, n8n workflow in Python"),
 ("5", "FastAPI for AI applications", "Routes, validation, authentication, middleware, async, streaming, file uploads, Docker basics", "AI chat API, authentication API, file upload API"),
 ("6", "AI system design and LLM APIs", "Request lifecycle, prompt vs workflow vs RAG vs agents, cost, latency, caching, security, multiple model providers", "Enterprise AI assistant design, multi-provider chat app"),
 ("7", "LangChain fundamentals", "Chat models, prompt templates, LCEL, chains, output parsers, tool calling, LangSmith", "Chatbot, translator, summariser, email generator"),
 ("8", "RAG with LangChain", "Embeddings, chunking, retrievers, hybrid search, reranking, vector databases (Chroma, Pinecone, Qdrant, pgvector)", "PDF chatbot, company knowledge base, documentation assistant"),
 ("9", "Agents and LangGraph", "ReAct, memory, tools, state, nodes, edges, multi-agent systems, supervisors, handoffs; overview of CrewAI, OpenAI Agents SDK, Google ADK", "Research agent, coding agent, multi-agent workflow"),
 ("10", "MCP and production AI", "MCP architecture, servers, clients, resources, tools, authentication and security; evaluation, guardrails, observability", "GitHub MCP, Slack MCP, evaluation dashboard"),
 ("11", "Claude Code mastery", "CLAUDE.md, slash commands, hooks, skills, planning mode, code review, sub-agents, MCP integration", "AI coding assistant, refactor an existing project"),
 ("12", "Databases and deployment", "PostgreSQL, Supabase, Redis, storage, authentication, Docker, CI/CD, monitoring, logging", "Deploy a production AI application"),
 ("13", "Multimodal AI", "Voice, image and video model families", "Voice assistant, AI content generator"),
 ("14-16", "Capstone: production AI SaaS", "Three weeks building one production-grade AI application", "AI CRM, support platform, HR platform, knowledge base, voice agent or marketing platform"),
]
BOOTCAMP = program_page(
 "academy/programs/ai-engineering-bootcamp.html", "The Complete AI Engineering Bootcamp (2026)",
 "AI Engineering Bootcamp 2026: 16 Weeks, 40+ Projects",
 "16-week AI Engineering Bootcamp: prompts, n8n, Python, FastAPI, LangChain, RAG, LangGraph, MCP, Claude Code and a production AI SaaS capstone.",
 "Academy · AI engineering",
 ["ai engineering bootcamp", "langchain langgraph course", "rag course", "mcp course", "n8n ai agents course", "claude code course"],
 "The Complete AI Engineering Bootcamp (2026) runs 16 weeks, about 60 to 80 hours, with more than 40 projects. It moves from prompt engineering and n8n automation through Python, FastAPI, LangChain, RAG, LangGraph agents, MCP, Claude Code and deployment, and ends with a three-week capstone to build a production AI SaaS application.",
 "Beginner to intermediate", "16 weeks · 60-80 hours · 40+ projects", "On request", None,
 ["16-week structured path in 7 phases", "40+ hands-on projects", "Production AI SaaS capstone", "Career modules: portfolio, resume, interviews, freelancing"],
 ["Write structured prompts and evaluate model outputs", "Automate work with n8n and AI agents", "Build APIs with Python and FastAPI", "Build RAG systems with embeddings and vector databases", "Design agents and multi-agent systems with LangGraph", "Expose tools safely through MCP", "Use Claude Code for AI-first development", "Deploy, monitor and evaluate AI applications"],
 [("Phase 1: AI foundations (week 1)", ["AI fundamentals, LLMs, tokens, context windows, ethics", "ChatGPT, Claude, Gemini, Perplexity, NotebookLM", "Prompt engineering patterns and projects"]),
  ("Phase 2: AI automation (weeks 2-3)", ["n8n interface, triggers, expressions, error handling", "AI agent node, memory, tools, webhooks", "AI CRM, support agent, scheduler, sales agent"]),
  ("Phase 3: AI development (weeks 4-5)", ["Python, APIs and tooling", "FastAPI, authentication, streaming, Docker basics"]),
  ("Phase 4: AI engineering (weeks 6-10)", ["AI system design and LLM APIs", "LangChain, RAG, agents and LangGraph", "MCP and production AI: evaluation, guardrails, observability"]),
  ("Phase 5-6: AI-first development and production (weeks 11-13)", ["Claude Code workflow", "Databases, deployment, CI/CD, monitoring", "Multimodal AI"]),
  ("Phase 7: capstone (weeks 14-16)", ["Production AI SaaS with FastAPI, RAG, agents, MCP, vector database, Docker, authentication, evaluation and monitoring", "Documentation and final presentation"]),
  ("Bonus modules (self-paced)", ["Git, Linux, Docker deep dive, Playwright, OpenTelemetry", "Fine-tuning fundamentals, CrewAI, Google ADK, OpenAI Agents SDK", "AI product strategy, portfolio, resume and LinkedIn, technical interviews, freelancing"])],
 [("Developers", "Add AI engineering skills to your backend or full-stack work."), ("Data and automation professionals", "Move from scripts and dashboards to agents and RAG."), ("MarTech practitioners", "Connect AI agents to customer data and journeys, then see the Agentic AI + MCP track.")],
 [("Week-by-week plan", table(["Week", "Module", "Topics", "Projects"], BOOT), "plain", "Schedule"),
  ("Fees and enquiry", CXO_BLOCK + '<p><strong>CXO and executive program fee: ₹1,00,000.</strong> Fees are confirmed in writing before payment. No job, salary or certification outcome is guaranteed.</p>' + NOTE + f'<p><a class="btn btn-primary" href="{WA}">Enrol or ask on WhatsApp</a> <a class="btn btn-ghost" href="../../contact-us.html">Book a demo via the form</a></p>', "alt", "Fees")],
 [("Do I need to know Python first?", "No. Week 4 teaches the Python and API basics used in the rest of the bootcamp."),
  ("Is this about Adobe?", "No. This is general AI engineering. For Adobe-specific agentic work, see the Agentic AI and MCP track."),
  ("Do you guarantee a job?", "No. The bootcamp builds skills and a portfolio; hiring decisions rest with employers.")],
 ["academy/programs/agentic-ai-mcp-track.html", "academy/promo-video.html", "learn/index.html"])

# ---------- AEP implementation track ----------
MODS = [  # (num, slug, title, hours, prereq, lede, objectives, covers, mistakes)
 ("01", "web-sdk", "AEP Data Collection and Web SDK", "2-3 hours", "Module 0 complete. Admin rights on an AEP Data Collection property.", "Stand up a Data Collection (Tags) property and wire the Web SDK extension into a demo site.",
  ["Create a Data Collection property and map it to the demo website", "Install and configure the Web SDK extension (datastream, edge domain)", "Fire a first event and confirm it lands in Experience Platform"],
  ["Tags property structure: extensions, rules, data elements", "Web SDK versus legacy AT.js and Visitor API, and why AEP standardises on Web SDK", "Configuring a datastream and binding it to a sandbox", "Validating delivery with the debugger and Assurance"],
  ["Pointing the datastream at the wrong sandbox or dataset", "Sending events that do not match the XDM schema", "Testing with an ad blocker or consent state that suppresses the call"]),
 ("03", "rtcp", "Real-Time Customer Profile", "2-3 hours", "Modules 1-2 complete. Identity-enabled schema and dataset.", "Enable profile on a dataset and explore how identities stitch events into a unified customer view.",
  ["Enable Profile and Identity on a schema and dataset", "Understand identity namespaces and merge policies", "Look up a unified profile in the UI and through the API"],
  ["Profile fragments versus time-series (ExperienceEvent) data", "Identity namespaces, primary identity and merge policies", "Profile lookups: UI, Profile API and privacy considerations", "Computed attributes as a preview of segmentation inputs"],
  ["Enabling every dataset for Profile without a business need", "Missing or untyped identity namespaces on the schema", "Assuming the default merge policy fits every use case"]),
 ("05", "intelligent-services", "Intelligent Services", "2 hours", "Modules 2-4 complete.", "Survey AEP's AI and ML layer and where it plugs into the profile and activation flow.",
  ["Understand Customer AI, Attribution AI and Anomaly Detection at a conceptual level", "Identify which datasets and schemas each service needs as input", "Map an intelligent service output back into a reusable audience"],
  ["Where ML-derived attributes live on the profile", "Feeding model outputs back into Real-Time CDP segmentation", "Governance considerations for AI-derived attributes"],
  ["Treating a model score as ground truth", "Skipping the documented input requirements of each service", "Using derived attributes in activation without governance review"]),
 ("06", "rtcdp-segment", "Real-Time CDP: Build a Segment", "3 hours", "Modules 2-3 complete. Profile-enabled datasets with sample traffic.", "Author your first audience in Segment Builder and activate it to a destination.",
  ["Build a rule-based segment using profile and event attributes", "Understand segment evaluation: streaming, edge and batch", "Connect and activate the segment to a destination"],
  ["Segment Builder: attributes, events and the merge policy dependency", "Streaming and edge segmentation versus nightly batch evaluation", "Destination catalogue: connecting a first activation channel", "Validating activation in the destination"],
  ["Expecting batch rules to qualify in real time", "Activating without checking consent and data usage labels", "Not validating that profiles actually arrive at the destination"]),
 ("07", "ajo-orchestration", "Adobe Journey Optimizer: Orchestration", "3 hours", "Module 6 complete. An audience available for entry.", "Build your first orchestrated journey: entry audience, action and exit.",
  ["Create a journey with an audience-qualification entry event", "Add a message action and basic branching logic", "Publish and monitor journey execution"],
  ["Journey canvas concepts: entry, conditions, actions, goals", "Audience qualification versus event-triggered entry (preview of Module 10)", "Journey monitoring and troubleshooting a stalled journey"],
  ["Building one very large journey instead of smaller ones (Adobe documents a 50-activity guardrail)", "Publishing without using test mode or a dry run", "No explicit exit or goal condition"]),
 ("08", "ajo-external-data", "AJO External Data and Custom Actions", "2-3 hours", "Module 7 complete.", "Pull external context into a journey and call out to a non-Adobe system mid-journey.",
  ["Configure an external data source lookup inside a journey", "Build and invoke a custom action (webhook or API call)", "Handle the response and branch on it"],
  ["When to use external data versus profile-resident attributes", "Custom action contracts: request and response schema", "Error handling and retry behaviour for external calls"],
  ["Sending personal data in a payload without a consent check", "No fallback path when the external call fails or times out", "Leaving credentials in a shared document instead of a secure store"]),
 ("09", "ajo-offer-decisioning", "AJO: Offer Decisioning", "2-3 hours", "Modules 7-8 complete.", "Model offers, placements and decision rules, then serve a personalised offer inside a journey.",
  ["Define offers, collections and a placement", "Author eligibility and ranking rules", "Call the decision from a journey action and confirm the offer served"],
  ["Offer Decisioning data model: offers, collections, placements, rules", "Eligibility versus ranking versus prioritisation rules", "Integrating decisioning calls into a journey action"],
  ["Mixing eligibility and ranking logic in one rule", "No fallback offer when nothing is eligible", "Testing only with the profile you built the offer for"]),
 ("10", "ajo-event-journeys", "AJO: Event-Based Journeys", "2-3 hours", "Module 7 complete.", "Trigger a journey off a real-time event instead of audience qualification, for near-real-time use cases.",
  ["Configure an event-based entry using a schema event", "Compare latency and behaviour with audience-qualification entry", "Build a simple cart-abandonment style trigger"],
  ["Event-based versus audience-qualification entry, side by side", "Designing for idempotency and re-entry", "Latency expectations for event-triggered journeys"],
  ["Allowing unintended re-entry for the same event", "Assuming event journeys never need a wait or exit condition", "Not validating the event payload against the schema"]),
]
PENDING = [("00", "Getting Started"), ("02", "Data Ingestion"), ("04", "Query Service"), ("11", "Customer Journey Analytics: Analysis Workspace Dashboard")]
TRACK = "academy/aep-implementation-track"


def module_page(i):
    num, slug, title, hrs, pre, lede, obj, cov, mist = MODS[i]
    prev_ = (f'<a href="{MODS[i-1][1]}.html">&larr; Module {MODS[i-1][0]}: {e(MODS[i-1][2])}</a>' if i else '')
    next_ = (f'<a href="{MODS[i+1][1]}.html">Module {MODS[i+1][0]}: {e(MODS[i+1][2])} &rarr;</a>' if i < len(MODS) - 1 else '')
    return dict(
        path=f"{TRACK}/{slug}.html", nav=f"Module {num}",
        title=f"Module {num}: {title} | AEP"[:65],
        desc=f"AEP implementation track module {num}: {lede} Objectives, topics, common mistakes and prerequisites."[:160],
        h1=f"Module {num}: {title}", kicker="Academy · AEP implementation track",
        keywords=[title.lower(), f"aep module {num}", "aep implementation training"],
        answer=f"{lede} This module takes about {hrs} and lists its learning objectives, topics, common mistakes and prerequisites. Prerequisites: {pre}",
        schema="Article", category="Academy", date="2026-10-19",
        sections=[
            ("Learning objectives", '<ul class="checklist">' + "".join(f"<li>{e(x)}</li>" for x in obj) + "</ul>", "plain", "Objectives"),
            ("What this module covers", '<ul class="checklist">' + "".join(f"<li>{e(x)}</li>" for x in cov) + "</ul>", "alt", "Topics"),
            ("Common mistakes to avoid", '<ul class="checklist">' + "".join(f"<li>{e(x)}</li>" for x in mist) + "</ul>", "plain", "Pitfalls"),
            ("Time and prerequisites", f"<p><strong>Time investment:</strong> {e(hrs)}. <strong>Prerequisites:</strong> {e(pre)}</p><p class=\"small muted\">Lab screenshots, sandbox names and configuration IDs are shared with enrolled learners inside the Academy LMS, not on this public page.</p>", "alt", "Plan"),
            ("Move through the track", f'<p class="link-pills">{prev_}{next_}<a href="index.html">All modules</a></p>', "plain", "Navigate"),
        ],
        faqs=[], related=["academy/aep-launchpad-bootcamp.html", f"{TRACK}/index.html", "adobe-experience-platform/index.html"],
        sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform"), ("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer")],
    )


TRACK_INDEX = dict(
    path=f"{TRACK}/index.html", nav="AEP track",
    title="AEP MarTech Implementation Track: Module Guide | Infinite360",
    desc="Module guide for the Infinite360 AEP implementation track: Web SDK, Profile, Intelligent Services, Real-Time CDP segments and Journey Optimizer, step by step.",
    h1="AEP MarTech implementation track: module guide", kicker="Academy · Learning track",
    keywords=["aep implementation track", "aep training modules", "aep web sdk module", "ajo journey module"],
    answer="The AEP MarTech Implementation Track walks from data collection with the Web SDK through Real-Time Customer Profile, Intelligent Services, Real-Time CDP segments and Adobe Journey Optimizer orchestration, external data, offer decisioning and event-based journeys. Each module lists objectives, topics, prerequisites and common mistakes.",
    schema="CollectionPage",
    sections=[
        ("Modules", '<div class="grid-3">' + "".join(f'<a class="card" href="{m[1]}.html"><h3>Module {m[0]}</h3><p><strong>{e(m[2])}</strong></p><p class="small muted">{e(m[3])}</p></a>' for m in MODS) + "</div>", "plain", "Track"),
        ("In preparation", "<ul class=\"checklist\">" + "".join(f"<li>Module {n}: {e(t)}</li>" for n, t in PENDING) + "</ul><p class=\"small muted\">These modules are taught in the live program and are not yet published as public pages.</p>", "alt", "Coming"),
        ("Join the program", batch_block() + f'<p>Learn the full track with labs and mentoring in the <a href="../aep-launchpad-bootcamp.html">AEP Launchpad Bootcamp</a>, or ask about fees on <a href="{WA}">WhatsApp +91 82968 93895</a>. No job, salary or certification outcome is guaranteed.</p>', "plain", "Enrol"),
    ],
    faqs=[("Do I need Adobe access?", "Hands-on labs use a sandbox provided to enrolled learners. The public pages explain concepts and checklists.")],
    related=["academy/aep-launchpad-bootcamp.html", "academy/promo-video.html", "learn/index.html"],
)

# ---------- Architecture guide ----------
ARCH = dict(
    path="guides/agentic-customer-engagement-architecture.html", nav="Agentic engagement architecture",
    title="Agentic AI Customer Engagement Architecture on AEP",
    desc="Reference architecture for customer engagement with AEP, Real-Time CDP, Journey Optimizer, CJA and agentic AI through MCP, with guardrails.",
    h1="Customer engagement architecture: AEP plus agentic AI", kicker="Guide · Architecture",
    keywords=["agentic ai aep architecture", "mcp adobe experience platform", "ai agents journey optimizer", "next best action architecture", "aep reference architecture"],
    answer="A safe agentic architecture keeps Adobe Experience Platform as the system of record for identity and profile, Real-Time CDP for audiences, Journey Optimizer as the single execution engine and Customer Journey Analytics for measurement. AI agents read profile and journey state, propose actions through narrowly scoped MCP tools and a guardrail check, and never send messages directly.",
    schema="Article", category="Guides", date="2026-10-19",
    sections=[
        ("The two loops", figure(flow_svg("Customer engagement loop", [("Sources", "web, CRM, POS"), ("Identity", "graph"), ("Profile", "unified"), ("Audience", "RTCDP"), ("Agent proposes", "guardrails"), ("Journey", "AJO"), ("Measure", "CJA")]), "Data loop from sources to audiences, and decision loop from agent proposal to measured outcome.") +
         "<p>The <strong>data loop</strong> moves sources to identity, profile, audience and activation. The <strong>decision loop</strong> has an agent observe profile and journey state, propose an action, let Journey Optimizer execute it and let analytics score the outcome for the next decision.</p>", "plain", "Overview"),
        ("Components", table(["Layer", "Component", "Role"], [("Ingestion", "AEP sources and Edge Network", "Normalise web, app, batch and streaming data into XDM"), ("Identity", "Identity Service", "Link namespaced identifiers into an identity graph"), ("Profile", "Real-Time Customer Profile", "Merge identity-linked fragments under merge policies"), ("Analytics store", "Data Lake and Query Service", "Raw and derived datasets for SQL and CJA"), ("Audience", "Real-Time CDP", "Streaming and batch segments, activation to destinations"), ("Decisioning", "Journey Optimizer", "Event journeys, offers and channel delivery"), ("Agentic", "Planner, scorer and guardrail agents", "Propose and score actions; check policy"), ("Tooling", "MCP servers", "Typed, permissioned bridges from agents to platform APIs"), ("Measurement", "Customer Journey Analytics", "Cross-channel outcomes and reward signal")]), "alt", "Component table"),
        ("Identity and profile", '<ul class="checklist"><li><strong>Namespace hygiene:</strong> register every identifier under a distinct, correctly typed namespace; untyped namespaces are a leading cause of false merges.</li><li><strong>Authentication as an anchor:</strong> a login event is the highest-confidence stitching signal.</li><li><strong>Merge policies:</strong> version them and document field precedence.</li><li><strong>Freshness:</strong> streaming attributes and batch-computed traits update differently; agents must know which is which.</li></ul>', "plain", "Foundations"),
        ("How agents decide", table(["Agent", "Input", "Output", "Constraint"], [("Planner", "Profile state, active journeys, calendar", "Candidate next best action", "Rate-limited per profile per day"), ("Scorer", "Candidate actions, historical CJA outcomes", "Ranked action with confidence", "Must cite the outcome data behind the rank"), ("Guardrail", "Proposed action, consent, frequency caps, brand rules", "Approve, block or escalate", "Runs before any execution call")]) + "<p>Agents reach platform data only through MCP tools such as <code>get_profile</code> or <code>submit_journey_action</code> with least-privilege scopes, never through shared admin credentials. Actions above a defined risk threshold go to a human for approval.</p>", "alt", "Agentic layer"),
        ("Orchestration and feedback", '<p>Journey Optimizer stays the single execution engine so frequency capping, suppression and consent live in one place. Customer Journey Analytics feeds back in two separate ways: <strong>rule feedback</strong> adjusts standing segment definitions on a reviewed cadence, and <strong>reward feedback</strong> informs how the agent ranks actions inside audiences that already qualify. Keeping them separate makes it possible to audit why a customer received a message.</p>', "plain", "Loop"),
        ("Risks to plan for", '<ul class="checklist"><li>Identity graph drift from one misconfigured connector</li><li>Treating stale batch traits as real time</li><li>Agent proposal volume outpacing human review capacity</li><li>Over-broad MCP credentials: scope each server to the minimum</li><li>Consent changes not reaching in-flight agent proposals</li><li>Unstable attribution models making the reward signal noisy</li></ul>', "alt", "Risks"),
        ("Enterprise practices", '<ul class="checklist"><li>Treat agent prompts, MCP tool schemas and guardrail thresholds as versioned code.</li><li>Log every guardrail decision with input state and rationale, retained like marketing message logs.</li><li>Measure agent-ranked actions against rule-based baselines so value is shown, not assumed.</li></ul><p class="small muted">This is an independent reference architecture, not a vendor-issued document. Verify product capabilities against current Adobe documentation before implementation.</p><p class="link-pills"><a href="../lp/aep-architecture-review.html">Request an architecture review</a><a href="../academy/programs/agentic-ai-mcp-track.html">Agentic AI and MCP track</a><a href="what-is-mcp.html">What is MCP?</a></p>', "plain", "Practice"),
    ],
    faqs=[("Should agents send messages directly?", "We recommend not. Agents propose, and Journey Optimizer executes, so consent, suppression and frequency rules stay in one engine.")],
    related=["guides/what-is-mcp.html", "adobe-experience-platform/architecture.html", "services/agentic-ai-mcp.html", "use-cases/abandoned-cart-sports-entertainment.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform"), ("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer"), ("Customer Journey Analytics documentation", f"{EL}/analytics-platform/using/cja-landing"), ("Model Context Protocol", "https://modelcontextprotocol.io/")],
)

# ---------- Use case ----------
SPORTS = use_case(
 "abandoned-cart-sports-entertainment", "Abandoned Cart Re-engagement for Sports and Entertainment | AJO",
 "Win back sports and live-event fans who leave carts: events, loyalty enrichment, an AJO journey, personalised picks, SMS follow-up and measurement.",
 "Abandoned cart re-engagement for sports and entertainment",
 ["sports abandoned cart journey", "ajo cart abandonment fans", "personalised product recommendations journey optimizer", "ticketing merchandise abandoned cart"],
 "A fan who browses or adds merchandise or tickets and leaves is re-engaged by a journey that starts about 30 minutes after abandonment. The email mixes popular products with a few personalised picks based on team affiliation and history, tests subject lines, follows up by SMS if the email goes unopened for 24 hours and exits the fan on purchase.",
 "Sports and entertainment", "browse or cart-add event without purchase, then a 30-minute wait",
 ["Product ID, category and browsing duration from Web SDK events", "Loyalty tier and fan interests on the profile", "Purchase history for recommendations", "Email and SMS consent"],
 [("Browse or cart", "Web SDK"), ("Enrich", "loyalty, team"), ("Wait", "30 min"), ("Email", "popular + picks"), ("No open 24h?", "SMS"), ("Exit on buy", "measure")],
 ["Capture browse and cart events with product ID, category and duration", "Enrich profiles with loyalty tier and team affiliation; build a high-value segment such as fans who browsed several products and are loyalty members", "Start the journey 30 minutes after abandonment", "Email popular products plus a few personalised picks; test two subject-line variants", "Send an SMS reminder if the email is unopened after 24 hours, where SMS consent exists", "Exit fans who purchase"],
 ["Email", "SMS", "On-site recommendation"],
 ["Conversion rate against a holdout group", "Revenue per email", "Lifetime value and unsubscribe rate", "Review A/B results and refine recommendations roughly every two weeks"],
 ["Send SMS only with explicit consent", "Do not offer discounts that conflict with licensing or pricing rules", "Cap total reminders per fan"],
 "case-studies/retail-omnichannel-identity-stitching.html", ["use-cases/abandoned-cart-recovery.html", "use-cases/index.html", "guides/agentic-customer-engagement-architecture.html"])

EXPAND_PAGES = [PROMO, REGION, BOOTCAMP, TRACK_INDEX] + [module_page(i) for i in range(len(MODS))] + [ARCH, SPORTS]
