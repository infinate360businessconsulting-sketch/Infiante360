"""Original inline SVG illustrations (no third-party artwork)."""


def _box(x, y, w, h, label, sub="", fill="#13254a", stroke="#2c4475", tc="#ffffff"):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}"/>'
    s += f'<text x="{x + w/2}" y="{y + (h/2 if not sub else h/2 - 6)}" text-anchor="middle" dominant-baseline="middle" fill="{tc}" font-size="15" font-weight="700">{label}</text>'
    if sub:
        s += f'<text x="{x + w/2}" y="{y + h/2 + 13}" text-anchor="middle" dominant-baseline="middle" fill="#9fb0cc" font-size="11.5">{sub}</text>'
    return s


def _arrow(x1, y1, x2, y2, color="#ff4b55"):
    return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="2" fill="none" marker-end="url(#ah)" stroke-dasharray="5 5"><animate attributeName="stroke-dashoffset" from="20" to="0" dur="1.6s" repeatCount="indefinite"/></path>'


def architecture_svg():
    """Data sources -> AEP foundation -> applications -> channels, with an agentic AI layer."""
    parts = ['<svg viewBox="0 0 560 470" role="img" xmlns="http://www.w3.org/2000/svg" font-family="Plus Jakarta Sans, system-ui, sans-serif">',
             '<title>Customer data architecture: sources flow into Adobe Experience Platform, which powers Real-Time CDP, Journey Optimizer and Customer Journey Analytics across channels, with a governed agentic AI layer.</title>',
             '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#ff4b55"/></marker>',
             '<linearGradient id="core" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d7141e"/><stop offset="1" stop-color="#8f0b12"/></linearGradient></defs>',
             '<rect x="0" y="0" width="560" height="470" rx="24" fill="#0e1d3b" stroke="#24375f"/>',
             '<text x="28" y="40" fill="#ff8a91" font-size="11" font-weight="800" letter-spacing="2">SOURCES</text>']
    for i, (a, b) in enumerate([("CRM", "accounts · leads"), ("Web &amp; app", "Web SDK events"), ("Commerce", "orders · products"), ("Warehouse", "data platforms")]):
        parts.append(_box(28 + i * 130, 54, 114, 58, a, b))
    parts.append(_arrow(280, 118, 280, 150))
    parts.append('<rect x="28" y="156" width="504" height="110" rx="16" fill="url(#core)"/>')
    parts.append('<text x="280" y="184" text-anchor="middle" fill="#fff" font-size="17" font-weight="800">Adobe Experience Platform</text>')
    for i, lab in enumerate(["XDM schemas", "Identity graph", "Real-Time Profile", "Consent &amp; policy"]):
        parts.append(f'<rect x="{44 + i*122}" y="204" width="110" height="44" rx="10" fill="rgba(255,255,255,.14)"/><text x="{99 + i*122}" y="227" text-anchor="middle" dominant-baseline="middle" fill="#fff" font-size="12" font-weight="700">{lab}</text>')
    parts.append(_arrow(140, 270, 120, 300))
    parts.append(_arrow(280, 270, 280, 300))
    parts.append(_arrow(420, 270, 440, 300))
    for i, (a, b) in enumerate([("Real-Time CDP", "audiences · activation"), ("Journey Optimizer", "journeys · decisioning"), ("CJA", "cross-channel insight")]):
        parts.append(_box(28 + i * 172, 304, 160, 60, a, b, fill="#13254a", stroke="#ff4b55"))
    parts.append('<rect x="28" y="384" width="504" height="58" rx="14" fill="none" stroke="#5b8cff" stroke-dasharray="6 6"/>')
    parts.append('<text x="280" y="408" text-anchor="middle" fill="#cfe0ff" font-size="14" font-weight="800">Agentic AI layer · MCP tools · human approval</text>')
    parts.append('<text x="280" y="428" text-anchor="middle" fill="#9fb0cc" font-size="11.5">Email · Web · App · Paid media · Service · Sales</text>')
    parts.append('</svg>')
    return "".join(parts)


def journey_svg():
    """Learn -> Build -> Implement -> Deploy loop for the academy."""
    steps = [("Learn", "concepts"), ("Build", "labs"), ("Implement", "projects"), ("Deploy", "career")]
    parts = ['<svg viewBox="0 0 520 300" role="img" xmlns="http://www.w3.org/2000/svg" font-family="Plus Jakarta Sans, system-ui, sans-serif">',
             '<title>Learning path: learn, build, implement, deploy.</title>',
             '<defs><marker id="ah2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#ff4b55"/></marker></defs>']
    for i, (a, b) in enumerate(steps):
        cx = 70 + i * 127
        parts.append(f'<circle cx="{cx}" cy="140" r="52" fill="#13254a" stroke="#ff4b55" stroke-width="2"/>')
        parts.append(f'<text x="{cx}" y="134" text-anchor="middle" fill="#fff" font-size="15" font-weight="800">{a}</text>')
        parts.append(f'<text x="{cx}" y="156" text-anchor="middle" fill="#9fb0cc" font-size="12">{b}</text>')
        if i < 3:
            parts.append(_arrow(cx + 54, 140, cx + 72, 140).replace("url(#ah)", "url(#ah2)"))
    parts.append('<text x="260" y="250" text-anchor="middle" fill="#cfe0ff" font-size="13" font-weight="700">AEP · RTCDP · AJO · CJA · Web SDK · Agentic AI &amp; MCP</text>')
    parts.append('</svg>')
    return "".join(parts)


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;") if "&amp;" not in t else t


def flow_svg(title, stages, accent="#d7141e"):
    """Numbered left-to-right flow (wraps to rows of 3). stages: [(label, sub)]."""
    per_row, bw, bh, gx, gy = 3, 168, 74, 26, 34
    rows = (len(stages) + per_row - 1) // per_row
    W = per_row * bw + (per_row - 1) * gx + 48
    H = rows * bh + (rows - 1) * gy + 78
    import hashlib
    mid = "fl" + hashlib.md5(title.encode()).hexdigest()[:6]
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" font-family="Plus Jakarta Sans, system-ui, sans-serif">',
           f'<title>{_esc(title)}</title>',
           f'<defs><marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{accent}"/></marker></defs>',
           f'<rect width="{W}" height="{H}" rx="20" fill="#0e1d3b"/>',
           f'<text x="24" y="34" fill="#ff8a91" font-size="12" font-weight="800" letter-spacing="1.5">{_esc(title.upper())[:70]}</text>']
    pos = []
    for i, (lab, sub) in enumerate(stages):
        r, c = divmod(i, per_row)
        if r % 2:
            c = per_row - 1 - c  # snake layout keeps arrows short
        x, y = 24 + c * (bw + gx), 52 + r * (bh + gy)
        pos.append((x, y))
        fill = accent if i in (0, len(stages) - 1) else "#13254a"
        out.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="12" fill="{fill}" stroke="#2c4475"/>')
        out.append(f'<circle cx="{x+18}" cy="{y+18}" r="11" fill="#fff"/><text x="{x+18}" y="{y+22}" text-anchor="middle" font-size="11" font-weight="800" fill="#0b1730">{i+1}</text>')
        out.append(f'<text x="{x+bw/2+8}" y="{y+32}" text-anchor="middle" fill="#fff" font-size="13.5" font-weight="700">{_esc(lab)}</text>')
        if sub:
            out.append(f'<text x="{x+bw/2}" y="{y+54}" text-anchor="middle" fill="#c9d4ea" font-size="11">{_esc(sub)}</text>')
    for i in range(len(pos) - 1):
        (x1, y1), (x2, y2) = pos[i], pos[i + 1]
        if y1 == y2:
            a, b = (x1 + bw, x2) if x2 > x1 else (x1, x2 + bw)
            out.append(f'<path d="M{a+2} {y1+bh/2} L{b-4} {y2+bh/2}" stroke="{accent}" stroke-width="2.2" marker-end="url(#{mid})"/>')
        else:
            out.append(f'<path d="M{x1+bw/2} {y1+bh+2} L{x2+bw/2} {y2-4}" stroke="{accent}" stroke-width="2.2" marker-end="url(#{mid})"/>')
    out.append("</svg>")
    return "".join(out)


def layers_svg(title, layers):
    """Stacked architecture layers. layers: [(layer name, [component, ...])]."""
    W, lh, gap = 640, 70, 14
    H = 60 + len(layers) * (lh + gap)
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" xmlns="http://www.w3.org/2000/svg" font-family="Plus Jakarta Sans, system-ui, sans-serif">',
           f'<title>{_esc(title)}</title>', f'<rect width="{W}" height="{H}" rx="20" fill="#f4f6fb" stroke="#e2e6ef"/>',
           f'<text x="24" y="34" fill="#d7141e" font-size="12" font-weight="800" letter-spacing="1.5">{_esc(title.upper())[:80]}</text>']
    for i, (name, comps) in enumerate(layers):
        y = 48 + i * (lh + gap)
        dark = i == len(layers) // 2
        out.append(f'<rect x="20" y="{y}" width="{W-40}" height="{lh}" rx="14" fill="{"#0b1730" if dark else "#fff"}" stroke="{"#0b1730" if dark else "#d5dbe8"}"/>')
        out.append(f'<text x="38" y="{y+lh/2+5}" fill="{"#ff8a91" if dark else "#d7141e"}" font-size="12.5" font-weight="800">{_esc(name)}</text>')
        n = max(len(comps), 1)
        cw = (W - 230) / n
        for j, comp in enumerate(comps):
            cx = 190 + j * cw
            out.append(f'<rect x="{cx}" y="{y+14}" width="{cw-10}" height="{lh-28}" rx="9" fill="{"rgba(255,255,255,.12)" if dark else "#eef1f8"}"/>')
            out.append(f'<text x="{cx+(cw-10)/2}" y="{y+lh/2+4}" text-anchor="middle" fill="{"#fff" if dark else "#0b1730"}" font-size="11.5" font-weight="700">{_esc(comp)}</text>')
    out.append("</svg>")
    return "".join(out)


def figure(svg, caption):
    return f'<figure class="diagram">{svg}<figcaption>{caption}</figcaption></figure>'
