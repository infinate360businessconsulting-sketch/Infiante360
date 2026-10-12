"""Industry use-case pages (12) built from the curated pattern library, plus hands-on projects page.
All use cases are illustrative design patterns, not completed client work."""
import html as _h
from visuals import flow_svg, figure
from content_cases import pills, WHATSAPP_MSG, REGISTER
from usecase_patterns import P

e = _h.escape
EL = "https://experienceleague.adobe.com/en/docs"

# slug, name, customer, product, event_a, event_b, sources, starter flow, risk sentence, pattern indices, extra intro
IND = [
("banking", "Banking", "account holder", "account", "login", "loan-application-start",
 ["Core banking and account events", "Digital banking app and web events", "CRM and contact preferences", "Consent and marketing permissions", "Call-centre and branch interactions"],
 [("Login", "authenticated"), ("Intent signal", "loan page"), ("Consent check", ""), ("Eligible audience", "governed"), ("Journey", "AJO"), ("Measure", "holdout")],
 "Keep financial attributes and credit-related decisions out of advertising destinations, and involve compliance before any eligibility-based messaging.",
 [0, 2, 12, 14, 41, 45, 70, 78, 92, 98]),
("insurance", "Insurance", "policyholder", "policy", "quote-start", "renewal-window",
 ["Policy administration and renewal dates", "Quote and purchase journeys", "Claims status events", "Agent and broker data", "Consent and communication preferences"],
 [("Quote start", "event"), ("Wait", ""), ("Quote finished?", "exit"), ("Consent", ""), ("Reminder", "AJO"), ("Advisor offer", "")],
 "Treat health and claims data as restricted; do not use it for cross-sell targeting without legal review.",
 [3, 10, 31, 33, 40, 43, 49, 71, 90, 99]),
("retail", "Retail", "shopper", "product", "product-view", "cart-add",
 ["Web and app events", "Point-of-sale and store transactions", "Loyalty programme data", "Product catalogue and inventory", "Email and push consent"],
 [("Product view", "event"), ("Cart add", "event"), ("Wait", "1 hour"), ("Purchased?", "exit"), ("Reminder", "AJO"), ("Measure", "holdout")],
 "Exclude payment data and keep sensitive product categories out of retargeting audiences.",
 [4, 11, 20, 23, 32, 34, 45, 62, 85, 89]),
("travel", "Travel", "traveller", "booking", "search", "booking-abandon",
 ["Search and booking events", "Reservation and ticketing systems", "Loyalty and profile data", "Disruption feeds", "Contact preferences"],
 [("Search", "event"), ("Abandon", "no booking"), ("Alternative", "date or fare"), ("Consent", ""), ("Message", "AJO"), ("Measure", "")],
 "Do not store passport or document details in marketing profiles, and respect each market's consent rules.",
 [4, 12, 25, 36, 47, 55, 61, 77, 87, 94]),
("telecom", "Telecom", "subscriber", "plan", "usage-alert", "bill-shock",
 ["Usage and network events", "Billing and payment events", "Contract and plan data", "Care interactions", "Channel and consent preferences"],
 [("Usage alert", "event"), ("Plan fit", "check"), ("Consent", ""), ("Message", "SMS or app"), ("Care task", "if needed"), ("Measure", "")],
 "Location and usage data are sensitive; limit use to consented, necessary purposes.",
 [13, 20, 31, 40, 41, 44, 70, 72, 91, 98]),
("healthcare", "Healthcare providers", "patient", "appointment", "portal-login", "missed-appointment",
 ["Appointment and scheduling events", "Patient portal events (non-clinical)", "Communication preferences", "Provider directory", "Consent records"],
 [("Appointment", "scheduled"), ("Reminder", "preferred channel"), ("Missed?", "event"), ("Rebook offer", ""), ("Consent check", ""), ("Measure", "")],
 "Do not place clinical data in the marketing platform; run every message design through compliance review.",
 [10, 15, 21, 51, 55, 73, 74, 77, 94, 98]),
("hospitality", "Hospitality", "guest", "stay", "booking", "pre-arrival",
 ["Reservation and property systems", "Loyalty tier data", "Web and app events", "On-property transactions", "Guest preferences and consent"],
 [("Booking", "event"), ("Pre-arrival", "3 days"), ("Preferences", "capture"), ("Upgrade offer", "AJO"), ("Stay", ""), ("Review request", "")],
 "Identity documents and payment details stay out of the profile; use preferences the guest has given.",
 [10, 13, 30, 35, 60, 62, 64, 69, 82, 90]),
("media", "Media and streaming", "viewer", "subscription", "title-start", "session-drop",
 ["Playback and content events", "Subscription and billing events", "Device and app data", "Content metadata", "Viewing-consent records"],
 [("Title start", "event"), ("Session drop", "signal"), ("Next title", "decisioning"), ("Prompt", "in-app"), ("Retain", ""), ("Measure", "")],
 "Treat viewing history as personal data and give viewers a clear way to adjust personalisation.",
 [21, 22, 24, 26, 36, 40, 43, 48, 82, 88]),
("education", "Higher education", "applicant", "programme", "enquiry", "application-start",
 ["Enquiry and application events", "Student information system (limited)", "Event and open-day registrations", "Communication preferences", "Consent records"],
 [("Enquiry", "event"), ("Programme interest", "profile"), ("Counsellor task", "if consented"), ("Reminder", "AJO"), ("Apply", ""), ("Measure", "")],
 "Exclude minors from marketing journeys and restrict academic or financial-aid data.",
 [5, 7, 11, 13, 17, 31, 45, 58, 73, 99]),
("manufacturing", "Manufacturing", "dealer", "product line", "catalogue-view", "order",
 ["Dealer and distributor orders", "Catalogue and product data", "Warranty and service records", "CRM account data", "Portal events"],
 [("Catalogue view", "event"), ("Order history", "profile"), ("Restock prompt", "AJO"), ("Account task", "CRM"), ("Order", ""), ("Measure", "")],
 "Keep contract pricing and terms out of marketing profiles and honour account-level data access rules.",
 [1, 11, 20, 33, 39, 46, 48, 75, 91, 97]),
("public-sector", "Public sector", "citizen", "service", "portal-visit", "form-abandon",
 ["Service portal events", "Form and application status", "Contact preferences", "Accessibility needs (with consent)", "Case-management references"],
 [("Portal visit", "event"), ("Form abandon", "signal"), ("Reminder", "consented channel"), ("Help option", "callback"), ("Complete", ""), ("Measure", "")],
 "Apply strict consent, accessibility and retention rules; do not profile citizens beyond service delivery.",
 [4, 7, 14, 18, 71, 72, 74, 76, 93, 98]),
("saas", "SaaS", "trial user", "workspace", "signup", "feature-use",
 ["Product usage events", "Subscription and billing data", "CRM and support data", "Account hierarchy", "Marketing consent"],
 [("Sign-up", "event"), ("Feature use", "event"), ("Milestone?", "branch"), ("In-app guide", "AJO"), ("Upgrade prompt", ""), ("Measure", "")],
 "Separate workspace and customer data from marketing profiles and honour account-level admin settings.",
 [10, 11, 15, 16, 26, 31, 36, 44, 85, 96]),
]

def _fmt(s, d):
    return s.format(customer=d["cust"], product=d["prod"], event_a=d["ea"], event_b=d["eb"])

def _rows(d):
    out = []
    for i in d["idx"]:
        cat, name, trig, comp, ch, kpi = P[i]
        out.append((cat, _fmt(name, d), _fmt(trig, d), comp, ch, kpi))
    return out

def industry_page(row):
    slug, name, cust, prod, ea, eb, sources, flow, risk, idx = row
    d = dict(cust=cust, prod=prod, ea=ea, eb=eb, idx=idx)
    rows = _rows(d)
    tbl = ('<div class="table-wrap"><table><thead><tr><th>Category</th><th>Use case</th><th>Trigger</th><th>Adobe components</th><th>Channel</th><th>KPI to measure</th></tr></thead><tbody>'
           + "".join(f"<tr><td>{e(c)}</td><th scope=\"row\">{e(n)}</th><td>{e(t)}</td><td>{e(co)}</td><td>{e(ch)}</td><td>{e(k)}</td></tr>" for c, n, t, co, ch, k in rows)
           + "</tbody></table></div>")
    return dict(
        path=f"use-cases/industries/{slug}.html",
        title=f"{name} Use Cases: AEP, RTCDP & Journey Optimizer"[:64],
        desc=f"Ten illustrative {name.lower()} use cases on Adobe Experience Platform: triggers, components, channels, KPIs and the governance checks to run first.",
        h1=f"{name} MarTech use cases on Adobe Experience Platform",
        kicker="Industry use cases", nav=name, schema="Article", category="Use cases", date="2026-10-12",
        keywords=[f"{name.lower()} aep use cases", f"{name.lower()} customer data platform", f"{name.lower()} journey optimizer", f"{name.lower()} personalisation", f"{name.lower()} martech"],
        answer=f"These ten {name.lower()} use cases show how a {cust} signal such as {ea} or {eb} can drive a governed journey on Adobe Experience Platform, Real-Time CDP and Journey Optimizer. They are illustrative design patterns for planning, with the KPI to measure for each, not delivered client results.",
        sections=[
            ("Read this first", '<p class="note"><strong>Illustrative designs.</strong> Each row is a planning pattern. It is not evidence of a completed client engagement and lists metrics to track, not results. Validate identity, consent and data quality in your own environment first.</p>'),
            ("Starting journey", figure(flow_svg(f"{name}: starting journey", flow), f"A starting journey for {name.lower()}.")),
            ("Ten use cases", tbl),
            ("Data you will need", '<ul class="checklist">' + "".join(f"<li>{e(s)}</li>" for s in sources) + "</ul>"),
            (f"Governance for {name.lower()}", f"<p>{e(risk)}</p><ul class=\"checklist\"><li>Check consent and channel permissions before every send</li><li>Use a holdout group so the KPI shows real lift</li><li>Document data sources, owners and retention</li></ul>"),
            ("Build or learn this", pills(("Request an architecture review", "../../lp/aep-architecture-review.html"), ("All industries", "index.html"), ("Learn to build it", "../../training/index.html"), ("50-use-case library", "../real-time-use-case-library.html"))),
        ],
        faqs=[(f"Are these {name.lower()} use cases client results?", "No. They are illustrative design patterns. Real client work is published only with written approval and evidence."),
              ("Which Adobe products are involved?", "Mostly Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics, with Web SDK for data collection.")],
        related=["use-cases/index.html", "services/adobe-journey-optimizer.html", "services/real-time-cdp.html"],
        sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform"), ("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer")],
    )

INDUSTRY_PAGES = [industry_page(r) for r in IND]

HUB = dict(
    path="use-cases/industries/index.html",
    title="Industry MarTech Use Cases: Banking, Retail, Travel & More",
    desc="Illustrative Adobe MarTech use cases by industry: banking, insurance, retail, travel, telecom, healthcare, hospitality, media, education and more.",
    h1="MarTech use cases by industry",
    kicker="Industry use cases", nav="Industry use cases", schema="CollectionPage", category="Use cases",
    keywords=["martech use cases by industry", "aep use cases banking", "rtcdp retail use cases", "journey optimizer telecom", "industry customer data platform"],
    answer="This hub lists twelve industries with ten illustrative Adobe MarTech use cases each, covering triggers, components, channels, KPIs and governance. Each page is a planning pattern, not a completed client engagement. A full pattern library of 4,000 variations exists as a downloadable working file, not as site pages.",
    sections=[("Industries", '<div class="grid-2">' + "".join(f'<a class="card link-card" href="{p["path"].split("/")[-1]}"><span class="tag">Industry</span><h3>{p["nav"]}</h3><p>{p["answer"][:130]}...</p></a>' for p in INDUSTRY_PAGES) + "</div>"),
              ("Next", pills(("All use cases", "../index.html"), ("Case studies", "../../case-studies/index.html"), ("Request an architecture review", "../../lp/aep-architecture-review.html")))],
    faqs=[], related=["use-cases/index.html", "solutions/index.html", "industries.html"],
)

PROJECTS = [
 ("Enterprise Customer 360", "Sources, XDM, identity, Profile, audiences and activation, end to end."),
 ("Real-time transaction journey", "A streaming event feeds Profile, triggers an AJO journey and sends a message."),
 ("RTCDP activation", "Segment strategy, qualification, destinations and activation QA."),
 ("CJA executive intelligence", "Cross-channel journey analysis and KPI storytelling in Workspace."),
 ("Web SDK modernisation", "Data layer to Web SDK to datastream to AEP event flow."),
 ("Agentic AI marketing assistant", "An agent with governed tools, customer context and workflow automation."),
]
PROJECT_PAGE = dict(
    path="academy/hands-on-projects.html",
    title="Hands-On Adobe MarTech Projects & Capstone Portfolio",
    desc="Six hands-on Adobe MarTech projects for your portfolio: Customer 360, real-time journey, RTCDP activation, CJA, Web SDK and an Agentic AI assistant.",
    h1="Hands-on Adobe MarTech projects and capstone portfolio",
    kicker="Academy projects", nav="Projects", schema="Article", category="Academy", date="2026-10-12",
    keywords=["aep projects for portfolio", "adobe experience platform hands-on project", "customer 360 project", "ajo journey project", "cja dashboard project"],
    answer="Infinite360 Tech Academy learners build six enterprise-style projects on practice environments: Customer 360, a real-time transaction journey, RTCDP activation, a CJA executive dashboard, Web SDK modernisation and an Agentic AI marketing assistant. They give you evidence of practical skill for interviews. They do not guarantee a job.",
    sections=[
        ("The six projects", '<ol class="steps">' + "".join(f"<li><strong>{n}.</strong> {e(t)}</li>" for n, t in PROJECTS) + "</ol>"),
        ("How the projects work", '<ul class="checklist"><li>Built on simulation or sandbox environments with synthetic data</li><li>Each ends with documentation you can show in an interview</li><li>Reviewed against a checklist for schema, identity, consent and measurement</li><li>Part of the Career Accelerator and the recorded Foundation + Advanced course</li></ul>'),
        ("Join", pills(("Career Accelerator", "../training/index.html"), ("Register", REGISTER), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Do the projects guarantee a job?", "No. They give you practical evidence of your skills. Hiring depends on your experience and the market.")],
    related=["academy/index.html", "academy/simulators.html", "training/index.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
)

INDUSTRY_ALL = [HUB] + INDUSTRY_PAGES + [PROJECT_PAGE]
