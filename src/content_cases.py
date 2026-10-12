"""Case studies (simulation-based implementation projects and training delivery models),
contract hiring, simulators and the learner recording platform.

Integrity rule: implementation case studies are built on Infinite360 Tech Academy simulation
environments with synthetic data. They describe scope, architecture and approach only - no client
names, endorsements or invented results.
"""
from visuals import flow_svg, layers_svg, figure

REGISTER = "https://techacademy.infinate360.in"
WHATSAPP_MSG = "https://wa.me/message/CHZQWLVK32OTI1"
LMS = "https://martechlms.infiante360techacademy.com"
BROCHURE = "/brochures.html"
LI_GROUP = "https://www.linkedin.com/groups/13904850"
LI_COMPANY = "https://www.linkedin.com/company/30928383"
APPROACH_VIDEO = "https://youtu.be/myBbVjB9vXo"
FOCUS = "https://aboutus.infiante360techacademy.com"
AGENTIC = "https://agenticaiskills.infiante360techacademy.com"
MARTECH_PAGE = "https://infiante360techacademy.com/Martech.html"

SIMULATORS = [
    ("Adobe MarTech Consultant Portal", "https://adobe.martechconsultant.tech/", "Consulting",
     ["AEP implementation scenarios", "RTCDP use cases", "Journey design workshops", "Consulting frameworks", "Architecture documentation", "Client engagement simulations"]),
    ("AEP Simulator", "https://aepsimualtor.infiante360techacademy.com/", "Platform",
     ["Schema design", "Identity management", "Data ingestion", "Query Service", "Segmentation", "Activation workflows"]),
    ("Banking (BFSI) simulator", "https://anibanking.infiante360techacademy.com/", "BFSI",
     ["Banking customer journeys", "Loan applications", "Customer acquisition flows", "Cross-sell and upsell", "Real-time personalisation"]),
    ("Airline experience simulator", "https://appify.infiante360techacademy.com/", "Travel",
     ["Mobile engagement", "Customer lifecycle management", "Journey optimisation", "Event-based personalisation"]),
    ("Hospitality &amp; services simulator", "https://aramark.infiante360techacademy.com/", "Hospitality",
     ["Hospitality and services scenarios", "Customer service journeys", "Loyalty programs", "Operational analytics"]),
    ("Insurance simulator", "https://insurance.infiante360techacademy.com/", "Insurance",
     ["Policy onboarding journeys", "Claims management", "Customer retention programs", "Renewal campaign automation"]),
    ("Telecom simulator", "https://tele.infiante360techacademy.com/", "Telecom",
     ["Subscriber acquisition", "Churn prevention", "Network-event personalisation", "Customer lifecycle journeys"]),
]
SIM_URL = {s[2]: s[1] for s in SIMULATORS}

SIM_NOTE = ('<p class="note"><strong>About this case study:</strong> this is an Infinite360 Tech Academy project case study delivered on a '
            'simulation environment with synthetic data. It shows the scope, architecture and approach our consultants and learners practise. '
            'It is not a client engagement and implies no affiliation with, or endorsement by, any company or brand.</p>')

LINK_PILLS = (f'<div class="link-pills">'
              f'<a href="{REGISTER}" rel="noopener" target="_blank">Register at the Tech Academy</a>'
              f'<a href="{WHATSAPP_MSG}" rel="noopener" target="_blank">Ask on WhatsApp</a>'
              f'<a href="{BROCHURE}">Download the program brochure</a>'
              f'<a href="{LMS}" rel="noopener" target="_blank">Open the MarTech LMS</a>'
              f'<a href="{LI_GROUP}" rel="noopener" target="_blank">Join the LinkedIn group</a></div>')


def pills(*links):
    ext = ' rel="noopener" target="_blank"'
    return '<div class="link-pills">' + "".join(
        f'<a href="{u}"{ext if u.startswith("http") else ""}>{t}</a>' for t, u in links) + "</div>"


def _glance(rows):
    return '<div class="table-wrap"><table class="glance"><tbody>' + "".join(f"<tr><th scope=\"row\">{k}</th><td>{v}</td></tr>" for k, v in rows) + "</tbody></table></div>"


def _cards(items):
    return '<div class="grid-3">' + "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + "</div>"


BRINGS = [
    ("Architecture first", "A documented target architecture, identity strategy and data model before a single journey is built."),
    ("Reusable accelerators", "Schema patterns, naming conventions, backlog templates, QA checklists and runbooks reused across projects."),
    ("Validation discipline", "Every stage is validated - payloads, identity graphs, profile fragments, audience counts and journey test runs."),
    ("Governance built in", "Consent, data usage labels and least-privilege access are designed in, not bolted on at go-live."),
    ("Knowledge transfer", "Walkthrough recordings, documentation and pairing so your team can run and extend the solution."),
    ("Day-one-ready people", "Consultants and contract engineers who have practised the same pattern end to end before joining your team."),
]


def case_study(path, title, desc, h1, keywords, answer, industry, sim_key, platforms, roles, challenge, layers, flow, use_cases, validation, faqs, related):
    sim = SIM_URL[sim_key]
    return dict(
        path=path, title=title, desc=desc, h1=h1, kicker=f"Case study · {industry}", keywords=keywords, answer=answer,
        schema="Article", category="Case studies", date="2026-10-11",
        hero_cta=("Explore the simulator", sim),
        sections=[
            ("Case study at a glance", SIM_NOTE + _glance([
                ("Industry", industry), ("Platforms", platforms), ("Type", "Academy project case study (simulated environment, synthetic data)"),
                ("Roles practised", roles), ("Environment", f'<a href="{sim}" rel="noopener" target="_blank">{sim.split("//")[1].rstrip("/")}</a>')])),
            ("The business challenge", challenge),
            ("Target architecture", figure(layers_svg(f"{industry} reference architecture", layers), f"Reference architecture used in the {industry.lower()} case study.")),
            ("Implementation approach", figure(flow_svg(f"{industry} delivery flow", flow), "Delivery sequence: each stage is validated before the next starts.")
             + '<ol class="steps">' + "".join(f"<li><strong>{a}</strong> &mdash; {b}</li>" for a, b in flow) + "</ol>"),
            ("Use cases implemented", '<ul class="checklist cols-2">' + "".join(f"<li>{u}</li>" for u in use_cases) + "</ul>"),
            ("Validation and governance checks", '<ul class="checklist">' + "".join(f"<li>{v}</li>" for v in validation) + "</ul>"),
            ("What Infinite360 brings", _cards(BRINGS)),
            ("From case study to contract delivery", f'<p>The roles that practise this case study &mdash; {roles} &mdash; are the same profiles we place through <a href="../services/contract-hiring.html">contract hiring</a> and <a href="../services/staff-augmentation.html">staff augmentation</a>. Because they have already built this pattern end to end, onboarding focuses on your systems and standards rather than on learning the platform.</p>'
             + pills(("Explore the simulator", sim), ("Hire contract talent", "../lp/hire-aep-contract-talent.html"), ("Request an architecture review", "../lp/aep-architecture-review.html"), ("Register for training", REGISTER))),
        ],
        faqs=faqs, related=related,
        sources=[("Adobe Experience Platform documentation", "https://experienceleague.adobe.com/en/docs/experience-platform"),
                 ("Adobe Journey Optimizer documentation", "https://experienceleague.adobe.com/en/docs/journey-optimizer")],
    )


CASES = [
    case_study(
        "case-studies/banking-customer-360-cross-sell.html",
        "BFSI Case Study: Banking Customer 360 & Cross-Sell on AEP",
        "Banking case study on Adobe Experience Platform: Customer 360, loan-application journeys, cross-sell audiences and governed real-time personalisation.",
        "Banking Customer 360 and cross-sell on Adobe Experience Platform",
        ["banking customer 360 aep", "bfsi adobe experience platform case study", "loan application journey ajo", "bank cross-sell personalisation", "rtcdp banking"],
        "This banking case study builds a governed Customer 360 on Adobe Experience Platform from core banking, CRM, web and app data, then uses Real-Time CDP audiences and Journey Optimizer to recover abandoned loan applications and run consent-aware cross-sell journeys. It is delivered on the Infinite360 banking simulator with synthetic data.",
        "BFSI", "BFSI", "AEP, Real-Time CDP, Journey Optimizer, CJA, Web SDK", "AEP data engineer, identity architect, AJO developer, CJA analyst",
        "<p>A retail bank holds customer data in core banking, CRM, card and digital channels, each with its own identifier. Marketing cannot see a single customer, loan applications that stall are not followed up in time, and cross-sell offers ignore products the customer already holds. Strict regulation means consent and sensitive-data handling must be provable.</p>",
        [("Sources", ["Core banking", "CRM", "Cards", "Web &amp; app"]), ("Collect", ["Batch files", "Streaming", "Web SDK"]),
         ("AEP", ["XDM", "Identity graph", "Profile", "Consent"]), ("Activate", ["RTCDP audiences", "AJO journeys", "Destinations"]), ("Measure", ["CJA", "Dashboards"])],
        [("Use-case discovery", "loan, cross-sell, onboarding"), ("XDM &amp; identity", "CRM ID primary, ECID"), ("Ingestion", "batch + streaming"),
         ("Profile &amp; consent", "merge policy, labels"), ("Audiences &amp; journeys", "RTCDP + AJO"), ("Measure in CJA", "funnel + attribution")],
        ["Loan-application drop-off recovery journey", "Credit-card cross-sell excluding existing holders", "New-to-bank onboarding series",
         "Consent-aware email and SMS orchestration", "High-value customer audience for paid-media suppression", "Branch and digital funnel reporting in CJA"],
        ["Identity namespaces documented with owners; CRM ID chosen as the authenticated anchor", "Sensitive attributes labelled before ingestion and blocked from ad destinations",
         "Profile fragments checked for representative synthetic customers", "Journey test mode run for eligible, ineligible and partial profiles", "Audience counts reconciled against source extracts"],
        [("Is this a real bank engagement?", "No. It is a simulation-based project using synthetic data, designed to mirror the scope of a banking AEP program."),
         ("Which identity is primary for banking profiles?", "Typically the CRM or customer ID for authenticated data, with ECID linking anonymous web and app behaviour; the final choice depends on the bank's identity strategy.")],
        ["use-cases/loan-application-drop-off.html", "solutions/customer-360.html", "academy/simulators.html"],
    ),
    case_study(
        "case-studies/airline-mobile-journey-orchestration.html",
        "Airline Case Study: Mobile Engagement & Journey Orchestration",
        "Airline case study: mobile app engagement, booking-to-boarding lifecycle and event-based personalisation with AEP and Adobe Journey Optimizer.",
        "Airline mobile engagement and journey orchestration",
        ["airline customer journey ajo", "travel mobile personalisation aep", "flight disruption notification journey", "airline cdp case study", "mobile sdk aep airline"],
        "This airline case study connects mobile app events, bookings and loyalty data in Adobe Experience Platform, then orchestrates booking-to-boarding journeys and disruption notifications in Journey Optimizer with event-based personalisation. It runs on the Infinite360 airline simulator using synthetic passenger and flight data.",
        "Travel &amp; airlines", "Travel", "AEP, Mobile SDK, Journey Optimizer, Real-Time CDP, CJA", "Mobile SDK engineer, AJO journey designer, data engineer",
        "<p>An airline's app, booking engine, loyalty program and operations systems all hold part of the passenger story. Messages about check-in, upgrades and disruptions are sent from separate tools, so passengers receive duplicate or late communication and the airline cannot measure which messages change behaviour.</p>",
        [("Sources", ["Booking engine", "Loyalty", "Ops events", "Mobile app"]), ("Collect", ["Mobile SDK", "Streaming API"]),
         ("AEP", ["XDM events", "Identity", "Profile"]), ("Orchestrate", ["AJO journeys", "Push", "Email/SMS"]), ("Measure", ["CJA", "Journey reports"])],
        [("Map lifecycle", "book → fly → return"), ("Model events", "booking, check-in, delay"), ("Mobile SDK", "app events + push"),
         ("Profile &amp; loyalty", "tier, preferences"), ("Journeys", "check-in, upgrade, disruption"), ("Measure", "CJA lifecycle view")],
        ["Check-in reminder journey triggered by departure time", "Paid upgrade offer for eligible loyalty tiers", "Flight-delay notification from an operational event",
         "Post-trip feedback and rebooking journey", "App re-engagement audience for dormant users", "Lifecycle reporting from booking to repeat trip"],
        ["Event payloads validated against the XDM schema before journeys use them", "Push permissions and channel consent respected per passenger",
         "Journeys kept modular so each stays well within platform activity guardrails", "Frequency caps prevent duplicate disruption messages", "Fallback content tested for passengers missing loyalty data"],
        [("Can AJO react to operational events such as delays?", "Yes. An operational system can send a unitary or business event that triggers a journey; payload design and throttling need to be planned up front."),
         ("Is this based on a real airline?", "No. It is a simulation with synthetic data built to reflect a typical airline engagement scope.")],
        ["use-cases/flight-disruption-notifications.html", "services/adobe-journey-optimizer.html", "academy/simulators.html"],
    ),
    case_study(
        "case-studies/hospitality-loyalty-personalisation.html",
        "Hospitality Case Study: Loyalty, Service Journeys & Analytics",
        "Hospitality and services case study: loyalty profiles, customer service journeys, offer attribution and operational analytics on AEP, AJO and CJA.",
        "Hospitality loyalty, service journeys and operational analytics",
        ["hospitality cdp case study", "loyalty personalisation aep", "customer service journey ajo", "hospitality analytics cja", "offer attribution aep"],
        "This hospitality and services case study builds loyalty-aware customer profiles in Adobe Experience Platform, runs service and loyalty journeys in Journey Optimizer, attributes offers to outcomes and reports operational performance in Customer Journey Analytics. It runs on the Infinite360 hospitality simulator with synthetic guest and service data.",
        "Hospitality &amp; services", "Hospitality", "AEP, Journey Optimizer, CJA, Web SDK", "XDM modeller, AJO developer, CJA analyst, QA specialist",
        "<p>A hospitality and services business runs loyalty, service requests, product views and offers across many locations. Offer performance cannot be attributed, service follow-ups are manual and analytics teams spend days reconciling data before they can answer simple questions.</p>",
        [("Sources", ["Loyalty", "Service desk", "Web", "Offers"]), ("Collect", ["Web SDK", "Batch workflows"]),
         ("AEP", ["Profile schema", "Event schemas", "Lookup data"]), ("Engage", ["AJO journeys", "Offers"]), ("Analyse", ["CJA data views", "Journey summary"])],
        [("ERD &amp; use cases", "entities and journeys"), ("Schemas", "profile, events, lookup"), ("Ingestion", "CSV via workflows"),
         ("Attribution IDs", "offer and journey IDs"), ("Journeys", "loyalty + service"), ("CJA reporting", "ops and offers")],
        ["Loyalty tier-upgrade journey", "Service-request follow-up and satisfaction survey", "Product-view and call-to-action event tracking",
         "Offer attribution with journey and offer identifiers", "Journey summary reporting for operations", "Win-back audience for lapsed members"],
        ["Experience Event datasets use the standard _id, timestamp and eventType fields rather than custom duplicates",
         "Every schema field expected by a dataset exists before ingestion; mismatches are logged in the backlog", "CSV data ingested through workflows; JSON or Parquet for direct upload",
         "Attribution identifiers mapped consistently across journey, offer and customer datasets", "CJA data view components named and documented for analysts"],
        [("Why do Experience Event datasets fail on missing IDs?", "Each record needs a unique _id. In the project we compute a UUID during mapping rather than relying on source files to supply one."),
         ("Is this a real company's data?", "No. The simulator uses synthetic data and implies no affiliation with any company.")],
        ["use-cases/loyalty-tier-upgrade.html", "services/customer-journey-analytics.html", "academy/simulators.html"],
    ),
    case_study(
        "case-studies/insurance-policy-onboarding-renewal.html",
        "Insurance Case Study: Policy Onboarding, Claims & Renewals",
        "Insurance case study on AEP and Journey Optimizer: policy onboarding journeys, claims updates, retention programs and automated renewal campaigns.",
        "Insurance policy onboarding, claims and renewal automation",
        ["insurance customer journey aep", "policy renewal campaign ajo", "insurance claims notification journey", "insurance cdp case study", "policyholder retention martech"],
        "This insurance case study unifies policy, claims and digital data in Adobe Experience Platform and uses Journey Optimizer to onboard new policyholders, keep them informed during claims and automate renewal reminders with retention offers. It runs on the Infinite360 insurance simulator using synthetic policyholder data.",
        "Insurance", "Insurance", "AEP, Journey Optimizer, Real-Time CDP, CJA", "Data engineer, AJO developer, governance specialist",
        "<p>An insurer's policy administration, claims and digital systems are disconnected. New policyholders receive generic welcome packs, claimants chase updates by phone and renewal reminders go out on a fixed calendar regardless of risk or engagement.</p>",
        [("Sources", ["Policy admin", "Claims", "Agents/CRM", "Web"]), ("Collect", ["Batch", "Streaming", "Web SDK"]),
         ("AEP", ["XDM", "Identity", "Profile", "Labels"]), ("Engage", ["Onboarding", "Claims", "Renewal"]), ("Measure", ["CJA", "Retention view"])],
        [("Policy lifecycle map", "quote → renew"), ("Schemas &amp; labels", "sensitive data first"), ("Ingest", "policy + claims"),
         ("Audiences", "renewal windows"), ("Journeys", "onboard, claim, renew"), ("Retention reporting", "CJA cohorts")],
        ["Policy onboarding series with document reminders", "Claim-status update journey triggered by claim events", "Renewal reminders at 60, 30 and 7 days",
         "Retention offer for at-risk policyholders", "Cross-sell for single-policy households", "Retention cohort analysis in CJA"],
        ["Health and claims data labelled and excluded from marketing destinations", "Renewal windows computed outside AEP and ingested as clean attributes",
         "Claims journeys tested for missing or delayed events", "Suppression rules prevent offers to customers with open complaints", "Every journey has an owner, purpose and version in its name"],
        [("Should sensitive claims data be used for marketing?", "Only where policy and consent allow. In the project, sensitive fields are labelled at ingestion so governance blocks their use in marketing activation."),
         ("Is this based on a real insurer?", "No. It is a simulation built with synthetic data.")],
        ["use-cases/policy-renewal-reminders.html", "services/real-time-cdp.html", "academy/simulators.html"],
    ),
    case_study(
        "case-studies/telecom-churn-prevention.html",
        "Telecom Case Study: Churn Prevention & Lifecycle Journeys",
        "Telecom case study: subscriber acquisition, churn-risk audiences, network-event personalisation and lifecycle journeys with AEP, RTCDP and AJO.",
        "Telecom churn prevention and subscriber lifecycle journeys",
        ["telecom churn prevention aep", "subscriber lifecycle journey ajo", "network event personalisation", "telecom cdp case study", "churn risk audience rtcdp"],
        "This telecom case study brings subscriber, usage, network-event and digital data into Adobe Experience Platform, builds churn-risk and upgrade audiences in Real-Time CDP and orchestrates save, upgrade and network-event journeys in Journey Optimizer. It runs on the Infinite360 telecom simulator using synthetic subscriber data.",
        "Telecom", "Telecom", "AEP, Real-Time CDP, Journey Optimizer, CJA, Query Service", "Data engineer, data scientist, AJO developer, CJA analyst",
        "<p>A telecom operator sees churn only after a subscriber ports out. Usage drops, repeated network issues and contract end dates live in separate systems, so retention teams cannot intervene early and offers are not matched to the reason a subscriber is at risk.</p>",
        [("Sources", ["Billing", "Usage", "Network events", "App &amp; web"]), ("Collect", ["Batch", "Streaming"]),
         ("AEP", ["Household identity", "Profile", "Query Service"]), ("Activate", ["Churn audiences", "AJO save journeys"]), ("Measure", ["CJA", "Save rate view"])],
        [("Define churn signals", "usage, issues, contract"), ("Model &amp; ingest", "subscriber + events"), ("Score risk", "Query Service / model"),
         ("Audiences", "risk tiers"), ("Journeys", "save, upgrade, apology"), ("Measure", "holdout comparison")],
        ["Churn-risk audiences by reason (price, network, contract end)", "Network-incident apology journey with service credit offer", "Contract-end upgrade journey",
         "New-subscriber onboarding and activation", "Paid-media suppression for recently saved subscribers", "Retention measurement with a holdout group"],
        ["Risk features engineered outside the profile and ingested as clean attributes", "Holdout group defined before launch so impact can be measured honestly",
         "Network-event journeys throttled to avoid message floods during outages", "Household and individual identities kept distinct to prevent false merges", "Offer eligibility and fallbacks tested for every risk tier"],
        [("How is churn risk calculated?", "In the project, features such as usage decline, repeated incidents and contract end date are combined in Query Service or an external model and ingested as profile attributes."),
         ("Is this a real operator's data?", "No. All subscriber data in the simulator is synthetic.")],
        ["solutions/churn-prevention.html", "services/real-time-cdp.html", "academy/simulators.html"],
    ),
    case_study(
        "case-studies/aep-end-to-end-implementation.html",
        "AEP Case Study: End-to-End Implementation, Schema to Activation",
        "End-to-end Adobe Experience Platform case study: schema design, identity, ingestion, Query Service, segmentation and activation in one project.",
        "End-to-end AEP implementation: schema to activation",
        ["aep implementation case study", "adobe experience platform end to end project", "aep schema to activation", "aep project for beginners", "aep hands on project"],
        "This case study walks through a complete Adobe Experience Platform implementation: XDM schema design, identity namespaces, batch and streaming ingestion, Query Service validation, segmentation and activation to destinations. It is the core project in the Infinite360 AEP Simulator and the foundation for every industry case study.",
        "Cross-industry", "Platform", "AEP, Query Service, Real-Time CDP, Web SDK", "AEP developer, data engineer, solution architect",
        "<p>Teams new to Adobe Experience Platform often configure features in isolation and discover late that schemas, identities and datasets do not fit together. This project builds the platform in the right order so each step can be validated before the next.</p>",
        [("Sources", ["CSV/JSON files", "Web SDK", "Cloud storage"]), ("Model", ["Classes", "Field groups", "Data types"]),
         ("Platform", ["Datasets", "Identity", "Profile"]), ("Analyse", ["Query Service", "Audiences"]), ("Activate", ["Destinations", "Journeys"])],
        [("Use cases &amp; backlog", "dependencies first"), ("XDM schemas", "profile + events"), ("Identities", "namespaces, primary"),
         ("Ingestion", "batch + streaming"), ("Validate", "Query Service"), ("Segment &amp; activate", "audiences → destinations")],
        ["Customer profile and Experience Event schemas with reusable data types", "Identity namespaces and primary identity selection",
         "Batch ingestion through workflows and streaming through datastreams", "Query Service checks for counts, duplicates and nulls",
         "Batch, streaming and edge audiences", "Activation to a file-based and an advertising destination"],
        ["Reusable data types shared between profile and event field groups", "Profile enablement switched on only after schema review, because it cannot be reversed",
         "Record counts and distinct IDs reconciled with source files", "Profile fragments and identity graph inspected for test customers", "Audience estimates compared with Query Service results"],
        [("What order should an AEP implementation follow?", "Use cases, schema design, identity strategy, datasets, ingestion, profile stitching, consent and governance, segmentation, destinations, activation, QA and go-live."),
         ("Can I practise this without a client sandbox?", "Yes. The AEP Simulator and training sandboxes are provided to enrolled learners.")],
        ["adobe-experience-platform/implementation-guide.html", "guides/martech-implementation-backlog.html", "academy/simulators.html"],
    ),
    case_study(
        "case-studies/martech-consulting-engagement-simulation.html",
        "Consulting Case Study: Running an Adobe MarTech Engagement",
        "Consulting case study: discovery, architecture documentation, RTCDP use cases and journey design workshops in a simulated Adobe MarTech engagement.",
        "Running an Adobe MarTech consulting engagement",
        ["martech consulting engagement", "adobe consulting framework", "aep discovery workshop", "martech architecture documentation", "rtcdp use case workshop"],
        "This case study simulates a full Adobe MarTech consulting engagement: stakeholder discovery, current-state audit, RTCDP use-case prioritisation, architecture documentation, journey design workshops and a delivery roadmap. It uses the Adobe MarTech Consultant Portal to practise client-facing consulting alongside hands-on delivery.",
        "Consulting", "Consulting", "AEP, RTCDP, AJO, CJA, consulting frameworks", "Solution consultant, architect, business analyst, program manager",
        "<p>Technical skill alone does not deliver an Adobe program. Consultants must run discovery, translate business goals into prioritised use cases, document architecture decisions and keep stakeholders aligned through delivery.</p>",
        [("Discover", ["Stakeholders", "Current state", "KPIs"]), ("Prioritise", ["Use cases", "Value vs effort"]),
         ("Design", ["Architecture", "Identity", "Data model"]), ("Plan", ["Backlog", "30/60/90"]), ("Deliver", ["Sprints", "QA", "Handover"])],
        [("Kick-off &amp; discovery", "interviews, audit"), ("Use-case workshop", "prioritise"), ("Architecture", "documented decisions"),
         ("Journey workshop", "design sessions"), ("Roadmap", "30/60/90 days"), ("Governance &amp; handover", "RACI, runbooks")],
        ["Stakeholder discovery interview guides", "Use-case prioritisation matrix", "Architecture decision records",
         "Journey design workshop outputs", "Dependency-tracked implementation backlog", "Executive readout and roadmap"],
        ["Every use case linked to a KPI and an owner", "Architecture decisions recorded with alternatives considered", "Backlog dependencies mapped before sprint planning",
         "Risks and open questions tracked to closure", "Handover pack reviewed with the client team"],
        [("What does a consulting simulation teach?", "How to run discovery, prioritise use cases, document architecture and manage stakeholders - the skills that make technical work land with a client."),
         ("Is this a real client engagement?", "No. It is a simulated engagement with fictional stakeholders and synthetic data.")],
        ["services/engagement-model.html", "services/martech-strategy-advisory.html", "case-studies/aep-end-to-end-implementation.html"],
    ),
    case_study(
        "case-studies/retail-omnichannel-identity-stitching.html",
        "Retail Case Study: Omnichannel Identity Stitching in AEP",
        "Retail case study: stitching anonymous web, app, CRM and in-store purchases into one AEP profile, with a troubleshooting walkthrough for unstitched profiles.",
        "Retail omnichannel identity stitching and troubleshooting",
        ["aep identity stitching retail", "anonymous to known profile aep", "profile not merging aep", "omnichannel customer profile", "web sdk identitymap login"],
        "This retail case study stitches anonymous browsing, app activity, CRM records and in-store purchases into one Real-Time Customer Profile, then walks through how to troubleshoot a profile that still shows as anonymous after login. It is a scenario used in Infinite360 architect-level troubleshooting sessions with synthetic data.",
        "Retail", "Platform", "AEP, Web SDK, Mobile SDK, Real-Time CDP", "Web SDK engineer, identity architect, QA specialist",
        "<p>A retailer has a website on Web SDK, a mobile app on Mobile SDK, CRM batch files and a streaming point-of-sale feed. A shopper browses anonymously, views products, adds items to the cart, logs in and later buys in store &mdash; yet the profile still looks anonymous. The team needs a repeatable way to find the break.</p>",
        [("Channels", ["Web SDK", "Mobile SDK", "POS stream", "CRM batch"]), ("Identity", ["ECID", "Email", "CRM ID"]),
         ("AEP", ["Identity graph", "Profile-enabled datasets", "Merge policy"]), ("Activate", ["Cart audiences", "Journeys"]), ("Validate", ["Debugger", "Profile viewer"])],
        [("Check Web SDK", "identityMap after login"), ("Edge debugger", "ECID, email, CRM ID"), ("Identity graph", "links present?"),
         ("Dataset", "profile-enabled?"), ("Merge policy", "correct precedence"), ("Root cause &amp; fix", "retest")],
        ["Anonymous-to-known stitching on login", "Cart-abandonment audience across web and app", "Store purchase linked to the online profile",
         "Suppression of recent purchasers from cart journeys", "Identity graph health monitoring", "Troubleshooting runbook for unstitched profiles"],
        ["Authenticated identity sent in identityMap on login with the correct authenticated state", "Same namespace and hashing used for email in every source",
         "All datasets that should build the profile are profile-enabled", "Merge policy precedence reviewed so the newest trusted data wins", "Graph checked for over-merging from shared devices"],
        [("Why does a profile stay anonymous after login?", "The most common root cause is that no authenticated identity is sent after login, so ECID is never linked to the email or CRM ID."),
         ("What tools help debug identity?", "The Adobe Experience Platform Debugger, the identity graph viewer and the profile viewer, plus Query Service checks on the datasets.")],
        ["adobe-experience-platform/identity-service.html", "guides/web-sdk-troubleshooting.html", "guides/hashed-email-identity-aep.html"],
    ),
]


def training_case(path, title, desc, h1, keywords, answer, who, model, flow, components, measures, related):
    return dict(
        path=path, title=title, desc=desc, h1=h1, kicker="Training case study", keywords=keywords, answer=answer,
        schema="Article", category="Case studies", date="2026-10-11", hero_cta=("Register", REGISTER),
        sections=[
            ("Who it is for", who),
            ("Delivery model", figure(flow_svg(h1, flow), "Learner journey through the program.") + '<ol class="steps">' + "".join(f"<li><strong>{a}</strong> &mdash; {b}</li>" for a, b in flow) + "</ol>"),
            ("What the program includes", '<ul class="checklist cols-2">' + "".join(f"<li>{c}</li>" for c in components) + "</ul>"),
            ("How progress is checked", '<ul class="checklist">' + "".join(f"<li>{m}</li>" for m in measures) + '</ul><p class="note">We report participation and assessment progress honestly. No job, salary or certification outcome is guaranteed.</p>'),
            ("What Infinite360 brings", _cards(BRINGS[:3] + [BRINGS[4], ("Live mentor access", "Doubts are answered in class, in the community and in written follow-ups with references to Adobe documentation."), ("Simulators and sandboxes", "Industry simulators and practice environments so learners build, break and fix real configurations.")])),
            ("Next steps", LINK_PILLS),
        ],
        faqs=[], related=related,
    )


TRAINING_CASES = [
    training_case(
        "case-studies/career-accelerator-delivery-model.html",
        "Training Case Study: How the AEP Career Accelerator Runs",
        "How the Infinite360 career accelerator is delivered: live classes, recordings, simulators, projects, doubt resolution and interview preparation.",
        "How the AEP career accelerator is delivered",
        ["aep career accelerator", "adobe experience platform training program", "aep course with projects", "martech career training india", "aep interview preparation"],
        "The Infinite360 career accelerator combines live online classes, recorded lessons on the learner platform, industry simulators, enterprise-style projects, mentor-led doubt resolution and interview preparation. Learners move from AEP foundations through RTCDP, AJO, CJA, Web SDK and Agentic AI, practising each skill on a project before moving on.",
        "<p>Working professionals and career switchers &mdash; developers, data engineers, analysts, testers, consultants and freshers &mdash; who want practical Adobe MarTech skills rather than slideware. See <a href=\"../training/career-transition.html\">career transition paths</a>.</p>",
        None,
        [("Career mapping", "background → target role"), ("Live classes", "concepts + demos"), ("Recordings", "learner platform"),
         ("Simulator projects", "build, break, fix"), ("Doubt resolution", "mentor answers"), ("Interview prep", "scenarios + mock")],
        ["Live online sessions with recordings", "AEP, RTCDP, AJO, CJA, Web SDK and Agentic AI modules", "Industry simulators and practice sandboxes",
         "Enterprise-style project with a dependency-tracked backlog", "Architect-level troubleshooting scenarios", "Interview question bank and mock scenarios"],
        ["Module assessments and project checkpoints", "Mentor review of project configurations", "Interview readiness review against role expectations"],
        ["training/index.html", "academy/recording-platform.html", "academy/simulators.html"],
    ),
    training_case(
        "case-studies/corporate-team-enablement-model.html",
        "Training Case Study: Corporate Adobe Team Enablement Model",
        "How Infinite360 enables corporate Adobe teams: skills baseline, role-based tracks, project labs, assessments and knowledge transfer into delivery.",
        "Corporate Adobe team enablement model",
        ["corporate adobe training", "aep team enablement", "adobe experience platform corporate training", "martech capability building", "role based adobe training"],
        "Corporate enablement starts with a skills baseline, then runs role-based tracks for engineers, analysts, architects and managers, built around labs on your use cases. Assessments track progress, and knowledge transfer connects training to live delivery so teams apply what they learn on current projects.",
        "<p>L&amp;D leaders, Adobe practice heads, SI delivery leaders and enterprise CoEs that need teams productive on AEP, RTCDP, AJO and CJA. See <a href=\"../training/corporate-training.html\">corporate training</a>.</p>",
        None,
        [("Skills baseline", "assess current roles"), ("Track design", "role-based paths"), ("Labs on your use cases", "hands-on"),
         ("Assessments", "checkpoints"), ("Project pairing", "apply on delivery"), ("Handover", "playbooks + recordings")],
        ["Skills baseline and gap report", "Role-based tracks: engineer, analyst, architect, manager", "Labs designed around your industry and use cases",
         "Assessments and progress reporting", "Pairing on live backlog items where agreed", "Recordings and playbooks for future joiners"],
        ["Pre- and post-track skill assessments", "Lab completion and review", "Manager feedback on applied work"],
        ["training/corporate-training.html", "lp/corporate-adobe-training.html", "services/engagement-model.html"],
    ),
    training_case(
        "case-studies/mentor-led-doubt-resolution.html",
        "Training Case Study: Mentor-Led Doubt Resolution for AEP",
        "How learner questions on AEP, Web SDK, AJO and CJA are captured, answered with Adobe documentation references and turned into a public knowledge base.",
        "Mentor-led doubt resolution and the learner knowledge base",
        ["aep doubts answered", "aep student questions", "adobe experience platform mentor", "aep troubleshooting help", "aep learning support"],
        "Every learner question is captured in a shared doubts log, answered by a mentor with a plain-language explanation and an Adobe documentation reference, then reviewed for recurring themes. Recurring answers become public knowledge-base guides, so each batch benefits from the questions of the batches before it.",
        "<p>Learners in live and recorded batches who get stuck on schemas, identities, ingestion, Web SDK, journeys or reporting. Browse the resulting <a href=\"../learn/student-questions.html\">AEP student questions knowledge base</a>.</p>",
        None,
        [("Capture", "doubt logged with context"), ("Triage", "concept, config or bug"), ("Answer", "plain language + reference"),
         ("Demonstrate", "in class if needed"), ("Publish", "knowledge-base guide"), ("Improve", "update lessons")],
        ["Shared doubts log per batch", "Answers with Adobe Experience League references", "Screen-share debugging for configuration issues",
         "Recurring questions turned into guides", "Interview-style follow-up questions", "Lesson updates based on common confusion"],
        ["Open doubts reviewed every session", "Answers checked against current documentation", "Recurring themes fed back into the curriculum"],
        ["learn/student-questions.html", "training/index.html", "academy/free-resources.html"],
    ),
]

CONTRACT = [
    dict(
        path="services/contract-hiring.html",
        title="Contract Hiring: Day-One-Ready AEP & Adobe MarTech Talent",
        desc="Contract AEP, RTCDP, AJO, CJA and Web SDK engineers prepared to contribute from day one through simulator projects, readiness checks and onboarding.",
        h1="Contract hiring for day-one-ready Adobe MarTech talent",
        nav="Contract hiring",
        kicker="Contract hiring",
        keywords=["aep contract hiring", "adobe martech contract engineers", "hire aep developer contract", "contract to hire adobe consultant", "rtcdp ajo cja contract talent"],
        answer="Infinite360 contract hiring provides Adobe MarTech engineers, analysts and architects who have built the same patterns end to end in simulator projects before they join you. Our aim is for each person to contribute from the first day: readiness is checked against your stack, and onboarding focuses on your systems, standards and backlog rather than on learning the platform.",
        schema="Service", service_type="Contract hiring for Adobe MarTech talent", interest="staff",
        hero_cta=("Request contract talent", "lp/hire-aep-contract-talent.html"),
        sections=[
            ("How we prepare people to be productive from day one", figure(flow_svg("Day-one readiness", [
                ("Role brief", "skills, stack, backlog"), ("Shortlist", "matched profiles"), ("Readiness check", "scenario interview"),
                ("Pre-onboarding", "your standards, tools"), ("Day one", "first backlog item"), ("30-day review", "fit and output")]), "Our day-one readiness process.")
             + """<ol class="steps">
<li><strong>Role brief</strong> &mdash; we capture the platforms, use cases, backlog and working hours the person must support.</li>
<li><strong>Shortlist</strong> &mdash; profiles matched on practised patterns (for example identity stitching, AJO journeys or CJA data views), not keywords alone.</li>
<li><strong>Readiness check</strong> &mdash; a scenario interview based on our case studies: design, troubleshoot and explain trade-offs.</li>
<li><strong>Pre-onboarding</strong> &mdash; access requests, naming conventions, environments and your definition of done are prepared before day one.</li>
<li><strong>Day one</strong> &mdash; the engineer starts on an agreed first backlog item with a named buddy on your team.</li>
<li><strong>30-day review</strong> &mdash; a check-in on output and fit, with replacement options discussed openly if it is not working.</li>
</ol>"""),
            ("Roles available", """<div class="table-wrap"><table><thead><tr><th>Role</th><th>Typical scope</th><th>Practised in</th></tr></thead><tbody>
<tr><td>AEP data engineer</td><td>XDM, datasets, ingestion, Query Service</td><td><a href="../case-studies/aep-end-to-end-implementation.html">End-to-end AEP</a></td></tr>
<tr><td>Identity &amp; profile specialist</td><td>Namespaces, graphs, merge policies</td><td><a href="../case-studies/retail-omnichannel-identity-stitching.html">Retail identity</a></td></tr>
<tr><td>Web SDK / Tags engineer</td><td>Data layer, data elements, datastreams, consent</td><td><a href="../guides/web-sdk-troubleshooting.html">Web SDK troubleshooting</a></td></tr>
<tr><td>AJO developer</td><td>Journeys, campaigns, events, content, decisioning</td><td><a href="../case-studies/airline-mobile-journey-orchestration.html">Airline journeys</a></td></tr>
<tr><td>RTCDP specialist</td><td>Audiences, destinations, activation</td><td><a href="../case-studies/banking-customer-360-cross-sell.html">Banking Customer 360</a></td></tr>
<tr><td>CJA analyst</td><td>Connections, data views, Workspace</td><td><a href="../case-studies/hospitality-loyalty-personalisation.html">Hospitality analytics</a></td></tr>
<tr><td>MarTech QA specialist</td><td>Payload, identity, journey and report validation</td><td><a href="../case-studies/insurance-policy-onboarding-renewal.html">Insurance journeys</a></td></tr>
<tr><td>Solution architect</td><td>Architecture, governance, roadmaps</td><td><a href="../case-studies/martech-consulting-engagement-simulation.html">Consulting engagement</a></td></tr>
</tbody></table></div>"""),
            ("Engagement options", _cards([
                ("Contract", "Fixed-term specialists for a project phase, migration or peak workload."),
                ("Contract-to-hire", "Start on contract, convert to a permanent role once both sides are confident."),
                ("Managed pod", "A small team with a lead, scoped to deliver a backlog with agreed outcomes.")])),
            ("What we will and will not promise", '<ul class="checklist"><li>Profiles who have practised the patterns your backlog needs</li><li>Transparent readiness evidence from scenario interviews</li><li>Onboarding preparation so day one is productive</li></ul><p class="note">We do not guarantee outcomes we cannot control, such as your access approvals or changing requirements; we plan for them with you instead.</p>'),
            ("Request talent", pills(("Request contract talent", "../lp/hire-aep-contract-talent.html"), ("Talk on WhatsApp", WHATSAPP_MSG), ("See staff augmentation", "staff-augmentation.html"), ("Browse case studies", "../case-studies/index.html"))),
        ],
        faqs=[("How fast can a contract engineer start?", "It depends on the role and your onboarding process; we agree a start date once the brief and shortlist are confirmed."),
              ("Can contractors work in my time zone?", "Yes. Working hours and overlap are part of the role brief."),
              ("What if the fit is not right?", "We review at 30 days and discuss replacement options openly.")],
        related=["services/staff-augmentation.html", "case-studies/index.html", "lp/hire-aep-contract-talent.html"],
    ),
]

ACADEMY_EXTRA = [
    dict(
        path="academy/simulators.html",
        title="Adobe MarTech Simulators: AEP, Banking, Airline & Telecom",
        desc="Hands-on simulation environments for AEP, BFSI, airline, hospitality, insurance and telecom scenarios used in Infinite360 bootcamps and projects.",
        h1="Practical simulation environments for Adobe MarTech",
        nav="Simulators",
        kicker="Learning environments",
        keywords=["aep simulator", "adobe experience platform practice environment", "martech simulator", "banking aep simulation", "aep hands on practice"],
        answer="Infinite360 Tech Academy provides simulation environments that replicate enterprise business scenarios: an Adobe MarTech consultant portal, an AEP simulator and industry simulators for banking, airlines, hospitality, insurance and telecom. Learners use them throughout bootcamps for schema design, identity, ingestion, journeys, analytics and Agentic AI use cases.",
        schema="CollectionPage", category="Academy",
        sections=[
            ("Simulation environments", '<div class="grid-2">' + "".join(
                f'<div class="card sim-card"><span class="tag">{k}</span><h3>{n}</h3><ul>' + "".join(f"<li>{x}</li>" for x in items)
                + f'</ul><a class="btn btn-primary" href="{u}" rel="noopener" target="_blank">Open {n.split(" (")[0]}</a></div>'
                for n, u, k, items in SIMULATORS) + "</div>"),
            ("How simulators are used in the program", figure(flow_svg("Simulator learning loop", [("Scenario brief", "business problem"), ("Design", "schema, identity"), ("Build", "configure"), ("Break", "inject issues"), ("Fix", "troubleshoot"), ("Explain", "interview-style")]), "Each scenario follows a build-break-fix loop.")),
            ("Case studies built on these environments", '<ul class="cols-2">' + "".join(f'<li><a href="../{c["path"]}">{c["h1"]}</a></li>' for c in CASES) + "</ul>"),
            ("Get access", '<p>Simulator access is provided to enrolled learners. Public pages may be viewable, but projects, data and sandboxes are part of the program.</p>' + LINK_PILLS),
        ],
        faqs=[("Are the simulators real company systems?", "No. They are training environments with synthetic data. Brand-like names in a simulator address are scenario labels and imply no affiliation."),
              ("Do I get an Adobe sandbox?", "Enrolled learners get access to practice environments as described for their program; ask us for current details before you enrol.")],
        related=["case-studies/index.html", "academy/index.html", "academy/recording-platform.html"],
    ),
    dict(
        path="academy/recording-platform.html",
        title="Learner Recording Platform: Video Library & Onboarding",
        desc="How Infinite360 Tech Academy learners access recorded batches: folder-based video library, naming standard, learning sequence and onboarding flow.",
        h1="The learner recording platform and video library",
        nav="Recording platform",
        kicker="Learner platform",
        keywords=["aep recorded course", "adobe training recordings", "tech academy video library", "recorded aep batch", "learn aep at your own pace"],
        answer="Recorded batches are delivered through the Infinite360 Tech Academy learner app. Lessons are organised in a fixed sequence of folders - pre-recordings, walkthroughs, MarTech videos, interview accelerator, Adobe Experience content and Agentic AI pre-recordings - so learners sign in once, follow the same order and complete activities before moving on.",
        schema="WebPage", category="Academy",
        hero_cta=("Open the learner platform", REGISTER),
        sections=[
            ("How the video library is organised", """<div class="table-wrap"><table><thead><tr><th>Order</th><th>Folder</th><th>What it contains</th></tr></thead><tbody>
<tr><td>01</td><td>Pre-recording</td><td>Orientation and pre-session content</td></tr>
<tr><td>02</td><td>Walkthrough</td><td>Step-by-step platform walkthroughs</td></tr>
<tr><td>03</td><td>MarTech videos</td><td>Core MarTech training recordings</td></tr>
<tr><td>04</td><td>Interview accelerator</td><td>Interview preparation content</td></tr>
<tr><td>05</td><td>Adobe Experience training</td><td>AEP, RTCDP, AJO and CJA course content</td></tr>
<tr><td>06</td><td>Agentic AI pre-recordings</td><td>Agentic AI and MCP content</td></tr>
</tbody></table></div>"""),
            ("Learner onboarding flow", figure(flow_svg("Learner onboarding", [("Course link", "one approved link"), ("Sign in", "registered account"), ("Open batch", "your package"), ("Pick folder", "in sequence"), ("Watch", "recording"), ("Activity", "then next lesson")]), "From the course link to the next lesson.")
             + '<ul class="checklist"><li>Use the single course-entry link shared for your batch.</li><li>Sign in with your registered Academy account so assigned content appears.</li><li>Follow folders in order; earlier lessons are prerequisites for later ones.</li><li>Complete the activity or assessment after each recording.</li></ul>'),
            ("How lessons are named", '<p>Every recording follows one pattern so you can find a lesson without opening it:</p><p><code>[Folder] | [Module number] | [Topic] | [Batch]</code></p><ul><li>Walkthrough | 01 | Platform Navigation | US Recording Batch</li><li>MarTech Videos | 02 | AEP Data Ingestion | US Recording Batch</li><li>Interview Accelerator | 03 | AEP Interview Questions | US Recording Batch</li></ul>'),
            ("Quality checks before each batch", '<ul class="checklist cols-2"><li>All required folders exist</li><li>Folder order matches the learner journey</li><li>Names are approved and consistently spelled</li><li>Each recording is in the correct folder</li><li>Titles follow one naming convention</li><li>No duplicate, test or obsolete recordings visible</li><li>Learner view tested before the batch link is sent</li></ul>'),
            ("Related platforms", pills(("Learner app", REGISTER), ("MarTech LMS", LMS), ("Simulators", "simulators.html"), ("YouTube playlists", "youtube-playlists.html"))),
        ],
        faqs=[("Can I learn only from recordings?", "Yes, recorded batches are available. Live sessions add doubt resolution and project reviews; ask which format suits you."),
              ("Which login do I use?", "Your registered Academy account, so the content assigned to your batch is visible.")],
        related=["academy/index.html", "case-studies/career-accelerator-delivery-model.html", "academy/youtube-playlists.html"],
    ),
]

PLAYLISTS = [
    ("PLOY34GHz7wwLrI_dHpleIkmFIMmjiRK40", "Playlist 1"), ("PLOY34GHz7wwIZPqs3uphKxx32pJyS7Ka1", "Playlist 2"),
    ("PLOY34GHz7wwJeARrqrRiVlugddWD4qIN8", "Playlist 3"), ("PLOY34GHz7wwIft6y2Eruv0gQ9_WxVCeno", "Playlist 4"),
    ("PLOY34GHz7wwIARGr7wK6378yk64V3kZ8_", "Playlist 5"), ("PLOY34GHz7wwIbtaluPTjV6KvbHeNVi47-", "Playlist 6"),
    ("PLOY34GHz7wwJl6rmZWFiwCrQ51d7Gfc3u", "Playlist 7"), ("PLOY34GHz7wwJTxvebvpeF0t04Lbvamo_H", "Playlist 8"),
    ("PLOY34GHz7wwINDxoFUvYn3PQnLewzMdFL", "Playlist 9"),
]

ACADEMY_EXTRA.append(dict(
    path="academy/youtube-playlists.html",
    title="Free AEP, AJO & CJA YouTube Playlists | Infinite360",
    desc="Free Infinite360 Tech Academy YouTube playlists on Adobe Experience Platform, Journey Optimizer, CJA, Web SDK and Agentic AI.",
    h1="Free Adobe MarTech YouTube playlists",
    nav="YouTube playlists",
    kicker="Free learning",
    keywords=["aep youtube playlist", "adobe experience platform free videos", "ajo tutorial videos", "cja tutorial youtube", "adobe martech free training"],
    answer="Infinite360 Tech Academy publishes free YouTube playlists that cover Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Web SDK and Agentic AI. Use them to preview the teaching style, revise concepts between classes or start learning before you enrol.",
    schema="CollectionPage", category="Academy",
    sections=[
        ("Playlists", '<div class="grid-3">' + "".join(
            f'<a class="card link-card" href="https://www.youtube.com/playlist?list={pid}" rel="noopener" target="_blank"><span class="tag">YouTube</span><h3>Infinite360 Tech Academy &middot; {n}</h3><p>Open the playlist on YouTube.</p><span class="more">Watch &rarr;</span></a>'
            for pid, n in PLAYLISTS) + "</div>"),
        ("Watch our approach", pills(("Our training approach (video)", APPROACH_VIDEO), ("Featured videos", "videos.html"), ("Subscribe on YouTube", "https://www.youtube.com/@Infiante360TechAcademy"))),
        ("Go further", "<p>Videos explain concepts; projects build skill. When you are ready, move to the <a href=\"simulators.html\">simulators</a> and a <a href=\"index.html\">structured program</a>.</p>" + LINK_PILLS),
    ],
    faqs=[], related=["academy/videos.html", "academy/free-resources.html", "academy/recording-platform.html"],
))

ACADEMY_EXTRA.append(dict(
    path="academy/community.html",
    title="Infinite360 Community: LinkedIn Group, WhatsApp & Links",
    desc="Join the Infinite360 Tech Academy community on LinkedIn and WhatsApp, and find every official academy link: LMS, simulators, brochure and focus areas.",
    h1="Join the Infinite360 community",
    nav="Community",
    kicker="Community",
    keywords=["adobe martech community", "aep linkedin group", "infinite360 tech academy links", "martech whatsapp community", "aep learners community"],
    answer="The Infinite360 community connects learners, alumni and practitioners through a LinkedIn group, the company LinkedIn page, WhatsApp and YouTube. This page lists every official academy link in one place - registration, learner LMS, simulators, program brochure, focus areas and the Agentic AI skills site - so you always use the right address.",
    schema="WebPage", category="Academy",
    sections=[
        ("Official links", pills(("Register: techacademy.infinate360.in", REGISTER), ("WhatsApp", WHATSAPP_MSG), ("LinkedIn company page", LI_COMPANY), ("LinkedIn group", LI_GROUP),
                                 ("MarTech LMS", LMS), ("AEP Simulator", "https://aepsimualtor.infiante360techacademy.com/"), ("Program brochure", BROCHURE),
                                 ("Our approach (video)", APPROACH_VIDEO), ("Our focus", FOCUS), ("Agentic AI skills", AGENTIC), ("MarTech program page", MARTECH_PAGE))),
        ("Hashtags we use", '<ul class="chips chips-light">' + "".join(f"<li>#{h}</li>" for h in ["AdobeConsultant", "MarTechTraining", "AdobeExperiencePlatform", "AEP", "RTCDP", "AdobeJourneyOptimizer", "CustomerJourneyAnalytics", "AgenticAI", "MarTechCareers", "Infinite360TechAcademy"]) + "</ul>"),
        ("Community guidelines", '<ul class="checklist"><li>Ask questions with context: what you tried, what you expected, what happened.</li><li>Never post passwords, API keys or customer data.</li><li>Share answers back so the next learner benefits.</li></ul>'),
    ],
    faqs=[], related=["academy/testimonials.html", "academy/youtube-playlists.html", "contact-us.html"],
))

ACADEMY_EXTRA.append(dict(
    path="academy/testimonials.html",
    title="Learner & Client Reviews: Share Your Infinite360 Experience",
    desc="Read verified reviews from Infinite360 learners and clients, and share your own. We publish only reviews with permission and confirmed participation.",
    h1="Reviews from learners and clients",
    nav="Reviews",
    kicker="Reviews",
    keywords=["infinite360 reviews", "infinite360 tech academy reviews", "aep training reviews", "adobe martech training feedback", "infinite360 testimonials"],
    answer="This page shows reviews only from people we can verify attended a program or worked with us, published with their written permission. If you are a learner or client, you can submit your review below; we confirm participation before it appears and you can ask us to remove it at any time.",
    schema="WebPage", category="Academy",
    sections=[
        ("Verified reviews", "@@TESTIMONIALS@@"),
        ("Share your review", "@@TESTIMONIAL_FORM@@"),
        ("Our review policy", '<ul class="checklist"><li>We publish reviews only with written permission.</li><li>We confirm the reviewer attended a program or worked with us.</li><li>We do not edit meaning; we may shorten for length with your approval.</li><li>We never pay for reviews or publish invented ones.</li><li>You can request removal at any time.</li></ul>'),
    ],
    faqs=[], related=["academy/community.html", "case-studies/index.html", "academy/index.html"],
))

HUB = dict(
    path="case-studies/index.html",
    title="Case Studies: Adobe AEP Implementation & Training Projects",
    desc="Implementation case studies across banking, airlines, hospitality, insurance, telecom and retail, plus training delivery and contract-hiring models.",
    h1="Case studies: implementation, training and talent",
    nav="Case studies",
    kicker="Case studies",
    keywords=["aep case studies", "adobe experience platform case study", "rtcdp ajo case study", "martech implementation case study", "adobe training case study"],
    answer="Infinite360 case studies show how we approach Adobe MarTech work: industry implementation projects built on our simulation environments, training delivery models for individuals and corporate teams, and the contract-hiring process that prepares people to contribute from day one. Each one lists scope, architecture, approach and validation - without invented client names or results.",
    schema="CollectionPage", category="Case studies",
    sections=[
        ("Implementation case studies", '<div class="grid-2">' + "".join(
            f'<a class="card link-card case-card" href="../{c["path"]}"><span class="tag">{c["kicker"].split("· ")[1]}</span><h3>{c["h1"]}</h3><p>{c["desc"]}</p><span class="more">Read the case study &rarr;</span></a>' for c in CASES) + "</div>", "plain", "Implementation"),
        ("Training case studies", '<div class="grid-3">' + "".join(
            f'<a class="card link-card" href="../{c["path"]}"><span class="tag">Training</span><h3>{c["h1"]}</h3><p>{c["desc"]}</p></a>' for c in TRAINING_CASES) + "</div>", "alt", "Capability building"),
        ("Contract hiring: productive from day one", '<div class="split"><div><p class="lead">The people who build these case studies are the profiles we place on contract. Our readiness process is designed so they start on your backlog on day one.</p>'
         + pills(("How contract hiring works", "../services/contract-hiring.html"), ("Request contract talent", "../lp/hire-aep-contract-talent.html")) + '</div><div>'
         + figure(flow_svg("Case study to contract", [("Practise", "simulator project"), ("Validate", "scenario interview"), ("Deploy", "your backlog")]), "From practised pattern to productive contractor.") + "</div></div>", "dark", "Talent"),
        ("How to read these case studies", '<p>Implementation case studies use simulation environments and synthetic data. They show how we would scope, architect, build and validate a program; they are not client engagements and do not claim business results. When a client approves publication of a real engagement, it will be labelled as such.</p>', "plain", "Transparency"),
    ],
    bands=True,
    faqs=[("Are these real client projects?", "The implementation case studies are simulation-based projects with synthetic data. We publish real client work only with written approval."),
          ("Can you run a similar project for my organisation?", "Yes. Start with an architecture review or a discovery call and we will scope it against your use cases.")],
    related=["services/contract-hiring.html", "academy/simulators.html", "use-cases/index.html"],
)

CASE_PAGES = [HUB] + CASES + TRAINING_CASES + CONTRACT + ACADEMY_EXTRA
