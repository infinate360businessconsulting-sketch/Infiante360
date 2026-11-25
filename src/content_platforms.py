"""Five approved consulting pages: Snowflake, BigQuery, Databricks, Kafka streaming, Enterprise Architecture.
Approved by the owner on 2026-11-25. No client names, results, partner status or vendor logos. Diagrams are original (assets/visuals/).
Reference patterns are illustrative; product capabilities must be checked against vendor documentation (linked in Sources).
"""
EL = "https://experienceleague.adobe.com/en/docs/experience-platform"
IMG = "assets/visuals/{s}/"


def _cards(items):
    return '<div class="grid-2">' + "".join(f'<div class="card"><h3>{h}</h3><p>{t}</p></div>' for h, t in items) + "</div>"


def _ul(items):
    return '<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def _ol(items):
    return '<ol class="steps">' + "".join(f"<li><strong>{h}</strong> &mdash; {t}</li>" for h, t in items) + "</ol>"


def _fig(slug, alt, cap):
    return (f'<figure class="diagram"><picture><img src="../{IMG.format(s=slug)}hero-800.webp" srcset="../{IMG.format(s=slug)}hero-800.webp 800w, ../{IMG.format(s=slug)}hero.webp 1600w" '
            f'sizes="(max-width: 900px) 100vw, 900px" width="1600" height="900" loading="lazy" alt="{alt}"></picture>'
            f'<figcaption>{cap} <a href="../{IMG.format(s=slug)}diagram.svg">Open the full diagram (SVG)</a>.</figcaption></figure>')


def _sources(links):
    return "<ul>" + "".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t, u in links) + "</ul>"


ENGAGE = [("Architecture review", "A short, fixed-scope assessment of the current design with prioritised recommendations."),
          ("Design and build", "Target architecture, implementation and handover with your engineers."),
          ("Advisory retainer", "Periodic design reviews and decision support while your team delivers."),
          ("Team enablement", "Hands-on working sessions so your team can run and extend the solution.")]
DELIV = ["Current-state findings and a risk register", "Target architecture and decision records", "Data model and integration specification",
         "Delivery plan with quality gates", "Runbook, monitoring checklist and handover session"]
NOTE = '<p class="small muted">Reference patterns on this page are illustrative and are not descriptions of a client engagement. Infiante360 is independent and not affiliated with or endorsed by Adobe, Snowflake, Google, Databricks or the Apache Software Foundation. Product names belong to their owners.</p>'


def page(path, slug, title, desc, h1, kicker, nav, keywords, answer, stype, intro, challenges, caps, arch_text, method, usecases, governance, security, faqs, sources, related, adobe_link):
    sections = [
        ("Who this is for", f"<p>{intro}</p>"),
        ("Challenges we are asked to solve", _ul(challenges), "alt"),
        ("Capabilities", _cards(caps)),
        ("Reference architecture", f"<p>{arch_text}</p>" + _fig(slug, f"{title} diagram", f"Reference architecture: {h1}."), "plain", "Architecture"),
        ("Methodology", _ol(method), "alt"),
        ("Use cases", _cards(usecases)),
        ("Governance and security", f"<h3>Governance</h3>{_ul(governance)}<h3>Security</h3>{_ul(security)}", "alt"),
        ("Engagement models", _cards(ENGAGE)),
        ("Deliverables", _ul(DELIV), "alt"),
        ("Where this connects to Adobe Experience Platform", f"<p>{adobe_link}</p>"),
        ("Sources", _sources(sources) + NOTE, "alt"),
        ("Start a conversation", '<p>Tell us your current platform, the decision you need to make and your timeline. We reply with a proposed scope before any commitment.</p><p class="cta-row"><a class="btn btn-primary" href="../contact-us.html">Discuss your requirement</a></p>'),
    ]
    return dict(path=path, nav=nav, title=title, desc=desc, h1=h1, kicker=kicker, keywords=keywords, answer=answer, schema="Service",
                service_type=stype, sections=sections, faqs=faqs, related=related, category="Services",
                og_image=f"visuals/{slug}/og.png", og_alt=f"{h1}: reference architecture")


A = "adobe-experience-platform/"
PLATFORM_PAGES = [
    page("services/snowflake-martech-integration.html", "snowflake-aep-integration-architecture",
         "Snowflake Consulting for MarTech and Adobe Experience Platform",
         "Snowflake consulting for customer data: warehouse design, governance and integration with Adobe Experience Platform, with an original reference architecture.",
         "Snowflake consulting for MarTech and customer data", "Data & cloud", "Snowflake integration",
         ["snowflake consulting", "snowflake aep integration", "snowflake customer 360", "snowflake data sharing martech", "snowflake for marketing data"],
         "Snowflake consulting from Infiante360 designs how customer and marketing data is modelled, governed and shared in Snowflake, and how it connects to Adobe Experience Platform for profiles, audiences and journeys. We start with ownership of each attribute, then design schemas, access policies and integration patterns.",
         "Snowflake data warehousing and Adobe MarTech",
         "Data leaders and architects who keep customer data in Snowflake and need it to work with Adobe Experience Platform without duplicating every table or losing governance.",
         ["Two copies of customer data that disagree, with no declared source of truth", "Marketing teams waiting on engineering for every new audience", "Warehouse credits growing faster than the value of the queries", "Consent and retention rules enforced in one system but not the other", "Identity keys that differ between the warehouse and the CDP"],
         [("Data modelling", "Curated customer, event and consent schemas that map cleanly to XDM."), ("Access and governance", "Role-based access, masking and tagging for personal data."),
          ("Integration patterns", "Batch and incremental loads, and warehouse-to-AEP flows chosen per use case."), ("Cost control", "Warehouse sizing, query review and workload separation.")],
         "The pattern keeps raw and curated data in Snowflake under role-based policies, loads only what activation needs into Adobe Experience Platform as XDM datasets, and returns outcomes to the warehouse for analysis. Which connector or API fits depends on volume, latency and product edition; confirm in the vendor documentation.",
         [("Assess", "map sources, owners, volumes and current spend."), ("Model", "define curated schemas, keys and consent attributes."), ("Integrate", "build and test the load paths with reconciliation checks."), ("Operate", "monitoring, cost review and handover.")],
         [("Customer 360 in the warehouse", "Unify CRM, commerce and event data, then expose a governed subset to activation."), ("Audience prototyping", "Test segment logic in SQL before building it in the CDP."),
          ("Closed-loop measurement", "Return journey and campaign outcomes to Snowflake for analysis."), ("Data sharing", "Share governed datasets with partners without copying files.")],
         ["Declare the source of truth per attribute and record it", "Tag personal data and apply masking policies", "Keep retention rules identical on both sides", "Reconcile row counts and keys after every load"],
         ["Least-privilege roles and separation of duties", "Network and authentication controls set by your security team", "Audit access to personal data", "No credentials in code or documentation"],
         [("Do we need Snowflake if we already use Adobe Experience Platform?", "Not necessarily. Many teams keep analytical history in a warehouse because it is cheaper and easier to govern, and load only activation data into the CDP. The right split depends on your use cases."),
          ("Can you review our current Snowflake design?", "Yes. An architecture review covers modelling, access, cost and the integration with your Adobe stack, and returns prioritised recommendations."),
          ("Do you resell Snowflake?", "No. Infiante360 is an independent consulting firm and is not a Snowflake reseller or partner.")],
         [("Snowflake documentation", "https://docs.snowflake.com/"), ("Adobe Experience Platform sources and datasets", EL + "/sources/home"), ("XDM system overview", EL + "/xdm/home")],
         [A + "data-ingestion.html", "services/data-engineering.html", "services/aep-consulting.html"],
         'See the guides on <a href="../adobe-experience-platform/data-ingestion.html">AEP data ingestion</a> and <a href="../adobe-experience-platform/architecture.html">AEP architecture</a>, and the broader <a href="data-engineering.html">customer data engineering</a> service.'),
    page("services/bigquery-martech-integration.html", "bigquery-martech-analytics-architecture",
         "BigQuery Consulting for MarTech Analytics and Customer Data",
         "BigQuery consulting for marketing analytics: event modelling, cost control, governance and activation, with an original layered reference architecture.",
         "BigQuery consulting for marketing analytics", "Data & cloud", "BigQuery integration",
         ["bigquery consulting", "bigquery martech", "bigquery marketing analytics", "ga4 bigquery export", "bigquery customer data platform"],
         "BigQuery consulting from Infiante360 covers event collection, partitioned data models, governance and cost control on Google Cloud, plus how the results feed audiences, dashboards and Adobe Experience Platform. We design for query cost and clarity first, then connect consumption tools.",
         "BigQuery analytics and customer data modelling",
         "Analytics and data teams on Google Cloud who need marketing event data modelled, governed and affordable to query.",
         ["Event tables that are expensive to scan and slow to explain", "Metrics defined differently in every dashboard", "Raw exports with no quality tests", "Column-level access to personal data not enforced", "Unclear hand-off between analytics and activation"],
         [("Event modelling", "Partitioned and clustered fact tables with documented grain."), ("Transformation layer", "SQL or dbt models with tests and lineage."),
          ("Governance", "IAM, policy tags and column-level controls for personal data."), ("Cost management", "Query review, slot and storage choices, and budget alerts.")],
         "Events arrive through SDK collection, server-side tagging or batch exports into raw tables, are modelled into partitioned facts, governed by IAM and policy tags, then consumed by BI, audience tables and machine-learning features. Partitioning and clustering choices decide both speed and cost.",
         [("Inventory", "list event sources, schemas and current query cost."), ("Model", "define grain, keys and partitioning."), ("Test", "add data quality and reconciliation checks."), ("Hand over", "document metrics and train analysts.")],
         [("Web and app analytics", "Model first-party events for analysis beyond standard reports."), ("Audience tables", "Build reusable audience logic in SQL for downstream activation."),
          ("Attribution inputs", "Prepare consistent touchpoint data for measurement work."), ("Feature tables", "Provide governed features for propensity and lifetime-value models.")],
         ["Document metric definitions in one place", "Add automated data quality tests to every model", "Tag personal data with policy tags", "Review cost and access quarterly"],
         ["Least-privilege IAM roles", "Column-level security for personal data", "Audit logs reviewed by your security team", "Secrets held in a managed store, never in code"],
         [("Is BigQuery a replacement for Adobe Analytics or CJA?", "No. They answer different needs. BigQuery is a warehouse for modelling and analysis; Adobe products provide reporting and activation. Many teams use both."),
          ("Can you reduce our BigQuery cost?", "We review partitioning, clustering and query patterns and recommend changes. We do not promise a specific saving before seeing your workload."),
          ("Do you work with the GA4 export?", "Yes, as one source among others. We model it alongside first-party and CRM data.")],
         [("BigQuery documentation", "https://cloud.google.com/bigquery/docs"), ("Adobe Experience Platform Query Service", EL + "/query-service/home"), ("Customer Journey Analytics", "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-landing")],
         [A + "data-ingestion.html", "services/customer-journey-analytics.html", "services/data-engineering.html"],
         'BigQuery often sits beside <a href="customer-journey-analytics.html">Customer Journey Analytics</a> and <a href="aep-consulting.html">Adobe Experience Platform</a>; we design which system holds which data and why.'),
    page("services/databricks-martech-integration.html", "databricks-lakehouse-customer-data-architecture",
         "Databricks Consulting for Customer Data and AI Pipelines",
         "Databricks consulting for customer data: lakehouse design, bronze-silver-gold pipelines, governance and activation, with an original reference architecture.",
         "Databricks consulting for customer data pipelines", "Data & cloud", "Databricks integration",
         ["databricks consulting", "databricks lakehouse customer data", "databricks medallion architecture", "databricks aep integration", "databricks identity resolution"],
         "Databricks consulting from Infiante360 designs lakehouse pipelines for customer data: ingestion, bronze, silver and gold layers, identity keys, governance and feature tables. We then define how curated outputs reach Adobe Experience Platform and downstream models, with ownership and quality checks at every layer.",
         "Databricks lakehouse engineering for customer data",
         "Data engineering and ML teams who need customer data pipelines that are reliable, governed and ready for both activation and modelling.",
         ["Pipelines that fail silently and are fixed by hand", "No agreed rules for deduplication and identity keys", "Notebooks in production with no tests", "Features recomputed differently by each team", "Access control that stops at the workspace"],
         [("Pipeline design", "Batch and streaming ingestion into layered tables."), ("Identity and entity rules", "Documented match rules and survivorship for customer entities."),
          ("Governance", "Catalog structure, lineage and access policies."), ("ML readiness", "Feature tables and reproducible training data.")],
         "Data lands in append-only bronze tables, is cleansed and deduplicated in silver with identity keys resolved, and is published as gold tables for customer features, audiences and metrics. A governing catalog spans every layer for lineage, access and audit.",
         [("Discover", "map sources, volumes and existing jobs."), ("Design", "define layers, keys and ownership."), ("Build", "implement with tests and monitoring."), ("Operate", "cost review, incident runbook and handover.")],
         [("Customer entity resolution", "Build and test match rules before results reach the CDP."), ("Feature engineering", "Shared, versioned features for propensity and churn models."),
          ("Streaming enrichment", "Combine events with reference data close to real time."), ("Data products", "Publish owned, documented gold tables to other teams.")],
         ["Assign an owner to every gold table", "Version match rules and review changes", "Track lineage from source to activation", "Test data quality before publishing"],
         ["Least-privilege access through the catalog", "Separate development, test and production workspaces", "Audit logs reviewed regularly", "No secrets in notebooks"],
         [("Do we need Databricks or a warehouse?", "It depends on your workloads. Heavy transformation and machine learning favour a lakehouse; SQL-centred analytics may suit a warehouse. We compare options against your use cases."),
          ("Can Databricks feed Adobe Experience Platform?", "Yes, through supported ingestion paths. The right one depends on volume and latency; we confirm against Adobe documentation."),
          ("Do you provide Databricks training?", "Training is offered separately through the academy where a course exists; this page covers consulting.")],
         [("Databricks documentation", "https://docs.databricks.com/"), ("Adobe Experience Platform data ingestion", EL + "/ingestion/home"), ("Identity service", EL + "/identity/home")],
         [A + "data-ingestion.html", "services/data-engineering.html", "services/agentic-ai-mcp.html"],
         'Curated gold tables can be loaded to Adobe Experience Platform for activation; see <a href="../adobe-experience-platform/data-ingestion.html">AEP data ingestion</a> and <a href="data-engineering.html">customer data engineering</a>.'),
    page("services/kafka-streaming-customer-data.html", "kafka-real-time-streaming-architecture",
         "Kafka Consulting for Real-Time Customer Data Streaming",
         "Kafka consulting for real-time customer data: topic and schema design, stream processing, delivery guarantees and Adobe integration, with a reference diagram.",
         "Kafka consulting for real-time customer data", "Data & cloud", "Kafka streaming",
         ["kafka consulting", "kafka real-time streaming", "kafka to aep", "kafka schema registry design", "event streaming customer data"],
         "Kafka consulting from Infiante360 designs the event backbone behind real-time personalization and analytics: topics, partitions, schemas, retention, processing and consumers. We make delivery guarantees, ordering and schema changes explicit, then connect streams to Adobe Experience Platform where real-time use cases need them.",
         "Apache Kafka event streaming for customer data",
         "Platform and data engineers who must move customer events reliably between applications, the CDP, the warehouse and monitoring.",
         ["Duplicate or missing events after retries and outages", "Schema changes that break consumers", "Topic and partition choices made once and never revisited", "No replay plan when downstream systems fail", "Real-time use cases that do not need real time, adding cost"],
         [("Topic and schema design", "Naming, partitioning keys, compatibility rules and a schema registry."), ("Processing", "Validation, enrichment and dead-letter handling."),
          ("Reliability", "Delivery semantics, idempotent consumers and replay procedures."), ("Observability", "Lag, throughput and error monitoring with alert thresholds.")],
         "Producers publish events to governed topics. The platform enforces schemas and retention, stream processing validates and enriches, and consumers include the customer data platform, the warehouse or lake, and alerting. Delivery guarantees and ordering are designed per topic.",
         [("Qualify", "decide which use cases truly need streaming."), ("Design", "topics, keys, schemas and retention."), ("Build", "producers, processors and consumers with failure tests."), ("Run", "monitoring, capacity review and runbooks.")],
         [("Real-time profile updates", "Send qualifying events to the CDP for immediate use."), ("Event-triggered journeys", "Start journeys from validated business events."),
          ("Operational alerting", "Detect pipeline lag and malformed events early."), ("Warehouse and lake feeds", "Land the same events for analysis without a second integration.")],
         ["Compatibility rules enforced in the schema registry", "Owners named for every topic", "Retention aligned with privacy requirements", "Dead-letter topics reviewed on a schedule"],
         ["Authentication and authorization on clusters and topics", "Encryption in transit and at rest per your policy", "Personal data minimised in event payloads", "No credentials in code or configuration files"],
         [("Do we need Kafka for real-time personalization?", "Not always. If a use case tolerates minutes of delay, batch or micro-batch may be simpler. We test the real latency requirement first."),
          ("Managed Kafka or self-managed?", "That is a cost, skills and compliance decision. We compare options against your constraints."),
          ("Can Kafka send data to Adobe Experience Platform?", "Yes, through supported streaming ingestion paths. We confirm the current options in Adobe documentation before design.")],
         [("Apache Kafka documentation", "https://kafka.apache.org/documentation/"), ("AEP streaming ingestion", EL + "/ingestion/home"), ("Adobe Experience Platform Web SDK", EL + "/web-sdk/home")],
         [A + "data-ingestion.html", "services/data-engineering.html", "services/adobe-journey-optimizer.html"],
         'Streams commonly feed <a href="../adobe-experience-platform/data-ingestion.html">AEP data ingestion</a> and trigger <a href="adobe-journey-optimizer.html">Adobe Journey Optimizer</a> journeys when events qualify.'),
    page("services/enterprise-architecture-consulting.html", "enterprise-architecture-digital-transformation-roadmap",
         "Enterprise Architecture and Digital Transformation Consulting",
         "Enterprise architecture consulting for MarTech and customer data: current-state review, target design, governance and a phased transformation roadmap.",
         "Enterprise architecture and digital transformation consulting", "Strategy & architecture", "Enterprise architecture",
         ["enterprise architecture consulting", "digital transformation consulting", "martech architecture review", "customer data architecture roadmap", "enterprise martech strategy"],
         "Enterprise architecture consulting from Infiante360 maps your current MarTech and customer data landscape, designs a governed target state, and sequences a phased roadmap. Each phase ends with a decision your sponsor can approve, change or stop, so transformation stays tied to business outcomes.",
         "Enterprise architecture and digital transformation",
         "CIOs, CTOs, CDOs and enterprise architects who need a clear, defensible path from a fragmented MarTech and data estate to a governed target state.",
         ["Overlapping tools with unclear ownership", "Customer data spread across systems with no agreed model", "Transformation programmes without measurable decision points", "Integration decisions made project by project", "Governance written down but not applied"],
         [("Current-state assessment", "Capability, data and integration maps with risks."), ("Target architecture", "Principles, patterns and decision records."),
          ("Roadmap and sequencing", "Prioritised phases with dependencies and quality gates."), ("Governance model", "Ownership, standards and review cadence.")],
         "The roadmap moves through four phases: assess, design, plan and deliver. Every phase has named outputs and a decision point, and the target architecture is expressed as principles and patterns your teams can apply, not a one-off diagram.",
         [("Assess", "interview stakeholders and map systems, data and spend."), ("Design", "agree principles and the target architecture."), ("Plan", "sequence work into releasable increments."), ("Deliver", "support delivery with design reviews and handover.")],
         [("MarTech rationalisation", "Decide which platforms to keep, consolidate or retire."), ("Customer 360 programme", "Define the data model, identity approach and ownership."),
          ("Cloud and data modernisation", "Sequence migrations around business priorities."), ("AI readiness", "Set data, governance and integration foundations for AI use cases.")],
         ["Architecture decision records kept current", "Named owner for every domain and dataset", "Standards reviewed on a fixed cadence", "Exceptions recorded with an expiry date"],
         ["Security and privacy requirements captured as design inputs", "Consent and retention rules designed across systems", "Third-party access reviewed", "Your security team approves the target design"],
         [("How long does an architecture review take?", "It depends on scope and access. We agree a fixed scope and timeline in writing before starting."),
          ("Do you recommend specific vendors?", "We recommend against your requirements and constraints, and we are independent of the vendors named on this site."),
          ("Can you work with our delivery partner?", "Yes. We can provide design authority and reviews alongside your existing delivery team.")],
         [("Adobe Experience Platform documentation", EL + "/landing/home"), ("Adobe Experience Platform architecture overview", EL + "/landing/home"), ("TOGAF Standard (The Open Group)", "https://www.opengroup.org/togaf")],
         [A + "architecture.html", "services/martech-strategy-advisory.html", "services/aep-consulting.html"],
         'See the guide to <a href="../adobe-experience-platform/architecture.html">AEP architecture</a> and the <a href="martech-strategy-advisory.html">MarTech strategy advisory</a> service.'),
]
