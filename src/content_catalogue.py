"""Course catalogue hub. Reads data/catalogue/catalogue.json; shows only status=published entries that have a live page.
Draft courses (curriculum, instructor, price or schedule not yet approved) are counted as 'in planning' and never named."""
import html as _h, json as _j, os as _o
e = _h.escape
_P = _o.path.join(_o.path.dirname(_o.path.dirname(_o.path.abspath(__file__))), "data", "catalogue", "catalogue.json")
CAT = _j.load(open(_P, encoding="utf-8"))["categories"]


def _rel(pg):
    return pg[len("academy/"):] if pg.startswith("academy/") else "../" + pg


def _block(c):
    live = [k for k in c["courses"] if k["status"] == "published" and k.get("page")]
    plan = len(c["courses"]) - len(live)
    li = "".join(f'<li><a href="{e(_rel(k["page"]))}">{e(k["title"])}</a> <a href="{e(_rel(k["page"]))}">Know more</a></li>' for k in live)
    out = ("<ul class=\"checklist\">" + li + "</ul>") if live else ""
    if plan:
        out += f'<p>{plan} more topic{"s" if plan != 1 else ""} in planning. Curriculum, dates and fees will be announced after approval. <a href="../contact-us.html">Ask to be notified</a>.</p>'
    return out


CATALOGUE_PAGE = dict(
    path="academy/catalogue.html", nav="Course catalogue",
    title="Course Catalogue: Adobe MarTech, AI and Data | Infiante360",
    desc="Browse Infiante360 Tech Academy course categories: Adobe Experience Cloud, Agentic AI, data engineering and more. Know more links go to each live course page.",
    h1="Infiante360 Tech Academy course catalogue", kicker="Courses",
    keywords=["infiante360 course catalogue", "adobe experience platform courses", "agentic ai course", "martech training courses", "data engineering training"],
    schema="WebPage", category="Academy",
    answer="This catalogue groups Infiante360 Tech Academy learning by technology: Adobe Experience Cloud, Agentic AI, MarTech, data engineering, cloud, analytics and career programs. Courses with a live page have a Know more link. Other topics are in planning, and their curriculum, dates and fees will be announced once approved. Nothing here is a placement or certification promise.",
    sections=[(c["category"], _block(c)) for c in CAT] + [
        ("Watch free demos", '<p>See sample sessions on the <a href="https://www.youtube.com/@Infiante360TechAcademy" rel="noopener" target="_blank">Infiante360 YouTube channel</a>, or <a href="videos.html">browse the demo list</a>.</p>'),
        ("Talk to us", '<p>Questions about a course or team training? Call or WhatsApp +91 82968 93895 or use the <a href="../contact-us.html">contact form</a>.</p>'),
    ],
    faqs=[("Why are some categories without course links?", "Those topics are in planning. We publish a course page only after its curriculum, instructor, fee and schedule are approved."),
          ("Is Infiante360 affiliated with Adobe?", "No. It is independent. Adobe product names belong to Adobe.")],
    related=["academy/index.html", "academy/videos.html", "training/corporate-training.html"],
)
CATALOGUE_ALL = [CATALOGUE_PAGE]
