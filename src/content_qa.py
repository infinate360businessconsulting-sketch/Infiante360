"""Sourced Q&A hub: topic pages, index, sources page. Data in qa_data1/qa_data2, citations in qa_sources."""
import html as _h, re as _re, os as _o
from qa_data1 import TOPICS1
from qa_data2 import TOPICS2
from qa_sources import S
e = _h.escape
WA = "https://wa.me/918296893895"
LI = "https://www.linkedin.com/in/pavanbabu1"
TOPICS = TOPICS1 + TOPICS2
_ROOT = _o.path.dirname(_o.path.dirname(_o.path.abspath(__file__)))
KEYWORDS = [l.strip() for l in open(_o.path.join(_ROOT, "content", "search-keywords.txt"), encoding="utf-8") if l.strip()]
DATE = "2026-10-19"
DISCLOSE = "Answers are AI-assisted summaries of Adobe's public documentation and the instructors' practice, written for learning. Product behaviour changes, so confirm details in the linked official page before relying on them."

def cites(ids):
    return " ".join(f'<a href="{S[i][1]}" rel="noopener" target="_blank">{e(S[i][0])}</a>' for i in ids)

def cta(rel):
    return (f'<p>Need help applying this? <a class="btn btn-primary" href="{rel}contact-us.html">Ask us via the form</a> '
            f'<a class="btn btn-ghost" href="{WA}">WhatsApp +91 82968 93895</a> '
            f'<a class="btn btn-ghost" href="{LI}" rel="noopener" target="_blank">LinkedIn: Pavan Babu Gandla</a></p>')

def topic_page(t):
    secs = []
    used = []
    for n, (q, a, ids) in enumerate(t["items"]):
        for i in ids:
            if i not in used: used.append(i)
        src = f'<p class="small muted">Sources: {cites(ids)}</p>' if ids else '<p class="small muted">Source: Infinite360 Tech Academy programme information.</p>'
        secs.append((q, f"<p>{e(a)}</p>{src}", "alt" if n % 2 else "plain", f"Q{n+1}"))
    secs.append(("Ask a question or join a demo", cta("../") + f'<p class="small muted">{e(DISCLOSE)}</p>', "plain", "Contact"))
    others = [o for o in TOPICS if o["slug"] != t["slug"]][:4]
    return dict(
        path=f"answers/{t['slug']}.html", nav=t["title"].split(":")[0][:28],
        title=t["title"][:65], desc=t["desc"][:160], h1=t["title"], kicker="Answers · Sourced Q&A",
        keywords=[k for k in KEYWORDS if any(w in k.lower() for w in t["slug"].split("-")[:2])][:8] or [t["slug"].replace("-", " ")],
        answer=f"{t['intro']} This page gives {len(t['items'])} short answers, each linked to the official Adobe documentation it is based on, so you can verify and go deeper.",
        schema="Article", category="Answers", date=DATE, sections=secs, faqs=[],
        related=["answers/index.html"] + [f"answers/{o['slug']}.html" for o in others],
        sources=[(S[i][0], S[i][1]) for i in used[:8]],
    )

QA_TOPIC_PAGES = [topic_page(t) for t in TOPICS]
TOTAL = sum(len(t["items"]) for t in TOPICS)

def _all_ids():
    c = {}
    for t in TOPICS:
        for _, _, ids in t["items"]:
            for i in ids: c[i] = c.get(i, 0) + 1
    return c
USE = _all_ids()

INDEX = dict(
    path="answers/index.html", nav="Answers",
    title="Adobe AEP, AJO & CJA Answers Hub: Sourced Q&A | Infinite360"[:65],
    desc=f"{TOTAL} short answers on Adobe Experience Platform, Real-Time CDP, AJO, CJA, Web SDK and Agentic AI, each cited to official documentation."[:160],
    h1="Adobe Experience Platform answers hub", kicker="Answers · Sourced Q&A",
    keywords=["aep questions and answers", "adobe experience platform faq", "aep interview questions", "aep citations"],
    answer=f"This hub holds {TOTAL} short, sourced answers on Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, the Web SDK and Agentic AI across {len(TOPICS)} topics. Every answer links to the official Adobe documentation it is based on, and the full set is also published as answers.json for search engines and AI assistants.",
    schema="CollectionPage", category="Answers", date=DATE,
    sections=[
        ("Topics", '<div class="grid-3">' + "".join(f'<a class="card" href="{t["slug"]}.html"><h3>{e(t["title"].split(":")[0])}</h3><p class="small muted">{len(t["items"])} answers</p><p>{e(t["desc"])}</p></a>' for t in TOPICS) + "</div>", "plain", "Browse"),
        ("Machine-readable copies", f'<p>All questions, answers and source URLs are available as <a href="../answers.json">answers.json</a> and <a href="../llms-full.txt">llms-full.txt</a>. The <a href="../sitemap.xml">XML sitemap</a> lists every page, and <a href="../robots.txt">robots.txt</a> allows search and AI crawlers.</p><p><a href="sources.html">All {len(USE)} cited Adobe documentation pages</a></p>', "alt", "Data"),
        ("Ask us", cta("../") + f'<p class="small muted">{e(DISCLOSE)}</p>', "plain", "Contact"),
    ],
    faqs=[], related=["learn/index.html", "academy/aep-implementation-track/index.html", "search-topics.html"],
)

SOURCES = dict(
    path="answers/sources.html", nav="Sources",
    title="Citations: Adobe Documentation Used in Our Answers | Infinite360"[:65],
    desc=f"The {len(USE)} official Adobe documentation pages cited across our {TOTAL} AEP, AJO, CJA and Web SDK answers, with the number of answers using each."[:160],
    h1="Cited Adobe documentation", kicker="Answers · Citations",
    keywords=["adobe experience platform documentation", "aep citations", "experience league links"],
    answer=f"This page lists the {len(USE)} official Adobe Experience League and related pages cited in the answers hub, with the count of answers that rely on each. Citations point to Adobe's own documentation, which is the authority for product behaviour, limits and availability.",
    schema="CollectionPage", category="Answers", date=DATE,
    sections=[("Sources", '<ul class="checklist">' + "".join(f'<li><a href="{S[i][1]}" rel="noopener" target="_blank">{e(S[i][0])}</a> <span class="small muted">({n} answers)</span></li>' for i, n in sorted(USE.items(), key=lambda x: -x[1])) + "</ul>", "plain", "Citations"),
              ("Back to answers", '<p><a href="index.html">Answers hub</a></p>', "alt", "Navigate")],
    faqs=[], related=["answers/index.html", "learn/index.html"],
)

QA_PAGES = [INDEX, SOURCES] + QA_TOPIC_PAGES

def export():
    import json
    rows = []
    for t in TOPICS:
        for q, a, ids in t["items"]:
            rows.append({"topic": t["title"], "page": f"answers/{t['slug']}.html", "question": q, "answer": a,
                         "sources": [{"title": S[i][0], "url": S[i][1]} for i in ids]})
    return rows

def coverage():
    blob = " ".join((q + " " + a).lower() for t in TOPICS for q, a, _ in t["items"])
    stop = {"adobe", "for", "and", "the", "of", "in", "to", "with", "a", "on"}
    hit = 0
    for k in KEYWORDS:
        ws = [w for w in _re.findall(r"[a-z0-9]+", k.lower()) if w not in stop]
        if ws and all(w in blob for w in ws): hit += 1
    return hit, len(KEYWORDS)
