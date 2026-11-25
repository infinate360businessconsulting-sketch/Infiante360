#!/usr/bin/env python3
"""Print the detail behind seo-health.json and a compact route table to stdout (for CI logs).
Usage: python3 scripts/seo_report_print.py <seo_report_dir>
Read-only. Output is plain text so it can be read from `gh run view --log` when artifacts cannot be downloaded.
"""
import json, os, sys

d = sys.argv[1]
h = json.load(open(os.path.join(d, "seo-health.json")))
inv = {r["file"]: r for r in json.load(open(os.path.join(d, "route-inventory.json")))}
by_route = {r["route"]: r for r in inv.values()}


def row(f):
    r = inv.get(f.lstrip("/")) or by_route.get(f) or {}
    return f"{f} | {r.get('title_len','?')} | {r.get('title','')} | H1={r.get('h1',[''])[:1]} | words={r.get('words','?')} | in={r.get('inbound_links','?')}"


for key in ["title_over_65", "orphans_indexable", "indexable_pages_missing_from_sitemap", "missing_h1", "missing_description",
            "missing_canonical", "thin_pages_under_250_words", "desc_over_160", "multiple_h1", "pages_without_jsonld"]:
    print(f"### {key} ({len(h[key])})")
    for f in h[key]:
        print("  " + row(f))
for key in ["duplicate_h1", "duplicate_titles", "duplicate_descriptions"]:
    print(f"### {key} ({len(h[key])})")
    for k, v in h[key].items():
        print(f"  {k!r}: {v}")
print("### ROUTES")
for r in sorted(inv.values(), key=lambda x: x["route"]):
    print(f"R|{r['route']}|{r['title_len']}|{r['words']}|{r['inbound_links']}|{'N' if r['noindex'] else 'I'}|{r['title']}|{(r['h1'] or [''])[0]}")
