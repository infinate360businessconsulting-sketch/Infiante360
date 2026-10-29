"""Cold-email campaign landing page: one noindex page, four segment panels chosen by utm_content, same form as the rest of the site.
Segments: enterprise | cxo | training | capacity. Fee and cohort come from content/cxo-hive.json."""
from content_cxo import CFG, FEE, cohort_block, MAIN as CXO_MAIN

SEGS = [
    ("enterprise", "Enterprise Adobe teams", "MarTech strategy / architecture review", "Architecture review",
     "<h3>Independent architecture review</h3><p>For CDOs, CTOs, VPs of MarTech and architects running or planning Adobe Experience Platform, Real-Time CDP, Journey Optimizer or Customer Journey Analytics.</p>"
     "<ul class=\"checklist\"><li>Schemas, datasets, identity and Profile configuration reviewed</li><li>Ingestion, governance and consent checked</li><li>Audiences, journeys and destinations assessed</li><li>Prioritised findings and a 30/60/90-day plan</li></ul>"
     "<p><a href=\"aep-architecture-review.html\">See how the review works</a></p>"),
    ("cxo", "C-level leaders", "CXO Hive: C-level program", "CXO Hive",
     f"<h3>CXO Hive: a 10-week live program for C-level executives</h3><p>Architecture, AI governance, an operating model and an executive investment case, built on your own organisation. Fee {FEE}.</p>{cohort_block()}"
     "<ul class=\"checklist\"><li>Live every Saturday and Sunday plus two short midweek checkpoints</li><li>Six executive deliverables you keep</li><li>C-level only; no job, salary or certification guarantee</li></ul>"
     f"<p><a href=\"../{CXO_MAIN}\">Full program details</a> &middot; <a href=\"cxo-hive-apply.html\">Apply directly</a></p>"),
    ("training", "L&amp;D and capability leaders", "Corporate training", "Corporate training",
     "<h3>Role-based Adobe MarTech training for your team</h3><p>Tracks for engineers, analysts, architects and managers, with hands-on labs, assessments and progress reporting.</p>"
     "<ul class=\"checklist\"><li>Skills baseline for your team</li><li>Labs built on your use cases</li><li>Live, recorded or blended delivery</li></ul><p><a href=\"corporate-adobe-training.html\">Request a proposal</a></p>"),
    ("capacity", "SI and delivery leaders", "Staff augmentation (engineers / architects)", "Specialist capacity",
     "<h3>Specialist Adobe capacity for your delivery team</h3><p>Architects, engineers and consultants for AEP, RTCDP, AJO, CJA and Web SDK work, scoped per project.</p>"
     "<ul class=\"checklist\"><li>Contract, contract-to-hire or managed pod</li><li>Scenario-based readiness checks</li><li>Onboarding prepared before day one</li></ul>"),
]
import json as _j
_tabs = "".join(f'<button type="button" role="tab" class="btn btn-ghost" data-seg="{k}" data-interest="{i}" aria-selected="false">{n}</button> ' for k, n, i, _, _h in SEGS)
_panels = "".join(f'<div class="card" role="tabpanel" data-panel="{k}">{h}</div>' for k, _n, _i, _s, h in SEGS)
SCRIPT = """<script>(function(){try{var q=new URLSearchParams(location.search),want=q.get("utm_content")||"enterprise",
tabs=document.querySelectorAll("[data-seg]"),panels=document.querySelectorAll("[data-panel]"),sel=document.querySelector("#enquire-form select[name=interest]");
function show(k){var ok=false;tabs.forEach(function(t){if(t.dataset.seg===k)ok=true});if(!ok)k="enterprise";
tabs.forEach(function(t){var on=t.dataset.seg===k;t.setAttribute("aria-selected",on);t.style.outline=on?"2px solid #4F46E5":"none"});
panels.forEach(function(p){p.hidden=p.dataset.panel!==k});
if(sel){tabs.forEach(function(t){if(t.dataset.seg===k){for(var i=0;i<sel.options.length;i++){if(sel.options[i].text===t.dataset.interest){sel.selectedIndex=i}}}})}}
tabs.forEach(function(t){t.addEventListener("click",function(){show(t.dataset.seg)})});show(want);document.querySelector("[data-tabs]").classList.add("js")}catch(x){}})();</script>"""
PAGES_CAMPAIGN = [dict(
    path="lp/adobe-martech-conversation.html", nav="Adobe MarTech conversation",
    title="Book an Adobe MarTech Conversation | Infinate360",
    desc="Choose your path: architecture review, CXO Hive, corporate training or specialist Adobe capacity. Tell us what you need and we reply with next steps.",
    h1="Let's talk about your Adobe MarTech priorities", kicker="Get started",
    keywords=["adobe martech consultation", "book martech call"], answer="Pick the option that matches your role, then use the form. We read every enquiry, reply with next steps, and charge nothing until you agree a proposal or enrol. Infinate360 is independent and not an Adobe partner.",
    schema="WebPage", landing=True, robots="noindex,follow", hero_cta=("Fill in the form", "#enquire-form"),
    sections=[("Choose your path", f'<div data-tabs><div role="tablist" aria-label="Your role" class="cta-row">{_tabs}</div><div style="margin-top:16px">{_panels}</div></div>'
               '<div class="form-card" id="enquire-form" style="margin-top:24px">@@LP_FORM@@</div>' + SCRIPT, "plain", "Options")],
    faqs=[("Is there any cost to enquire?", "No. We reply with next steps; nothing is charged until you agree a proposal or enrol."),
          ("How quickly will you reply?", "Usually within two business days, or faster on WhatsApp.")],
    related=[],
)]
