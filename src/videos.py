"""Video sitemap + VideoObject JSON-LD from an approved registry (content/videos.json). Empty registry => no file is written.

A video is eligible only when it is approved, has a public page with a transcript, a real thumbnail, a real file URL, a real duration (seconds) and a real publish date.
The two 10-second silent promo clips are NOT registered: they are decorative, have no spoken content or transcript, and show garbled on-screen text."""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REQUIRED = ("page", "title", "description", "thumbnail", "content_url", "duration", "published")


def load(path=None):
    with open(path or os.path.join(ROOT, "content", "videos.json"), encoding="utf-8") as f:
        return json.load(f)


def eligible(v):
    return bool(v.get("approved") and v.get("has_transcript") and all(v.get(k) for k in REQUIRED) and isinstance(v["duration"], int) and 0 < v["duration"] <= 28800)


def video_sitemap(base, videos=None):
    vids = [v for v in (load() if videos is None else videos) if eligible(v)]
    if not vids:
        return None
    e = html.escape
    rows = []
    for v in vids:
        tags = "".join(f"<video:tag>{e(t)}</video:tag>" for t in v.get("tags", [])[:32])
        rows.append(f"  <url><loc>{e(base + v['page'])}</loc><video:video><video:thumbnail_loc>{e(v['thumbnail'])}</video:thumbnail_loc><video:title>{e(v['title'][:100])}</video:title>"
                    f"<video:description>{e(v['description'][:2048])}</video:description><video:content_loc>{e(v['content_url'])}</video:content_loc><video:duration>{v['duration']}</video:duration>"
                    f"<video:publication_date>{e(v['published'])}</video:publication_date><video:family_friendly>yes</video:family_friendly>{tags}</video:video></url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def video_jsonld(v, base):
    return {"@context": "https://schema.org", "@type": "VideoObject", "name": v["title"], "description": v["description"], "thumbnailUrl": [v["thumbnail"]],
            "uploadDate": v["published"], "duration": f"PT{v['duration'] // 60}M{v['duration'] % 60}S", "contentUrl": v["content_url"], "url": base + v["page"]}
