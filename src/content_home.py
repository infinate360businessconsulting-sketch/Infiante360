"""Homepage (long-form corporate layout) and shared fee constant."""
from visuals import architecture_svg
from content_academy import program_cards, course_tiles

COURSE_FEE_INR = 60000
COURSE_FEE_LABEL = "₹60,000"
REG_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfKeY_33fgEBKYskgG2shgRcYLvHx50ES_KqrULMKromsE3mg/viewform?usp=header"

TIERS = """
<div class="tiers">
<div class="tier"><span class="verb">Advise me</span><h3>Strategy &amp; architecture</h3><p>Readiness assessments, architecture reviews and roadmaps for leadership decisions.</p><ul><li>MarTech audit</li><li>Target architecture</li><li>30/60/90-day plan</li></ul><a class="more" href="services/martech-strategy-advisory.html">Advisory &rarr;</a></div>
<div class="tier"><span class="verb">Teach me</span><h3>Capability building</h3><p>Role-based corporate programs and an individual career accelerator.</p><ul><li>Hands-on labs</li><li>Assessments</li><li>Capstones</li></ul><a class="more" href="training/corporate-training.html">Training &rarr;</a></div>
<div class="tier"><span class="verb">Build with me</span><h3>Co-delivery</h3><p>We work alongside your team to activate priority use cases.</p><ul><li>Use-case sprints</li><li>Pairing &amp; reviews</li><li>Knowledge transfer</li></ul><a class="more" href="services/engagement-model.html">Engagement model &rarr;</a></div>
<div class="tier"><span class="verb">Build for me</span><h3>Implementation</h3><p>End-to-end delivery of AEP, RTCDP, AJO, CJA and integrations.</p><ul><li>Architecture to go-live</li><li>QA &amp; governance</li><li>Runbooks</li></ul><a class="more" href="services/aep-consulting.html">Implementation &rarr;</a></div>
<div class="tier"><span class="verb">Extend my team</span><h3>Specialist capacity</h3><p>Engineers, analysts and architects who join your delivery process.</p><ul><li>AEP &amp; Adobe engineers</li><li>Data &amp; integration</li><li>Architects</li></ul><a class="more" href="services/staff-augmentation.html">Staff augmentation &rarr;</a></div>
</div>"""

PLATFORMS = """
<div class="tiles">
<a class="tile link-card" href="adobe-experience-platform/index.html"><span class="abbr">AEP</span><h3>Adobe Experience Platform</h3><p>XDM, ingestion, identity, Real-Time Customer Profile and governance.</p></a>
<a class="tile link-card" href="services/real-time-cdp.html"><span class="abbr">CDP</span><h3>Real-Time CDP</h3><p>Audiences, activation and Customer 360 for marketing and advertising.</p></a>
<a class="tile link-card" href="services/adobe-journey-optimizer.html"><span class="abbr">AJO</span><h3>Journey Optimizer</h3><p>Event and audience journeys, decisioning and cross-channel messaging.</p></a>
<a class="tile link-card" href="services/customer-journey-analytics.html"><span class="abbr">CJA</span><h3>Customer Journey Analytics</h3><p>Cross-channel analysis, attribution and executive reporting.</p></a>
<a class="tile link-card" href="services/web-sdk-adobe-tags.html"><span class="abbr">SDK</span><h3>Web SDK &amp; Tags</h3><p>Data layers, datastreams, consent and Edge Network collection.</p></a>
<a class="tile link-card" href="services/adobe-experience-cloud.html"><span class="abbr">AXC</span><h3>Wider Experience Cloud</h3><p>Adobe Analytics, Target, AEM, Campaign, Commerce and Marketo Engage.</p></a>
</div>"""

HOME = dict(
    path="index.html",
    nav="Home",
    bands=True,
    hero_ctas=True,
    hero_visual=architecture_svg(),
    title="Infinite360 | Adobe MarTech Consulting, AEP Training & AI",
    desc="Adobe MarTech consulting and training for AEP, Real-Time CDP, Journey Optimizer, CJA and Agentic AI — for enterprise teams and professionals.",
    lede="Enterprise MarTech, customer data and AI transformation. We help organisations design, implement and scale Adobe Experience Cloud — and build the teams that run it.",
    h1="Turn customer data into intelligent experiences",
    kicker="Adobe MarTech · Customer Data · Agentic AI",
    keywords=["adobe martech consulting", "adobe experience platform training", "aep consultant india", "martech consultant", "agentic ai martech", "adobe experience cloud consultant"],
    answer="Infinite360 is an Adobe MarTech consulting and learning brand. We help enterprises design and implement Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics, and help professionals build practical AEP and Agentic AI skills through hands-on training and free guides.",
    schema="WebPage",
    sections=[
        ("Technologies we work with", '<div class="logo-band"><span>Adobe Experience Platform</span><span>Real-Time CDP</span><span>Journey Optimizer</span><span>Customer Journey Analytics</span><span>Adobe Analytics</span><span>Web SDK &amp; Tags</span><span>Target</span><span>AEM</span><span>Marketo Engage</span><span>Snowflake</span><span>BigQuery</span><span>Databricks</span><span>Kafka</span><span>Agentic AI &amp; MCP</span></div>', "plain", "Platform expertise"),
        ("Three journeys, one ecosystem", """
<div class="grid-3">
<a class="card link-card accent-red" href="services/index.html"><span class="tag">Enterprise consulting</span><h3>Architecture &amp; implementation</h3><p>For CDOs, CTOs, CMOs and MarTech leaders: AEP, RTCDP, AJO, CJA, Web SDK, data engineering and governed AI.</p><span class="more">Explore services &rarr;</span></a>
<a class="card link-card accent-blue" href="training/corporate-training.html"><span class="tag">Capability building</span><h3>Corporate training</h3><p>For L&amp;D, CoE and delivery leaders: role-based, project-based enablement with assessments.</p><span class="more">Corporate training &rarr;</span></a>
<a class="card link-card accent-green" href="training/index.html"><span class="tag">Tech Academy</span><h3>Career accelerator</h3><p>For professionals and career switchers: live online Adobe MarTech and Agentic AI training.</p><span class="more">View the program &rarr;</span></a>
</div>""", "alt", "Who we help"),
        ("Engage the way you need", TIERS, "plain", "Engagement options"),
        ("The Adobe Experience Cloud, connected", PLATFORMS, "alt", "Platforms"),
        ("From audit to scale", """
<p class="lead">Every engagement follows a clear path, so leadership sees progress and teams build lasting capability.</p>
<div class="timeline">
<div class="step"><h3>Discover &amp; diagnose</h3><p>Audit experience, data, MarTech, AI, engineering and skills.</p></div>
<div class="step"><h3>Strategize</h3><p>Prioritised use cases, target architecture and a 30/60/90-day plan.</p></div>
<div class="step"><h3>Enable &amp; build</h3><p>Train teams, deliver proofs of concept and implement with governance.</p></div>
<div class="step"><h3>Scale</h3><p>Transfer knowledge, set standards and keep optimising.</p></div>
</div>
<p style="margin-top:20px"><a href="services/engagement-model.html">See the full engagement model &rarr;</a></p>""", "dark", "How we work"),
        ("Solution patterns we deliver", """
<div class="grid-2">
<a class="card link-card" href="solutions/customer-360.html"><h3>Customer 360 &amp; identity</h3><p>Unify CRM, web, app and offline data into governed, real-time profiles.</p></a>
<a class="card link-card" href="solutions/real-time-personalization.html"><h3>Real-time personalisation</h3><p>Act on behaviour in the moment across web, app, email and paid media.</p></a>
<a class="card link-card" href="solutions/churn-prevention.html"><h3>Retention &amp; churn prevention</h3><p>Detect risk signals and orchestrate save journeys with measurement.</p></a>
<a class="card link-card" href="solutions/b2b-lead-to-revenue.html"><h3>B2B lead-to-revenue</h3><p>Align Marketo, CRM and AEP so lead stages, scoring and audiences agree.</p></a>
</div>
<p><a href="solutions/index.html">All solutions &rarr;</a></p>""", "plain", "Solutions"),
        ("Industries", """
<div class="grid-3">
<div class="card"><h3>BFSI</h3><p>Strict identity, sensitive-data governance, onboarding and cross-sell journeys.</p></div>
<div class="card"><h3>Retail &amp; e-commerce</h3><p>Web, app, store and loyalty data with abandonment and suppression journeys.</p></div>
<div class="card"><h3>Telecom</h3><p>Churn signals, upgrade journeys and household identity.</p></div>
<div class="card"><h3>Travel &amp; hospitality</h3><p>Booking-to-stay lifecycle, loyalty profiles and real-time offers.</p></div>
<div class="card"><h3>Healthcare</h3><p>Consent-first engagement and strict data minimisation.</p></div>
<div class="card"><h3>Enterprise technology</h3><p>B2B lead management, account data and product-led journeys.</p></div>
</div>
<p><a href="industries.html">Explore industries &rarr;</a></p>""", "alt", "Where we focus"),
        ("Infinite360 Tech Academy", f"""
<div class="split">
<div><p class="lead">A live, online, hands-on career accelerator for Adobe Experience Platform, Real-Time CDP, Journey Optimizer, CJA, Web SDK and Agentic AI &mdash; built around projects, troubleshooting and interview preparation.</p>
<ul class="checklist"><li>Six phases with enterprise-style projects</li><li>Architect-level troubleshooting scenarios</li><li>Career mapping and interview preparation</li></ul>
<p class="cta-row"><a class="btn btn-light" href="academy/index.html">View all programs</a><a class="btn btn-ghost" style="color:#fff" href="{REG_FORM}" rel="noopener" target="_blank">Register</a></p></div>
<div class="price-card" style="background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.18);box-shadow:none"><div><div class="price" style="color:#fff">{COURSE_FEE_LABEL}<small style="color:#ffd5d8">Career accelerator program fee</small></div></div><p style="margin:0">Live online sessions, labs, projects and career support. Contact us for corporate pricing.</p></div>
</div>""", "red", "Learn"),
        ("Upcoming: AEP Launchpad bootcamp", '<div class="split"><div><p class="lead">Sunday, 11 October 2026 · 6:00 – 9:00 PM IST · live online · ₹3,000</p><p><strong>Free bonus:</strong> ₹3,500 Interview &amp; Certification Test Series for every attendee.</p><p class="cta-row"><a class="btn btn-light" href="academy/aep-launchpad-bootcamp.html">View the bootcamp</a><a class="btn btn-ghost" style="color:#fff" href="academy/workshops.html">Friday workshops</a></p></div><div><p>Next live Foundations batch starts <strong>15 October, 8:00 – 9:30 AM IST</strong>, Monday–Friday for two weeks.</p><p><a href="academy/aep-foundations-batch.html" style="color:#fff">See the batch plan &rarr;</a></p></div></div>', "red", "Workshops &amp; bootcamps"),
        ("Academy programs and fees", program_cards(0) + '<h3 style="margin-top:32px">Single-tool courses</h3>' + course_tiles(0) + '<p style="margin-top:16px"><a href="academy/index.html">Explore the academy &rarr;</a> &middot; <a href="academy/videos.html">Watch free demo sessions &rarr;</a></p>', "alt", "Course catalog"),
        ("Free guides and answers", """
<div class="grid-3">
<a class="card link-card" href="adobe-experience-platform/index.html"><h3>The AEP guide</h3><p>Schemas to activation, step by step.</p></a>
<a class="card link-card" href="guides/aep-vs-real-time-cdp.html"><h3>AEP vs Real-Time CDP</h3><p>What is the difference?</p></a>
<a class="card link-card" href="guides/cja-vs-adobe-analytics.html"><h3>CJA vs Adobe Analytics</h3><p>Use cases and trade-offs.</p></a>
<a class="card link-card" href="adobe-experience-platform/identity-service.html"><h3>Identity resolution</h3><p>Namespaces, graphs and graph collapse.</p></a>
<a class="card link-card" href="guides/what-is-mcp.html"><h3>What is MCP?</h3><p>Safe agentic AI for enterprise MarTech.</p></a>
<a class="card link-card" href="guides/marketo-engage-aep.html"><h3>Marketo Engage and AEP</h3><p>Lead lifecycle, scoring and integration.</p></a>
</div>
<p><a href="learn/index.html">All learning hubs &rarr;</a></p>""", "plain", "Insights"),
    ],
    faqs=[
        ("What does Infinite360 do?", "Infinite360 provides Adobe MarTech consulting, corporate training and a Tech Academy career accelerator focused on Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, data engineering and Agentic AI."),
        ("How much does the career accelerator cost?", "The career accelerator program fee is ₹60,000. Corporate training is priced per engagement."),
        ("How do I contact Infinite360?", "Use the contact form, WhatsApp +91 82968 93895, or book a call from the contact page."),
    ],
    related=["services/index.html", "solutions/index.html", "pavan-babu-gandla.html"],
)
