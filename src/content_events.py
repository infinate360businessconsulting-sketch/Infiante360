"""Workshops, bootcamp landing page and live foundations batch (dates in IST).

Update EVENT_* constants when a new batch or bootcamp is announced.
"""
import html

REG_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfKeY_33fgEBKYskgG2shgRcYLvHx50ES_KqrULMKromsE3mg/viewform?usp=header"
WHATSAPP = "https://wa.me/918296893895"

BOOTCAMP = dict(name="AEP Launchpad: Foundations Bootcamp", date="Sunday, 11 October 2026", time="6:00 PM – 9:00 PM IST",
                start="2026-10-11T18:00:00+05:30", end="2026-10-11T21:00:00+05:30", price=3000, price_label="₹3,000")
BATCH = dict(name="Live AEP Foundations Batch", date="Starts Thursday, 15 October 2026", time="8:00 AM – 9:30 AM IST",
             start="2026-10-15T08:00:00+05:30", end="2026-10-28T09:30:00+05:30")

WORKSHOPS = [
    ("Fri 16 Oct", "Schema Sprint", "Design your first XDM model",
     "Classes, field groups and identity fields — model a retail customer and purchase event.",
     ["Profile vs ExperienceEvent classes", "Choosing standard field groups", "Marking identity fields", "Review: common modelling mistakes"]),
    ("Fri 23 Oct", "Data on the Move", "Ingestion basics lab",
     "Create a dataset, map a sample file with Data Prep and read batch errors like a pro.",
     ["Datasets from schemas", "Batch upload and mapping", "Reading failed records", "Batch vs streaming at a glance"]),
    ("Fri 30 Oct", "Who's Who", "Identity foundations lab",
     "Namespaces, primary identity and how identity graphs link known and anonymous data.",
     ["Namespaces and ECID", "Primary identity", "Viewing an identity graph", "Spotting shared identifiers"]),
    ("Fri 6 Nov", "One Customer View", "Real-Time Profile lab",
     "Enable data for Profile, inspect merged profiles and understand merge policies.",
     ["Profile-enabled schemas and datasets", "Profile fragments", "Merge policies", "Validating a sample profile"]),
    ("Fri 13 Nov", "Audience Studio", "Segmentation foundations",
     "Build and validate your first audiences with batch, streaming and edge evaluation.",
     ["Segment Builder basics", "Evaluation methods", "Estimating and validating size", "Naming and governance"]),
    ("Fri 20 Nov", "Go Live", "Activation and destinations basics",
     "Connect an audience to a destination and run the activation QA checklist.",
     ["How destinations work", "Mapping identities", "Consent and policy checks", "Reconciling counts"]),
]

BONUS = """<div class="bonus">
<span class="bonus-badge">Free bonus</span>
<h3>₹3,500 Interview &amp; Certification Test Series &mdash; free with your ₹3,000 bootcamp</h3>
<p>Every bootcamp attendee gets access to the Infinite360 interview preparation and certification practice question series, built to reinforce Adobe Experience Platform concepts and build interview and exam confidence.</p>
<ul class="checklist cols-2"><li>Scenario-based practice questions</li><li>Interview-style AEP questions</li><li>Covers schemas, identity, profiles and segmentation</li><li>Use alongside Adobe's official exam guide</li></ul>
<p class="small">Practice materials support preparation; they do not guarantee interview or official certification results.</p>
</div>"""


def ticket(ev, label, cta_href, cta_text, extra=""):
    return f"""<div class="ticket">
<span class="ticket-label">{label}</span>
<h3>{html.escape(ev['name'])}</h3>
<dl><div><dt>Date</dt><dd>{ev['date']}</dd></div><div><dt>Time</dt><dd>{ev['time']}</dd></div>
<div><dt>Format</dt><dd>Live online</dd></div>{f"<div><dt>Fee</dt><dd>{ev['price_label']}</dd></div>" if ev.get('price_label') else ''}</dl>
{extra}
<p class="countdown" data-countdown="{ev['start']}" aria-live="polite"></p>
<a class="btn btn-primary" href="{cta_href}"{' rel="noopener" target="_blank"' if cta_href.startswith('http') else ''}>{cta_text}</a>
</div>"""


def workshop_cards():
    out = []
    for i, (date, name, sub, desc, agenda) in enumerate(WORKSHOPS, 1):
        out.append(f'<article class="card workshop"><span class="tag" style="background:var(--red-50);color:var(--red-700)">Workshop {i} · {date}</span>'
                   f'<h3>{name}: {sub}</h3><p>{desc}</p><ul>' + "".join(f"<li>{a}</li>" for a in agenda) + "</ul></article>")
    return '<div class="grid-3">' + "".join(out) + "</div>"


AGENDA = [
    ("6:00 PM", "Welcome: AEP in one picture", "How data flows from sources to profiles to audiences to channels."),
    ("6:20 PM", "XDM schemas and datasets", "Live demo, then model a simple customer schema."),
    ("6:55 PM", "Ingestion basics", "Load a sample file, map fields and read errors."),
    ("7:25 PM", "Break", "Ten-minute break."),
    ("7:35 PM", "Identity and Real-Time Profile", "Namespaces, identity graphs and merged profiles."),
    ("8:10 PM", "Segmentation and activation basics", "Build an audience and see how it reaches a destination."),
    ("8:40 PM", "Career path and test series walkthrough", "How to use the free test series, next steps and live Q&A."),
]

agenda_html = '<ol class="agenda">' + "".join(f'<li><time>{t}</time><div><strong>{a}</strong><span>{b}</span></div></li>' for t, a, b in AGENDA) + "</ol>"

EVENTS = [
    dict(
        path="academy/aep-launchpad-bootcamp.html",
        nav="AEP Launchpad Bootcamp",
        bands=True, program=True,
        title="AEP Launchpad Bootcamp: Adobe Experience Platform Foundations",
        desc="Live 3-hour AEP foundations bootcamp, Sunday 11 Oct 2026, 6–9 PM IST. ₹3,000 with a free ₹3,500 interview & certification test series.",
        h1="Start your Adobe Experience Platform journey here",
        kicker="AEP Launchpad: Foundations Bootcamp",
        lede="Understand customer data, schemas, identity, profiles, segmentation and activation through guided demonstrations and practical exercises. Learn. Practice. Build. Get career-ready.",
        keywords=["aep bootcamp", "adobe experience platform bootcamp", "aep foundations workshop", "aep training online india", "aep certification practice test"],
        answer="AEP Launchpad: Foundations is a live, three-hour online bootcamp on Sunday 11 October 2026 from 6:00 to 9:00 PM IST. It covers the Adobe Experience Platform foundations — XDM schemas, datasets, ingestion, identity, Real-Time Customer Profile, segmentation and activation — for ₹3,000, with a ₹3,500 interview and certification test series included free.",
        schema="WebPage",
        event=dict(name=BOOTCAMP["name"], start=BOOTCAMP["start"], end=BOOTCAMP["end"], price=BOOTCAMP["price"]),
        hero_visual=ticket(BOOTCAMP, "Next bootcamp", REG_FORM, "Register for ₹3,000", '<p class="ticket-bonus">+ ₹3,500 test series free</p>'),
        interest_options=["Sunday bootcamp (₹3,000)", "Live Foundations batch (from 15 Oct)", "Friday hands-on workshops"],
        sections=[
            ("Your bootcamp package", BONUS + """<div class="grid-3" style="margin-top:22px">
<div class="card"><h3>Live, instructor-led</h3><p>Three hours of live AEP foundations training taught by a working MarTech architect.</p></div>
<div class="card"><h3>Hands-on</h3><p>Guided demonstrations and short practical exercises, not slides alone.</p></div>
<div class="card"><h3>Career-ready next steps</h3><p>How the foundations map to AEP roles, interviews and certification preparation.</p></div>
</div>""", "plain", "What you get"),
            ("Bootcamp agenda", agenda_html + '<p class="small muted">Timings are approximate and may shift slightly with live Q&amp;A.</p>', "alt", "Sunday · 6:00 – 9:00 PM IST"),
            ("What you'll learn", """<ul class="checklist cols-2">
<li>How Adobe Experience Platform fits together end to end</li><li>XDM schemas: classes, field groups and identities</li>
<li>Datasets and batch ingestion basics</li><li>Identity namespaces and identity graphs</li>
<li>Real-Time Customer Profile and merge policies</li><li>Building and validating your first audience</li>
<li>How audiences reach destinations</li><li>Where to go next in your AEP learning path</li></ul>""", "plain", "Foundations only"),
            ("Two ways to start", f"""<div class="grid-2">
{ticket(BOOTCAMP, "Card A · Weekend", REG_FORM, "Register for the bootcamp", '<p class="ticket-bonus">3 hours · ₹3,000 · + ₹3,500 test series free</p>')}
{ticket(BATCH, "Card B · Weekdays", "aep-foundations-batch.html", "Explore the Foundations batch", '<p class="ticket-bonus">Two weeks · Monday–Friday · beginner-friendly</p>')}
</div><p style="margin-top:16px">Plus <a href="workshops.html">hands-on workshops every Friday</a>.</p>""", "dark", "Schedule (IST)"),
            ("Who should attend", """<div class="grid-3">
<div class="card"><h3>Beginners &amp; students</h3><p>No prior Adobe experience needed.</p></div>
<div class="card"><h3>Career switchers</h3><p>Developers, data engineers, analysts and marketers moving into MarTech.</p></div>
<div class="card"><h3>Working professionals</h3><p>Anyone who wants a clear mental model of AEP before an interview or project.</p></div>
</div>""", "alt", "Audience"),
        ],
        faqs=[
            ("When is the bootcamp?", "Sunday, 11 October 2026, 6:00 PM to 9:00 PM Indian Standard Time, live online."),
            ("How much does it cost?", "₹3,000 per participant. The ₹3,500 interview and certification test series is included free."),
            ("Do I need Adobe experience?", "No. The bootcamp covers foundations only and is designed for beginners and career switchers."),
            ("Does the test series guarantee certification?", "No. It is practice material to support preparation. Official certification outcomes are not guaranteed."),
            ("How do I register?", "Use the Register button or the form on this page; the team will confirm your seat and share the joining link."),
        ],
        related=["academy/workshops.html", "academy/aep-foundations-batch.html", "training/index.html"],
    ),
    dict(
        path="academy/workshops.html",
        bands=True, program=True,
        title="AEP Workshops & Bootcamps: Hands-on Every Friday | Infinite360",
        desc="Hands-on Adobe Experience Platform workshops every Friday, the AEP Launchpad bootcamp and live foundations batches from Infinite360 Tech Academy.",
        h1="Workshops and bootcamps",
        kicker="Academy · Hands-on",
        lede="Short, practical sessions that build AEP foundations one skill at a time: a weekend bootcamp, a two-week foundations batch and hands-on workshops every Friday.",
        keywords=["aep workshop", "adobe experience platform workshop", "aep hands-on lab", "martech bootcamp", "aep webinar series"],
        answer="Infinite360 Tech Academy runs three foundation formats: the AEP Launchpad bootcamp (Sunday 11 October 2026, 6–9 PM IST, ₹3,000 with a free ₹3,500 test series), a live two-week AEP Foundations batch starting 15 October at 8:00 AM IST, and hands-on workshops every Friday, each focused on one AEP skill.",
        schema="CollectionPage",
        hero_visual=ticket(BOOTCAMP, "Next bootcamp", "aep-launchpad-bootcamp.html", "View the bootcamp", '<p class="ticket-bonus">+ ₹3,500 test series free</p>'),
        interest_options=["Sunday bootcamp (₹3,000)", "Live Foundations batch (from 15 Oct)", "Friday hands-on workshops"],
        sections=[
            ("Choose your format", f"""<div class="grid-3">
<a class="card link-card" href="aep-launchpad-bootcamp.html"><span class="tag" style="background:var(--red-50);color:var(--red-700)">Bootcamp · ₹3,000</span><h3>AEP Launchpad: Foundations</h3><p>{BOOTCAMP['date']}, {BOOTCAMP['time']}. Three hours, live, with a free ₹3,500 test series.</p><span class="more">View bootcamp &rarr;</span></a>
<a class="card link-card" href="aep-foundations-batch.html"><span class="tag" style="background:var(--blue-50);color:var(--blue)">Batch · 2 weeks</span><h3>Live AEP Foundations batch</h3><p>{BATCH['date']}, {BATCH['time']}, Monday–Friday.</p><span class="more">View batch &rarr;</span></a>
<a class="card link-card" href="#friday-workshop-series"><span class="tag" style="background:var(--green-50);color:var(--green)">Every Friday</span><h3>Hands-on workshops</h3><p>One AEP skill per session: model, ingest, resolve, unify, segment, activate.</p><span class="more">See the series &rarr;</span></a>
</div>""", "plain", "Formats"),
            ("Friday workshop series", workshop_cards() + '<p class="small muted" style="margin-top:14px">Workshop timings and joining details are shared on registration. Topics may be updated; each session stands alone.</p>', "alt", "Foundations · one skill per Friday"),
            ("How every workshop runs", """<div class="timeline">
<div class="step"><h3>Concept</h3><p>Twenty minutes on the why and the mental model.</p></div>
<div class="step"><h3>Demo</h3><p>A live walkthrough in Adobe Experience Platform.</p></div>
<div class="step"><h3>Hands-on</h3><p>A guided exercise you complete yourself.</p></div>
<div class="step"><h3>Review</h3><p>Common mistakes, Q&amp;A and what to practise next.</p></div>
</div>""", "dark", "Format"),
            ("Keep going after the foundations", """<p class="lead">Foundations are the first step. When you are ready for depth, move into a full program.</p>
<p class="cta-row"><a class="btn btn-primary" href="../training/">Career Accelerator · ₹60,000</a><a class="btn btn-ghost" href="index.html">All programs</a></p>""", "plain", "Next steps"),
        ],
        faqs=[
            ("How often are workshops held?", "Hands-on workshops run every Friday. Bootcamps and foundations batches are announced on this page."),
            ("Do I need to attend in order?", "No. Each workshop stands alone, though attending in order builds the full AEP foundations picture."),
            ("Are the workshops recorded?", "Ask the team when you register; availability of recordings can vary by session."),
        ],
        related=["academy/aep-launchpad-bootcamp.html", "academy/aep-foundations-batch.html", "academy/index.html"],
    ),
    dict(
        path="academy/aep-foundations-batch.html",
        bands=True, program=True,
        title="Live AEP Foundations Batch: Starts 15 Oct, 8 AM IST",
        desc="Two-week live Adobe Experience Platform foundations batch from 15 October 2026, 8:00–9:30 AM IST, Monday to Friday, with guided hands-on workshops.",
        h1="Live AEP Foundations batch",
        kicker="Academy · Two-week batch",
        lede="A beginner-friendly, two-week live batch on Adobe Experience Platform foundations with guided hands-on workshops — early mornings, Monday to Friday.",
        keywords=["aep foundations course", "aep live batch", "adobe experience platform beginner course", "aep morning batch ist", "aep course for beginners"],
        answer="The Live AEP Foundations batch starts on 15 October 2026 and runs for two weeks, Monday to Friday from 8:00 to 9:30 AM IST, subject to the published batch calendar. It is a beginner-friendly, live online program covering AEP foundations with guided hands-on workshops. The fee is shared on registration.",
        schema="WebPage",
        event=dict(name=BATCH["name"], start=BATCH["start"], end=BATCH["end"]),
        hero_visual=ticket(BATCH, "Next batch", REG_FORM, "Reserve your seat", '<p class="ticket-bonus">Two weeks · Monday–Friday</p>'),
        interest_options=["Live Foundations batch (from 15 Oct)", "Sunday bootcamp (₹3,000)", "Friday hands-on workshops"],
        sections=[
            ("Ten-session plan", """<ol class="agenda">
<li><time>Day 1</time><div><strong>AEP in one picture</strong><span>Platform architecture and the end-to-end data flow.</span></div></li>
<li><time>Day 2</time><div><strong>XDM fundamentals</strong><span>Classes, field groups and data types.</span></div></li>
<li><time>Day 3</time><div><strong>Schema design lab</strong><span>Model a customer and an event schema.</span></div></li>
<li><time>Day 4</time><div><strong>Datasets and batch ingestion</strong><span>Load, map and validate sample data.</span></div></li>
<li><time>Day 5</time><div><strong>Streaming and Web SDK basics</strong><span>How events reach AEP in near real time.</span></div></li>
<li><time>Day 6</time><div><strong>Identity foundations</strong><span>Namespaces, primary identity and graphs.</span></div></li>
<li><time>Day 7</time><div><strong>Real-Time Customer Profile</strong><span>Profile enablement and merge policies.</span></div></li>
<li><time>Day 8</time><div><strong>Segmentation</strong><span>Batch, streaming and edge audiences.</span></div></li>
<li><time>Day 9</time><div><strong>Activation basics</strong><span>Destinations, consent and QA.</span></div></li>
<li><time>Day 10</time><div><strong>Mini project and next steps</strong><span>End-to-end exercise, interview prep and learning path.</span></div></li>
</ol><p class="small muted">Session plan is indicative and follows the published batch calendar.</p>""", "plain", "8:00 – 9:30 AM IST"),
            ("Who it's for", """<div class="grid-3">
<div class="card"><h3>Beginners</h3><p>No prior Adobe experience required.</p></div>
<div class="card"><h3>Early risers</h3><p>A 90-minute morning slot before the working day.</p></div>
<div class="card"><h3>Future AEP practitioners</h3><p>A foundation for the career accelerator or certification preparation.</p></div>
</div>""", "alt", "Audience"),
            ("Try before you commit", f'<p class="lead">Join the Sunday bootcamp first: {BOOTCAMP["date"]}, {BOOTCAMP["time"]}, ₹3,000 with a free ₹3,500 test series.</p><p class="cta-row"><a class="btn btn-light" href="aep-launchpad-bootcamp.html">View the bootcamp</a></p>', "dark", "Weekend option"),
        ],
        faqs=[
            ("What is the fee for the Foundations batch?", "The fee is shared on registration. Contact the team using the form or WhatsApp."),
            ("What if I miss a session?", "Ask the team on registration about catch-up options for missed sessions."),
        ],
        related=["academy/aep-launchpad-bootcamp.html", "academy/workshops.html", "academy/courses/aep-certification-prep.html"],
    ),
]
