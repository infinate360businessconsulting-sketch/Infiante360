"""Homepage banner slider. Data: content/banners.json. Only approved banners with an existing image are rendered."""
import html, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load():
    try:
        data = json.load(open(os.path.join(ROOT, "content", "banners.json"), encoding="utf-8"))["banners"]
    except (OSError, ValueError, KeyError):
        return []
    return [b for b in data if b.get("approved") is True and b.get("image") and b.get("alt")
            and os.path.exists(os.path.join(ROOT, "assets", "banners", b["image"]))]


def slider_html():
    items = load()
    if not items:
        return ""
    e = html.escape
    slides = []
    for i, b in enumerate(items):
        img = (f'<img src="assets/banners/{e(b["image"])}" alt="{e(b["alt"])}" loading="{"eager" if i == 0 else "lazy"}" decoding="async"'
               f'{" width=%d height=%d" % (b["width"], b["height"]) if b.get("width") and b.get("height") else ""}>')
        link = b.get("link")
        inner = f'<a href="{e(link)}">{img}</a>' if link else img
        slides.append(f'<li class="slide" role="group" aria-roledescription="slide" aria-label="{i+1} of {len(items)}"{"" if i == 0 else " hidden"}>{inner}</li>')
    dots = "".join(f'<button type="button" class="dot" aria-label="Show banner {i+1}"{" aria-current=true" if i == 0 else ""}></button>' for i in range(len(items)))
    ctl = ('<button type="button" class="prev" aria-label="Previous banner">&#8249;</button><button type="button" class="next" aria-label="Next banner">&#8250;</button>'
           f'<div class="dots">{dots}</div>') if len(items) > 1 else ""
    return f'<div class="banner-slider" data-slider aria-roledescription="carousel" aria-label="Featured programmes"><ul class="slides">{"".join(slides)}</ul>{ctl}</div>'
