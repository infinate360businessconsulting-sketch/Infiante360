"""Group-brand pages and country pages (sitemap4.xml), built from owner-supplied strategy docs (2026-11-25).

Rules: brands are described as owner-stated portfolio names only. No legal-entity, domain, office, client, course-count, fee or date claims.
Country pages carry real, distinct privacy-law context for customer-data work; no local office is claimed. City pages are deliberately not
generated (thin duplicates); Bengaluru has its own page because the founder is based there."""
import html
from content_cases import pills, REGISTER, WHATSAPP_MSG, LI_GROUP

e = html.escape
DATE = "2026-11-25"
PHONE = "+91 82968 93895"
NOTE_LEGAL = "Guidance only, not legal advice. Laws change; confirm current requirements with your counsel and the regulator."
ADOBE_DOCS = [("Adobe Experience Platform documentation", "https://experienceleague.adobe.com/en/docs/experience-platform"),
              ("Adobe Experience Platform Web SDK", "https://experienceleague.adobe.com/en/docs/experience-platform/web-sdk/home")]


def _row_links(head, rows):
    """rows: tuples of plain strings; a string beginning with '@' is (text|href)."""
    out = []
    for r in rows:
        cells = []
        for c in r:
            if c.startswith("@"):
                t, h = c[1:].split("|")
                cells.append(f'<td><a href="{h}">{e(t)}</a></td>')
            else:
                cells.append(f"<td>{e(c)}</td>")
        out.append("<tr>" + "".join(cells) + "</tr>")
    return '<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in head) + "</tr></thead><tbody>" + "".join(out) + "</tbody></table></div>"


# slug, name, short law label, region, utc, law, regulator, source, comms rule, design implication
C = [
 ("india", "India", "DPDP Act", "South Asia", "UTC+5:30, no daylight saving", "the Digital Personal Data Protection Act, 2023", "the Data Protection Board of India", ("MeitY", "https://www.meity.gov.in/"),
  "Marketing calls and SMS are also shaped by TRAI commercial-communication rules, so check current registration and preference requirements.",
  "Capture consent per purpose, make withdrawal as easy as giving it, and check the current rules on consent managers and children's data."),
 ("united-states", "United States", "state privacy laws", "North America", "UTC-5 to UTC-8 across time zones, with daylight saving", "a patchwork of state laws such as the California Consumer Privacy Act as amended by CPRA, rather than one federal law", "state attorneys general, the California Privacy Protection Agency and the FTC", ("FTC", "https://www.ftc.gov/"),
  "The TCPA covers marketing calls and texts, and CAN-SPAM covers commercial email.",
  "Honour opt-out and do-not-sell-or-share choices in audience activation, and keep state-level consent flags on the profile."),
 ("canada", "Canada", "PIPEDA and CASL", "North America", "UTC-3:30 to UTC-8 across regions, with daylight saving in most", "PIPEDA federally, plus provincial laws such as Quebec's Law 25", "the Office of the Privacy Commissioner of Canada", ("Office of the Privacy Commissioner of Canada", "https://www.priv.gc.ca/"),
  "CASL requires consent for commercial electronic messages.",
  "Record express and implied consent separately, and plan for Quebec's stricter notice and impact-assessment duties."),
 ("united-kingdom", "United Kingdom", "UK GDPR and PECR", "Europe", "UTC+0, and UTC+1 in summer", "the UK GDPR, the Data Protection Act 2018 and PECR", "the Information Commissioner's Office", ("ICO", "https://ico.org.uk/"),
  "PECR sets the rules for cookies and electronic marketing.",
  "Hold non-essential tags until consent is given, and keep consent evidence that can be passed to every downstream destination."),
 ("ireland", "Ireland", "GDPR and ePrivacy", "Europe", "UTC+0, and UTC+1 in summer", "the GDPR and the ePrivacy Regulations 2011", "the Data Protection Commission", ("Data Protection Commission", "https://www.dataprotection.ie/"),
  "Cookie and direct-marketing rules sit in the ePrivacy Regulations.",
  "Ireland is the EU lead-authority location for many multinational companies, so document cross-border flows to audience destinations carefully."),
 ("germany", "Germany", "GDPR, BDSG and TDDDG", "Europe", "UTC+1, and UTC+2 in summer", "the GDPR, the Federal Data Protection Act (BDSG) and the TDDDG", "the Federal Commissioner (BfDI) and the state data protection authorities", ("BfDI", "https://www.bfdi.bund.de/"),
  "The TDDDG governs storing or reading information on a user's device, which is how cookies and SDK tags are treated.",
  "Treat loading of Web SDK and tag containers as consent-dependent, and map which state authority applies to the controller."),
 ("france", "France", "GDPR and CNIL guidance", "Europe", "UTC+1, and UTC+2 in summer", "the GDPR and the French Data Protection Act", "the CNIL", ("CNIL", "https://www.cnil.fr/en"),
  "CNIL guidance expects refusing cookies to be as easy as accepting them.",
  "Show a refuse option at the same level as accept, and make sure the refusal reaches the datastream and every destination."),
 ("netherlands", "Netherlands", "GDPR and UAVG", "Europe", "UTC+1, and UTC+2 in summer", "the GDPR and the Dutch implementation act (UAVG)", "the Autoriteit Persoonsgegevens", ("Autoriteit Persoonsgegevens", "https://www.autoriteitpersoonsgegevens.nl/en"),
  "Tracking cookies fall under the Telecommunications Act and need consent.",
  "Document the legal basis for each audience and destination, not only for the collection point."),
 ("switzerland", "Switzerland", "revised FADP", "Europe", "UTC+1, and UTC+2 in summer", "the revised Federal Act on Data Protection (FADP), in force since September 2023", "the Federal Data Protection and Information Commissioner (FDPIC)", ("FDPIC", "https://www.edoeb.admin.ch/en"),
  "The Federal Act against Unfair Competition covers unsolicited mass advertising.",
  "Keep a record of processing activities and prepare transfer documentation before profiles are sent outside Switzerland."),
 ("sweden", "Sweden", "GDPR and IMY", "Europe", "UTC+1, and UTC+2 in summer", "the GDPR and the Swedish Data Protection Act", "the Swedish Authority for Privacy Protection (IMY)", ("IMY", "https://www.imy.se/en/"),
  "Cookie and tracking rules sit in the Electronic Communications Act.",
  "Align analytics and Customer Journey Analytics measurement with the consent signals actually collected."),
 ("united-arab-emirates", "United Arab Emirates", "UAE PDPL", "Middle East", "UTC+4, no daylight saving", "Federal Decree-Law No. 45 of 2021 on personal data protection, with separate regimes in DIFC and ADGM", "the UAE Data Office", ("UAE government portal", "https://u.ae/en"),
  "The telecom regulator (TDRA) also sets rules for marketing calls and messages.",
  "Check whether DIFC or ADGM rules apply to the entity before choosing consent and retention settings."),
 ("saudi-arabia", "Saudi Arabia", "KSA PDPL", "Middle East", "UTC+3, no daylight saving", "the Personal Data Protection Law (PDPL)", "SDAIA, the Saudi Data and AI Authority", ("SDAIA", "https://sdaia.gov.sa/en/"),
  "The law has rules on using personal data for marketing and on consent.",
  "Check the conditions for transferring data outside the Kingdom before activating profiles to overseas destinations."),
 ("qatar", "Qatar", "Qatar PDPPL", "Middle East", "UTC+3, no daylight saving", "Law No. 13 of 2016 on Personal Data Privacy Protection, with a separate regime in the Qatar Financial Centre", "Qatar's national data privacy authority", ("National Cyber Security Agency", "https://www.ncsa.gov.qa/"),
  "Check the law's rules on electronic marketing and consent for each channel.",
  "Record the purpose of each audience and the controls on cross-border transfers."),
 ("singapore", "Singapore", "PDPA", "Asia-Pacific", "UTC+8, no daylight saving", "the Personal Data Protection Act 2012 (PDPA)", "the Personal Data Protection Commission", ("PDPC", "https://www.pdpc.gov.sg/"),
  "Do Not Call Registry rules apply to marketing calls, texts and faxes to Singapore numbers.",
  "Check the registry before any phone or SMS step in a journey."),
 ("australia", "Australia", "Privacy and Spam Acts", "Asia-Pacific", "UTC+8 to UTC+11 across states, with daylight saving in some", "the Privacy Act 1988 and the Australian Privacy Principles", "the Office of the Australian Information Commissioner", ("OAIC", "https://www.oaic.gov.au/"),
  "The Spam Act 2003 requires consent, sender identification and an unsubscribe option for commercial electronic messages.",
  "Build an unsubscribe that is honoured across every channel in the journey, not only the one that sent the message."),
 ("new-zealand", "New Zealand", "Privacy Act 2020", "Asia-Pacific", "UTC+12, and UTC+13 in summer", "the Privacy Act 2020", "the Office of the Privacy Commissioner", ("Office of the Privacy Commissioner", "https://www.privacy.org.nz/"),
  "The Unsolicited Electronic Messages Act 2007 requires consent and an unsubscribe for commercial messages.",
  "Apply the information privacy principles to collection and retention rules for profile data."),
 ("japan", "Japan", "APPI", "Asia-Pacific", "UTC+9, no daylight saving", "the Act on the Protection of Personal Information (APPI)", "the Personal Information Protection Commission", ("PPC", "https://www.ppc.go.jp/en/"),
  "Marketing email is also covered by the Act on Regulation of Transmission of Specified Electronic Mail.",
  "Check how identifiers that become personal information when combined are treated, and the rules on third-party transfers."),
]
COUNTRY_PATH = {c[0]: f"locations/{c[0]}.html" for c in C}


def _country(c):
    slug, name, short, region, utc, law, reg, src, comms, design = c
    kw = [f"adobe experience platform training {name.lower()}", f"martech consulting {name.lower()}", f"customer data platform consultant {name.lower()}",
          f"adobe journey optimizer course {name.lower()}", f"agentic ai mcp training {name.lower()}", f"{short.lower()} customer data"]
    return dict(
        path=COUNTRY_PATH[slug], title=f"Adobe MarTech Training and Consulting in {name}",
        desc=f"Online Adobe Experience Platform training and MarTech consulting for teams in {name}, with notes on {short} and customer data consent design.",
        h1=f"Adobe MarTech training and consulting in {name}", kicker=f"Locations · {region}", nav=name, schema="WebPage", category="Locations", date=DATE, keywords=kw,
        answer=f"Infiante360 offers Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Agentic AI training and MarTech consulting online to professionals and teams in {name}. No local office is claimed. For customer data work in {name}, start from {law}, overseen by {reg}. This page is guidance, not legal advice.",
        sections=[
            (f"Customer data rules to design for in {name}", _row_links(["Topic", "What to know"], [("Main framework", law[0].upper() + law[1:]), ("Regulator", reg[0].upper() + reg[1:]), ("Marketing messages", comms), ("Design implication for AEP and Real-Time CDP", design)])
             + f'<p class="note">{e(NOTE_LEGAL)}</p>'),
            (f"What we offer online to {name}", '<ul class="checklist"><li><a href="../training/index.html">Adobe MarTech and Agentic AI training</a> for individuals</li><li><a href="../training/corporate-training.html">Corporate training</a> for teams, scoped to your stack</li><li><a href="../services/index.html">Consulting</a> on AEP, Real-Time CDP, AJO, CJA and consent-aware architecture</li><li><a href="../academy/event-calendar.html">Proposed live sessions</a>; none is scheduled yet</li></ul>'),
            ("Working hours and delivery", f"<p>{e(name)} runs on {e(utc)}. Live sessions are delivered online and are planned around your local business hours; India Standard Time is UTC+5:30. We do not claim a local office in {e(name)}.</p>"
             + pills(("Ask about " + name + " on WhatsApp " + PHONE, WHATSAPP_MSG), ("Register interest", REGISTER), ("All locations", "index.html"))),
        ],
        faqs=[(f"Which privacy framework should a customer data platform in {name} start from?", f"Start from {law}, overseen by {reg}, then add the channel rules for marketing messages. Confirm the details with your counsel."),
              (f"Do you have an office in {name}?", f"No local office is claimed. Training and consulting for {name} are delivered online.")],
        related=["locations/index.html", "training/corporate-training.html", "services/index.html", "academy/community-tracks.html"], sources=[src] + ADOBE_DOCS[:1], sitemap4=True)


COUNTRY_PAGES = [_country(c) for c in C]

BENGALURU = dict(
    path="locations/bengaluru.html", title="Adobe MarTech Training and Consulting in Bengaluru",
    desc="Adobe Experience Platform training and MarTech consulting from Bengaluru, India, for enterprise and global capability centre teams, delivered online.",
    h1="Adobe MarTech training and consulting in Bengaluru", kicker="Locations · India", nav="Bengaluru", schema="WebPage", category="Locations", date=DATE,
    keywords=["adobe experience platform training bengaluru", "martech consulting bengaluru", "adobe journey optimizer course bangalore", "customer data platform consultant bengaluru", "gcc technology training bengaluru"],
    answer="The founder of Infiante360 is based in Bengaluru. Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Agentic AI training and MarTech consulting are delivered online, including to enterprise teams and global capability centres. This page does not claim a public office or in-person classes. India's data protection rules are on the India page.",
    sections=[
        ("What is delivered from Bengaluru", '<ul class="checklist"><li>Live online training in IST, with evening and weekend options</li><li><a href="../training/corporate-training.html">Corporate training</a> for capability and delivery teams</li><li><a href="../services/index.html">Consulting</a> on AEP, Real-Time CDP, AJO, CJA and Agentic AI</li></ul>'),
        ("Teams in Bengaluru", "<p>Bengaluru hosts a large number of global capability centres and technology teams. Corporate sessions can be scoped to a team's stack, role mix and project stage. No client engagement is implied by this page.</p>"
         + pills(("Request a proposal", REGISTER), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("India privacy notes", "india.html"))),
    ],
    faqs=[("Are there in-person classes in Bengaluru?", "Not at present. Sessions are online, and any in-person event would be announced with its venue and date."),
          ("Can a company team book a private batch?", "Yes. Use the corporate training route and share the team's tools, roles and goals.")],
    related=["locations/india.html", "locations/index.html", "training/corporate-training.html", "academy/community-tracks.html"], sources=ADOBE_DOCS[:1], sitemap4=True)

_rows = [(c[1], c[3], f"@{c[2]}|{c[0]}.html") for c in C]
HUB_LOC = dict(
    path="locations/index.html", title="Locations: Adobe MarTech Training and Consulting Worldwide",
    desc="Online Adobe MarTech training and consulting for 17 countries and Bengaluru, with the privacy framework to design customer data around in each place.",
    h1="Adobe MarTech training and consulting worldwide", kicker="Locations", nav="Locations", schema="WebPage", category="Locations", date=DATE,
    keywords=["adobe martech training worldwide", "martech consultant global", "adobe experience platform consultant international", "customer data platform privacy by country", "online adobe training india usa uk uae singapore"],
    answer="Infiante360 delivers Adobe MarTech and Agentic AI training and consulting online. This hub lists 17 countries and Bengaluru, each with the privacy framework, marketing-message rule and design implication that matter for customer data work there. No local offices are claimed. City pages are added only when there is real local content.",
    list_items=[(c[1], COUNTRY_PATH[c[0]]) for c in C] + [("Bengaluru", "locations/bengaluru.html")],
    sections=[
        ("Countries", _row_links(["Country", "Region", "Privacy framework"], [(c[1], c[3], f"@{c[2]}|{c[0]}.html") for c in C]) + '<p>Also: <a href="bengaluru.html">Bengaluru</a>, where the founder is based.</p>'),
        ("How to read these pages", f'<ul class="checklist"><li>Each page is guidance for designing consent and activation in AEP and Real-Time CDP, not legal advice</li><li>Delivery is online and planned around local business hours</li><li>No local office or client in a country is implied</li><li>Missing your country? <a href="https://wa.me/918296893895">Message us on WhatsApp {PHONE}</a></li></ul>'),
    ],
    faqs=[("Why are there no city pages?", "City pages would repeat each other. We add one only when there is genuine local content, as with Bengaluru."),
          ("Is this legal advice?", NOTE_LEGAL)],
    related=["locations/india.html", "locations/united-kingdom.html", "locations/singapore.html", "ecosystem/index.html"], sources=ADOBE_DOCS[:1], sitemap4=True)

# ---- brand pages ----
DOMAINS = [("Adobe Experience Cloud", "AEP, AJO, CJA, Real-Time CDP, AEM, Analytics, Target"), ("Guidewire", "PolicyCenter, ClaimCenter, BillingCenter, Gosu"), ("SAP", "S/4HANA, FICO, MM, SD, ABAP, BASIS, BTP"),
           ("Microsoft", "Azure, Dynamics 365, Power Platform, Fabric"), ("IBM", "Mainframe, Maximo, WebSphere, Sterling"), ("Salesforce", "CRM, Marketing Cloud, Data Cloud, Agentforce, MuleSoft"),
           ("Oracle", "Fusion ERP, HCM, SCM, PL/SQL, OCI"), ("ServiceNow", "ITSM, ITOM, HRSD, CMDB, administration"), ("Workday", "HCM, Finance, Payroll, integrations"), ("Anaplan", "Model building, connected planning, FP&A"),
           ("SailPoint", "Identity security and integrations"), ("CyberArk", "Privileged access management and administration"), ("Cybersecurity", "SOC, SIEM, cloud security"),
           ("Artificial intelligence", "Agentic AI, MCP, LLMs, RAG, AI engineering"), ("Data engineering", "Snowflake, Databricks, Kafka, Spark, Airflow"), ("Cloud computing", "AWS, Azure, GCP, cloud architecture"),
           ("DevOps and platform engineering", "Kubernetes, Docker, Terraform, CI/CD"), ("Software development", "Python, Java, TypeScript, React, APIs"), ("Software testing", "Selenium, Playwright, API testing"),
           ("Business intelligence", "Power BI, Tableau, Looker, Excel"), ("Digital marketing", "SEO, GEO, AEO, GA4, campaign management"), ("MarTech platforms", "Braze, HubSpot, Marketo, Tealium, Segment"),
           ("Project management", "Scrum, Agile, SAFe, PMP preparation"), ("Enterprise architecture", "TOGAF preparation, solution architecture"), ("IT service management", "ITIL preparation, service delivery"),
           ("Governance and compliance", "ISO 27001, ISO 42001, privacy, AI governance"), ("Business and finance", "FP&A, financial modelling, business analysis"), ("Leadership and management", "Strategy, executive communication"),
           ("Entrepreneurship and startups", "Startup development, fundraising, go-to-market, SaaS"), ("Career development", "Resumes, interviews, professional branding")]
VENDOR_NOTE = "Vendor and product names belong to their owners. Naming a technology here does not imply vendor endorsement, accreditation or partnership."

SKILLSURF = dict(
    path="ecosystem/skillsurf.html", title="SkillSurf: Enterprise Technology Training Brand",
    desc="SkillSurf is a multi-vendor enterprise technology training brand in the Infinate360 portfolio. See its 30 planned domains; courses open only when confirmed.",
    h1="SkillSurf: ride the wave of enterprise technology", kicker="Ecosystem · SkillSurf", nav="SkillSurf", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["skillsurf", "skillsurf training", "enterprise technology training india", "sap guidewire salesforce training", "corporate it training", "multi vendor technology courses"],
    answer="SkillSurf is a broad enterprise technology training brand in the Infinate360 portfolio, covering 30 planned domains from SAP, Guidewire and Salesforce to cybersecurity, data engineering and AI. Infiante360 Tech Academy stays the specialist route for Adobe MarTech and Agentic AI. Courses, dates and fees are shown only once confirmed.",
    sections=[
        ("Where SkillSurf fits", _row_links(["Brand", "Focus", "Audience"], [("SkillSurf", "Multi-vendor enterprise technology training", "IT professionals, learners and corporate teams"),
                                                                             ("Infiante360 Tech Academy", "Architecture-led Adobe MarTech, customer data and Agentic AI", "MarTech specialists, engineers and architects")])),
        ("Thirty planned domains", _row_links(["Domain", "Example topics"], DOMAINS) + f'<p class="note">Planned coverage, not a published catalogue. {e(VENDOR_NOTE)}</p>'),
        ("Corporate practices", '<ul class="checklist"><li>ERP, insurance technology, cybersecurity and AI engineering enablement</li><li>Data engineering, cloud, IT operations and leadership tracks</li><li>Graduate onboarding bootcamps</li></ul><p>For team training today, see <a href="../training/corporate-training.html">corporate training</a>.</p>'),
        ("How a course goes live", '<ul class="checklist"><li>Trainer and curriculum confirmed, then reviewed</li><li>Delivery mode, dates and fees stated before enrolment opens</li><li>No ratings, learner counts or testimonials are carried across brands</li></ul>'
         + pills(("Register interest", REGISTER), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("Ecosystem", "index.html"))),
    ],
    faqs=[("Can I enrol in SkillSurf courses from this page?", "No. This page describes the brand and planned domains. Enrolment opens only on a confirmed course page."),
          ("Is SkillSurf an official partner of SAP, Oracle or other vendors?", "No partnership or accreditation is claimed here.")],
    related=["products/index.html", "events/choose-your-enterprise-technology-path.html", "training/corporate-training.html", "locations/index.html"], sources=[], sitemap4=True)

PROGRAMS = [("Startup Founder Launchpad", "7 days", "Idea validation and founder roadmap"), ("AI Startup Accelerator", "30 days", "AI product prototype"), ("SaaS Startup Bootcamp", "30 days", "MVP and SaaS business model"),
            ("Zero-to-One Founder Program", "8 weeks", "Startup execution plan"), ("Agentic AI Startup Lab", "6 weeks", "Agent-based product prototype"), ("No-Code Startup Studio", "4 weeks", "Working no-code application"),
            ("Startup Growth Marketing", "4 weeks", "Customer acquisition strategy"), ("B2B Sales and SDR Academy", "4 weeks", "Sales pipeline and outreach playbook"), ("Startup Finance and Unit Economics", "2 weeks", "Financial model and cash-flow plan"),
            ("Pitch Deck Mastery", "2 weeks", "Investor-ready presentation draft"), ("Product Management for Founders", "4 weeks", "Product roadmap"), ("Enterprise AI Entrepreneurship", "6 weeks", "Enterprise AI solution concept"),
            ("Women Entrepreneur Launchpad", "6 weeks", "Business development roadmap"), ("Student Startup Accelerator", "4 weeks", "Prototype and business pitch"), ("Founder-to-CXO Leadership", "8 weeks", "Leadership and scaling strategy")]
STARTUP = dict(
    path="ecosystem/startup-studio.html", title="Infinate360 Startup Studio: Founder Programmes (Proposed)",
    desc="Fifteen proposed founder and startup education programmes, from idea validation to pitch decks. Educational only: no funding or investor access is promised.",
    h1="Startup Studio: from your first idea to your first enterprise", kicker="Ecosystem · Startup Studio", nav="Startup Studio", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["startup studio india", "founder programme ai startup", "startup idea validation workshop", "saas startup bootcamp", "pitch deck workshop", "student startup accelerator", "agentic ai startup lab"],
    answer="Infinate360 Startup Studio is a proposed founder education division with 15 programmes, from a 7-day idea-validation launchpad to an 8-week founder-to-CXO leadership track. Durations are proposed and nothing is open for enrolment yet. These are educational programmes, not an accredited incubator, and no funding, investor access or business outcome is promised.",
    sections=[
        ("Fifteen proposed programmes", _row_links(["Programme", "Proposed duration", "Intended output"], PROGRAMS)),
        ("What founders would work on", '<ul class="checklist"><li>Idea validation, customer discovery and market research</li><li>MVP planning, AI product development and SaaS architecture</li><li>Go-to-market, pricing, sales pipeline and unit economics</li><li>Pitch deck drafting and fundraising education</li></ul>'),
        ("Clear limits", '<p class="note">Educational guidance only. It is not investment advice, and no funding, investor introductions or success are promised. Programmes open only after curriculum, mentors, dates and fees are confirmed.</p>'
         + pills(("Register interest", REGISTER), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("Ecosystem", "index.html"))),
    ],
    faqs=[("Is this an incubator or accelerator that invests in startups?", "No. These are proposed education programmes. No investment or funding is offered."),
          ("When do programmes start?", "No dates are set. Interest registrations are used to decide what to schedule first.")],
    related=["products/index.html", "events/idea-validation-sprint.html", "events/pitch-deck-clinic.html", "academy/community-tracks.html"], sources=[], sitemap4=True)

EXPLORER = dict(
    path="ecosystem/infinate360-explorer.html", title="Infinate360Explorer: Career Intelligence Brand",
    desc="Infinate360Explorer focuses on job discovery, resume intelligence, skills assessments and career mentoring. See what it covers and the limits it keeps.",
    h1="Infinate360Explorer: discover, assess, learn, transform", kicker="Ecosystem · Explorer", nav="Infinate360Explorer", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["infinate360explorer", "career intelligence platform", "resume keyword scanner", "technology job discovery", "career mentoring martech", "skills assessment adobe ai"],
    answer="Infinate360Explorer is the career-focused brand in the Infinate360 portfolio. Its focus areas are job discovery, resume intelligence, skills assessments and career mentoring for jobseekers and career changers. Each tool is described on its own page only when it is live. Jobs come from authorised sources, and no job, interview or placement is guaranteed.",
    sections=[
        ("Focus areas", _row_links(["Area", "What it covers"], [("Job discovery", "Relevant vacancies from authorised sources, with original application links"), ("Resume intelligence", "Keyword and skills-gap feedback on your own resume"),
                                                                ("Skills assessments", "Technical and role-based practice assessments"), ("Career mentoring", "Personalised roadmaps and interview preparation")])),
        ("Rules it keeps", '<ul class="checklist"><li>Resumes and career reports stay private and are never published</li><li>Vacancies are listed only where the source allows, with attribution</li><li>Training suggestions are optional and separate from employer requirements</li><li>No job, interview or placement is promised</li></ul>'),
        ("Start with free resources", '<p>The academy already offers a <a href="../academy/career-accelerator-roadmap.html">90-day learning roadmap</a> and <a href="../academy/portfolio-projects-and-interview-scenarios.html">portfolio projects and interview scenarios</a>.</p>'
         + pills(("Register interest", REGISTER), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("Ecosystem", "index.html"))),
    ],
    faqs=[("Is there a live job board?", "Not on this site yet. A jobs feed would be added only with verified, permitted sources."),
          ("Do you guarantee jobs?", "No. Outcomes depend on your background, practice and the market.")],
    related=["products/index.html", "products/explorer-jobs-by-technology.html", "products/explorer-resume-scanner.html", "academy/career-accelerator-roadmap.html"], sources=[], sitemap4=True)

CXO = dict(
    path="ecosystem/cxo-hive.html", title="CXO Hive: Executive MarTech and AI Leadership Brand",
    desc="CXO Hive is the executive brand for CIOs, CTOs, CDOs, CMOs and GCC leaders on MarTech, enterprise AI and transformation. See audiences and proposed forums.",
    h1="CXO Hive: lead the transformation, don't just manage it", kicker="Ecosystem · CXO Hive", nav="CXO Hive", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["cxo hive", "executive martech ai leadership", "cio cto cdo cmo programme", "gcc leadership transformation", "enterprise ai investment roundtable", "executive architecture leadership"],
    answer="CXO Hive is the executive brand in the Infinate360 portfolio for CIOs, CTOs, chief data officers, CMOs, enterprise architects and global capability centre leaders. It covers MarTech strategy, enterprise AI and transformation. The programme page has the current offer. Forums and roundtables listed here are proposed, with no dates, speakers or member counts.",
    sections=[
        ("Who it is for", _row_links(["Role", "Typical concerns"], [("CIO and CTO", "Platform strategy, integration and AI governance"), ("Chief Data Officer", "Customer 360, identity, data quality and consent"),
                                                                      ("CMO and MarTech leaders", "Personalisation, journeys and measurement"), ("Enterprise architects", "Target architecture and operating model"), ("GCC leaders", "Moving from delivery capability to innovation ownership")])),
        ("Current programme", '<p>The executive programme is described on <a href="../academy/programs/executive-architecture-leadership.html">its own page</a>.</p>'),
        ("Proposed forums", '<ul class="checklist"><li>Enterprise AI investment roundtable</li><li>MarTech centre of excellence forum</li><li>Chief data officer leadership exchange</li><li>AI governance executive roundtable</li></ul><p class="note">Proposed only: no dates or speakers are confirmed. Confidential company discussions would be kept private.</p>'
         + pills(("Register interest", REGISTER), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("Ecosystem", "index.html"))),
    ],
    faqs=[("Is CXO Hive a membership network today?", "Not yet. The programme page is the current offer; forums are proposals."),
          ("Can my leadership team get a private session?", "Yes, ask through corporate training or consulting and share your goals.")],
    related=["products/cxo-hive-programme.html", "products/index.html", "academy/programs/executive-architecture-leadership.html", "events/martech-ai-coe-roundtable.html"], sources=[], sitemap4=True)

HUB_ECO = dict(
    path="ecosystem/index.html", title="Infinate360 Ecosystem: Brands, Academy and Consulting",
    desc="How Infinate360 brands fit together: Tech Academy, consulting, research, CXO Hive, SkillSurf, Explorer and Startup Studio, with the status of each.",
    h1="The Infinate360 ecosystem", kicker="Ecosystem", nav="Ecosystem", schema="WebPage", category="Ecosystem", date=DATE,
    keywords=["infinate360", "infiante360 tech academy", "infinate360 ecosystem", "infinate360 consulting", "martech education and consulting brands", "adobe martech academy and research"],
    answer="Infinate360 groups education, consulting, research, executive and career brands. Infiante360 Tech Academy and the consulting services are live on this site, with a research hub and a CXO Hive programme page. SkillSurf, Infinate360Explorer and Startup Studio have brand pages, and anything not yet open is marked as proposed. Events and jobs have their own pages.",
    list_items=[("Infiante360 Tech Academy", "academy/index.html"), ("Consulting", "services/index.html"), ("Research and Intelligence", "research/index.html"), ("CXO Hive", "ecosystem/cxo-hive.html"),
                ("SkillSurf", "ecosystem/skillsurf.html"), ("Infinate360Explorer", "ecosystem/infinate360-explorer.html"), ("Startup Studio", "ecosystem/startup-studio.html"),
                ("Products", "products/index.html"), ("Events", "events/index.html")],
    sections=[
        ("Brands and status", _row_links(["Brand", "Focus", "Status", "Page"], [
            ("Infiante360 Tech Academy", "Architecture-led Adobe MarTech, customer data and Agentic AI education", "Live on this site", "@Academy|../academy/index.html"),
            ("Business consulting", "Enterprise MarTech, architecture, data and AI delivery", "Live on this site", "@Services|../services/index.html"),
            ("Research and Intelligence", "Technical research and architecture insight", "Live: research hub", "@Research|../research/index.html"),
            ("CXO Hive", "Executive MarTech and AI leadership", "Programme page live", "@CXO Hive|cxo-hive.html"),
            ("SkillSurf", "Multi-vendor enterprise technology training", "Brand page; courses listed when open", "@SkillSurf|skillsurf.html"),
            ("Infinate360Explorer", "Career intelligence, assessments and mentoring", "Brand page; tools listed when live", "@Explorer|infinate360-explorer.html"),
            ("Startup Studio", "Founder education", "Proposed", "@Startup Studio|startup-studio.html"),
            ("Events and community", "Webinars, workshops and topic communities", "Proposed calendar", "@Events|../events/index.html")])),
        ("Products", '<p>Side-by-side status of the four products is on the <a href="../products/index.html">products page</a>.</p>'),
        ("Where we deliver", '<p>Delivery is online. See <a href="../locations/index.html">locations</a> for 17 countries and Bengaluru, each with the privacy framework that matters for customer data work.</p>'),
        ("What this page does not claim", '<p class="note">It describes how the brands relate in focus and audience, and does not state a corporate structure or registered entity for any of them. Courses, events and programmes open only on pages that show confirmed dates, fees and delivery details.</p>'
         + pills(("Contact us", "../contact-us.html"), ("WhatsApp " + PHONE, WHATSAPP_MSG), ("Community", "../academy/community-tracks.html"))),
    ],
    faqs=[("Are all these brands one company?", "This page makes no claim about legal structure. It describes how the brands relate in focus and audience."),
          ("Which brand should I start with?", "Start with Infiante360 Tech Academy for Adobe MarTech and Agentic AI, or consulting for an enterprise engagement.")],
    related=["academy/index.html", "services/index.html", "research/index.html", "locations/index.html"], sources=[], sitemap4=True)

GROUP_PAGES = [HUB_ECO, SKILLSURF, EXPLORER, STARTUP, CXO, HUB_LOC] + COUNTRY_PAGES + [BENGALURU]
