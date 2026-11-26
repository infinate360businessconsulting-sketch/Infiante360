"""Meetup landing page. Date, venue and agenda are not confirmed, so the page collects interest only and says so."""
from content_growth import landing

MEETUP_PAGE = landing(
    "meetup", "Online MarTech Meetup: Register (Rs 250 per Meetup)",
    "Online Infiante360 MarTech and Agentic AI meetups cost Rs 250 per meetup. Register with your name, email and phone and we send the date and payment details.",
    "Infiante360 MarTech and Agentic AI meetup",
    ["adobe martech meetup", "aep meetup", "martech community meetup india", "agentic ai meetup", "adobe experience platform meetup"],
    "Infiante360 Tech Academy meetups for Adobe MarTech and Agentic AI practitioners are held online. Each meetup costs Rs 250. The next date and agenda are not confirmed yet. Register with your name, email and phone, and we will send the date and payment details before you pay anything. No job or certification is promised.",
    "Meetup registration",
    ["Online meetup, Rs 250 per meetup", "Share your name, email and phone number", "We send the date, agenda and payment details by email", "Nothing is charged on this form"],
    "Developers, data engineers, analysts, architects and leaders working with or moving into Adobe MarTech and Agentic AI.", "Meetup registration",
)
MEETUP_PAGE["sections"].insert(0, ("About the meetup", '<p>An informal online meetup for practitioners to share what works in customer data, identity, journeys and AI agents. Fee: ₹250 per meetup. Date and agenda: to be announced. We confirm payment details by email; this form does not take payment. Until then, join the <a href="../academy/community.html">learning community</a> or watch the <a href="../academy/videos.html">free demos</a>. Questions? WhatsApp +91 82968 93895.</p>'))
MEETUP_PAGE["related"] = ["academy/community.html", "lp/batches.html", "academy/practice.html"]
MEETUP_ALL = [MEETUP_PAGE]
