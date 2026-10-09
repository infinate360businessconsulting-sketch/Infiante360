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
