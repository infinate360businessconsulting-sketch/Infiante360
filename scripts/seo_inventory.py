#!/usr/bin/env python3
"""Inventory and health-check a built static site.  Usage: python3 scripts/seo_inventory.py <built_dir> <out_dir> [base_url]

Reads only the built HTML (no network). Produces:
  route-inventory.json  one record per HTML route (title, description, h1, canonical, robots, JSON-LD types, links)
  seo-health.json       machine-readable findings (broken links, orphans, duplicates, sitemap/robots checks)
  seo-health.md         short human summary
Every check is computed from files; nothing is estimated.
"""
import json, os, re, sys, collections
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""; self.in_title = False
        self.h1 = []; self.in_h1 = False
        self.meta = {}; self.canon = None; self.links = []; self.jsonld = []; self.in_ld = False
        self.words = 0; self.skip = 0; self.forms = 0; self.imgs_no_alt = 0
        self.svg = 0; self.title_done = False

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag == "svg": self.svg += 1
        if tag == "title" and not self.svg and not self.title_done: self.in_title = True
        elif tag == "h1": self.in_h1 = True; self.h1.append("")
        elif tag == "meta" and a.get("name"): self.meta[a["name"].lower()] = a.get("content", "")
        elif tag == "meta" and a.get("property"): self.meta[a["property"].lower()] = a.get("content", "")
        elif tag == "link" and a.get("rel") == "canonical": self.canon = a.get("href")
        elif tag == "a" and a.get("href"): self.links.append(a["href"])
        elif tag == "script" and a.get("type") == "application/ld+json": self.in_ld = True; self.jsonld.append("")
        elif tag in ("script", "style"): self.skip += 1
        elif tag == "form": self.forms += 1
        elif tag == "img" and a.get("alt") is None: self.imgs_no_alt += 1

    def handle_endtag(self, tag):
        if tag == "svg" and self.svg: self.svg -= 1
        if tag == "title" and self.in_title: self.in_title = False; self.title_done = True
        elif tag == "h1": self.in_h1 = False
        elif tag == "script":
            if self.in_ld: self.in_ld = False
            elif self.skip: self.skip -= 1
        elif tag == "style" and self.skip: self.skip -= 1

    def handle_data(self, d):
        if self.in_title: self.title += d
        if self.in_h1 and self.h1: self.h1[-1] += d
        if self.in_ld and self.jsonld: self.jsonld[-1] += d
        elif not self.skip: self.words += len(d.split())


def route_of(rel):
    r = "/" + rel.replace(os.sep, "/")
    if r.endswith("/index.html"): r = r[: -len("index.html")]
    return r


def main(built, out, base=None):
    os.makedirs(out, exist_ok=True)
    pages = {}
    for dp, _, fs in os.walk(built):
        for f in fs:
            if not f.endswith(".html"): continue
            full = os.path.join(dp, f); rel = os.path.relpath(full, built)
            p = P(); txt = open(full, encoding="utf-8", errors="ignore").read(); p.feed(txt)
            types, bad_ld = [], 0
            for blk in p.jsonld:
                try:
                    j = json.loads(blk)
                    for n in (j if isinstance(j, list) else j.get("@graph", [j])):
                        t = n.get("@type"); types += t if isinstance(t, list) else [t]
                except Exception: bad_ld += 1
            robots = p.meta.get("robots", "")
            pages["/" + rel.replace(os.sep, "/")] = {
                "file": rel.replace(os.sep, "/"), "route": route_of(rel), "title": p.title.strip(), "title_len": len(p.title.strip()),
                "description": p.meta.get("description", ""), "desc_len": len(p.meta.get("description", "")),
                "h1": [h.strip() for h in p.h1], "canonical": p.canon, "robots": robots, "noindex": "noindex" in robots.lower(),
                "jsonld_types": sorted({t for t in types if t}), "jsonld_invalid_blocks": bad_ld, "words": p.words,
                "forms": p.forms, "imgs_without_alt": p.imgs_no_alt, "links": p.links,
                "lang": bool(re.search(r"<html[^>]*\blang=", txt[:400])), "og_title": "og:title" in p.meta, "viewport": "viewport" in p.meta,
            }
    files = set(pages)
    def resolve(src, href):
        h = href.split("#")[0].split("?")[0]
        if not h or h.startswith(("mailto:", "tel:", "javascript:", "https://wa.me", "whatsapp:")): return None
        u = urlparse(href)
        if u.scheme in ("http", "https"):
            if base and u.netloc == urlparse(base).netloc: t = u.path or "/"
            else: return None
        else: t = urljoin(src, h)
        if t.endswith("/"): t += "index.html"
        if t == "": t = "/index.html"
        return t
    inbound = collections.defaultdict(set); broken = []
    for src, pg in pages.items():
        internal = []
        for href in pg["links"]:
            t = resolve(src, href)
            if t is None: continue
            internal.append(t)
            if t.endswith(".html") or t.endswith("/") or "." not in os.path.basename(t):
                if t in files: inbound[t].add(src)
                elif t + "/index.html" in files: inbound[t + "/index.html"].add(src)
                elif not os.path.exists(os.path.join(built, t.lstrip("/"))): broken.append({"from": src, "href": href, "resolved": t})
        pg["internal_links_out"] = len(set(internal))
    for src, pg in pages.items():
        pg["inbound_links"] = len(inbound.get(src, set()) - {src})
        del pg["links"]
    def dups(key):
        c = collections.defaultdict(list)
        for s, p in pages.items():
            if p.get("noindex"): continue
            v = p[key] if not isinstance(p[key], list) else (p[key][0] if p[key] else "")
            if v: c[v.strip().lower()].append(s)
        return {k: v for k, v in c.items() if len(v) > 1}
    # robots + sitemap
    robots_txt = open(os.path.join(built, "robots.txt"), encoding="utf-8").read() if os.path.exists(os.path.join(built, "robots.txt")) else None
    sm_urls, sm_files = [], []
    smp = os.path.join(built, "sitemap.xml")
    if os.path.exists(smp):
        x = open(smp, encoding="utf-8").read()
        sm_urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", x)
    csm = os.path.join(built, "corporate", "sitemap.xml")  # corporate section ships its own sitemap, referenced from robots.txt
    if os.path.exists(csm):
        sm_urls += re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", open(csm, encoding="utf-8").read())
    def sm_route(u):
        p = urlparse(u).path or "/"
        return p if not p.endswith("/") else p + "index.html"
    sm_set = {sm_route(u) for u in sm_urls}
    UTILITY = ("verifyfor", "zohoverify")  # third-party site-verification files: must stay byte-exact, not content pages
    utility = sorted(s for s in pages if any(u in s for u in UTILITY))
    indexable = [s for s, p in pages.items() if not p["noindex"] and s not in ("/404.html",) and s not in utility]
    health = {
        "pages_total": len(pages), "utility_pages_excluded": utility, "pages_indexable": len(indexable), "pages_noindex": sum(1 for p in pages.values() if p["noindex"]),
        "broken_internal_links": broken[:500], "broken_internal_links_count": len(broken),
        "orphans_indexable": sorted(s for s in indexable if not pages[s]["inbound_links"] and s != "/index.html"),
        "duplicate_titles": dups("title"), "duplicate_descriptions": dups("description"), "duplicate_h1": dups("h1"),
        "title_over_65": sorted(s for s, p in pages.items() if p["title_len"] > 65), "desc_over_160": sorted(s for s, p in pages.items() if p["desc_len"] > 160),
        "missing_title": sorted(s for s, p in pages.items() if not p["title"]), "missing_description": sorted(s for s, p in pages.items() if not p["description"] and not p["noindex"] and s not in utility),
        "missing_h1": sorted(s for s, p in pages.items() if not p["h1"] and not p["noindex"] and s not in utility), "multiple_h1": sorted(s for s, p in pages.items() if len(p["h1"]) > 1),
        "missing_canonical": sorted(s for s in indexable if not pages[s]["canonical"]),
        "invalid_jsonld_pages": sorted(s for s, p in pages.items() if p["jsonld_invalid_blocks"]),
        "pages_without_jsonld": sorted(s for s in indexable if not pages[s]["jsonld_types"]),
        "missing_viewport": sorted(s for s, p in pages.items() if not p["viewport"]),
        "imgs_without_alt_total": sum(p["imgs_without_alt"] for p in pages.values()),
        "thin_pages_under_250_words": sorted(s for s in indexable if pages[s]["words"] < 250),
        "robots_txt_present": robots_txt is not None, "robots_txt": robots_txt,
        "sitemap_present": os.path.exists(smp), "sitemap_url_count": len(sm_urls),
        "sitemap_urls_without_file": sorted(u for u in sm_urls if sm_route(u) not in files and not os.path.exists(os.path.join(built, urlparse(u).path.lstrip("/")))),
        "indexable_pages_missing_from_sitemap": sorted(s for s in indexable if s not in sm_set and s.replace("/index.html", "/") not in {urlparse(u).path for u in sm_urls}),
        "noindex_pages_in_sitemap": sorted(s for s in sm_set if s in pages and pages[s]["noindex"]),
        "sitemap_hosts": sorted({urlparse(u).netloc for u in sm_urls}), "canonical_hosts": sorted({urlparse(p["canonical"]).netloc for p in pages.values() if p["canonical"]}),
    }
    json.dump(sorted(pages.values(), key=lambda r: r["route"]), open(os.path.join(out, "route-inventory.json"), "w"), indent=1)
    json.dump(health, open(os.path.join(out, "seo-health.json"), "w"), indent=1)
    cnt = lambda k: len(health[k]) if isinstance(health[k], (list, dict)) else health[k]
    lines = ["# SEO health (computed from built files)", ""]
    for k in ["pages_total", "pages_indexable", "pages_noindex", "broken_internal_links_count", "orphans_indexable", "duplicate_titles", "duplicate_descriptions", "duplicate_h1",
              "title_over_65", "desc_over_160", "missing_description", "missing_h1", "multiple_h1", "missing_canonical", "invalid_jsonld_pages", "pages_without_jsonld",
              "thin_pages_under_250_words", "imgs_without_alt_total", "robots_txt_present", "sitemap_present", "sitemap_url_count", "sitemap_urls_without_file",
              "indexable_pages_missing_from_sitemap", "noindex_pages_in_sitemap"]:
        lines.append(f"- {k}: {cnt(k)}")
    lines.append(f"- sitemap_hosts: {health['sitemap_hosts']}"); lines.append(f"- canonical_hosts: {health['canonical_hosts']}")
    open(os.path.join(out, "seo-health.md"), "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
