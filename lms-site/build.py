#!/usr/bin/env python3
"""Static builder for the Infiante360 LMS site. Output: HTML files at repo root + assets/."""
import html, json, os
from data import CONFIG as C, SIMULATORS, KB, STEPS

ROOT = os.path.dirname(os.path.abspath(__file__))
E = html.escape
WA = "https://wa.me/" + C["wa"]


def wa(msg):
    from urllib.parse import quote
    return f"{WA}?text={quote(msg)}"


CSS = """
:root{--bg:#06122a;--bg2:#0b1f44;--card:#0f2752;--line:#1e3a6e;--tx:#eaf2ff;--mut:#9db4d8;--cy:#22d3ee;--or:#f59e0b;--ok:#34d399}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:16px/1.6 "Plus Jakarta Sans",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--tx)}
a{color:var(--cy)}a:focus-visible,button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible{outline:3px solid var(--or);outline-offset:2px}
.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;color:#000;padding:8px;z-index:99}
.ribbon{background:linear-gradient(90deg,#b45309,#f59e0b);color:#111;font-weight:600;text-align:center;padding:8px 40px;position:relative;font-size:14px}
.ribbon a{color:#111;text-decoration:underline;margin-left:8px}.ribbon button{position:absolute;right:10px;top:4px;background:none;border:0;font-size:20px;cursor:pointer;color:#111}
header.top{display:flex;align-items:center;gap:16px;flex-wrap:wrap;padding:12px 20px;background:rgba(6,18,42,.92);border-bottom:1px solid var(--line);position:sticky;top:0;z-index:10;backdrop-filter:blur(8px)}
.brand{display:flex;align-items:center;gap:10px;color:var(--tx);text-decoration:none;font-weight:800}.brand img{width:40px;height:40px;border-radius:10px}
.brand small{display:block;font-weight:500;color:var(--mut);font-size:12px;line-height:1}
nav.main{display:flex;gap:4px;flex-wrap:wrap;margin-left:auto}nav.main a{color:var(--tx);text-decoration:none;padding:8px 12px;border-radius:8px;font-size:15px}
nav.main a:hover,nav.main a[aria-current=page]{background:var(--card)}
.btn{display:inline-block;padding:12px 20px;border-radius:12px;font-weight:700;text-decoration:none;border:1px solid var(--line);color:var(--tx);background:var(--card);cursor:pointer;font-size:16px}
.btn.pri{background:linear-gradient(135deg,var(--or),#fb923c);color:#111;border:0}.btn.cy{background:linear-gradient(135deg,#0891b2,var(--cy));color:#04131f;border:0}
.btn:hover{transform:translateY(-2px);box-shadow:0 10px 24px rgba(0,0,0,.35)}
main{max-width:1120px;margin:0 auto;padding:28px 20px 70px}
.hero{display:grid;grid-template-columns:1.2fr .8fr;gap:36px;align-items:center;padding:28px 0 36px}
.hero h1{font-size:clamp(30px,4.6vw,52px);line-height:1.1;margin:.2em 0}.hero p.lead{color:var(--mut);font-size:18px;max-width:56ch}
.kick{color:var(--cy);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:13px}
.scene{perspective:900px}.tilt{transform-style:preserve-3d;transition:transform .15s ease-out;background:linear-gradient(145deg,#0f2d5f,#0a1a3a);border:1px solid var(--line);border-radius:22px;padding:26px;box-shadow:0 30px 60px rgba(0,0,0,.5)}
.tilt img{width:100%;border-radius:14px;transform:translateZ(40px);display:block}.tilt .chip{display:inline-block;margin:10px 6px 0 0;padding:4px 12px;border-radius:99px;background:#0b1f44;border:1px solid var(--line);color:var(--mut);font-size:13px;transform:translateZ(25px)}
.grid{display:grid;gap:18px;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:20px}.card h3{margin:.1em 0 .4em}.card p{color:var(--mut);margin:.3em 0 .9em}
h2{font-size:28px;margin:44px 0 14px}.pill{display:inline-block;font-size:12px;padding:2px 10px;border-radius:99px;background:#0b1f44;border:1px solid var(--line);color:var(--cy)}
.steps{counter-reset:s;list-style:none;padding:0;display:grid;gap:12px}.steps li{counter-increment:s;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 18px 14px 58px;position:relative}
.steps li:before{content:counter(s);position:absolute;left:16px;top:12px;width:30px;height:30px;border-radius:50%;background:var(--or);color:#111;font-weight:800;display:grid;place-items:center}
.note{background:#1a2a14;border:1px solid #3f6212;border-radius:12px;padding:12px 16px;color:#d9f99d}.warn{background:#2a1a0a;border:1px solid #92400e;color:#fde68a}
details{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0}summary{cursor:pointer;font-weight:700}
details p{color:var(--mut)}input[type=search],input[type=text],textarea,select{width:100%;padding:12px;border-radius:10px;border:1px solid var(--line);background:#081833;color:var(--tx);font:inherit}
img{max-width:100%;height:auto}.ph{border:2px dashed var(--line);border-radius:14px;display:grid;place-items:center;min-height:150px;color:var(--mut);background:#081833;text-align:center;padding:10px}
footer{border-top:1px solid var(--line);padding:26px 20px;color:var(--mut);font-size:14px;text-align:center}footer a{color:var(--mut)}
#asst-btn{position:fixed;right:16px;bottom:16px;z-index:20;background:linear-gradient(135deg,var(--cy),#0891b2);color:#04131f;border:0;border-radius:99px;padding:12px 18px;font-weight:800;cursor:pointer;box-shadow:0 10px 30px rgba(0,0,0,.5)}
#asst{position:fixed;right:16px;bottom:70px;width:min(380px,calc(100vw - 32px));max-height:70vh;display:none;flex-direction:column;background:var(--bg2);border:1px solid var(--line);border-radius:16px;z-index:21;overflow:hidden}
#asst.open{display:flex}#asst .hd{padding:12px 14px;background:var(--card);font-weight:700}#asst .log{padding:12px;overflow:auto;flex:1;display:grid;gap:10px;align-content:start}
#asst .m{padding:10px 12px;border-radius:12px;background:var(--card);font-size:14px}#asst .u{background:#0e3a5f;justify-self:end}#asst form{display:flex;gap:6px;padding:10px;border-top:1px solid var(--line)}
@media(max-width:820px){.hero{grid-template-columns:1fr}}
@media(prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}.tilt{transform:none!important}}
"""

JS = r"""
(function(){
var rb=document.getElementById('ribbon-x');if(rb)rb.addEventListener('click',function(){var r=document.getElementById('ribbon');if(r)r.remove();try{sessionStorage.setItem('rb','1')}catch(e){}});
try{if(sessionStorage.getItem('rb')){var r=document.getElementById('ribbon');if(r)r.remove()}}catch(e){}
var t=document.querySelector('.tilt');if(t&&!matchMedia('(prefers-reduced-motion:reduce)').matches){var s=t.parentNode;
s.addEventListener('mousemove',function(e){var b=s.getBoundingClientRect(),x=(e.clientX-b.left)/b.width-.5,y=(e.clientY-b.top)/b.height-.5;t.style.transform='rotateY('+(x*14)+'deg) rotateX('+(-y*14)+'deg)'});
s.addEventListener('mouseleave',function(){t.style.transform=''})}
var f=document.getElementById('kbq');if(f){var items=[].slice.call(document.querySelectorAll('[data-kb]')),c=document.getElementById('kbc');
function run(){var q=f.value.toLowerCase().trim(),n=0;items.forEach(function(d){var ok=!q||d.getAttribute('data-kb').indexOf(q)>-1;d.style.display=ok?'':'none';if(ok)n++});c.textContent=n+' of '+items.length+' answers'}
f.addEventListener('input',run);run()}
})();
"""

ASSISTANT = r"""
/* Search-based help assistant. Finds the closest published answer; it does not generate text and stores nothing. */
(function(){
var WA=window.__WA||'',KB=[];
var STOP='a an the and or of to in on for with is are was be it this that what how why when where do does can i you my me we our about from at as by not no if then so'.split(' ');
function tok(s){return (s.toLowerCase().match(/[a-z0-9_]+/g)||[]).filter(function(w){return STOP.indexOf(w)<0&&w.length>1})}
var btn=document.createElement('button');btn.id='asst-btn';btn.type='button';btn.textContent='Ask the LMS assistant';btn.setAttribute('aria-expanded','false');
var box=document.createElement('div');box.id='asst';box.setAttribute('role','dialog');box.setAttribute('aria-label','LMS help assistant');
var hd=document.createElement('div');hd.className='hd';hd.textContent='LMS assistant (answers from published pages)';
var log=document.createElement('div');log.className='log';log.setAttribute('aria-live','polite');
var form=document.createElement('form');var inp=document.createElement('input');inp.type='text';inp.placeholder='Ask about access, simulators, AEP...';inp.setAttribute('aria-label','Your question');
var go=document.createElement('button');go.className='btn pri';go.type='submit';go.textContent='Ask';form.appendChild(inp);form.appendChild(go);
box.appendChild(hd);box.appendChild(log);box.appendChild(form);document.body.appendChild(btn);document.body.appendChild(box);
function add(cls,node){var d=document.createElement('div');d.className='m '+cls;d.appendChild(node);log.appendChild(d);log.scrollTop=log.scrollHeight}
function txt(s){return document.createTextNode(s)}
function link(h,t){var a=document.createElement('a');a.href=h;a.textContent=t;a.rel='noopener';return a}
add('',txt('Hi. I answer from the pages and knowledge base on this site. I am a search tool, not a person, and I can be wrong. Check Adobe documentation for product details.'));
fetch((window.__ROOT||'')+'assets/kb.json').then(function(r){return r.json()}).then(function(j){KB=j}).catch(function(){});
btn.addEventListener('click',function(){var o=box.classList.toggle('open');btn.setAttribute('aria-expanded',o);if(o)inp.focus()});
form.addEventListener('submit',function(e){e.preventDefault();var q=inp.value.trim();if(!q)return;inp.value='';
var u=document.createDocumentFragment();u.appendChild(txt(q));add('u',u);
var qt=tok(q),sc=KB.map(function(k){var t=tok(k.q+' '+k.a+' '+k.t),n=0;qt.forEach(function(w){if(t.indexOf(w)>-1)n++;if(k.q.toLowerCase().indexOf(w)>-1)n+=1});return {k:k,n:n}}).filter(function(x){return x.n>=2}).sort(function(a,b){return b.n-a.n}).slice(0,2);
var f=document.createDocumentFragment();
if(!sc.length){f.appendChild(txt('I could not find a close answer. '));f.appendChild(link(WA+'?text='+encodeURIComponent('Hi, I need help: '+q),'Ask the team on WhatsApp'))}
else sc.forEach(function(x,i){var p=document.createElement('p');var b=document.createElement('strong');b.textContent=x.k.q;p.appendChild(b);p.appendChild(document.createElement('br'));p.appendChild(txt(x.k.a+' '));p.appendChild(link(x.k.u,'Open'));f.appendChild(p)});
add('',f)})
})();
"""

PLACEHOLDER = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 450"><rect width="800" height="450" fill="#081833"/><rect x="6" y="6" width="788" height="438" fill="none" stroke="#1e3a6e" stroke-width="3" stroke-dasharray="14 10"/><text x="400" y="210" text-anchor="middle" fill="#9db4d8" font-family="Arial" font-size="30">{t}</text><text x="400" y="255" text-anchor="middle" fill="#6b86b3" font-family="Arial" font-size="20">Replace this file in assets/images/</text></svg>"""

PAGES = [
    ("index.html", "Home"), ("student-login.html", "Student login"), ("simulators.html", "Simulators"),
    ("knowledge-base.html", "Knowledge base"), ("community.html", "Community"), ("admin-login.html", "Admin"),
]


def nav(cur):
    return "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{E(t)}</a>' for h, t in PAGES)


def page(fn, title, desc, body, noindex=False):
    rb_t, rb_h = C["ribbon_link"]
    canon = f'<link rel="canonical" href="{C["base_url"]}/{fn}">' if C["base_url"] else ""
    robots = '<meta name="robots" content="noindex,nofollow">' if noindex else ""
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}">{canon}{robots}
<meta name="theme-color" content="#06122a"><link rel="icon" href="assets/favicon-64.png">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="assets/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="assets/site.css"></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="ribbon" id="ribbon" role="status">{E(C["ribbon"])} <a href="{rb_h}">{E(rb_t)}</a><button id="ribbon-x" type="button" aria-label="Dismiss notice">&times;</button></div>
<header class="top"><a class="brand" href="index.html"><img src="assets/logo-mark.png" width="40" height="40" alt=""><span>{E(C["short"])}<small>{E(C["brand"])}</small></span></a>
<nav class="main" aria-label="Main">{nav(fn)}</nav></header>
<main id="main">{body}</main>
<footer><p>{E(C["brand"])} LMS. Operated by PAVAN BABU GANDLA (legal name), trading as Infiante360 Business Consulting &amp; Tech Academy. Email: <a href="mailto:infinate360businessconsulting@gmail.com">infinate360businessconsulting@gmail.com</a>. Phone: <a href="tel:+918296893895">+91 82968 93895</a>. Independent of Adobe; Adobe product names are trademarks of Adobe. No job, salary or certification outcome is guaranteed.</p>
<p><a href="{C["main_site"]}">Main website</a> &middot; <a href="{C["main_site"]}privacy-policy.html">Privacy policy</a> &middot; <a href="{C["youtube"]}">YouTube</a> &middot; <a href="{WA}">WhatsApp</a></p></footer>
<script>window.__WA={json.dumps(WA)};</script><script src="assets/site.js" defer></script><script src="assets/assistant.js" defer></script></body></html>"""


def home():
    cards = "".join(f'<div class="card"><span class="pill">{E(t)}</span><h3>{E(q)}</h3><p>{E(a[:130])}...</p><a href="knowledge-base.html#{i}">Read the answer</a></div>' for i, t, q, a, _ in KB[:3])
    steps = "".join(f"<li><strong>{E(a)}.</strong> {E(b)}</li>" for a, b in STEPS)
    return f"""<section class="hero"><div><span class="kick">Learning suite</span><h1>Learn, practise and get help in one place</h1>
<p class="lead">Live classes, recordings, test series and hands-on simulators for Adobe Experience Platform, Real-Time CDP, Journey Optimizer, Customer Journey Analytics and Agentic AI.</p>
<p><a class="btn pri" href="student-login.html">Student login</a> <a class="btn cy" href="simulators.html">Open simulators</a> <a class="btn" href="community.html">Community</a></p></div>
<div class="scene"><div class="tilt"><img src="assets/logo-banner.png" alt="Infiante360 Consulting and Academy logo"><span class="chip">AEP</span><span class="chip">RTCDP</span><span class="chip">AJO</span><span class="chip">CJA</span><span class="chip">Agentic AI</span></div></div></section>
<h2>How access works</h2><ol class="steps">{steps}</ol>
<h2>Who goes where</h2><div class="grid">
<div class="card"><h3>Students</h3><p>Log in to the learning platform with your activation code, then use simulators and the knowledge base.</p><a class="btn pri" href="student-login.html">Student login</a></div>
<div class="card"><h3>Trainers and staff</h3><p>Admin access (activation codes, courses, users, test reports) is on the platform and is limited to authorised staff.</p><a class="btn" href="admin-login.html">Admin access</a></div>
<div class="card"><h3>Community</h3><p>Ask trainers questions, share fixes and follow answered questions.</p><a class="btn" href="community.html">Open community</a></div></div>
<h2>From the knowledge base</h2><div class="grid">{cards}</div><p><a href="knowledge-base.html">All {len(KB)} answers</a></p>
<h2>Images (placeholders)</h2><div class="grid"><div class="ph"><img src="assets/images/hero.svg" alt="Placeholder: learning hero image" width="400"></div><div class="ph"><img src="assets/images/classroom.svg" alt="Placeholder: live classroom image" width="400"></div><div class="ph"><img src="assets/images/trainer.svg" alt="Placeholder: trainer photo" width="400"></div></div>"""


def student():
    return f"""<h1>Student login</h1><p class="lead">The learning platform holds your live classes, recorded courses and test series. Access is switched on with an activation code from us.</p>
<p><a class="btn pri" href="{C["platform_url"]}" rel="noopener">Log in to the learning platform</a></p>
<h2>First time here</h2><ol class="steps">{"".join(f"<li><strong>{E(a)}.</strong> {E(b)}</li>" for a, b in STEPS)}</ol>
<h2>Need a code or help?</h2><p>Message us with the email you enrolled with and your program or batch. Never send passwords or payment details.</p>
<p><a class="btn cy" href="{wa("Hi, I need an activation code or login help. Program/batch: ")}">WhatsApp us</a></p>
<p class="note">Single sign-on (Google or Microsoft) and WhatsApp notifications are planned and not live yet. Until then, sign in on the platform.</p>"""


def admin():
    return f"""<h1>Admin access</h1><p class="lead">For authorised Infiante360 staff and trainers only.</p>
<div class="card"><h3>Admin panel</h3><p>Activation codes, courses and packages, test reports and user management are managed on the learning platform. Sign in there with your staff account.</p><a class="btn pri" href="{C["platform_url"]}" rel="noopener">Go to the platform</a></div>
<p class="note warn">This page does not log anyone in and holds no credentials. Never share admin accounts. Staff roles (admin, trainer, moderator) are set on the platform.</p>
<h2>What admins can do</h2><ul><li>Issue and revoke activation codes by plan or batch</li><li>Publish courses, recordings and test series</li><li>Approve or remove community posts (see the community page)</li><li>Review test reports and learner activity</li></ul>"""


def sims():
    cards = "".join(f'<div class="card"><span class="pill">Simulator</span><h3>{E(n)}</h3><p>{E(d)}</p><a class="btn cy" href="{E(u)}" rel="noopener" target="_blank">Open</a></div>' for n, u, d in SIMULATORS)
    return f"""<h1>Simulators</h1><p class="lead">Practice environments that replicate enterprise scenarios, used in exercises, architecture design, journey orchestration and Agentic AI use cases.</p>
<div class="grid">{cards}</div>
<p class="note warn">Some simulator addresses use plain http. Open them only on a network you trust; we plan to move them to https.</p>"""


def kb():
    topics = sorted({t for _, t, *_ in KB})
    items = ""
    for i, t, q, a, refs in KB:
        r = "".join(f'<li><a href="{E(u)}" rel="noopener" target="_blank">{E(l)}</a></li>' for l, u in refs)
        items += f'<details id="{i}" data-kb="{E((q + " " + a + " " + t).lower())}"><summary>{E(q)} <span class="pill">{E(t)}</span></summary><p>{E(a)}</p>{"<p>Official docs:</p><ul>" + r + "</ul>" if r else ""}</details>'
    return f"""<h1>Knowledge base</h1><p class="lead">Short answers to questions learners ask most, written from trainer replies. Always confirm product behaviour in the current Adobe documentation.</p>
<label for="kbq">Search answers</label><input id="kbq" type="search" placeholder="e.g. hashed email, profile, consent"><p id="kbc" aria-live="polite"></p>{items}
<p>Topics: {", ".join(E(t) for t in topics)}.</p>"""


def community():
    return f"""<h1>Community</h1><p class="lead">A place for learners and trainers to ask questions and share fixes.</p>
<div class="grid"><div class="card"><h3>Ask a question now</h3><p>Post in the WhatsApp community. Include the step you are on, what you expected and what happened, plus a screenshot. Do not share passwords, sandbox logins or customer data.</p><a class="btn pri" href="{wa("Hi, I have a question for the trainers: ")}">Ask on WhatsApp</a></div>
<div class="card"><h3>Trainers</h3><p>Trainers answer in the community, and good answers are added to the <a href="knowledge-base.html">knowledge base</a> without learner names.</p></div>
<div class="card"><h3>Admin moderation</h3><p>Admins control who has access, can remove posts and can add trainers.</p></div></div>
<h2>Community rules</h2><ul><li>Be respectful; no ads or spam.</li><li>No credentials, sandbox access details or personal data.</li><li>Do not share paid course material.</li><li>No promises of jobs, salaries or certification results.</li></ul>
<p class="note">Threaded questions with trainer and admin roles, inside this site, need a server and database. That build is planned and not live yet.</p>"""


def build():
    os.makedirs(f"{ROOT}/assets/images", exist_ok=True)
    open(f"{ROOT}/assets/site.css", "w").write(CSS)
    open(f"{ROOT}/assets/site.js", "w").write(JS)
    open(f"{ROOT}/assets/assistant.js", "w").write(ASSISTANT)
    kbj = [{"t": t, "q": q, "a": a, "u": f"knowledge-base.html#{i}"} for i, t, q, a, _ in KB]
    kbj += [{"t": "simulators", "q": n, "a": d, "u": "simulators.html"} for n, _, d in SIMULATORS]
    kbj += [{"t": "access login activation code", "q": "How do I log in and activate my access?", "a": " ".join(a + " " + b for a, b in STEPS), "u": "student-login.html"}]
    open(f"{ROOT}/assets/kb.json", "w").write(json.dumps(kbj))
    for n, t in (("hero", "Hero image"), ("classroom", "Live classroom image"), ("trainer", "Trainer photo")):
        open(f"{ROOT}/assets/images/{n}.svg", "w").write(PLACEHOLDER.format(t=t))
    out = {
        "index.html": ("Infiante360 LMS: classes, simulators and community", "Learning suite for Adobe Experience Platform, RTCDP, AJO, CJA and Agentic AI: login, simulators, knowledge base and community.", home()),
        "student-login.html": ("Student login | Infiante360 LMS", "Log in to the Infiante360 learning platform and activate your access with a code.", student()),
        "admin-login.html": ("Admin access | Infiante360 LMS", "Admin access for authorised Infiante360 staff and trainers.", admin()),
        "simulators.html": ("Simulators | Infiante360 LMS", "Hands-on AEP, banking, airline, hospitality, insurance and telecom simulation environments.", sims()),
        "knowledge-base.html": ("Knowledge base | Infiante360 LMS", "Searchable answers on AEP ingestion, identity, schemas, governance, AJO and Web SDK.", kb()),
        "community.html": ("Community | Infiante360 LMS", "Ask trainers questions and follow answered questions in the Infiante360 community.", community()),
    }
    for fn, (t, d, b) in out.items():
        assert len(t) <= 65 and len(d) <= 160, (fn, len(t), len(d))
        open(f"{ROOT}/{fn}", "w").write(page(fn, t, d, b, noindex=(fn == "admin-login.html")))
    open(f"{ROOT}/404.html", "w").write(page("404.html", "Page not found | Infiante360 LMS", "This page does not exist.", '<h1>Page not found</h1><p><a href="index.html">Back to the LMS home</a></p>', True))
    base = C["base_url"]
    urls = [f for f in out if f != "admin-login.html"]
    (open(f"{ROOT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{base}/{u}</loc></url>" for u in urls) + "</urlset>") if base else None)
    open(f"{ROOT}/robots.txt", "w").write("User-agent: *\nAllow: /\nDisallow: /admin-login.html\n" + (f"Sitemap: {base}/sitemap.xml\n" if base else ""))
    print("built", len(out) + 1, "pages")


if __name__ == "__main__":
    build()
