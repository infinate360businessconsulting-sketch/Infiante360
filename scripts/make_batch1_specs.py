#!/usr/bin/env python3
"""Diagram specs for guide batch 1 (10 guides) -> data/visuals/specs/<slug>.json, then run:
   python3 scripts/visual_engine.py build <slugs> && python3 scripts/image_pipeline.py <slugs>
Same spec format as make_article_specs.py. Labels are short and exact (deterministic SVG, no generative model)."""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "visuals", "specs")
NOTE = "Illustrative teaching schematic, not a client deployment."
S = {
 "xdm-schema-design-checklist": ("XDM schema design checklist", "Class, field groups, identity, then Profile", "red", "flow",
   [("Class", ["Profile or event", "Decide first"]), ("Fields", ["Field groups", "Custom namespace"]), ("Identity", ["Primary identity", "Namespace"]), ("Enable", ["Profile only if needed", "Hard to undo"])], "Plan the schema before the first dataset exists."),
 "aep-sandboxes-schemas-datasets": ("Sandboxes, schemas and datasets", "How the objects nest", "cyan", "layers",
   [("Sandbox", ["Development", "Production"]), ("Schema", ["Structure and rules"]), ("Dataset", ["Stored data"]), ("Batches", ["Each load"])], "Every object belongs to one sandbox."),
 "audience-evaluation-batch-streaming-edge": ("Audience evaluation methods", "Batch, streaming and edge compared", "violet", "flow",
   [("Batch", ["Scheduled", "Complex rules"]), ("Streaming", ["Continuous", "Rule limits apply"]), ("Edge", ["Immediate", "Narrowest rules"]), ("Choose", ["By how fast it must react"])], "Check current eligibility rules in the documentation."),
 "rtcdp-destination-activation-checklist": ("Destination activation checklist", "Before an audience leaves the platform", "orange", "flow",
   [("Purpose", ["Why send it", "Which marketing action"]), ("Fields", ["Only what is needed", "Identity to match"]), ("Policy", ["Labels checked", "Consent applied"]), ("Verify", ["Sample records", "Count at destination"])], "Send the minimum that does the job."),
 "aep-data-usage-labels-policies": ("Data usage labels and policies", "Label the data, then govern the use", "red", "flow",
   [("Label", ["Fields and datasets"]), ("Define", ["Marketing actions", "Policies"]), ("Enforce", ["At activation"]), ("Review", ["Blocked cases", "Owners"])], "Labels do nothing until a policy uses them."),
 "cja-vs-adobe-analytics-decision": ("Customer Journey Analytics or Adobe Analytics", "Choose by question, not by product", "cyan", "flow",
   [("Questions", ["Single channel", "Cross-channel"]), ("Data", ["Report suites", "AEP datasets"]), ("Identity", ["Visitor", "Person ID"]), ("Plan", ["Run both", "Migrate in stages"])], "Reconcile before you switch anything off."),
 "web-sdk-datastreams-event-design": ("Web SDK datastreams and events", "From page to platform", "violet", "flow",
   [("Page", ["Data layer", "Consent"]), ("SDK", ["Configure", "Send event"]), ("Datastream", ["Services chosen", "Per environment"]), ("Platform", ["Dataset", "Validate"])], "Keep one event model across web and app."),
 "mcp-vs-rest-enterprise-agents": ("MCP or direct REST for agents", "What each gives you and what it leaves to you", "orange", "layers",
   [("Agent", ["Chooses a tool"]), ("MCP server", ["Describes tools", "Applies policy"]), ("REST API", ["Does the work"]), ("Platform", ["Your data"])], "Policy lives in the server, not in the prompt."),
 "enterprise-ai-coworker-scope-guardrails": ("Scoping an AI coworker", "Task, access, review", "red", "flow",
   [("Task", ["One narrow job", "Written scope"]), ("Access", ["Least privilege", "Read first"]), ("Guardrails", ["Blocked actions", "Logging"]), ("Review", ["Human sign-off", "Weekly sample"])], "Widen scope only after evidence."),
 "customer-360-data-model-layers": ("Customer 360 data model", "Layers, keys and owners", "cyan", "layers",
   [("Sources", ["CRM", "Web", "Commerce"]), ("Identity", ["Keys", "Match rules"]), ("Profile", ["Attributes", "Events"]), ("Use", ["Audiences", "Analytics", "Service"])], "Every layer needs a named owner."),
}
os.makedirs(OUT, exist_ok=True)
for slug, (title, sub, accent, kind, lanes, band) in S.items():
    spec = dict(id="IMG-ART-" + slug[:24].upper().replace("-", ""), slug=slug, page=f"guides/{slug}.html", title=title, subtitle=sub, keyword=title.lower(),
                kind=kind, accent=accent, kicker="Infiante360 guide", band=band, note=NOTE,
                alt=f"Schematic diagram: {title.lower()} - " + ", ".join(l[0].lower() for l in lanes) + ".", caption=f"{title}: schematic.")
    spec["layers" if kind == "layers" else "lanes"] = [dict(title=t, items=i) for t, i in lanes]
    json.dump(spec, open(os.path.join(OUT, slug + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(S), "specs written:", " ".join(S))
