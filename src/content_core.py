"""Home, about, training, guides, industries, FAQ, contact, privacy pages."""
from visuals import journey_svg

EL = "https://experienceleague.adobe.com/en/docs"
REG_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfKeY_33fgEBKYskgG2shgRcYLvHx50ES_KqrULMKromsE3mg/viewform?usp=header"
CAREER_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSctdT6hTSgIeBxok4KgCKC4EISTB8l-S3rKV1NK8SedwGvMZQ/viewform?usp=sharing&ouid=117017541254219120366"
BOOKING = "https://calendar.app.google/5CHbD1hmQBHxcJyy5"

CORE = [
    dict(
        path="index.html",
        nav="Home",
        title="Infinite360 | Adobe MarTech Consulting, AEP Training & AI",
        desc="Adobe MarTech consulting and training for AEP, Real-Time CDP, Journey Optimizer, CJA and Agentic AI — for enterprise teams and professionals.",
        h1="Turn customer data into intelligent experiences",
        kicker="Adobe MarTech · Customer Data · Agentic AI",
        keywords=["adobe martech consulting", "adobe experience platform training", "aep consultant india", "martech consultant", "agentic ai martech", "adobe experience cloud consultant"],
        answer="Infinite360 is an Adobe MarTech consulting and learning brand. We help enterprises design and implement Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics, and help professionals build practical AEP and Agentic AI skills through hands-on training and free guides.",
        schema="WebPage",
        hero_ctas=True,
        sections=[
            ("Three ways we help", """
<div class="grid-3">
<a class="card link-card accent-red" href="services/index.html"><span class="tag">Enterprise consulting</span><h3>Architecture &amp; implementation</h3><p>AEP, RTCDP, AJO, CJA, Web SDK, data engineering and governed AI for enterprise teams.</p><span class="more">Explore services &rarr;</span></a>
<a class="card link-card accent-blue" href="training/corporate-training.html"><span class="tag">Capability building</span><h3>Corporate training</h3><p>Tailored, project-based enablement for MarTech, data and consulting teams.</p><span class="more">Corporate training &rarr;</span></a>
<a class="card link-card accent-green" href="training/index.html"><span class="tag">Tech Academy</span><h3>Career accelerator</h3><p>Hands-on Adobe MarTech and Agentic AI learning for individual professionals.</p><span class="more">View the program &rarr;</span></a>
</div>"""),
            ("Free Adobe Experience Platform guides", """
<p>Practical, step-by-step guides that follow the real AEP data flow.</p>
<div class="grid-3">
<a class="card link-card" href="adobe-experience-platform/xdm-schemas.html"><h3>XDM schemas</h3><p>Design schemas with classes, field groups and identities.</p></a>
<a class="card link-card" href="adobe-experience-platform/data-ingestion.html"><h3>Data ingestion</h3><p>Batch, streaming, source connectors and Data Prep.</p></a>
<a class="card link-card" href="adobe-experience-platform/identity-service.html"><h3>Identity resolution</h3><p>Namespaces, identity graphs and avoiding graph collapse.</p></a>
<a class="card link-card" href="adobe-experience-platform/real-time-customer-profile.html"><h3>Customer profiles</h3><p>Real-Time Customer Profile and merge policies.</p></a>
<a class="card link-card" href="adobe-experience-platform/segmentation-audiences.html"><h3>Segments &amp; audiences</h3><p>Batch, streaming and edge segmentation.</p></a>
<a class="card link-card" href="adobe-experience-platform/implementation-guide.html"><h3>Implementation guide</h3><p>End-to-end steps and checklist.</p></a>
</div>
<p class="center"><a class="btn btn-ghost" href="adobe-experience-platform/index.html">See the full AEP guide &rarr;</a></p>"""),
            ("Outcomes we focus on", """
<ul class="checklist cols-2">
<li>Stronger MarTech strategy tied to business goals</li>
<li>Connected customer data and technology</li>
<li>Real-time, personalised customer engagement</li>
<li>AI-assisted marketing operations with governance</li>
<li>Skilled, confident internal teams</li>
<li>Measurable, well-instrumented journeys</li>
</ul>"""),
            ("Popular questions", """
<div class="grid-3">
<a class="card link-card" href="guides/aep-vs-real-time-cdp.html"><h3>AEP vs Real-Time CDP</h3><p>What is the difference?</p></a>
<a class="card link-card" href="guides/cja-vs-adobe-analytics.html"><h3>CJA vs Adobe Analytics</h3><p>Use cases and trade-offs.</p></a>
<a class="card link-card" href="guides/what-is-mcp.html"><h3>What is MCP?</h3><p>Using MCP safely with enterprise MarTech.</p></a>
</div>"""),
        ],
        faqs=[
            ("What does Infinite360 do?", "Infinite360 provides Adobe MarTech consulting, corporate training and a Tech Academy career accelerator focused on Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, data engineering and Agentic AI."),
            ("How do I contact Infinite360?", "Use the contact form, WhatsApp +91 82968 93895, or book a call from the contact page."),
        ],
        related=["services/index.html", "training/index.html", "adobe-experience-platform/index.html"],
    ),
    dict(
        path="about-us.html",
        nav="About",
        title="About Infinite360 | Adobe MarTech Consulting & Tech Academy",
        desc="About Infinite360: Adobe MarTech consulting and learning focused on AEP, customer data, analytics, data engineering and Agentic AI.",
        h1="About Infinite360",
        kicker="Learn · Build · Transform · Lead",
        keywords=["about infinite360", "infinite360 tech academy", "pavan babu gandla", "adobe martech consultant", "martech academy india"],
        answer="Infinite360 is a practical learning and enterprise enablement brand focused on Adobe MarTech, customer data, analytics, data engineering, Agentic AI and digital transformation. It combines consulting for enterprises with hands-on training for teams and individual professionals.",
        schema="AboutPage",
        sections=[
            ("Who we are", """
<p>Infinite360 is built around a simple idea: professionals learn faster, and platforms deliver more, when concepts are connected to architecture, implementation, troubleshooting and business context.</p>
<p>Our work spans <a href="adobe-experience-platform/index.html">Adobe Experience Platform</a>, XDM, identity, <a href="services/real-time-cdp.html">Real-Time CDP</a>, <a href="services/adobe-journey-optimizer.html">Journey Optimizer</a>, <a href="services/customer-journey-analytics.html">Customer Journey Analytics</a>, Adobe Analytics, <a href="services/web-sdk-adobe-tags.html">Web SDK</a>, APIs, <a href="services/agentic-ai-mcp.html">Agentic AI and MCP</a>, <a href="services/data-engineering.html">data engineering</a> and enterprise architecture.</p>"""),
            ("Leadership", """
<div class="card person">
<h3>Pavan Babu Gandla</h3>
<p class="muted">Founder &middot; Digital Transformation &amp; MarTech Leader</p>
<p>Pavan works as a MarTech and data architect focused on Adobe Experience Cloud, customer data architecture and Agentic AI, advising enterprise data, technology and marketing leaders.</p>
<p><a href="https://www.martechconsultant.tech/Pavan.html" rel="noopener" target="_blank">Consulting profile</a> &middot; <a href="https://linkedin.com/in/pavanbabu1" rel="noopener" target="_blank">LinkedIn</a></p>
</div>"""),
            ("Our approach", """
<ol class="steps">
<li><strong>Learn</strong> &mdash; understand the concepts and the why.</li>
<li><strong>Practice</strong> &mdash; work through hands-on labs and real scenarios.</li>
<li><strong>Apply</strong> &mdash; implement on projects with architecture discipline.</li>
<li><strong>Measure</strong> &mdash; validate outcomes and data quality.</li>
<li><strong>Scale</strong> &mdash; document and enable teams to repeat success.</li>
</ol>"""),
            ("Our commitments", """
<ul class="checklist">
<li>We do not publish client names, results or testimonials without permission.</li>
<li>We do not promise jobs, salaries or certification outcomes.</li>
<li>Training outcomes depend on participation and practice.</li>
</ul>"""),
        ],
        faqs=[
            ("Is Infinite360 an Adobe partner?", "Infinite360 is an independent consulting and training brand. Adobe product names are trademarks of Adobe; their use here describes the technologies we work with and does not imply endorsement."),
        ],
        related=["services/index.html", "training/index.html", "contact-us.html"],
    ),
    dict(
        path="training/index.html",
        nav="Training",
        hero_visual=journey_svg(),
        hero_cta=("Register for ₹60,000", REG_FORM),
        price_inr=60000,
        title="AEP Course: Adobe MarTech & Agentic AI Career Accelerator",
        desc="Live online Adobe Experience Platform course: AEP, RTCDP, AJO, CJA, Web SDK and Agentic AI training with projects, labs and interview prep.",
        h1="Adobe MarTech + Agentic AI career accelerator",
        kicker="Infinite360 Tech Academy",
        keywords=["adobe experience platform course", "aep training", "aep course online", "aep certification training", "rtcdp training", "ajo training", "cja training", "adobe martech training india"],
        answer="The Infinite360 career accelerator is a live, online, hands-on Adobe Experience Platform course for professionals moving into Adobe MarTech roles. It covers AEP, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Web SDK and Agentic AI through labs, enterprise-style projects, troubleshooting scenarios and interview preparation.",
        schema="Course",
        sections=[
            ("What you will learn", """
<div class="grid-3">
<div class="card"><h3>AEP architecture</h3><p>XDM, datasets, ingestion, Profile, Identity Service, governance and segmentation.</p></div>
<div class="card"><h3>RTCDP &amp; Customer 360</h3><p>Identity resolution, audience design, destinations and activation patterns.</p></div>
<div class="card"><h3>AJO orchestration</h3><p>Event and audience journeys, decisioning, suppression and validation.</p></div>
<div class="card"><h3>CJA &amp; analytics</h3><p>Connections, data views, cross-channel analysis and reporting.</p></div>
<div class="card"><h3>Web SDK</h3><p>Data layers, datastreams, consent and the Edge Network.</p></div>
<div class="card"><h3>Agentic AI &amp; MCP</h3><p>AI agents, governed tools and MarTech workflow automation.</p></div>
</div>"""),
            ("Program tracks", """
<div class="grid-2">
<div class="card"><h3>Adobe Experience &amp; MarTech</h3><p>Adobe Experience Platform, Journey Optimizer, Customer Journey Analytics, Adobe Analytics, Target, Experience Manager, Real-Time CDP and personalisation.</p></div>
<div class="card"><h3>AI &amp; Agentic AI</h3><p>Generative AI and LLMs, AI agents, AI automation, AI for marketing and CX, enterprise AI solutions and AI transformation.</p></div>
<div class="card"><h3>Data engineering &amp; analytics</h3><p>Python, SQL, PySpark, Databricks and big data, ETL/ELT pipelines, cloud data platforms, data modelling, warehousing and analytics engineering.</p></div>
<div class="card"><h3>Corporate &amp; customised training</h3><p>Transformation programs, hands-on implementation, industry-specific solutions and expert-led workshops. See <a href="corporate-training.html">corporate training</a>.</p></div>
</div>
<p>Moving from another role? See <a href="career-transition.html">how your current experience maps to Adobe MarTech roles</a>.</p>"""),
            ("A 90-day roadmap in six phases", """
<ol class="steps">
<li><strong>AEP core</strong> &mdash; XDM, datasets, ingestion, Profile, Identity, Query Service.</li>
<li><strong>Web SDK, CJA and AJO</strong> &mdash; datastreams, connections, data views and real-time journeys.</li>
<li><strong>RTCDP and activation</strong> &mdash; audiences, destinations, personalisation and validation.</li>
<li><strong>Architect patterns</strong> &mdash; APIs, integration, security, environments, QA and monitoring.</li>
<li><strong>Agentic AI and MCP</strong> &mdash; agents, tools and governed data access.</li>
<li><strong>Career deployment</strong> &mdash; capstone, mock interviews and portfolio positioning.</li>
</ol>"""),
            ("Hands-on projects", """
<ul class="cols-2">
<li>Enterprise Customer 360 data model</li>
<li>Real-time transaction journey</li>
<li>RTCDP audience activation</li>
<li>CJA executive reporting</li>
<li>Web SDK modernisation</li>
<li>Enterprise data pipeline</li>
<li>MarTech integration hub</li>
<li>Production readiness checklist</li>
<li>Agentic AI marketing assistant</li>
<li>AEP + AI capstone</li>
</ul>"""),
            ("Who it is for", """
<p>Beginners and students with an analytics or technology background, career switchers, marketers, developers, data engineers, implementation specialists, consultants and aspiring architects. Sessions run live online in Indian Standard Time, so learners can join from Bangalore, Hyderabad, Chennai, Mumbai, Pune, Delhi NCR and elsewhere in India, or internationally where the timings suit.</p>"""),
            ("Program fee and registration", f"""
<div class="price-card">
<div><div class="price">₹60,000<small>Adobe MarTech + Agentic AI Career Accelerator</small></div>
<p class="cta-row" style="margin-top:20px"><a class="btn btn-primary" href="{REG_FORM}" rel="noopener" target="_blank">Register now</a> <a class="btn btn-ghost" href="{CAREER_FORM}" rel="noopener" target="_blank">Free career mapping</a></p></div>
<ul class="checklist">
<li>Live online sessions across six phases</li>
<li>Hands-on labs and enterprise-style projects</li>
<li>AEP, RTCDP, AJO, CJA, Web SDK, Agentic AI &amp; MCP</li>
<li>Architect troubleshooting scenarios and interview preparation</li>
<li>Career mapping, resume and LinkedIn positioning guidance</li>
</ul>
</div>
<p>Batch dates and session timings are shared on registration. Corporate and team pricing is quoted separately &mdash; see <a href="corporate-training.html">corporate training</a>.</p>
<p class="small muted">Training outcomes depend on individual participation and practice. No job, salary or certification outcome is guaranteed.</p>"""),
        ],
        faqs=[
            ("Is the AEP course online?", "Yes. Sessions are delivered live online with hands-on exercises."),
            ("How much does the career accelerator cost?", "The program fee is ₹60,000 for the Adobe MarTech + Agentic AI Career Accelerator. Corporate and team pricing is quoted separately."),
            ("Does the course prepare me for Adobe certification?", "The program covers the concepts tested in Adobe certifications relevant to AEP, but it is independent of Adobe and does not guarantee a certification result."),
            ("Do I need prior Adobe experience?", "No. A basic understanding of data, marketing or web technology helps. Beginners start with the AEP data flow."),
        ],
        related=["adobe-experience-platform/career-path.html", "adobe-experience-platform/interview-questions.html", "training/corporate-training.html"],
    ),
    dict(
        path="training/corporate-training.html",
        title="Corporate AEP Training: Adobe MarTech Team Upskilling",
        desc="Corporate training for enterprise and SI teams: tailored AEP, RTCDP, AJO, CJA, data engineering and Agentic AI programs with hands-on labs.",
        h1="Corporate Adobe MarTech training",
        kicker="Capability building",
        keywords=["corporate aep training", "adobe experience platform training for enterprise teams", "martech team upskilling", "rtcdp corporate training", "agentic ai corporate training"],
        answer="Corporate training from Infinite360 upskills enterprise MarTech, data and consulting teams through tailored, project-based programs on Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, data engineering and Agentic AI, with labs, assessments and capstones aligned to your use cases.",
        schema="Service",
        service_type="Corporate MarTech training",
        sections=[
            ("Program formats", """
<div class="grid-3">
<div class="card"><h3>Foundation</h3><p>MarTech, analytics, data and customer experience fundamentals for mixed business and technical teams.</p></div>
<div class="card"><h3>Practitioner</h3><p>Hands-on Adobe, AEP, analytics and journey implementation labs.</p></div>
<div class="card"><h3>Advanced</h3><p>APIs, integrations, complex use cases, troubleshooting and governance.</p></div>
<div class="card"><h3>Architect</h3><p>Enterprise architecture, operating model, solution design and transformation.</p></div>
<div class="card"><h3>Capstone</h3><p>A use case relevant to your organisation, delivered as an architecture, design or implementation artefact.</p></div>
<div class="card"><h3>Mentoring</h3><p>Senior practitioners guide teams from training into project execution.</p></div>
</div>"""),
            ("Training tracks", """
<ul class="cols-2">
<li><strong>Adobe Experience &amp; MarTech</strong> &mdash; AEP, AJO, CJA, Adobe Analytics, Target, AEM, Real-Time CDP and personalisation.</li>
<li><strong>AI &amp; Agentic AI</strong> &mdash; generative AI and LLMs, AI agents, automation, AI for marketing and CX, enterprise AI solutions.</li>
<li><strong>Data engineering &amp; analytics</strong> &mdash; Python, SQL, PySpark, Databricks, ETL/ELT pipelines, cloud data platforms, data modelling and warehousing.</li>
<li><strong>Transformation programs</strong> &mdash; leadership and CTO transformation programs, digital transformation, industry-specific solutions and expert-led workshops.</li>
</ul>"""),
            ("How programs are built", """
<p>Every corporate program follows the same capability cycle: <strong>Assess &rarr; Train &rarr; Practice &rarr; Build &rarr; Review &rarr; Implement &rarr; Transfer &rarr; Scale</strong>.</p>
<ol class="steps">
<li>Skills assessment and goals with L&amp;D and delivery leaders.</li>
<li>Role-based curriculum tailored to your platforms and use cases.</li>
<li>Live sessions, hands-on labs and project work.</li>
<li>Assessments, review and a capstone presented to stakeholders.</li>
<li>Mentored transfer into real project delivery, with reusable standards.</li>
</ol>"""),
            ("Who it is for", "<p>L&amp;D and capability leaders, consulting and SI delivery leaders, Centres of Excellence and enterprise transformation teams.</p>"),
        ],
        faqs=[
            ("Can training be customised to our implementation?", "Yes. Programs can use your own use cases and, where permitted, sanitised examples from your environment."),
        ],
        related=["training/index.html", "services/index.html", "contact-us.html"],
    ),
    dict(
        path="guides/aep-vs-real-time-cdp.html",
        title="AEP vs Real-Time CDP: What Is the Difference?",
        desc="Adobe Experience Platform vs Real-Time CDP: what each does, how they relate, which capabilities belong where, and how to decide what you need.",
        h1="AEP vs Real-Time CDP: what is the difference?",
        kicker="Comparison guide",
        keywords=["aep vs rtcdp", "adobe experience platform vs real-time cdp", "difference between aep and rtcdp", "what is real-time cdp"],
        answer="Adobe Experience Platform (AEP) is the underlying data foundation: schemas, ingestion, identity, profiles, segmentation and governance. Real-Time CDP (RTCDP) is an application built on AEP that adds customer data platform capabilities, most notably activating audiences and profiles to marketing and advertising destinations.",
        schema="Article",
        sections=[
            ("Side-by-side", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Adobe Experience Platform</th><th>Real-Time CDP</th></tr></thead>
<tbody>
<tr><td>Role</td><td>Data foundation for Adobe applications</td><td>CDP application on AEP</td></tr>
<tr><td>Core capabilities</td><td>XDM, ingestion, identity, profile, segmentation, governance</td><td>Uses those capabilities plus destination activation and CDP workflows</td></tr>
<tr><td>Typical users</td><td>Data engineers, architects</td><td>Marketers, MarTech teams</td></tr>
</tbody></table></div>
<p>Exact features depend on the edition and licence; confirm with Adobe documentation and your contract.</p>"""),
            ("How to decide", """
<ul>
<li>If you need to activate audiences to channels, you are evaluating Real-Time CDP.</li>
<li>If you need journeys, look at <a href="../services/adobe-journey-optimizer.html">Journey Optimizer</a>; for analytics, <a href="../services/customer-journey-analytics.html">CJA</a>.</li>
<li>All of them depend on a well-designed <a href="../adobe-experience-platform/index.html">AEP foundation</a>.</li>
</ul>"""),
        ],
        faqs=[
            ("Can I use AEP without Real-Time CDP?", "AEP is provisioned with Adobe applications such as RTCDP, AJO or CJA; the available capabilities depend on what you license."),
        ],
        sources=[("Real-Time CDP overview", f"{EL}/experience-platform/rtcdp/home"), ("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
        related=["services/real-time-cdp.html", "adobe-experience-platform/activation-destinations.html", "adobe-experience-platform/index.html"],
    ),
    dict(
        path="guides/cja-vs-adobe-analytics.html",
        title="CJA vs Adobe Analytics: Use Cases, Differences and Trade-offs",
        desc="Customer Journey Analytics vs Adobe Analytics compared: data model, cross-channel analysis, identity, implementation with Web SDK, and when to migrate.",
        h1="CJA vs Adobe Analytics: use cases and trade-offs",
        kicker="Comparison guide",
        keywords=["cja vs adobe analytics", "customer journey analytics vs adobe analytics", "adobe analytics to cja migration", "what is customer journey analytics"],
        answer="Adobe Analytics is a digital analytics product built on report suites, mainly for web and app data. Customer Journey Analytics (CJA) analyses any AEP dataset, online or offline, joined on a person ID, enabling cross-channel journey analysis. Many organisations migrate to CJA with Web SDK, while weighing reporting continuity and feature differences.",
        schema="Article",
        sections=[
            ("Key differences", """
<div class="table-wrap"><table>
<thead><tr><th></th><th>Adobe Analytics</th><th>Customer Journey Analytics</th></tr></thead>
<tbody>
<tr><td>Data source</td><td>Report suites</td><td>AEP datasets via connections</td></tr>
<tr><td>Scope</td><td>Primarily digital channels</td><td>Cross-channel, online and offline</td></tr>
<tr><td>Configuration</td><td>Variables at collection</td><td>Data views defined at reporting time</td></tr>
</tbody></table></div>"""),
            ("Migration considerations", """
<ul class="checklist">
<li>Map existing variables and KPIs to XDM and data view components.</li>
<li>Plan Web SDK collection and parallel running.</li>
<li>Agree a person ID strategy for cross-channel stitching.</li>
<li>Retrain analysts on Workspace in CJA.</li>
</ul>
<p>Need help? See <a href="../services/customer-journey-analytics.html">CJA consulting</a>.</p>"""),
        ],
        faqs=[
            ("Does CJA replace Adobe Analytics?", "It can, depending on requirements. Some organisations run both during migration. Compare features against your reporting needs first."),
        ],
        sources=[("Customer Journey Analytics documentation", f"{EL}/analytics-platform/using/cja-landing")],
        related=["services/customer-journey-analytics.html", "services/web-sdk-adobe-tags.html", "adobe-experience-platform/datasets.html"],
    ),
    dict(
        path="guides/what-is-mcp.html",
        title="What Is MCP? Model Context Protocol for Enterprise MarTech",
        desc="What the Model Context Protocol (MCP) is, how AI agents use MCP tools, and how to apply it safely to enterprise MarTech workflows.",
        h1="What is MCP, and how can it be used safely with enterprise MarTech?",
        kicker="Agentic AI guide",
        keywords=["what is mcp", "model context protocol", "mcp martech", "mcp enterprise security", "agentic ai adobe"],
        answer="The Model Context Protocol (MCP) is an open standard that lets AI applications connect to external tools and data through MCP servers. In enterprise MarTech, MCP can give AI agents controlled access to documentation, configuration checks or approved data, provided access is least-privilege, actions are approved and every call is logged.",
        schema="Article",
        sections=[
            ("How MCP works", """
<ol class="steps">
<li>An MCP server exposes tools (actions) and resources (data) with descriptions.</li>
<li>An AI application (the client) discovers those tools.</li>
<li>The model decides when to call a tool; the client executes it and returns results.</li>
</ol>"""),
            ("Safe-use checklist", """
<ul class="checklist">
<li>Start read-only; add write tools only with human approval.</li>
<li>Scope credentials per tool; keep secrets out of prompts.</li>
<li>Filter personal data and respect consent and governance labels.</li>
<li>Log tool calls and review them.</li>
<li>Test with evaluation sets before production.</li>
</ul>"""),
            ("MarTech examples", "<p>Schema validation helpers, audience QA checks, documentation assistants and analytics question-answering over approved data views. See <a href=\"../services/agentic-ai-mcp.html\">Agentic AI &amp; MCP consulting</a>.</p>"),
        ],
        faqs=[
            ("Is MCP secure by default?", "No protocol is secure by default. Security depends on how servers, credentials, permissions and approvals are configured."),
        ],
        sources=[("Model Context Protocol", "https://modelcontextprotocol.io/")],
        related=["services/agentic-ai-mcp.html", "training/index.html", "services/data-engineering.html"],
    ),
    dict(
        path="industries.html",
        nav="Industries",
        title="Adobe MarTech for BFSI, Retail, Telecom & Hospitality",
        desc="How AEP, Real-Time CDP, Journey Optimizer and CJA apply to banking and financial services, retail, telecom and hospitality.",
        h1="Industries we focus on",
        kicker="Industries",
        keywords=["adobe experience platform banking", "cdp for retail", "telecom churn adobe", "hospitality personalization", "bfsi martech consulting"],
        answer="Infinite360 focuses on industries with rich customer data and real-time engagement needs: banking, financial services and insurance (BFSI), retail and e-commerce, telecom, and travel and hospitality. The same AEP foundation applies, but identity, consent and use cases differ by industry.",
        schema="WebPage",
        sections=[
            ("Banking, financial services and insurance", "<p>Strict identity around customer IDs, sensitive-data governance, consent, onboarding and cross-sell journeys, and service personalisation. See <a href=\"adobe-experience-platform/architecture.html\">AEP architecture</a> for governance patterns.</p>"),
            ("Retail and e-commerce", "<p>Unifying web, app, store and loyalty data; cart and browse abandonment journeys; suppression of recent purchasers; product affinity audiences. See <a href=\"adobe-experience-platform/segmentation-audiences.html\">segmentation</a>.</p>"),
            ("Telecom", "<p>Churn-risk signals, plan-upgrade journeys, service-event triggers and household identity considerations. See <a href=\"services/adobe-journey-optimizer.html\">Journey Optimizer</a>.</p>"),
            ("Travel and hospitality", "<p>Booking and stay lifecycle journeys, loyalty profiles and real-time offers across channels. See <a href=\"services/real-time-cdp.html\">Real-Time CDP</a>.</p>"),
        ],
        faqs=[
            ("Do you work in other industries?", "Yes, the same principles apply to education, manufacturing, media and others. Contact us to discuss your use case."),
        ],
        related=["services/index.html", "adobe-experience-platform/index.html", "contact-us.html"],
    ),
    dict(
        path="faq.html",
        nav="FAQ",
        title="FAQ: Adobe MarTech Consulting, AEP Training & Infinite360",
        desc="Answers to common questions about Infinite360 consulting and training, Adobe Experience Platform, Real-Time CDP, Journey Optimizer, CJA and Agentic AI.",
        h1="Frequently asked questions",
        kicker="FAQ",
        keywords=["infinite360 faq", "aep training faq", "adobe experience platform faq", "martech consulting faq"],
        answer="Quick answers about Infinite360's consulting and training, and about Adobe Experience Platform concepts. For anything not covered here, contact us through the form or WhatsApp.",
        schema="FAQPage",
        sections=[],
        faqs=[
            ("What is Adobe Experience Platform (AEP)?", "AEP is Adobe's real-time customer data foundation that standardises data with XDM, ingests it, resolves identities, builds profiles, evaluates audiences and powers applications such as Real-Time CDP, Journey Optimizer and CJA."),
            ("What is the difference between AEP and Real-Time CDP?", "AEP is the data foundation; Real-Time CDP is an application on AEP that adds activation to destinations."),
            ("What services does Infinite360 offer?", "Adobe MarTech consulting (AEP, RTCDP, AJO, CJA, Web SDK), data engineering, Agentic AI and MCP, strategy and advisory, corporate training and an individual career accelerator."),
            ("Is the training online?", "Yes. Training is delivered live online with hands-on labs and projects."),
            ("What is the course fee?", "The Adobe MarTech + Agentic AI Career Accelerator fee is ₹60,000. Corporate programs are quoted per engagement."),
            ("Do you guarantee jobs or certification?", "No. Outcomes depend on participation and practice. We do not guarantee jobs, salaries or certification results."),
            ("Is Infinite360 affiliated with Adobe?", "No. Infinite360 is independent. Adobe product names are trademarks of Adobe."),
            ("How do I get started?", "Use the contact form to describe your goal, or message us on WhatsApp at +91 82968 93895."),
        ],
        related=["contact-us.html", "training/index.html", "services/index.html"],
    ),
    dict(
        path="contact-us.html",
        nav="Contact",
        title="Contact Infinite360 | AEP Consulting & Training Enquiries",
        desc="Contact Infinite360 about AEP consulting, RTCDP, AJO, CJA, Agentic AI, corporate training or the career accelerator. Form, WhatsApp or call.",
        h1="Contact Infinite360",
        kicker="Let's talk",
        keywords=["contact infinite360", "aep consultant contact", "adobe martech consulting enquiry", "aep training enquiry"],
        answer="Tell us what you need and we will reply by your preferred contact method. Use the form below for consulting, corporate training or course enquiries, or reach us directly on WhatsApp or by email.",
        schema="ContactPage",
        sections=[("Send an enquiry", "@@CONTACT_FORM@@")],
        faqs=[],
        related=["services/index.html", "training/index.html", "faq.html"],
    ),
    dict(
        path="privacy-policy.html",
        title="Privacy Policy | Infinite360",
        desc="How Infinite360 handles information submitted through this website's contact forms, and how to request access or deletion.",
        h1="Privacy policy",
        kicker="Legal",
        keywords=[],
        answer="This website does not use analytics or advertising cookies. When you submit a contact form, the details you enter are sent to Infinite360 by email so we can respond to your enquiry.",
        schema="WebPage",
        sections=[
            ("What we collect", "<p>Only the information you choose to enter in a form: for example your name, email, phone, company, role, country, area of interest and message.</p>"),
            ("How it is processed", "<p>Form submissions are delivered to our email inbox through FormSubmit (formsubmit.co), a third-party form-forwarding service. If you choose WhatsApp, your message is sent through WhatsApp under its own terms.</p>"),
            ("How we use it", "<p>Only to respond to your enquiry and related follow-up. We do not sell your information.</p>"),
            ("Your choices", "<p>To access, correct or delete your information, email <a href=\"mailto:infinate360businessconsulting@gmail.com\">infinate360businessconsulting@gmail.com</a>.</p>"),
        ],
        faqs=[],
        related=["contact-us.html"],
    ),
]
