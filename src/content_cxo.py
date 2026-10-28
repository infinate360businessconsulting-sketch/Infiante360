"""CXO Hive: C-level executive program. Data-driven from content/cxo-hive.json (fee, cohorts, format).
Outcomes are deliverables and decisions the participant produces; no business result is guaranteed."""
import json, os, datetime, html as _h
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(_ROOT, "content", "cxo-hive.json"), encoding="utf-8"))
e = _h.escape
FEE = CFG["fee_label"]
MAIN = "academy/programs/executive-architecture-leadership.html"
APPLY = "lp/cxo-hive-apply.html"
NAME = CFG["name"]
EL = "https://experienceleague.adobe.com/en/docs"


def _fmt(d):
    return d.strftime("%A %-d %B %Y")


def next_cohort():
    today = datetime.date.today()
    for c in CFG["cohorts"]:
        if c.get("status") == "open" and datetime.date.fromisoformat(c["first_weekend"]) >= today:
            return c
    return None


def cohort_line():
    c = next_cohort()
    if not c:
        return "Next cohort dates to be announced. Apply to join the waitlist."
    return (f'{c["label"]}: kick-off {_fmt(datetime.date.fromisoformat(c["kickoff"]))}; '
            f'first weekend workshop {_fmt(datetime.date.fromisoformat(c["first_weekend"]))}.')


def cohort_block():
    data = e(json.dumps(CFG["cohorts"]))
    return ('<p class="cxo-cohort"><strong>Next cohort: <span id="cxo-next" data-cohorts="' + data + '">' + e(cohort_line()) + '</span></strong> '
            '<span id="cxo-count" class="muted small"></span></p>'
            '<script>(function(){try{var el=document.getElementById("cxo-next");var cs=JSON.parse(el.getAttribute("data-cohorts"));'
            'var t=new Date();t.setHours(0,0,0,0);var f=function(s){return new Date(s+"T00:00:00").toLocaleDateString("en-GB",{weekday:"long",day:"numeric",month:"long",year:"numeric"})};'
            'var n=null;for(var i=0;i<cs.length;i++){var d=new Date(cs[i].first_weekend+"T00:00:00");if(cs[i].status==="open"&&d>=t){n=cs[i];break}}'
            'if(!n){el.textContent="Next cohort dates to be announced. Apply to join the waitlist.";return}'
            'el.textContent=n.label+": kick-off "+f(n.kickoff)+"; first weekend workshop "+f(n.first_weekend)+".";'
            'var k=Math.round((new Date(n.kickoff+"T00:00:00")-t)/86400000);'
            'var c=document.getElementById("cxo-count");if(c){c.textContent=k>0?"("+k+" days to kick-off)":(k===0?"(kick-off today)":"(cohort has started)")}}catch(x){}})();</script>')


# ---------------- curriculum ----------------
WEEKS = [
    ("1", "Executive thesis and baseline", "Role and ambition discovery; capability baseline across data, platforms, AI and operating model", "Outcome tree and evidence inventory; stakeholder map", "Executive thesis and baseline scorecard"),
    ("2", "Customer data and value", "Customer lifecycle, KPI trees, current-state assessment of data, identity and consent", "Problem brief and decision rights; prioritised use cases", "Problem brief and use-case shortlist"),
    ("3", "MarTech reference architecture", "Platform ecosystem; AEP and Real-Time CDP, identity, profile, governance", "Architecture review questions; build, buy or configure", "Target-state architecture v1"),
    ("4", "Data and integration for leaders", "Event quality, APIs, batch and streaming, data quality and observability", "Hands-on validation of a sample pipeline and schema", "Data-readiness assessment"),
    ("5", "Journeys and measurement", "Journey orchestration, suppression, testing; Customer Journey Analytics and experiment design", "Journey blueprint and measurement model", "Journey test plan and KPI tree"),
    ("6", "AI strategy", "Generative AI, RAG and agents in the enterprise; use-case scoring by value, effort and risk", "AI opportunity workshop on your own processes", "Prioritised AI use-case backlog"),
    ("7", "Agentic AI and MCP", "Tools, state, approvals and audit trails; MCP and least privilege", "Design a supervised agent with a release checklist", "Agent release checklist and risk register"),
    ("8", "Operating model and governance", "CIO-CMO alignment, decision rights, forums, escalation and release gates", "Draft a RACI and an operating cadence for your organisation", "Governance pack"),
    ("9", "Business case and value", "Investment case, benefits baseline, cost and FinOps, risk and adoption", "Build a one-page investment case with assumptions labelled", "Executive investment case"),
    ("10", "Capstone and 90-day plan", "Capstone presentation, peer challenge and gap closure", "Executive review and next-quarter roadmap", "Capstone and 90-day plan"),
]
SESSION = [("0:00-0:20", "Review commitments, blockers and decisions since the last session", "Updated status"),
           ("0:20-1:20", "Teach one core idea with a real enterprise pattern", "Shared mental model"),
           ("1:20-2:50", "Build, analyse or rehearse on your own context", "Visible artifact"),
           ("2:50-3:30", "Challenge assumptions and test edge cases", "Decision log"),
           ("3:30-4:00", "Summarise, assign owners and set acceptance criteria", "Next actions")]


def table(head, rows):
    return ('<div class="table-wrap"><table><thead><tr>' + "".join(f"<th>{e(h)}</th>" for h in head) + '</tr></thead><tbody>'
            + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + '</tbody></table></div>')


def disclaimer():
    return ('<p class="small muted">Outcomes are the artifacts and decisions you produce. No business result, promotion, job, salary or certification is guaranteed. '
            + e(CFG["fee_note"]) + '</p>')


READINESS = r'''
<div class="form-card" id="cxo-check"><h3>Executive fit check</h3>
<p class="muted small">Eight questions, answered in your browser. Nothing is stored or sent.</p>
<form id="cxo-form" onsubmit="return false">
<div class="field"><label for="q1">Your role</label><select id="q1"><option value="">Select</option><option value="c">CEO, founder or managing director</option><option value="c">CIO or CTO</option><option value="c">CMO, CDO or Chief Product Officer</option><option value="c">COO or CFO</option><option value="c">Chief AI, Data or Digital Officer</option><option value="n">VP or director</option><option value="n">Other</option></select></div>
<div class="field"><label for="q2">Your involvement in MarTech, data or AI transformation</label><select id="q2"><option value="">Select</option><option value="3">I own it</option><option value="2">I sponsor it</option><option value="1">I influence decisions</option><option value="0">Not involved</option></select></div>
<div class="field"><label for="q3">Organisation size</label><select id="q3"><option value="">Select</option><option value="1">Under 250 people</option><option value="2">250 to 999</option><option value="3">1,000 or more</option></select></div>
<div class="field"><label for="q4">Adobe Experience Cloud in your stack</label><select id="q4"><option value="">Select</option><option value="3">Core platform</option><option value="2">Partly in use</option><option value="1">Evaluating</option><option value="0">No</option></select></div>
<div class="field"><label for="q5">Main goal for the program</label><select id="q5"><option value="">Select</option><option value="case">Build an investment case</option><option value="ops">Design an operating model</option><option value="ai">Govern AI and agents</option><option value="arch">Decide on architecture</option><option value="team">Build team capability</option></select></div>
<div class="field"><label for="q6">Can you join live on Saturdays and Sundays for 10 weeks?</label><select id="q6"><option value="">Select</option><option value="2">Yes</option><option value="1">Most weekends</option><option value="0">No</option></select></div>
<div class="field"><label for="q7">AI initiatives today</label><select id="q7"><option value="">Select</option><option value="0">None yet</option><option value="1">Pilots</option><option value="2">In production</option></select></div>
<div class="field"><label for="q8">When do you want to start</label><select id="q8"><option value="">Select</option><option value="2">Next cohort</option><option value="1">Within 3 months</option><option value="0">Exploring</option></select></div>
<button class="btn btn-primary" type="button" id="cxo-go" data-apply="@@APPLY@@">Check my fit</button>
</form>
<div id="cxo-result" class="notice" role="status" aria-live="polite" style="margin-top:14px" hidden></div></div>
<script>(function(){var go=document.getElementById("cxo-go");if(!go)return;go.addEventListener("click",function(){
var v=function(i){return document.getElementById(i).value},out=document.getElementById("cxo-result"),ids=["q1","q2","q3","q4","q5","q6","q7","q8"];
for(var i=0;i<ids.length;i++){if(!v(ids[i])){out.hidden=false;out.textContent="Please answer all eight questions.";return}}
var tx={case:"the executive investment case (week 9)",ops:"the operating model and governance weeks (weeks 8)",ai:"AI strategy and agentic AI governance (weeks 6 and 7)",arch:"reference architecture and data readiness (weeks 3 and 4)",team:"capability and adoption planning (weeks 1, 8 and 10)"};
if(v("q1")!=="c"){out.hidden=false;out.textContent="CXO Hive is for C-level executives only. For your role, the Career Accelerator or the Live Customised MarTech Program is a better fit (see the links below the form).";return}
var s=+v("q2")*2+ +v("q3")+ +v("q4")+ +v("q6")*2+ +v("q7")+ +v("q8");
var fit=s>=11?"strong":(s>=7?"good":"early");
var msg="Indicative fit: "+fit+". Your focus areas would be "+tx[v("q5")]+".";
if(v("q6")==="0"){msg+=" The weekend live format may not suit you now; ask about a private or in-house cohort."}
else if(v("q8")==="0"){msg+=" You can apply later; join the waitlist for the next cohort."}
var a=document.createElement("a");a.textContent="Apply for CXO Hive";a.setAttribute("href",go.getAttribute("data-apply"));out.innerHTML=msg+" ";out.appendChild(a);out.appendChild(document.createTextNode(". This is an indicative check, not an admission decision."));return;
out.hidden=false;out.innerHTML=msg})})();</script>
'''


def readiness(depth_prefix):
    return READINESS.replace("@@APPLY@@", depth_prefix + APPLY) + (
        '<p class="small muted">Not C-level? See the <a href="' + depth_prefix + 'training/">Career Accelerator</a> or the <a href="' + depth_prefix + 'academy/programs/live-customised-program.html">Live Customised MarTech Program</a>.</p>')


PAGES_CXO = []

PAGES_CXO.append(dict(
    path=MAIN, nav="CXO Hive",
    title="CXO Hive: Executive MarTech & AI Leadership Program",
    desc=f"CXO Hive is a 10-week live program for C-level executives on MarTech, data and AI leadership: architecture, governance, investment case. {FEE}.",
    h1=NAME, kicker="Academy · C-level program",
    keywords=["cxo program martech", "executive ai leadership program", "cio cmo alignment training", "martech leadership program india", "agentic ai strategy for executives"],
    answer=(f"CXO Hive is a {CFG['weeks']}-week, live, instructor-led program for C-level executives who sponsor MarTech, customer data and AI transformation. "
            f"It runs every Saturday and Sunday with two short midweek checkpoints and ends with an executive investment case, a target architecture, an operating model and a 90-day plan. The fee is {FEE}."),
    schema="Course", course_name=NAME, price_inr=CFG["fee_inr"], course_workload="P10W",
    teaches=["MarTech architecture", "Customer data strategy", "AI and agentic AI governance", "Executive operating model", "Investment case"],
    bands=True, program=True, hero_cta=("Apply for CXO Hive", APPLY),
    interest_options=["Apply for the next cohort", "Request the program brief", "A private in-house executive cohort"],
    sections=[
        ("Program at a glance", f'''<div class="price-card"><div><div class="price">{FEE}<small>one-time program fee</small></div>
<div class="meta" style="margin-top:14px"><span>C-level only</span><span>{CFG["weeks"]} weeks</span><span>100% live</span></div>
{cohort_block()}
<p class="cta-row" style="margin-top:20px"><a class="btn btn-primary" href="../../{APPLY}">Apply for CXO Hive</a> <a class="btn btn-ghost" href="#enquire">Request the brief</a> <a class="btn btn-ghost" href="{CFG["whatsapp"]}" rel="noopener" target="_blank">Ask on WhatsApp</a></p></div>
<ul class="checklist"><li>Live sessions every Saturday and Sunday, {CFG["hours_per_weekend_day"]} hours each day</li><li>Two midweek checkpoints of 30 to 45 minutes</li><li>Work on your own organisation, not generic case studies</li><li>Six executive artifacts, ready to take to your board or committee</li><li>Architecture, governance and AI risk templates</li><li>Peer cohort of C-level leaders</li></ul></div>
{disclaimer()}''', "plain", "Fees &amp; cohort"),
        ("Why C-level leaders join", '''<div class="grid-3"><div class="card"><h3>Shared CIO-CMO agenda</h3><p>Technology and marketing leaders agree priorities, decision rights and success measures before more tools are bought.</p></div>
<div class="card"><h3>AI with accountability</h3><p>Move from scattered pilots to governed use cases with owners, evaluation and human approval points.</p></div>
<div class="card"><h3>Data you can trust</h3><p>Understand identity, consent and data quality well enough to challenge a roadmap and fund the right fixes.</p></div></div>''', "alt", "Why"),
        ("What you leave with", '''<div class="grid-2"><div class="card"><h3>1. Executive investment case</h3><p>One page and five slides: options, cost, risk, owner, baseline and target, with assumptions labelled.</p></div>
<div class="card"><h3>2. Target-state architecture</h3><p>A reference architecture for your organisation covering data, identity, consent, platforms and AI.</p></div>
<div class="card"><h3>3. Operating model and RACI</h3><p>Decision rights, forums, escalation paths and release gates for MarTech and AI work.</p></div>
<div class="card"><h3>4. AI use-case backlog</h3><p>Use cases scored by value, effort and risk, with a release checklist for agentic workflows.</p></div>
<div class="card"><h3>5. 90-day roadmap</h3><p>Priorities, owners, KPIs and baselines. Targets are labelled as targets, never as achieved results.</p></div>
<div class="card"><h3>6. Board-ready briefing</h3><p>A short narrative you can present to your board or executive committee.</p></div></div>
<p><a href="cxo-hive-outcomes.html">See outcomes and the capstone &rarr;</a></p>''', "plain", "Outcomes"),
        ("The 10-week journey", table(["Weeks", "Focus"], [("1-2", "Executive thesis, customer value and current-state assessment"), ("3-5", "Reference architecture, data readiness, journeys and measurement"), ("6-7", "AI strategy, agentic AI and MCP governance"), ("8-9", "Operating model, governance and the business case"), ("10", "Capstone, executive review and 90-day plan")])
         + '<p><a href="cxo-hive-curriculum.html">Week-by-week curriculum &rarr;</a> &middot; <a href="cxo-hive-operating-model.html">CIO-CMO alignment and governance guide &rarr;</a></p>', "alt", "Curriculum"),
        ("How the program works", table(["Element", "Detail"], [("Format", CFG["format"]), ("Weekend sessions", f'{CFG["hours_per_weekend_day"]} hours on Saturday and {CFG["hours_per_weekend_day"]} hours on Sunday'),
                                                               ("Midweek", f'{CFG["midweek_checkpoints_per_week"]} checkpoints per week, 30 to 45 minutes: unblock work and check the deliverable'), ("Timing", e(CFG["session_time_note"])),
                                                               ("Led by", "Pavan Babu Gandla, founder of Infinite360"), ("Work product", "Each week ends with an artifact you review with the faculty and peers")]), "plain", "Format"),
        ("Who it is for", '''<div class="grid-2"><div class="card"><h3>For</h3><ul class="checklist"><li>CEOs, founders and managing directors</li><li>CIOs and CTOs</li><li>CMOs, CDOs and Chief Product Officers</li><li>COOs and CFOs sponsoring digital programs</li><li>Chief AI, Data or Digital Officers</li></ul></div>
<div class="card"><h3>Not for</h3><p>Managers, architects and practitioners. For them, see the <a href="../../training/">Career Accelerator</a> or the <a href="live-customised-program.html">Live Customised MarTech Program</a>.</p></div></div>''', "alt", "Audience"),
        ("Fit check", readiness("../../"), "plain", "Is it right for you?"),
        ("Fee and enrolment", f'''<p><strong>Program fee: {FEE}.</strong> {e(CFG["fee_note"])}</p><ol class="steps"><li><strong>Apply</strong> &mdash; share your role and goals.</li><li><strong>Conversation</strong> &mdash; a short call to confirm fit and answer questions.</li><li><strong>Written confirmation</strong> &mdash; fee, schedule and terms in writing.</li><li><strong>Pay and onboard</strong> &mdash; baseline assessment and kick-off.</li></ol>
<p><a class="btn btn-primary" href="../../{APPLY}">Apply for CXO Hive</a> <a class="btn btn-ghost" href="{CFG["whatsapp"]}" rel="noopener" target="_blank">Ask on WhatsApp</a></p>''', "alt", "Fees"),
    ],
    faqs=[("Who can join CXO Hive?", "C-level executives only. Applications from other roles are redirected to the Career Accelerator or the Live Customised MarTech Program."),
          ("Is it technical?", "It is strategy- and architecture-led. You learn enough about data, identity, journeys and AI to decide and challenge, not to write code."),
          ("What outcome can I expect?", "Six executive artifacts built on your own organisation: an investment case, target architecture, operating model, AI backlog, 90-day roadmap and board briefing. Business results are not guaranteed."),
          ("Do you promise certification or business results?", "No. The program builds judgement and deliverables. Results depend on your organisation and execution."),
          ("Can my leadership team join together?", "Yes. Ask about a private in-house executive cohort; scope and price are agreed per engagement."),
          ("What is the time commitment?", f'Eight live hours each weekend for {CFG["weeks"]} weeks plus two short midweek checkpoints, with a small amount of preparation between sessions.')],
    related=["academy/programs/cxo-hive-curriculum.html", "academy/programs/cxo-hive-outcomes.html", "services/martech-strategy-advisory.html"],
))

PAGES_CXO.append(dict(
    path="academy/programs/cxo-hive-curriculum.html", nav="CXO Hive curriculum",
    title="CXO Hive Curriculum: 10 Weeks of MarTech & AI for Executives",
    desc="Week-by-week curriculum for CXO Hive: executive thesis, customer data, architecture, AI and agentic governance, operating model, business case and capstone.",
    h1="CXO Hive curriculum: ten weeks, week by week", kicker="Academy · C-level program", schema="Article", category="Academy", date="2026-10-28",
    keywords=["cxo program curriculum", "executive martech curriculum", "ai leadership syllabus"],
    answer="The CXO Hive curriculum runs ten weeks. Each weekend has a four-hour Saturday and a four-hour Sunday session, and every week ends with an executive artifact built on the participant's own organisation. Topics move from strategy and customer data to architecture, AI and agentic governance, operating model and the business case.",
    sections=[
        ("Weekly plan", table(["Week", "Theme", "Saturday and Sunday focus", "Working session", "Artifact"], [(w, f"<strong>{t}</strong>", a, b, c) for w, t, a, b, c in WEEKS]), "plain", "Curriculum"),
        ("Midweek checkpoints", "<ul class=\"checklist\"><li><strong>Checkpoint A:</strong> inspect evidence, unblock the current task, test assumptions and update the risk log.</li><li><strong>Checkpoint B:</strong> check the artifact against acceptance criteria, review progress against the mission and set the next commitment.</li></ul>", "alt", "Support"),
        ("Inside each four-hour session", table(["Time", "Activity", "Output"], SESSION), "plain", "Session design"),
        ("Platforms and references", "<p>Examples use Adobe Experience Platform, Real-Time CDP, Journey Optimizer and Customer Journey Analytics, with AI and agent patterns that apply across vendors. Official references are used first, including <a href=\"" + EL + "/experience-platform\" rel=\"noopener\">Adobe Experience Platform documentation</a> and the <a href=\"https://modelcontextprotocol.io/\" rel=\"noopener\">Model Context Protocol</a> site. Infinite360 is independent and is not an Adobe partner.</p>" + disclaimer(), "alt", "References"),
    ],
    faqs=[("Do I need prior Adobe experience?", "No. The program is strategy-led and explains each platform concept in business terms."),
          ("Are sessions recorded?", "The program is live. Whether recordings are shared is confirmed at enrolment.")],
    related=[MAIN, "academy/programs/cxo-hive-outcomes.html", "guides/what-is-mcp.html"],
))

PAGES_CXO.append(dict(
    path="academy/programs/cxo-hive-outcomes.html", nav="CXO Hive outcomes",
    title="CXO Hive Outcomes: Six Executive Deliverables You Build",
    desc="What CXO Hive participants produce: investment case, target architecture, operating model, AI backlog, 90-day roadmap and board briefing. No guaranteed results.",
    h1="CXO Hive outcomes and capstone", kicker="Academy · C-level program", schema="Article", category="Academy", date="2026-10-28",
    keywords=["executive program outcomes", "ai investment case", "martech roadmap deliverables"],
    answer="CXO Hive outcomes are six executive deliverables built on your own organisation: an investment case, a target-state architecture, an operating model with decision rights, a scored AI use-case backlog, a 90-day roadmap with baselines and targets, and a board-ready briefing. They are decisions and documents, not promised business results.",
    sections=[
        ("The six deliverables", table(["Deliverable", "What it contains", "Decision it supports"], [
            ("Executive investment case", "Options, cost, risk, owner, baseline, target, assumptions", "Fund, defer or stop an initiative"),
            ("Target-state architecture", "Data, identity, consent, platforms, AI components and boundaries", "Build, buy or configure"),
            ("Operating model and RACI", "Forums, cadence, decision rights, escalation, release gates", "Who decides what, and how fast"),
            ("AI use-case backlog", "Use cases scored by value, effort and risk; agent release checklist", "Which AI work to start first"),
            ("90-day roadmap", "Priorities, owners, KPIs, baselines and clearly labelled targets", "What happens next quarter"),
            ("Board-ready briefing", "A short narrative with risks, asks and measures", "Alignment with the board or committee")]), "plain", "Deliverables"),
        ("Capstone", "<p>In weeks 9 and 10 you assemble the deliverables into one executive story for your own organisation, present it to the cohort and faculty, and close gaps from the challenge session. Confidential data is not required: use sanitised or illustrative figures.</p>", "alt", "Capstone"),
        ("Definition of done", "<ul class=\"checklist\"><li>Problem, audience and assumptions are stated.</li><li>A diagram shows data flow and system boundaries.</li><li>Risks and failure modes are listed with owners.</li><li>A baseline and a target are shown, and the target is labelled as a target.</li><li>A three-minute briefing and a one-page summary exist.</li></ul>", "plain", "Standard"),
        ("How progress is tracked", table(["Dimension", "Leading indicator", "Outcome indicator"], [("Capability", "Sessions attended; exercises completed", "Quality of the capstone"), ("Decisions", "Decisions logged with owners", "Roadmap reviewed with your team"), ("Governance", "RACI drafted and circulated", "Operating cadence agreed internally"), ("AI readiness", "Use cases scored", "A release checklist applied to one pilot")]), "alt", "Measures"),
        ("What we do not promise", disclaimer() + "<p>Participants decide what to share publicly. Do not publish client names or confidential architecture without permission.</p>", "plain", "Honesty"),
    ],
    faqs=[("Will my board approve the plan?", "That is your organisation's decision. The program prepares a clear, well-evidenced briefing."),
          ("Can I keep the templates?", "Yes. Participants keep the templates and the artifacts they produce.")],
    related=[MAIN, "academy/programs/cxo-hive-curriculum.html", APPLY],
))

PAGES_CXO.append(dict(
    path="academy/programs/cxo-hive-operating-model.html", nav="CIO-CMO operating model",
    title="CIO-CMO Alignment: Operating Model for AI-Era MarTech",
    desc="A practical guide for C-level leaders: joint decision forums, a RACI for MarTech and AI, and a release checklist for governed agentic workflows.",
    h1="CIO-CMO alignment: an operating model for AI-era MarTech", kicker="Academy · C-level program", schema="Article", category="Academy", date="2026-10-28",
    keywords=["cio cmo alignment", "martech operating model", "ai governance raci", "agentic ai release checklist"],
    answer="Aligning the CIO and CMO means agreeing outcomes, decision rights and risk limits before scaling AI in MarTech. A monthly steering committee, a biweekly delivery review, weekly use-case squads and a pre-release control gate give each decision an owner and a cadence. A RACI and a release checklist keep agentic workflows accountable.",
    sections=[
        ("Why alignment comes first", "<p>MarTech and AI programs stall when technology and marketing leaders hold different priorities, data ownership is unclear and accountability for risk is fragmented. Platform delivery alone does not fix this; a shared agenda does.</p><ul class=\"checklist\"><li>One list of customer, revenue, productivity and risk outcomes.</li><li>One roadmap with funding decisions made jointly.</li><li>Named owners for data, identity, consent and AI risk.</li></ul>", "plain", "Context"),
        ("Operating cadence", table(["Forum", "Participants", "Output"], [("Monthly steering committee", "CMO, CIO or CTO, CDO, CISO, product and business owner", "Priorities, funding decisions, risk acceptance, value review"), ("Biweekly delivery review", "MarTech, data, engineering, analytics, security and operations leads", "Dependencies, delivery health, data-quality issues, release readiness"), ("Weekly use-case squad", "Product owner, journey owner, architect, data or AI engineer, analyst", "Working increment, results, decision log, next actions"), ("Pre-release control gate", "Business owner with security, privacy and platform owners", "Evaluation evidence, access controls, fallback and rollback plan")]), "alt", "Cadence"),
        ("Illustrative RACI", table(["Decision or activity", "Responsible", "Accountable", "Consulted or informed"], [("Business outcome and journey priority", "Product or journey team", "CMO or business sponsor", "CIO, analytics, sales and service"), ("Customer data quality and identity", "Data engineering and stewardship", "CDO or named data owner", "CMO, CIO, privacy, analytics"), ("Platform architecture and integration", "Architecture and engineering", "CIO or CTO", "CDO, CISO, MarTech owner"), ("AI risk, privacy and security controls", "AI governance, security, privacy", "Designated risk executive", "Business owner, legal, engineering"), ("Value measurement", "Analytics, finance, product", "Executive sponsor", "CMO, CIO, delivery lead")])
         + "<p class=\"small muted\">RACI: Responsible, Accountable, Consulted, Informed. Adapt to your organisation; each decision needs one accountable owner.</p>", "plain", "Decision rights"),
        ("Release checklist for agentic workflows", "<ul class=\"checklist\"><li>A job to be done and a baseline process are documented before agents are added.</li><li>The agent has least-privilege access, scoped tools, logging and clear approval boundaries.</li><li>Evaluation covers quality, groundedness, policy compliance, latency, cost and failure handling.</li><li>Human escalation, safe fallback, rollback and incident ownership are tested.</li><li>Business and technology owners agree launch criteria and post-launch monitoring.</li></ul>", "alt", "Control"),
        ("Use it in CXO Hive", "<p>You draft this operating model for your own organisation in week 8 and refine it in the capstone. See the <a href=\"executive-architecture-leadership.html\">CXO Hive program</a>.</p>", "plain", "Next step"),
    ],
    faqs=[("Is this specific to Adobe?", "No. The operating model applies to any MarTech and AI stack; examples use Adobe Experience Cloud."),
          ("Who is accountable for AI risk?", "One designated risk executive should be accountable, with security, privacy, legal and the business owner consulted.")],
    related=[MAIN, "guides/what-is-mcp.html", "insights/responsible-ai.html"],
))

PAGES_CXO.append(dict(
    path=APPLY, nav="Apply for CXO Hive",
    title="Apply for CXO Hive: C-Level MarTech & AI Program",
    desc=f"Apply for CXO Hive, a 10-week live program for C-level executives on MarTech, data and AI leadership. Fee {FEE}. Check your fit and apply.",
    h1="Apply for CXO Hive", kicker="C-level only",
    keywords=["cxo hive apply", "executive ai program admission", "c-level martech program"],
    answer=(f"CXO Hive is a {CFG['weeks']}-week live program for C-level executives, run every Saturday and Sunday, with a fee of {FEE}. Apply with your role and goals; we confirm fit in a short call and share fee, schedule and terms in writing before any payment."),
    schema="WebPage", interest="cxo", landing=True, hero_cta=("Apply now", "#enquire-form"), bands=True,
    sections=[
        ("Program summary", f'''<div class="contact-grid lp-grid"><div>{cohort_block()}<ul class="checklist"><li>{FEE} one-time program fee</li><li>100% live, Saturdays and Sundays, {CFG["weeks"]} weeks</li><li>Six executive deliverables on your own organisation</li><li>C-level executives only</li></ul>
<p><a href="../academy/programs/executive-architecture-leadership.html">Full program details</a> &middot; <a href="../academy/programs/cxo-hive-curriculum.html">Curriculum</a> &middot; <a href="../academy/programs/cxo-hive-outcomes.html">Outcomes</a></p>{disclaimer()}</div>
<div class="form-card" id="enquire-form">@@LP_FORM@@</div></div>''', "plain", "Apply"),
        ("Check your fit first", readiness("../"), "alt", "Optional"),
    ],
    faqs=[("What happens after I apply?", "We review your role and goals, then hold a short call. Fee, schedule and terms are sent in writing before any payment."),
          ("Is there a charge to apply?", "No. Nothing is charged until you agree and enrol.")],
    related=[MAIN],
))
