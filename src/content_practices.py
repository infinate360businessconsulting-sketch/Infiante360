"""Practices overview page: how Infiante360 organises its consulting, in a hero / services / practices / insights / next-step layout.
Original text. Links to existing service and guide pages only. No partner status, certification counts, project counts or client claims."""
def _l(items):
    return '<ul class="checklist">' + "".join(f'<li>{i}</li>' for i in items) + "</ul>"

def _prac(title, text, url):
    return f'<h3>{title}</h3><p>{text} <a href="{url}">Learn more</a></p>'

PRACTICES_PAGE = dict(
    path="practices/index.html", nav="Practices",
    title="Our Practices: Customer Data, Journeys, AI | Infiante360",
    desc="How Infiante360 organises its Adobe MarTech consulting: identity, personalisation, journeys, collection, data engineering and governed AI. See each practice.",
    h1="Practices built for enterprise reality", kicker="Practices",
    keywords=["martech consulting practices", "adobe experience cloud practices", "customer data and identity", "journey orchestration consulting", "agentic ai martech"],
    schema="WebPage", category="Company",
    answer="Infiante360 organises its Adobe MarTech consulting into six practices: customer data and identity, real-time personalisation, journeys and measurement, data collection, data engineering and cloud, and governed AI. Each practice has its own service page with scope, approach and engagement options. Infiante360 is independent and is not affiliated with Adobe. Results depend on your data, team and goals.",
    sections=[
        ("What we deliver", _l(["Adobe Experience Platform and Real-Time CDP architecture and delivery support", "Journey Optimizer and Customer Journey Analytics design and measurement", "Web SDK and Tags implementation, with consent and validation", "Data engineering and cloud data platforms for customer data", "Agentic AI and MCP with scoped access and approval steps", "Staff augmentation and team training when you want to build in-house"])),
        ("The six practices",
         _prac("1. Customer data and identity", "Customer 360 models, identity resolution and profile design that your teams can explain and own.", "../services/customer-360-identity-resolution.html")
         + _prac("2. Real-time personalisation", "Audiences, destinations and activation, from rules-based targeting to decisioning, with consent respected.", "../services/real-time-cdp.html")
         + _prac("3. Journeys and measurement", "Journey design across channels, and analytics that reconcile before anything is switched off.", "../services/adobe-journey-optimizer.html")
         + _prac("4. Data collection", "Web SDK, datastreams, Tags and event design, validated in every environment.", "../services/web-sdk-adobe-tags.html")
         + _prac("5. Data engineering and cloud", "Pipelines, quality and cost control on Snowflake, BigQuery, Databricks and Kafka.", "../services/data-engineering.html")
         + _prac("6. Governed AI", "Agentic AI and MCP where policy lives in the server, and agents cannot approve their own actions.", "../services/agentic-ai-mcp.html")),
        ("How we work with you", '<p>Five ways: advise, teach, build with you, build for you, or extend your team. See the <a href="../services/engagement-model.html">engagement model</a>, <a href="../services/staff-augmentation.html">staff augmentation</a> and <a href="../training/corporate-training.html">corporate training</a>.</p>'),
        ("From our guides", _l(['<a href="../guides/customer-360-data-model-layers.html">The layers of a customer 360 data model</a>', '<a href="../guides/cja-vs-adobe-analytics-decision.html">Customer Journey Analytics or Adobe Analytics: how to decide</a>', '<a href="../guides/mcp-vs-rest-enterprise-agents.html">MCP or direct REST for enterprise agents</a>']) + '<p><a href="../learn/">All guides and insights</a></p>'),
        ("Start a project", '<p>Starting a new implementation or fixing an existing one? <a href="../lp/aep-architecture-review.html">Book an architecture review</a> or <a href="../contact-us.html">talk to us</a>. WhatsApp or call +91 82968 93895.</p>'),
    ],
    faqs=[("Is Infiante360 an Adobe partner?", "No. Infiante360 is independent and is not affiliated with or endorsed by Adobe. Adobe product names belong to their owners."),
          ("Do you publish client results?", "Not unless we have written permission and the facts are verified. Case studies on this site are illustrative unless stated.")],
    related=["services/index.html", "solutions/index.html", "about-us.html"],
)
PRACTICES_ALL = [PRACTICES_PAGE]
