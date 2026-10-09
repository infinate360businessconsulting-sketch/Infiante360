"""Pages added from the academy, learning-hub and client-engagement source material."""

EL = "https://experienceleague.adobe.com/en/docs"
CAREER_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSctdT6hTSgIeBxok4KgCKC4EISTB8l-S3rKV1NK8SedwGvMZQ/viewform?usp=sharing&ouid=117017541254219120366"

ROLES = [
    ("Software developers", "Move from application development, JavaScript, APIs and integration into AEP development, Web SDK, Adobe I/O, data collection and Journey Optimizer implementation.", "AEP developer · MarTech engineer · Adobe integration developer"),
    ("Data engineers", "Apply ETL, databases, pipelines and cloud data experience to XDM schema design, data ingestion, identity resolution and Real-Time Customer Profile.", "AEP data engineer · customer data engineer · CDP engineer"),
    ("Data analysts", "Build on analytics and reporting experience with customer journeys, attribution, behavioural analysis, dashboards and Customer Journey Analytics.", "CJA analyst · customer analytics specialist · MarTech analyst"),
    ("Cloud &amp; DevOps professionals", "Extend cloud, automation, deployment and API skills into MarTech integrations, data movement, platform operations and automated workflows.", "MarTech integration engineer · platform engineer · automation specialist"),
    ("Architects &amp; technical leads", "Transition from application, cloud or enterprise architecture into customer data architecture, AEP architecture, RTCDP and journey orchestration.", "AEP architect · MarTech architect · customer data architect"),
    ("Business &amp; systems analysts", "Combine requirements, process mapping and stakeholder management with customer journeys, segmentation and personalisation.", "MarTech business analyst · CX analyst · solution consultant"),
    ("Consultants &amp; IT professionals", "Use enterprise delivery experience to design, implement and optimise Adobe-based customer experience ecosystems.", "Adobe MarTech consultant · AEP consultant · technical consultant"),
    ("Project &amp; program managers", "Add MarTech technology understanding to delivery leadership for Adobe transformation and customer data programs.", "MarTech program manager · delivery manager · transformation manager"),
    ("QA, testing &amp; support", "Transfer testing and production-support skills to validating schemas, data flows, tracking, integrations and journeys.", "MarTech QA specialist · implementation specialist · support consultant"),
    ("Sales &amp; presales", "Combine customer-facing experience with MarTech knowledge for discovery, solution design and demonstrations.", "MarTech solution consultant · presales consultant · solution advisor"),
    ("Security &amp; governance", "Connect security, compliance and governance experience with customer data, identity, consent and access requirements.", "MarTech governance specialist · customer data governance consultant"),
    ("Students &amp; freshers", "Build a practical foundation across AEP, XDM, identity, RTCDP, Web SDK, AJO, CJA and Agentic AI with project experience.", "Junior MarTech engineer · AEP associate · MarTech analyst"),
]

role_cards = "".join(
    f'<div class="card"><h3>{r}</h3><p>{d}</p><p class="small"><strong>Target roles:</strong> {t}</p></div>' for r, d, t in ROLES)

HUBS = [
    ("AEP", "AEP learning hub: XDM, datasets, ingestion, Identity, Profile, segmentation, activation and architecture.",
     [("adobe-experience-platform/index.html", "AEP guide"), ("adobe-experience-platform/xdm-schemas.html", "XDM schemas"), ("adobe-experience-platform/identity-service.html", "Identity")]),
    ("Marketo", "Marketo learning hub: lead lifecycle, programs, scoring, CRM alignment, APIs and AEP integration.",
     [("guides/marketo-engage-aep.html", "Marketo Engage and AEP")]),
    ("Agentic AI", "Agents, tools, MCP, governance, customer context and marketing workflows.",
     [("guides/what-is-mcp.html", "What is MCP?"), ("services/agentic-ai-mcp.html", "Agentic AI &amp; MCP")]),
    ("Architecture", "Reference architectures, data flows, integration patterns, governance and production readiness.",
     [("adobe-experience-platform/architecture.html", "AEP architecture"), ("services/engagement-model.html", "Engagement model")]),
    ("Tutorials", "Hands-on implementation tutorials and troubleshooting guides.",
     [("adobe-experience-platform/implementation-guide.html", "AEP implementation"), ("adobe-experience-platform/data-ingestion.html", "Data ingestion"), ("services/web-sdk-adobe-tags.html", "Web SDK")]),
    ("Career", "Pathways from developer, data, analytics, cloud and consulting backgrounds into Adobe MarTech roles.",
     [("training/career-transition.html", "Career transition"), ("adobe-experience-platform/career-path.html", "AEP career path"), ("adobe-experience-platform/interview-questions.html", "Interview questions")]),
    ("Insights", "Deep-dive analysis connecting Adobe MarTech, customer data, analytics and Agentic AI to enterprise implementation.",
     [("guides/aep-vs-real-time-cdp.html", "AEP vs Real-Time CDP"), ("guides/cja-vs-adobe-analytics.html", "CJA vs Adobe Analytics")]),
]

hub_cards = "".join(
    f'<div class="card"><h3>{n}</h3><p>{d}</p><ul>' + "".join(f'<li><a href="../{p}">{l}</a></li>' for p, l in links) + "</ul></div>"
    for n, d, links in HUBS)

MORE = [
    dict(
        path="training/career-transition.html",
        title="MarTech Career Transition: Move Into Adobe AEP Roles",
        desc="How developers, data engineers, analysts, cloud engineers, architects, consultants and freshers can move into Adobe MarTech and AEP roles.",
        h1="Turn your current experience into an Adobe MarTech career",
        kicker="Career transition",
        keywords=["martech career transition", "move into adobe experience platform", "aep career for developers", "data engineer to aep", "career switch to martech"],
        answer="You do not need to restart your career to enter Adobe MarTech. Developers, data engineers, analysts, cloud and DevOps engineers, architects, analysts, consultants, project managers and freshers can add an enterprise MarTech layer — AEP, XDM, identity, RTCDP, Web SDK, AJO, CJA and Agentic AI — on top of the skills they already have.",
        schema="Article",
        sections=[
            ("Don't restart your career. Redirect it.", f'<p>Your existing skills are the foundation. Pick the background closest to yours to see where it maps in Adobe MarTech.</p><div class="grid-3">{role_cards}</div>'),
            ("One program, multiple entry points", """
<ol class="steps">
<li><strong>Your existing skills</strong> &mdash; engineering, data, cloud, analytics, IT, consulting or business.</li>
<li><strong>Build the MarTech layer</strong> &mdash; AEP, XDM, identity, RTCDP, Web SDK, Analytics, AJO and CJA.</li>
<li><strong>Work on enterprise-style projects</strong> &mdash; Customer 360, segmentation, ingestion, journeys, analytics and AI.</li>
<li><strong>Target new roles</strong> &mdash; engineer, consultant, analyst, architect, specialist or manager.</li>
</ol>"""),
            ("Next step", f'<p>Start with a free <a href="{CAREER_FORM}" rel="noopener" target="_blank">career mapping</a>, then review the <a href="index.html">career accelerator</a> and the <a href="../adobe-experience-platform/career-path.html">AEP career path</a>.</p>'),
        ],
        faqs=[
            ("Can a non-Adobe developer move into AEP?", "Yes. JavaScript, API and integration skills transfer directly to Web SDK, data collection and AEP integration work; the new layer is XDM, identity and the Adobe application model."),
            ("Can data engineers move into Adobe MarTech?", "Yes. ETL, SQL and pipeline experience maps closely to AEP schema design, ingestion, identity and profile work."),
        ],
        related=["training/index.html", "adobe-experience-platform/career-path.html", "adobe-experience-platform/interview-questions.html"],
    ),
    dict(
        path="services/engagement-model.html",
        title="MarTech Audit & Transformation Engagement Model",
        desc="How Infinite360 engagements run: discover, diagnose, strategize, enable, build, implement, augment and scale — with a client audit and 30/60/90-day plan.",
        h1="Our engagement model: from audit to scale",
        kicker="How we engage",
        keywords=["martech audit", "digital transformation engagement model", "martech maturity assessment", "30 60 90 day martech plan", "adobe transformation roadmap"],
        answer="Infinite360 engagements start with a structured audit of your digital experience, data, MarTech, personalisation, AI, engineering and skills. Findings become a prioritised 30/60/90-day plan and roadmap, followed by enablement, proofs of concept, implementation support, optional specialist capacity and knowledge transfer so results scale.",
        schema="Service",
        service_type="MarTech audit and transformation",
        sections=[
            ("Eight-step engagement model", """
<ol class="steps">
<li><strong>Discover</strong> &mdash; audit the website, digital ecosystem, MarTech stack and customer journeys.</li>
<li><strong>Diagnose</strong> &mdash; convert findings into prioritised business, data, experience and engineering gaps.</li>
<li><strong>Strategize</strong> &mdash; create a 30/60/90-day plan and a longer-term transformation vision.</li>
<li><strong>Enable</strong> &mdash; train teams with role-based, hands-on, real-world use cases.</li>
<li><strong>Build</strong> &mdash; develop proofs of concept, accelerators, integrations and implementation patterns.</li>
<li><strong>Implement</strong> &mdash; provide architecture, engineering, testing, governance and delivery support.</li>
<li><strong>Augment</strong> &mdash; add specialist engineers or architects where capacity is needed.</li>
<li><strong>Scale</strong> &mdash; transfer knowledge, establish reusable standards and keep optimising.</li>
</ol>"""),
            ("What the audit covers", """
<div class="table-wrap"><table>
<thead><tr><th>Area</th><th>What we assess</th><th>Typical action</th></tr></thead>
<tbody>
<tr><td>Digital experience</td><td>Web/app journeys, UX, content, conversion paths</td><td>Experience optimisation and measurement</td></tr>
<tr><td>Data &amp; analytics</td><td>Collection, quality, identity, reporting, journey visibility</td><td>Analytics and data foundation</td></tr>
<tr><td>MarTech</td><td>Adobe/CDP/journey/personalisation maturity and integrations</td><td>MarTech roadmap and implementation</td></tr>
<tr><td>Personalisation</td><td>Audiences, segmentation, targeting, orchestration</td><td>Real-time personalisation</td></tr>
<tr><td>AI</td><td>Automation, intelligence and decision support</td><td>Governed AI / agentic proofs of concept</td></tr>
<tr><td>Engineering</td><td>Architecture, APIs, cloud, DevOps, delivery bottlenecks</td><td>Engineering modernisation</td></tr>
<tr><td>People &amp; skills</td><td>Current capabilities and gaps</td><td>Corporate academy and mentoring</td></tr>
</tbody></table></div>"""),
            ("Audit deliverables", """
<ul class="checklist cols-2">
<li>Executive summary of the most important findings</li>
<li>Current-state maturity: people, process, technology, data, governance</li>
<li>Opportunity map: quick wins, medium-term and strategic initiatives</li>
<li>Platform recommendations only where the audit justifies them</li>
<li>Target-state architecture from data to measurement</li>
<li>30/60/90-day action plan and 12-month roadmap</li>
<li>Capability-building plan</li>
<li>Implementation and proof-of-concept backlog</li>
<li>KPIs and measurement framework</li>
</ul>"""),
        ],
        faqs=[
            ("Do you recommend specific platforms?", "Only where the audit findings justify them. Recommendations are tied to use cases, current-state maturity and measurable outcomes."),
        ],
        related=["services/martech-strategy-advisory.html", "services/staff-augmentation.html", "training/corporate-training.html"],
    ),
    dict(
        path="services/staff-augmentation.html",
        title="MarTech Staff Augmentation: AEP Engineers & Architects",
        desc="Flexible MarTech delivery capacity: AEP and Adobe engineers, analytics, data and integration engineers, QA specialists, technical leads and architects.",
        h1="MarTech staff augmentation",
        kicker="Delivery capacity",
        keywords=["martech staff augmentation", "aep engineers for hire", "adobe consultants contract", "martech architect contract", "analytics implementation engineer"],
        answer="Staff augmentation adds specialised MarTech capacity to your existing team for a defined period: Adobe and AEP engineers, analytics implementation engineers, data and integration engineers, QA and validation specialists, technical leads and solution architects, working inside your delivery process.",
        schema="Service",
        service_type="MarTech staff augmentation",
        sections=[
            ("Profiles available", """
<ul class="cols-2">
<li>AEP / Adobe engineers</li>
<li>Analytics implementation engineers</li>
<li>MarTech engineers</li>
<li>Data and integration engineers</li>
<li>QA and validation specialists</li>
<li>Technical leads</li>
<li>Solution and MarTech architects</li>
</ul>
<p>Availability depends on timing and skill mix; we confirm profiles before any engagement starts.</p>"""),
            ("How it works", """
<ol class="steps">
<li>Agree scope, skills, duration and time-zone overlap.</li>
<li>Review profiles and run your own interviews.</li>
<li>Onboard into your tools, standards and governance.</li>
<li>Regular check-ins, with knowledge transfer before roll-off.</li>
</ol>"""),
        ],
        faqs=[
            ("Can augmented staff work in our time zone?", "Overlap hours are agreed at the start of each engagement based on your team's working hours."),
        ],
        related=["services/engagement-model.html", "services/aep-consulting.html", "contact-us.html"],
    ),
    dict(
        path="learn/index.html",
        nav="Learn",
        title="Infinite360 Learning Hubs: AEP, Marketo, Agentic AI & More",
        desc="Infinite360 learning hubs for AEP, Marketo, Agentic AI, architecture, tutorials, careers and insights — practical guides built around implementation.",
        h1="Learning hubs",
        kicker="Learn",
        keywords=["adobe martech learning hub", "aep tutorials", "marketo learning", "agentic ai learning", "martech architecture guides"],
        answer="The Infinite360 learning hubs organise free guides by topic: Adobe Experience Platform, Marketo, Agentic AI, architecture, hands-on tutorials, careers and insights. Every guide is written around implementation: what it is, why it matters, how to apply it, common mistakes and where to go next.",
        schema="CollectionPage",
        sections=[
            ("Hubs", f'<div class="grid-3">{hub_cards}</div>'),
            ("Our article standard", """
<p>Every guide aims to cover:</p>
<ul class="checklist cols-2">
<li>What changed or what it is</li>
<li>Why it matters</li>
<li>Implementation view</li>
<li>Common mistakes</li>
<li>Hands-on exercise</li>
<li>Related academy module</li>
<li>Sources</li>
</ul>"""),
            ("News, podcasts and daily intelligence", '<p>Curated MarTech news and podcast summaries with practitioner analysis are published only after editorial review. Until then, follow updates on <a href="https://linkedin.com/in/pavanbabu1" rel="noopener" target="_blank">LinkedIn</a> and <a href="https://www.youtube.com/@Infiante360TechAcademy" rel="noopener" target="_blank">YouTube</a>.</p>'),
        ],
        faqs=[],
        related=["adobe-experience-platform/index.html", "guides/marketo-engage-aep.html", "training/index.html"],
    ),
    dict(
        path="guides/marketo-engage-aep.html",
        title="Marketo Engage and AEP: Lead Lifecycle, Scoring & Integration",
        desc="How Marketo Engage handles lead lifecycle, programs, scoring and CRM sync, and how it connects with Adobe Experience Platform audiences and data.",
        h1="Marketo Engage and Adobe Experience Platform",
        kicker="Marketo hub",
        keywords=["marketo engage", "marketo aep integration", "marketo lead scoring", "marketo lead lifecycle", "marketo crm sync"],
        answer="Marketo Engage is Adobe's B2B marketing automation application for lead management, programs, scoring, email and CRM alignment. Connected with Adobe Experience Platform, Marketo data can feed AEP profiles and AEP audiences can be activated to Marketo, so B2B lead nurture uses the same governed customer data as other channels.",
        schema="Article",
        sections=[
            ("Why it matters", "<p>B2B teams often run lead management in Marketo while customer data lives elsewhere. Connecting the two avoids conflicting definitions of a lead, duplicate scoring logic and audiences that drift between systems.</p>"),
            ("Implementation view", """
<ol class="steps">
<li><strong>Lead lifecycle</strong> &mdash; agree stage definitions (for example known, engaged, MQL, SQL) with sales before building anything.</li>
<li><strong>Programs</strong> &mdash; organise campaigns into programs with consistent channels, statuses and naming.</li>
<li><strong>Scoring</strong> &mdash; separate behaviour and fit scoring; document every rule and its owner.</li>
<li><strong>CRM alignment</strong> &mdash; map fields and sync rules with the CRM so ownership is clear.</li>
<li><strong>AEP integration</strong> &mdash; bring Marketo data into AEP through the Marketo source connector and activate AEP audiences to Marketo where your licence supports it.</li>
<li><strong>APIs</strong> &mdash; use the Marketo REST API for integrations, respecting rate limits and secure credential storage.</li>
</ol>"""),
            ("Common mistakes", """
<ul class="checklist">
<li>Scoring models nobody owns or reviews.</li>
<li>Different MQL definitions in Marketo, CRM and reporting.</li>
<li>Syncing every field instead of the fields use cases need.</li>
<li>API credentials stored in scripts or shared documents.</li>
</ul>"""),
            ("Hands-on exercise", "<p>Draw your current lead lifecycle on one page: stages, entry rules, owners and the system of record for each field. Mark where Marketo, the CRM and AEP disagree &mdash; that list is your integration backlog.</p>"),
            ("Related academy module", '<p>Marketo and B2B topics connect with the <a href="../training/index.html">career accelerator</a> and the <a href="../adobe-experience-platform/data-ingestion.html">AEP data ingestion</a> guide.</p>'),
        ],
        faqs=[
            ("Is Marketo part of Adobe Experience Platform?", "No. Marketo Engage is a separate Adobe application. It can be integrated with AEP through source connectors and destinations, depending on licensing."),
        ],
        sources=[("Marketo Engage documentation", "https://experienceleague.adobe.com/en/docs/marketo/using/home"), ("AEP data ingestion overview", f"{EL}/experience-platform/ingestion/home")],
        related=["learn/index.html", "adobe-experience-platform/data-ingestion.html", "services/aep-consulting.html"],
    ),
]
