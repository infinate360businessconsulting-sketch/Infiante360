"""Infinite360 Tech Academy: hub, program catalog, single-tool courses, videos, resources, roles guide.

Prices: ₹60,000 career accelerator (stated by owner). Leadership and customised programs ₹1,00,000
(from the owner-supplied reference catalog) — flagged for confirmation in the hand-off.
"""
import html

REG_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfKeY_33fgEBKYskgG2shgRcYLvHx50ES_KqrULMKromsE3mg/viewform?usp=header"
CAREER_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSctdT6hTSgIeBxok4KgCKC4EISTB8l-S3rKV1NK8SedwGvMZQ/viewform?usp=sharing&ouid=117017541254219120366"
SIGNUP = "https://techacademy.infinate360.in/signup"
CHALLENGE = "https://techacademy.infinate360.in/testapp/255893"
DEMO_AEP = "https://techacademy.infinate360.in/static/media/appx_dl.html?digest=eyJhY3RfY29kZSI6MSwiYWN0X2RhdGEiOjIxNDY4LCJleGFtX3VybCI6Ii90ZXN0cy8xNDc5L2FlcC1yZWFsd29ybGQtdXNlLWNhc2UtdGVzdC1zZXJpZXMifQ=="
DEMO_AI = "https://techacademy.infinate360.in/static/media/appx_dl.html?digest=eyJhY3RfY29kZSI6MSwiYWN0X2RhdGEiOjIxMTIwLCJleGFtX3VybCI6Ii90ZXN0cy8xNDc5L2FlcC1yZWFsd29ybGQtdXNlLWNhc2UtdGVzdC1zZXJpZXMifQ=="
CASE_PACK = "https://drive.google.com/file/d/11hkOjfB7a8z7V8ZJJVOyX9mSSlUxvMxQ/view?usp=sharing"
YOUTUBE = "https://www.youtube.com/@Infiante360TechAcademy"
MTJ = {
    "academy/programs/aep-ajo-cja-foundation-advanced.html": "https://martechjobs.io/courses/adobe-aep-ajo-cja/",
    "academy/programs/executive-architecture-leadership.html": "https://martechjobs.io/courses/cxo-hive-executive-architecture/",
    "academy/programs/live-customised-program.html": "https://martechjobs.io/courses/live-customised-martech-program/",
}

PROGRAMS = [
    # path (relative to site root), name, category, level, format, price label, price_inr, summary
    ("training/index.html", "Adobe MarTech + Agentic AI Career Accelerator", "Adobe Experience Cloud", "Beginner to intermediate", "Live online · 90 days", "₹60,000", 60000,
     "The flagship live program: AEP, RTCDP, AJO, CJA, Web SDK and Agentic AI through labs, enterprise-style projects and interview preparation."),
    ("academy/programs/aep-ajo-cja-foundation-advanced.html", "Adobe AEP, Journey Optimizer & CJA: Foundation + Advanced Architecture", "Adobe Experience Cloud", "Intermediate", "Recorded · self-paced", "₹60,000", 60000,
     "Learn AEP, AJO and CJA, then the MarTech and CDP architecture behind enterprise implementations."),
    ("academy/programs/executive-architecture-leadership.html", "CXO Hive: Executive & Architecture Program", "MarTech leadership", "Leaders & architects", "Live · with post-program support", "₹1,00,000", 100000,
     "For CXOs, technology leaders and enterprise architects building MarTech and AI capability at scale."),
    ("academy/programs/live-customised-program.html", "Live Customised MarTech Program", "Any MarTech stack", "All levels", "Live · individuals or teams", "₹1,00,000", 100000,
     "A live program built around your role, business requirements and technology landscape."),
    ("academy/programs/agentic-ai-mcp-track.html", "Agentic AI & MCP for MarTech", "Agentic AI", "Intermediate", "Live · weekend track", "On request", None,
     "Agents, governed tools, MCP architecture and an enterprise marketing copilot capstone."),
]

COURSES = [
    ("academy/courses/rtcdp-training.html", "Real-Time CDP", "RTCDP"),
    ("academy/courses/ajo-training.html", "Journey Optimizer", "AJO"),
    ("academy/courses/cja-training.html", "Customer Journey Analytics", "CJA"),
    ("academy/courses/adobe-analytics-training.html", "Adobe Analytics", "AA"),
    ("academy/courses/web-sdk-training.html", "Web SDK & Tags", "SDK"),
    ("academy/courses/agentic-ai-training.html", "Agentic AI for MarTech", "AI"),
    ("academy/courses/aep-certification-prep.html", "AEP certification preparation", "CERT"),
]

VIDEOS = [
    ("GdPW5lYdmdA", "Adobe MarTech + Agentic AI Career Accelerator", "Featured session", None),
    ("AXzbSBsItAc", "AEP · RTCDP · AJO · CJA", "Adobe Experience Cloud", 4853),
    ("inBQ8nDiChM", "Enterprise MarTech Implementation", "MarTech mastery", None),
    ("RBEtErJatu4", "Program Onboarding Session", "Onboarding", 48),
    ("fkGj9cWoYlY", "Adobe MarTech Demo Session", "Free demo", 79),
    ("71iiZ5imujA", "MarTech Expert Insights", "Expert session", None),
]


def rel_from(depth):
    return "../" * depth


def program_cards(depth, exclude=None):
    up = rel_from(depth)
    out = []
    for path, name, cat, level, fmt, price, _, summary in PROGRAMS:
        if path == exclude:
            continue
        href = up + path.replace("index.html", "")
        out.append(f'<a class="program-card link-card" href="{href}"><span class="tag" style="background:var(--red-50);color:var(--red-700)">{html.escape(cat)}</span>'
                   f'<h3>{html.escape(name)}</h3><p>{html.escape(summary)}</p>'
                   f'<div class="meta"><span>{html.escape(level)}</span><span>{html.escape(fmt)}</span></div>'
                   f'<div class="program-foot"><span class="program-price">{price}</span><span class="more">View program &rarr;</span></div></a>')
    return '<div class="programs">' + "".join(out) + "</div>"


def course_tiles(depth, exclude=None):
    up = rel_from(depth)
    return '<div class="tiles">' + "".join(
        f'<a class="tile link-card" href="{up}{p}"><span class="abbr">{a}</span><h3>{n} training</h3><p>Focused, single-tool learning path.</p></a>'
        for p, n, a in COURSES if p != exclude) + "</div>"


def video_grid():
    cards = []
    for vid, title, label, start in VIDEOS:
        q = f"?start={start}&rel=0&modestbranding=1" if start else "?rel=0&modestbranding=1"
        watch = f"https://www.youtube.com/watch?v={vid}" + (f"&t={start}s" if start else "")
        cards.append(f'<figure class="video-card"><button class="video-facade" type="button" data-embed="https://www.youtube-nocookie.com/embed/{vid}{q}" '
                     f'aria-label="Play video: {html.escape(title)}" style="background-image:url(https://i.ytimg.com/vi/{vid}/hqdefault.jpg)"><span class="play" aria-hidden="true"></span></button>'
                     f'<figcaption><span class="tag" style="background:var(--blue-50);color:var(--blue)">{label}</span><strong>{html.escape(title)}</strong>'
                     f'<a href="{watch}" rel="noopener" target="_blank">Watch on YouTube</a></figcaption></figure>')
    return '<div class="video-grid">' + "".join(cards) + "</div>"


def program_page(path, name, title, desc, kicker, keywords, answer, level, fmt, price, price_inr, includes, learn, modules, audience, extra_sections, faqs, related):
    depth = path.count("/")
    up = rel_from(depth)
    price_block = f"""<div class="price-card">
<div><div class="price">{price}<small>{'one-time program fee' if price_inr else 'pricing shared on request'}</small></div>
<div class="meta" style="margin-top:14px"><span>{level}</span><span>{fmt}</span></div>
<p class="cta-row" style="margin-top:20px"><a class="btn btn-primary" href="#enquire">Request details</a> <a class="btn btn-ghost" href="{REG_FORM}" rel="noopener" target="_blank">Register</a></p></div>
<ul class="checklist">{''.join(f'<li>{i}</li>' for i in includes)}</ul></div>
{f'<p>This program is also listed on <a href="{MTJ[path]}" rel="noopener" target="_blank">MarTechJobs.io</a>.</p>' if path in MTJ else ''}
<p class="small muted">No payment is taken on this site. Outcomes depend on participation and practice; no job, salary or certification outcome is guaranteed.</p>"""
    sections = [
        ("Program at a glance", price_block, "plain", "Fees &amp; format"),
        ("What you'll learn", '<ul class="checklist cols-2">' + "".join(f"<li>{l}</li>" for l in learn) + "</ul>", "alt", "Outcomes"),
        ("Course content", "".join(f'<details class="qa"><summary>{m} <span class="muted small">· {len(t)} topics</span></summary><ul>' + "".join(f"<li>{x}</li>" for x in t) + "</ul></details>" for m, t in modules), "plain", "Curriculum"),
        ("Who this program is for", '<div class="grid-3">' + "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in audience) + "</div>", "alt", "Audience"),
    ] + extra_sections + [
        ("Explore other programs", program_cards(depth, exclude=path), "plain", "More programs"),
    ]
    return dict(path=path, title=title, desc=desc, h1=name, kicker=kicker, keywords=keywords, answer=answer,
                schema="Course", course_name=name, price_inr=price_inr, bands=True, program=True,
                hero_cta=("Request details", "#enquire"), sections=sections, faqs=faqs, related=related)


def course_page(path, tool, abbr, title, desc, keywords, answer, modules, projects, prereq, guide_links, faqs):
    depth = path.count("/")
    up = rel_from(depth)
    sections = [
        ("Curriculum", "".join(f'<details class="qa"><summary>Module {i+1}: {m}</summary><ul>' + "".join(f"<li>{x}</li>" for x in t) + "</ul></details>" for i, (m, t) in enumerate(modules)), "plain", "What you'll learn"),
        ("Hands-on projects", '<div class="grid-2">' + "".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in projects) + "</div>", "alt", "Practice"),
        ("Prerequisites and format", f"""<ul class="checklist">{''.join(f'<li>{x}</li>' for x in prereq)}</ul>
<p>{tool} training is available as a focused single-tool path, as part of the <a href="{up}training/">career accelerator (₹60,000)</a>, or inside a <a href="{up}academy/programs/live-customised-program.html">customised program</a>. Ask for single-tool pricing using the form below.</p>""", "plain", "Format"),
        ("Free reading before you start", "<ul>" + "".join(f'<li><a href="{up}{p}">{l}</a></li>' for p, l in guide_links) + "</ul>", "alt", "Guides"),
        ("Other single-tool courses", course_tiles(depth, exclude=path), "plain", "Courses"),
    ]
    return dict(path=path, title=title, desc=desc, h1=f"{tool} training", kicker=f"Academy · {abbr}", keywords=keywords, answer=answer,
                schema="Course", course_name=f"{tool} training", bands=True, program=True, hero_cta=("Request details", "#enquire"),
                sections=sections, faqs=faqs, related=["academy/index.html", "training/index.html", "academy/free-resources.html"])


ACADEMY = [
    dict(
        path="academy/index.html",
        nav="Academy",
        bands=True,
        title="Infinite360 Tech Academy: Adobe MarTech & AI Programs",
        desc="Infinite360 Tech Academy: Adobe MarTech career accelerator, leadership, customised and Agentic AI programs, single-tool courses, demos and free resources.",
        h1="Infinite360 Tech Academy",
        kicker="Learn · Build · Transform · Lead",
        lede="Hands-on Adobe MarTech, customer data and Agentic AI programs taught by a working MarTech architect — built around the platforms enterprises use.",
        keywords=["infinite360 tech academy", "adobe martech courses", "aep course india", "martech training programs", "agentic ai course", "adobe experience cloud training"],
        answer="Infinite360 Tech Academy offers live and customised programs in Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Web SDK and Agentic AI. Programs range from the ₹60,000 live career accelerator and recorded Foundation + Advanced Architecture course to ₹1,00,000 leadership and customised programs, plus single-tool courses, free demo sessions and resources.",
        schema="CollectionPage",
        hero_cta=("Browse programs", "#programs"),
        sections=[
            ("Programs", program_cards(1), "plain", "Course catalog"),
            ("Workshops and bootcamps", '<p class="lead">New to AEP? Start with a short, live, hands-on format.</p><div class="grid-3"><a class="card link-card" href="aep-launchpad-bootcamp.html"><span class="tag" style="background:var(--red-50);color:var(--red-700)">Sun 11 Oct · ₹3,000</span><h3>AEP Launchpad bootcamp</h3><p>3 hours, 6–9 PM IST, with a free ₹3,500 test series.</p></a><a class="card link-card" href="aep-foundations-batch.html"><span class="tag" style="background:var(--blue-50);color:var(--blue)">From 15 Oct · 8 AM IST</span><h3>Live Foundations batch</h3><p>Two weeks, Monday–Friday, beginner-friendly.</p></a><a class="card link-card" href="workshops.html"><span class="tag" style="background:var(--green-50);color:var(--green)">Every Friday</span><h3>Hands-on workshops</h3><p>One AEP skill per session.</p></a></div>', "dark", "Start here"),
            ("Single-tool courses", '<p class="lead">Only need one platform? Each course is a focused path you can take alone or as part of a program.</p>' + course_tiles(1), "alt", "Learn one tool"),
            ("Why learn with Infinite360", """<div class="grid-3">
<div class="card"><h3>Practical learning</h3><p>Hands-on labs, enterprise-style projects and capstone implementations.</p></div>
<div class="card"><h3>Architect-led teaching</h3><p>Taught from enterprise delivery experience: why designs work, not just where to click.</p></div>
<div class="card"><h3>Troubleshooting first</h3><p>Identity failures, streaming delays and audience mismatches &mdash; the problems real projects hit.</p></div>
<div class="card"><h3>Career acceleration</h3><p>Career mapping, resume and LinkedIn positioning and interview preparation.</p></div>
<div class="card"><h3>Agentic AI included</h3><p>AI agents, MCP and governed automation alongside the Adobe stack.</p></div>
<div class="card"><h3>Teams welcome</h3><p>Customised and corporate programs built around your platforms and roles.</p></div>
</div>""", "dark", "Why us"),
            ("Your learning path", """<div class="timeline">
<div class="step"><h3>Learn</h3><p>Concepts and the AEP data flow.</p></div>
<div class="step"><h3>Build</h3><p>Labs: schemas, ingestion, identity, audiences.</p></div>
<div class="step"><h3>Implement</h3><p>Enterprise-style projects and troubleshooting.</p></div>
<div class="step"><h3>Deploy</h3><p>Capstone, portfolio and interview preparation.</p></div>
</div>
<p style="margin-top:18px">Moving from another role? See <a href="../training/career-transition.html">career transition paths</a> and <a href="martech-roles.html">MarTech roles explained</a>.</p>""", "plain", "How it works"),
            ("Watch before you decide", f'<p class="lead">Free sessions from the Infinite360 Tech Academy channel.</p><p><a class="btn btn-primary" href="videos.html">Watch demo sessions</a> <a class="btn btn-ghost" href="{YOUTUBE}" rel="noopener" target="_blank">YouTube channel</a></p>', "alt", "Demo sessions"),
            ("Free resources", f"""<div class="grid-3">
<a class="card link-card" href="{SIGNUP}" rel="noopener" target="_blank"><h3>Free signup + challenge</h3><p>Join the academy platform and try the challenge.</p></a>
<a class="card link-card" href="{CHALLENGE}" rel="noopener" target="_blank"><h3>AEP Architect Challenge</h3><p>Test your architecture thinking with scenario questions.</p></a>
<a class="card link-card" href="{CAREER_FORM}" rel="noopener" target="_blank"><h3>Free career mapping</h3><p>Map your current skills to Adobe MarTech roles.</p></a>
</div><p><a href="free-resources.html">All free resources &rarr;</a></p>""", "plain", "Start free"),
        ],
        faqs=[
            ("How much does the career accelerator cost?", "The Adobe MarTech + Agentic AI Career Accelerator fee is ₹60,000. Leadership and customised programs are ₹1,00,000 per program; corporate programs are quoted per engagement."),
            ("Are programs live or recorded?", "The career accelerator, leadership and customised programs are delivered live online. Demo sessions are available free on YouTube."),
            ("Can I learn just one tool?", "Yes. Single-tool courses are available for RTCDP, AJO, CJA, Adobe Analytics, Web SDK, Agentic AI and AEP certification preparation; ask for single-tool pricing."),
            ("Is job placement guaranteed?", "No. Programs include career guidance and interview preparation, but no job, salary or certification outcome is guaranteed."),
        ],
        related=["training/index.html", "training/corporate-training.html", "academy/martech-roles.html"],
    ),
    program_page(
        "academy/programs/aep-ajo-cja-foundation-advanced.html",
        "Adobe AEP, Journey Optimizer & CJA: Foundation + Advanced Architecture",
        "AEP, AJO & CJA Course: Foundation + Advanced Architecture",
        "Recorded course: Adobe Experience Platform, Journey Optimizer and CJA, then enterprise MarTech and CDP architecture. ₹60,000 one-time.",
        "Academy · Adobe Experience Cloud",
        ["aep ajo cja course", "adobe experience platform recorded course", "aep architecture course", "cdp architecture training", "adobe journey optimizer course"],
        "Adobe AEP, Journey Optimizer & CJA: Foundation + Advanced Architecture is a recorded, self-paced course. It teaches Adobe Experience Platform, Journey Optimizer and Customer Journey Analytics, then the MarTech and customer data platform architecture behind enterprise implementations. The fee is ₹60,000 one-time and includes recorded lessons, a test series, ERD resources and an e-library.",
        "Intermediate", "Recorded · learn at your own pace", "₹60,000", 60000,
        ["Recorded video lessons", "Test series", "ERD resources", "E-library", "Additional learning material"],
        ["Adobe Experience Platform (AEP)", "Adobe Journey Optimizer (AJO)", "Customer Journey Analytics (CJA)", "Digital and MarTech architecture", "Enterprise implementation patterns", "Customer Data Platform architecture", "AI and data-driven customer experience"],
        [("Foundation MarTech Series", ["Adobe Experience Platform (AEP)", "Adobe Journey Optimizer (AJO)", "Customer Journey Analytics (CJA)"]),
         ("Advanced Digital Architecture Program", ["Digital and MarTech architecture", "Enterprise implementation patterns", "Customer Data Platform architecture", "AI and data-driven customer experience"])],
        [("Aspiring Adobe practitioners", "People who want to work on AEP, Journey Optimizer or CJA projects."), ("Marketing ops &amp; MarTech engineers", "Professionals moving into the Adobe stack."), ("Self-paced learners", "Anyone who prefers recorded lessons over live batches.")],
        [("Prefer live learning?", '<p>The <a href="../../training/">Career Accelerator</a> covers the same platforms live over 90 days with projects and interview preparation, also at ₹60,000.</p>', "alt", "Compare")],
        [("Is this course live or recorded?", "Recorded and self-paced. For live sessions, choose the Career Accelerator or the Live Customised MarTech Program."),
         ("Can I buy a single tool only?", "Yes. Choose 'A single tool at a lower price' in the form and tell us which tool, for example AEP only.")],
        ["training/index.html", "academy/courses/aep-certification-prep.html", "adobe-experience-platform/index.html"],
    ),
    program_page(
        "academy/programs/executive-architecture-leadership.html",
        "CXO Hive: Executive & Architecture Program",
        "CXO Hive: Executive & Architecture Program | MarTech & AI CoE",
        "Live program for CXOs, technology leaders and enterprise architects: MarTech and AI centres of excellence, CDP strategy and governance. ₹1,00,000.",
        "Academy · MarTech leadership",
        ["martech leadership program", "martech center of excellence", "cdp strategy course", "enterprise architecture martech", "agentic ai strategy for leaders"],
        "CXO Hive: Executive & Architecture Program is a live program for CXOs, technology leaders and enterprise architects who are setting up MarTech and AI capability at scale. It covers centres of excellence, GCC-to-global capability models, agentic AI strategy, CDP strategy, enterprise architecture and governance. The fee is ₹1,00,000.",
        "Leaders &amp; architects", "Live · post-program support", "₹1,00,000", 100000,
        ["Live sessions", "One month of post-program support", "Architecture and governance templates", "Capability-model workshop"],
        ["Set up a MarTech / AI Centre of Excellence", "GCC-to-global capability transformation", "AI and agentic AI strategy", "Customer Data Platform strategy", "Enterprise architecture and governance", "Reusable capabilities and global delivery models"],
        [("Strategy", ["Setting up a MarTech / AI Centre of Excellence", "AI and agentic AI strategy", "Customer Data Platform strategy"]),
         ("Architecture and delivery", ["Enterprise architecture and governance", "GCC-to-global capability transformation", "Reusable capabilities and global delivery models"])],
        [("CXOs", "C-level executives sponsoring MarTech, data and AI transformation."), ("Technology leaders", "Heads of MarTech, data, digital and engineering."), ("Enterprise architects", "Architects designing platforms and operating models.")],
        [("How the program runs", """<div class="timeline"><div class="step"><h3>Assess</h3><p>Current capability and ambition.</p></div><div class="step"><h3>Design</h3><p>CoE, architecture and governance model.</p></div><div class="step"><h3>Plan</h3><p>Roadmap and delivery model.</p></div><div class="step"><h3>Support</h3><p>One month of follow-up guidance.</p></div></div>""", "dark", "Format")],
        [("Is this program technical?", "It is architecture- and strategy-led. Technical depth is matched to the audience, with enough detail for architects to act on.")],
        ["services/martech-strategy-advisory.html", "academy/programs/live-customised-program.html", "pavan-babu-gandla.html"],
    ),
    program_page(
        "academy/programs/live-customised-program.html",
        "Live Customised MarTech Program",
        "Live Customised MarTech Program for Individuals & Teams",
        "A live MarTech program built around your role, business requirements and technology landscape — for individuals or teams. ₹1,00,000 per program.",
        "Academy · Any MarTech stack",
        ["customised martech training", "custom adobe training", "martech team training", "tailored aep course", "live martech program"],
        "The Live Customised MarTech Program is built around your role, your business requirements and your technology landscape. It suits individuals who want a program fitted to their job and organisations training a team. Content can cover Adobe Experience Cloud and other MarTech stacks. The fee is ₹1,00,000 per program.",
        "All levels", "Live · individuals or teams", "₹1,00,000", 100000,
        ["Live sessions", "Content customised to you or your team", "Use cases from your own environment where permitted", "Assessment and capstone"],
        ["Content built around your role", "Fitted to your business requirements", "Matched to your technology landscape", "Hands-on labs on the tools you use", "A capstone tied to a real use case", "Next-step plan for continued learning"],
        [("Discovery", ["Role and skills assessment", "Business requirements and use cases", "Technology landscape review"]),
         ("Delivery", ["Live sessions and labs", "Project work and reviews", "Capstone and next-step plan"])],
        [("Organisations", "Teams that need training matched to their platforms."), ("Individuals", "Professionals who want a program fitted to their role."), ("Consultancies &amp; SIs", "Delivery teams preparing for client projects.")],
        [],
        [("Can the program cover non-Adobe tools?", "Yes. The customised program can cover other MarTech stacks; tell us which platforms you use in the enquiry form.")],
        ["training/corporate-training.html", "academy/programs/executive-architecture-leadership.html", "academy/index.html"],
    ),
    program_page(
        "academy/programs/agentic-ai-mcp-track.html",
        "Agentic AI & MCP for MarTech",
        "Agentic AI & MCP for MarTech: Live Weekend Track",
        "Live weekend track on Agentic AI and MCP for MarTech: agents, governed tools, AEP data context, journey intelligence and an AI copilot capstone.",
        "Academy · Agentic AI",
        ["agentic ai course", "mcp training", "ai agents for marketing", "agentic ai martech training", "enterprise ai copilot course"],
        "The Agentic AI & MCP track teaches how AI agents use tools and enterprise context safely. It covers agent foundations, responsible AI, Model Context Protocol architecture, developer authentication concepts, using AEP datasets and identity as context, audience and journey intelligence, and an enterprise marketing copilot capstone. Pricing is shared on request.",
        "Intermediate", "Live · weekend track", "On request", None,
        ["Live weekend sessions", "Hands-on agent and MCP labs", "Governance and responsible-AI checklists", "Enterprise copilot capstone"],
        ["Agentic AI foundations and patterns", "Responsible AI and governance", "MCP architecture: servers, tools and resources", "Developer console and OAuth concepts", "Using AEP datasets and identity as context", "Audience and journey intelligence with AI"],
        [("Foundations", ["Agents, tools and planning", "Responsible AI and guardrails", "MCP architecture"]),
         ("Enterprise context", ["Authentication and access concepts", "AEP datasets, identity and profiles as context", "Audience and journey intelligence"]),
         ("Capstone", ["Design a governed marketing copilot", "Evaluation and human approval", "Presentation and review"])],
        [("MarTech engineers", "Engineers adding AI automation to marketing workflows."), ("Architects", "Architects designing governed AI on enterprise data."), ("Analysts &amp; consultants", "Professionals exploring AI-assisted analysis and operations.")],
        [("Related reading", '<p>Start with <a href="../../guides/what-is-mcp.html">What is MCP?</a> and <a href="../../services/agentic-ai-mcp.html">Agentic AI &amp; MCP consulting</a>. Product capabilities change quickly; we verify every integration against current documentation.</p>', "alt", "Guides")],
        [("Do I need to code?", "Basic scripting helps. Labs provide starter code, and the capstone can be design-led for non-developers.")],
        ["guides/what-is-mcp.html", "academy/courses/agentic-ai-training.html", "training/index.html"],
    ),
    course_page("academy/courses/rtcdp-training.html", "Real-Time CDP", "RTCDP",
        "Real-Time CDP Training: Audiences, Activation & Customer 360",
        "Adobe Real-Time CDP training: profiles, identity, audience design, destinations, activation QA and governance with hands-on projects.",
        ["rtcdp training", "real-time cdp course", "rtcdp implementation training", "adobe cdp training", "rtcdp consultant course"],
        "Real-Time CDP training teaches how Adobe's customer data platform turns AEP profiles into activated audiences. You learn identity and profile foundations, audience design across batch, streaming and edge evaluation, destination setup, consent and governance, and activation QA, finishing with an end-to-end activation project.",
        [("Profiles and identity", ["Real-Time Customer Profile and merge policies", "Identity namespaces and graphs", "Customer 360 design"]),
         ("Audience design", ["Batch, streaming and edge evaluation", "Segment Builder patterns", "Validating audience sizes"]),
         ("Activation", ["Streaming and batch destinations", "Mapping identities and attributes", "Consent and data usage policies"]),
         ("Operations", ["Activation QA and reconciliation", "Monitoring dataflows", "Troubleshooting common issues"])],
        [("Audience strategy", "Design lifecycle and suppression audiences for a retail brand."), ("Activation QA", "Activate an audience and reconcile counts with the destination.")],
        ["Basic understanding of marketing data", "Familiarity with AEP concepts helps (see the free AEP guide)"],
        [("adobe-experience-platform/segmentation-audiences.html", "AEP segments & audiences"), ("adobe-experience-platform/activation-destinations.html", "AEP activation"), ("guides/aep-vs-real-time-cdp.html", "AEP vs Real-Time CDP")],
        [("Is RTCDP training different from AEP training?", "Yes. AEP training covers the data foundation; RTCDP training focuses on audiences and activation built on it.")]),
    course_page("academy/courses/ajo-training.html", "Journey Optimizer", "AJO",
        "Adobe Journey Optimizer (AJO) Training: Journeys & Decisioning",
        "Adobe Journey Optimizer training: event and audience journeys, channels, decisioning, suppression, frequency rules, testing and measurement.",
        ["ajo training", "adobe journey optimizer course", "ajo implementation training", "journey orchestration course", "ajo certification prep"],
        "Adobe Journey Optimizer training covers how to design, build, test and measure real-time journeys. You learn event and audience journeys, channel configuration, personalisation and decisioning, suppression and frequency rules, test profiles and journey reporting, and build an event-triggered journey end to end.",
        [("Foundations", ["How AJO uses AEP profiles and events", "Event vs audience journeys", "Channel surfaces"]),
         ("Journey design", ["Conditions, waits and paths", "Personalisation and content", "Decisioning and offers"]),
         ("Governance", ["Suppression and frequency rules", "Consent", "Approvals and testing"]),
         ("Measurement", ["Journey reporting", "CJA analysis", "Troubleshooting non-triggering journeys"])],
        [("Real-time transaction journey", "Streaming event to profile to AJO trigger to message."), ("Abandonment journey", "Cart abandonment with suppression after purchase.")],
        ["Basic marketing campaign knowledge", "Familiarity with AEP profiles and events"],
        [("services/adobe-journey-optimizer.html", "AJO consulting and journey design steps"), ("adobe-experience-platform/data-ingestion.html", "AEP data ingestion")],
        [("Why is my journey not triggering?", "Common causes are event configuration, datastream routing, identity, entry conditions and consent; the course covers each.")]),
    course_page("academy/courses/cja-training.html", "Customer Journey Analytics", "CJA",
        "CJA Training: Customer Journey Analytics Connections & Data Views",
        "Customer Journey Analytics training: connections, data views, Workspace, cross-channel analysis, attribution and migration from Adobe Analytics.",
        ["cja training", "customer journey analytics course", "cja implementation training", "cja dashboard course", "adobe analytics to cja"],
        "Customer Journey Analytics training teaches how to analyse AEP data across channels. You learn connections and person IDs, data view components and settings, Workspace analysis, cross-channel journeys and attribution, and migration from Adobe Analytics, finishing with an executive dashboard project.",
        [("Setup", ["Connections and datasets", "Person ID strategy", "Lookups and profile data"]),
         ("Data views", ["Components and settings", "Sessions and attribution", "Calculated metrics"]),
         ("Analysis", ["Workspace panels and visualisations", "Cross-channel journeys", "Flow and fallout"]),
         ("Migration", ["Adobe Analytics to CJA", "Web SDK collection", "Reporting continuity"])],
        [("Executive journey dashboard", "Build KPI storytelling across web, app and offline."), ("Missing dataset debug", "Trace why an AEP dataset is missing in CJA.")],
        ["Analytics or reporting experience", "Basic AEP dataset concepts"],
        [("guides/cja-vs-adobe-analytics.html", "CJA vs Adobe Analytics"), ("services/customer-journey-analytics.html", "CJA consulting")],
        [("Do I need Adobe Analytics experience?", "No, but it helps. The course explains Workspace from first principles.")]),
    course_page("academy/courses/adobe-analytics-training.html", "Adobe Analytics", "AA",
        "Adobe Analytics Training: Implementation, Tracking & Reporting",
        "Adobe Analytics training: measurement strategy, implementation and tracking with Tags and Web SDK, reporting in Workspace and validation.",
        ["adobe analytics training", "adobe analytics course", "adobe analytics implementation", "adobe analytics tracking", "workspace reporting course"],
        "Adobe Analytics training covers digital measurement from strategy to reporting. You learn solution design, variables and events, implementation with Adobe Tags and Web SDK, validation and debugging, and Workspace reporting, with a project that instruments and reports on a sample site.",
        [("Strategy", ["Measurement plans and KPIs", "Solution design references", "Data governance"]),
         ("Implementation", ["Variables, events and classifications", "Adobe Tags rules", "Web SDK collection"]),
         ("Validation", ["Debugging tools", "QA checklists", "Bot and invalid traffic considerations"]),
         ("Reporting", ["Workspace projects", "Segments and calculated metrics", "Stakeholder dashboards"])],
        [("Instrument a site", "Implement page, product and click tracking with validation."), ("Reporting pack", "Build a stakeholder Workspace with segments.")],
        ["Basic HTML and JavaScript awareness", "Interest in digital analytics"],
        [("services/web-sdk-adobe-tags.html", "Web SDK & Tags implementation"), ("guides/cja-vs-adobe-analytics.html", "CJA vs Adobe Analytics")],
        [("Is Adobe Analytics still relevant with CJA?", "Many organisations run Adobe Analytics today and migrate over time; understanding both is valuable.")]),
    course_page("academy/courses/web-sdk-training.html", "Web SDK & Tags", "SDK",
        "Adobe Web SDK Training: Data Layer, Datastreams & Edge Network",
        "Adobe Web SDK training: XDM data layers, datastreams, Adobe Tags, consent, Edge Network, event forwarding and end-to-end validation.",
        ["web sdk training", "adobe web sdk course", "alloy js training", "datastream setup course", "adobe tags training"],
        "Web SDK training teaches modern Adobe data collection. You learn XDM-aligned data layers, datastreams, deploying Web SDK through Adobe Tags, consent, the Edge Network and event forwarding, and how to validate events end to end into AEP datasets, Analytics and Target.",
        [("Foundations", ["Web SDK and the Edge Network", "XDM data layers", "Datastreams"]),
         ("Implementation", ["Adobe Tags extension setup", "Page view and interaction events", "Identity and ECID"]),
         ("Consent &amp; forwarding", ["Consent configuration", "Event forwarding patterns", "Server-side considerations"]),
         ("Validation", ["Debugging tools", "Dataset previews", "Migration from legacy libraries"])],
        [("Web SDK modernisation", "Data layer to Web SDK to datastream to AEP event flow."), ("Migration plan", "Plan a safe move from AppMeasurement with parallel running.")],
        ["HTML and JavaScript basics", "Access to a test site or sandbox (provided in labs)"],
        [("services/web-sdk-adobe-tags.html", "Web SDK implementation steps"), ("adobe-experience-platform/data-ingestion.html", "AEP data ingestion")],
        [("Does Web SDK replace AppMeasurement?", "It is designed to replace legacy libraries with one library; migrations should be planned to protect reporting.")]),
    course_page("academy/courses/agentic-ai-training.html", "Agentic AI for MarTech", "AI",
        "Agentic AI Training for MarTech: Agents, Tools & Governance",
        "Agentic AI training for MarTech professionals: AI agents, tool use, MCP, governance, evaluation and marketing workflow automation.",
        ["agentic ai training", "ai agents course", "ai for marketing technology", "mcp course", "ai workflow automation training"],
        "Agentic AI training for MarTech explains how AI agents plan and act through tools, and how to use them safely with customer data. You learn agent patterns, tool design, the Model Context Protocol, governance and human approval, evaluation, and practical marketing workflow automations.",
        [("Agents", ["What makes AI agentic", "Planning and tool use", "Failure modes"]),
         ("Tools &amp; MCP", ["Designing tools", "MCP servers and clients", "Least-privilege access"]),
         ("Governance", ["Human approval", "Logging and audit", "Personal data and consent"]),
         ("Applications", ["Audience and journey QA assistants", "Analytics question answering", "Content operations"])],
        [("Marketing assistant", "Agent with governed tools and customer context."), ("Evaluation set", "Measure an assistant's accuracy before rollout.")],
        ["Comfort with basic scripting or no-code automation", "Interest in marketing operations"],
        [("guides/what-is-mcp.html", "What is MCP?"), ("services/agentic-ai-mcp.html", "Agentic AI & MCP consulting")],
        [("Is this the same as the Agentic AI & MCP track?", "This is the focused single-tool course; the track adds AEP context and an enterprise copilot capstone.")]),
    course_page("academy/courses/aep-certification-prep.html", "AEP certification preparation", "CERT",
        "AEP Certification Preparation: Study Plan & Practice Scenarios",
        "Prepare for Adobe Experience Platform certification: exam-aligned study plan, scenario practice, weak-area review and hands-on reinforcement.",
        ["aep certification", "adobe experience platform certification prep", "aep exam preparation", "rtcdp certification", "adobe certification training"],
        "AEP certification preparation gives you a structured study plan, scenario-based practice and hands-on reinforcement of the topics Adobe certifications test. It is independent of Adobe; always check the current exam guide on Adobe's certification site, and no exam result is guaranteed.",
        [("Plan", ["Read the current exam guide", "Baseline self-assessment", "Study schedule"]),
         ("Core topics", ["Schemas, datasets and ingestion", "Identity and profiles", "Segmentation and activation"]),
         ("Practice", ["Scenario questions", "Troubleshooting cases", "Timed practice"]),
         ("Review", ["Weak-area review", "Hands-on reinforcement", "Exam-day checklist"])],
        [("Scenario bank", "Work through architecture and troubleshooting scenarios."), ("Lab reinforcement", "Rebuild weak areas hands-on in a sandbox.")],
        ["Working knowledge of AEP concepts", "Time for regular practice"],
        [("adobe-experience-platform/index.html", "The AEP guide"), ("adobe-experience-platform/interview-questions.html", "AEP interview questions")],
        [("Is this an official Adobe course?", "No. It is independent preparation. Adobe sets and administers its certifications.")]),
    dict(
        path="academy/videos.html",
        bands=True,
        title="Free Adobe MarTech Demo Sessions & Videos | Infinite360",
        desc="Watch free Infinite360 Tech Academy sessions: career accelerator overview, AEP, RTCDP, AJO and CJA, implementation, onboarding and expert insights.",
        h1="Free demo sessions",
        kicker="Academy · Watch",
        keywords=["aep training video", "adobe martech demo session", "free aep class", "infinite360 youtube", "adobe experience platform tutorial video"],
        answer="These free sessions from the Infinite360 Tech Academy YouTube channel show the teaching approach and implementation depth: a career accelerator overview, AEP, RTCDP, AJO and CJA sessions, enterprise implementation, onboarding, a demo class and expert insights. Videos load only when you press play.",
        schema="CollectionPage",
        hero_cta=("Visit the YouTube channel", YOUTUBE),
        sections=[("Sessions", video_grid(), "plain", "Watch"),
                  ("Ready for the next step?", f'<p class="cta-row"><a class="btn btn-light" href="../training/">Career accelerator · ₹60,000</a><a class="btn btn-ghost" style="color:#fff" href="index.html">All programs</a></p>', "dark", "Programs")],
        faqs=[],
        related=["academy/index.html", "academy/free-resources.html", "training/index.html"],
    ),
    dict(
        path="academy/free-resources.html",
        bands=True,
        title="Free Adobe MarTech Learning Resources | Infinite360 Academy",
        desc="Free Infinite360 Tech Academy resources: signup and challenge, AEP Architect Challenge, demo classes, case study pack, career mapping and AEP guides.",
        h1="Free learning resources",
        kicker="Academy · Start free",
        keywords=["free aep resources", "aep architect challenge", "free martech course", "aep case study pack", "free career mapping martech"],
        answer="Start free with the academy signup and challenge, the AEP Architect Challenge, AEP, AJO and CJA master-class demos, the Agentic AI demo class, the architecture case study pack, free career mapping, and the Infinite360 AEP guides.",
        schema="CollectionPage",
        sections=[("Try it free", f"""<div class="grid-3">
<a class="card link-card" href="{SIGNUP}" rel="noopener" target="_blank"><h3>Free signup + challenge</h3><p>Create an academy account and start the challenge.</p><span class="more">Sign up &rarr;</span></a>
<a class="card link-card" href="{CHALLENGE}" rel="noopener" target="_blank"><h3>AEP Architect Challenge</h3><p>Scenario questions that test architecture thinking.</p><span class="more">Take the challenge &rarr;</span></a>
<a class="card link-card" href="{DEMO_AEP}" rel="noopener" target="_blank"><h3>AEP, AJO &amp; CJA master classes</h3><p>Real-world use-case demo series.</p><span class="more">Watch demo &rarr;</span></a>
<a class="card link-card" href="{DEMO_AI}" rel="noopener" target="_blank"><h3>Agentic AI demo class</h3><p>AI agents, MCP and workflow automation.</p><span class="more">Watch demo &rarr;</span></a>
<a class="card link-card" href="{CASE_PACK}" rel="noopener" target="_blank"><h3>Architecture &amp; case study pack</h3><p>Programme material and architecture content.</p><span class="more">Open pack &rarr;</span></a>
<a class="card link-card" href="{CAREER_FORM}" rel="noopener" target="_blank"><h3>Free career mapping</h3><p>Map your skills to Adobe MarTech roles.</p><span class="more">Start mapping &rarr;</span></a>
</div>""", "plain", "Start here"),
                  ("Free guides on this site", """<div class="grid-3">
<a class="card link-card" href="../adobe-experience-platform/index.html"><h3>The AEP guide</h3><p>Schemas to activation.</p></a>
<a class="card link-card" href="../adobe-experience-platform/interview-questions.html"><h3>AEP interview questions</h3><p>Scenario-based answers.</p></a>
<a class="card link-card" href="../learn/index.html"><h3>Learning hubs</h3><p>AEP, Marketo, Agentic AI and more.</p></a>
</div>""", "alt", "Read")],
        faqs=[],
        related=["academy/videos.html", "academy/index.html", "learn/index.html"],
    ),
    dict(
        path="academy/martech-roles.html",
        bands=True,
        title="MarTech Roles Explained: Ops, RevOps, Engineering & Architecture",
        desc="What MarTech roles do — marketing operations, RevOps, MarTech engineer, CDP engineer, analytics, journey specialist and architect — and the skills each needs.",
        h1="MarTech roles explained",
        kicker="Academy · Careers",
        keywords=["martech roles", "marketing operations career", "martech engineer skills", "cdp engineer role", "martech architect career", "revops career"],
        answer="MarTech careers span marketing operations, revenue operations, MarTech and CDP engineering, analytics, journey and personalisation specialists, and solution architects. Each combines platform skills (such as Adobe, Salesforce, HubSpot or Marketo) with data, process and stakeholder skills; Adobe Experience Cloud adds specialised AEP, RTCDP, AJO and CJA roles.",
        schema="Article",
        sections=[("Common MarTech roles", """<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>What they do</th><th>Core skills</th></tr></thead><tbody>
<tr><td>Marketing operations</td><td>Run campaigns, data hygiene and automation platforms</td><td>Marketo/HubSpot, segmentation, QA, process</td></tr>
<tr><td>Revenue operations</td><td>Align marketing, sales and customer success data and process</td><td>CRM, lead routing, reporting, governance</td></tr>
<tr><td>MarTech engineer</td><td>Integrate and automate the marketing stack</td><td>APIs, scripting, data pipelines, tag management</td></tr>
<tr><td>CDP / AEP engineer</td><td>Model, ingest and govern customer data</td><td>XDM, ingestion, identity, SQL</td></tr>
<tr><td>Analytics specialist</td><td>Measure journeys and campaign impact</td><td>Adobe Analytics/CJA, GA, BI tools, statistics</td></tr>
<tr><td>Journey &amp; personalisation specialist</td><td>Design triggered journeys and tests</td><td>AJO, Target, experimentation, content</td></tr>
<tr><td>Solution architect</td><td>Design end-to-end platforms and governance</td><td>Architecture, identity strategy, security, stakeholder leadership</td></tr>
</tbody></table></div>""", "plain", "Roles"),
                  ("Skills employers look for", """<ul class="checklist cols-2">
<li>Hands-on platform experience, not just feature knowledge</li><li>Data modelling and SQL</li>
<li>Integration and API literacy</li><li>Consent, privacy and governance awareness</li>
<li>Troubleshooting and validation habits</li><li>Explaining technical design to business stakeholders</li></ul>
<p>Salaries vary widely by country, experience and platform depth; check current listings and salary surveys for your market.</p>""", "alt", "Skills"),
                  ("Build these skills", '<p class="cta-row"><a class="btn btn-light" href="../training/">Career accelerator</a><a class="btn btn-ghost" style="color:#fff" href="../training/career-transition.html">Career transition paths</a></p>', "dark", "Next step")],
        faqs=[("Which MarTech role pays the most?", "It depends on market and seniority. Architect and specialised platform roles often command a premium, but check current local listings rather than relying on general figures.")],
        related=["training/career-transition.html", "adobe-experience-platform/career-path.html", "academy/index.html"],
    ),
]
