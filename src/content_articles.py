"""Article batch 1 (articles A-001..A-010). Plan ids refer to data/seo/articles.json (ids 351-360).
Original practitioner guidance. Every worked example is labelled illustrative; no client names, results or guarantees."""
EL = "https://experienceleague.adobe.com/en/docs/experience-platform"
S_ING = ("Adobe Experience Platform data ingestion", f"{EL}/ingestion/home")
S_ID = ("Adobe Experience Platform Identity Service", f"{EL}/identity/home")
S_GOV = ("Data governance overview", f"{EL}/data-governance/home")
S_PROF = ("Real-Time Customer Profile", f"{EL}/profile/home")
S_XDM = ("XDM system overview", f"{EL}/xdm/home")
S_WSDK = ("Adobe Experience Platform Web SDK", f"{EL}/web-sdk/home")
ILL = '<p class="small muted">Illustrative example for teaching. It is not a client case and the numbers are not results.</p>'


def ul(items):
    return '<ul class="checklist">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def ol(items):
    return '<ol class="steps">' + "".join(f"<li><strong>{h}</strong> &mdash; {t}</li>" for h, t in items) + "</ol>"


def tbl(head, rows):
    return ('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{h}</th>" for h in head) + "</tr></thead><tbody>"
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table></div>")


def art(slug, title, desc, h1, kw, answer, sections, faqs, src, related, topic):
    return dict(path=f"guides/{slug}.html", title=title, desc=desc, h1=h1, kicker=f"Guide · {topic}", keywords=kw, answer=answer,
                schema="Article", category="Guides", date="2026-11-25", sections=sections, faqs=faqs, sources=src, related=related)


A = [
    art("loan-onboarding-event-model", "Loan Onboarding Event Model for AEP and AJO Journeys",
        "Design the events, identities and suppression rules behind a loan onboarding journey, with a worked illustrative event table and test cases.",
        "Loan onboarding event model: events, identity and suppression",
        ["loan onboarding journey", "banking journey event model", "aep event schema banking", "ajo suppression rules"],
        "A loan onboarding journey is only as reliable as its event model. Define each step as a named event with a timestamp and an identity, decide which identifier joins pre-login and post-login activity, and write suppression rules before building any message. Test the model with synthetic applicants before go-live.",
        [("Start with the steps, not the tool", ol([("List the stages", "enquiry, application started, documents uploaded, verification pending, decision, disbursement."), ("Name one event per stage", "use consistent verbs and a single schema for all of them."), ("Mark the system of record", "state which system emits each event so owners can fix gaps."), ("Add the exit events", "approved, declined, withdrawn and expired must all stop earlier messages.")])),
         ("Illustrative event table", tbl(["Event", "Emitted by", "Identity present", "Used for"], [["application_started", "Web or app", "Cookie ID; login ID after sign-in", "Abandonment nudge"], ["documents_uploaded", "Loan platform", "Customer ID", "Progress message"], ["verification_pending", "Verification service", "Customer ID", "Status update"], ["decision_made", "Decision engine", "Customer ID", "Stops all nudges"]]) + ILL),
         ("Identity and suppression rules", ul(["Choose the join key between anonymous and signed-in activity and test it with a returning visitor", "Suppress promotional messages while an application is open", "Stop abandonment nudges the moment a decision event arrives", "Apply consent and channel preferences before any send", "Record why a customer was suppressed so support can answer"])),
         ("Test cases to run before go-live", ul(["Applicant starts on mobile web and finishes in the app", "Decision arrives while a nudge is queued", "Two applications by the same customer", "Customer withdraws then restarts", "Missing consent for the preferred channel"]))],
        [("Should regulated messages use the same journey as marketing?", "Usually not. Keep service and regulatory communications separate from promotional journeys, and confirm rules with your compliance team."),
         ("How many events do we need?", "Start with the smallest set that covers entry, progress and exit. Add events only when a decision or message needs them.")],
        [S_XDM, S_ID, ("Adobe Journey Optimizer documentation", "https://experienceleague.adobe.com/en/docs/journey-optimizer")],
        ["use-cases/loan-application-drop-off.html", "use-cases/industries/banking.html", "guides/ajo-implementation-best-practices.html"], "Banking"),

    art("renewal-journey-holdout-design", "Insurance Renewal Holdout Design: Sample Size and Setup",
        "How to design a holdout group for a policy renewal journey: sizing rule of thumb, assignment, guardrails and a worked illustrative calculation.",
        "Insurance renewal journey holdout design: sizing and setup",
        ["holdout group design", "insurance renewal journey", "journey measurement holdout", "ajo experiment sample size"],
        "A holdout group is a random set of eligible customers who do not receive the renewal journey, so you can measure what the journey adds. Size it from your baseline renewal rate and the smallest lift you care about, assign at random before the journey starts, and agree stop rules with compliance in advance.",
        [("Why a holdout beats before-and-after", "<p>Renewals move with season, pricing and market changes. Comparing this quarter to last quarter mixes those effects into the journey result. A randomly assigned holdout faces the same conditions, so the difference between groups is a fairer estimate of what the journey did.</p>"),
         ("Sizing rule of thumb", "<p>For a yes/no outcome at roughly 95% confidence and 80% power, a common approximation is <strong>n per group &asymp; 16 &times; p &times; (1 &minus; p) / d&sup2;</strong>, where p is the baseline rate and d is the smallest absolute lift worth detecting.</p>" + tbl(["Baseline p", "Lift d", "Customers per group"], [["0.30", "0.02", "8,400"], ["0.30", "0.05", "1,344"], ["0.60", "0.03", "6,400"]]) + ILL + "<p>Treat this as a planning estimate and confirm with your analytics team.</p>"),
         ("Set it up safely", ol([("Define eligibility first", "only customers who would normally receive the journey."), ("Randomise once", "assign before the first message and keep the assignment fixed."), ("Keep service messages", "holdout customers still receive required policy communications."), ("Agree stop rules", "decide in advance what result or complaint level pauses the test.")])),
         ("Common mistakes", ul(["Holding out only low-value customers", "Re-randomising mid-journey", "Ending the test the first time the lines separate", "Measuring opens instead of renewals"]))],
        [("How large should the holdout be as a share of customers?", "Size it from the formula, not a fixed percentage. Small lifts need large groups."),
         ("Is a holdout ethical for renewals?", "Required service notices must still go out. Review the design with compliance and keep the holdout to promotional treatment only.")],
        [("Adobe Journey Optimizer documentation", "https://experienceleague.adobe.com/en/docs/journey-optimizer"), ("Customer Journey Analytics", "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-landing")],
        ["use-cases/policy-renewal-reminders.html", "use-cases/industries/insurance.html", "guides/ajo-campaigns-vs-journeys.html"], "Insurance"),

    art("airline-disruption-messaging-consent", "Airline Disruption Messages and Consent: Service vs Marketing",
        "How to separate operational disruption notices from marketing in an airline journey, map consent by purpose and test the edge cases.",
        "Airline disruption messaging and consent: service vs marketing",
        ["airline disruption notifications", "service vs marketing messages", "consent by purpose", "flight delay journey design"],
        "Flight disruption notices are operational messages, while offers and upgrades are marketing. Keep them in separate journeys, record consent by purpose and channel, and make sure a marketing opt-out never blocks a necessary service notice. Confirm the exact rules for each market with your legal team.",
        [("Two message classes", tbl(["", "Service notice", "Marketing"], [["Purpose", "Inform about the booking", "Promote or upsell"], ["Typical trigger", "Delay, gate change, cancellation", "Segment or campaign"], ["Consent basis", "Defined by your legal team", "Opt-in or as local rules require"], ["Journey", "Operational", "Promotional"]])),
         ("Design rules", ul(["Never attach an offer to a service notice unless legal approves", "Store consent by purpose and channel, not as one flag", "Choose the contact channel from the booking, not only the profile", "Send once per change, not once per system event", "Log the notice and the channel used"])),
         ("Edge cases to test", ul(["Customer opted out of marketing but has an active booking", "Two passengers on one booking with different contact details", "Delay changes three times within an hour", "Mobile number present but no app installed", "Customer in a market with stricter rules"])),
         ("Illustrative flow", "<p>Operational system emits <code>flight_disrupted</code> &rarr; journey checks booking and channel &rarr; sends notice &rarr; records outcome. Marketing journeys read the disruption event only to pause promotions.</p>" + ILL)],
        [("Can we offer a rebooking link in the notice?", "A rebooking link is usually part of the service. Offers for upgrades or partners are marketing and need separate approval."),
         ("Where does consent live in AEP?", "In consent fields in your profile schema, enforced through data usage and consent policies. Validate your own setup against the documentation.")],
        [S_GOV, S_PROF, S_ID],
        ["use-cases/flight-disruption-notifications.html", "guides/onetrust-consent-aep.html", "use-cases/consent-aware-personalisation.html"], "Travel"),

    art("hotel-loyalty-identity-reconciliation", "Hotel Loyalty Identity Reconciliation: Namespaces and Tests",
        "Reconcile loyalty ID, email, booking and device identifiers in AEP: namespace choices, merge risks and a test set for hospitality data.",
        "Hotel loyalty identity reconciliation: namespaces and tests",
        ["loyalty identity resolution", "hospitality identity graph", "aep namespaces loyalty", "guest identity stitching"],
        "Hotel guests appear as loyalty members, booking contacts and anonymous web visitors. Choose a primary person-level identifier, register the others as separate namespaces, and test for wrongly merged guests such as shared family emails or travel-agent addresses before activating anything.",
        [("Identifiers to separate", tbl(["Identifier", "Level", "Risk"], [["Loyalty number", "Person", "Low if issued once"], ["Email", "Person or shared", "Shared family and agent emails"], ["Booking reference", "Stay", "Not a person"], ["Device or cookie", "Device", "Shared devices, resets"]])),
         ("Rules that prevent bad merges", ul(["Treat booking references as event identifiers, not person identities", "Flag generic or agent emails and keep them out of person-level linking", "Limit how many people one device can represent", "Review a sample of merged profiles every release"])),
         ("Test set", ul(["Family books under one parent email", "Travel agent books for many guests", "Guest joins loyalty after three prior stays", "Guest uses two emails", "Shared hotel kiosk or lobby device"]) + ILL),
         ("What good looks like", "<p>You can answer three questions from data: who is this guest, which stays are theirs, and why were two records merged. If you cannot explain a merge, tighten the rule.</p>")],
        [("Should email be the primary identifier?", "Only if it is reliably person-level in your data. Many hospitality datasets contain shared and agent addresses, so a loyalty number is often safer."),
         ("How often should we audit merges?", "At each release and after any change to identity rules.")],
        [S_ID, S_PROF, S_XDM],
        ["services/customer-360-identity-resolution.html", "use-cases/industries/hospitality.html", "adobe-experience-platform/identity-service.html"], "Hospitality"),

    art("telecom-household-identity-churn-signals", "Telecom Household Identity and Churn Signals: Design Notes",
        "How to model household versus individual identity for a telecom CDP, which churn signals to capture and the privacy limits to set.",
        "Telecom household identity and churn signals: design notes",
        ["telecom household identity", "churn signals cdp", "telecom customer 360", "household vs individual profile"],
        "Telecom accounts often cover several people, so decide early whether a profile represents the account holder, the user or the household, and keep those levels distinct. Capture churn signals such as usage decline and unresolved service contacts, and limit who can see household-level inferences.",
        [("Three profile levels", tbl(["Level", "Use", "Caution"], [["Account holder", "Billing, contracts", "May not be the user"], ["Line user", "Usage and device signals", "Often unknown on shared lines"], ["Household", "Bundle offers", "Inferred groupings need governance"]])),
         ("Signals worth capturing", ul(["Usage trend against the customer's own baseline", "Repeated service contacts or unresolved tickets", "Contract end and recent plan changes", "Payment friction events", "Device age where it is known"])),
         ("Privacy limits", ul(["Do not expose one household member's data to another", "Label inferred household links as inferred", "Keep sensitive attributes out of churn models unless approved", "Document the purpose of each signal"])),
         ("Validation", "<p>Back-test the signals on past cancellations before using them in a live journey, and compare with a control group. A signal that cannot be explained to a service agent is hard to act on.</p>" + ILL)],
        [("Is a household profile always useful?", "No. It helps for bundle and family-plan offers, but it adds privacy and accuracy risk. Start with account and line levels."),
         ("Which churn signal matters most?", "It varies by business. Test candidates against your own history rather than assuming.")],
        [S_PROF, S_ID, S_GOV],
        ["solutions/churn-prevention.html", "use-cases/industries/telecom.html", "services/customer-360-identity-resolution.html"], "Telecom"),

    art("healthcare-data-minimization-checklist", "Healthcare Engagement Data Minimization Checklist",
        "A practical checklist for limiting data in healthcare engagement journeys: purpose, fields, retention, labels and access, with review questions.",
        "Healthcare engagement data minimization checklist",
        ["data minimization checklist", "healthcare marketing data governance", "aep data usage labels healthcare", "privacy by design martech"],
        "Data minimization means collecting and activating only what a stated purpose needs. For healthcare engagement, list the purpose first, keep clinical detail out of marketing systems unless your legal team approves it, label sensitive fields, set retention, and restrict access. This is general guidance, not legal advice.",
        [("Checklist", ul(["State the purpose of each journey in one sentence", "List every field used and remove any without a named use", "Keep diagnosis and treatment detail out of marketing profiles unless approved", "Apply data usage labels to sensitive fields", "Set retention for events and profiles", "Limit access by role and review it", "Check destinations and vendors before sending any attribute", "Keep an audit trail of changes"])),
         ("Review questions", ul(["Would the person expect this use of their data?", "Can the message work without the sensitive field?", "Who can see the field, and why?", "What happens if the destination is breached?"])),
         ("Where AEP features help", "<p>Data usage labels and policies can restrict how labelled fields are used and where they are sent. They support your process; they do not replace legal review. Test that a policy blocks a prohibited activation.</p>"),
         ("Local rules", "<p>Health privacy rules differ by country and organisation (for example HIPAA in the United States). Confirm which apply with your privacy officer before design.</p>")],
        [("Can we use appointment data in marketing journeys?", "Only if your legal and privacy teams approve the purpose and consent. Many organisations keep appointment reminders as service messages."),
         ("Is pseudonymised data safe to use?", "It reduces risk but may still be personal data. Check your local definition.")],
        [S_GOV, ("Data usage labels glossary", f"{EL}/data-governance/labels/reference"), S_PROF],
        ["services/consent-governance-privacy.html", "use-cases/industries/healthcare.html", "insights/data-privacy.html"], "Healthcare"),

    art("saas-product-usage-signals", "SaaS Product Usage Signals: Event Taxonomy for CDPs",
        "Design a clean event taxonomy for SaaS product usage, define activation signals and send them to a CDP without flooding it with noise.",
        "SaaS product usage signals: an event taxonomy for CDPs",
        ["product usage signals", "saas event taxonomy", "product qualified lead", "usage data cdp"],
        "To use product usage in marketing, define a small taxonomy of events that mean something, such as account created, key feature used and seat added. Send those to the CDP with account and user identifiers, and compute signals like activation or risk from them rather than streaming every click.",
        [("Taxonomy rules", ul(["Use object_action names, such as report_created", "Keep one definition per event across web, app and backend", "Attach both user and account identifiers", "Version the taxonomy and record changes"])),
         ("Illustrative signals", tbl(["Signal", "Built from", "Possible use"], [["Activated", "Key feature used within first days", "Onboarding journey exit"], ["Expanding", "Seats or usage rising", "Account team alert"], ["At risk", "Usage drop against own baseline", "Service outreach"]]) + ILL),
         ("What to keep out of the CDP", ul(["Every raw click", "Free-text user input", "Fields that identify end customers of your customers", "Events nobody can name a use for"])),
         ("Account versus user", "<p>B2B SaaS decisions happen at account level. Model both and make sure a signal can roll up from users to the account without double counting.</p>")],
        [("Should product events go to the CDP or the warehouse?", "Both can hold them. Keep detailed history in the warehouse and send curated signals to the CDP for activation."),
         ("How many events are enough?", "Enough to support your signals. Start small and add on demand.")],
        [S_XDM, S_ING, S_ID],
        ["solutions/b2b-lead-to-revenue.html", "use-cases/industries/saas.html", "services/data-engineering.html"], "SaaS"),

    art("retail-store-to-web-validation", "Retail Store-to-Web Validation: Reconciliation Tests",
        "How to validate that in-store purchases link to the right online profiles: match-rate checks, sampling, false-match review and reporting rules.",
        "Retail store-to-web attribution validation: reconciliation tests",
        ["store to web identity", "omnichannel validation", "offline online matching", "retail identity tests"],
        "Linking store purchases to online profiles creates value only if the matches are right. Measure the match rate, sample matched records for false links, compare totals against the finance source, and report matched and unmatched sales separately so nobody mistakes coverage for attribution.",
        [("Four checks", ol([("Match rate", "share of store transactions linked to a known profile, by store and channel."), ("False-match sample", "review a random set of links by hand against a trusted key."), ("Total reconciliation", "store sales in the CDP against the finance system for the same period."), ("Timing", "how long after the sale the link appears and whether late links change reports.")])),
         ("Illustrative result table", tbl(["Check", "Pass condition", "If it fails"], [["Match rate", "Stable week to week", "Look for a store capture change"], ["False matches", "Below the threshold you set", "Tighten the matching rule"], ["Reconciliation", "Within an agreed tolerance", "Find missing feeds"]]) + ILL),
         ("Reporting rules", ul(["Show matched and unmatched sales separately", "Do not extrapolate matched behaviour to all stores", "State the matching rule next to every chart", "Record changes to capture practices"])),
         ("Consent", "<p>Loyalty sign-up and receipt capture must follow your consent rules. Check them before activating in-store identifiers.</p>")],
        [("What match rate is good?", "It depends on how identifiers are captured in store. Track your own trend instead of a benchmark."),
         ("Can we attribute online ads to store sales?", "Only with a defensible method such as a holdout. Matching alone does not prove cause.")],
        [S_ID, S_PROF, ("Customer Journey Analytics", "https://experienceleague.adobe.com/en/docs/analytics-platform/using/cja-landing")],
        ["use-cases/industries/retail.html", "case-studies/retail-omnichannel-identity-stitching.html", "guides/hashed-email-identity-aep.html"], "Retail"),

    art("aep-batch-ingestion-failure-diagnostic", "AEP Batch Ingestion Failure: A Diagnostic Worksheet",
        "A step-by-step worksheet to find why an AEP batch failed or loaded nothing: status, schema, identity, format and volume checks in order.",
        "AEP batch ingestion failure: a diagnostic worksheet",
        ["aep batch ingestion failed", "aep dataset no data", "aep ingestion troubleshooting", "xdm validation error"],
        "When a batch fails or a dataset stays empty, work from the outside in: check the batch status and error message, confirm the target dataset and schema, check required fields and identities, then file format and size. Change one thing at a time and keep a record of each retry.",
        [("Worksheet", ol([("Find the batch", "note batch ID, dataset, time and the status shown in monitoring."), ("Read the error", "copy the exact message and the first failing record if shown."), ("Confirm the target", "right dataset, right schema, profile enabled only if intended."), ("Check required fields", "mandatory XDM fields and data types match the file."), ("Check identities", "identity fields are populated and use the expected namespace."), ("Check format", "dates, nulls, delimiters and encoding."), ("Retry small", "resend a few rows before the full file.")])),
         ("Common causes", tbl(["Symptom", "Likely cause", "Check"], [["Failed with schema error", "Type or field mismatch", "Mapping and source column types"], ["Succeeded but no profiles", "Dataset not profile-enabled or no identity", "Dataset settings and identity fields"], ["Partial load", "Bad rows rejected", "Error report for the batch"], ["Slow or stuck", "Very large file", "Split the file and retry"]])),
         ("Write it down", "<p>Record what you changed and what happened. A short log turns a repeat failure into a five-minute fix and gives support the facts they need.</p>"),
         ("Related checks", "<p>For validating a big load after it succeeds, see the guide on validating large batch ingestion.</p>")],
        [("Should I retry the same file?", "Not before you know the cause. Fix the reason, then retry a small sample."),
         ("Where do I find the error?", "In the ingestion monitoring views and the batch details; the exact screens depend on your product version, so follow the current documentation.")],
        [S_ING, S_XDM, S_PROF],
        ["guides/validate-large-batch-ingestion.html", "guides/aep-ingestion-methods-batch-streaming.html", "adobe-experience-platform/data-ingestion.html"], "Troubleshooting"),

    art("identity-graph-collapse-test-lab", "Identity Graph Collapse: A Test Lab with Synthetic Data",
        "A hands-on lab to test whether shared identifiers wrongly merge people in an identity graph, using synthetic data and clear pass criteria.",
        "Identity graph collapse test lab: synthetic data and pass criteria",
        ["identity graph collapse", "aep identity test", "identity resolution testing", "shared device identity"],
        "A graph collapse happens when a shared identifier, such as a family device or generic email, links people who are different. Test for it before go-live using synthetic data with deliberately shared identifiers, then check that profiles stay separate and that your rules limit the damage.",
        [("Lab design", ol([("Create synthetic people", "twenty fictional customers, no real data."), ("Add traps", "a shared tablet, a family email, a generic company address."), ("Load the data", "use a sandbox and the same ingestion path as production."), ("Inspect the graph", "check which profiles merged and why."), ("Adjust rules", "change namespace priority or exclusions, then repeat.")])),
         ("Pass criteria", ul(["No two synthetic people are merged by a shared device or generic email", "Every merge can be explained from the data", "A deliberate real link, such as a login on two devices, does merge", "Results are repeatable on a second run"])),
         ("Trap table", tbl(["Trap", "Expected result"], [["Shared tablet used by two logins", "Two people remain separate"], ["Family email on two accounts", "Separate unless a rule says otherwise"], ["Generic company inbox", "Not used for person linking"], ["Same login on phone and laptop", "One person"]]) + ILL),
         ("Why a sandbox", "<p>Run the lab in a development sandbox so a test cannot touch production profiles. Check product limits and behaviour for your version in the documentation.</p>")],
        [("Can this lab use real customer data?", "Avoid it. Synthetic data makes results repeatable and keeps personal data out of testing."),
         ("How often should we rerun it?", "After any change to identity namespaces, priorities or sources.")],
        [S_ID, S_PROF, S_ING],
        ["adobe-experience-platform/identity-service.html", "services/customer-360-identity-resolution.html", "guides/hashed-email-identity-aep.html"], "Identity"),
]
