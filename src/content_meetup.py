"""Meetup landing page. Date, venue and agenda are not confirmed, so the page collects interest only and says so."""
from content_growth import landing

MEETUP_PAGE = landing(
    "meetup", "Infiante360 MarTech Meetup: Register Your Interest",
    "Register your interest in the Infiante360 MarTech and Agentic AI meetup. Share your name, email and phone, and we will send the date, venue and agenda.",
    "Infiante360 MarTech and Agentic AI meetup",
    ["adobe martech meetup", "aep meetup", "martech community meetup india", "agentic ai meetup", "adobe experience platform meetup"],
    "Infiante360 Tech Academy is organising a meetup for Adobe MarTech and Agentic AI practitioners. The date, venue and agenda are not confirmed yet. Register your interest with your name, email and phone, and we will send the details as soon as they are final. There is no cost to register interest, and no job or certification is promised.",
    "Meetup interest",
    ["Share your name, email and phone number", "We send the date, venue and agenda once confirmed", "Meet other MarTech, data and AI practitioners", "Registering interest does not reserve a seat"],
    "Developers, data engineers, analysts, architects and leaders working with or moving into Adobe MarTech and Agentic AI.", "Meetup interest",
)
MEETUP_PAGE["sections"].insert(0, ("About the meetup", '<p>An informal meetup for practitioners to share what works in customer data, identity, journeys and AI agents. Date, venue and agenda: to be announced. Until then, join the <a href="../academy/community.html">learning community</a> or watch the <a href="../academy/videos.html">free demos</a>. Questions? WhatsApp +91 82968 93895.</p>'))
MEETUP_PAGE["related"] = ["academy/community.html", "lp/batches.html", "academy/practice.html"]
MEETUP_ALL = [MEETUP_PAGE]
