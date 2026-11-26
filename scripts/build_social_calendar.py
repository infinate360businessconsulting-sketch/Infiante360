"""Builds data/social/calendar-100.csv in the upload-post bulk template format.
Guide posts are derived from data/visuals/specs/*.json (real pages and images); the rest are hand-written below.
Nothing is posted by this script. Run: python3 -I scripts/build_social_calendar.py"""
import csv, glob, json, os, re, datetime as dt
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = "https://infiante360techacademy.com/"
YT = "https://www.youtube.com/@Infiante360TechAcademy"
IMG = B + "assets/social/"
ALL = "linkedin|facebook|instagram|x"
TXT = "linkedin|facebook|x"
posts = []  # (text_with_{L}, link, media, networks)


def add(text, link, media="", nets=None):
    posts.append((text, link, media, nets or (ALL if media else TXT)))

# ---- A. 36 guide posts (real pages + real og images) ----
HOOKS = [
    "{band} That is the core of our {kw} guide: {L}",
    "Stuck on {kw}? Start with one rule: {band} Full walkthrough: {L}",
    "How does your team handle {kw}? Our checklist and schematic: {L}",
    "Save this for your next design review: {kw}. {band} {L}",
    "A rule worth pinning above your desk: {band} (from our {kw} guide) {L}",
    "Quick read on {kw}. {band} {L}",
]
TAGS = [("xdm|schema|sandbox|dataset", "#AdobeExperiencePlatform #XDM"), ("cja|journey analytics", "#CustomerJourneyAnalytics #Analytics"),
        ("mcp|agent|ai ", "#AgenticAI #MCP"), ("consent|privacy|governance|healthcare", "#DataGovernance #Consent"),
        ("snowflake|bigquery|databricks|kafka", "#DataEngineering #CloudData"), ("identity|customer 360", "#IdentityResolution #Customer360"),
        ("web sdk", "#AdobeWebSDK #MarTech"), ("journey|activation|audience|rtcdp|personalization", "#MarTech #Personalization")]
specs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, "data/visuals/specs/*.json")))]
for i, s in enumerate(specs):
    tag = next((t for k, t in TAGS if re.search(k, s["keyword"] + " ", re.I)), "#MarTech #Adobe")
    kw, band = s["keyword"], s["band"]
    t = HOOKS[i % len(HOOKS)].format(band=band, kw=kw, L="{L}") + " " + tag
    add(t, B + s["page"], IMG.replace("social/", "visuals/") + s["slug"] + "/og.png")

# ---- B. hand-written (64) ----
def bn(n): return IMG + n
P = []
# Programs and batches (10)
add("Mornings are for learning. Our Weekday Morning Live Batch runs Monday to Friday, usually 6:45 to 8:30 AM IST: Adobe MarTech and Agentic AI, day by day. Next dates on enquiry. {L} #AdobeExperiencePlatform #LiveTraining", B + "academy/programs/weekday-morning-batch.html", bn("01-career-accelerator.png"))
add("Prefer weekends? The Agentic AI + Adobe CDP Weekend Batch is 16 live sessions covering agents, AEP, RTCDP, AJO and CJA. See the outline and ask for the next dates: {L} #AgenticAI #WeekendLearning", B + "academy/programs/agentic-ai-cdp-weekend-batch.html")
add("Already know the basics? The Adobe MarTech SME Batch goes deeper across AEP, RTCDP, AJO, CJA, Web SDK and APIs, led by a working architect. {L} #AdobeMarTech #SME", B + "academy/programs/martech-sme-batch.html", bn("02-six-day-martech-sme.png"))
add("Six live evenings, 10:00 to 11:00 PM IST, one connected view of MarTech instead of tool-by-tool learning. Next series dates are shared on enquiry. {L} #MarTech #AdobeExperienceCloud", B + "lp/martech-sme-accelerator.html", bn("02-six-day-martech-sme.png"))
add("Moving into Adobe MarTech from data, development or analytics? Our Career Accelerator is 90 days of live online learning with labs and interview preparation. No job or salary is promised; the work is yours and ours. {L} #CareerTransition #AdobeMarTech", B + "training/", bn("01-career-accelerator.png"))
add("For executives: CXO Hive is a 10-weekend live program on MarTech architecture, AI governance, operating models and an investment case. Built for people who decide, not just implement. {L} #Leadership #EnterpriseArchitecture", B + "academy/programs/executive-architecture-leadership.html", bn("19-executive-leadership.png"))
add("Can't find the batch that fits? Tell us your role and goal and we will point you to the right one. One short form, replies within two business days. {L} #AdobeTraining", B + "lp/batches.html", "", "linkedin|facebook|x")
add("Batch choices in one place: weekday morning, weekend, SME, six-day accelerator and career accelerator. Pick one and register your interest. {L} #MarTech #Learning", B + "lp/batches.html", bn("01-career-accelerator.png"))
add("Looking for a particular technology? Browse the course catalogue by category: Adobe Experience Cloud, Agentic AI, data engineering and more. Live pages get a Know more link; the rest are in planning. {L} #TechTraining", B + "academy/catalogue.html")
add("Every course page on our site ends with the same promise: no placement or certification guarantees, just practical learning. Start with the catalogue. {L} #HonestLearning #MarTech", B + "academy/catalogue.html", bn("08-career-transformation.png"))
# Course spotlights with banners (10)
add("Adobe Experience Platform, explained from raw data to intelligent experiences: schemas, identity, profiles, audiences and activation. Course details: {L} #AdobeExperiencePlatform #AEP", B + "academy/programs/aep-ajo-cja-foundation-advanced.html", bn("03-adobe-experience-platform.png"))
add("Real-Time CDP is more than segments. It is data, identity and activation working as one. See what we cover in the Real-Time CDP course: {L} #RealTimeCDP #CDP", B + "academy/courses/rtcdp-training.html", bn("04-real-time-cdp.png"))
add("Every interaction, a smarter journey. Adobe Journey Optimizer training covers journeys, messages, decisioning and measurement. Know more: {L} #AdobeJourneyOptimizer #AJO", B + "academy/courses/ajo-training.html", bn("05-adobe-journey-optimizer.png"))
add("Understand customers, not just clicks. Customer Journey Analytics training: data views, connections and cross-channel analysis. Know more: {L} #CustomerJourneyAnalytics #CJA", B + "academy/courses/cja-training.html", bn("06-customer-journey-analytics.png"))
add("Clean, consented data starts in the browser. Our Adobe Web SDK and Tags course covers datastreams, events and validation. Know more: {L} #AdobeWebSDK #AdobeTags", B + "academy/courses/web-sdk-training.html", bn("18-web-sdk.png"))
add("Data-driven decisions need trustworthy measurement. Adobe Analytics training: implementation, reporting and analysis. Know more: {L} #AdobeAnalytics #DigitalAnalytics", B + "academy/courses/adobe-analytics-training.html", bn("17-adobe-analytics.png"))
add("Engineer intelligence, with guardrails. Our Agentic AI course covers agents, tools, MCP and governance for MarTech use cases. Know more: {L} #AgenticAI #MCP", B + "academy/courses/agentic-ai-training.html", bn("07-agentic-ai-mcp.png"))
add("Going further with agents? The Advanced Agentic AI program runs 30 hours of hands-on architecture work. Syllabus and enquiry: {L} #AgenticAI #AIArchitecture", B + "academy/programs/agentic-ai-advanced-30-hour.html", bn("20-agentic-ai-30-hour.png"))
add("Studying for AEP? Our certification-prep page lays out topics to revise and how to practise. It prepares you; it does not promise a result. {L} #AEP #ExamPrep", B + "academy/courses/aep-certification-prep.html")
add("Building a team's skills? Corporate training is tailored to your platforms and use cases, with hands-on labs and assessments. Request a proposal: {L} #CorporateTraining #Upskilling", B + "lp/corporate-adobe-training.html", bn("09-corporate-training.png"))
# YouTube references (8)
add("New to Adobe MarTech? Our YouTube channel has free demo sessions on AEP, Real-Time CDP, AJO, CJA and Agentic AI. Watch one before you decide anything: {L} #YouTube #AdobeExperiencePlatform", YT, "", TXT)
add("Prefer watching to reading? Our demo list brings the free sessions together by topic: {L} #FreeDemo #MarTech", B + "academy/videos.html")
add("Playlists make a learning path: tutorials, CDP, journeys, analytics and Agentic AI in one place. Pick a playlist and start: {L} #LearnAdobe #YouTube", B + "academy/youtube-playlists.html")
add("Subscribe for practical MarTech demos from a working architect: XDM, identity, journeys, measurement and AI agents. {L} #Subscribe #AdobeMarTech", YT, bn("03-adobe-experience-platform.png"))
add("Watched a demo and want more depth? The live batches follow the same style, with labs and Q&A. {L} #LiveTraining", B + "lp/batches.html")
add("Short on time? Start with one demo, then read the matching guide. Demos: {L} Guides: " + B + "learn/ #MicroLearning", B + "academy/videos.html")
add("From video to practice: watch a demo, then try the free quiz and the AJO handout. Free resources: {L} #FreeResources #Adobe", B + "academy/free-resources.html")
add("We reuse real demo recordings instead of placeholder clips. Here is the channel, check what is there today: {L} #YouTube", YT, "", TXT)
# Services (10)
add("An AEP architecture review looks at schemas, identity, ingestion, governance, audiences and activation, then gives a 30/60/90-day plan. Book one: {L} #AEP #Consulting", B + "lp/aep-architecture-review.html", bn("12-adobe-experience-cloud.png"))
add("Adobe Experience Cloud consulting from strategy to implementation. See what we do and how we engage: {L} #AdobeExperienceCloud #MarTechConsulting", B + "services/adobe-experience-cloud.html")
add("Real-Time CDP consulting: identity, audiences, destinations and governance for enterprise data. {L} #RealTimeCDP #CustomerData", B + "services/real-time-cdp.html")
add("Journey Optimizer and Customer Journey Analytics consulting, from journey design to measurement. {L} #AJO #CJA", B + "services/adobe-journey-optimizer.html")
add("Agentic AI and MCP for enterprise MarTech: scoped agents, approved tools and consent enforced in the server. {L} #AgenticAI #EnterpriseAI", B + "services/agentic-ai-mcp.html", bn("07-agentic-ai-mcp.png"))
add("Data engineering for customer data platforms: pipelines, quality and cost, built to last. {L} #DataEngineering #CDP", B + "services/data-engineering.html", bn("14-data-engineering.png"))
add("Consent, governance and privacy design for MarTech, with evidence you can keep. Not legal advice. {L} #Privacy #DataGovernance", B + "services/consent-governance-privacy.html")
add("Need a specialist, not a project? MarTech staff augmentation and contract talent, matched to your backlog. {L} #ContractTalent #MarTech", B + "lp/hire-aep-contract-talent.html")
add("Five ways to work with us: Advise, Teach, Build with you, Build for you, Extend your team. Find yours: {L} #MarTechConsulting", B + "services/engagement-model.html", bn("10-business-consulting.png"))
add("Architecture that solves business challenges, not architecture for its own sake. Our consulting overview: {L} #EnterpriseArchitecture #DigitalTransformation", B + "services/index.html", bn("10-business-consulting.png"))
# Tips and education (12)
add("Pick identity namespaces before you build audiences. Fixing duplicate profiles after launch costs far more than ten minutes of design. Walk-through: {L} #IdentityResolution #AEP", B + "adobe-experience-platform/identity-service.html")
add("Test consent in every environment, not only production. A banner that works on one page can fail on another. {L} #WebSDK #Consent", B + "guides/web-sdk-consent-regression-testing.html", "", TXT)
add("If a journey has no exit event, it has no end. Define exits first, then messages. {L} #AJO #JourneyDesign", B + "guides/loan-onboarding-event-model.html", "", TXT)
add("A holdout group is the only honest way to say a campaign worked. Plan it before you launch. {L} #Measurement #Experimentation", B + "guides/renewal-journey-holdout-design.html", "", TXT)
add("Do you need every click in your CDP? Usually not. Choose signals that change a decision. {L} #CustomerData #CDP", B + "guides/saas-product-usage-signals.html", "", TXT)
add("Name an owner for every data layer. Unowned layers decay quietly. {L} #Customer360 #DataStrategy", B + "guides/customer-360-data-model-layers.html", "", TXT)
add("A schema is easier to extend than to repair. Design for additions. {L} #XDM #DataModelling", B + "adobe-experience-platform/xdm-schemas.html", "", TXT)
add("Agents should draft, people should approve. Where do you draw the line in your team? {L} #AIGovernance #AgenticAI", B + "guides/enterprise-ai-agent-approval-gate.html", "", TXT)
add("Reconcile first, retire later. When moving from Adobe Analytics to CJA, run both until the numbers agree within a tolerance you chose in advance. {L} #CJA #AdobeAnalytics", B + "guides/cja-vs-adobe-analytics.html", "", TXT)
add("What is MCP, and why should data teams care? A plain-language explanation with the safety questions to ask first: {L} #MCP #AI", B + "guides/what-is-mcp.html")
add("AEP vs Real-Time CDP: the question we hear most. A short, honest comparison: {L} #AEP #RealTimeCDP", B + "guides/aep-vs-real-time-cdp.html")
add("Interview season? Revise identity, XDM, ingestion, segmentation and activation with our AEP interview questions. {L} #InterviewPrep #AEP", B + "adobe-experience-platform/interview-questions.html")
# Polls and questions (6)
add("Poll: which Adobe topic should we cover next? 1) AEP architecture 2) Real-Time CDP 3) AJO 4) CJA 5) Agentic AI. Reply with a number. Past topics: {L} #Poll #AdobeMarTech", B + "academy/videos.html", "", TXT)
add("Question for MarTech leaders: who owns identity in your organisation, marketing, data or IT? Our view on operating models: {L} #MarTech #Leadership", B + "guides/martech-coe-operating-model-raci.html", "", TXT)
add("What stops your AEP project from moving faster: schema, identity, ingestion or activation? Share below. If it is one of these, start here: {L} #AEP", B + "adobe-experience-platform/", "", TXT)
add("Which would you rather learn first this quarter: Web SDK, CJA or Agentic AI? Compare the course pages: {L} #Upskilling", B + "academy/catalogue.html", "", TXT)
add("Hiring or learning? We run both: contract talent for teams and live training for individuals. Tell us which you need: {L} #MarTechCareers", B + "contact-us.html", "", TXT)
add("Which role fits you: architect, engineer, analyst, consultant? Our MarTech roles guide explains each path: {L} #CareerPath #MarTech", B + "academy/martech-roles.html", "", TXT)
# Brand and community (8)
add("Learn. Architect. Implement. Transform. That is how we teach and how we consult. Meet Infiante360 Tech Academy: {L} #Infiante360 #TechAcademy", B, bn("08-career-transformation.png"))
add("Infiante360 is independent. We are not affiliated with or endorsed by Adobe, and Adobe product names belong to their owners. We teach and advise on the platforms professionals use. {L} #Transparency", B + "about-us.html", "", TXT)
add("Questions about a course, a team program or consulting? Call or WhatsApp +91 82968 93895, or write to us through the contact page: {L} #Infiante360", B + "contact-us.html", bn("10-business-consulting.png"))
add("Join the Academy community for questions, demos and learning notes from other MarTech practitioners: {L} #Community #MarTech", B + "academy/community.html")
add("From a different background? Our career-paths guide maps developers, analysts, testers and freshers into Adobe MarTech roles: {L} #CareerSwitch", B + "academy/career-paths-by-background.html", bn("08-career-transformation.png"))
add("Practice with simulators built around real implementation patterns, not just slides. Try one: {L} #HandsOnLearning", B + "academy/simulators.html")
add("Research and insights: how MCP, customer data and enterprise architecture fit together. Explore: {L} #Research #EnterpriseAI", B + "research/index.html", bn("11-research-intelligence.png"))
add("Everything in one place: services, programs, guides, demos and contact. Bookmark our links hub: {L} #Infiante360", B + "links.html")
assert len(posts) == 100, len(posts)

# ---- schedule: weekdays 09:30 and 18:30 IST, weekends 11:00 ----
slots, d = [], dt.date(2026, 11, 27)
while len(slots) < 100:
    for hm in (("09:30", "18:30") if d.weekday() < 5 else ("11:00",)):
        slots.append(f"{d.isoformat()} {hm}")
    d += dt.timedelta(days=1)
# interleave types so no two guide posts or two banner posts run back to back
guides, rest = posts[:36], posts[36:]
order, gi, ri = [], 0, 0
while gi < len(guides) or ri < len(rest):
    if ri < len(rest): order.append(rest[ri]); ri += 1
    if ri < len(rest): order.append(rest[ri]); ri += 1
    if gi < len(guides): order.append(guides[gi]); gi += 1
def xlen(t): return len(re.sub(r"https?://\S+", "x" * 23, t))
out, seen = [], set()
for n, ((text, link, media, nets), slot) in enumerate(zip(order, slots), 1):
    url = f"{link}{'&' if '?' in link else '?'}utm_source=social&utm_medium=organic&utm_campaign=cal100-{n:03d}"
    t = text.replace("{L}", url)
    if "x" in nets.split("|") and xlen(t) > 280:
        nets = "|".join(x for x in nets.split("|") if x != "x")
    if "instagram" in nets.split("|"):
        t = t.replace(url, "(link in bio) " + B.rstrip("/").replace("https://", ""), 1) if False else t
    assert t not in seen; seen.add(t)
    out.append([t, media, slot, nets, "", "", ""])
with open(os.path.join(ROOT, "data/social/calendar-100.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["text", "media_url", "date", "networks", "title", "profile", "media_type"]); w.writerows(out)
print(len(out), "rows;", sum(1 for r in out if "x" not in r[3].split("|")), "rows dropped from X (over 280)")
