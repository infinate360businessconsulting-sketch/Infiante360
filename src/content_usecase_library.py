"""Use-case library by industry: all 4,000 rows of data/usecases/martech_use_cases.csv published on 40 industry pages + 1 hub.
One page per industry (100 distinct patterns each), not one page per row: rows differ by industry word, so per-row pages would be near-duplicates.
Rows are illustrative design patterns (CSV Status column); no client results are claimed."""
import csv, html, os, re
from banners import slider_html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV = os.path.join(ROOT, "data", "usecases", "martech_use_cases.csv")
DATE = "2026-11-25"
e = html.escape

_ROWS = list(csv.DictReader(open(CSV, encoding="utf-8-sig")))
CATS = []
for r in _ROWS:
    if r["Category"] not in CATS:
        CATS.append(r["Category"])
INDUSTRIES = []
for r in _ROWS:
    if r["Industry"] not in INDUSTRIES:
        INDUSTRIES.append(r["Industry"])


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# existing hand-written industry hubs, linked where they exist
_EXISTING = {"Retail": "retail", "Banking": "banking", "Insurance": "insurance", "Telecom": "telecom", "Travel": "travel", "Hospitality": "hospitality",
             "Healthcare providers": "healthcare", "Education": "education", "SaaS": "saas", "Manufacturing": "manufacturing",
             "Public sector": "public-sector", "Media and streaming": "media"}

# component text -> documented service page on this site (first match wins)
_LINKS = [("rtcdp", "services/real-time-cdp.html"), ("journey", "services/adobe-journey-optimizer.html"), ("ajo", "services/adobe-journey-optimizer.html"),
          ("decisioning", "services/adobe-journey-optimizer.html"), ("cja", "services/customer-journey-analytics.html"), ("data views", "services/customer-journey-analytics.html"),
          ("reporting", "services/customer-journey-analytics.html"), ("web sdk", "services/web-sdk-adobe-tags.html"), ("edge", "services/web-sdk-adobe-tags.html"),
          ("identity", "services/customer-360-identity-resolution.html"), ("consent", "services/consent-governance-privacy.html"),
          ("privacy", "services/consent-governance-privacy.html"), ("governance", "services/consent-governance-privacy.html"), ("xdm", "services/consent-governance-privacy.html")]


def _link(components):
    c = components.lower()
    return next((u for k, u in _LINKS if k in c), "services/aep-consulting.html")


def _title(ind):
    return f"{ind} MarTech Use Cases: 100 Adobe Patterns"


def _industry_page(ind):
    rows = [r for r in _ROWS if r["Industry"] == ind]
    gov = rows[0]["Governance note"]
    secs = []
    sl = slider_html("../../")
    if sl:
        secs.append(("Featured programmes", sl))
    secs.append(("How to read this library", f'<p class="note"><strong>Illustrative designs.</strong> Every row is a planning pattern for {e(ind.lower())}, not evidence of a delivered client project. The KPI column lists what to track, not results achieved. Standing governance note for this industry: <strong>{e(gov)}</strong>.</p>'
                 '<p>Pick a trigger, check the components, then set a baseline and holdout for the KPI before launch. Component names link to the matching service page.</p>'))
    for cat in CATS:
        cr = [r for r in rows if r["Category"] == cat]
        body = ('<div class="table-wrap"><table><thead><tr><th>ID</th><th>Use case</th><th>Trigger</th><th>Adobe components</th><th>Channel</th><th>KPI to measure</th></tr></thead><tbody>'
                + "".join(f'<tr><td>{e(r["ID"])}</td><th scope="row" id="{e(r["ID"].lower())}">{e(re.sub(r" [(][^)]*[)]$", "", r["Use case"]))}</th><td>{e(r["Trigger"])}</td>'
                          f'<td><a href="../../{_link(r["Adobe components"])}">{e(r["Adobe components"])}</a></td><td>{e(r["Channel"])}</td><td>{e(r["KPI to measure"])}</td></tr>' for r in cr)
                + "</tbody></table></div>")
        secs.append((cat, body))
    nm = ind.lower()
    return dict(
        path=f"use-cases/library/{slug(ind)}.html", title=_title(ind),
        desc=f"100 illustrative Adobe MarTech use cases for {nm}: triggers, components, channels, KPIs and governance. Design patterns, not client results.",
        h1=f"{ind}: 100 Adobe MarTech use cases", kicker=f"Use-case library · {ind}", nav=f"{ind} use cases",
        keywords=[f"{nm} martech use cases", f"{nm} adobe experience platform use cases", f"{nm} customer journey use cases", f"{nm} real-time cdp use cases"],
        answer=f"This page lists 100 illustrative MarTech use cases for {nm}, grouped into ten lifecycle categories from acquisition to measurement and governance. Each row gives the trigger, Adobe components, channel and KPI. The standing governance note for this industry is: {gov}. They are design patterns to adapt, not delivered client results.",
        schema="WebPage", category="Use cases", date=DATE, sections=secs,
        faqs=[(f"Are these {nm} use cases client results?", "No. Each row is an illustrative design pattern for planning. None of them describes a delivered engagement or a measured outcome."),
              (f"Where should a {nm} team start?", f"Pick one use case with a clear trigger and a KPI you can compare against a holdout, confirm the governance note ({gov}) is met, then build it end to end before adding more.")],
        related=["use-cases/library/index.html", "use-cases/index.html", "services/real-time-cdp.html", "services/adobe-journey-optimizer.html"]
        + ([f"use-cases/industries/{_EXISTING[ind]}.html"] if ind in _EXISTING else []),
        sources=[("Adobe Journey Optimizer documentation", "https://experienceleague.adobe.com/en/docs/journey-optimizer"),
                 ("Real-Time CDP documentation", "https://experienceleague.adobe.com/en/docs/experience-platform/rtcdp/home")])


def _hub():
    cards = "".join(
        f'<a class="card link-card" href="{slug(i)}.html"><span class="tag">100 use cases</span><h3>{e(i)}</h3><p>{e(next(r["Governance note"] for r in _ROWS if r["Industry"] == i))}</p></a>' for i in INDUSTRIES)
    secs = []
    sl = slider_html("../../")
    if sl:
        secs.append(("Featured programmes", sl))
    secs += [("Browse by industry", f'<div class="grid-3">{cards}</div>'),
             ("Ten lifecycle categories", "<ul class=\"checklist cols-2\">" + "".join(f"<li>{e(c)}: 10 per industry, 400 in total</li>" for c in CATS) + "</ul>"),
             ("What this library is", f'<p class="note"><strong>Illustrative designs.</strong> The library holds {len(_ROWS):,} planning patterns across {len(INDUSTRIES)} industries. They are not client engagements and carry no results. Each industry page keeps all 100 of its patterns together so they can be compared, instead of splitting them into thin single-row pages.</p>'
              '<p>Looking for a single worked example? See the <a href="../index.html">hand-written use cases</a> and the <a href="../real-time-use-case-library.html">50 real-time use cases</a>.</p>')]
    return dict(
        path="use-cases/library/index.html", title="MarTech Use-Case Library: 40 Industries, 4,000 Patterns",
        desc="Browse 4,000 illustrative Adobe MarTech use cases across 40 industries and ten lifecycle categories, each with trigger, components, channel and KPI.",
        h1="MarTech use-case library by industry", kicker="Use-case library", nav="Use-case library",
        keywords=["martech use cases by industry", "adobe experience platform use cases", "customer journey use case library", "real-time cdp use cases"],
        answer="This library lists 4,000 illustrative Adobe MarTech use cases across 40 industries and ten lifecycle categories, from acquisition to measurement and governance. Open an industry to see its 100 patterns with triggers, components, channels and KPIs. They are design patterns for planning, not delivered client results.",
        schema="CollectionPage", category="Use cases", date=DATE, sections=secs,
        faqs=[("Are these real client results?", "No. Every row is an illustrative design pattern for planning. None describes a delivered engagement."),
              ("Why one page per industry?", "The same patterns recur across industries with different triggers and governance notes. One page per industry keeps each set comparable and avoids thousands of near-identical pages.")],
        related=["use-cases/index.html", "use-cases/real-time-use-case-library.html", "services/real-time-cdp.html", "services/adobe-journey-optimizer.html"],
        sources=[("Adobe Experience Platform documentation", "https://experienceleague.adobe.com/en/docs/experience-platform")])


LIBRARY_PAGES = [_hub()] + [_industry_page(i) for i in INDUSTRIES]
