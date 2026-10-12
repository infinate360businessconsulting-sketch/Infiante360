#!/usr/bin/env python3
"""Static site generator for the Infinite360 GitHub Pages site.

Usage:  python3 src/build.py [out_dir]          (default out_dir: _site)
Env:    SITE_BASE  absolute base URL with trailing slash.

Generates every page from the content modules with one shared template, then writes
sitemap.xml, robots.txt, llms.txt, 404.html and thank-you.html, and finally validates:
unique titles/descriptions/H1s, description length, valid JSON-LD, and that every internal
link resolves to a generated page. The build fails on any error.
"""
import datetime as dt
import html
import json
import os
import re
import shutil
import sys
from urllib.parse import urljoin

sys.path.insert(0, os.path.dirname(__file__))
from content_aep import AEP_PAGES  # noqa: E402
from content_core import CORE, BOOKING  # noqa: E402
from content_services import SERVICES  # noqa: E402
from content_more import MORE  # noqa: E402
from content_home import HOME  # noqa: E402
from content_corp import CORP  # noqa: E402
from content_academy import ACADEMY  # noqa: E402
from content_events import EVENTS  # noqa: E402
from content_cases import CASE_PAGES, SIMULATORS, REGISTER, WHATSAPP_MSG, LMS, BROCHURE, LI_GROUP  # noqa: E402
from content_kb import KB_PAGES  # noqa: E402
from content_growth import GROWTH_PAGES, LANDINGS, LEGAL  # noqa: E402
from content_stacks import STACK_PAGES  # noqa: E402
from content_industry import INDUSTRY_ALL  # noqa: E402
from content_plan import PLAN_ALL  # noqa: E402
from content_quiz import QUIZ_ALL  # noqa: E402
from content_brochures import BRO_ALL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(ROOT, "_site")
_VERCEL = os.environ.get("VERCEL_PROJECT_PRODUCTION_URL")  # set by Vercel during builds
BASE = os.environ.get("SITE_BASE") or (f"https://{_VERCEL}/" if _VERCEL else "https://infinate360businessconsulting-sketch.github.io/Infiante360/")
TODAY = os.environ.get("SITE_LASTMOD", dt.date.today().isoformat())

BRAND = "Infinite360"
EMAIL = "infinate360businessconsulting@gmail.com"
PHONE_E164 = "+918296893895"
PHONE_DISPLAY = "+91 82968 93895"
WHATSAPP = "https://wa.me/918296893895"
LINKEDIN_PERSON = "https://linkedin.com/in/pavanbabu1"
LINKEDIN_COMPANY = "https://www.linkedin.com/company/30928383"
YOUTUBE = "https://www.youtube.com/@Infiante360TechAcademy"
PORTFOLIO = "https://www.martechconsultant.tech/Pavan.html"
FORM_ACTION = f"https://formsubmit.co/{EMAIL}"

def _load(name):
    with open(os.path.join(ROOT, "content", name), encoding="utf-8") as fh:
        return json.load(fh)


SETTINGS = _load("settings.json")
GA4_ID = os.environ.get("GA4_ID") or SETTINGS.get("ga4_id", "")
GTM_ID = os.environ.get("GTM_ID") or SETTINGS.get("gtm_id", "")
if GA4_ID and not re.fullmatch(r"G-[A-Z0-9]{4,12}", GA4_ID):
    sys.exit(f"Invalid GA4 measurement ID: {GA4_ID!r}")
if GTM_ID and not re.fullmatch(r"GTM-[A-Z0-9]{4,10}", GTM_ID):
    sys.exit(f"Invalid GTM container ID: {GTM_ID!r}")
TESTIMONIALS = [t for t in _load("testimonials.json").get("items", []) if t.get("verified") and t.get("consent")]

PAGES = [HOME] + SERVICES + AEP_PAGES + CORE[1:] + MORE + CORP + ACADEMY + EVENTS + CASE_PAGES + KB_PAGES + GROWTH_PAGES + STACK_PAGES + INDUSTRY_ALL + PLAN_ALL + QUIZ_ALL + BRO_ALL

TOPICS = [
    ("adobe-experience-platform", "Adobe Experience Platform", "AEP", ["experience platform", "aep", "xdm", "schema", "dataset", "ingestion", "identity", "profile"]),
    ("real-time-cdp", "Real-Time CDP", "RTCDP", ["real-time cdp", "rtcdp", "audience", "activation", "destination", "suppression", "customer 360"]),
    ("journey-optimizer", "Adobe Journey Optimizer", "AJO", ["journey optimizer", "ajo", "journey", "campaign", "onboarding", "renewal"]),
    ("analytics-cja", "Customer Journey Analytics and Adobe Analytics", "CJA", ["cja", "customer journey analytics", "adobe analytics", "evar", "backfill", "attribution"]),
    ("web-sdk-tags", "Web SDK and Adobe Tags", "Web SDK", ["web sdk", "tags", "data element", "ecid", "datastream", "consent"]),
    ("agentic-ai-mcp", "Agentic AI and MCP", "Agentic AI", ["agentic", "mcp", " ai "]),
    ("careers-training", "Careers and training", "Careers", ["career", "training", "course", "bootcamp", "interview", "academy", "workshop"]),
    ("industries", "Industry solutions", "Industries", ["bank", "bfsi", "airline", "travel", "insurance", "telecom", "retail", "hospitality"]),
]


def _topic_pages():
    pages = []
    for slug_, name, short, terms in TOPICS:
        pages.append(dict(
            path=f"topics/{slug_}.html", nav=short, title=(f"{name}: Guides, Case Studies & Services" if len(name) < 28 else f"{short}: Guides, Case Studies & Services"),
            desc=f"Every Infinite360 page on {name}: services, case studies, use cases, student questions, guides and training.",
            h1=f"{name}: everything in one place", kicker="Topic", schema="CollectionPage", topic_terms=terms,
            keywords=[f"{name.lower()} guides", f"{short.lower()} case study", f"{short.lower()} training", f"{short.lower()} consulting"],
            answer=f"This topic page collects every Infinite360 page related to {name} - consulting services, implementation case studies, use cases, student questions, guides and training programs - so you can explore the subject in depth and move between related pages easily.",
            sections=[("Pages on this topic", "@@TOPIC_LIST@@")], faqs=[], related=[]))
    return pages


TOPIC_PAGES = _topic_pages()
PAGES += TOPIC_PAGES

# Admin-editable overrides (content/overrides.json, edited through /admin/)
for _o in _load("overrides.json").get("items", []):
    for _p in PAGES:
        if _p["path"] == _o.get("path"):
            for _k in ("title", "desc", "h1", "lede", "answer", "notice"):
                if _o.get(_k):
                    _p[_k] = _o[_k]
BY_PATH = {p["path"]: p for p in PAGES}
LEGAL_PATHS = {l["path"] for l in LEGAL}
SOURCES_FILE = os.path.join(ROOT, "content", "news-sources.json")

INTERESTS = [
    ("aep", "Adobe Experience Platform (AEP) consulting"),
    ("rtcdp", "Real-Time CDP"),
    ("ajo", "Adobe Journey Optimizer (AJO)"),
    ("cja", "Customer Journey Analytics / Adobe Analytics"),
    ("websdk", "Web SDK / Adobe Tags implementation"),
    ("data", "Data engineering & integration"),
    ("ai", "Agentic AI & MCP"),
    ("advisory", "MarTech strategy / architecture review"),
    ("staff", "Staff augmentation (engineers / architects)"),
    ("corporate", "Corporate training"),
    ("course", "Career accelerator (individual course)"),
    ("other", "Something else"),
]
INTEREST_BY_PATH = {
    "services/aep-consulting.html": "aep", "services/real-time-cdp.html": "rtcdp",
    "services/adobe-journey-optimizer.html": "ajo", "services/customer-journey-analytics.html": "cja",
    "services/web-sdk-adobe-tags.html": "websdk", "services/data-engineering.html": "data",
    "services/agentic-ai-mcp.html": "ai", "services/martech-strategy-advisory.html": "advisory",
    "services/engagement-model.html": "advisory", "services/staff-augmentation.html": "staff",
    "training/corporate-training.html": "corporate", "training/index.html": "course",
}

NAV = [
    ("services/index.html", "Services"),
    ("solutions/index.html", "Solutions"),
    ("academy/index.html", "Academy"),
    ("case-studies/index.html", "Case studies"),
    ("about-us.html", "About"),
    ("learn/index.html", "Learn"),
]

SECTION_HUBS = {
    "services": ("services/index.html", "Services"),
    "adobe-experience-platform": ("adobe-experience-platform/index.html", "AEP Guides"),
    "training": ("academy/index.html", "Academy"),
    "academy": ("academy/index.html", "Academy"),
    "guides": ("learn/index.html", "Learn"),
    "learn": ("learn/index.html", "Learn"),
    "solutions": ("solutions/index.html", "Solutions"),
    "case-studies": ("case-studies/index.html", "Case studies"),
    "use-cases": ("use-cases/index.html", "Use cases"),
    "stacks": ("stacks/index.html", "MarTech stacks"),
    "lp": (None, ""),
    "topics": ("sitemap.html", "Site map"),
}

LOGO_SVG = (
    '<svg viewBox="0 0 64 34" aria-hidden="true" focusable="false"><path d="M17 4C8.7 4 3 9.9 3 17s5.7 13 14 13c6.5 0 10.6-4.6 15-10.1C36.4 '
    '14.4 40.5 10 47 10c4.4 0 7.5 3 7.5 7s-3.1 7-7.5 7c-3.3 0-5.9-1.9-8.4-4.6" fill="none" stroke="#d7141e" stroke-width="5.5" '
    'stroke-linecap="round"/><path d="M25.4 13.6C22.9 10.9 20.3 9 17 9c-4.4 0-7.5 3-7.5 8s3.1 8 7.5 8M47 4c8.3 0 14 5.9 14 13s-5.7 13-14 '
    '13c-6.5 0-10.6-4.6-15-10.1" fill="none" stroke="#0b1730" stroke-width="5.5" stroke-linecap="round"/></svg>'
)
WA_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5 0a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.6-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.4-.3Z"/></svg>'
MENU_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h16M4 17h16" stroke="#0b1730" stroke-width="2" stroke-linecap="round"/></svg>'

e = html.escape


# ------------------------------------------------------------------ URL helpers
def url_path(path):
    """Public path for a page file ('services/index.html' -> 'services/')."""
    if path == "index.html":
        return ""
    if path.endswith("/index.html"):
        return path[: -len("index.html")]
    return path


def abs_url(path):
    return BASE + url_path(path)


def rel(target, from_path):
    """Relative href from one page file to another page file (directory style for index pages)."""
    from_dir = os.path.dirname(from_path) or "."
    tgt = url_path(target)
    if tgt == "" or tgt.endswith("/"):
        r = os.path.relpath(tgt.rstrip("/") or ".", from_dir)
        return "./" if r == "." else r + "/"
    return os.path.relpath(tgt, from_dir)


_VERSIONS = {}


def asset_version(name):
    """Short content hash so browsers fetch new CSS/JS after each deploy (assets are cached for a week)."""
    if name not in _VERSIONS:
        import hashlib
        with open(os.path.join(ROOT, "assets", name), "rb") as fh:
            _VERSIONS[name] = hashlib.sha1(fh.read()).hexdigest()[:10]
    return _VERSIONS[name]


def asset(name, from_path):
    url = os.path.relpath("assets/" + name, os.path.dirname(from_path) or ".")
    return url + ("?v=" + asset_version(name) if name.endswith((".css", ".js")) else "")


def normalise_links(body):
    """Content is authored with explicit 'index.html' links; publish them directory-style."""
    body = re.sub(r'href="((?:\.\./)*(?:[\w-]+/)*)index\.html"', lambda m: f'href="{m.group(1) or "./"}"', body)
    return body


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


# ------------------------------------------------------------------ Components
def short_name(p):
    return p.get("nav") or re.split(r"[:|(]", p["h1"])[0].strip()


def crumbs(p):
    items = [("index.html", "Home")]
    parts = p["path"].split("/")
    if len(parts) > 1:
        hub, label = SECTION_HUBS.get(parts[0], (None, ""))
        if hub and hub != p["path"]:
            items.append((hub, label))
    if p["path"] != "index.html":
        items.append((p["path"], short_name(p)))
    return items


def header(p):
    links = []
    for path, label in NAV:
        cur = ' aria-current="page"' if (p["path"] == path or (path.endswith("index.html") and path != "index.html" and p["path"].startswith(os.path.dirname(path) + "/"))) else ""
        links.append(f'<li><a href="{rel(path, p["path"])}"{cur}>{label}</a></li>')
    links.append(f'<li><a class="btn btn-primary" href="{rel("contact-us.html", p["path"])}">Contact us</a></li>')
    ann = ""
    if SETTINGS.get("announcement"):
        link = SETTINGS.get("announcement_link") or ""
        target = link if link.startswith("http") else rel(link, p["path"]) if link in BY_PATH else ""
        ann = f'<a class="announce" href="{target}">{e(SETTINGS["announcement"])} &rarr;</a>' if target else f'<span class="announce">{e(SETTINGS["announcement"])}</span>'
    top = f"""<div class="topbar"><div class="wrap topbar-row">{ann}
<nav class="toplinks" aria-label="Quick links"><a href="{REGISTER}" rel="noopener" target="_blank">Register</a><a href="{WHATSAPP_MSG}" rel="noopener" target="_blank">WhatsApp</a><a href="{rel('academy/simulators.html', p['path'])}">Simulators</a><a href="{LMS}" rel="noopener" target="_blank">LMS</a><a href="{BROCHURE}" rel="noopener" target="_blank">Brochure</a><a href="{rel('sitemap.html', p['path'])}">Site map</a></nav></div></div>"""
    return f"""<a class="skip-link" href="#main">Skip to content</a>
{gtm_noscript()}{top}
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="{rel('index.html', p['path'])}" aria-label="{BRAND} home">{LOGO_SVG}<span>{BRAND}<small>Consulting &middot; Academy</small></span></a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{MENU_SVG}</button>
    <nav id="site-nav" class="site-nav" aria-label="Main"><ul>{''.join(links)}</ul></nav>
  </div>
</header>"""


def breadcrumb_html(p):
    if p["path"] == "index.html":
        return ""
    items = crumbs(p)
    lis = []
    for i, (path, label) in enumerate(items):
        if i == len(items) - 1:
            lis.append(f'<li><span aria-current="page">{e(label)}</span></li>')
        else:
            lis.append(f'<li><a href="{rel(path, p["path"])}">{e(label)}</a></li>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb"><ol>{"".join(lis)}</ol></nav>'


def hero(p):
    home = p["path"] == "index.html"
    ctas = ""
    if p.get("hero_ctas"):
        ctas = f"""<div class="cta-row">
<a class="btn btn-primary" href="{rel('services/index.html', p['path'])}">Explore consulting</a>
<a class="btn btn-ghost" href="{rel('training/index.html', p['path'])}">View training</a></div>
<ul class="chips" aria-label="Technologies">{''.join(f'<li>{t}</li>' for t in ['Adobe Experience Platform','Real-Time CDP','Journey Optimizer','Customer Journey Analytics','Web SDK','Agentic AI &amp; MCP'])}</ul>"""
    lede = p.get("lede") or p["desc"]
    if p.get("hero_cta"):
        label, target = p["hero_cta"]
        ctas += f'<div class="cta-row"><a class="btn btn-primary" href="{target if target.startswith(("http", "#")) else rel(target, p["path"])}">{label}</a><a class="btn btn-ghost" href="{rel("contact-us.html", p["path"])}">Talk to us</a></div>'
    visual = p.get("hero_visual", "")
    copy = f"""{breadcrumb_html(p)}
<span class="kicker">{p['kicker']}</span>
<h1>{e(p['h1'])}</h1>
<p class="lede">{e(lede)}</p>
{ctas}"""
    inner = f'<div class="hero-grid"><div class="hero-copy">{copy}</div><div class="hero-visual" aria-hidden="true">{visual}</div></div>' if visual else copy
    return f"""<div class="hero{' home' if home else ''}"><div class="hero-orbs" aria-hidden="true"></div><div class="wrap">
{inner}
</div></div>"""


def service_cards(from_path):
    cards = []
    for s in SERVICES[1:]:
        cards.append(f'<a class="card link-card" href="{rel(s["path"], from_path)}"><h3>{e(short_name(s))}</h3><p>{e(s["desc"].split(":")[0] if len(s["desc"]) > 150 else s["desc"])}</p><span class="more">Learn more &rarr;</span></a>')
    return f'<div class="grid-2">{"".join(cards)}</div>'


def form_html(p, compact=False):
    pre = p.get("interest") or INTEREST_BY_PATH.get(p["path"])
    fid = "q" if compact else "c"
    opts = ['<option value="">Select an option</option>'] + [
        f'<option value="{e(label)}"{" selected" if key == pre else ""}>{e(label)}</option>' for key, label in INTERESTS]

    def field(name, label, typ="text", req=True, auto="", hint="", full=False, extra=""):
        r = ' required aria-required="true"' if req else ""
        star = ' <span class="req" aria-hidden="true">*</span>' if req else ' <span class="muted small">(optional)</span>'
        hint_html = f'<span class="hint" id="{fid}-{name}-hint">{hint}</span>' if hint else ""
        desc = f' aria-describedby="{fid}-{name}-error{" " + fid + "-" + name + "-hint" if hint else ""}"'
        ac = f' autocomplete="{auto}"' if auto else ""
        return (f'<div class="field{" full" if full else ""}"><label for="{fid}-{name}">{label}{star}</label>'
                f'<input id="{fid}-{name}" name="{name}" type="{typ}"{ac}{r}{desc}{extra}>{hint_html}'
                f'<span class="error" id="{fid}-{name}-error" aria-live="polite"></span></div>')

    interest = (f'<div class="field{" full" if compact else ""}"><label for="{fid}-interest">What can we help with? <span class="req" aria-hidden="true">*</span></label>'
                f'<select id="{fid}-interest" name="interest" required aria-required="true" aria-describedby="{fid}-interest-error" data-msg-required="Please choose a topic.">{"".join(opts)}</select>'
                f'<span class="error" id="{fid}-interest-error" aria-live="polite"></span></div>')
    message = (f'<div class="field full"><label for="{fid}-message">Message <span class="req" aria-hidden="true">*</span></label>'
               f'<textarea id="{fid}-message" name="message" required aria-required="true" minlength="10" aria-describedby="{fid}-message-error {fid}-message-hint" '
               f'data-msg-required="Please tell us briefly what you need."></textarea>'
               f'<span class="hint" id="{fid}-message-hint">Goals, current platforms and timeline help us reply with useful next steps. Please do not include passwords or customer data.</span>'
               f'<span class="error" id="{fid}-message-error" aria-live="polite"></span></div>')
    consent = (f'<div class="field full"><div class="consent"><input id="{fid}-consent" name="consent" type="checkbox" value="yes" required aria-required="true" aria-describedby="{fid}-consent-error" data-msg-required="Please confirm so we can reply.">'
               f'<label for="{fid}-consent" style="font-weight:500">I agree that {BRAND} may use these details to respond to my enquiry, as described in the <a href="{rel("privacy-policy.html", p["path"])}">privacy policy</a>.</label></div>'
               f'<span class="error" id="{fid}-consent-error" aria-live="polite"></span></div>')

    if compact and p.get("program"):
        prog = (f'<input type="hidden" name="program" value="{e(p["h1"])}">'
                '<fieldset class="field full"><legend>What are you interested in?</legend><div class="choice">'
                + "".join(f'<label><input type="radio" name="interest" value="{v}"{" checked" if i == 0 else ""}> {v}</label>'
                          for i, v in enumerate(p.get("interest_options") or ["This program", "A single tool at a lower price", "A course on another platform"]))
                + "</div></fieldset>")
        rows = (field("name", "Your name", auto="name", extra=' data-msg-required="Please enter your name."')
                + field("email", "Email", typ="email", auto="email", extra=' data-msg-required="Please enter your email."')
                + field("phone", "Phone / WhatsApp", typ="tel", req=False, auto="tel", extra=' pattern="[+0-9 ()-]{7,20}" data-msg-pattern="Use digits, spaces and + only."')
                + prog
                + field("tool", "Which tool?", req=False, hint="Optional, e.g. AEP only, AJO, CJA")
                + message + consent)
    elif compact:
        rows = (field("name", "Full name", auto="name", extra=' data-msg-required="Please enter your name."')
                + field("email", "Email", typ="email", auto="email", extra=' data-msg-required="Please enter your email."')
                + interest + message + consent)
    else:
        rows = (field("first_name", "First name", auto="given-name", extra=' data-msg-required="Please enter your first name."')
                + field("last_name", "Last name", auto="family-name", extra=' data-msg-required="Please enter your last name."')
                + field("email", "Business email", typ="email", auto="email", extra=' data-msg-required="Please enter your email."')
                + field("phone", "Phone / WhatsApp", typ="tel", req=False, auto="tel", hint="Include country code, e.g. +91.", extra=' pattern="[+0-9 ()-]{7,20}" data-msg-pattern="Use digits, spaces and + only."')
                + field("company", "Company", req=False, auto="organization")
                + field("job_title", "Job title", req=False, auto="organization-title")
                + field("country", "Country", req=False, auto="country-name")
                + interest
                + f'<fieldset class="field full"><legend>Preferred contact method</legend><div class="choice">'
                + "".join(f'<label><input type="radio" name="preferred_contact" value="{v}"{" checked" if v == "Email" else ""}> {v}</label>' for v in ["Email", "Phone", "WhatsApp"])
                + "</div></fieldset>"
                + message + consent)
    return f"""<form class="form js-validate" action="{FORM_ACTION}" method="POST" aria-describedby="{fid}-form-note">
<input type="hidden" name="_subject" value="New enquiry from the {BRAND} website">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="{BASE}thank-you.html">
<input type="hidden" name="source_page" value="{abs_url(p['path'])}">
<div class="hp" aria-hidden="true"><label for="{fid}-honey">Leave this field empty</label><input id="{fid}-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
<div class="form-grid">{rows}</div>
<div class="cta-row"><button class="btn btn-primary" type="submit">Send enquiry</button>
<button class="btn btn-wa js-whatsapp" type="button">{WA_SVG} Send via WhatsApp instead</button></div>
<p class="form-status" role="status" aria-live="polite"></p>
<p class="small muted" id="{fid}-form-note">Fields marked <span class="req">*</span> are required. We usually reply within two business days.</p>
</form>"""


def contact_block(p):
    return f"""<div class="contact-grid">
<div class="form-card">{form_html(p)}</div>
<aside class="card" aria-label="Direct contact">
<h3>Prefer to talk directly?</h3>
<ul class="contact-list">
<li><strong>WhatsApp / phone</strong><a href="{WHATSAPP}" rel="noopener" target="_blank">{PHONE_DISPLAY}</a></li>
<li><strong>Email</strong><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><strong>Book a call</strong><a href="{BOOKING}" rel="noopener" target="_blank">Choose a time in the calendar</a></li>
<li><strong>LinkedIn</strong><a href="{LINKEDIN_PERSON}" rel="noopener" target="_blank">Pavan Babu Gandla</a></li>
</ul>
</aside></div>"""


def faq_html(p):
    if not p.get("faqs"):
        return ""
    items = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in p["faqs"])
    head = "" if p["schema"] == "FAQPage" else "<h2 id=\"faq\">Frequently asked questions</h2>"
    return f'<section class="faq" aria-labelledby="faq">{head}{items}</section>'


def topic_chips(p):
    if p["path"].startswith(("topics/", "lp/")) or p["path"] in LEGAL_PATHS:
        return ""
    terms = page_terms(p)
    hits = [t for t in TOPIC_PAGES if any(k in terms for k in t["topic_terms"])]
    if not hits:
        return ""
    return ('<nav class="topic-chips" aria-label="Topics"><span>Explore topics:</span>'
            + "".join(f'<a href="{rel(t["path"], p["path"])}">{e(t["nav"])}</a>' for t in hits) + "</nav>")


def related_html(p):
    rel_paths = [r for r in p.get("related", []) if r in BY_PATH]
    chips = topic_chips(p)
    if not rel_paths:
        return f'<div class="wrap">{chips}</div>' if chips else ""
    cards = "".join(
        f'<a class="card link-card" href="{rel(r, p["path"])}"><h3>{e(short_name(BY_PATH[r]))}</h3><p>{e(BY_PATH[r]["desc"][:140].rsplit(" ", 1)[0])}&hellip;</p></a>'
        for r in rel_paths)
    return f'<section class="section alt" aria-labelledby="related"><div class="wrap"><h2 id="related">Related pages</h2><div class="grid-3">{cards}</div>{chips}</div></section>'


def cta_band(p):
    if p["path"] in ("contact-us.html", "privacy-policy.html") or p.get("landing") or p["path"] in LEGAL_PATHS:
        return ""
    if p["path"] in INTEREST_BY_PATH or p.get("program") or p.get("interest"):
        return f"""<section class="section" aria-labelledby="enquire"><div class="wrap"><div class="contact-grid">
<div><h2 id="enquire">{"Request details: " if p.get("program") else "Talk to us about "}{e(short_name(p))}</h2><p>{"Tell us you are interested and we will email the full syllabus, dates and next steps. Only need one tool? Choose a single tool at a lower price. No payment now." if p.get("program") else "Share a few details and we will reply with practical next steps. No obligation."}</p>
<ul class="contact-list"><li><strong>WhatsApp</strong><a href="{WHATSAPP}" rel="noopener" target="_blank">{PHONE_DISPLAY}</a></li><li><strong>Book a call</strong><a href="{BOOKING}" rel="noopener" target="_blank">Choose a time</a></li></ul></div>
<div class="form-card">{form_html(p, compact=True)}</div></div></div></section>"""
    return f"""<section class="section"><div class="wrap"><div class="cta-band">
<div><h2>Ready to move your Adobe MarTech program forward?</h2><p>Consulting for enterprise teams, training for professionals. Tell us where you are today.</p></div>
<div class="cta-row"><a class="btn btn-light" href="{rel('contact-us.html', p['path'])}">Contact us</a><a class="btn btn-ghost" style="color:#fff" href="{rel('training/index.html', p['path'])}">See training</a></div>
</div></div></section>"""


def floater(p):
    """Floating proof widget: rotates verified reviews if any exist, otherwise invites a review. Hidden on landing, legal and admin pages."""
    if p.get("landing") or p["path"] in LEGAL_PATHS or p["path"] == "academy/testimonials.html":
        return ""
    page = rel("academy/testimonials.html", p["path"])
    cases = rel("case-studies/index.html", p["path"])
    data = json.dumps([{"q": t["quote"][:220], "n": t["name"], "r": " · ".join(x for x in (t.get("role"), t.get("program")) if x)} for t in TESTIMONIALS], ensure_ascii=False)
    return (f'<aside class="floater" id="floater" aria-label="Reviews and case studies" hidden data-reviews="{e(data)}" data-page="{page}">'
            f'<button type="button" class="floater-x" aria-label="Dismiss">&times;</button>'
            f'<p class="floater-text"></p><p class="floater-links"><a class="floater-main" href="{page}"></a> <a href="{cases}">Case studies</a></p></aside>')


ABOUT_FOOTER = """<section class="footer-about" aria-labelledby="fa-h"><h2 id="fa-h">About Infinite360 Business Consulting</h2>
<div class="fa-cols"><div>
<p>Infinite360 Business Consulting is a technology and digital transformation consulting firm helping organizations turn complex data, customer experience, and technology challenges into measurable business outcomes.</p>
<p>We specialize in Adobe Experience Cloud, Customer Data Platforms, MarTech, Data Engineering, AI, Analytics, and Digital Transformation, helping enterprises build connected customer experiences and modern, scalable technology ecosystems.</p>
<p>Our consulting approach combines strategy, architecture, implementation, optimization, and enablement. We work closely with business and technology teams to understand their objectives, identify opportunities, design the right solution, and accelerate execution.</p>
<h3>Our approach</h3><p>We believe successful transformation is not just about implementing technology. It is about connecting people, data, processes, platforms, and business objectives. Our methodology: <strong>Discover &rarr; Design &rarr; Build &rarr; Integrate &rarr; Activate &rarr; Measure &rarr; Optimize</strong>. This helps organizations move from disconnected systems and fragmented customer data toward real-time, intelligent, personalized, and measurable customer experiences.</p>
</div><div>
<h3>What we do</h3><ul><li>Digital Transformation &amp; Technology Consulting</li><li>Adobe Experience Platform (AEP) &amp; Real-Time CDP</li><li>Adobe Journey Optimizer (AJO)</li><li>Customer Journey Analytics (CJA) &amp; Adobe Analytics</li><li>Customer 360 &amp; Data Strategy</li><li>MarTech &amp; Customer Experience Architecture</li><li>AI &amp; Agentic AI Solutions</li><li>Data Engineering, Cloud &amp; Analytics</li><li>Marketing Automation &amp; Personalization</li><li>Architecture Reviews, Assessments &amp; Optimization</li><li>Corporate Training &amp; Technology Enablement</li></ul>
<h3>Why Infinite360</h3><p>We bring together technical expertise, enterprise consulting experience, and practical implementation knowledge to help clients reduce complexity, accelerate delivery, improve customer engagement, and create sustainable business value from their technology investments.</p>
<p><strong>Vision:</strong> To help organizations build intelligent, connected, and future-ready digital businesses through technology, data, AI, and customer experience innovation.</p>
<p><strong>Mission:</strong> Make enterprise technology simpler, smarter, and more valuable for the business.</p>
</div></div></section>
"""


def footer(p):
    def col(title, paths):
        lis = "".join(f'<li><a href="{rel(x, p["path"])}">{e(short_name(BY_PATH[x]))}</a></li>' for x in paths)
        return f"<div><h2>{title}</h2><ul>{lis}</ul></div>"
    svc = [s["path"] for s in SERVICES] + ["services/adobe-experience-cloud.html", "services/engagement-model.html", "services/staff-augmentation.html", "solutions/index.html"]
    aep = [a["path"] for a in AEP_PAGES]
    learn = ["academy/index.html", "academy/workshops.html", "academy/aep-launchpad-bootcamp.html", "academy/videos.html", "academy/free-resources.html", "academy/martech-roles.html", "learn/index.html", "training/index.html", "training/career-transition.html", "training/corporate-training.html", "guides/marketo-engage-aep.html", "guides/aep-vs-real-time-cdp.html", "guides/cja-vs-adobe-analytics.html", "guides/what-is-mcp.html"]
    company = ["about-us.html", "pavan-babu-gandla.html", "industries.html", "case-studies/index.html", "use-cases/index.html", "services/contract-hiring.html", "faq.html", "contact-us.html", "stacks/index.html"] + [c["path"] for c in STACK_PAGES[1:]]
    more = ["academy/simulators.html", "academy/recording-platform.html", "academy/youtube-playlists.html", "academy/community.html", "academy/testimonials.html",
            "learn/student-questions.html", "guides/ajo-implementation-best-practices.html", "feeds.html", "sitemap.html"] + [l["path"] for l in LANDINGS]
    return f"""<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><a class="brand" href="{rel('index.html', p['path'])}">{LOGO_SVG}<span>{BRAND}<small>Consulting &middot; Academy</small></span></a>
<p style="margin-top:14px">Adobe MarTech consulting, corporate training and a practical Tech Academy for AEP, RTCDP, AJO, CJA and Agentic AI.</p>
<ul><li><a href="{WHATSAPP}" rel="noopener" target="_blank">WhatsApp {PHONE_DISPLAY}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><a href="{LINKEDIN_PERSON}" rel="noopener" target="_blank">LinkedIn</a> &middot; <a href="{YOUTUBE}" rel="noopener" target="_blank">YouTube</a></li></ul>
{col("Company", company).replace('<div><h2>', '<div style="margin-top:18px"><h2>')}</div>
{col("Services", svc)}
{col("AEP guides", aep)}
{col("Training &amp; guides", learn)}
{col("Academy &amp; get started", more)}
</div>
{ABOUT_FOOTER}
<nav class="legal-links" aria-label="Legal">{" ".join(f'<a href="{rel(x, p["path"])}">{e(short_name(BY_PATH[x]))}</a>' for x in ["privacy-policy.html", "terms-and-conditions.html", "refund-policy.html", "disclaimer.html", "sitemap.html"])}</nav>
<div class="footer-legal">
<p>&copy; <span id="year">{TODAY[:4]}</span> {BRAND}. Adobe, Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics are trademarks of Adobe. {BRAND} is independent and not affiliated with or endorsed by Adobe.</p>
<p>Some content on this site is created or enhanced with AI assistance to support research and organisation, and is curated for accuracy and relevance. Always confirm product details against current Adobe documentation.</p>
<p>Training outcomes depend on participation and practice; no job, salary or certification outcome is guaranteed.</p>
</div></div></footer>
{floater(p)}
<a class="fab" href="{WHATSAPP}" rel="noopener" target="_blank" aria-label="Chat on WhatsApp">{WA_SVG}<span>WhatsApp</span></a>"""


# ------------------------------------------------------------------ Structured data
ORG_ID = BASE + "#organization"
SITE_ID = BASE + "#website"
PERSON_ID = BASE + "pavan-babu-gandla.html#person"


def org_node():
    return {"@type": "Organization", "@id": ORG_ID, "name": BRAND, "url": BASE,
            "logo": BASE + "assets/logo-512.png", "email": EMAIL, "telephone": PHONE_E164,
            "sameAs": [LINKEDIN_COMPANY, YOUTUBE],
            "founder": {"@id": PERSON_ID},
            "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "telephone": PHONE_E164, "email": EMAIL, "availableLanguage": ["en"]},
            "knowsAbout": ["Adobe Experience Platform", "Real-Time CDP", "Adobe Journey Optimizer", "Customer Journey Analytics",
                           "Adobe Web SDK", "Customer data platforms", "Data engineering", "Agentic AI", "Model Context Protocol"]}


def jsonld(p):
    url = abs_url(p["path"])
    graph = []
    if p["path"] == "index.html":
        graph.append(org_node())
        graph.append({"@type": "WebSite", "@id": SITE_ID, "url": BASE, "name": BRAND, "publisher": {"@id": ORG_ID}, "inLanguage": "en"})
    if p["path"] == "pavan-babu-gandla.html":
        graph.append({"@type": "Person", "@id": PERSON_ID, "name": "Pavan Babu Gandla", "jobTitle": "Digital Transformation & MarTech Leader",
                      "worksFor": {"@id": ORG_ID}, "url": url, "sameAs": [LINKEDIN_PERSON, PORTFOLIO],
                      "knowsAbout": ["Adobe Experience Platform", "Real-Time CDP", "Adobe Journey Optimizer", "Customer Journey Analytics", "Enterprise architecture", "Agentic AI"]})
    if p["path"] == "about-us.html":
        graph.append(org_node())
        graph.append({"@type": "Person", "@id": PERSON_ID, "name": "Pavan Babu Gandla", "jobTitle": "Digital Transformation & MarTech Leader",
                      "worksFor": {"@id": ORG_ID}, "url": PORTFOLIO, "sameAs": [LINKEDIN_PERSON, PORTFOLIO]})
    page_type = {"Article": "WebPage", "HowTo": "WebPage", "Service": "WebPage", "Course": "WebPage"}.get(p["schema"], p["schema"])
    page = {"@type": page_type, "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["desc"],
            "isPartOf": {"@id": SITE_ID}, "inLanguage": "en", "dateModified": TODAY,
            "breadcrumb": {"@id": url + "#breadcrumb"}, "publisher": {"@id": ORG_ID}}
    if p["schema"] == "ProfilePage":
        page["mainEntity"] = {"@id": PERSON_ID}
    if p["schema"] == "FAQPage":
        page["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]
    graph.append(page)
    if p["schema"] in ("Article", "HowTo"):
        art = {"@type": "Article", "@id": url + "#article", "headline": p["h1"][:110], "description": p["desc"], "mainEntityOfPage": {"@id": url + "#webpage"},
               "author": {"@id": ORG_ID}, "publisher": {"@id": ORG_ID}, "dateModified": TODAY, "datePublished": p.get("date", TODAY), "inLanguage": "en",
               "image": BASE + "assets/og-image.png", "keywords": ", ".join(p.get("keywords", []))}
        graph.append(art)
    if p["schema"] == "HowTo" and p.get("steps"):
        graph.append({"@type": "HowTo", "@id": url + "#howto", "name": p["h1"], "description": p["answer"],
                      "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t, "url": f"{url}#step-{i+1}"} for i, (n, t) in enumerate(p["steps"])]})
    if p["schema"] == "Service":
        graph.append({"@type": "Service", "@id": url + "#service", "name": p["h1"], "serviceType": p.get("service_type", p["h1"]),
                      "description": p["answer"], "provider": {"@id": ORG_ID}, "url": url,
                      "areaServed": "Worldwide", "availableChannel": {"@type": "ServiceChannel", "serviceUrl": BASE + "contact-us.html"}})
    if p.get("event"):
        ev = p["event"]
        graph.append({"@type": "EducationEvent", "@id": url + "#event", "name": ev["name"], "description": p["answer"],
                      "startDate": ev["start"], "endDate": ev["end"], "eventStatus": "https://schema.org/EventScheduled",
                      "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
                      "location": {"@type": "VirtualLocation", "url": url}, "organizer": {"@id": ORG_ID}, "url": url,
                      **({"offers": {"@type": "Offer", "price": str(ev["price"]), "priceCurrency": "INR", "availability": "https://schema.org/InStock", "url": url, "validFrom": TODAY}} if ev.get("price") else {})})
    if p["schema"] == "Course":
        graph.append({"@type": "Course", "@id": url + "#course", "name": p.get("course_name", "Adobe MarTech + Agentic AI Career Accelerator"),
                      "description": p["answer"], "provider": {"@id": ORG_ID}, "url": url, "inLanguage": "en",
                      "teaches": ["Adobe Experience Platform", "Real-Time CDP", "Adobe Journey Optimizer", "Customer Journey Analytics", "Adobe Web SDK", "Agentic AI and MCP"],
                      "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": "P90D"},
                      **({"offers": {"@type": "Offer", "price": str(p["price_inr"]), "priceCurrency": "INR", "category": "Paid", "availability": "https://schema.org/InStock", "url": url}} if p.get("price_inr") else {})})
    graph.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": label, "item": abs_url(path)} for i, (path, label) in enumerate(crumbs(p))]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))


# ------------------------------------------------------------------ Analytics (consent-first)
GSV = re.sub(r"[^A-Za-z0-9_-]", "", str(_load("settings.json").get("google_site_verification", "")))


def analytics_head():
    """Consent Mode v2 defaults to denied; the banner in site.js updates consent. Tags load only when IDs are configured."""
    if not (GA4_ID or GTM_ID):
        return ""
    s = ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
         "gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500});"
         "try{var c=localStorage.getItem('i360_consent');if(c==='granted'){gtag('consent','update',{analytics_storage:'granted'});}}catch(e){}</script>\n")
    if GTM_ID:
        s += ("<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],"
              "j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);"
              f"}})(window,document,'script','dataLayer','{GTM_ID}');</script>\n")
    if GA4_ID:
        s += (f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>\n'
              f"<script>gtag('js',new Date());gtag('config','{GA4_ID}');</script>\n")
    return s


def gtm_noscript():
    if not GTM_ID:
        return ""
    return (f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" '
            'style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>\n')


FEEDS = [("rss.xml", "All guides, case studies and use cases"), ("feeds/case-studies.xml", "Case studies"),
         ("feeds/guides.xml", "Guides and student questions"), ("feeds/use-cases.xml", "Use cases"), ("feeds/academy.xml", "Academy")]


# ------------------------------------------------------------------ Page
def head(p, robots="index,follow,max-image-preview:large,max-snippet:-1", canonical=True, asset_prefix=None):
    a = (lambda n: asset_prefix + n + ("?v=" + asset_version(n) if n.endswith((".css", ".js")) else "")) if asset_prefix else (lambda n: asset(n, p["path"]))
    url = abs_url(p["path"])
    kw = f'<meta name="keywords" content="{e(", ".join(p.get("keywords", [])))}">' if p.get("keywords") else ""
    can = f'<link rel="canonical" href="{url}">' if canonical else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
{('<meta name="google-site-verification" content="' + GSV + '">') if GSV else ""}
<title>{e(p['title'])}</title>
<meta name="description" content="{e(p['desc'])}">
{kw}
<meta name="robots" content="{robots}">
{can}
<meta name="author" content="{BRAND}">
<meta name="theme-color" content="#0b1730">
<meta property="og:type" content="{'website' if p['path'] == 'index.html' else 'article'}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(p['title'])}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/og-image.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{BRAND} — Adobe MarTech consulting and training">
<meta property="og:locale" content="en_IN">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(p['title'])}">
<meta name="twitter:description" content="{e(p['desc'])}">
<meta name="twitter:image" content="{BASE}assets/og-image.png">
<link rel="icon" href="{a('favicon.svg')}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{a('logo-512.png')}">
<link rel="sitemap" type="application/xml" href="{BASE}sitemap.xml">
<link rel="alternate" type="application/rss+xml" title="{BRAND} - guides and case studies" href="{BASE}rss.xml">
{analytics_head()}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="{a('site.css')}">
<script type="application/ld+json">{jsonld(p) if canonical else '{}'}</script>
</head>"""


def fill(content, p):
    content = content.replace("@@SERVICE_CARDS@@", service_cards(p["path"])).replace("@@CONTACT_FORM@@", contact_block(p))
    if "@@LP_FORM@@" in content:
        content = content.replace("@@LP_FORM@@", form_html(p))
    if "@@TESTIMONIALS@@" in content:
        content = content.replace("@@TESTIMONIALS@@", testimonials_html())
    if "@@TESTIMONIAL_FORM@@" in content:
        content = content.replace("@@TESTIMONIAL_FORM@@", testimonial_form(p))
    if "@@SITEMAP@@" in content:
        content = content.replace("@@SITEMAP@@", sitemap_html(p))
    if "@@FEEDS@@" in content:
        content = content.replace("@@FEEDS@@", '<div class="link-pills">' + "".join(f'<a href="{BASE}{f}">{t} (RSS)</a>' for f, t in FEEDS) + f'<a href="{BASE}sitemap.xml">XML sitemap</a><a href="{BASE}llms.txt">llms.txt</a></div>')
    if "@@SOURCES@@" in content:
        content = content.replace("@@SOURCES@@", sources_html())
    if "@@TOPIC_LIST@@" in content:
        content = content.replace("@@TOPIC_LIST@@", topic_list(p))
    return content


def testimonials_html():
    if not TESTIMONIALS:
        return ('<div class="card"><p><strong>We are collecting verified reviews.</strong> We publish a review only after confirming the person attended a program or worked with us, and with their written permission. '
                'Until then this section stays empty rather than showing anything we cannot verify. Learners and clients can add a review using the form below.</p></div>')
    cards = "".join(
        f'<figure class="card quote"><blockquote><p>{e(t["quote"])}</p></blockquote><figcaption><strong>{e(t["name"])}</strong>'
        f'{" &middot; " + e(t["role"]) if t.get("role") else ""}{" &middot; " + e(t["program"]) if t.get("program") else ""}</figcaption></figure>' for t in TESTIMONIALS)
    return f'<div class="grid-3">{cards}</div>'


def testimonial_form(p):
    fid = "t"
    def f(name, label, typ="text", req=True, auto=""):
        r = ' required aria-required="true"' if req else ""
        star = ' <span class="req" aria-hidden="true">*</span>' if req else ' <span class="muted small">(optional)</span>'
        ac = f' autocomplete="{auto}"' if auto else ""
        return (f'<div class="field"><label for="{fid}-{name}">{label}{star}</label><input id="{fid}-{name}" name="{name}" type="{typ}"{ac}{r} aria-describedby="{fid}-{name}-error">'
                f'<span class="error" id="{fid}-{name}-error" aria-live="polite"></span></div>')
    return f"""<div class="form-card"><form class="form js-validate" action="{FORM_ACTION}" method="POST">
<input type="hidden" name="_subject" value="New review submission for the {BRAND} website">
<input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="{BASE}thank-you.html"><input type="hidden" name="form_type" value="testimonial">
<input type="hidden" name="source_page" value="{abs_url(p['path'])}">
<div class="hp" aria-hidden="true"><label for="{fid}-honey">Leave this field empty</label><input id="{fid}-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
<div class="form-grid">{f("name", "Name as it should appear", auto="name")}{f("email", "Email (not published)", "email", auto="email")}
{f("program", "Program or engagement")}{f("role", "Role and company", req=False, auto="organization-title")}
<div class="field full"><label for="{fid}-review">Your review <span class="req" aria-hidden="true">*</span></label><textarea id="{fid}-review" name="review" required aria-required="true" minlength="30" aria-describedby="{fid}-review-error"></textarea><span class="error" id="{fid}-review-error" aria-live="polite"></span></div>
<div class="field full"><div class="consent"><input id="{fid}-consent" name="publish_permission" type="checkbox" value="yes" required aria-required="true" aria-describedby="{fid}-consent-error" data-msg-required="Please confirm permission to publish.">
<label for="{fid}-consent" style="font-weight:500">I give {BRAND} permission to publish this review with my name and role, and I understand it will be verified first and can be removed on request.</label></div><span class="error" id="{fid}-consent-error" aria-live="polite"></span></div></div>
<div class="cta-row"><button class="btn btn-primary" type="submit">Submit review</button></div><p class="form-status" role="status" aria-live="polite"></p></form></div>"""


def sitemap_html(p):
    groups = {}
    for x in PAGES:
        seg = x["path"].split("/")[0] if "/" in x["path"] else "main"
        groups.setdefault(seg, []).append(x)
    names = {"main": "Main pages", "services": "Services", "solutions": "Solutions", "case-studies": "Case studies", "use-cases": "Use cases",
             "adobe-experience-platform": "AEP guides", "guides": "Guides and answers", "learn": "Learning hubs", "academy": "Academy",
             "training": "Training", "stacks": "MarTech stacks", "lp": "Get started", "topics": "Topics"}
    out = []
    for seg, items in groups.items():
        lis = "".join(f'<li><a href="{rel(x["path"], p["path"])}">{e(x["h1"])}</a></li>' for x in items)
        out.append(f'<div class="card"><h3>{names.get(seg, seg.title())}</h3><ul>{lis}</ul></div>')
    return f'<div class="grid-2 sitemap-grid">{"".join(out)}</div>'


def sources_html():
    if not os.path.exists(SOURCES_FILE):
        return ""
    data = json.load(open(SOURCES_FILE, encoding="utf-8"))
    cats = {}
    for x in data:
        cats.setdefault(x["category"], []).append(x)
    out = []
    for c, items in sorted(cats.items()):
        lis = "".join(f'<li><a href="{e(x["website"])}" rel="noopener nofollow" target="_blank">{e(x["source"])}</a> &middot; <a href="{e(x["rss_url"])}" rel="noopener nofollow" target="_blank">RSS</a></li>' for x in items)
        out.append(f'<div class="card"><h3>{e(c)}</h3><ul>{lis}</ul></div>')
    return '<p class="small muted">Third-party sources are listed for research; we are not affiliated with them.</p><div class="grid-3">' + "".join(out) + "</div>"


def page_terms(x):
    return (" " + " ".join([x["title"], x["h1"], x["desc"], " ".join(x.get("keywords", [])), x["path"].replace("-", " ").replace("/", " ")]) + " ").lower()


def topic_list(p):
    terms = p["topic_terms"]
    hits = [x for x in PAGES if x["path"] != p["path"] and not x["path"].startswith(("topics/", "lp/")) and x["path"] not in LEGAL_PATHS
            and x["path"] not in ("sitemap.html", "feeds.html") and any(t in page_terms(x) for t in terms)]
    cards = "".join(f'<a class="card link-card" href="{rel(x["path"], p["path"])}"><span class="tag">{e(x.get("category") or x["kicker"].split(" ·")[0])}</span><h3>{e(x["h1"])}</h3><p>{e(x["desc"])}</p></a>' for x in hits)
    return f'<p class="muted">{len(hits)} pages</p><div class="grid-2">{cards}</div>'


def body(p):
    sections = p.get("sections", [])
    toc = ""
    sec_html = []
    for sec in sections:
        title, content = sec[0], sec[1]
        content = fill(content, p)
        sec_html.append(f'<section aria-labelledby="{slug(title)}"><h2 id="{slug(title)}">{e(title)}</h2>{content}</section>')
    if p.get("steps"):
        steps = "".join(f'<li id="step-{i+1}"><strong>{e(n)}</strong> &mdash; {e(t)}</li>' for i, (n, t) in enumerate(p["steps"]))
        sec_html.insert(0, f'<section aria-labelledby="steps"><h2 id="steps">Step-by-step implementation</h2><ol class="steps">{steps}</ol></section>')
    titles = (["Step-by-step implementation"] if p.get("steps") else []) + [s[0] for s in sections]
    wide = p["path"] in ("index.html", "contact-us.html", "services/index.html")
    if len(titles) >= 3 and not wide:
        toc = '<aside class="toc" aria-label="On this page"><h2>On this page</h2><ol>' + "".join(
            f'<li><a href="#{"steps" if t == "Step-by-step implementation" else slug(t)}">{e(t)}</a></li>' for t in titles) + (
            '<li><a href="#faq">FAQ</a></li>' if p.get("faqs") and p["schema"] != "FAQPage" else "") + "</ol></aside>"
    sources = ""
    if p.get("sources"):
        sources = '<aside class="sources" aria-label="Sources"><h2>Sources and further reading</h2><ul>' + "".join(
            f'<li><a href="{u}" rel="noopener" target="_blank">{e(t)}</a></li>' for t, u in p["sources"]) + "</ul></aside>"
    updated = f'<p class="updated">Last updated: <time datetime="{TODAY}">{dt.date.fromisoformat(TODAY).strftime("%-d %B %Y")}</time></p>' if p["schema"] in ("Article", "HowTo") else ""
    prose_cls = "" if wide else "prose"
    notice = f'<p class="note">{e(p["notice"])}</p>' if p.get("notice") else ""
    if p.get("bands"):
        bands = []
        for sec in sections:
            title, content = sec[0], sec[1]
            style = sec[2] if len(sec) > 2 else "plain"
            eyebrow = sec[3] if len(sec) > 3 else ""
            content = fill(content, p)
            eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
            bands.append(f'<section class="band band-{style}" aria-labelledby="{slug(title)}"><div class="wrap"><div class="band-head">{eb}<h2 id="{slug(title)}">{e(title)}</h2></div>{content}</div></section>')
        faq = faq_html(p)
        if faq:
            bands.append(f'<section class="band band-plain"><div class="wrap narrow">{faq}</div></section>')
        main_html = f"""<main id="main">
{hero(p)}
<div class="wrap answer-wrap"><div class="answer" role="note"><strong>Quick answer</strong><p>{e(p['answer'])}</p></div>{notice}</div>
{''.join(bands)}
{related_html(p)}
{cta_band(p)}
</main>"""
        return f"""<body>
{header(p)}
{normalise_links(main_html)}
{footer(p)}
<script src="{asset('site.js', p['path'])}" defer></script>
</body>
</html>
"""
    main_html = f"""<main id="main">
{hero(p)}
<div class="section"><div class="wrap">
<div class="answer" role="note"><strong>Quick answer</strong><p>{e(p['answer'])}</p></div>{notice}
</div>
<div class="wrap" style="margin-top:36px"><div class="layout{' has-toc' if toc else ''}">
<article class="{prose_cls}">
{''.join(sec_html)}
{faq_html(p)}
{sources}
{updated}
</article>
{toc}
</div></div></div>
{related_html(p)}
{cta_band(p)}
</main>"""
    return f"""<body>
{header(p)}
{normalise_links(main_html)}
{footer(p)}
<script src="{asset('site.js', p['path'])}" defer></script>
</body>
</html>
"""


def render(p):
    return head(p) + "\n" + body(p)


def simple_page(path, title, h1, text, robots, links_html):
    """404 and thank-you pages: absolute asset URLs because 404 can be served at any depth."""
    p = dict(path=path, title=title, desc=text, h1=h1, kicker=BRAND, answer=text, schema="WebPage", keywords=[], sections=[], faqs=[])
    h = head(p, robots=robots, canonical=False, asset_prefix=BASE + "assets/")
    hdr = re.sub(r'href="(?!https?:|#|mailto:)([^"]*)"', lambda m: f'href="{urljoin(BASE, m.group(1))}"', header(p))
    ftr = re.sub(r'href="(?!https?:|#|mailto:)([^"]*)"', lambda m: f'href="{urljoin(BASE, m.group(1))}"', footer(p))
    return f"""{h}
<body>{hdr}
<main id="main"><div class="hero"><div class="wrap"><span class="kicker">{BRAND}</span><h1>{e(h1)}</h1><p class="lede">{e(text)}</p>
<div class="cta-row">{links_html}</div></div></div></main>
{ftr}
<script src="{BASE}assets/site.js?v={asset_version('site.js')}" defer></script></body></html>
"""


# ------------------------------------------------------------------ Build + validate
def write(rel_path, content):
    full = os.path.join(OUT, rel_path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(content)


def validate():
    errors = []
    seen = {}
    for key in ("title", "desc", "h1"):
        seen = {}
        for p in PAGES:
            if p[key] in seen:
                errors.append(f"duplicate {key}: {p['path']} and {seen[p[key]]}")
            seen[p[key]] = p["path"]
    for p in PAGES:
        if not (70 <= len(p["desc"]) <= 160):
            errors.append(f"{p['path']}: description length {len(p['desc'])}")
        if len(p["title"]) > 65:
            errors.append(f"{p['path']}: title length {len(p['title'])}")
        words = len(p["answer"].split())
        if not (25 <= words <= 90):
            errors.append(f"{p['path']}: quick answer {words} words")
    built = set()
    for dirpath, _, files in os.walk(OUT):
        for f in files:
            built.add(os.path.relpath(os.path.join(dirpath, f), OUT).replace(os.sep, "/"))
    inbound = {p["path"]: 0 for p in PAGES}
    for p in PAGES:
        doc = open(os.path.join(OUT, p["path"]), encoding="utf-8").read()
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', doc, re.S):
            try:
                json.loads(block)
            except ValueError as ex:
                errors.append(f"{p['path']}: invalid JSON-LD {ex}")
        if doc.count("<h1") != 1:
            errors.append(f"{p['path']}: expected exactly one h1")
        for href in re.findall(r'href="([^"]+)"', doc):
            if href.startswith(("http:", "https:", "mailto:", "tel:", "#")):
                continue
            target = os.path.normpath(os.path.join(os.path.dirname(p["path"]), href.split("#")[0].split("?")[0]))
            target = target.replace(os.sep, "/")
            if href.endswith("/") or href in ("./", "../"):
                target = (target + "/index.html").lstrip("./") if target != "." else "index.html"
            if target.startswith("./"):
                target = target[2:]
            if target not in built:
                errors.append(f"{p['path']}: broken link {href} -> {target}")
            elif target in inbound and target != p["path"]:
                inbound[target] += 1
    for path, n in inbound.items():
        if n == 0 and path != "index.html":
            errors.append(f"orphan page: {path}")
    return errors


def rss_doc(title, link_path, items):
    def item(x):
        d = dt.date.fromisoformat(x.get("date", TODAY))
        pub = dt.datetime(d.year, d.month, d.day, 9, 0, tzinfo=dt.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")
        cat = x.get("category") or "Guides"
        return (f"<item><title>{e(x['h1'])}</title><link>{e(abs_url(x['path']))}</link><guid isPermaLink=\"true\">{e(abs_url(x['path']))}</guid>"
                f"<category>{e(cat)}</category><pubDate>{pub}</pubDate><description>{e(x['answer'])}</description></item>")
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel>'
            f"<title>{e(title)}</title><link>{e(BASE)}</link><description>{e(title)} from {BRAND}: Adobe MarTech, AEP, AJO, CJA and Agentic AI.</description>"
            f'<language>en</language><atom:link href="{e(BASE + link_path)}" rel="self" type="application/rss+xml"/>'
            + "".join(item(x) for x in items) + "</channel></rss>\n")


def write_feeds():
    def cat(x):
        if x.get("category"):
            return x["category"]
        if x["path"].startswith(("guides/", "adobe-experience-platform/")):
            return "Guides"
        if x["path"].startswith(("academy/", "training/")):
            return "Academy"
        return None
    editorial = [x for x in PAGES if cat(x) and x["schema"] in ("Article", "HowTo", "FAQPage", "Course", "WebPage", "CollectionPage") and not x["path"].endswith("index.html")]
    for x in editorial:
        x.setdefault("category", cat(x))
    write("rss.xml", rss_doc(f"{BRAND} - guides, case studies and use cases", "rss.xml", editorial))
    for fpath, title in FEEDS[1:]:
        name = {"feeds/case-studies.xml": "Case studies", "feeds/guides.xml": "Guides", "feeds/use-cases.xml": "Use cases", "feeds/academy.xml": "Academy"}[fpath]
        write(fpath, rss_doc(f"{BRAND} - {title.lower()}", fpath, [x for x in editorial if x["category"] == name]))


def dashboard_html():
    """Read-only SEO/content inventory for the site owner (noindex; robots-disallowed)."""
    inbound = {x["path"]: 0 for x in PAGES}
    for x in PAGES:
        doc = open(os.path.join(OUT, x["path"]), encoding="utf-8").read()
        for href in set(re.findall(r'href="([^"#?]+)', doc)):
            if href.startswith(("http", "mailto", "tel")):
                continue
            t = os.path.normpath(os.path.join(os.path.dirname(x["path"]), href)).replace(os.sep, "/")
            if href.endswith("/"):
                t = (t + "/index.html") if t != "." else "index.html"
            if t in inbound and t != x["path"]:
                inbound[t] += 1
    rows, sections = [], {}
    for x in PAGES:
        seg = x["path"].split("/")[0] if "/" in x["path"] else "main"
        sections[seg] = sections.get(seg, 0) + 1
        text = " ".join(str(sec[1]) for sec in x.get("sections", [])) + " " + x["answer"] + " " + " ".join(q + " " + a for q, a in x.get("faqs", [])) + " " + " ".join(n + " " + t for n, t in x.get("steps", []))
        words = len(re.sub(r"<[^>]+>", " ", text).split())
        flags = []
        if len(x["title"]) > 60: flags.append("long title")
        if len(x["desc"]) < 110: flags.append("short desc")
        if words < 200 and x["schema"] not in ("CollectionPage",) and not x.get("landing") and x["path"] not in LEGAL_PATHS and x["path"] not in ("sitemap.html", "feeds.html"): flags.append("thin")
        if inbound[x["path"]] < 2 and x["path"] != "index.html": flags.append("few links")
        rows.append(f'<tr><td><a href="../{url_path(x["path"])}">{e(x["path"])}</a></td><td>{e(x["schema"])}</td><td>{len(x["title"])}</td><td>{len(x["desc"])}</td>'
                    f'<td>{words}</td><td>{len(x.get("keywords", []))}</td><td>{inbound[x["path"]]}</td><td>{", ".join(flags) or "ok"}</td></tr>')
    tiles = "".join(f'<div class="kpi"><b>{n}</b><span>{e(k)}</span></div>' for k, n in sorted(sections.items(), key=lambda kv: -kv[1]))
    tracking = "configured" if (GA4_ID or GTM_ID) else "not configured - add IDs in Admin &rarr; Site settings"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>Site dashboard | {BRAND}</title>
<link rel="stylesheet" href="../assets/site.css?v={asset_version('site.css')}"></head><body class="dash">
<main class="wrap" id="main"><h1>Site dashboard</h1><p class="muted">Built {TODAY} &middot; base {e(BASE)} &middot; analytics: {tracking}</p>
<p class="cta-row"><a class="btn btn-primary" href="./">Edit content (Admin)</a><a class="btn btn-ghost" href="https://search.google.com/search-console" rel="noopener" target="_blank">Search Console</a>
<a class="btn btn-ghost" href="https://www.bing.com/webmasters" rel="noopener" target="_blank">Bing Webmaster</a><a class="btn btn-ghost" href="https://analytics.google.com/" rel="noopener" target="_blank">Google Analytics</a>
<a class="btn btn-ghost" href="https://pagespeed.web.dev/analysis?url={e(BASE)}" rel="noopener" target="_blank">PageSpeed</a></p>
<div class="kpis"><div class="kpi"><b>{len(PAGES)}</b><span>indexable pages</span></div><div class="kpi"><b>{len(TESTIMONIALS)}</b><span>verified reviews</span></div>{tiles}</div>
<h2>Content inventory</h2><div class="table-wrap"><table class="dash-table"><thead><tr><th>Path</th><th>Schema</th><th>Title</th><th>Desc</th><th>Words</th><th>Keywords</th><th>Inbound</th><th>Flags</th></tr></thead>
<tbody>{"".join(rows)}</tbody></table></div></main></body></html>"""


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    for p in PAGES:
        write(p["path"], render(p))
    write("404.html", simple_page("404.html", f"Page not found | {BRAND}", "Page not found",
                                  "The page you are looking for has moved or does not exist.", "noindex,follow",
                                  f'<a class="btn btn-primary" href="{BASE}">Go to the homepage</a><a class="btn btn-ghost" href="{BASE}adobe-experience-platform/">Browse AEP guides</a>'))
    write("thank-you.html", simple_page("thank-you.html", f"Thank you | {BRAND}", "Thank you — we have your enquiry",
                                        "We will reply by your preferred contact method, usually within two business days.", "noindex,nofollow",
                                        f'<a class="btn btn-primary" href="{BASE}">Back to the homepage</a><a class="btn btn-ghost" href="{BASE}adobe-experience-platform/">Read the AEP guides</a>'))
    _bl = "".join(f'<a class="btn btn-primary" href="{BASE}assets/brochures/Infinate360-brochure-{k}.pdf" download>{t}</a> ' for k, t in [("learners", "Learners brochure (PDF)"), ("corporate-training", "Corporate training brochure (PDF)"), ("enterprise-coe", "Enterprise and CoE brochure (PDF)"), ("c2c-partners", "C2C brochure (PDF)"), ("master", "Full 15-page brochure (PDF)")]) + f'<a class="btn btn-ghost" href="{BASE}assets/brochures/Infinate360-brochure-master.pptx" download>Full brochure (PowerPoint)</a>'
    write("brochure-download.html", simple_page("brochure-download.html", f"Download your brochure | {BRAND}", "Thank you: download your brochure",
                                                "Choose the brochure that matches your need. We will follow up on your requirement using the details you shared.", "noindex,nofollow", _bl))
    urls = "\n".join(f"  <url><loc>{e(abs_url(p['path']))}</loc>{('<lastmod>' + str(p['date']) + '</lastmod>') if p.get('date') else ''}</url>"
                     for p in PAGES)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    _dis = "Disallow: /thank-you.html\nDisallow: /admin/\nDisallow: /api/\n"
    _bots = [("Search engines", ["Googlebot", "Bingbot", "DuckDuckBot", "Applebot"]),
             ("AI search and answer engines", ["OAI-SearchBot", "ChatGPT-User", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User", "DuckAssistBot"]),
             ("AI training and model crawlers", ["GPTBot", "ClaudeBot", "Google-Extended", "Applebot-Extended", "Amazonbot", "Meta-ExternalAgent", "CCBot", "cohere-ai", "Bytespider"])]
    _rb = "# Public pages are open to search engines and AI crawlers. Private paths stay disallowed.\n# robots.txt is not access control.\n\n"
    for _lbl, _names in _bots:
        _rb += f"# {_lbl}\n" + "".join(f"User-agent: {n}\n" for n in _names) + f"Allow: /\n{_dis}\n"
    _rb += f"# Everyone else\nUser-agent: *\nAllow: /\n{_dis}\nSitemap: {BASE}sitemap.xml\n"
    write("robots.txt", _rb)
    write_feeds()
    if os.path.isdir(os.path.join(ROOT, "admin")):
        shutil.copytree(os.path.join(ROOT, "admin"), os.path.join(OUT, "admin"), dirs_exist_ok=True)
    write("admin/dashboard.html", dashboard_html())
    llms = [f"# {BRAND}", "", "> Adobe MarTech consulting, corporate training and a Tech Academy career accelerator focused on Adobe Experience Platform (AEP), Real-Time CDP, Adobe Journey Optimizer, Customer Journey Analytics, Web SDK, data engineering and Agentic AI.", "",
            f"Contact: {EMAIL} | WhatsApp {PHONE_DISPLAY}", "", "## Pages", ""]
    llms += [f"- [{p['title']}]({abs_url(p['path'])}): {p['answer']}" for p in PAGES if p["path"] != "privacy-policy.html"]
    write("llms.txt", "\n".join(llms) + "\n")
    write(".nojekyll", "")
    errors = validate()
    print(f"Built {len(PAGES)} pages + 404 + thank-you into {OUT}")
    print(f"Sitemap URLs: {len(PAGES)}")
    if errors:
        print("VALIDATION ERRORS:")
        for err in errors:
            print(" -", err)
        sys.exit(1)
    print("Validation passed: unique titles/descriptions/H1s, valid JSON-LD, no broken internal links, no orphan pages.")


if __name__ == "__main__":
    main()
