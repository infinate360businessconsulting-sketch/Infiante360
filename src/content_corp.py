"""Corporate pages: solutions, Adobe Experience Cloud platforms, founder profile.

Solution pages describe delivery patterns, not client case studies. No client names,
metrics or testimonials are used anywhere.
"""

EL = "https://experienceleague.adobe.com/en/docs"
PORTFOLIO = "https://martechconsultant.tech"

PATTERN_NOTE = '<p class="small muted">This page describes a solution pattern we deliver. It is not a client case study, and results depend on each organisation\'s data, licensing and execution.</p>'


def solution(path, title, desc, h1, kicker, keywords, answer, problem, architecture, steps, measures, related, faqs):
    return dict(
        path=path, title=title, desc=desc, h1=h1, kicker=kicker, keywords=keywords, answer=answer,
        schema="Article", bands=True, hero_cta=("Discuss this solution", "contact-us.html"),
        sections=[
            ("The business problem", f"<p class=\"lead\">{problem}</p>", "plain", "Why it matters"),
            ("Reference architecture", architecture, "alt", "How it fits together"),
            ("Delivery approach", "<ol class=\"steps\">" + "".join(f"<li><strong>{a}</strong> &mdash; {b}</li>" for a, b in steps) + "</ol>", "plain", "Implementation"),
            ("How success is measured", "<ul class=\"checklist cols-2\">" + "".join(f"<li>{m}</li>" for m in measures) + "</ul>" + PATTERN_NOTE, "dark", "Measurement"),
        ],
        faqs=faqs, related=related,
    )


CORP = [
    dict(
        path="solutions/index.html",
        nav="Solutions",
        bands=True,
        title="MarTech Solutions: Customer 360, Personalisation & Retention",
        desc="Adobe MarTech solution patterns: Customer 360 and identity, real-time personalisation, retention and churn prevention, and B2B lead-to-revenue.",
        h1="Solutions built on a governed customer data foundation",
        kicker="Solutions",
        keywords=["martech solutions", "customer 360 solution", "real-time personalization adobe", "churn prevention martech", "b2b lead to revenue"],
        answer="Infinite360 delivers four core solution patterns on Adobe Experience Cloud: Customer 360 and identity resolution, real-time personalisation, retention and churn prevention, and B2B lead-to-revenue alignment. Each starts from a business outcome and is built on the same governed AEP data foundation.",
        schema="CollectionPage",
        hero_cta=("Talk about your use case", "contact-us.html"),
        sections=[
            ("Solution patterns", """
<div class="grid-2">
<a class="card link-card" href="customer-360.html"><span class="tag" style="background:var(--red-50);color:var(--red-700)">Foundation</span><h3>Customer 360 &amp; identity</h3><p>Unify CRM, web, app, commerce and offline data into governed real-time profiles with a deliberate identity strategy.</p><span class="more">Explore &rarr;</span></a>
<a class="card link-card" href="real-time-personalization.html"><span class="tag" style="background:var(--blue-50);color:var(--blue)">Engagement</span><h3>Real-time personalisation</h3><p>Use streaming and edge audiences to tailor web, app, email and paid media in the moment.</p><span class="more">Explore &rarr;</span></a>
<a class="card link-card" href="churn-prevention.html"><span class="tag" style="background:var(--green-50);color:var(--green)">Retention</span><h3>Retention &amp; churn prevention</h3><p>Detect risk signals, trigger save journeys and measure retained value.</p><span class="more">Explore &rarr;</span></a>
<a class="card link-card" href="b2b-lead-to-revenue.html"><span class="tag" style="background:#f3e8ff;color:#6b21a8">B2B</span><h3>B2B lead-to-revenue</h3><p>Align Marketo, CRM and AEP so lead stages, scoring and audiences agree.</p><span class="more">Explore &rarr;</span></a>
</div>""", "plain", "What we deliver"),
            ("Every solution follows the same path", """
<div class="timeline">
<div class="step"><h3>Outcome</h3><p>Agree the business KPI and the decision it informs.</p></div>
<div class="step"><h3>Data &amp; identity</h3><p>Model only the data the use case needs, with consent.</p></div>
<div class="step"><h3>Activation</h3><p>Audiences, journeys and channels with governance.</p></div>
<div class="step"><h3>Measurement</h3><p>Holdouts, CJA reporting and continuous optimisation.</p></div>
</div>""", "dark", "Method"),
        ],
        faqs=[("Are these client case studies?", "No. These pages describe solution patterns we deliver. We publish client case studies only with permission and verified results.")],
        related=["services/index.html", "industries.html", "services/engagement-model.html"],
    ),
    solution(
        "solutions/customer-360.html",
        "Customer 360 & Identity Resolution on Adobe Experience Platform",
        "Build a governed Customer 360 on Adobe Experience Platform: source unification, identity strategy, real-time profiles, consent and activation readiness.",
        "Customer 360 and identity resolution",
        "Solution · Foundation",
        ["customer 360", "customer 360 adobe", "identity resolution solution", "unified customer profile", "aep customer 360"],
        "A Customer 360 on Adobe Experience Platform unifies CRM, web, app, commerce and offline data into real-time customer profiles. It depends on an XDM data model built around use cases, a deliberate identity strategy that avoids merging different people, consent-aware governance, and merge policies that decide which source wins.",
        "Most organisations hold customer data in many systems that disagree about who a customer is. Marketing, service and analytics teams each build their own version, which leads to duplicated messages, poor personalisation and reports nobody trusts.",
        """<div class="grid-2"><div class="card"><h3>Sources</h3><p>CRM, web and app events via Web SDK, commerce orders, service interactions and warehouse tables.</p></div>
<div class="card"><h3>Model</h3><p>XDM Individual Profile and ExperienceEvent schemas with custom field groups only where needed.</p></div>
<div class="card"><h3>Identity</h3><p>Ranked namespaces (CRM ID, hashed email, ECID) with rules that exclude shared identifiers.</p></div>
<div class="card"><h3>Profile</h3><p>Real-Time Customer Profile with documented merge policies and consent attributes.</p></div></div>
<p>Read more: <a href="../adobe-experience-platform/identity-service.html">identity resolution</a> &middot; <a href="../adobe-experience-platform/real-time-customer-profile.html">profiles &amp; merge policies</a></p>""",
        [("Inventory", "map every source, identifier and owner"), ("Model", "design schemas for the first use cases"), ("Identity", "agree linking rules and test graphs in a dev sandbox"), ("Ingest", "batch and streaming dataflows with reconciliation"), ("Validate", "inspect sample profiles end to end"), ("Operate", "monitoring, data quality ownership and runbooks")],
        ["Share of profiles with a known identifier", "Graph health: no oversized or collapsed graphs", "Source reconciliation within agreed tolerance", "Time from source change to profile update", "Audience build time for marketing teams", "Number of teams using the shared profile"],
        ["solutions/real-time-personalization.html", "adobe-experience-platform/identity-service.html", "services/aep-consulting.html"],
        [("How long does a Customer 360 take?", "It depends on the number of sources and data quality. We recommend delivering one use case end to end first, then adding sources in phases.")],
    ),
    solution(
        "solutions/real-time-personalization.html",
        "Real-Time Personalisation with AEP, RTCDP, AJO & Target",
        "Real-time personalisation on Adobe Experience Cloud: streaming and edge audiences, Journey Optimizer, Target, consent and holdout-based measurement.",
        "Real-time personalisation across channels",
        "Solution · Engagement",
        ["real-time personalization", "adobe personalization", "edge segmentation personalization", "ajo personalization", "adobe target personalization"],
        "Real-time personalisation uses fresh behavioural and profile data to change what a customer sees or receives while it still matters. On Adobe Experience Cloud this combines Web SDK collection, streaming or edge audiences in AEP, Journey Optimizer for messaging and Adobe Target or decisioning for on-site experiences, measured against holdout groups.",
        "Batch campaigns react days after a customer signals intent. By then the moment has passed, and generic messages erode engagement and margin.",
        """<div class="grid-2"><div class="card"><h3>Signals</h3><p>Web SDK and app events streamed through the Edge Network.</p></div>
<div class="card"><h3>Audiences</h3><p>Edge audiences for same-page decisions; streaming audiences for triggered journeys.</p></div>
<div class="card"><h3>Decisions</h3><p>Journey Optimizer journeys and decisioning; Adobe Target for on-site experiences.</p></div>
<div class="card"><h3>Guardrails</h3><p>Consent checks, frequency caps and suppression rules.</p></div></div>
<p>Read more: <a href="../adobe-experience-platform/segmentation-audiences.html">segmentation methods</a> &middot; <a href="../services/adobe-journey-optimizer.html">Journey Optimizer</a></p>""",
        [("Use cases", "pick two or three moments with clear value"), ("Collection", "instrument the events those moments need"), ("Audiences", "choose edge, streaming or batch per use case"), ("Experiences", "design content and offers with fallbacks"), ("Test", "launch with holdouts and QA profiles"), ("Optimise", "review results in CJA and iterate")],
        ["Incremental conversion versus holdout", "Time from signal to experience", "Engagement per message, not just volume", "Suppression accuracy (no messages after purchase)", "Consent compliance", "Content production cycle time"],
        ["solutions/customer-360.html", "services/adobe-journey-optimizer.html", "services/web-sdk-adobe-tags.html"],
        [("Do we need Adobe Target for personalisation?", "Not always. Journey Optimizer, Real-Time CDP destinations and Target cover different channels; the right mix depends on your licences and use cases.")],
    ),
    solution(
        "solutions/churn-prevention.html",
        "Customer Retention & Churn Prevention with Adobe MarTech",
        "Retention and churn prevention on Adobe Experience Cloud: risk signals, retention audiences, save journeys in AJO, and measurement in CJA.",
        "Retention and churn prevention",
        "Solution · Retention",
        ["churn prevention", "customer retention martech", "telecom churn adobe", "retention journeys ajo", "churn risk audiences"],
        "Churn prevention identifies customers showing risk signals — falling usage, service issues, contract milestones or competitor research — and triggers timely, relevant save actions. On Adobe Experience Cloud, AEP unifies the signals, audiences segment risk, Journey Optimizer orchestrates retention journeys and CJA measures retained customers against a control group.",
        "Retention offers often go to customers who would have stayed anyway, while genuinely at-risk customers are reached too late. Without a shared view of risk signals, retention budgets are hard to justify.",
        """<div class="grid-2"><div class="card"><h3>Signals</h3><p>Usage trends, service tickets, billing events, contract dates and digital behaviour.</p></div>
<div class="card"><h3>Risk audiences</h3><p>Rule-based or model-scored segments refreshed on the right cadence.</p></div>
<div class="card"><h3>Save journeys</h3><p>Service recovery, proactive outreach and offers with eligibility rules.</p></div>
<div class="card"><h3>Measurement</h3><p>Control groups and retained-value reporting in CJA.</p></div></div>""",
        [("Define churn", "agree what churn means per product and segment"), ("Signals", "bring the right events and attributes into AEP"), ("Segment", "build and validate risk audiences"), ("Journeys", "design save paths with suppression and caps"), ("Control", "hold out a group to measure true impact"), ("Iterate", "refine signals and offers using results")],
        ["Retention rate versus control", "Cost per retained customer", "Offer take-up among high-risk customers", "Time from risk signal to first contact", "Complaint and opt-out rates", "Retained revenue (where measurable)"],
        ["industries.html", "services/customer-journey-analytics.html", "solutions/real-time-personalization.html"],
        [("Do we need a machine-learning model?", "Not to start. Clear rule-based signals often deliver value first; models can be added once data and measurement are in place.")],
    ),
    solution(
        "solutions/b2b-lead-to-revenue.html",
        "B2B Lead-to-Revenue: Marketo, CRM & AEP Alignment",
        "Align Marketo Engage, CRM and Adobe Experience Platform for B2B: lifecycle stages, scoring, account data, audiences and pipeline reporting.",
        "B2B lead-to-revenue alignment",
        "Solution · B2B",
        ["b2b lead to revenue", "marketo crm alignment", "b2b customer data platform", "lead scoring marketo", "account based marketing data"],
        "B2B lead-to-revenue alignment makes marketing automation, CRM and customer data agree on who a lead is, what stage it is in and when sales should act. Typical components are Marketo Engage for lifecycle and scoring, CRM sync for ownership, Adobe Experience Platform for unified person and account data, and analytics that connect campaigns to pipeline.",
        "Marketing and sales often argue about lead quality because each system defines stages differently. Scoring rules drift, account data is fragmented and pipeline attribution is disputed.",
        """<div class="grid-2"><div class="card"><h3>Lifecycle</h3><p>Shared stage definitions and service-level agreements between marketing and sales.</p></div>
<div class="card"><h3>Scoring</h3><p>Behaviour and fit scoring with owners and review cadence.</p></div>
<div class="card"><h3>Data</h3><p>Person and account data unified in AEP; audiences activated back to Marketo where licensed.</p></div>
<div class="card"><h3>Reporting</h3><p>Campaign-to-pipeline reporting agreed with finance and sales.</p></div></div>
<p>Read more: <a href="../guides/marketo-engage-aep.html">Marketo Engage and AEP</a></p>""",
        [("Align", "agree lifecycle stages and SLAs"), ("Audit", "review scoring, programs and sync rules"), ("Integrate", "connect Marketo, CRM and AEP"), ("Activate", "build account and buying-group audiences"), ("Report", "pipeline reporting with agreed attribution"), ("Govern", "owners and quarterly reviews")],
        ["Lead-to-opportunity conversion", "Speed to lead", "Share of leads with a clear owner", "Scoring accuracy versus closed-won", "Data sync error rate", "Pipeline influenced by programs"],
        ["guides/marketo-engage-aep.html", "services/martech-strategy-advisory.html", "solutions/customer-360.html"],
        [("Can AEP replace Marketo?", "No. They play different roles: Marketo Engage handles B2B marketing automation, while AEP provides unified data and audiences that can feed it.")],
    ),
    dict(
        path="services/adobe-experience-cloud.html",
        bands=True,
        title="Adobe Experience Cloud Consulting: Analytics, Target, AEM & More",
        desc="Consulting across Adobe Experience Cloud: Adobe Analytics, Target, Experience Manager, Campaign, Commerce, Marketo Engage, AEP, RTCDP, AJO and CJA.",
        h1="Adobe Experience Cloud consulting",
        kicker="Platforms",
        keywords=["adobe experience cloud consulting", "adobe analytics consultant", "adobe target consultant", "aem consulting", "adobe campaign consultant", "marketo consultant"],
        answer="Infinite360 consults across the Adobe Experience Cloud: the data foundation (AEP, Real-Time CDP), engagement (Journey Optimizer, Campaign, Marketo Engage), experience (Target, Experience Manager, Commerce) and insight (Adobe Analytics, Customer Journey Analytics). We focus on how these products connect through shared data, identity and governance.",
        schema="Service",
        service_type="Adobe Experience Cloud consulting",
        hero_cta=("Discuss your Adobe stack", "contact-us.html"),
        sections=[
            ("Data foundation", """<div class="tiles">
<a class="tile link-card" href="aep-consulting.html"><span class="abbr">AEP</span><h3>Adobe Experience Platform</h3><p>Schemas, ingestion, identity, profiles and governance.</p></a>
<a class="tile link-card" href="real-time-cdp.html"><span class="abbr">CDP</span><h3>Real-Time CDP</h3><p>Audiences and activation to marketing and advertising destinations.</p></a>
<a class="tile link-card" href="web-sdk-adobe-tags.html"><span class="abbr">SDK</span><h3>Web SDK &amp; Tags</h3><p>Modern data collection through the Edge Network.</p></a></div>""", "plain", "Collect and unify"),
            ("Engagement and orchestration", """<div class="tiles">
<a class="tile link-card" href="adobe-journey-optimizer.html"><span class="abbr">AJO</span><h3>Journey Optimizer</h3><p>Real-time journeys, decisioning and cross-channel messaging.</p></a>
<div class="tile"><span class="abbr">AC</span><h3>Adobe Campaign</h3><p>Campaign orchestration for scheduled, multi-step marketing programs.</p></div>
<a class="tile link-card" href="../guides/marketo-engage-aep.html"><span class="abbr">MKT</span><h3>Marketo Engage</h3><p>B2B lead management, scoring and CRM alignment.</p></a></div>""", "alt", "Engage"),
            ("Experience and commerce", """<div class="tiles">
<div class="tile"><span class="abbr">TGT</span><h3>Adobe Target</h3><p>A/B testing, experience targeting and on-site personalisation.</p></div>
<div class="tile"><span class="abbr">AEM</span><h3>Experience Manager</h3><p>Content and digital asset management feeding personalised experiences.</p></div>
<div class="tile"><span class="abbr">COM</span><h3>Adobe Commerce</h3><p>Commerce data and events connected to profiles and journeys.</p></div></div>""", "plain", "Experience"),
            ("Insight and measurement", """<div class="tiles">
<div class="tile"><span class="abbr">AA</span><h3>Adobe Analytics</h3><p>Digital analytics implementation, tracking and reporting.</p></div>
<a class="tile link-card" href="customer-journey-analytics.html"><span class="abbr">CJA</span><h3>Customer Journey Analytics</h3><p>Cross-channel analysis and attribution on AEP data.</p></a>
<a class="tile link-card" href="agentic-ai-mcp.html"><span class="abbr">AI</span><h3>Agentic AI &amp; MCP</h3><p>Governed AI assistants on top of approved data and tools.</p></a></div>""", "alt", "Measure"),
            ("What we do across the stack", """<ul class="checklist cols-2">
<li>Platform audits and readiness assessments</li><li>Architecture and integration design</li>
<li>Implementation and migration support</li><li>Data collection and governance</li>
<li>Team enablement and runbooks</li><li>Optimisation roadmaps</li></ul>
<p class="small muted">Infinite360 is independent and not an Adobe partner; product availability depends on your Adobe licences.</p>""", "dark", "Capabilities"),
        ],
        faqs=[("Which Adobe products do you implement hands-on?", "Our deepest hands-on focus is AEP, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Adobe Analytics and Web SDK. For other products we advise on architecture and integration and scope delivery per engagement.")],
        sources=[("Adobe Experience League", "https://experienceleague.adobe.com/")],
        related=["services/aep-consulting.html", "solutions/index.html", "services/engagement-model.html"],
    ),
    dict(
        path="pavan-babu-gandla.html",
        bands=True,
        title="Pavan Babu Gandla | Digital Transformation & MarTech Leader",
        desc="Pavan Babu Gandla, founder of Infinite360: Digital Transformation and MarTech leader focused on Adobe Experience Cloud, customer data and Agentic AI.",
        h1="Pavan Babu Gandla",
        kicker="Founder · Digital Transformation & MarTech Leader",
        lede="Adobe Experience Cloud SME and Agentic AI architect helping enterprises turn customer data into revenue, retention and real-time intelligence.",
        keywords=["pavan babu gandla", "adobe experience cloud sme", "martech consultant india", "agentic ai architect", "fractional cdo martech"],
        answer="Pavan Babu Gandla is the founder of Infinite360 and a Digital Transformation and MarTech leader. He focuses on Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, enterprise architecture and Agentic AI, advising CDOs, CTOs and CMOs on customer data and AI transformation.",
        schema="ProfilePage",
        hero_cta=("Book a discovery call", "https://calendar.app.google/5CHbD1hmQBHxcJyy5"),
        sections=[
            ("How I can help", """<div class="grid-3">
<a class="card link-card" href="services/aep-consulting.html"><h3>AEP architecture &amp; implementation</h3><p>XDM, identity, ingestion, profiles and activation &mdash; discovery through go-live.</p></a>
<a class="card link-card" href="services/real-time-cdp.html"><h3>Real-Time CDP strategy</h3><p>Audience strategy, activation, consent and governance.</p></a>
<a class="card link-card" href="services/adobe-journey-optimizer.html"><h3>Journey orchestration (AJO)</h3><p>Journey design, decisioning, suppression and cross-channel orchestration.</p></a>
<a class="card link-card" href="services/customer-journey-analytics.html"><h3>Customer Journey Analytics</h3><p>Workspace architecture, attribution and executive reporting.</p></a>
<a class="card link-card" href="services/agentic-ai-mcp.html"><h3>Agentic AI on Adobe</h3><p>Governed MCP architectures connecting AI agents to approved data and tools.</p></a>
<a class="card link-card" href="services/martech-strategy-advisory.html"><h3>Fractional CDO &amp; advisory</h3><p>Platform decisions, architecture governance, vendor evaluation and AI strategy.</p></a>
</div>""", "plain", "Engagements"),
            ("Expertise", """<div class="logo-band" style="justify-content:flex-start"><span>Adobe Experience Platform</span><span>Real-Time CDP</span><span>Journey Optimizer</span><span>Customer Journey Analytics</span><span>Web SDK</span><span>Identity resolution</span><span>Data governance</span><span>Enterprise architecture</span><span>Agentic AI &amp; MCP</span><span>Google Cloud</span><span>Azure</span><span>Kafka</span><span>Spark</span><span>LangChain</span><span>Adobe I/O</span></div>
<p style="margin-top:20px">Industries: BFSI, retail, telecom, hospitality, healthcare and enterprise technology. Engagements are delivered remotely for organisations across EMEA, APAC and North America.</p>""", "alt", "Focus areas"),
            ("Consulting portfolio", f'<p class="lead">Case studies, insights and certifications are published on the personal consulting portfolio.</p><p class="cta-row"><a class="btn btn-primary" href="{PORTFOLIO}" rel="noopener" target="_blank">Visit martechconsultant.tech</a><a class="btn btn-ghost" href="https://linkedin.com/in/pavanbabu1" rel="noopener" target="_blank">LinkedIn</a></p>', "plain", "More"),
            ("Learn with Pavan", '<p>Pavan leads the Infinite360 Tech Academy career accelerator and corporate programs.</p><p class="cta-row"><a class="btn btn-light" href="training/index.html">Career accelerator</a><a class="btn btn-ghost" style="color:#fff" href="training/corporate-training.html">Corporate training</a></p>', "dark", "Academy"),
        ],
        faqs=[("How do I engage Pavan for consulting?", "Book a discovery call or use the contact form, describing your Adobe stack, the business problem and your timeline.")],
        related=["about-us.html", "services/martech-strategy-advisory.html", "training/index.html"],
    ),
]
