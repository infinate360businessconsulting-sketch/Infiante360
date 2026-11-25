#!/usr/bin/env python3
"""Mechanical checks for research pages (src/content_research.py). Fails on: missing sources/FAQs, partner or guarantee wording,
unsourced percentages or currency amounts, missing 'illustrative' label next to scenarios. Exit 1 on any finding."""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from content_research import RESEARCH_PAGES  # noqa: E402

BAD = re.compile(r"Solution Partner|Certified Learning Partner|guarantee|best in class|\b\d{1,3}(?:\.\d+)?\s?%|[$₹€]\s?\d", re.I)


def findings():
    out = []
    for p in RESEARCH_PAGES:
        blob = " ".join([p["answer"]] + [str(s[1]) for s in p["sections"]] + [str(f) for f in p["faqs"]])
        for m in BAD.finditer(blob):
            out.append((p["path"], "claim-pattern", m.group(0)))
        if p["schema"] == "Article":
            if not p.get("sources"): out.append((p["path"], "no sources", ""))
            if not p.get("faqs"): out.append((p["path"], "no faqs", ""))
            if "Illustrative" not in blob and "illustrative" not in blob.lower(): out.append((p["path"], "scenario not labelled", ""))
    return out


if __name__ == "__main__":
    f = findings()
    print(f"research pages checked: {len(RESEARCH_PAGES)}; findings: {len(f)}")
    for x in f: print(" ", x)
    sys.exit(1 if f else 0)
