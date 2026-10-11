"""MarTech stack coverage: hub plus category pages (distinct content, no job counts or partnership claims)."""
from content_cases import pills, WHATSAPP_MSG

STACK_NOTE = ('<p class="note"><strong>How to read this page.</strong> Adobe Experience Cloud is Infinite360\'s deepest area. '
              'For other tools we assess, integrate and train around them in the context of your architecture. Product names belong to their owners; '
              'listing a tool here is not a claim of partnership, certification or endorsement.</p>')

CATS = [
    ("adobe-experience-cloud", "Adobe Experience Cloud", "Adobe",
     ["Adobe Experience Platform (AEP)", "Real-Time CDP", "Adobe Journey Optimizer (AJO)", "Customer Journey Analytics (CJA)", "Adobe Analytics", "Adobe Target", "Adobe Campaign", "Adobe Experience Manager (AEM)", "Marketo Engage", "Adobe Web SDK and Tags"],
     "Core delivery and training area: schemas and identity in AEP, audiences in Real-Time CDP, journeys in AJO, analysis in CJA and Adobe Analytics, and collection through Web SDK and Tags.",
     ["Data model (XDM), identity and consent design", "Datastream and Web SDK implementation", "Audience activation and journey orchestration", "Analytics migration and CJA reporting"],
     ["services/adobe-experience-platform.html", "services/real-time-cdp.html", "services/adobe-journey-optimizer.html", "training/index.html"]),
    ("crm-marketing-automation", "CRM and marketing automation", "CRM",
     ["Salesforce", "Salesforce Marketing Cloud", "Pardot", "HubSpot", "Marketo", "Eloqua", "Braze", "Iterable", "Klaviyo", "Zoho"],
     "These systems own contacts, leads, campaigns and messaging. The architecture question is which system is the source of truth for identity, consent and lifecycle stage, and how events flow to and from the customer data layer.",
     ["Lead and contact data model alignment", "Consent and preference synchronisation", "Event and audience exchange with a CDP", "Lifecycle stage and attribution definitions"],
     ["services/real-time-cdp.html", "topics/real-time-cdp.html", "use-cases/index.html"]),
    ("data-warehouse-cloud", "Data warehouse and cloud", "Cloud data",
     ["Snowflake", "BigQuery", "Databricks", "Google Cloud Platform", "Azure", "AWS", "dbt", "Apache Kafka", "Apache Spark", "Airflow"],
     "Warehouses and pipelines hold the history that personalisation and measurement depend on. We design ingestion, transformation and reverse-ETL patterns that keep the warehouse and the experience layer consistent.",
     ["Batch and streaming ingestion design", "dbt-style transformation and testing", "Warehouse-to-platform activation patterns", "Cost, latency and data-quality controls"],
     ["services/data-engineering.html", "topics/adobe-experience-platform.html", "guides/index.html"]),
    ("analytics-bi", "Analytics and BI", "Analytics",
     ["Google Analytics 4", "Adobe Analytics", "Customer Journey Analytics", "Tableau", "Power BI", "Looker", "Amplitude", "Mixpanel"],
     "Measurement tools only help when definitions are agreed. We map metrics, dimensions and identities across tools, and design dashboards that answer decisions rather than list numbers.",
     ["Measurement plan and tracking specification", "Metric definitions shared across tools", "Dashboard and self-service design", "Validation of tag, event and report accuracy"],
     ["services/customer-journey-analytics.html", "topics/analytics-cja.html", "guides/index.html"]),
    ("cdp-tag-management", "CDP, tag management and integration", "CDP and tags",
     ["Segment", "Tealium", "Hightouch", "mParticle", "Google Tag Manager", "Adobe Tags", "MuleSoft", "Workato", "Zapier", "n8n"],
     "Collection, routing and integration tools decide how clean and fast the data is. We review event design, server-side options, consent enforcement and integration reliability before adding another tool.",
     ["Event schema and data layer design", "Consent-aware tag and server-side setups", "Integration monitoring and retries", "Tool-rationalisation assessments"],
     ["topics/web-sdk-tags.html", "services/index.html", "guides/index.html"]),
    ("personalization-experimentation", "Personalisation and experimentation", "Personalisation",
     ["Adobe Target", "Optimizely", "Dynamic Yield", "AEM", "Contentful", "Sitecore", "Adobe Commerce", "Shopify"],
     "Experience tools execute decisions. We focus on audience quality, test design, content modelling and guardrails so experiments and personalisation can be trusted and measured against a holdout.",
     ["Experiment design and measurement", "Content model and variation governance", "Audience and decisioning inputs", "Performance and flicker controls"],
     ["use-cases/index.html", "solutions/real-time-personalization.html", "topics/journey-optimizer.html"]),
    ("ai-automation", "AI, agentic workflows and automation", "AI",
     ["OpenAI APIs", "Claude and MCP servers", "Python", "LangChain-style frameworks", "n8n", "Zapier", "Vertex AI", "Azure OpenAI"],
     "AI is useful in MarTech when it works on governed data with clear tool boundaries. We design agent and automation patterns with human approval steps, logging and least-privilege access.",
     ["Agent and tool boundaries (including MCP)", "Prompt, evaluation and review workflows", "Access control and audit logging", "Cost and failure handling"],
     ["topics/agentic-ai-mcp.html", "services/index.html", "training/index.html"]),
    ("abm-advertising", "ABM, advertising and engagement", "ABM and ads",
     ["6sense", "Demandbase", "Google Ads", "Meta Ads", "LinkedIn Ads", "Intercom", "Drift", "Twilio"],
     "Paid and engagement platforms depend on audiences passed from first-party data. We design suppression, consent-respecting activation and measurement so spend is not wasted on customers who already converted.",
     ["Audience syndication and suppression", "Consent and sensitive-data rules", "Conversion and offline-event feedback", "Incrementality and holdout design"],
     ["use-cases/index.html", "topics/real-time-cdp.html", "lp/aep-architecture-review.html"]),
]

REGIONS = ["India", "United States", "United Kingdom", "Europe", "Middle East", "Asia-Pacific", "Canada", "Australia"]


def cat_page(c):
    slug, name, short, tools, intro, work, related = c
    return dict(
        path=f"stacks/{slug}.html",
        title=f"{name}: Consulting & Training", desc=f"How Infinite360 approaches {short.lower()} tooling: tools covered, architecture questions, delivery focus and related training.",
        h1=f"{name}: consulting and training", kicker="MarTech stacks", nav=short, schema="Article", category="Stacks", date="2026-10-11",
        keywords=[f"{name.lower()} consultant", f"{short.lower()} martech", f"{name.lower()} training", "martech stack consulting", f"{short.lower()} integration"],
        answer=f"{intro} Infinite360 supports teams working with {', '.join(tools[:4])} and related tools, remotely for clients in any country. Engagements start with an architecture review and can include corporate training.",
        sections=[
            ("Notice", STACK_NOTE),
            ("Tools in this category", '<ul class="chips chips-light">' + "".join(f"<li>{t}</li>" for t in tools) + "</ul>"),
            ("What we work on", '<ul class="checklist">' + "".join(f"<li>{w}</li>" for w in work) + "</ul>"),
            ("Next step", pills(("Request an architecture review", "../lp/aep-architecture-review.html"), ("Corporate training", "../training/index.html"), ("All stacks", "index.html"))),
        ],
        faqs=[(f"Do you support tools outside Adobe in {name.lower()}?", "Yes, as part of an architecture and integration assessment. Adobe Experience Cloud remains the deepest area; we say so when a tool needs a specialist.")],
        related=related,
    )


HUB = dict(
    path="stacks/index.html",
    title="MarTech Stacks We Support: Adobe, CRM, Cloud & AI",
    desc="Infinite360 supports Adobe-centred and multi-vendor MarTech stacks: CRM, data warehouse, analytics, CDP, personalisation and AI tools, for teams in any country.",
    h1="MarTech stacks we support",
    kicker="MarTech stacks", nav="MarTech stacks", schema="CollectionPage", category="Stacks",
    keywords=["martech stack consulting", "martech consultant", "martech training", "adobe and salesforce integration", "martech tools consulting"],
    answer="Infinite360 is stack-aware rather than single-vendor. Adobe Experience Cloud is the deepest specialism; around it we assess and integrate CRM, marketing automation, data warehouse, analytics, CDP, personalisation and AI tools. Work is delivered remotely for teams in any country, and stack decisions follow your architecture, not a product preference.",
    sections=[
        ("Notice", STACK_NOTE),
        ("Stack categories", '<div class="grid-2">' + "".join(f'<a class="card link-card" href="{c[0]}.html"><span class="tag">{c[2]}</span><h3>{c[1]}</h3><p>{", ".join(c[3][:5])} and more.</p></a>' for c in CATS) + "</div>"),
        ("Where we work", "<p>Infinite360 serves teams remotely, including in " + ", ".join(REGIONS) + ". This describes where clients can be served, not physical offices.</p>"),
        ("Start", pills(("Request an architecture review", "../lp/aep-architecture-review.html"), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Do you support every MarTech tool?", "We cover the categories above and assess other tools case by case. We say plainly when a tool needs a specialist partner."),
          ("Are these official partnerships?", "No. Tool names are listed to describe the stacks we work around, not to claim partnerships or certifications.")],
    related=["services/index.html", "training/index.html", "use-cases/index.html"],
)

STACK_PAGES = [HUB] + [cat_page(c) for c in CATS]
