"""/lms: learning suite landing page (login, activation codes, test series, live classes, smart path finder)."""
import html
e = html.escape
PATH = "lms.html"
LOGIN = "https://techacademy.infinate360.in/"
CLASSROOM = "https://techacademy.infinate360.in/static/media/appx_dl.html?digest=eyJhY3RfY29kZSI6MSwiYWN0X2RhdGEiOjIxOTE1LCJleGFtX3VybCI6Ii90ZXN0cy8xNDc5L2FlcC1yZWFsd29ybGQtdXNlLWNhc2UtdGVzdC1zZXJpZXMifQ=="
LNK = 'rel="noopener" target="_blank"'

suite = [
 ("Live classes", "Scheduled live sessions with the trainer, joined from your learning account."),
 ("Recorded video courses", "On-demand lessons you can revisit at your own pace once your access is active."),
 ("Test series", "Timed practice tests with scores and a test report so you can see where to improve."),
 ("E-library", "Reading material and reference resources alongside the courses."),
 ("Activation codes", "Your access is switched on with a code from Infinite360, so each plan and batch is controlled by us."),
 ("Progress and reports", "Test results and learner activity are tracked inside the platform."),
]
steps = [
 ("Enrol", "Choose a program or membership and complete payment or enrolment with Infinite360."),
 ("Get your code", "We send an activation code for your plan or batch to your registered email or WhatsApp."),
 ("Log in", f'Open the <a href="{LOGIN}" {LNK}>learning platform</a> and sign in or create your account.'),
 ("Activate", "Enter the activation code under your account to unlock the courses and test series in your plan."),
 ("Learn", "Join live classes, watch recordings and attempt tests from the same account."),
]

FINDER = """<div class="card" id="finder" style="max-width:720px">
<div class="form-grid">
<div class="field"><label for="pf-role">Your role</label><select id="pf-role"><option value="dev">Developer or data engineer</option><option value="mkt">Marketing or MarTech practitioner</option><option value="arch">Architect or consultant</option><option value="lead">C-level or senior leader</option><option value="new">Career switcher or fresher</option><option value="team">Training for a team</option></select></div>
<div class="field"><label for="pf-goal">Your goal</label><select id="pf-goal"><option value="job">Get career ready</option><option value="skill">Learn one tool well</option><option value="cert">Practice with tests</option><option value="lead">Lead MarTech and AI programs</option></select></div>
<div class="field"><label for="pf-mode">How you like to learn</label><select id="pf-mode"><option value="live">Live with a trainer</option><option value="self">Recorded, self-paced</option></select></div>
</div>
<p class="cta-row"><button class="btn btn-primary" type="button" id="pf-go">Suggest a path</button></p>
<p id="pf-out" role="status" aria-live="polite" style="font-weight:600;margin-top:10px"></p>
<p class="small muted">This is a simple rule-based guide, not a personal assessment. Nothing you select is stored or sent.</p></div>
<script>(function(){var P={
cxo:["CXO Hive executive program","academy/programs/executive-architecture-leadership.html"],
team:["Live customised program for teams","academy/programs/live-customised-program.html"],
acc:["Adobe MarTech + Agentic AI Career Accelerator (live)","training/index.html"],
fnd:["Foundation + Advanced Architecture (recorded)","academy/programs/aep-ajo-cja-foundation-advanced.html"],
bro:["Bronze Membership: recorded videos, question bank and sandbox","academy/programs/bronze-membership.html"]};
function pick(r,g,m){if(r==="lead"||g==="lead")return "cxo";if(r==="team")return "team";if(g==="cert"||(g==="skill"&&m==="self"))return "bro";if(m==="self")return "fnd";return "acc"}
var b=document.getElementById("pf-go");if(!b)return;b.addEventListener("click",function(){
var k=pick(document.getElementById("pf-role").value,document.getElementById("pf-goal").value,document.getElementById("pf-mode").value),o=document.getElementById("pf-out");
o.textContent="";var t=document.createTextNode("Suggested: "+P[k][0]+". "),a=document.createElement("a");a.href=ROOTP+P[k][1];a.textContent="View program";o.appendChild(t);o.appendChild(a)})})();</script>""".replace("ROOTP", '"./"')

PAGES_LMS = [dict(
 path=PATH, nav="Learning suite (LMS)",
 title="Infinite360 Learning Suite: Login, Live Classes and Test Series",
 desc="Log in to the Infinite360 learning suite for live classes, recorded video courses and test series. Access is activated with a code from Infinite360.",
 h1="Infinite360 learning suite", kicker="Academy · Learning platform",
 keywords=["infinite360 lms login", "adobe martech test series", "aep live classes login", "activation code learning platform"],
 answer="The Infinite360 learning suite is where enrolled learners log in for live classes, recorded video courses and test series. Access is switched on with an activation code issued by Infinite360 for your plan or batch. Sign in on the learning platform, enter your code and start learning.",
 schema="WebPage", landing=False, interest="lms", hero_cta=("Log in to the learning platform", LOGIN),
 sections=[
  ("Log in or activate your access", f'<p>Already enrolled? Sign in and enter your activation code.</p><p class="cta-row"><a class="btn btn-primary" href="{LOGIN}" {LNK}>Log in to the learning platform &rarr;</a><a class="btn btn-ghost" href="{CLASSROOM}" {LNK}>Open the live classroom</a><a class="btn btn-ghost" href="#activation-help">Need a code?</a></p>', "plain", "Login"),
  ("How access works", '<ol class="steps">' + "".join(f"<li><strong>{e(a)}.</strong> {b}</li>" for a, b in steps) + "</ol>", "alt", "Steps"),
  ("What is in the suite", '<div class="grid-3">' + "".join(f'<div class="card"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in suite) + "</div><p class=\"small muted\">What you can open depends on your plan or batch. Programs and prices are listed on the <a href=\"academy/index.html\">academy page</a>.</p>", "plain", "Features"),
  ("Smart path finder (AI-style guide)", "<p>Not sure where to start? Answer three questions and get a suggested program.</p>" + FINDER, "alt", "Guide"),
  ("Where AI fits in learning here", '<ul class="checklist"><li><strong>Live now:</strong> the rule-based path finder above, and Agentic AI and MCP content inside the programs.</li><li><strong>Planned, not live:</strong> an AI study assistant that answers questions from the course material, and AI-generated practice questions reviewed by an instructor.</li></ul><p class="small muted">We will announce AI features only when they are live and tested.</p>', "plain", "AI"),
  ("Need an activation code or help logging in?", '<div id="activation-help"></div><p>Send the form below with the email you used to enrol and the program or batch name, or message <a href="https://wa.me/918296893895" rel="noopener" target="_blank">+91 82968 93895</a>. Do not send passwords or payment details.</p><div class="form-card">@@LP_FORM@@</div>', "alt", "Help"),
 ],
 faqs=[("How do I get an activation code?", "Infinite360 issues a code after enrolment for your plan or batch. If you have not received one, send the help form."),
       ("I forgot my password.", "Use the password reset option on the learning platform login page, or send the help form."),
       ("Can I use the same code on two accounts?", "No. A code unlocks one plan for the account that redeems it."),
       ("Are test series included in every plan?", "It depends on your plan. Check the program page or ask us before enrolling.")],
 related=["academy/index.html", "academy/free-resources.html"],
)]
