#!/usr/bin/env python3
"""Ingest the Growth Execution workbook into normalized JSON/CSV datasets under data/seo/.

Usage: python3 scripts/seo_ingest.py <workbook.xlsx>
Re-runnable and idempotent. Source rows are never dropped: every record keeps its original ID and row number.
No metrics are invented: values the workbook does not contain are stored as null.
"""
import csv, json, os, re, shutil, sys, collections
import openpyxl

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "seo")

SHEETS = {  # sheet -> (dataset file, expected count, id column)
    "Keywords": ("keywords", 1000, "ID"),
    "Commercial 100": ("commercial_100", 100, "ID"),
    "Long tail 100": ("longtail_100", 100, "ID"),
    "Pillars": ("pillars", 50, "ID"),
    "Articles": ("articles", 365, "ID"),
    "AI discovery": ("ai_discovery", 100, "ID"),
    "Landing pages": ("landing_pages", 30, "ID"),
    "90 day execution": ("roadmap_90", 90, "Day"),
    "90 day social": ("social_90", 90, "Day"),
    "Authority 50": ("authority_50", 50, "ID"),
    "Measurement": ("measurement", 8, "Metric"),
    "Audit evidence": ("audit_evidence", 10, "Area"),
}


def snake(h):
    return re.sub(r"[^a-z0-9]+", "_", str(h).strip().lower()).strip("_")


def norm_kw(s):
    return re.sub(r"\s+", " ", str(s).strip().lower())


def read_sheet(ws):
    rows = list(ws.iter_rows(values_only=True))
    head = [snake(h) for h in rows[0]]
    out = []
    for i, r in enumerate(rows[1:], start=2):
        if not any(c is not None and str(c).strip() for c in r):
            continue
        rec = {h: (None if c is None or str(c).strip() == "" else (c if isinstance(c, (int, float)) else str(c).strip())) for h, c in zip(head, r)}
        rec["_source_row"] = i
        out.append(rec)
    return head, out


def main(path):
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(os.path.join(OUT, "source"), exist_ok=True)
    src_name = os.path.basename(path)
    # keep a copy of the source so the import is reproducible
    shutil.copyfile(path, os.path.join(OUT, "source", re.sub(r"^[0-9a-f]{8}-", "", src_name)))
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    report = {"source_file": re.sub(r"^[0-9a-f]{8}-", "", src_name), "datasets": {}, "problems": []}
    data = {}
    for sheet, (name, expected, idcol) in SHEETS.items():
        if sheet not in wb.sheetnames:
            report["problems"].append(f"missing sheet: {sheet}")
            continue
        head, recs = read_sheet(wb[sheet])
        idc = snake(idcol)
        ids = [str(r.get(idc)) for r in recs]
        dup_ids = [k for k, v in collections.Counter(ids).items() if v > 1]
        missing = collections.Counter()
        for r in recs:
            for h in head:
                if r.get(h) is None:
                    missing[h] += 1
        for r in recs:
            r["source_sheet"] = sheet
            r["source_file"] = report["source_file"]
        data[name] = recs
        report["datasets"][name] = {
            "sheet": sheet, "expected": expected, "imported": len(recs), "match": len(recs) == expected,
            "duplicate_ids": dup_ids, "missing_values_by_column": dict(missing),
        }
        with open(os.path.join(OUT, f"{name}.json"), "w", encoding="utf-8") as f:
            json.dump(recs, f, ensure_ascii=False, indent=1)
        cols = head + ["_source_row", "source_sheet", "source_file"]
        with open(os.path.join(OUT, f"{name}.csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows({c: r.get(c) for c in cols} for r in recs)

    kws = data["keywords"]
    # duplicate keyword text (not just id)
    norm_counts = collections.Counter(norm_kw(k["keyword"]) for k in kws if k.get("keyword"))
    report["keyword_text_duplicates"] = sorted(k for k, v in norm_counts.items() if v > 1)
    report["keyword_invalid"] = [k["id"] for k in kws if not k.get("keyword") or not k.get("id")]
    report["clusters"] = dict(collections.Counter(k["cluster"] for k in kws))
    report["intent_split"] = dict(collections.Counter(k["intent"] for k in kws))
    report["priority_split"] = dict(collections.Counter(k["priority"] for k in kws))
    ids = {k["id"] for k in kws}
    for sub in ("commercial_100", "longtail_100"):
        missing = [r["id"] for r in data[sub] if r["id"] not in ids]
        report["datasets"][sub]["not_in_master_keywords"] = missing
    ok = all(d["match"] and not d["duplicate_ids"] for d in report["datasets"].values()) and not report["keyword_text_duplicates"] and not report["keyword_invalid"]
    report["all_counts_reconciled"] = bool(ok)
    with open(os.path.join(OUT, "reconciliation.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1)
    print(json.dumps({k: (v["imported"], v["expected"]) for k, v in report["datasets"].items()}))
    print("reconciled:", ok, "problems:", report["problems"])
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
