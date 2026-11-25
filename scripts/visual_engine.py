#!/usr/bin/env python3
"""Deterministic visual engine: specs -> SVG diagrams (light, editorial) and dark hero/OG bases.

No generative model is used (none is available in this environment; see data/seo/image_provider_probe.json).
Every label comes from the spec, so technical text is exact. The same spec always renders the same image.

Spec (data/visuals/specs/<slug>.json):
  id, slug, page, title, subtitle, keyword, kind: flow | layers | phases, accent: red|cyan|orange|violet,
  lanes|layers|phases: structure for the kind, band: bottom text, note: honesty line, alt, caption
Usage: python3 scripts/visual_engine.py build [slug ...]   (writes SVG + base PNG; branding/optimising are separate steps)
"""
import base64, html, io, json, os, subprocess, sys, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPECS = os.path.join(ROOT, "data", "visuals", "specs")
OUT = os.path.join(ROOT, "assets", "visuals")
LOGO = os.path.join(ROOT, "assets", "logo-mark.png")  # approved logo asset already in the repo
FONT = "Inter, 'Segoe UI', Arial, sans-serif"
ACC = {"red": ("#E5322D", "#FF7A45"), "cyan": ("#0891B2", "#22D3EE"), "orange": ("#EA580C", "#FDBA74"), "violet": ("#6D28D9", "#A78BFA")}
esc = html.escape


def wrap(text, width_px, fs):
    n = max(8, int(width_px / (fs * 0.56)))
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + (1 if cur else 0) <= n:
            cur = (cur + " " + w).strip()
        else:
            lines.append(cur); cur = w
    return lines + ([cur] if cur else [])


def text_block(x, y, lines, fs, fill, weight=400, anchor="start", lh=1.3):
    out = []
    for i, l in enumerate(lines):
        out.append(f'<text x="{x}" y="{round(y + i * fs * lh, 1)}" font-size="{fs}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="{FONT}">{esc(l)}</text>')
    return "".join(out)


def theme(name, accent):
    a1, a2 = ACC[accent]
    if name == "dark":
        return dict(bg="#0A1128", box="#14213F", stroke="#2F4272", text="#E8EEF9", muted="#9FB0D3", head=a1, head2=a2, headtext="#FFFFFF", arrow=a2, band="#101B38", bandtext="#CFE0FF")
    return dict(bg="#F8FAFC", box="#FFFFFF", stroke="#CBD5E1", text="#0F172A", muted="#475569", head="#0B1B3A", head2=a1, headtext="#FFFFFF", arrow=a1, band="#EAF1FB", bandtext="#0F172A")


def arrow(x, y, c):
    return f'<path d="M{x-7},{y-9} L{x+7},{y} L{x-7},{y+9} Z" fill="{c}"/>'


def draw(spec, th, W):
    """Return (svg_fragment, height) for the spec drawn at width W with theme th."""
    kind, pad, parts, y = spec["kind"], 28, [], 28
    if kind == "flow":
        lanes = spec["lanes"]; n = len(lanes); gap = 34
        cw = (W - 2 * pad - (n - 1) * gap) / n
        fs = 14 if cw > 150 else 12
        maxi = max(len(l["items"]) for l in lanes)
        bh = 66 if fs == 14 else 60
        for i, lane in enumerate(lanes):
            x = pad + i * (cw + gap)
            parts.append(f'<rect x="{round(x,1)}" y="{y}" width="{round(cw,1)}" height="40" rx="8" fill="{th["head"]}"/>')
            parts.append(text_block(round(x + cw / 2, 1), y + 25, [lane["title"]], fs, th["headtext"], 700, "middle"))
            for j, it in enumerate(lane["items"]):
                by = y + 52 + j * (bh + 10)
                parts.append(f'<rect x="{round(x,1)}" y="{by}" width="{round(cw,1)}" height="{bh}" rx="8" fill="{th["box"]}" stroke="{th["stroke"]}"/>')
                ls = wrap(it, cw - 16, fs - 1)[:3]
                parts.append(text_block(round(x + cw / 2, 1), by + bh / 2 - (len(ls) - 1) * (fs - 1) * 0.65 + 4, ls, fs - 1, th["text"], 500, "middle"))
            if i < n - 1:
                parts.append(arrow(round(x + cw + gap / 2, 1), y + 20, th["arrow"]))
        y += 52 + maxi * (bh + 10) + 6
    elif kind == "layers":
        layers = spec["layers"]; lw = 200; fs = 14
        for k, lay in enumerate(layers):
            items = lay["items"]; avail = W - 2 * pad - lw - 16
            per = min(len(items), 4); iw = (avail - (per - 1) * 10) / per
            rows = (len(items) + per - 1) // per; rh = 54
            h = max(rows * (rh + 8) - 8, 54)
            parts.append(f'<rect x="{pad}" y="{y}" width="{lw}" height="{h}" rx="8" fill="{th["head"]}"/>')
            tl = wrap(lay["title"], lw - 20, fs)
            parts.append(text_block(pad + lw / 2, y + h / 2 - (len(tl) - 1) * fs * 0.65 + 5, tl, fs, th["headtext"], 700, "middle"))
            for j, it in enumerate(items):
                ix = pad + lw + 16 + (j % per) * (iw + 10); iy = y + (j // per) * (rh + 8)
                parts.append(f'<rect x="{round(ix,1)}" y="{iy}" width="{round(iw,1)}" height="{rh}" rx="8" fill="{th["box"]}" stroke="{th["stroke"]}"/>')
                ls = wrap(it, iw - 14, fs - 1)[:3]
                parts.append(text_block(round(ix + iw / 2, 1), iy + rh / 2 - (len(ls) - 1) * (fs - 1) * 0.65 + 4, ls, fs - 1, th["text"], 500, "middle"))
            y += h
            if k < len(layers) - 1:
                parts.append(f'<path d="M{pad+lw/2-9},{y+3} L{pad+lw/2+9},{y+3} L{pad+lw/2},{y+17} Z" fill="{th["arrow"]}"/>'); y += 22
    else:  # phases
        ph = spec["phases"]; n = len(ph); gap = 10; cw = (W - 2 * pad - (n - 1) * gap) / n; fs = 14
        for i, p in enumerate(ph):
            x = pad + i * (cw + gap)
            parts.append(f'<path d="M{round(x,1)},{y} L{round(x+cw-18,1)},{y} L{round(x+cw,1)},{y+25} L{round(x+cw-18,1)},{y+50} L{round(x,1)},{y+50} L{round(x+14,1)},{y+25} Z" fill="{th["head"] if i % 2 == 0 else th["head2"]}"/>')
            parts.append(text_block(round(x + cw / 2 + 4, 1), y + 30, [p["title"]], fs, th["headtext"], 700, "middle"))
            yy = y + 72
            for b in p["items"]:
                ls = wrap("• " + b, cw - 10, fs - 2)
                parts.append(text_block(round(x + 4, 1), yy, ls, fs - 2, th["text"], 400)); yy += len(ls) * (fs - 2) * 1.3 + 6
        y += 72 + max(sum(len(wrap("• " + b, cw - 10, fs - 2)) * (fs - 2) * 1.3 + 6 for b in p["items"]) for p in ph)
    if spec.get("band"):
        bl = wrap(spec["band"], W - 2 * pad - 24, 14)
        bh = 18 + len(bl) * 19
        parts.append(f'<rect x="{pad}" y="{y+8}" width="{W-2*pad}" height="{bh}" rx="8" fill="{th["band"]}" stroke="{th["stroke"]}"/>')
        parts.append(text_block(W / 2, y + 8 + 25, bl, 14, th["bandtext"], 600, "middle")); y += bh + 8
    if spec.get("note"):
        parts.append(text_block(pad, y + 28, wrap(spec["note"], W - 2 * pad, 12), 12, th["muted"], 400)); y += 14 + 19 * len(wrap(spec["note"], W - 2 * pad, 12))
    return "".join(parts), y + 40


def logo_b64(px):
    from PIL import Image
    im = Image.open(LOGO).convert("RGB").resize((px, px), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, "PNG", optimize=True)
    return base64.b64encode(b.getvalue()).decode()


def logo_svg(x, y, px):
    cid = f"lg{px}"
    return (f'<defs><clipPath id="{cid}"><rect x="{x}" y="{y}" width="{px}" height="{px}" rx="{px//5}"/></clipPath></defs>'
            f'<image x="{x}" y="{y}" width="{px}" height="{px}" clip-path="url(#{cid})" opacity="0.95" href="data:image/png;base64,{logo_b64(px*2)}"/>')


def diagram_svg(spec, logo=True):
    W = 1200; th = theme("light", spec["accent"])
    body, H = draw(spec, th, W)
    tag = esc(spec.get("alt", spec["title"]))
    lg = logo_svg(W - 28 - 40, H - 40 - 6, 40) if logo else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">'
            f'<title id="t">{esc(spec["title"])}</title><desc id="d">{tag}</desc><rect width="{W}" height="{H}" fill="{th["bg"]}"/>{body}{lg}</svg>')


def hero_svg(spec, W, H):
    """Dark editorial cover: headline on top, the real diagram scaled below. No logo (applied afterwards by brand_overlay)."""
    th = theme("dark", spec["accent"]); a1, a2 = ACC[spec["accent"]]
    seed = int(hashlib.sha256(spec["slug"].encode()).hexdigest()[:8], 16)
    inner_w = 1200
    body, ih = draw({**spec, "note": None}, th, inner_w)
    top = int(H * 0.30); avail_h = H - top - 24; avail_w = W - 60
    sc = min(avail_w / inner_w, avail_h / ih)
    tx = (W - inner_w * sc) / 2
    fs = 54 if W >= 1500 else 42
    tl = wrap(spec["title"], W - 120, fs)[:2]
    glow = "".join(f'<circle cx="{(seed >> (i*3)) % W}" cy="{(seed >> (i*2+1)) % max(top, 1)}" r="{60 + (seed >> i) % 90}" fill="url(#gl)" opacity="0.35"/>' for i in range(4))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#070C1E"/><stop offset="1" stop-color="#121D42"/></linearGradient>'
            f'<radialGradient id="gl"><stop offset="0" stop-color="{a1}"/><stop offset="1" stop-color="{a1}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="{W}" height="{H}" fill="url(#bg)"/>{glow}<rect x="0" y="0" width="10" height="{H}" fill="{a1}"/>'
            + text_block(48, 54, [spec.get("kicker", "Infiante360 reference architecture").upper()], 16, a2, 700)
            + text_block(48, 54 + fs + 10, tl, fs, "#FFFFFF", 800, lh=1.15)
            + text_block(48, 54 + fs + 14 + len(tl) * fs * 1.15, wrap(spec["subtitle"], W - 120, 20)[:2], 20, "#B8C7E8", 400)
            + f'<g transform="translate({round(tx,1)},{top}) scale({round(sc,4)})">{body}</g></svg>')


def render_png(svg_path, png_path, width):
    subprocess.run(["rsvg-convert", "-w", str(width), "-o", png_path, svg_path], check=True)


def build(slugs=None):
    os.makedirs(OUT, exist_ok=True)
    done = []
    for f in sorted(os.listdir(SPECS)):
        spec = json.load(open(os.path.join(SPECS, f), encoding="utf-8"))
        if slugs and spec["slug"] not in slugs: continue
        d = os.path.join(OUT, spec["slug"]); os.makedirs(os.path.join(d, "base"), exist_ok=True)
        open(os.path.join(d, "diagram.svg"), "w", encoding="utf-8").write(diagram_svg(spec))
        for name, (w, h) in {"hero": (1600, 900), "og": (1200, 630)}.items():
            sp = os.path.join(d, "base", f"{name}.svg")
            open(sp, "w", encoding="utf-8").write(hero_svg(spec, w, h)); render_png(sp, os.path.join(d, "base", f"{name}.png"), w)
            os.unlink(sp)
        done.append(spec["slug"])
    print("built:", ", ".join(done) or "(none)")
    return done


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        build(sys.argv[2:] or None)
    else:
        print(__doc__)
