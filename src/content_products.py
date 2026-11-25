"""Product pages (SkillSurf, Explorer, Startup Studio, CXO Hive) and proposed events, sitemap4.xml. Owner go-ahead 2026-11-25.

Rules: no dates, fees, counts, job numbers, ratings, outcomes, partnerships or legal-entity claims. Events have date = to be announced.
Jobs are not scraped or listed; a feed needs owner-named, terms-checked sources. Salesforce/Braze training is a proposed extension."""
import html
from content_cases import pills, REGISTER, WHATSAPP_MSG
from content_group import _row_links, DATE, PHONE, VENDOR_NOTE

e = html.escape
WA = ("WhatsApp " + PHONE, WHATSAPP_MSG)
REG = ("Register interest", REGISTER)

# ---------------------------------------------------------------- Explorer product pages
TECH = [("Adobe Experience Cloud", "AEP, Real-Time CDP, AJO, CJA, Analytics, Target, AEM, Web SDK, Campaign, Marketo, Commerce, Workfront"),
        ("Salesforce", "CRM, Marketing Cloud, Data Cloud, Sales Cloud, Service Cloud, Commerce Cloud"),
        ("Marketing automation", "Braze, HubSpot, Iterable, Eloqua, Klaviyo, ActiveCampaign, MoEngage, CleverTap"),
        ("Customer data platforms", "Twilio Segment, Tealium, Treasure Data, mParticle, Hightouch, RudderStack"),
        ("Analytics", "Google Analytics 4, Adobe Analytics, Amplitude, Mixpanel"), ("Business intelligence", "Tableau, Power BI, Looker, Qlik"),
        ("Data engineering", "Snowflake, Databricks, BigQuery, Redshift, Spark, Kafka, Airflow, dbt"),
        ("AI engineering", "Agentic AI, MCP, RAG, LLMs, LangChain, LangGraph"), ("Cloud", "AWS, Azure, Google Cloud"),
        ("CRM and enterprise", "Microsoft Dynamics, SAP, Oracle, Zoho"), ("Programming", "Python, Java, JavaScript, TypeScript, SQL"),
        ("Architecture", "Enterprise and solution architecture, microservices, API integration")]

EX_TECH = dict(
    path="products/explorer-jobs-by-technology.html", title="Explorer: Jobs by Technology Stack Plan (12 Families)",
    desc="How Infinate360Explorer would organise MarTech and data jobs into 12 technology families, from Adobe and Salesforce to cloud and AI. Planned, not live.",
    h1="Explorer jobs by technology: the 12 families we plan to cover", kicker="Explorer · Product plan", nav="Jobs by technology", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["martech jobs by technology", "adobe experience platform jobs", "salesforce marketing cloud jobs", "braze hubspot jobs", "snowflake data engineering jobs", "vendor neutral technology career platform"],
    answer="Infinate360Explorer plans to group jobs into 12 technology families, from Adobe Experience Cloud and Salesforce to data engineering, AI and cloud. Each family would get one landing page rather than one page per product synonym. No vacancies are listed on this site yet. Counts would be shown only from authorised, de-duplicated sources, with a last-refreshed time.",
    sections=[
        ("Twelve technology families", _row_links(["Family", "Platforms and skills"], TECH) + f'<p class="note">Planned taxonomy, not a live job board. {e(VENDOR_NOTE)}</p>'),
        ("What each technology page would show", '<ul class="checklist"><li>Plain introduction and the roles that use the technology</li><li>Vacancies from permitted sources, with the source named and a link to the original application</li><li>Last refreshed time, and whether a figure is an exact count or a sample</li><li>Common job titles and requested skills</li><li>Salary figures only where a reliable, permitted source exists, with place, currency, period and date</li><li>Related assessments, courses and an optional alert signup</li></ul>'),
        ("Why families, not thousands of pages", '<p>One page per family avoids near-duplicate pages for every spelling of a tool. Roles are covered on the <a href="explorer-jobs-by-role.html">roles page</a>, and the brand is described on the <a href="../ecosystem/infinate360-explorer.html">Explorer page</a>.</p>'
         + pills(REG, WA, ("All products", "index.html"))),
    ],
    faqs=[("Are there live jobs here?", "No. This page is the plan. A jobs feed starts only after sources and their terms are confirmed."),
          ("Does listing a technology mean a vendor endorses Explorer?", "No. Product names belong to their owners and no partnership is claimed.")],
    related=["products/index.html", "products/explorer-jobs-by-role.html", "ecosystem/infinate360-explorer.html", "stacks/index.html"], sources=[], sitemap4=True)

ROLES = [("Marketing Technology Analyst", "MarTech"), ("Marketing Operations Manager", "MarTech"), ("Marketing Automation Specialist", "MarTech"), ("MarTech Technologist", "MarTech"),
         ("MarTech SME", "MarTech"), ("MarTech Architect", "Architecture"), ("Salesforce Marketing Cloud Developer", "Salesforce"), ("Salesforce Data Cloud Consultant", "Salesforce"),
         ("CRM Manager", "CRM"), ("Marketing Analytics Manager", "Analytics"), ("Adobe AEP Developer", "Adobe"), ("Adobe AEP Architect", "Adobe"), ("Real-Time CDP Consultant", "Adobe"),
         ("AJO Developer", "Adobe"), ("CJA Analyst", "Adobe"), ("Customer 360 Engineer", "Data"), ("Agentic AI Engineer", "AI"), ("MCP Developer", "AI"), ("LLM Engineer", "AI"),
         ("AI Solutions Architect", "AI"), ("Data Engineer", "Data"), ("Snowflake Architect", "Data"), ("Cloud Architect", "Cloud"), ("Enterprise Architect", "Architecture"),
         ("Digital Transformation Consultant", "Consulting"), ("Technology Director", "Leadership"), ("Head of MarTech", "Leadership"), ("Chief Technology Officer", "Leadership"),
         ("Chief Data Officer", "Leadership"), ("Chief AI Officer", "Leadership")]
EX_ROLE = dict(
    path="products/explorer-jobs-by-role.html", title="Explorer: 30 MarTech, Data and AI Job Roles Mapped",
    desc="Thirty MarTech, data, AI and leadership roles Infinate360Explorer plans to cover, grouped by family, and how titles are normalised. A plan, not a job board.",
    h1="Explorer job roles: 30 titles and how they group", kicker="Explorer · Product plan", nav="Jobs by role", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["martech architect jobs", "adobe aep developer jobs", "agentic ai engineer jobs", "customer 360 engineer role", "head of martech role", "mcp developer role", "chief ai officer role"],
    answer="Infinate360Explorer plans to map 30 job titles, from Marketing Technology Analyst and Adobe AEP Developer to MCP Developer and Chief AI Officer, into role families. Similar titles would be normalised so a role has one page, not one per spelling. This is a planned taxonomy. No vacancies are listed, and job counts would appear only from authorised sources.",
    sections=[
        ("Thirty planned roles", _row_links(["Role", "Family"], ROLES)),
        ("How titles would be normalised", '<ul class="checklist"><li>Equivalent titles resolve to one canonical role, with the original title kept on each vacancy</li><li>Seniority is a filter, not a separate page</li><li>Geographic limits on remote roles are shown, never presented as worldwide</li></ul>'),
        ("Next step for you", '<p>Pick the closest role, then compare it with your own skills using the free <a href="../academy/career-accelerator-roadmap.html">90-day roadmap</a>. Technology families are on the <a href="explorer-jobs-by-technology.html">technology page</a>.</p>'
         + pills(REG, WA, ("All products", "index.html"))),
    ],
    faqs=[("Are these roles hiring now?", "This page does not say. It lists roles Explorer plans to cover, not open vacancies."),
          ("Why are there no salary figures?", "Salary data is shown only from reliable, permitted sources with place, currency and date. None is published here.")],
    related=["products/index.html", "products/explorer-jobs-by-technology.html", "ecosystem/infinate360-explorer.html", "academy/career-accelerator-roadmap.html"], sources=[], sitemap4=True)

SCAN = [("Resume parsing", "Read confirmed details from PDF and DOCX, then let the candidate correct them"), ("Keyword matching", "Compare resume skills with a job description the candidate supplies"),
        ("Missing keywords", "List relevant skills with no supporting evidence in the resume"), ("Readability and formatting", "Flag structure and common parsing problems"),
        ("Achievement prompts", "Suggest where to describe genuine outcomes"), ("Learning suggestions", "Link a skill gap to an assessment or course, as optional")]
EX_SCAN = dict(
    path="products/explorer-resume-scanner.html", title="Explorer Resume Keyword Scanner: Plan, Method and Limits",
    desc="What the planned Infinate360Explorer resume scanner will check, how it will score, and what it will never claim, such as an official employer ATS score.",
    h1="Resume keyword scanner: what it will do and what it will not", kicker="Explorer · Product plan", nav="Resume scanner", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["resume keyword scanner", "resume job description matcher", "ats resume formatting checker", "skill gap analyzer martech", "resume for adobe martech roles"],
    answer="The planned Explorer resume scanner compares your resume with a job description you supply, then shows matched and missing keywords, readability and formatting issues, and optional learning suggestions. Its score would be explained as a keyword-alignment estimate, never an employer ATS score. It is not live yet, and uploads would be private and need a secure backend first.",
    sections=[
        ("Planned checks", _row_links(["Check", "What it would do"], SCAN)),
        ("Rules it will keep", '<ul class="checklist"><li>The score is Explorer\'s own keyword-alignment estimate and is explained with its limits</li><li>It never suggests adding a skill you do not have</li><li>Resumes are private, encrypted and deletable on request</li><li>No resume goes to an employer without your explicit choice</li><li>Uploaded files and pasted job text are treated as untrusted input</li></ul>'),
        ("Status", '<p class="note">Not built or live. Secure upload, parsing and storage must exist first. Until then, use the <a href="../academy/portfolio-projects-and-interview-scenarios.html">portfolio and interview scenarios</a> to prepare.</p>'
         + pills(REG, WA, ("All products", "index.html"))),
    ],
    faqs=[("Does a high score mean I will get an interview?", "No. Employers use their own systems and people. The scanner only estimates keyword alignment."),
          ("Can I try it today?", "No. This page describes the plan. We will announce when a working version exists.")],
    related=["products/index.html", "products/explorer-jobs-by-role.html", "ecosystem/infinate360-explorer.html", "events/resume-keyword-clinic.html"], sources=[], sitemap4=True)

EMP = [("Employer registration", "Verified organisation accounts"), ("Post a job", "Publish authorised vacancies"), ("Manage vacancies", "Edit, close and archive roles"),
       ("Applications", "Receive applications the candidate chose to send"), ("Contract talent", "Submit specialist resource needs"), ("Corporate training and consulting", "Team enablement and enterprise projects"),
       ("Sponsored jobs", "Promoted vacancies, clearly labelled as sponsored")]
EX_EMP = dict(
    path="products/explorer-for-employers.html", title="Explorer for Employers: Hiring and Team Enablement Plan",
    desc="The planned employer side of Infinate360Explorer: verified job posting, contract talent requests and corporate training. Candidates control what is shared.",
    h1="Explorer for employers: find talent, build capability", kicker="Explorer · Product plan", nav="For employers", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["post martech jobs", "contract adobe talent", "hire aep developers", "martech corporate training for hiring teams", "employer verification job board", "sponsored job disclosure"],
    answer="Infinate360Explorer plans an employer side with verified accounts, job posting, contract talent requests and links to corporate training and consulting. Candidates would decide which employers see their resume, and sponsored jobs would be labelled. None of it is live. Today, hiring teams can ask about contract talent or team training through the contact route.",
    sections=[
        ("Planned employer features", _row_links(["Feature", "Purpose"], EMP)),
        ("Candidate protections", '<ul class="checklist"><li>Employers get no unrestricted access to resumes</li><li>Candidates approve sharing, employer by employer</li><li>No candidate contact lists are sold or exported in bulk</li><li>Sponsored listings carry a visible disclosure</li></ul>'),
        ("Available now", '<p>Hiring teams can already ask for <a href="../services/contract-hiring.html">contract hiring support</a> or <a href="../training/corporate-training.html">corporate training</a>.</p>'
         + pills(("Contact us", "../contact-us.html"), WA, ("All products", "index.html"))),
    ],
    faqs=[("Can I post a job on this site today?", "No. Posting needs employer verification and moderation that are not built yet."),
          ("Do you share candidate details with employers?", "Not without the candidate's explicit approval for that employer.")],
    related=["products/index.html", "services/contract-hiring.html", "training/corporate-training.html", "ecosystem/infinate360-explorer.html"], sources=[], sitemap4=True)

MAP = [("Adobe AEP, AJO and CJA", "Adobe Experience Cloud", "Developer, consultant, architect"), ("CXO Hive", "Architecture, AI, CDP", "CTO, CDO, enterprise architect"),
       ("Live customised MarTech programme", "Chosen MarTech stack", "SME, consultant, specialist"), ("Agentic AI and MCP", "Agents, LLMs, MCP", "AI engineer, AI architect"),
       ("Customer 360", "Identity, CDP, data engineering", "CDP engineer, data architect"), ("Adobe Analytics", "Digital measurement", "Analytics developer, analyst"),
       ("Web SDK", "Data collection, XDM", "Implementation engineer"), ("Snowflake data engineering", "SQL, Snowflake, pipelines", "Data engineer")]
EX_MAP = dict(
    path="products/explorer-course-job-map.html", title="Explorer Course-to-Role Map: Skills Behind Each Course",
    desc="How Infinate360Explorer would connect each course's skills to the job roles that use them, with Salesforce and Braze marked as proposed, not offered.",
    h1="Course-to-role map: which skills lead where", kicker="Explorer · Product plan", nav="Course-to-role map", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["adobe course career path", "aep developer training roles", "agentic ai course jobs", "cja analyst training", "snowflake data engineer course", "martech training to job role"],
    answer="This map connects eight programme themes to the technologies they teach and the job roles that use them, such as AEP to developer, consultant and architect. It shows relevance, not outcomes: no placement or hiring is promised. Salesforce and Braze training are proposed extensions that would open only after trainer capability is confirmed. Live job demand would come from authorised sources.",
    sections=[
        ("Programme themes and roles", _row_links(["Programme theme", "Technologies", "Relevant roles"], MAP)),
        ("Proposed extensions", '<p class="note">Salesforce Marketing Cloud and Braze training are proposals. They will be offered only after trainer capability and a confirmed course exist.</p>'),
        ("How demand would be shown", '<ul class="checklist"><li>Counts calculated from authorised, de-duplicated vacancies, never typed in by hand</li><li>A last-refreshed time on every figure</li><li>Exact counts kept separate from sampled observations</li><li>No claim of complete job-market coverage</li></ul>'
         + pills(("Academy programmes", "../academy/index.html"), REG, ("All products", "index.html"))),
    ],
    faqs=[("Does finishing a course lead to a job?", "No outcome is promised. The map shows which skills roles commonly use, not what will happen to you."),
          ("Where do live demand figures come from?", "None are shown yet. They would come only from authorised vacancy sources.")],
    related=["products/index.html", "products/explorer-jobs-by-role.html", "academy/index.html", "ecosystem/infinate360-explorer.html"], sources=[], sitemap4=True)

# ---------------------------------------------------------------- CXO Hive
CXO_LEARN = [("Strategy and transformation", "Set up a MarTech and AI centre of excellence, define enterprise AI and Agentic AI strategy, shape a customer data platform strategy, weigh technology investments"),
             ("Architecture and governance", "Enterprise architecture and operating models, customer data governance, responsible AI adoption, integration strategy, modernisation planning"),
             ("Global capability and delivery", "Move a global capability centre from delivery to ownership, build scalable delivery models, grow internal capability, reuse implementation frameworks")]
CXO_OUT = ["Technology investment case", "Target enterprise architecture", "Capability maturity assessment", "MarTech and AI operating model", "Prioritised implementation roadmap", "90-day transformation action plan"]
CXO_PROG = dict(
    path="products/cxo-hive-programme.html", title="CXO Hive Programme: Executive MarTech and AI Architecture",
    desc="What the CXO Hive executive programme covers: AI and MarTech centre of excellence, GCC transformation, governance and a 90-day plan. Fees on request.",
    h1="CXO Hive programme: lead the transformation, don't just manage it", kicker="CXO Hive · Programme", nav="CXO Hive programme", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["cxo hive programme", "executive martech ai centre of excellence", "gcc to global transformation", "enterprise ai strategy for cto", "customer data platform strategy executives", "enterprise architecture leadership course"],
    answer="The CXO Hive programme is for CXOs, technology leaders and enterprise architects who build MarTech, customer data and AI capability at scale. It covers strategy, architecture and governance, and global capability, and produces six deliverables including a target architecture and a 90-day action plan. Dates, duration, fees and post-programme support are confirmed on request, not published here.",
    sections=[
        ("What you learn", _row_links(["Area", "Topics"], CXO_LEARN)),
        ("Deliverables you take away", "<ul class=\"checklist\">" + "".join(f"<li>{e(x)}</li>" for x in CXO_OUT) + "</ul>"),
        ("Who should attend", '<ul class="checklist"><li>CIOs, CTOs, chief data officers and CMOs</li><li>Enterprise and solution architects</li><li>Technology directors and senior delivery leaders</li><li>Global capability centre leadership and digital transformation leads</li></ul>'),
        ("Delivery, fees and enquiry", '<p>Format is live sessions, executive discussion and architecture exercises. Duration, post-programme support, fees and any member discount are confirmed in writing on enquiry; this page does not state them. The detailed syllabus is on the <a href="../academy/programs/executive-architecture-leadership.html">executive architecture programme page</a>.</p>'
         + pills(("Request details", REGISTER), WA, ("Corporate proposal", "../training/corporate-training.html"))),
    ],
    faqs=[("What does it cost and how long is it?", "We confirm fees, duration and dates when you enquire. They are not published on this page."),
          ("Can my whole leadership team attend privately?", "Yes. Ask for a corporate proposal and share your goals.")],
    related=["products/index.html", "ecosystem/cxo-hive.html", "academy/programs/executive-architecture-leadership.html", "events/martech-ai-coe-roundtable.html"], sources=[], sitemap4=True)

# ---------------------------------------------------------------- Events (all proposed, no dates)
NOTE_EV = "Proposed session. Date, time, speaker and fee are to be announced, and nothing is scheduled until a confirmation is posted here."


def _event(slug, product, title, desc, h1, fmt, aud, mins, agenda, takeaway, bring, kw, ans, faqs, rel):
    return dict(
        path=f"events/{slug}.html", title=title, desc=desc, h1=h1, kicker=f"Events · {product}", nav=title.split(":")[0], schema="WebPage", category="Events", date=DATE,
        keywords=kw, answer=ans,
        sections=[
            ("At a glance", _row_links(["Item", "Detail"], [("Product", product), ("Format", fmt), ("For", aud), ("Planned length", mins), ("Date and time", "To be announced"), ("Fee", "Stated when the date is confirmed")])
             + f'<p class="note">{e(NOTE_EV)}</p>'),
            ("Agenda", "<ol>" + "".join(f"<li>{e(a)}</li>" for a in agenda) + "</ol>"),
            ("What you leave with", f"<p>{e(takeaway)}</p>"),
            ("What to bring", f"<p>{e(bring)}</p>" + pills(REG, WA, ("All events", "index.html"))),
        ],
        faqs=faqs, related=rel, sources=[], sitemap4=True)


EVENTS = [
    _event("resume-keyword-clinic", "Infinate360Explorer", "Resume Keyword Clinic for MarTech and Data Roles",
           "A proposed hands-on clinic on matching your resume to a MarTech or data job description honestly. Date to be announced; register interest.",
           "Resume keyword clinic for MarTech and data roles", "Live workshop with exercises", "Jobseekers and career changers in MarTech, data and AI", "About 90 minutes",
           ["How job descriptions are structured: required versus preferred skills", "Matching your real experience to the wording, without adding skills you lack", "Turning duties into evidence of outcomes you can support", "Formatting problems that confuse parsers", "Questions on your own resume"],
           "A marked-up checklist for your resume and a short list of skills worth learning next.", "Your resume and one job description you want to apply for.",
           ["resume keyword clinic", "resume for martech jobs", "match resume to job description", "adobe resume keywords", "resume workshop india"],
           "This proposed 90-minute clinic shows MarTech and data jobseekers how to match a resume to a job description honestly. You would learn required versus preferred skills, evidence-based wording and common formatting problems. Date, speaker and fee are to be announced, and it is not scheduled until confirmed here.",
           [("Will you review my resume privately?", "Group exercises use your own copy. A private review would be arranged separately and kept confidential."), ("Does this guarantee interviews?", "No. It helps you present real experience clearly; outcomes depend on you and the market.")],
           ["events/index.html", "products/explorer-resume-scanner.html", "academy/career-accelerator-roadmap.html", "ecosystem/infinate360-explorer.html"]),
    _event("career-roadmap-skill-gap-session", "Infinate360Explorer", "Career Roadmap and Skill-Gap Session for Adobe and AI",
           "A proposed session to map your current skills to a target Adobe MarTech or AI role and plan the next 90 days. Date to be announced; register interest.",
           "Career roadmap and skill-gap session", "Guided group session", "Analysts, developers and engineers moving into Adobe MarTech or Agentic AI", "About 2 hours",
           ["Rate your current skills honestly against a target role", "Find the two or three gaps that matter most", "Choose practice projects that prove each skill", "Draft a 30-60-90 day plan", "Optional next learning steps"],
           "A one-page plan with target role, gaps, projects and a weekly study rhythm.", "A target role in mind and a rough list of your current tools.",
           ["career roadmap session", "skill gap analysis martech", "adobe career transition plan", "agentic ai career plan", "90 day learning plan"],
           "This proposed two-hour session helps analysts, developers and engineers moving into Adobe MarTech or Agentic AI map current skills to a target role. You would rate skills, find the main gaps and draft a 30-60-90 day plan. Date, speaker and fee are to be announced and nothing is scheduled yet.",
           [("Do I need to know Adobe tools already?", "No. Bring your current skills; the session helps you plan the path in."), ("Is a job offered at the end?", "No. It is a planning session, with no placement promised.")],
           ["events/index.html", "academy/career-accelerator-roadmap.html", "products/explorer-course-job-map.html", "ecosystem/infinate360-explorer.html"]),
    _event("martech-ai-coe-roundtable", "CXO Hive", "MarTech and AI Centre of Excellence Roundtable (Proposed)",
           "A proposed executive roundtable on setting up a MarTech and AI centre of excellence: scope, operating model and governance. Date to be announced.",
           "MarTech and AI centre of excellence roundtable", "Closed executive roundtable", "CIOs, CTOs, CDOs, CMOs and enterprise architects", "About 90 minutes",
           ["Why organisations set up a centre of excellence and what it owns", "Operating model options: central, federated, hybrid", "Governance for customer data and AI use", "Funding, skills and measurement", "Open discussion under the Chatham House rule"],
           "A comparison of operating model options and a list of questions to take back to your leadership team.", "A short description of your current MarTech or AI setup, kept confidential.",
           ["martech centre of excellence", "ai centre of excellence roundtable", "cxo roundtable india", "martech operating model", "enterprise ai governance leaders"],
           "This proposed executive roundtable covers setting up a MarTech and AI centre of excellence: what it owns, operating model options and governance. It is for CIOs, CTOs, CDOs, CMOs and architects. Date, moderator and fee are to be announced, and it is not scheduled until confirmed here.",
           [("Will company details be shared?", "No. Discussion would be under the Chatham House rule, and attendees are not named publicly without consent."), ("Is this a sales presentation?", "It is planned as a discussion, not a product pitch.")],
           ["events/index.html", "products/cxo-hive-programme.html", "ecosystem/cxo-hive.html", "services/index.html"]),
    _event("gcc-global-transformation-forum", "CXO Hive", "GCC-to-Global Transformation Forum (Proposed)",
           "A proposed forum for global capability centre leaders on moving from delivery to capability ownership in MarTech, data and AI. Date to be announced.",
           "GCC-to-global transformation forum", "Closed leadership forum", "Global capability centre leaders and digital transformation heads", "About 2 hours",
           ["From service delivery to product and capability ownership", "Building reusable assets and frameworks", "Growing internal technical depth", "Working with the parent organisation and partners", "Peer questions and takeaways"],
           "A maturity checklist and a short list of actions for the next quarter.", "One capability you want to move up the value chain.",
           ["gcc leadership forum", "global capability centre transformation", "gcc to global capability", "gcc martech ai capability", "capability centre leaders india"],
           "This proposed forum is for global capability centre leaders who want to move from delivery to capability ownership in MarTech, data and AI. Topics include reusable assets, internal depth and working with the parent organisation. Date, speakers and fee are to be announced and nothing is scheduled yet.",
           [("Who can attend?", "Capability centre and transformation leaders. Attendee details stay private."), ("Is a fee charged?", "Any fee is stated when the date is confirmed.")],
           ["events/index.html", "products/cxo-hive-programme.html", "ecosystem/cxo-hive.html", "training/corporate-training.html"]),
    _event("choose-your-enterprise-technology-path", "SkillSurf", "Choose Your Enterprise Technology Path (Proposed Session)",
           "A proposed session helping IT professionals compare enterprise technology paths such as ERP, Salesforce, data and cloud. Date to be announced.",
           "Choose your enterprise technology path", "Live information session", "IT professionals and graduates choosing a specialism", "About 75 minutes",
           ["How enterprise technology areas differ: ERP, CRM, data, cloud, security, AI", "Typical roles and starting skills in each area", "Questions to ask yourself before choosing", "How to test a path with a small project", "Q and A"],
           "A short comparison sheet and a first small project to try in your chosen area.", "Your background and two areas you are considering.",
           ["choose it career path", "enterprise technology career guidance", "sap salesforce data cloud career choice", "it training path india", "skillsurf session"],
           "This proposed 75-minute session helps IT professionals and graduates compare enterprise technology paths such as ERP, CRM, data, cloud, security and AI. You would see typical roles, starting skills and a way to test a path with a small project. Date, speaker and fee are to be announced.",
           [("Will courses in every area be offered?", "No. Course availability is confirmed separately; this session is general guidance."), ("Is this vendor-endorsed?", "No vendor partnership or endorsement is claimed.")],
           ["events/index.html", "ecosystem/skillsurf.html", "products/index.html", "training/career-transition.html"]),
    _event("corporate-team-enablement-briefing", "SkillSurf", "Corporate Team Enablement Briefing for L&D Leaders",
           "A proposed briefing for learning and development leaders on planning team technology training: needs, format, assessment and measures. Date to be announced.",
           "Corporate team enablement briefing", "Briefing with worked examples", "L&D leaders, capability leads and delivery managers", "About 60 minutes",
           ["Turning a project need into a skills need", "Choosing format: workshop, lab or project-based", "Assessing before and after training", "Measures that mean something, and ones that do not", "How to request a tailored proposal"],
           "A one-page training brief template you can reuse.", "A team skills need, even if rough.",
           ["corporate technology training planning", "l and d team upskilling", "team enablement briefing", "corporate training proposal", "capability building leaders"],
           "This proposed 60-minute briefing helps learning and development leaders turn a project need into a team training plan. Topics include format choice, before-and-after assessment and measures that matter, with a reusable training brief. Date, speaker and fee are to be announced, and it is not scheduled until confirmed here.",
           [("Can we skip the briefing and ask for a proposal?", "Yes. Use the corporate training page and share your goals."), ("Is it specific to one vendor?", "No. It covers planning, not a single product.")],
           ["events/index.html", "training/corporate-training.html", "ecosystem/skillsurf.html", "products/index.html"]),
    _event("idea-validation-sprint", "Startup Studio", "Idea Validation Sprint for First-Time Founders (Proposed)",
           "A proposed hands-on sprint to test a startup idea with real customer questions before you build. Educational only; date to be announced.",
           "Idea validation sprint for first-time founders", "Hands-on workshop", "Aspiring founders, students and professionals with a business idea", "Half day",
           ["Write the problem and the customer in plain words", "Draft interview questions that avoid leading the answer", "Plan five conversations and what you will listen for", "Decide what evidence would change your mind", "Set a one-week test"],
           "A one-page validation plan and a script for your first customer conversations.", "One idea, even if it is rough.",
           ["startup idea validation", "first time founder workshop", "customer discovery workshop", "startup studio india", "validate startup idea before building"],
           "This proposed half-day sprint helps first-time founders test a startup idea with real customer questions before building. You would define the problem, draft non-leading interview questions and set a one-week test. It is educational only, with no funding promised. Date, mentor and fee are to be announced.",
           [("Will you invest in my idea?", "No. This is education, with no investment, introductions or funding."), ("Do I need a company registered?", "No. The sprint happens before that stage.")],
           ["events/index.html", "ecosystem/startup-studio.html", "products/index.html", "academy/community-tracks.html"]),
    _event("pitch-deck-clinic", "Startup Studio", "Pitch Deck Clinic: Structure and Story (Proposed)",
           "A proposed clinic on structuring a clear pitch deck: problem, solution, market, model and ask. Educational only; date to be announced.",
           "Pitch deck clinic: structure and story", "Feedback clinic", "Founders with a draft pitch deck or an outline", "About 2 hours",
           ["The slide sequence investors usually expect, and why", "Stating the problem and solution in one sentence each", "Showing traction honestly, or saying you have none yet", "Common claims that weaken trust", "Live feedback on volunteer decks"],
           "A checklist for revising your deck and a short list of questions to be ready for.", "A draft deck or a bullet outline; confidential material stays private.",
           ["pitch deck workshop", "investor pitch deck structure", "startup pitch clinic", "founder pitch feedback", "pitch deck mistakes"],
           "This proposed two-hour clinic helps founders structure a clear pitch deck: problem, solution, market, model and ask. It covers showing traction honestly and common claims that weaken trust, with live feedback on volunteer decks. It is educational only and promises no investor access. Date, mentor and fee are to be announced.",
           [("Will you introduce me to investors?", "No. No investor access or funding is offered."), ("Is my deck kept private?", "Yes. Decks are used only for the session and not published.")],
           ["events/index.html", "ecosystem/startup-studio.html", "products/index.html", "academy/event-calendar.html"]),
]

HUB_EV = dict(
    path="events/index.html", title="Infinate360 Events: Eight Proposed Sessions Across Four Brands",
    desc="Eight proposed sessions across Explorer, CXO Hive, SkillSurf and Startup Studio, from resume clinics to pitch decks. Dates and fees to be announced.",
    h1="Proposed events across the Infinate360 products", kicker="Events", nav="Events", schema="WebPage", category="Events", date=DATE,
    keywords=["infinate360 events", "martech career workshop", "cxo roundtable india", "startup founder workshop india", "enterprise technology career session", "adobe martech events"],
    answer="Eight proposed sessions cover the four Infinate360 products: two for Explorer, two for CXO Hive, two for SkillSurf and two for Startup Studio. None has a confirmed date, speaker or fee, so none is scheduled yet. Each page lists the planned agenda. Register interest and we will contact you when one is confirmed. Adobe MarTech weekly slots are on the academy event calendar.",
    list_items=[("Resume keyword clinic", "events/resume-keyword-clinic.html"), ("Career roadmap and skill-gap session", "events/career-roadmap-skill-gap-session.html"),
                ("MarTech and AI centre of excellence roundtable", "events/martech-ai-coe-roundtable.html"), ("GCC-to-global transformation forum", "events/gcc-global-transformation-forum.html"),
                ("Choose your enterprise technology path", "events/choose-your-enterprise-technology-path.html"), ("Corporate team enablement briefing", "events/corporate-team-enablement-briefing.html"),
                ("Idea validation sprint", "events/idea-validation-sprint.html"), ("Pitch deck clinic", "events/pitch-deck-clinic.html")],
    sections=[
        ("Eight proposed sessions", _row_links(["Session", "Product", "Status"], [
            ("@Resume keyword clinic|resume-keyword-clinic.html", "Explorer", "Date to be announced"), ("@Career roadmap and skill-gap session|career-roadmap-skill-gap-session.html", "Explorer", "Date to be announced"),
            ("@MarTech and AI CoE roundtable|martech-ai-coe-roundtable.html", "CXO Hive", "Date to be announced"), ("@GCC-to-global forum|gcc-global-transformation-forum.html", "CXO Hive", "Date to be announced"),
            ("@Choose your technology path|choose-your-enterprise-technology-path.html", "SkillSurf", "Date to be announced"), ("@Corporate enablement briefing|corporate-team-enablement-briefing.html", "SkillSurf", "Date to be announced"),
            ("@Idea validation sprint|idea-validation-sprint.html", "Startup Studio", "Date to be announced"), ("@Pitch deck clinic|pitch-deck-clinic.html", "Startup Studio", "Date to be announced")])),
        ("When a session is confirmed", '<ul class="checklist"><li>Date, time and time zone</li><li>Named speaker and a short biography</li><li>Fee, or free, stated up front</li><li>Registration with marketing consent kept separate</li></ul><p>Weekly Adobe MarTech slots are on the <a href="../academy/event-calendar.html">academy event calendar</a>.</p>'
         + pills(REG, WA, ("Products", "../products/index.html"))),
    ],
    faqs=[("Why are there no dates?", "Dates are set only after speakers and venues or platforms are confirmed. We would rather publish nothing than a date we cannot keep."),
          ("Can I request a private session for my team?", "Yes. Use corporate training and describe the topic and team size.")],
    related=["academy/event-calendar.html", "products/index.html", "ecosystem/index.html", "academy/community-tracks.html"], sources=[], sitemap4=True)

# ---------------------------------------------------------------- Products hub
HUB_PROD = dict(
    path="products/index.html", title="Infinate360 Products: SkillSurf, Explorer, Studio, CXO Hive",
    desc="The four Infinate360 products side by side: SkillSurf training, Explorer career tools, Startup Studio and CXO Hive, with the real status of each.",
    h1="Infinate360 products", kicker="Products", nav="Products", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["infinate360 products", "skillsurf", "infinate360explorer", "startup studio india", "cxo hive", "martech training career and executive programmes"],
    answer="Infinate360 has four products. SkillSurf is multi-vendor enterprise technology training, Infinate360Explorer is career discovery and mentoring, Startup Studio is founder education, and CXO Hive is the executive programme. Each has its own pages here and a status: what is live, what is planned and what awaits confirmation. No fee, date, job count or outcome is stated unless confirmed.",
    list_items=[("SkillSurf", "ecosystem/skillsurf.html"), ("Infinate360Explorer", "ecosystem/infinate360-explorer.html"), ("Startup Studio", "ecosystem/startup-studio.html"), ("CXO Hive", "ecosystem/cxo-hive.html"),
                ("Explorer: jobs by technology", "products/explorer-jobs-by-technology.html"), ("Explorer: jobs by role", "products/explorer-jobs-by-role.html"),
                ("Explorer: resume scanner", "products/explorer-resume-scanner.html"), ("Explorer: for employers", "products/explorer-for-employers.html"),
                ("Explorer: course-to-role map", "products/explorer-course-job-map.html"), ("CXO Hive programme", "products/cxo-hive-programme.html"), ("Events", "events/index.html")],
    sections=[
        ("The four products", _row_links(["Product", "For", "What is live", "Pages"], [
            ("SkillSurf", "IT professionals and corporate teams", "Brand page with 30 planned domains; no catalogue", "@SkillSurf|../ecosystem/skillsurf.html"),
            ("Infinate360Explorer", "Jobseekers, career changers and employers", "Plans and free roadmaps; no job board or scanner yet", "@Explorer|../ecosystem/infinate360-explorer.html"),
            ("Startup Studio", "Founders and students", "Fifteen proposed programmes; none open", "@Startup Studio|../ecosystem/startup-studio.html"),
            ("CXO Hive", "Executives and architects", "Programme page; fees on request", "@CXO Hive|cxo-hive-programme.html")])),
        ("Explorer plan pages", '<ul class="checklist"><li><a href="explorer-jobs-by-technology.html">Jobs by technology</a>: twelve families</li><li><a href="explorer-jobs-by-role.html">Jobs by role</a>: thirty roles</li><li><a href="explorer-resume-scanner.html">Resume scanner</a>: method and limits</li><li><a href="explorer-for-employers.html">For employers</a>: planned features and protections</li><li><a href="explorer-course-job-map.html">Course-to-role map</a></li></ul>'),
        ("Events and corporate use", '<p>See <a href="../events/index.html">eight proposed events</a>, or ask about <a href="../training/corporate-training.html">corporate training</a>. Brand relationships are on the <a href="../ecosystem/index.html">ecosystem page</a>. Legal entities and official domains are being confirmed.</p>'
         + pills(REG, WA, ("Contact us", "../contact-us.html"))),
    ],
    faqs=[("Which product should I start with?", "Start with Infiante360 Tech Academy for Adobe MarTech and AI, or ask us about the product closest to your goal."),
          ("Are these separate companies?", "This page makes no claim about legal structure. They are separate products with different audiences.")],
    related=["ecosystem/index.html", "events/index.html", "academy/index.html", "training/corporate-training.html"], sources=[], sitemap4=True)

PRODUCT_PAGES = [HUB_PROD, EX_TECH, EX_ROLE, EX_SCAN, EX_EMP, EX_MAP, CXO_PROG]
EVENT_PAGES = [HUB_EV] + EVENTS
PRODUCT_ALL = PRODUCT_PAGES + EVENT_PAGES
