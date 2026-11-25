"""Top-of-page banner slider, chosen per page from its content. Data: content/banners.json. Only approved banners with an existing image are rendered."""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load():
    try:
        data = json.load(open(os.path.join(ROOT, "content", "banners.json"), encoding="utf-8"))["banners"]
    except (OSError, ValueError, KeyError):
        return []
    return [b for b in data if b.get("approved") is True and b.get("image") and b.get("alt")
            and os.path.exists(os.path.join(ROOT, "assets", "banners", b["image"]))]


NO_SLIDER = ("lp/", "corporate/", "404", "privacy", "terms", "cookie", "thank", "admin/", "zohoverify")


def select(page, limit=5, minimum=3):
    """Banners whose topics appear in the page path/title/category/keywords, best match first; the banner that links to
    the page itself is skipped; fallback banners fill up to `minimum`."""
    items = load()
    path = page.get("path", "")
    blob = " ".join([path, page.get("title", ""), page.get("category", ""), " ".join(page.get("keywords", []))]).lower()
    scored = []
    for n, b in enumerate(items):
        if b.get("link") == path:
            continue
        score = sum(1 for t in b.get("topics", []) if t in blob)
        scored.append((-score, n, b))
    scored.sort(key=lambda x: (x[0], x[1]))
    chosen = [b for sc, n, b in scored if sc < 0][:limit]
    for sc, n, b in scored:
        if len(chosen) >= minimum:
            break
        if b not in chosen and b.get("fallback"):
            chosen.append(b)
    return chosen


def top_slider(page):
    """Slider placed first inside <main>; empty for landing/utility pages or when no banner is approved."""
    path = page.get("path", "")
    if page.get("no_slider") or path.startswith(NO_SLIDER):
        return ""
    items = select(page)
    if not items:
        return ""
    prefix = "../" * path.count("/")
    return f'<div class="top-slider"><div class="wrap">{slider_html(prefix, items)}</div></div>'


def slider_html(prefix="", items=None):
    items = load() if items is None else items
    if not items:
        return ""
    e = html.escape
    slides = []
    for i, b in enumerate(items):
        img = (f'<img src="{prefix}assets/banners/{e(b["image"])}" alt="{e(b["alt"])}" loading="{"eager" if i == 0 else "lazy"}"{" fetchpriority=high" if i == 0 else ""} decoding="async"'
               f'{" width=%d height=%d" % (b["width"], b["height"]) if b.get("width") and b.get("height") else ""}>')
        link = b.get("link")
        inner = f'<a href="{e(prefix + link)}">{img}</a>' if link else img
        slides.append(f'<li class="slide" role="group" aria-roledescription="slide" aria-label="{i+1} of {len(items)}"{"" if i == 0 else " hidden"}>{inner}</li>')
    dots = "".join(f'<button type="button" class="dot" aria-label="Show banner {i+1}"{" aria-current=true" if i == 0 else ""}></button>' for i in range(len(items)))
    ctl = ('<button type="button" class="prev" aria-label="Previous banner">&#8249;</button><button type="button" class="next" aria-label="Next banner">&#8250;</button>'
           f'<div class="dots">{dots}</div><button type="button" class="pause" aria-label="Pause banner rotation" aria-pressed="false">&#10074;&#10074;</button>') if len(items) > 1 else ""
    return f'<div class="banner-slider" data-slider aria-roledescription="carousel" aria-label="Featured programmes"><ul class="slides">{"".join(slides)}</ul>{ctl}</div>'
