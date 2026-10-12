"""Brochure hub (gated download), C2C hiring explainer and MarTech Centre of Excellence pages."""
import html as _h
from content_cases import pills, WHATSAPP_MSG, REGISTER
e = _h.escape
EL = "https://experienceleague.adobe.com/en/docs"
EMAIL = "infinate360businessconsulting@gmail.com"
BASE = "https://infiante360techacademy.com/"

AUD = [("learners", "Learners and career switchers", "Programmes, timings, full table of contents and interview preparation.", "11 pages"),
       ("corporate-training", "Corporate L&D and delivery leaders", "Team training, Live Customised programme, CoE and course contents.", "12 pages"),
       ("enterprise-coe", "Enterprise leaders and architects", "Centre of Excellence set-up, CXO Hive and the C2C talent model.", "8 pages"),
       ("c2c-partners", "C2C consultants and client hiring teams", "How C2C works, skills covered and interview approach.", "7 pages"),
       ("master", "Everything: the full 16-page brochure", "About Infinate360, all courses with TOC, interviews, C2C, CoE and contact.", "16 pages")]

def _cards():
    return '<div class="grid-2">' + "".join(f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p><p class="muted small">PDF · {pg}</p></div>' for k, t, d, pg in AUD) + "</div>"

def _prev():
    items = [("preview-cover.jpg", "Brochure cover slide"), ("preview-programmes.jpg", "Programmes, fees and timings slide"), ("preview-c2c.jpg", "How C2C engagement works slide"), ("preview-coe.jpg", "MarTech Centre of Excellence slide")]
    return '<div class="grid-2">' + "".join(f'<figure><img src="../assets/brochures/{f}" alt="{a}" loading="lazy" width="800" height="450" style="width:100%;height:auto;border:1px solid #E2E8F0;border-radius:10px"><figcaption class="muted small">{a}</figcaption></figure>' for f, a in items) + "</div>"

def _f(i, label, typ="text", auto="", req=True):
    r = ' required aria-required="true"' if req else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if req else ' <span class="muted small">(optional)</span>'
    pat = ' pattern="[+0-9 ()-]{7,20}" data-msg-pattern="Use digits, spaces and + only."' if typ == "tel" else ""
    return (f'<div class="field"><label for="b-{i}">{label}{star}</label><input id="b-{i}" name="{i}" type="{typ}" autocomplete="{auto}"{r}{pat} aria-describedby="b-{i}-error" data-msg-required="Please fill this in.">'
            f'<span class="error" id="b-{i}-error" aria-live="polite"></span></div>')

OPTS = "".join(f'<option value="{k}">{e(t)}</option>' for k, t, d, pg in AUD)
FORM = f'''<form class="form js-validate" action="https://formsubmit.co/{EMAIL}" method="POST" aria-describedby="b-note">
<input type="hidden" name="_subject" value="Brochure download request"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="{BASE}brochure-download.html"><input type="hidden" name="form_type" value="brochure"><input type="hidden" name="source_page" value="">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
{_f("name", "Your name", auto="name")}{_f("email", "Email", "email", "email")}{_f("phone", "Phone / WhatsApp", "tel", "tel")}
<div class="field"><label for="b-interest">Which brochure? <span class="req" aria-hidden="true">*</span></label><select id="b-interest" name="interest" required aria-required="true" aria-describedby="b-interest-error" data-msg-required="Please choose one.">{OPTS}</select><span class="error" id="b-interest-error" aria-live="polite"></span></div>
<div class="field full"><label for="b-message">Your requirement <span class="req" aria-hidden="true">*</span></label><textarea id="b-message" name="message" required aria-required="true" minlength="10" aria-describedby="b-message-error" data-msg-required="Tell us briefly what you need."></textarea><span class="error" id="b-message-error" aria-live="polite"></span></div>
<div class="field full"><div class="consent"><input id="b-consent" name="consent" type="checkbox" value="yes" required aria-required="true" aria-describedby="b-consent-error" data-msg-required="Please confirm to continue."><label for="b-consent" style="font-weight:500">I agree that Infinite360 Tech Academy may contact me about my requirement, as described in the <a href="privacy-policy.html">privacy policy</a>. I can unsubscribe at any time.</label></div><span class="error" id="b-consent-error" aria-live="polite"></span></div>
<div class="field full"><button class="btn btn-primary" type="submit">Get the brochure</button><p class="hint" id="b-note">After you submit, the download page opens with your PDF links.</p><p class="form-status" role="status" aria-live="polite"></p></div></form>'''

BROCHURE_PAGE = dict(
    path="brochures.html",
    title="Free Brochures: Courses, TOC, C2C & MarTech CoE | Infinate360",
    desc="Download free Infinate360 brochures with course timings, tables of contents, interview preparation, C2C hiring and MarTech Centre of Excellence set-up.",
    h1="Free brochures for learners, teams and enterprises",
    kicker="Brochures", nav="Brochures", schema="WebPage", category="Academy", date="2026-10-12",
    keywords=["adobe experience platform course brochure", "aep training brochure", "martech center of excellence", "c2c hiring martech"],
    answer="Infinate360 offers five free PDF brochures: for learners, corporate training teams, enterprise leaders, C2C partners, and one full 16-page edition. They cover what Infinate360 is, courses with fees, timings and tables of contents, interview preparation, how C2C engagement works and how a MarTech Centre of Excellence is set up. Share your name, email, phone and requirement to download.",
    sections=[
        ("Choose your brochure", _cards()),
        ("Request your copy", FORM),
        ("Layout preview", _prev()),
        ("Read online", pills(("How C2C hiring works", "c2c-hiring.html"), ("MarTech Centre of Excellence", "martech-center-of-excellence.html"), ("All programmes", "academy/index.html"), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Are the brochures free?", "Yes. We ask for your contact details so we can follow up on your requirement, with your consent."),
          ("Do the brochures promise jobs or certifications?", "No. Roles are target pathways, and no job, salary or certification outcome is guaranteed."),
          ("Are fees final?", "Fees match the website. Items marked 'See site' or 'On request' are confirmed at registration.")],
    related=["academy/index.html", "c2c-hiring.html", "martech-center-of-excellence.html", "academy/workshops.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
)

C2C_PAGE = dict(
    path="c2c-hiring.html",
    title="C2C Hiring for Adobe MarTech: How Corp-to-Corp Works",
    desc="How corp-to-corp (C2C) engagement works for Adobe MarTech projects: steps, roles of client and consultant, what to agree in writing and how to start.",
    h1="How C2C (corp-to-corp) hiring works for Adobe MarTech",
    kicker="Talent", nav="C2C hiring", schema="Article", category="Services", date="2026-10-12",
    keywords=["c2c hiring", "corp to corp adobe consultant", "adobe aep contractor", "martech contractor", "c2c vs w2"],
    answer="Corp-to-corp (C2C) means a consultant contracts through their own registered business entity, which signs an agreement with the client or vendor and invoices for the work, instead of being a salaried employee. Typical steps are requirement, shortlist, client interview, contract between the two entities, delivery and invoicing. Rates and payment terms are agreed in writing per engagement.",
    sections=[
        ("The six steps", '<ol class="steps"><li><strong>Requirement.</strong> The client shares the role, skills, location or time zone, and duration.</li><li><strong>Match.</strong> We shortlist profiles with relevant AEP, RTCDP, AJO, CJA or Web SDK skills.</li><li><strong>Interview.</strong> The client interviews the consultant and checks fit.</li><li><strong>Contract.</strong> A master services agreement and statement of work are signed between the two entities.</li><li><strong>Deliver.</strong> The consultant works on the project against agreed scope.</li><li><strong>Invoice.</strong> The consultant\'s entity invoices on the agreed schedule.</li></ol>'),
        ("What it means for each side", '<div class="grid-2"><div class="card"><h3>Clients</h3><ul class="checklist"><li>Access to specialist contractors for a defined period</li><li>No salaried-employment overhead; the engagement is a commercial contract</li><li>You interview before you commit</li></ul></div><div class="card"><h3>Consultants</h3><ul class="checklist"><li>You contract through your own entity</li><li>You are responsible for your own taxes, insurance and benefits</li><li>Work should match your verified skills</li></ul></div></div>'),
        ("What to agree in writing", '<ul class="checklist"><li>Scope, deliverables and duration</li><li>Rate, invoicing cycle and payment terms</li><li>Confidentiality, intellectual property and data protection</li><li>Notice period and termination</li><li>Work location, hours and time-zone overlap</li><li>Who is responsible for tax, insurance and compliance</li></ul><p>These terms are not fixed in this page. They are agreed per engagement. Tax, employment and work-authorisation rules differ by country, so take professional advice for your situation.</p>'),
        ("Skills we focus on", '<ul class="checklist"><li>Adobe Experience Platform: XDM, ingestion, identity, Profile</li><li>Real-Time CDP: audiences and activation</li><li>Adobe Journey Optimizer and Customer Journey Analytics</li><li>Web SDK and Adobe Tags</li><li>Data engineering and Agentic AI for MarTech</li></ul>'),
        ("Get started", pills(("Download the C2C brochure", "brochures.html"), ("Email us", f"mailto:{EMAIL}"), ("Chat on WhatsApp", WHATSAPP_MSG), ("Train for AEP roles", "academy/index.html"))),
    ],
    faqs=[("What is C2C?", "C2C stands for corp-to-corp: a business entity contracts with another business entity for services."),
          ("Is C2C the same as employment?", "No. A C2C consultant is an independent contractor through their own entity, not an employee."),
          ("Does Infinate360 guarantee placements?", "No. Matching depends on skills, client demand and interviews.")],
    related=["brochures.html", "martech-center-of-excellence.html", "academy/index.html", "academy/aep-bfsi-quiz.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
)

COE_PAGE = dict(
    path="martech-center-of-excellence.html",
    title="MarTech Centre of Excellence Set-Up: Assess, Design, Build",
    desc="How to set up a MarTech or AI Centre of Excellence: assess, design, build and operate, with roles, governance, reusable assets and enablement.",
    h1="How to set up a MarTech Centre of Excellence",
    kicker="Enterprise", nav="MarTech CoE", schema="Service", category="Services", date="2026-10-12",
    keywords=["martech center of excellence", "marketing technology coe setup", "ai center of excellence", "gcc to global capability", "cdp operating model"],
    answer="A MarTech Centre of Excellence (CoE) gives an organisation one team that owns platform standards, governance, reusable assets and enablement. Set it up in four phases: assess the current stack and skills, design the operating model and governance, build reusable assets and train people, then operate with intake, quality checks and measurement. Infinate360 supports this through the CXO Hive programme and consulting.",
    sections=[
        ("Four phases", '<ol class="steps"><li><strong>Assess.</strong> Current stack, skills, sponsors and the use-case backlog.</li><li><strong>Design.</strong> Operating model, roles, governance, consent and architecture standards.</li><li><strong>Build.</strong> Reusable templates and data models, environments and release process, enablement and training.</li><li><strong>Operate.</strong> Intake and prioritisation, quality and measurement, continuous improvement.</li></ol>'),
        ("What a CoE owns", '<ul class="checklist"><li>Platform and data standards, naming and environments</li><li>Consent, data usage and governance policies</li><li>A reusable library of schemas, audiences and journeys</li><li>Intake, prioritisation and release management</li><li>Skills plan and training for delivery teams</li><li>KPIs and reporting for the business</li></ul>'),
        ("Typical roles", '<ul class="checklist"><li>Executive sponsor and CoE lead</li><li>Platform architect and data architect</li><li>Implementation and QA specialists</li><li>Governance and privacy partner</li><li>Analytics and measurement owner</li></ul>'),
        ("How Infinate360 can help", '<p>The <a href="academy/programs/executive-architecture-leadership.html">CXO Hive: Executive and Architecture Program</a> covers setting up a MarTech or AI Centre of Excellence, CDP and AI strategy, governance, and GCC-to-global capability models. For team skills, see the <a href="academy/programs/live-customised-program.html">Live Customised Program</a>. Scope and pricing for consulting are agreed per engagement.</p>'),
        ("Next step", pills(("Download the enterprise brochure", "brochures.html"), ("Architecture review", "contact-us.html"), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("How long does a CoE take to set up?", "It depends on scope and size. A discovery phase usually comes first to size the work."),
          ("Do you claim past CoE clients here?", "No. This page describes an approach, not client results.")],
    related=["brochures.html", "c2c-hiring.html", "academy/programs/executive-architecture-leadership.html", "services/index.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
)
BRO_ALL = [BROCHURE_PAGE, C2C_PAGE, COE_PAGE]
