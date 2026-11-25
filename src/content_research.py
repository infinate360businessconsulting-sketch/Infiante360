"""Research & Intelligence hub (first article). Registry: data/research/topic_registry.json.
Rules: primary sources only, no invented statistics or vendor capabilities, hypothetical examples labelled.
Sources are listed for the reader to verify; this module records no retrieval dates because none were captured by the build."""
from content_articles import art, ul, ol, tbl, ILL, EL, S_PROF, S_GOV, S_ID

MCP = ("Model Context Protocol (official site)", "https://modelcontextprotocol.io/")
OWASP = ("OWASP Top 10 for LLM Applications", "https://owasp.org/www-project-top-10-for-large-language-model-applications/")
NIST = ("NIST AI Risk Management Framework", "https://www.nist.gov/itl/ai-risk-management-framework")

ART = art(
    "mcp-customer-data-platforms", "MCP and Customer Data Platforms: Architecture Research",
    "Research on connecting Model Context Protocol servers to a customer data platform: architecture, access patterns, security limits and open questions.",
    "MCP integration with customer data platforms: architecture research",
    ["mcp customer data platform", "model context protocol cdp", "mcp server customer data", "ai agent cdp access"],
    "A customer data platform can be exposed to AI agents through a Model Context Protocol server that wraps approved operations such as profile lookup or audience counts. The server, not the model, must enforce consent, permissions and logging. Start read-only, add gated writes later, and verify every capability against current vendor documentation.",
    [("Research questions", ul(["What does MCP standardise, and what does it leave to the implementer?", "Which CDP operations are safe to expose to an agent, and in what order?", "Where must consent and access control be enforced?", "What is still unproven or vendor-specific?"])),
     ("What MCP defines", "<p>The official documentation describes MCP as an open protocol for connecting AI applications to external tools and data. An application hosts an MCP client, which talks to one or more MCP servers. Servers can expose tools (actions), resources (readable data) and prompts (reusable templates), and messages follow a JSON-RPC style exchange over defined transports. Read the official site for the current specification, because the protocol evolves.</p><p>What it does not define is your business policy: which customer fields an agent may see, which audiences it may create, or which actions need approval. Those decisions belong to the server you build and the governance around it.</p>"),
     ("Reference architecture", "<p>The pattern below puts a thin MCP server between the agent and the CDP. The server translates a small set of allowed operations into calls to the platform's documented APIs and applies policy before and after every call.</p>" + tbl(["Layer", "Responsibility", "Design question"], [["Agent host and MCP client", "Runs the model, calls tools", "Which model, which user identity?"], ["MCP server", "Exposes allowed operations only", "Which operations, with which limits?"], ["Policy layer", "Consent, role checks, field filtering, logging", "Who owns the rules?"], ["CDP APIs", "Profiles, audiences, activation", "Which documented API supports each operation?"]]) + ILL),
     ("Access patterns, from safest to riskiest", tbl(["Pattern", "Example", "Control"], [["Metadata read", "List audiences and their definitions", "Role check, logging"], ["Aggregate read", "Audience size without profile detail", "Minimum-count rule"], ["Single profile read", "Look up one customer for a service agent", "Consent check, field filter, audit"], ["Draft write", "Propose an audience in a sandbox", "Sandbox only, human review"], ["Activation", "Send an audience to a destination", "Human approval, rollback plan"]])),
     ("Security and governance", ul(["Enforce consent and field-level rules in the server, never in the prompt", "Use the narrowest credentials that work and separate non-production from production", "Treat text returned by tools as untrusted input; hidden instructions in data can steer a model (see OWASP guidance)", "Log each request, the identity behind it and the outcome", "Check the specification's current authorization guidance for remote servers before exposing one"])),
     ("Limitations and open questions", ul(["The protocol and its ecosystem are changing; pin versions and retest after upgrades", "Vendor support for MCP differs. Do not assume your CDP ships an official server; check its documentation", "Latency and cost of agent calls against large profile stores are not established here and need your own testing", "No public evidence supplied on this page proves business impact; measure it in your environment"])),
     ("Recommendations", ol([("Start read-only", "metadata and aggregate reads first."), ("Build the policy layer first", "consent, roles and logging before any write."), ("Test with synthetic profiles", "including hostile text hidden in fields."), ("Gate every write", "sandbox first, then human approval."), ("Review quarterly", "against the specification and your platform's documentation.")])),
     ("Illustrative scenario", "<p>A service team wants an assistant that answers questions about a customer's open requests. A server exposes one tool, <code>get_customer_summary</code>, which returns only approved fields for a customer the signed-in agent is allowed to see, and refuses if consent for service use is missing. The assistant cannot list all customers or change audiences.</p>" + ILL)],
    [("Is MCP a replacement for the CDP's own APIs?", "No. MCP is a way for AI applications to call tools and read data. The server still relies on the platform's APIs underneath."),
     ("Does Adobe provide an MCP server for Experience Platform?", "Check Adobe's current documentation. This article does not assume any specific vendor offering."),
     ("Where should consent be checked?", "In the server, on every call, before data reaches the model. A prompt instruction is not a control.")],
    [MCP, OWASP, NIST, S_PROF, S_GOV],
    ["guides/what-is-mcp.html", "services/agentic-ai-mcp.html", "guides/enterprise-ai-agent-approval-gate.html"], "Research")
ART["path"] = "research/mcp-customer-data-platforms.html"
ART["category"] = "Guides"
ART["related"].append("research/index.html")
RESEARCH_PAGES = [ART]


def _hub():
    import json, os
    reg = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "research", "topic_registry.json"), encoding="utf-8"))
    c = reg["counts"]
    links = [("MCP integration with customer data platforms (research article)", "mcp-customer-data-platforms.html"),
             ("Customer Journey Analytics reference architecture", "../guides/cja-reference-architecture.html"),
             ("Adobe Journey Optimizer reference architecture", "../guides/ajo-reference-architecture.html"),
             ("Enterprise AI agent approval gate design", "../guides/enterprise-ai-agent-approval-gate.html"),
             ("Testing an agentic AI implementation", "../guides/test-agentic-ai-implementation.html"),
             ("MarTech Center of Excellence: operating model and RACI", "../guides/martech-coe-operating-model-raci.html"),
             ("Snowflake, BigQuery, Databricks and Kafka consulting", "../services/snowflake-martech-integration.html")]
    body = '<ul class="checklist">' + "".join(f'<li><a href="{u}">{t}</a></li>' for t, u in links) + "</ul>"
    return dict(path="research/index.html", nav="Research", title="Research and Intelligence: Adobe MarTech, AI and Data",
                desc="Original research and architecture guidance on Adobe MarTech, customer data, Agentic AI and MCP, with primary sources and clearly labelled examples.",
                h1="Research and intelligence", kicker="Research", keywords=["martech research", "agentic ai research", "customer data architecture research"],
                answer="This section collects original research and architecture guidance on Adobe MarTech, customer data platforms, Agentic AI and data engineering. Each piece cites primary sources, labels hypothetical examples and avoids unverified statistics. Publication is driven by research quality, not a fixed schedule.",
                schema="CollectionPage", category="Research",
                sections=[("Read the research", body),
                          ("How we publish", '<ul class="checklist"><li>Primary sources only: vendor documentation and standards bodies</li><li>Hypothetical examples are labelled and never presented as client results</li><li>No invented statistics, rankings or vendor capabilities</li><li>One page per distinct question; existing pages are updated instead of duplicated</li></ul>'),
                          ("What is planned", f'<p>A topic registry tracks {reg["total"]} research topics: {c["exists"]} are already covered by existing pages, {c["new"]} are candidates for new research, and {c["blocked_data"]} need authorised job-market data before they can be written. Candidates are published only when the research is complete.</p>')],
                faqs=[], related=["guides/what-is-mcp.html", "insights/index.html", "services/agentic-ai-mcp.html"])


RESEARCH_PAGES.insert(0, _hub())
