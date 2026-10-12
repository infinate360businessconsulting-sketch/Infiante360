"""MarTech Bootcamp webinar page: prerecorded webinar embedded from webinar.gg with a registration link.
No dates are shown. Fees (if any) are shown on the registration page of the webinar platform."""
import html as _h
e = _h.escape
WID = "cmv5o854501cts60y39yf8wao"
REGISTER_URL = f"https://webinar.gg/register/{WID}"
EMBED_URL = f"https://webinar.gg/embed/{WID}"
EL = "https://experienceleague.adobe.com/en/docs/experience-platform"

PLAYER = f"""<div class="webinar-box">
<button class="webinar-facade" type="button" data-embed="{EMBED_URL}" aria-label="Load the webinar player">
<span class="play" aria-hidden="true"></span><span class="wf-text"><strong>What Is MarTech? AEP Foundations &amp; Live-Style Demo</strong><small>Prerecorded webinar · about 52 minutes · select to load the player</small></span></button>
<noscript><p>Turn on JavaScript to load the player here, or <a href="{REGISTER_URL}" rel="noopener" target="_blank">open the webinar page</a>.</p></noscript>
</div>
<p class="cta-row" style="margin-top:18px"><a class="btn btn-primary" href="{REGISTER_URL}" rel="noopener" target="_blank">Register for the webinar</a>
<a class="btn btn-ghost" href="{REGISTER_URL}" rel="noopener" target="_blank">Open in a new tab</a></p>
<p class="small muted">The player and registration are provided by the webinar platform (webinar.gg). It may ask you to register or sign in before the recording plays, and it may show any registration fee on its own page. If the player does not load in this page, use the registration link.</p>"""

AGENDA = [("Welcome and MarTech careers", "Who this webinar is for and why MarTech skills matter."),
          ("What is MarTech?", "Enterprise use cases and architecture: customer data, analytics, automation, journeys, personalisation and governance."),
          ("Adobe Experience Platform fundamentals", "XDM schemas, datasets, ingestion, Identity Service, Real-Time Customer Profile, segmentation and destinations."),
          ("Guided workflow demonstration", "A retail cart-abandonment example from requirement to audience."),
          ("How the Adobe ecosystem fits together", "AEP with Real-Time CDP, Journey Optimizer, Customer Journey Analytics, Adobe Analytics and Experience Manager."),
          ("Bootcamp overview and next steps", "Learning path, resources and how to register.")]
BLOCKS = [("XDM schemas", "Define the structure and meaning of customer experience data."),
          ("Datasets", "Store records that conform to a schema."),
          ("Data ingestion", "Brings data in through supported batch or streaming methods."),
          ("Identity Service", "Helps connect identifiers for the same customer under configured identity rules."),
          ("Real-Time Customer Profile", "Combines eligible profile and event data under merge policies."),
          ("Segmentation", "Defines audiences from attributes and behaviour."),
          ("Destinations", "Activate eligible audiences or data to connected systems.")]
STEPS = [("Requirement", "Understand behaviour and build an audience of customers who abandoned their carts."),
         ("Schema", "Design XDM schemas for the customer profile and experience events."),
         ("Ingest", "Load sample data into a dataset with an available ingestion method."),
         ("Identity and profile", "With identity and profile configured, eligible data contributes to Real-Time Customer Profiles."),
         ("Audience", "Define the audience with customer and event conditions."),
         ("Activate", "Review activation options and how Journey Optimizer could orchestrate a journey.")]


def grid(items):
    return '<div class="grid-3">' + "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in items) + "</div>"


def tl(items):
    return '<div class="timeline">' + "".join(f'<div class="step"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in items) + "</div>"


WEBINAR_PAGE = dict(
    path="academy/martech-bootcamp-webinar.html", nav="MarTech webinar",
    title="MarTech Bootcamp Webinar: What Is MarTech & AEP?",
    desc="Free-to-start prerecorded MarTech bootcamp webinar: what MarTech is, how Adobe Experience Platform works, a guided workflow and your next steps.",
    h1="MarTech Bootcamp webinar: what is MarTech and how AEP works", kicker="Academy · Prerecorded webinar",
    keywords=["what is martech", "adobe experience platform foundations", "martech bootcamp webinar", "aep demo for beginners", "martech webinar"],
    schema="WebPage", category="Academy", bands=True,
    hero_cta=("Register for the webinar", REGISTER_URL),
    answer="This prerecorded webinar explains what MarTech is and how Adobe Experience Platform (AEP) works, then walks through a retail example from schema and ingestion to profile, audience and activation. It is a beginner-friendly introduction to the Infinite360 MarTech bootcamp. Register through the webinar platform; training outcomes such as jobs or certification are not guaranteed.",
    sections=[
        ("Watch the webinar", PLAYER, "plain", "Prerecorded"),
        ("What is covered", tl(AGENDA), "alt", "Agenda"),
        ("What is MarTech?", "<p>MarTech combines marketing, technology, customer data, analytics and automation to plan, personalise, deliver and measure customer experiences. Think of a shopper who browses a product, leaves, and returns days later: a MarTech stack can recognise them where permitted, build relevant audiences, orchestrate a message and measure the result.</p>"
         '<ul class="checklist cols-2"><li>Customer Data Platforms</li><li>Digital analytics</li><li>Marketing automation</li><li>Journey orchestration</li><li>Personalisation and experimentation</li><li>Data engineering and integration</li><li>Consent and data governance</li><li>AI-assisted marketing operations</li></ul>', "plain", "Foundations"),
        ("AEP building blocks", grid(BLOCKS) + f'<p class="small muted">Read more: <a href="../adobe-experience-platform/">Adobe Experience Platform guides</a>, and Adobe\'s <a href="{EL}" rel="noopener" target="_blank">official documentation</a>.</p>', "alt", "Platform"),
        ("The demo workflow", tl(STEPS) + "<p>Where a configured environment is available the webinar shows the interface; otherwise it uses diagrams and sample records, clearly as a conceptual demonstration. No real customer data is used.</p>", "plain", "Retail example"),
        ("How the Adobe ecosystem fits", '<ul class="checklist"><li><strong>Real-Time CDP:</strong> audience building and activation.</li><li><strong>Journey Optimizer:</strong> journey orchestration and personalised engagement.</li><li><strong>Customer Journey Analytics:</strong> analysis of journeys across configured data sources.</li><li><strong>Adobe Analytics:</strong> digital analytics and behavioural reporting.</li><li><strong>Experience Manager:</strong> content and experience management.</li></ul>', "alt", "Ecosystem"),
        ("Your next step: the bootcamp", '<p>The bootcamp learning path covers the MarTech ecosystem, AEP and XDM design, ingestion, identity and profile, audiences and activation, RTCDP, AJO and CJA foundations, and practical troubleshooting scenarios.</p>'
         '<p class="cta-row"><a class="btn btn-primary" href="programs/weekday-morning-batch.html">Weekday morning batch</a><a class="btn btn-ghost" href="aep-launchpad-bootcamp.html">AEP Launchpad bootcamp</a><a class="btn btn-ghost" href="../training/">Career Accelerator · ₹60,000</a><a class="btn btn-ghost" href="../brochures.html">Download brochures</a><a class="btn btn-ghost" href="free-resources.html">Free resources</a></p>'
         '<p class="small muted">Some content is created or enhanced using AI and reviewed. Infinite360 is independent and not affiliated with Adobe. Training does not guarantee employment, salary or certification.</p>', "dark", "Continue"),
    ],
    faqs=[("Who is this webinar for?", "Beginners, working professionals, data engineers, analysts, digital marketers and career switchers who want a foundation in MarTech and AEP."),
          ("Is it live?", "No. It is a prerecorded webinar, shown in a live-style format by the webinar platform."),
          ("Do I need to register?", "Yes. Registration happens on the webinar platform through the link on this page; it may ask for your name and email, and it shows any fee on its own page."),
          ("Does it include hands-on access to Adobe tools?", "The webinar demonstrates concepts and a workflow. Hands-on sandbox practice is part of the paid programs.")],
    related=["academy/index.html", "academy/free-resources.html", "adobe-experience-platform/index.html"],
)
WEBINAR_ALL = [WEBINAR_PAGE]
