#!/usr/bin/env python3
"""Map all ingested keywords to canonical URLs, actions and gaps. Deterministic and re-runnable.

Inputs : data/seo/keywords.json, data/seo/cluster_url_map.json (owner-reviewable decisions), data/seo/route_snapshot.json (real routes)
Outputs: data/seo/keyword_url_mapping.{json,csv}, content_gap_registry.json, page_generation_queue.json,
         keyword_coverage_report.json, docs/KEYWORD_COVERAGE_REPORT.md
Rules : no volumes/difficulty/rankings are invented (stored as null). Every keyword gets exactly one record.
        One new page per justified gap cluster, never one page per keyword.
"""
import csv, json, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, "data", "seo")
J = lambda n: json.load(open(os.path.join(D, n), encoding="utf-8"))

kws = J("keywords.json")
cmap = J("cluster_url_map.json")["clusters"]
routes = {r["route"]: r for r in J("route_snapshot.json")["routes"]}

COMMERCIAL_C = {"consulting", "services", "consulting company", "implementation partner", "architecture assessment", "consulting cost",
                "managed support", "implementation assessment", "consultant India", "remote consulting", "proof of concept"}
CORP_T = {"corporate training", "training for enterprise teams", "training for global teams"}
FEES = {"course fees", "consulting cost"}
NEW_PAGES = {  # one planned page per justified gap cluster
    "Snowflake for MarTech": "/services/snowflake-martech-integration.html",
    "BigQuery for MarTech": "/services/bigquery-martech-integration.html",
    "Databricks for MarTech": "/services/databricks-martech-integration.html",
    "Kafka streaming for customer data": "/services/kafka-streaming-customer-data.html",
    "Enterprise architecture": "/services/enterprise-architecture-consulting.html",
}
CTA = {"training": "/lp/career-accelerator-admission.html", "corporate": "/lp/corporate-adobe-training.html", "consulting": "/lp/adobe-martech-conversation.html"}
CTA_OVERRIDE = {"Adobe MarTech staff augmentation": "/lp/hire-aep-contract-talent.html", "Executive MarTech and AI leadership": "/lp/cxo-hive-apply.html",
                "Agentic AI for MarTech": "/lp/agentic-ai-mcp-workshop.html", "Model Context Protocol": "/lp/agentic-ai-mcp-workshop.html",
                "Agentic AI implementation": "/lp/agentic-ai-mcp-workshop.html", "Enterprise MCP integration": "/lp/agentic-ai-mcp-workshop.html",
                "MarTech stack audit": "/lp/aep-architecture-review.html", "Adobe Experience Platform implementation": "/lp/aep-architecture-review.html",
                "Adobe MarTech corporate enablement": "/lp/corporate-adobe-training.html"}

problems = []


def need(url):
    if url and url not in routes:
        problems.append(url)
    return url


recs = []
for k in kws:
    cl, kw = k["cluster"], k["keyword"]
    c = cmap[cl]
    mod = kw[len(cl) + 1:] if kw.startswith(cl + " ") else kw
    fam = c["f"]
    informational = k["intent"] == "Informational"
    primary = need(c["primary"])
    info = need(c.get("info"))
    secondary, gap = [], []
    interim, canonical = primary, primary
    if fam == "training":
        if mod in CORP_T and cl != "Adobe MarTech corporate enablement":
            canonical = need("/training/corporate-training.html"); secondary.append(primary)
            gap.append(f"Corporate page is generic; add a {cl} section for enterprise teams")
        elif mod == "workshop":
            canonical = need("/academy/workshops.html"); secondary.append(primary)
        elif mod in ("hands-on labs", "practical exercises", "project portfolio") and cl != "Adobe sandbox labs":
            secondary.append(need("/academy/hands-on-projects.html"))
        elif mod in ("learning roadmap", "training for beginners", "training for experienced professionals"):
            secondary.append(need("/academy/career-paths-by-background.html"))
            if info: secondary.append(info)
        elif mod == "assessment questions" and cl.startswith(("Adobe Experience Platform", "AEP")):
            secondary.append(need("/academy/aep-bfsi-quiz.html"))
        if mod in FEES: gap.append("Fees must come from the approved programme catalogue; do not publish unconfirmed prices")
        if mod in ("training India", "training for global teams"): gap.append("Add genuine delivery-format and timezone detail; do not imply local offices")
        cta = CTA["corporate"] if canonical.endswith("corporate-training.html") else CTA["training"]
    else:
        if informational and info: canonical = info; secondary.append(primary)
        if mod in ("architecture assessment", "implementation assessment") and cl != "MarTech stack audit":
            secondary.append(need("/lp/aep-architecture-review.html"))
        if mod in FEES: gap.append("No published pricing: explain scoping factors only; do not invent figures")
        if mod == "consultant India": gap.append("Use accurate location context; do not claim offices or in-country delivery unless confirmed")
        cta = CTA["consulting"]
    cta = CTA_OVERRIDE.get(cl, cta) if not canonical.endswith("corporate-training.html") else cta
    need(cta)
    if c.get("gap"): gap.append(c["gap"])
    action = "ENHANCE_EXISTING_FAQ" if informational else "OPTIMIZE_EXISTING_PAGE"
    status = "MAPPED_NOT_IMPLEMENTED"
    planned = None
    if cl in NEW_PAGES:
        planned = NEW_PAGES[cl]; interim = primary
        action = "CREATE_COMMERCIAL_LANDING_PAGE" if not informational else "CREATE_TECHNICAL_ARTICLE"
        canonical = planned; status = "QUEUED_AWAITING_OWNER_APPROVAL"
    if c.get("research"):
        action = "RESEARCH_REQUIRED"; status = "BLOCKED_OWNER_CONFIRMATION"
    seo = "Existing page: per-page audit pending" if not planned else "New page not built"
    recs.append({
        "keyword_id": k["id"], "keyword": kw, "cluster": cl, "modifier": mod, "family": fam, "search_intent": k["intent"],
        "target_audience": k.get("audience"), "geography": k.get("geographies"),
        "existing_url": primary if primary in routes else None, "recommended_canonical": canonical, "planned_new_url": planned,
        "interim_url": interim, "secondary_urls": [s for s in dict.fromkeys(secondary) if s != canonical],
        "existing_content_quality": "Not assessed (no per-page content review yet)", "competitor_references": None,
        "content_gap": "; ".join(dict.fromkeys(gap)) or "None identified at mapping level; page-level review pending",
        "required_action": action, "commercial_relevance": k.get("conversion_hypothesis"), "priority": k.get("priority"),
        "conversion_cta": cta, "implementation_status": status,
        "image_requirement": "Original diagram or illustration for the target page" if planned or fam == "training" else "Original architecture diagram for the target page",
        "seo_status": seo, "geo_status": "Not assessed", "aeo_status": "Not assessed",
        "monthly_volume": None, "difficulty": None, "ranking": None,
        "evidence": "Rule-based mapping from cluster decisions and the CI route snapshot; no SERP, volume or competitor data used",
        "source_row": k.get("_source_row"), "source_sheet": k.get("source_sheet"),
    })

assert not problems, f"targets not in route snapshot: {sorted(set(problems))}"
assert len(recs) == len(kws) == len({r["keyword_id"] for r in recs})

json.dump(recs, open(os.path.join(D, "keyword_url_mapping.json"), "w"), indent=1, ensure_ascii=False)
cols = list(recs[0])
with open(os.path.join(D, "keyword_url_mapping.csv"), "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
    for r in recs: w.writerow({c: ("; ".join(r[c]) if isinstance(r[c], list) else r[c]) for c in cols})

by_cluster = collections.defaultdict(list)
for r in recs: by_cluster[r["cluster"]].append(r)
gaps = []
for cl, rs in by_cluster.items():
    g = cmap[cl].get("gap")
    if g: gaps.append({"cluster": cl, "family": cmap[cl]["f"], "gap": g, "existing_page": cmap[cl]["primary"], "keywords": len(rs),
                       "planned_new_url": NEW_PAGES.get(cl), "needs_owner_input": bool(cmap[cl].get("research")) or cl in NEW_PAGES})
gaps += [
    {"cluster": "ALL training", "gap": "Programme fees, schedules and durations must be reconciled against the approved catalogue before any are published", "needs_owner_input": True},
    {"cluster": "ALL", "gap": "Search volume, difficulty, SERP and competitor data are unmeasured; validate in Search Console / Keyword Planner", "needs_owner_input": False},
]
json.dump({"gaps": gaps}, open(os.path.join(D, "content_gap_registry.json"), "w"), indent=1)

queue = []
for cl, url in NEW_PAGES.items():
    rs = by_cluster[cl]
    queue.append({"queue_id": f"PG-{len(queue)+1:03d}", "type": "CREATE_COMMERCIAL_LANDING_PAGE", "planned_url": url, "cluster": cl,
                  "keyword_ids": [r["keyword_id"] for r in rs], "interim_url": cmap[cl]["primary"], "status": "QUEUED_AWAITING_OWNER_APPROVAL",
                  "requirements": ["Confirm genuine delivery experience for this platform", "Original architecture diagram (SVG)", "Sources: official vendor documentation",
                                   "No client names, results or partnership claims without evidence", "Distinct intent from /services/cloud-data-platforms.html and /services/data-engineering.html"],
                  "generated": False})
queue.append({"queue_id": f"PG-{len(queue)+1:03d}", "type": "RESEARCH_REQUIRED", "cluster": "Adobe Commerce",
              "keyword_ids": [r["keyword_id"] for r in by_cluster["Adobe Commerce"]], "status": "BLOCKED_OWNER_CONFIRMATION",
              "requirements": ["Owner confirms whether Adobe Commerce delivery is a real offering"], "generated": False})
json.dump({"queue": queue, "note": "Nothing in this queue has been generated or published."}, open(os.path.join(D, "page_generation_queue.json"), "w"), indent=1)

cnt = lambda key: dict(collections.Counter(r[key] for r in recs))
tgt = collections.Counter(r["recommended_canonical"] for r in recs)
report = {"keywords_total": len(kws), "keywords_mapped": len(recs), "keywords_unmapped": len(kws) - len(recs), "clusters": len(by_cluster),
          "by_action": cnt("required_action"), "by_family": cnt("family"), "by_status": cnt("implementation_status"), "by_intent": cnt("search_intent"),
          "distinct_canonical_targets": len(tgt), "existing_pages_targeted": sum(1 for u in tgt if u in routes), "planned_new_pages": len(NEW_PAGES),
          "top_targets": tgt.most_common(12), "metrics_measured": False,
          "route_snapshot_source": J("route_snapshot.json")["source"]}
json.dump(report, open(os.path.join(D, "keyword_coverage_report.json"), "w"), indent=1)

md = ["# Keyword coverage report", "", f"Generated by `scripts/seo_keyword_map.py` from `data/seo/keywords.json` and the CI route snapshot ({report['route_snapshot_source']}).", "",
      f"- Keywords imported: {report['keywords_total']}", f"- Keywords mapped to a canonical target: {report['keywords_mapped']} (unmapped: {report['keywords_unmapped']})",
      f"- Clusters: {report['clusters']}", f"- Distinct canonical targets: {report['distinct_canonical_targets']} ({report['existing_pages_targeted']} existing pages, {report['planned_new_pages']} planned new pages)",
      "- Search volume, difficulty, rankings and competitor data: **not measured** (stored as null)", "", "## By required action", ""]
md += [f"- {k}: {v}" for k, v in sorted(report["by_action"].items())]
md += ["", "## By status", ""] + [f"- {k}: {v}" for k, v in sorted(report["by_status"].items())]
md += ["", "## Most-targeted existing pages", ""] + [f"- {u}: {n} keywords" for u, n in report["top_targets"]]
md += ["", "## Planned new pages (awaiting owner approval, not generated)", ""] + [f"- {u}" for u in NEW_PAGES.values()]
md += ["", "## Open gaps", ""] + [f"- {g['cluster']}: {g['gap']}" for g in gaps]
md += ["", "Mapping is a recommendation. Each keyword still needs page-level review before content changes.", ""]
open(os.path.join(ROOT, "docs", "KEYWORD_COVERAGE_REPORT.md"), "w", encoding="utf-8").write("\n".join(md))
print(json.dumps({k: report[k] for k in ("keywords_mapped", "by_action", "by_status", "distinct_canonical_targets")}))
