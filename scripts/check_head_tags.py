#!/usr/bin/env python3
"""Fail CI if the configured Google site-verification tags are missing from the built homepage.
Usage: python3 scripts/check_head_tags.py <built_dir>
Reports (does not fail on) other generated pages that lack them. Corporate, LMS and verification-file pages are separate and skipped.
This only checks the tag is served; it does NOT prove Google ownership verification (Search Console confirms that).
"""
import glob, json, os, re, sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
built = sys.argv[1]
raw = json.load(open(os.path.join(root, "content", "settings.json"), encoding="utf-8")).get("google_site_verification", [])
tokens = [t for t in (raw if isinstance(raw, list) else [raw]) if t]
if not tokens:
    sys.exit("no google_site_verification configured")
SKIP = ("corporate/", "lms-hub/", "zohoverify/")
missing, checked = [], 0
for f in glob.glob(os.path.join(built, "**", "*.html"), recursive=True):
    rel = os.path.relpath(f, built).replace(os.sep, "/")
    if rel.startswith(SKIP) or "verifyfor" in rel:
        continue
    txt = open(f, encoding="utf-8", errors="ignore").read()
    checked += 1
    if not all(re.search(r'<meta name="google-site-verification" content="%s"' % re.escape(t), txt) for t in tokens):
        missing.append(rel)
home = os.path.join(built, "index.html")
ok_home = "index.html" not in missing
print(f"verification tokens configured: {len(tokens)}; pages checked: {checked}; pages missing a tag: {len(missing)}; homepage ok: {ok_home}")
for m in missing[:20]:
    print("  missing:", m)
sys.exit(0 if ok_home else 1)
