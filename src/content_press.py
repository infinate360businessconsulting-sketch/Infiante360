"""Press & media kit page: the single canonical landing point for off-page articles, PR and citations."""
import html as _h
e = _h.escape
WA = "https://wa.me/918296893895"
LI = "https://www.linkedin.com/in/pavanbabu1"
BASE = "https://infiante360techacademy.com/"
UTM = lambda src, med="referral": f"{BASE}answers/index.html?utm_source={src}&utm_medium={med}&utm_campaign=offpage"

BOILER = ("Infinite360 Tech Academy is a learning and consulting initiative focused on Adobe Experience Platform, Real-Time CDP, "
          "Adobe Journey Optimizer, Customer Journey Analytics, the Web SDK, data engineering and Agentic AI. It publishes sourced guides and "
          "answers, runs hands-on programs and offers corporate training. Founder: Pavan Babu Gandla, Bengaluru, India.")

PRESS = dict(
    path="press.html", nav="Press",
    title="Press & Media Kit | Infinite360 Tech Academy"[:65],
    desc="Official boilerplate, contact, author bio, brand links and linking guidelines for journalists, publishers and partners covering Infinite360 Tech Academy."[:160],
    h1="Press and media kit", kicker="Press · Media",
    keywords=["infinite360 press", "infinite360 tech academy about", "pavan babu gandla author"],
    answer="This page is the official reference for anyone writing about Infinite360 Tech Academy: the approved company description, founder contact, canonical links to link to, and rules for how articles and listings should describe us. Use only the facts here; we do not publish unverified client names, results or guarantees.",
    schema="WebPage", category="Press", date="2026-10-19",
    sections=[
        ("Approved company description", f"<p>{e(BOILER)}</p><p class=\"small muted\">Short version: Adobe Experience Platform training and consulting with sourced, practical guides.</p>", "plain", "Boilerplate"),
        ("Spokesperson", f'<p><strong>Pavan Babu Gandla</strong>, founder, Adobe Experience Cloud architect. <a href="{LI}" rel="noopener" target="_blank">LinkedIn</a>. Available for expert comment on Adobe Experience Platform, customer data architecture and Agentic AI in MarTech.</p><p><a class="btn btn-primary" href="contact-us.html">Request an interview or comment</a> <a class="btn btn-ghost" href="{WA}">WhatsApp +91 82968 93895</a></p>', "alt", "Contact"),
        ("Canonical pages to link to", '<ul class="checklist"><li><a href="answers/index.html">Adobe Experience Platform answers hub</a>: 191 sourced Q&amp;As</li><li><a href="academy/aep-implementation-track/index.html">AEP implementation track</a></li><li><a href="academy/programs/ai-engineering-bootcamp.html">AI Engineering Bootcamp</a></li><li><a href="training/corporate-training.html">Corporate training</a></li><li><a href="corporate/index.html">Infinate360 corporate consulting</a></li></ul>', "plain", "Links"),
        ("How to cite us", "<p>Link to the most relevant canonical page above using natural, descriptive anchor text, for example the name of the topic. Please do not use paid or automated link placements, and mark sponsored content as sponsored. Official Adobe product behaviour should always be cited to Adobe's own documentation.</p>", "alt", "Guidelines"),
        ("What we do not claim", "<p>Infinite360 is an independent training and consulting provider. We do not claim an official Adobe partnership, guaranteed jobs, guaranteed certification, or named client endorsements. Content on this site is AI-assisted and based on public documentation; check the linked source pages for current product details.</p>", "plain", "Accuracy"),
    ],
    faqs=[], related=["answers/index.html", "about-us.html", "contact-us.html"],
)
PRESS_PAGES = [PRESS]
