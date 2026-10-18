"""Topic search index: every tracked search phrase grouped by theme, each group linking to the page that answers it.
Phrases live in content/search-keywords.txt. Share links are user-initiated (no auto-posting)."""
import html as _h, os as _o, re as _re, urllib.parse as _u
e = _h.escape
_ROOT = _o.path.dirname(_o.path.dirname(_o.path.abspath(__file__)))
KEYWORDS = [l.strip() for l in open(_o.path.join(_ROOT, "content", "search-keywords.txt"), encoding="utf-8") if l.strip()]
HOST = "https://infiante360techacademy.com/"
PATH = "search-topics.html"

CLUSTERS = [  # (id, title, regex, blurb, [(label, href)])
 ("ai", "Agentic AI, MCP and generative AI", r"agentic|mcp|model context|\bai\b|llm|genai|generative|machine learning|\bml\b|rag\b|retrieval|prompt|copilot|langchain|claude|openai|vector|multi-agent|n8n|zapier|workflow automation|propensity",
  "Using AI agents and MCP safely with enterprise MarTech.", [("Agentic AI & MCP services", "services/agentic-ai-mcp.html"), ("What is MCP?", "guides/what-is-mcp.html"), ("Agentic AI & MCP workshop", "lp/agentic-ai-mcp-workshop.html")]),
 ("data", "Data engineering and cloud", r"kafka|snowflake|databricks|bigquery|spark|\betl\b|\belt\b|pipeline|data engineer|\bsql\b|python|airflow|dbt|warehouse|lake|gcp|azure|aws|cloud|dagster|prefect|streaming|data integration|data modeling|data quality|observability",
  "Pipelines, warehouses and platform data flows behind customer data platforms.", [("Data engineering for CDPs", "services/data-engineering.html"), ("AEP data ingestion", "adobe-experience-platform/data-ingestion.html")]),
 ("sdk", "Web SDK, tags and data collection", r"web sdk|alloy|\btags?\b|tag manager|launch|tracking|datastream|data collection|server-side|data layer|acdl|mobile sdk|ecid|debugging|event",
  "Collecting clean event data from web and mobile.", [("Web SDK & Adobe Tags", "services/web-sdk-adobe-tags.html"), ("AEP data ingestion", "adobe-experience-platform/data-ingestion.html")]),
 ("cja", "Analytics and Customer Journey Analytics", r"\bcja\b|customer journey analytics|analytics|attribution|measurement|report|analysis workspace|funnel|fallout|cohort|data views|calculated metrics|segment builder",
  "Measuring journeys and behaviour across channels.", [("Customer Journey Analytics", "services/customer-journey-analytics.html"), ("CJA vs Adobe Analytics", "guides/cja-vs-adobe-analytics.html")]),
 ("gov", "Privacy, consent and data governance", r"governance|consent|privacy|gdpr|dpdp|ccpa|compliance|data usage|labels|clean room|security|first-party|zero-party|third-party|onetrust",
  "Governing customer data and consent in a CDP.", [("AEP architecture", "adobe-experience-platform/architecture.html"), ("AEP implementation guide", "adobe-experience-platform/implementation-guide.html")]),
 ("pers", "Personalisation and decisioning", r"personali|offer|decision|next best|omnichannel|cross-channel|a/b|experiment|recommendation|engagement|marketing automation|email|sms|push|loyalty|churn|retention|lifecycle|customer lifetime",
  "Real-time offers and next-best-action design.", [("Real-time use-case library", "use-cases/real-time-use-case-library.html"), ("Journey Optimizer", "services/adobe-journey-optimizer.html")]),
 ("ajo", "Journey Optimizer, campaigns and B2B", r"\bajo\b|journey optimizer|journey|orchestrat|campaign|marketo|\btarget\b|b2b|account-based|\babm\b|\blead|magento",
  "Orchestrating journeys and campaigns on a unified profile.", [("Adobe Journey Optimizer", "services/adobe-journey-optimizer.html"), ("AJO best practices", "guides/ajo-implementation-best-practices.html"), ("Marketo Engage & AEP", "guides/marketo-engage-aep.html")]),
 ("cdp", "Real-Time CDP, identity and audiences", r"rtcdp|real.time cdp|\bcdp\b|customer data platform|identity|profile|unification|activation|customer 360|audience|segment|destination",
  "Unifying identities and activating audiences.", [("Real-Time CDP services", "services/real-time-cdp.html"), ("Identity Service", "adobe-experience-platform/identity-service.html"), ("Segmentation & audiences", "adobe-experience-platform/segmentation-audiences.html"), ("AEP vs Real-Time CDP", "guides/aep-vs-real-time-cdp.html")]),
 ("aep", "Adobe Experience Platform", r"\baep\b|experience platform|xdm|schema|dataset|ingestion|adobe experience|\baem\b|commerce|workfront|sandbox|adobe",
  "Schemas, datasets, ingestion and architecture on Adobe Experience Platform.", [("AEP guides", "adobe-experience-platform/"), ("XDM schemas", "adobe-experience-platform/xdm-schemas.html"), ("AEP consulting", "services/aep-consulting.html")]),
 ("career", "Training, courses and careers", r"course|training|certif|career|interview|job|salary|learn|bootcamp|academy|class|tutorial|fresher|placement|skill|exam|resume|roadmap",
  "Learning paths, labs and interview preparation. No job, certification or outcome is guaranteed.", [("Academy", "academy/"), ("Career transition", "training/career-transition.html"), ("AEP interview questions", "adobe-experience-platform/interview-questions.html"), ("Free demo sessions", "academy/videos.html")]),
 ("biz", "Consulting, implementation and hiring", r"consult|hire|staff|contract|c2c|freelanc|implementation|partner|agency|vendor|service|solution|enterprise|architect|strategy|transformation|martech",
  "Advisory, delivery and specialist capacity for enterprises.", [("All services", "services/"), ("Staff augmentation", "services/staff-augmentation.html"), ("AEP architecture review", "lp/aep-architecture-review.html"), ("Corporate training", "training/corporate-training.html")]),
 ("other", "More Adobe MarTech topics", r".", "Other topics we cover.", [("Explore learning", "learn/"), ("Site map", "sitemap.html")]),
]
_groups = {c[0]: [] for c in CLUSTERS}
for k in KEYWORDS:
    for cid, _t, rx, _b, _l in CLUSTERS:
        if _re.search(rx, k.lower()):
            _groups[cid].append(k); break

def _share():
    url = lambda src: f"{HOST}{PATH}?utm_source={src}&utm_medium=social&utm_campaign=topic-index"
    t = "Adobe Experience Platform, Real-Time CDP, AJO, CJA and Agentic AI: topic index and free demo"
    q = _u.quote
    items = [("LinkedIn", f"https://www.linkedin.com/sharing/share-offsite/?url={q(url('linkedin'))}"),
             ("Reddit", f"https://www.reddit.com/submit?url={q(url('reddit'))}&title={q(t)}"),
             ("Facebook", f"https://www.facebook.com/sharer/sharer.php?u={q(url('facebook'))}"),
             ("X", f"https://twitter.com/intent/tweet?url={q(url('x'))}&text={q(t)}"),
             ("WhatsApp", f"https://wa.me/?text={q(t + ' ' + url('whatsapp'))}")]
    return '<div class="link-pills">' + "".join(f'<a href="{e(h)}" rel="noopener nofollow" target="_blank">Share on {n}</a>' for n, h in items) + '</div><p class="small muted">Each button opens that network with a tagged link so you can post it yourself. Nothing is posted automatically. Please follow each community&rsquo;s rules, and post in a subreddit only where self-promotion is allowed.</p>'

def _cluster(cid, title, blurb, links):
    ks = _groups[cid]
    if not ks: return None
    pills = '<div class="link-pills">' + "".join(f'<a href="{h}">{e(l)}</a>' for l, h in links) + '</div>'
    return (f"{title} ({len(ks)})", f"<p>{e(blurb)}</p>{pills}<p class=\"small\">{' &middot; '.join(e(k) for k in ks)}</p>", "plain", "Topics")

PAGE = dict(
    path=PATH,
    title="Adobe MarTech Topic Index: AEP, CDP, AJO, CJA & AI Searches",
    desc="Find the Infinite360 page for any Adobe MarTech search: AEP, Real-Time CDP, Journey Optimizer, CJA, Web SDK, data engineering, Agentic AI, training and careers.",
    h1="Adobe MarTech topic index: find the page for what you are searching",
    nav="Topic index", kicker="Find your topic",
    keywords=["adobe experience platform topics", "adobe martech topics", "aep real-time cdp ajo cja", "martech search topics", "adobe martech learning"],
    answer="This index groups the Adobe MarTech topics people search for, from Adobe Experience Platform and Real-Time CDP to Journey Optimizer, Customer Journey Analytics, Web SDK, data engineering, Agentic AI, training and careers. Each group links to the Infinite360 page that covers it, so you can go straight to the guide, service or free demo you need.",
    schema="CollectionPage",
    sections=[("Start here", '<p>Pick the group closest to your search, then open the linked guide or service. New to Adobe MarTech? Start with the free demo sessions or the AEP guides. For a conversation, call or WhatsApp <a href="https://wa.me/918296893895">+91 82968 93895</a>.</p><div class="link-pills"><a href="academy/videos.html">Free demo sessions</a><a href="adobe-experience-platform/">AEP guides</a><a href="academy/">Academy</a><a href="services/">Services</a></div>', "plain", "Orientation"),
              ("Share this index", _share(), "alt", "Share")]
             + [s for s in (_cluster(c[0], c[1], c[3], c[4]) for c in CLUSTERS) if s],
    faqs=[("Is this a list of services?", "No. It is a topic index. Each group links to the guide or service page that covers those searches."),
          ("Do you guarantee jobs or certification?", "No. Training outcomes depend on the learner. We do not guarantee jobs, interviews or certification, and Infinite360 is independent of Adobe.")],
    related=["learn/index.html", "adobe-experience-platform/index.html", "academy/index.html", "services/index.html"],
)
TOPIC_INDEX = [PAGE]
