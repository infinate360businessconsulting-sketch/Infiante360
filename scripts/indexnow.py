#!/usr/bin/env python3
"""IndexNow notifier for infiante360techacademy.com (the verified production domain).
The key is a public verification token by design (served at /<key>.txt); it is not a credential.
Selects URLs from the live sitemap.xml whose <lastmod> is within --days (default 2) and POSTs them once to api.indexnow.org.
Default is a dry run. Use --submit to send. Deleted URLs: pass --urls-file with one URL per line (they should return 404/410).
Usage: python3 scripts/indexnow.py [--submit] [--days N] [--base https://infiante360techacademy.com/]"""
import argparse, datetime, glob, json, os, re, sys, urllib.error, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://api.indexnow.org/IndexNow"


def key():
    f = sorted(glob.glob(os.path.join(ROOT, "indexnow", "*.txt")))
    if not f:
        sys.exit("no key file in indexnow/")
    k = os.path.basename(f[0])[:-4]
    if open(f[0]).read().strip() != k:
        sys.exit("key file content must equal its name")
    return k


def recent_urls(base, days):
    xml = urllib.request.urlopen(base + "sitemap.xml", timeout=30).read().decode()
    cutoff = (datetime.date.today() - datetime.timedelta(days=days)).isoformat()
    return [m.group(1) for m in re.finditer(r"<url><loc>([^<]+)</loc>(?:<lastmod>([^<]+)</lastmod>)?", xml) if m.group(2) and m.group(2) >= cutoff]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--submit", action="store_true")
    ap.add_argument("--days", type=int, default=2)
    ap.add_argument("--base", default="https://infiante360techacademy.com/")
    ap.add_argument("--urls-file")
    a = ap.parse_args()
    k = key()
    urls = recent_urls(a.base, a.days)
    if a.urls_file:
        urls += [u.strip() for u in open(a.urls_file) if u.strip()]
    urls = sorted(set(urls))[:10000]
    host = re.sub(r"^https?://|/$", "", a.base)
    body = {"host": host, "key": k, "keyLocation": f"{a.base}{k}.txt", "urlList": urls}
    print(f"{len(urls)} URLs eligible for {host}")
    if not a.submit or not urls:
        print("dry run" if not a.submit else "nothing to submit")
        return 0
    req = urllib.request.Request(ENDPOINT, json.dumps(body).encode(), {"Content-Type": "application/json; charset=utf-8"})
    try:
        print("IndexNow response:", urllib.request.urlopen(req, timeout=30).status)
    except urllib.error.HTTPError as e:
        print("IndexNow response:", e.code, "(200/202 accepted; 403 key not found at keyLocation; 422 URL/host mismatch)")
        return 0 if e.code in (200, 202) else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
