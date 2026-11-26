"""Batches landing page: one registration form for every live batch. Leads go through the existing form -> /api/lead -> LEAD_WEBHOOK_URL (CRM) path.
No start dates or fees are stated: none are confirmed. See docs/growth/batch-lead-routing.md."""
from content_growth import landing

BATCHES = [
    ("Weekday Morning Live Batch", "Monday to Friday, usually 6:45 to 8:30 AM IST", "../academy/programs/weekday-morning-batch.html"),
    ("Agentic AI + Adobe CDP Weekend Batch", "16 live weekend sessions", "../academy/programs/agentic-ai-cdp-weekend-batch.html"),
    ("Adobe MarTech SME Batch", "Live, instructor-led", "../academy/programs/martech-sme-batch.html"),
    ("Six-Day MarTech SME Accelerator", "Six live evenings, 10:00 to 11:00 PM IST", "martech-sme-accelerator.html"),
    ("Adobe MarTech + Agentic AI Career Accelerator", "Live online, 90 days", "../training/index.html"),
]
_rows = "".join(f'<li><strong>{n}</strong>: {w}. <a href="{u}">Know more</a></li>' for n, w, u in BATCHES)

BATCH_PAGE = landing(
    "batches", "Live Batches: Register for Adobe MarTech and Agentic AI",
    "Register your interest in Infiante360 live batches: weekday morning, weekend, SME and career accelerator. Next batch dates are shared on enquiry.",
    "Register for an Infiante360 live batch",
    ["adobe martech live batch", "aep training batch", "agentic ai weekend batch", "martech training registration", "adobe experience platform batch india"],
    "Infiante360 Tech Academy runs live batches in Adobe MarTech and Agentic AI: weekday morning, weekend, SME and a career accelerator. Choose a batch below, tell us which one you prefer in the message box, and we will reply with the next dates, syllabus and fee. Dates are announced on enquiry, and no placement or certification is promised.",
    "Batch registration",
    ["Name the batch you prefer in the message box", "We reply with next start date, syllabus and fee", "Free demos are on our YouTube channel before you decide", "No payment is taken on this form"],
    "Developers, data engineers, analysts, architects and career switchers moving into Adobe MarTech or Agentic AI.", "Live batches",
)
BATCH_PAGE["sections"].insert(0, ("Available batches", f'<ul class="checklist">{_rows}</ul><p>Next dates for each batch are shared on enquiry. <a href="https://www.youtube.com/@Infiante360TechAcademy" rel="noopener" target="_blank">Watch free demos</a> first, or call or WhatsApp +91 82968 93895.</p>'))
BATCH_PAGE["related"] = ["academy/catalogue.html", "academy/index.html", "training/corporate-training.html"]
BATCHES_ALL = [BATCH_PAGE]
