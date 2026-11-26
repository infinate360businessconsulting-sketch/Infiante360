"""Builds data/social/youtube-descriptions-100.csv: one YouTube title + description + tags per calendar post.
Opening lines reuse the post's own text, so the video, post and page say the same thing. No chapters or claims about video contents are invented:
add real timestamps after recording. Run: python3 -I scripts/build_youtube_descriptions.py"""
import csv, glob, json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B = "https://infiante360techacademy.com/"
rows = list(csv.DictReader(open(os.path.join(ROOT, "data/social/calendar-100.csv"), encoding="utf-8")))
specs = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(ROOT, "data/visuals/specs/*.json")))]
# titles for the 64 hand-written posts, in the same order as scripts/build_social_calendar.py
T = ["Weekday Morning Live Batch: Adobe MarTech and Agentic AI", "Agentic AI + Adobe CDP Weekend Batch: 16 Live Sessions", "Adobe MarTech SME Batch: Advanced AEP, RTCDP, AJO and CJA",
"Six-Day MarTech SME Accelerator: Live Evenings", "Adobe MarTech Career Accelerator: 90 Days of Live Learning", "CXO Hive: MarTech Architecture Leadership for Executives",
"Which Adobe MarTech Batch Fits You?", "Live Batches: Weekday, Weekend, SME and Accelerator", "Course Catalogue: Adobe MarTech, AI and Data Courses", "Practical Learning Without Placement Promises",
"Adobe Experience Platform Course: Data to Intelligent Experiences", "Adobe Real-Time CDP Course: Data, Identity and Activation", "Adobe Journey Optimizer Course: Journeys, Messages, Decisioning",
"Customer Journey Analytics Course: Data Views and Cross-Channel Analysis", "Adobe Web SDK and Tags Course: Datastreams, Events, Validation", "Adobe Analytics Course: Implementation, Reporting, Analysis",
"Agentic AI and MCP Course for MarTech", "Advanced Agentic AI Program: 30 Hours of Architecture", "AEP Certification Preparation: Topics to Revise", "Corporate Adobe Training: Tailored Team Programs",
"Free Adobe MarTech Demos on YouTube", "Adobe MarTech Demo List by Topic", "Adobe MarTech Playlists: Build a Learning Path", "Subscribe: Practical Adobe MarTech Demos",
"From Demo to Live Batch: Learn Adobe MarTech Hands-On", "Start with One Demo, Then Read the Guide", "Free Adobe Resources: Quiz and AJO Handout", "Infiante360 Tech Academy Channel Tour",
"AEP Architecture Review: What We Assess", "Adobe Experience Cloud Consulting Overview", "Real-Time CDP Consulting: Identity, Audiences, Destinations", "Journey Optimizer and CJA Consulting",
"Agentic AI and MCP Consulting for Enterprise MarTech", "Data Engineering for Customer Data Platforms", "Consent, Governance and Privacy Design for MarTech", "MarTech Contract Talent and Staff Augmentation",
"Five Ways to Work with Infiante360", "Enterprise Architecture Consulting for MarTech", "Identity Namespaces in AEP: Design Before You Build", "Test Web SDK Consent in Every Environment",
"Journey Exit Events: Design Them First", "Holdout Groups: The Honest Way to Prove a Campaign Worked", "Which Signals Belong in Your CDP?", "Name an Owner for Every Customer Data Layer",
"XDM Schemas: Design for Extension", "AI Agents: Draft or Approve? Set the Line", "Adobe Analytics to CJA: Reconcile First", "What Is MCP? A Plain-Language Explanation",
"AEP vs Real-Time CDP: What Is the Difference?", "AEP Interview Questions to Revise", "Poll: Which Adobe Topic Should We Cover Next?", "Who Owns Identity in Your Organisation?",
"What Slows Your AEP Project?", "Web SDK, CJA or Agentic AI: What to Learn First", "Hiring or Learning? Two Ways We Help", "Which MarTech Role Fits You?",
"Learn. Architect. Implement. Transform.: Meet Infiante360", "Independent of Adobe: How We Work", "Contact Infiante360 Tech Academy", "Join the Infiante360 Learning Community",
"Career Paths into Adobe MarTech by Background", "Hands-On Simulators for Adobe MarTech", "Research and Insights: MCP, Customer Data, Architecture", "Infiante360 Links Hub: Services, Programs, Guides"]
assert len(T) == 64
# order used by the calendar: 2 hand-written, 1 guide, repeated
guides, rest = specs, T
order, gi, ri = [], 0, 0
while gi < len(guides) or ri < len(rest):
    for _ in range(2):
        if ri < len(rest): order.append(rest[ri]); ri += 1
    if gi < len(guides): order.append(guides[gi]); gi += 1
LINKS = f"""Register for live batches: {B}lp/batches.html
All courses: {B}academy/catalogue.html
Free demos: {B}academy/videos.html
Executive program (CXO Hive): {B}academy/programs/executive-architecture-leadership.html
Corporate training: {B}training/corporate-training.html
Enterprise consulting: {B}services/index.html
Contact: {B}contact-us.html
Subscribe: https://www.youtube.com/@Infiante360TechAcademy
WhatsApp / call: +91 82968 93895 | Email: infinate360businessconsulting@gmail.com"""
DISC = "Infiante360 is independent and is not affiliated with or endorsed by Adobe. Adobe product names are trademarks of their owners. This video is for education; jobs, salaries and certifications are not guaranteed and outcomes depend on individual effort."
out = []
for n, (r, item) in enumerate(zip(rows, order), 1):
    text = re.sub(r"https?://\S+", "", r["text"])
    tags = re.findall(r"#\w+", text)
    body = re.sub(r"#\w+", "", text).replace("(link in bio)", "").strip()
    body = re.sub(r"\s+", " ", body).rstrip(":").strip()
    if body and body[-1] not in ".?!": body += "."
    if isinstance(item, dict):
        title = f"{item['title']}: {item['subtitle']}"[:80] + " | Infiante360"
    else:
        title = item
    title = title[:95]
    link = re.search(r"https?://\S+", r["text"]).group(0)
    page = link.split("?")[0]
    desc = f"""{body}

Read the full page: {page}

{LINKS}

Chapters: add real timestamps after recording (00:00 start, at least three, each 10 seconds or longer).

{DISC}

{' '.join(dict.fromkeys(tags[:2] + ['#Infiante360']))[:200]}"""
    kw = ", ".join(dict.fromkeys([t[1:] for t in tags] + ["Infiante360", "Infiante360 Tech Academy", "adobe martech", "adobe experience platform"]))
    out.append([n, r["date"], title, desc, kw, page])
with open(os.path.join(ROOT, "data/social/youtube-descriptions-100.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["post_no", "date", "youtube_title", "youtube_description", "tags", "page"]); w.writerows(out)
print(len(out), max(len(o[3]) for o in out), max(len(o[2]) for o in out))
