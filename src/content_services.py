"""Consulting service pages (commercial intent: services / consultant / specialist / enterprise)."""

EL = "https://experienceleague.adobe.com/en/docs"

SERVICE_CTA = "Discuss your requirement"

SERVICES = [
    dict(
        path="services/index.html",
        nav="Services",
        title="Adobe MarTech Consulting Services: AEP, RTCDP, AJO, CJA",
        desc="Adobe MarTech consulting: Adobe Experience Platform, Real-Time CDP, Journey Optimizer, CJA, Web SDK, data engineering, Agentic AI and advisory.",
        h1="Adobe MarTech consulting services",
        kicker="Consulting & advisory",
        keywords=["adobe martech consulting", "adobe experience cloud consultant", "martech consulting india", "aep consulting services", "enterprise martech consulting"],
        answer="Infinite360 provides Adobe MarTech consulting across strategy, architecture, implementation and enablement: Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Web SDK and Tags, data engineering, and governed Agentic AI. Engagements range from architecture reviews to hands-on implementation support and team upskilling.",
        schema="CollectionPage",
        sections=[
            ("Services", "@@SERVICE_CARDS@@"),
            ("How we work", """
<ol class="steps">
<li><strong>Strategy</strong> &mdash; clarify business outcomes, use cases and constraints.</li>
<li><strong>Architecture</strong> &mdash; design data, identity, governance and integration.</li>
<li><strong>Implementation</strong> &mdash; build, test and hand over with documentation.</li>
<li><strong>Enablement</strong> &mdash; upskill your team so the platform keeps delivering.</li>
</ol>"""),
            ("Who we work with", "<p>CDOs, CTOs, CIOs, CMOs, MarTech and data leaders, enterprise architects, agencies and system-integrator delivery teams. See the <a href=\"../industries.html\">industries</a> we focus on.</p>"),
        ],
        faqs=[
            ("Do you work with teams outside India?", "Yes. Engagements are delivered remotely; time-zone overlap is agreed at the start of each engagement."),
            ("Can you review an existing Adobe implementation?", "Yes. An architecture review assesses data model, identity, governance, data quality and activation, and returns prioritised recommendations."),
        ],
        related=["adobe-experience-platform/index.html", "training/corporate-training.html", "contact-us.html"],
    ),
    dict(
        path="services/aep-consulting.html",
        title="Adobe Experience Platform (AEP) Consulting & Implementation",
        desc="AEP consulting: architecture, implementation, identity strategy, data ingestion, audits and team enablement from an experienced AEP consultant.",
        h1="Adobe Experience Platform (AEP) consulting",
        kicker="AEP consulting services",
        keywords=["adobe experience platform consulting", "aep consultant", "aep implementation services", "aep specialist", "adobe experience platform consultant india"],
        answer="Our Adobe Experience Platform consulting helps enterprise teams design and implement AEP correctly: use-case prioritisation, XDM data modelling, identity strategy, ingestion pipelines, profiles and audiences, activation, governance and go-live readiness, with knowledge transfer to your team.",
        schema="Service",
        service_type="Adobe Experience Platform consulting",
        sections=[
            ("What the engagement covers", """
<div class="grid-2">
<div class="card"><h3>Architecture review</h3><p>Assess schemas, identity graphs, merge policies, governance and data quality, then prioritise fixes.</p></div>
<div class="card"><h3>Implementation support</h3><p>Hands-on build of sources, Data Prep, datasets, profiles, audiences and destinations.</p></div>
<div class="card"><h3>Identity &amp; Customer 360</h3><p>Design an identity strategy that avoids graph collapse and joins known and anonymous data.</p></div>
<div class="card"><h3>Enablement</h3><p>Runbooks, documentation and team training so you can operate AEP confidently.</p></div>
</div>"""),
            ("Typical deliverables", """
<ul class="checklist">
<li>Use-case backlog with success metrics.</li>
<li>XDM data model and identity strategy document.</li>
<li>Ingestion and activation design with owners.</li>
<li>QA plan, go-live checklist and monitoring approach.</li>
</ul>"""),
            ("Learn the concepts", "<p>Explore the free <a href=\"../adobe-experience-platform/index.html\">AEP guide</a>, including the <a href=\"../adobe-experience-platform/implementation-guide.html\">implementation guide</a> and <a href=\"../adobe-experience-platform/architecture.html\">architecture best practices</a>.</p>"),
        ],
        faqs=[
            ("Do you resell Adobe licences?", "No. We provide independent consulting and training. Licensing is arranged directly with Adobe or your licensing partner."),
        ],
        sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
        related=["services/real-time-cdp.html", "adobe-experience-platform/architecture.html", "contact-us.html"],
    ),
    dict(
        path="services/real-time-cdp.html",
        title="Adobe Real-Time CDP Consulting: Audiences & Activation",
        desc="Real-Time CDP (RTCDP) consulting: Customer 360, identity resolution, audience strategy, destination activation, consent and measurement.",
        h1="Adobe Real-Time CDP (RTCDP) consulting",
        kicker="RTCDP consulting",
        keywords=["adobe real-time cdp consultant", "rtcdp consulting", "real-time cdp implementation", "customer data platform consulting", "rtcdp activation"],
        answer="Adobe Real-Time CDP (RTCDP) is the customer data platform application built on Adobe Experience Platform. Our RTCDP consulting covers Customer 360 design, identity resolution, audience strategy, destination activation, consent enforcement and measurement, so audiences reach the right channels with clean, governed data.",
        schema="Service",
        service_type="Adobe Real-Time CDP consulting",
        sections=[
            ("Where we help", """
<ul>
<li>Audience strategy aligned to campaigns, suppression and lifecycle stages.</li>
<li><a href="../adobe-experience-platform/activation-destinations.html">Destination activation</a> for paid media, email, CRM and data warehouses.</li>
<li><a href="../adobe-experience-platform/identity-service.html">Identity resolution</a> and <a href="../adobe-experience-platform/real-time-customer-profile.html">profile</a> design.</li>
<li>Consent, data usage labels and policy enforcement.</li>
</ul>"""),
            ("Related comparison", "<p>Unsure what you need? Read <a href=\"../guides/aep-vs-real-time-cdp.html\">AEP vs Real-Time CDP</a>.</p>"),
        ],
        faqs=[
            ("Is Real-Time CDP the same as AEP?", "No. RTCDP is an application on top of AEP that adds audience activation and CDP features. See our comparison guide."),
        ],
        sources=[("Real-Time CDP overview", f"{EL}/experience-platform/rtcdp/home")],
        related=["guides/aep-vs-real-time-cdp.html", "adobe-experience-platform/segmentation-audiences.html", "services/adobe-journey-optimizer.html"],
    ),
    dict(
        path="services/adobe-journey-optimizer.html",
        title="Adobe Journey Optimizer (AJO) Consulting & Journey Design",
        desc="Adobe Journey Optimizer consulting: event and audience journeys, decisioning, suppression, frequency rules, testing and measurement.",
        h1="Adobe Journey Optimizer (AJO) consulting",
        kicker="AJO consulting",
        keywords=["adobe journey optimizer consultant", "ajo consulting", "ajo journey design", "adobe journey optimizer implementation", "journey orchestration"],
        answer="Adobe Journey Optimizer (AJO) orchestrates real-time, cross-channel customer journeys using AEP profiles and events. We help design event-triggered and audience-based journeys, configure channels and decisioning, apply suppression and frequency rules, test safely, and measure journey performance.",
        schema="Service",
        service_type="Adobe Journey Optimizer consulting",
        sections=[
            ("How to design an AJO journey", """
<ol class="steps">
<li>Define the trigger (event or audience), goal and exit criteria.</li>
<li>Confirm the event schema, datastream and profile data the journey depends on.</li>
<li>Design paths, waits, conditions and channel actions.</li>
<li>Apply suppression, frequency capping and consent checks.</li>
<li>Test with test profiles, then publish with monitoring.</li>
<li>Measure with journey reporting and Customer Journey Analytics.</li>
</ol>"""),
            ("Prerequisites", "<p>Reliable <a href=\"../adobe-experience-platform/data-ingestion.html\">event ingestion</a>, a clear <a href=\"../adobe-experience-platform/identity-service.html\">identity strategy</a> and validated <a href=\"../adobe-experience-platform/segmentation-audiences.html\">audiences</a>.</p>"),
        ],
        faqs=[
            ("Why is my AJO journey not triggering?", "Check event configuration and schema, datastream routing, profile identity, journey entry conditions, consent and whether the journey is live."),
        ],
        sources=[("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer")],
        related=["services/real-time-cdp.html", "services/customer-journey-analytics.html", "adobe-experience-platform/segmentation-audiences.html"],
    ),
    dict(
        path="services/customer-journey-analytics.html",
        title="Customer Journey Analytics (CJA) Consulting & Migration",
        desc="CJA consulting: connections, data views, cross-channel analysis, Adobe Analytics migration, attribution and executive reporting.",
        h1="Customer Journey Analytics (CJA) consulting",
        kicker="CJA & Adobe Analytics",
        keywords=["customer journey analytics consultant", "cja consulting", "adobe analytics consultant", "cja implementation", "adobe analytics to cja migration"],
        answer="Customer Journey Analytics (CJA) analyses AEP datasets across online and offline channels. We design CJA connections and data views, plan migrations from Adobe Analytics, build cross-channel and attribution workspaces, and set up reporting that executives can trust.",
        schema="Service",
        service_type="Customer Journey Analytics consulting",
        sections=[
            ("What we deliver", """
<ul class="checklist">
<li>Connection design: which datasets, person ID and lookups.</li>
<li>Data views with components, attribution and session settings.</li>
<li>Migration plan from Adobe Analytics, including Web SDK.</li>
<li>Executive dashboards and KPI definitions.</li>
</ul>"""),
            ("Compare first", "<p>Read <a href=\"../guides/cja-vs-adobe-analytics.html\">CJA vs Adobe Analytics</a> to decide what fits your organisation.</p>"),
        ],
        faqs=[
            ("Why is my AEP dataset missing in CJA?", "The dataset must be added to a CJA connection with a valid person ID, and data appears after the connection's ingestion completes."),
        ],
        sources=[("Customer Journey Analytics documentation", f"{EL}/analytics-platform/using/cja-landing")],
        related=["guides/cja-vs-adobe-analytics.html", "services/web-sdk-adobe-tags.html", "adobe-experience-platform/datasets.html"],
    ),
    dict(
        path="services/web-sdk-adobe-tags.html",
        title="Adobe Web SDK & Tags Implementation: Datastreams & Validation",
        desc="Adobe Web SDK and Adobe Tags implementation: data layer, datastreams, consent, Edge Network, migration from legacy libraries and validation.",
        h1="Adobe Web SDK and Adobe Tags implementation",
        kicker="Data collection",
        keywords=["adobe web sdk implementation", "adobe tags consultant", "web sdk migration", "aep web sdk", "alloy js", "datastream setup"],
        answer="Adobe Web SDK (alloy.js) is a single JavaScript library that sends data to the Adobe Edge Network, where a datastream routes it to AEP, Analytics, Target and other services. We design the data layer, configure datastreams and consent, migrate from legacy libraries, and validate events end to end.",
        schema="Service",
        service_type="Adobe Web SDK implementation",
        sections=[
            ("How to implement Web SDK", """
<ol class="steps">
<li>Design an XDM-aligned data layer for pages and interactions.</li>
<li>Create the datastream and map it to AEP datasets and other services.</li>
<li>Deploy Web SDK through Adobe Tags with consent configured.</li>
<li>Send page views and key events; validate with debugging tools and dataset previews.</li>
<li>Decommission legacy libraries in a controlled migration.</li>
</ol>"""),
            ("Related", "<p>Web SDK is a form of <a href=\"../adobe-experience-platform/data-ingestion.html\">streaming ingestion</a> and the usual first step before <a href=\"customer-journey-analytics.html\">CJA</a>.</p>"),
        ],
        faqs=[
            ("Can Web SDK replace AppMeasurement and at.js?", "Web SDK is designed to replace the separate legacy libraries with one library; migration should be planned to protect reporting continuity."),
        ],
        sources=[("Adobe Experience Platform Web SDK", f"{EL}/experience-platform/web-sdk/home")],
        related=["services/customer-journey-analytics.html", "adobe-experience-platform/data-ingestion.html", "services/aep-consulting.html"],
    ),
    dict(
        path="services/agentic-ai-mcp.html",
        title="Agentic AI & MCP Consulting for Enterprise MarTech",
        desc="Agentic AI and Model Context Protocol (MCP) consulting for MarTech: governed AI agents, tool design, data access controls and automation.",
        h1="Agentic AI and MCP for enterprise MarTech",
        kicker="Agentic AI",
        keywords=["agentic ai consulting", "mcp enterprise", "agentic ai martech", "ai agents adobe experience platform", "model context protocol"],
        answer="Agentic AI uses AI models that plan and take actions through tools. The Model Context Protocol (MCP) is an open standard for connecting AI applications to tools and data. We design governed agents for MarTech workflows, with least-privilege tool access, human approval for sensitive actions, logging and evaluation.",
        schema="Service",
        service_type="Agentic AI and MCP consulting",
        sections=[
            ("Example use cases", """
<ul>
<li>Audience and journey QA assistants that check configuration against rules.</li>
<li>Implementation assistants that validate payloads against XDM schemas.</li>
<li>Analytics copilots that answer questions from approved data views.</li>
</ul>"""),
            ("Governance principles", """
<ul class="checklist">
<li>Read-only access by default; write actions require approval.</li>
<li>No secrets or personal data in prompts or logs.</li>
<li>Every tool call logged and reviewable.</li>
<li>Evaluation sets to measure accuracy before rollout.</li>
</ul>"""),
            ("Learn more", "<p>Read <a href=\"../guides/what-is-mcp.html\">What is MCP?</a></p>"),
        ],
        faqs=[
            ("Is MCP an Adobe product?", "No. MCP is an open protocol for connecting AI applications to tools and data. It can be used with enterprise systems where appropriate controls are in place."),
        ],
        related=["guides/what-is-mcp.html", "services/data-engineering.html", "training/index.html"],
    ),
    dict(
        path="services/data-engineering.html",
        title="Customer Data Engineering: ETL, Streaming & Pipelines for AEP",
        desc="Customer data engineering: ETL/ELT, Kafka streaming, Snowflake, BigQuery and Databricks integration, data quality and pipelines for AEP.",
        h1="Data engineering for customer data platforms",
        kicker="Data & cloud",
        keywords=["customer data engineering", "aep data engineer", "etl for adobe experience platform", "kafka to aep", "snowflake aep integration"],
        answer="Customer data engineering builds the pipelines that feed and consume a CDP: batch ETL/ELT from source systems, event streaming, warehouse integration, data quality checks and monitoring. We design pipelines with SQL, Python/PySpark, Kafka, dbt and orchestration tools, and integrate them with Adobe Experience Platform.",
        schema="Service",
        service_type="Customer data engineering",
        sections=[
            ("Capabilities", """
<div class="grid-2">
<div class="card"><h3>Batch pipelines</h3><p>Incremental extracts, transformations and loads with reconciliation.</p></div>
<div class="card"><h3>Streaming</h3><p>Event streaming with Kafka or cloud pub/sub into AEP streaming APIs.</p></div>
<div class="card"><h3>Warehouses</h3><p>Snowflake, BigQuery and Databricks integration patterns.</p></div>
<div class="card"><h3>Data quality</h3><p>Validation, deduplication, identity hygiene and monitoring.</p></div>
</div>"""),
            ("Related guides", "<p>See <a href=\"../adobe-experience-platform/data-ingestion.html\">AEP data ingestion</a> and <a href=\"../adobe-experience-platform/architecture.html\">AEP architecture</a>.</p>"),
        ],
        faqs=[
            ("Should we load everything into AEP?", "No. Load the data your use cases need; keep analytical history in your warehouse where it is cheaper and easier to govern."),
        ],
        related=["adobe-experience-platform/data-ingestion.html", "adobe-experience-platform/architecture.html", "services/agentic-ai-mcp.html"],
    ),
    dict(
        path="services/martech-strategy-advisory.html",
        title="MarTech Strategy & Fractional Advisory: Reviews & Roadmaps",
        desc="MarTech strategy and fractional advisory: Adobe Experience Cloud readiness assessments, architecture reviews, roadmaps and capability plans.",
        h1="MarTech strategy and fractional advisory",
        kicker="Strategy & advisory",
        keywords=["martech strategy consultant", "fractional martech advisor", "martech architecture review", "adobe experience cloud readiness", "digital transformation consultant"],
        answer="MarTech strategy and advisory helps leaders decide what to build, buy and fix. Typical engagements include an Adobe Experience Cloud readiness assessment, an executive architecture review, a prioritised roadmap, and ongoing fractional advisory for programme governance and team capability.",
        schema="Service",
        service_type="MarTech strategy and advisory",
        sections=[
            ("Advisory formats", """
<ul>
<li><strong>Readiness assessment</strong> &mdash; data, identity, consent, skills and use-case maturity.</li>
<li><strong>Architecture review</strong> &mdash; current-state findings and target architecture.</li>
<li><strong>Fractional advisory</strong> &mdash; ongoing senior guidance for programme decisions.</li>
</ul>
<p>Scope, format and pricing are agreed per engagement.</p>"""),
            ("Outcomes we focus on", """
<ul class="checklist">
<li>Clear priorities tied to business outcomes.</li>
<li>Reduced rework from early architecture decisions.</li>
<li>A team that can run the platform independently.</li>
</ul>"""),
        ],
        faqs=[
            ("What is fractional MarTech advisory?", "Part-time senior advisory, typically a set number of days per month, for organisations that need architecture and strategy leadership without a full-time hire."),
        ],
        related=["services/aep-consulting.html", "adobe-experience-platform/architecture.html", "contact-us.html"],
    ),
]
