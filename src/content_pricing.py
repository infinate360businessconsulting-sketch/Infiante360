"""Pricing page: the owner's price ladder (26 Nov 2026). Prices are exclusive of 18% GST; credit card payments add 2%; UPI has no extra charge.
No checkout exists: payment details are confirmed in writing before any payment."""
ROWS = [
    ("AEP Launchpad Bootcamp", "3 hours, Sunday 6 to 9 PM IST: XDM, datasets, identity, profile, segmentation and activation. The Rs 3,500 test series is free.", "₹5,000", "aep-launchpad-bootcamp.html"),
    ("Bronze Membership", "All recorded courses, the 3,500-question bank and sandbox. Self-paced, no live classes.", "₹2,00,000", "programs/bronze-membership.html"),
    ("Career Accelerator", "Live, hands-on AEP, Real-Time CDP, AJO, CJA, Web SDK and Agentic AI, with projects and interview preparation.", "₹70,000", "../training/index.html"),
    ("Foundation + Advanced Architecture (recorded)", "AEP, AJO and CJA, then enterprise MarTech and CDP architecture.", "₹70,000", "programs/aep-ajo-cja-foundation-advanced.html"),
    ("Leadership and Corporate", "Tailored, project-based training on AEP, Real-Time CDP, AJO, CJA, data engineering and Agentic AI.", "₹1,50,000 or custom quote", "programs/executive-architecture-leadership.html"),
    ("30-hour Agentic AI + AEP Lab Series with 4-week Adobe CX Agentic AI Bootcamp", "Journey agents, MCP pipelines, decisioning, CJA attribution, governance and a capstone.", "₹53,000", "programs/agentic-ai-advanced-30-hour.html"),
]
def _row(n, d, p, u):
    return f'<h3>{n}: {p}</h3><p>{d} <a href="{u}">Know more</a></p>'
PRICING_PAGE = dict(
    path="academy/pricing.html", nav="Pricing",
    title="Course Fees: Adobe MarTech and Agentic AI | Infiante360",
    desc="Infiante360 Tech Academy fees, from the Rs 5,000 AEP Launchpad Bootcamp to leadership and corporate programs. Prices exclude 18% GST. UPI has no extra charge.",
    h1="Course fees and programs", kicker="Pricing",
    keywords=["adobe martech course fees", "aep course price india", "adobe experience platform training fee", "career accelerator fee", "agentic ai course price"],
    schema="WebPage", category="Academy",
    answer="Infiante360 Tech Academy fees run from Rs 5,000 for the AEP Launchpad Bootcamp to Rs 1,50,000 or a custom quote for leadership and corporate programs. All prices exclude 18% GST. Credit card payments add 2%, and UPI has no extra charge. Payment details are confirmed in writing before you pay. No job or certification outcome is promised.",
    sections=[("Programs and fees", "".join(_row(*r) for r in ROWS)),
              ("Taxes and payment", '<p>All prices are exclusive of 18% GST. Credit card payments add 2%; UPI has no extra charge. We confirm the amount and payment method in writing before any payment. Online meetups are Rs 250 each; see the <a href="../lp/meetup.html">meetup page</a>.</p>'),
              ("Choose and ask", '<p>Not sure which fits? See the <a href="catalogue.html">course catalogue</a>, the <a href="../lp/batches.html">live batches</a> or <a href="../contact-us.html">contact us</a> (WhatsApp or call +91 82968 93895).</p>')],
    faqs=[("Do the prices include GST?", "No. Prices are exclusive of 18% GST."),
          ("Is there a charge for paying by card?", "Credit card payments add 2%. UPI has no extra charge.")],
    related=["academy/catalogue.html", "lp/batches.html", "training/corporate-training.html"],
)
PRICING_ALL = [PRICING_PAGE]
