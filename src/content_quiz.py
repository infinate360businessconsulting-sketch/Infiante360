"""Free AEP BFSI scenario quiz (lead capture with consent) and the AJO technical best-practices handout."""
import html as _h, json
from content_cases import pills, WHATSAPP_MSG, REGISTER
e = _h.escape
EL = "https://experienceleague.adobe.com/en/docs"
EMAIL = "infinate360businessconsulting@gmail.com"
BASE = "https://infiante360techacademy.com/"
PASS = 14

# (question, correct, [wrong x3], why)
Q = [
("A bank's segment is 'cardholders with monthly spend above ₹50,000 in the last 90 days'. Transactions arrive in one nightly batch. Which evaluation setup fits?",
 "Evaluate daily after the transaction batch completes", ["Evaluate every 5 minutes", "Evaluate once a year", "Evaluate once at go-live and never again"],
 "The data refreshes daily, so a daily run after the load keeps the segment fresh without paying for needless recomputation."),
("A customer taps 'Stop all marketing' in the mobile app. The bank must stop push and SMS within minutes, but consent flows only in nightly CRM batches. What must change?",
 "Stream consent changes and use real-time evaluation or decisioning for suppression", ["Keep the nightly batch and hope it is fast enough", "Send only email instead", "Ingest consent changes once a month"],
 "An opt-out is a compliance event. It has to reach suppression logic in near real time."),
("A bank has rich first-party data (balances, products, tenure) and third-party income bands with 70% coverage. What should be the core signal for 'premium upgrade eligibility'?",
 "First-party relationship value and behaviour, with third-party income as enrichment", ["Third-party income bands only", "Third-party social interests only", "Anonymous cookie behaviour only"],
 "Trusted first-party data drives eligibility. Third-party data enriches it and should not replace it."),
("A co-branded travel card sends partner spend data every 3 days. The bank wants 'travel spend in the last 24 hours' to trigger offers. What is the key constraint?",
 "The 3-day feed latency makes a 24-hour window incomplete or stale", ["There is no constraint", "The segment will be real time anyway", "Partner data can backfill missing KYC"],
 "A segment cannot be fresher than its slowest input. Change the window or the feed frequency."),
("Core banking holds an old email address. The authenticated digital profile holds a newer verified one. How should the merge policy treat email for marketing segments?",
 "Prefer the most recent verified email from authenticated digital channels", ["Always trust core banking", "Pick a source at random", "Keep both and use neither"],
 "A self-service update by a logged-in customer is the better signal for contact data."),
("'KYC completed' rarely changes. 'App logins in the last 7 days' changes constantly. How should evaluation cadence differ?",
 "Refresh KYC-based segments less often and behaviour-based segments more often", ["Use the same ultra-frequent schedule for all", "Evaluate behaviour yearly and KYC every minute", "Never re-evaluate after creation"],
 "Match the refresh rate to how quickly the underlying data changes."),
("A bank streams web events (loan calculator visits) and loads CRM product data nightly. It wants 'high online loan intent but no active loan'. How should it design this?",
 "Combine streaming intent events with the nightly CRM loan-ownership flag", ["Use CRM batches only", "Use streaming events only and ignore ownership", "Use third-party intent only"],
 "Pair a fast behavioural signal with a slower but trusted status attribute."),
("A bank wants '3+ card declines in the last 5 minutes' to trigger step-up authentication, but data lands as hourly files. What is the main gap?",
 "The ingestion and evaluation pattern is batch and cannot meet a 5-minute threshold", ["Too much first-party data", "The segment definition is too simple", "Merge policies will fix the delay"],
 "A 5-minute window needs streaming ingestion and real-time evaluation."),
("Agents record free-text notes ('customer disputed fee') and also a structured dispute_flag. What is the more robust primary condition for 'recent dispute'?",
 "The structured dispute_flag with a time window", ["Search the notes for the word 'angry'", "Call duration only", "Random keywords from the notes"],
 "A governed structured flag is easier to test and trust. Notes can be secondary enrichment."),
("A 'pre-approved loan' segment is evaluated daily at 2 AM and emails go out at 4 PM. Why do customers who became eligible at noon not get an offer that day?",
 "Evaluation runs only at 2 AM, so they join at the next run", ["Segments always include future customers", "The email tool is wrong", "Profiles are deleted every day"],
 "Evaluation time is decoupled from send time. Membership is a snapshot."),
("A bank wants a WhatsApp follow-up 10 minutes after an incomplete credit card application, but applications arrive as a daily CSV. What must change?",
 "Switch application events to streaming or near-real-time ingestion", ["Keep the CSV and send next month", "Use third-party SMS data", "Rely on branch visits"],
 "A 10-minute reaction needs the event to arrive within minutes."),
("A bank receives telco segments keyed by a hashed phone number. Its profiles use customer_id and phone_number. What must be in place to use them?",
 "An identity strategy that maps the hashed phone to known customer identities", ["Ignore the telco identifiers", "Create a random ID mapping", "Delete the data after ingestion"],
 "Second-party segments are only usable at person level when the external ID ties into your identity graph."),
("A bank buys third-party credit scores and wants 'medium income, high score, no existing loan'. What is a safe design principle?",
 "Restrict access and use scores as governed attributes combined with first-party data", ["Use scores for any purpose", "Expose scores to every downstream system", "Share scores automatically with partners"],
 "Sensitive attributes need governance, access control and purpose limits."),
("A segment should be 'more than 3 ATM withdrawals in the last 30 days', but the engineer sets a 365-day look-back. What happens?",
 "The segment grows and includes customers whose activity is not recent", ["The segment shrinks", "Nothing changes", "Only new customers qualify"],
 "A longer window counts older activity and inflates membership."),
("KYC data is strictly validated while marketing CRM holds free-text occupation. For regulated segments like 'self-employed customers', which source should the merge policy prefer?",
 "The KYC system as the system of record", ["CRM free text", "Whichever updated last, regardless of source", "A random source"],
 "Regulated attributes should come from the validated system of record."),
("A customer reports a stolen card in real time, but marketing SMS uses daily-refreshed segments. What is the risk?",
 "The customer may still get marketing SMS until the next refresh", ["No risk", "The customer receives fewer messages", "The card is unblocked automatically"],
 "A delay between a critical event and suppression can break trust and compliance."),
("A bank buys third-party 'auto-intender' audiences and also has first-party browsing on car-loan pages. What is a robust 'high auto intent' approach?",
 "Use first-party browsing and applications as primary, with third-party intent as a secondary signal", ["Third-party audiences only", "Ignore consent and combine everything", "Random selection"],
 "Real visits and applications are more precise. Third-party intent complements them."),
("A segment feeds weekly analytics dashboards and daily AJO activation. Why might the counts differ?",
 "Different evaluation cadences give different snapshots", ["They must always match", "One tool is always wrong", "Profiles are deleted at random"],
 "Membership depends on data state and evaluation time."),
("'Mass affluent' is defined only by credit card spend, yet many high-value customers hold deposits and use cards little. What is the core design issue?",
 "The segment relied on one product behaviour and ignored deposits and investments", ["Too much third-party data", "Merge policies are broken", "Too many identities"],
 "Value segmentation should use several first-party dimensions, not one product."),
("A bank wants 'dropped at the KYC step in the last hour' but ingests funnel events as daily batch logs. Can it do this?",
 "Not realistically; it needs real-time or very frequent ingestion", ["Yes, perfectly", "Yes, but only next year", "Only for very old customers"],
 "Hour-level funnel segments need near-real-time events."),
]
assert len(Q) == 20
DATA = json.dumps([{"q": q, "a": a, "w": w, "e": ex} for q, a, w, ex in Q], ensure_ascii=False).replace("</", "<\\/")

def _field(i, label, typ="text", auto="", req=True, hint=""):
    r = ' required aria-required="true"' if req else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if req else ""
    return (f'<div class="field"><label for="z-{i}">{label}{star}</label><input id="z-{i}" name="{i}" type="{typ}" autocomplete="{auto}"{r} aria-describedby="z-{i}-error" data-msg-required="Please fill this in."'
            + (' pattern="[+0-9 ()-]{7,20}" data-msg-pattern="Use digits, spaces and + only."' if typ == "tel" else "")
            + f'><span class="error" id="z-{i}-error" aria-live="polite"></span></div>')

FORM = f'''<div id="quiz-gate"><form class="form js-validate" action="https://formsubmit.co/{EMAIL}" method="POST" aria-describedby="z-note">
<input type="hidden" name="_subject" value="New AEP BFSI quiz registration"><input type="hidden" name="_template" value="table"><input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="{BASE}academy/aep-bfsi-quiz.html?quiz=1"><input type="hidden" name="form_type" value="quiz"><input type="hidden" name="interest" value="AEP BFSI scenario quiz"><input type="hidden" name="source_page" value="">
<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
{_field("name", "Your name", auto="name")}{_field("email", "Email", "email", "email")}{_field("phone", "Phone / WhatsApp", "tel", "tel")}
<div class="field full"><div class="consent"><input id="z-consent" name="consent" type="checkbox" value="yes" required aria-required="true" aria-describedby="z-consent-error" data-msg-required="Please confirm to continue.">
<label for="z-consent" style="font-weight:500">I agree that Infinite360 Tech Academy may contact me about this quiz, the handout and its programmes, as described in the <a href="../privacy-policy.html">privacy policy</a>. I can unsubscribe at any time.</label></div><span class="error" id="z-consent-error" aria-live="polite"></span></div>
<div class="field full"><button class="btn btn-primary" type="submit">Start the free quiz</button><p class="hint" id="z-note">Free. 20 questions, about 15 minutes. Score {PASS} or more to get the AJO handout link.</p><p class="form-status" role="status" aria-live="polite"></p></div>
</form></div>'''

JS = """<div id="quiz-app" hidden></div><noscript><p>This quiz needs JavaScript. You can still read the <a href="ajo-best-practices-handout.html">AJO handout</a>.</p></noscript>
<script>(function(){var D=%s,PASS=%d,gate=document.getElementById('quiz-gate'),app=document.getElementById('quiz-app');
try{var f=gate.querySelector('form');f.addEventListener('submit',function(){try{sessionStorage.setItem('i360_quiz',JSON.stringify({name:f.name.value,email:f.email.value,phone:f.phone.value}))}catch(x){}})}catch(x){}
if(!/[?&]quiz=1/.test(location.search))return;gate.hidden=true;app.hidden=false;
function sh(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
var i=0,score=0,qs=D.map(function(d){return{q:d.q,e:d.e,a:d.a,o:sh([d.a].concat(d.w))}});
function done(){var ok=score>=PASS;app.innerHTML='<h2>Your score: '+score+' / '+D.length+'</h2>'+(ok?'<p>Well done. Here is your free handout.</p><p><a class="btn btn-primary" href="ajo-best-practices-handout.html">Open the AJO technical best-practices handout</a></p>':'<p>You need '+PASS+' to unlock the handout link. Review the explanations and try again.</p><p><a class="btn btn-primary" href="aep-bfsi-quiz.html?quiz=1">Retake the quiz</a></p>')+'<p>Next: <a href="aep-launchpad-bootcamp.html">AEP Launchpad bootcamp</a> · <a href="workshops.html">Friday workshops</a></p>';
try{var l=JSON.parse(sessionStorage.getItem('i360_quiz')||'null');if(l&&navigator.sendBeacon)navigator.sendBeacon('/api/lead',new Blob([JSON.stringify({name:l.name,email:l.email,phone:l.phone,form_type:'quiz_result',interest:'AEP BFSI scenario quiz',message:'Quiz score '+score+'/'+D.length,source_page:location.href})],{type:'application/json'}))}catch(x){}
window.dataLayer=window.dataLayer||[];window.dataLayer.push({event:'quiz_complete',quiz_score:score})}
function show(){var c=qs[i],h='<p class="muted">Question '+(i+1)+' of '+D.length+'</p><h2 id="qt" style="font-size:1.15rem">'+c.q+'</h2><div class="choice" role="group" aria-labelledby="qt" style="display:grid;gap:10px">';
c.o.forEach(function(o,k){h+='<button type="button" class="btn btn-ghost" data-k="'+k+'" style="text-align:left;white-space:normal">'+o+'</button>'});h+='</div><div id="fb" role="status" aria-live="polite"></div>';app.innerHTML=h;
app.querySelectorAll('button[data-k]').forEach(function(b){b.onclick=function(){var ok=c.o[b.dataset.k]===c.a;if(ok)score++;app.querySelectorAll('button[data-k]').forEach(function(x){x.disabled=true;if(c.o[x.dataset.k]===c.a)x.style.outline='3px solid #10B981'});
document.getElementById('fb').innerHTML='<p><strong>'+(ok?'Correct.':'Not quite.')+'</strong> '+c.e+'</p><button type="button" class="btn btn-primary" id="nx">'+(i+1<D.length?'Next question':'See my score')+'</button>';
document.getElementById('nx').onclick=function(){i++;i<D.length?show():done()};document.getElementById('nx').focus()}})}
show()})();</script>""" % (DATA, PASS)

QUIZ_PAGE = dict(
    path="academy/aep-bfsi-quiz.html",
    title="Free AEP Quiz for BFSI: 20 Segmentation & Data Scenarios",
    desc="Test your Adobe Experience Platform skills with 20 banking scenarios on segments, merge policies, streaming vs batch and consent. Free, with a handout.",
    h1="Free AEP quiz: 20 banking and financial-services scenarios",
    kicker="Free quiz", nav="AEP quiz", schema="Article", category="Academy", date="2026-10-12",
    keywords=["aep interview questions", "aep segmentation quiz", "adobe experience platform quiz", "aep merge policy", "aep streaming vs batch"],
    answer=f"This free quiz has 20 scenario questions for banking and financial-services use of Adobe Experience Platform: segment evaluation, streaming versus batch data, merge policies, consent suppression and first-, second- and third-party data. Score {PASS} or more to unlock a free AJO technical best-practices handout. Registering takes a name, email and phone number, with your consent.",
    sections=[
        ("Take the quiz", FORM + JS),
        ("What you will practise", '<ul class="checklist"><li>Choosing batch, streaming and real-time evaluation</li><li>Merge policies and system-of-record choices</li><li>Consent, suppression and compliance timing</li><li>Using first-, second- and third-party data responsibly</li><li>Look-back windows and identity mapping</li></ul><p>The scenarios are teaching examples, not client engagements.</p>'),
        ("Keep learning", pills(("AJO handout", "ajo-best-practices-handout.html"), ("AEP Launchpad bootcamp", "aep-launchpad-bootcamp.html"), ("Friday workshops", "workshops.html"), ("Register", REGISTER), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Is the quiz really free?", "Yes. You share your name, email and phone number so we can send the handout details and follow up with your consent. You can unsubscribe at any time."),
          ("Do I need to pass to read the handout?", f"A score of {PASS} or more shows you the handout link on the results screen. The handout page is also linked from the Academy."),
          ("Does a good score certify me?", "No. It is a practice quiz, not a certification.")],
    related=["academy/index.html", "academy/free-resources.html", "academy/workshops.html", "academy/lesson-topics.html"],
    sources=[("Adobe Experience Platform documentation", f"{EL}/experience-platform"), ("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer")],
)

PRACTICES = [
("Design around events", "Name journey events clearly, agree the event schema first, and keep one unitary event per business moment (for example, cart abandon). Test with real payload shapes, not guesses."),
("Plan entry and re-entry", "Decide whether a person can re-enter a journey and after how long. Add exit conditions so people leave when the goal is met or they opt out."),
("Check consent and channel permissions", "Apply consent and channel preferences before each send. Treat opt-out as a real-time event and confirm the suppression path works end to end."),
("Use frequency and capping controls", "Set limits so one person is not messaged from several journeys at once. Review rules whenever you launch a new journey."),
("Prefer one trusted audience source", "Document which audience feeds a journey, how often it refreshes, and who owns it. Do not mix evaluation methods without knowing the latency of each."),
("Test before you publish", "Use test profiles and the product's testing tools, check each path, and confirm tokens, fallbacks and links render correctly before going live."),
("Separate environments", "Use development and production sandboxes with a clear promotion process, naming rules and change log."),
("Govern the data", "Apply data usage labels and policies to sensitive fields. Keep regulated data out of channels and destinations where it is not allowed."),
("Measure with a holdout", "Keep a small control group so the reported lift is real, and define the KPI before launch."),
("Monitor and clean up", "Watch journey reports and error rates after launch, pause failing journeys, and retire old ones regularly."),
]
HANDOUT_PAGE = dict(
    path="academy/ajo-best-practices-handout.html",
    title="AJO Technical Best Practices Handout: 10-Point Checklist",
    desc="A free 10-point Adobe Journey Optimizer technical checklist: events, re-entry, consent, capping, audiences, testing, environments, governance and measurement.",
    h1="Adobe Journey Optimizer technical best-practices handout",
    kicker="Free handout", nav="AJO handout", schema="Article", category="Academy", date="2026-10-12",
    keywords=["ajo implementation best practices", "adobe journey optimizer tutorial", "ajo event trigger", "ajo consent frequency capping"],
    answer="A good Adobe Journey Optimizer (AJO) implementation starts with a clear event design, then controls re-entry, consent, frequency, audience refresh, testing, environments, data governance and measurement. This free 10-point checklist from Infinite360 Tech Academy turns those into steps you can review before any journey goes live. Check each point against Adobe's current documentation.",
    sections=[
        ("The 10 checks", '<ol class="steps">' + "".join(f"<li><strong>{e(t)}.</strong> {e(d)}</li>" for t, d in PRACTICES) + "</ol>"),
        ("Before you launch", '<p>Print this page or save it as a PDF from your browser. It is general guidance, not a substitute for Adobe documentation or your own compliance review. Product features change, so confirm details in the sources below.</p>'),
        ("Practise and go deeper", pills(("Take the free AEP quiz", "aep-bfsi-quiz.html"), ("AJO training", "courses/ajo-training.html"), ("Friday workshops", "workshops.html"), ("Chat on WhatsApp", WHATSAPP_MSG))),
    ],
    faqs=[("Is this handout free?", "Yes. It is a free checklist from Infinite360 Tech Academy."),
          ("Is it official Adobe guidance?", "No. It is our own summary. Use Adobe Experience League for official product guidance.")],
    related=["academy/index.html", "academy/aep-bfsi-quiz.html", "academy/courses/ajo-training.html", "academy/free-resources.html"],
    sources=[("Adobe Journey Optimizer documentation", f"{EL}/journey-optimizer"), ("Adobe Experience Platform documentation", f"{EL}/experience-platform")],
)
QUIZ_ALL = [QUIZ_PAGE, HANDOUT_PAGE]
