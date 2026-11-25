#!/usr/bin/env python3
"""Source of truth for the 20 article diagram specs -> data/visuals/specs/<slug>.json (consumed by visual_engine.py).
Each spec is an original schematic of the article's own steps; labels are short and exact. Run: python3 scripts/make_article_specs.py"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "visuals", "specs")
NOTE = "Illustrative teaching schematic, not a client deployment."
# slug: (title, subtitle, accent, kind, [(lane title, [items])...], band)
S = {
 "loan-onboarding-event-model": ("Loan onboarding event model", "From enquiry to decision, with exits that stop messages", "red", "flow",
   [("Enquiry", ["application_started", "Anonymous ID"]), ("Progress", ["documents_uploaded", "verification_pending"]), ("Decision", ["decision_made", "Stops all nudges"]), ("Rules", ["Consent check", "Suppress while open"])], "Define exit events before building any message."),
 "renewal-journey-holdout-design": ("Renewal holdout design", "Random holdout to measure what the journey adds", "violet", "flow",
   [("Eligible", ["Customers due to renew"]), ("Randomise", ["Assign once", "Keep fixed"]), ("Treat", ["Journey group", "Holdout group"]), ("Compare", ["Renewal rate", "Agreed stop rules"])], "Size the groups from baseline rate and the smallest lift that matters."),
 "airline-disruption-messaging-consent": ("Disruption messages and consent", "Service notices kept apart from marketing", "cyan", "flow",
   [("Event", ["flight_disrupted"]), ("Checks", ["Booking and channel", "Consent by purpose"]), ("Send", ["Service notice", "One per change"]), ("Log", ["Outcome and channel", "Pause promotions"])], "A marketing opt-out never blocks a necessary service notice."),
 "hotel-loyalty-identity-reconciliation": ("Hotel guest identity reconciliation", "Separate namespaces, explainable merges", "orange", "flow",
   [("Identifiers", ["Loyalty number", "Email", "Booking reference"]), ("Rules", ["Person vs stay", "Flag shared emails"]), ("Merge", ["Explainable links"]), ("Audit", ["Sample merges", "Each release"])], "If you cannot explain a merge, tighten the rule."),
 "telecom-household-identity-churn-signals": ("Household identity and churn signals", "Account, user and household kept distinct", "red", "flow",
   [("Levels", ["Account holder", "Line user", "Household"]), ("Signals", ["Usage trend", "Service contacts"]), ("Limits", ["Label inferred links", "Restrict access"]), ("Validate", ["Back-test", "Control group"])], "Start with account and line levels."),
 "healthcare-data-minimization-checklist": ("Healthcare data minimization", "Purpose first, fewest fields, clear limits", "cyan", "flow",
   [("Purpose", ["One sentence per journey"]), ("Fields", ["Remove unused", "Label sensitive"]), ("Controls", ["Retention", "Role access"]), ("Review", ["Destinations", "Audit trail"])], "General guidance, not legal advice."),
 "saas-product-usage-signals": ("SaaS usage signals taxonomy", "Few meaningful events, signals computed", "violet", "flow",
   [("Events", ["object_action names", "User and account IDs"]), ("Signals", ["Activated", "Expanding", "At risk"]), ("CDP", ["Curated signals only"]), ("Warehouse", ["Detailed history"])], "Do not stream every click."),
 "retail-store-to-web-validation": ("Store-to-web validation", "Four checks before trusting matches", "orange", "flow",
   [("Match rate", ["By store", "By channel"]), ("False matches", ["Hand-review sample"]), ("Reconcile", ["Against finance totals"]), ("Report", ["Matched vs unmatched", "State the rule"])], "Coverage is not attribution."),
 "aep-batch-ingestion-failure-diagnostic": ("Batch ingestion diagnostic", "Work from the outside in", "red", "flow",
   [("Find", ["Batch ID", "Status"]), ("Read", ["Exact error"]), ("Check", ["Dataset and schema", "Identities"]), ("Retry", ["Few rows first", "Log each change"])], "Change one thing at a time."),
 "identity-graph-collapse-test-lab": ("Identity graph collapse lab", "Synthetic data with deliberate traps", "cyan", "flow",
   [("Create", ["Twenty fictional people"]), ("Add traps", ["Shared tablet", "Family email"]), ("Load", ["Sandbox", "Production path"]), ("Inspect", ["Who merged and why"])], "Repeat after any identity rule change."),
 "web-sdk-consent-regression-testing": ("Web SDK consent regression test", "Same matrix on every release", "violet", "flow",
   [("Set state", ["Clean browser", "Choose option"]), ("Record", ["Network calls", "Payloads"]), ("Compare", ["Expected row"]), ("Evidence", ["Date and build", "Files kept"])], "Technical evidence, not legal proof."),
 "cja-backfill-reconciliation-workbook": ("CJA backfill reconciliation", "Prove the data before sign-off", "orange", "flow",
   [("Scope", ["Dataset", "Date range"]), ("Compare", ["Daily counts", "Distinct people"]), ("Explain", ["Each difference", "Cause"]), ("Sign off", ["Agreed tolerance", "Owner approves"])], "Agree the tolerance in advance."),
 "enterprise-ai-agent-approval-gate": ("AI agent approval gate", "Tier actions by impact and reversibility", "red", "layers",
   [("Read only", ["Automatic", "Logged"]), ("Reversible write", ["Sandbox only"]), ("Customer-facing", ["Human approval"]), ("Destructive or financial", ["Blocked", "Two approvers"])], "Agents cannot approve their own actions."),
 "snowflake-incremental-load-lab": ("Snowflake incremental load", "Staging, merge, watermark, reconcile", "cyan", "flow",
   [("Stage", ["Changed rows", "Change timestamp"]), ("Merge", ["Match on key", "Update or insert"]), ("Watermark", ["Highest change time"]), ("Reconcile", ["Counts match", "Rerun is safe"])], "A rerun must change nothing."),
 "martech-coe-operating-model-raci": ("MarTech CoE operating model", "Scope, owners, cadence", "violet", "layers",
   [("Intake", ["Weekly review", "Ranked backlog"]), ("Standards", ["Data and platform", "Quarterly review"]), ("Architecture", ["Decision records"]), ("Enablement", ["Docs", "Training"])], "A CoE that approves everything becomes a bottleneck."),
 "ajo-reference-architecture": ("Journey Optimizer reference architecture", "Data, orchestration, content, channels, governance", "red", "layers",
   [("Data", ["Profiles", "Events", "Audiences"]), ("Orchestration", ["Journeys", "Triggers"]), ("Content", ["Templates", "Offers"]), ("Channels", ["Email", "Push", "SMS"]), ("Governance", ["Consent", "Frequency"])], "Verify capabilities against current documentation."),
 "cja-reference-architecture": ("Customer Journey Analytics architecture", "Datasets, connection, data view, workspace", "cyan", "layers",
   [("Datasets", ["Events", "Lookups"]), ("Connection", ["Person ID join"]), ("Data view", ["Metrics", "Dimensions"]), ("Workspace", ["Reports", "Analysis"])], "Give every data view an owner."),
 "test-agentic-ai-implementation": ("Testing an agentic AI build", "Four areas, pass criteria set first", "violet", "flow",
   [("Tool choice", ["Right tool", "Right arguments"]), ("Permissions", ["Refuses delete"]), ("Injection", ["Hidden instruction ignored"]), ("Consistency", ["Fixed evaluation set"])], "Block release if a permission test fails."),
 "test-consent-governance-implementation": ("Consent and governance tests", "Try to break the controls", "orange", "flow",
   [("No consent", ["Excluded from activation"]), ("Labels", ["Blocked destination"]), ("Withdrawal", ["Removed from audiences"]), ("Requests", ["Reach all systems"])], "Keep dated evidence of each test."),
 "test-real-time-personalization": ("Real-time personalization tests", "Data, decision, fallback, measurement", "red", "flow",
   [("Data", ["Event arrives in time"]), ("Decision", ["Test profile per audience"]), ("Fallback", ["Default if data missing"]), ("Measure", ["Control group"])], "Launch only when every level passes."),
}
for slug, (title, sub, accent, kind, lanes, band) in S.items():
    spec = dict(id="IMG-ART-" + slug[:24].upper().replace("-", ""), slug=slug, page=f"guides/{slug}.html", title=title, subtitle=sub, keyword=title.lower(),
                kind=kind, accent=accent, kicker="Infiante360 guide", band=band, note=NOTE,
                alt=f"Schematic diagram: {title.lower()} - " + ", ".join(l[0].lower() for l in lanes) + ".", caption=f"{title}: schematic.")
    if kind == "layers":
        spec["layers"] = [dict(title=t, items=i) for t, i in lanes]
    else:
        spec["lanes"] = [dict(title=t, items=i) for t, i in lanes]
    json.dump(spec, open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(S), "article specs written")
