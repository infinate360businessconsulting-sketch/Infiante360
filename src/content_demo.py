"""3-day paid demo bootcamp landing page. Data-driven from content/demo-bootcamp.json (dates, fee, payment link).
Payment is taken on the owner's Cashfree form; this site takes no payment."""
import json, os, datetime, html
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = json.load(open(os.path.join(_ROOT, "content", "demo-bootcamp.json"), encoding="utf-8"))
e = html.escape
PATH = "lp/martech-demo-bootcamp.html"
FEE = D["fee_label"]; PAY = D["payment_url"]
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def d(day):
    return datetime.date.fromisoformat(day["date"])


def fmt(day):
    return d(day).strftime("%A %-d %B %Y")


first, last = d(D["days"][0]), d(D["days"][-1])
span = f'{first.day}–{last.day} {last.strftime("%B")}' if first.month == last.month else f'{first.strftime("%-d %b")} – {last.strftime("%-d %b")}'
days_json = e(json.dumps([{"n": x["n"], "start": f'{x["date"]}T{D["start_hour"]}:00+05:30', "end": f'{x["date"]}T{D["end_hour"]}:00+05:30'} for x in D["days"]]))
pay_btn = f'<a class="btn btn-primary" id="demo-pay" href="{e(PAY)}" rel="noopener" target="_blank">Reserve your seat for {FEE} &rarr;</a>'

SCRIPT = """<script>(function(){try{var box=document.getElementById("demo-status");var days=JSON.parse(box.getAttribute("data-days"));var now=Date.now();
var s=days.map(function(x){return[new Date(x.start).getTime(),new Date(x.end).getTime()]});var pay=document.getElementById("demo-pay");var msg="";
if(now<s[0][0]){var k=Math.ceil((s[0][0]-now)/86400000);msg="Starts in "+k+(k===1?" day":" days")+". Seats are confirmed after payment."}
else if(now<=s[s.length-1][1]){var cur=-1;for(var i=0;i<s.length;i++){if(now<=s[i][1]){cur=i;break}}
msg=(now>=s[cur][0]&&now<=s[cur][1])?"Day "+(cur+1)+" is live now.":"The demo is in progress. Next session: Day "+(cur+1)+". You can still register for the remaining days."}
else{msg="This demo has ended. Send the enquiry form below to join the next run.";if(pay){pay.removeAttribute("href");pay.textContent="Registration closed";pay.setAttribute("aria-disabled","true");pay.style.opacity=".55"}}
box.textContent=msg}catch(x){}})();</script>"""

def ics():
    """Public calendar file with the three sessions. Joining link is included only when join_url is set in the config."""
    join = D.get("join_url", "").strip()
    desc = "Infinite360 live demo. " + (f"Join: {join}" if join else "Joining details are shared by email or WhatsApp after registration.") + " Questions: +91 82968 93895."
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Infinite360//Demo Bootcamp//EN", "CALSCALE:GREGORIAN", "METHOD:PUBLISH", "X-WR-CALNAME:Adobe MarTech 3-Day Demo Bootcamp"]
    for x in D["days"]:
        st = datetime.datetime.fromisoformat(f'{x["date"]}T{D["start_hour"]}:00+05:30').astimezone(datetime.timezone.utc)
        en = datetime.datetime.fromisoformat(f'{x["date"]}T{D["end_hour"]}:00+05:30').astimezone(datetime.timezone.utc)
        z = lambda t: t.strftime("%Y%m%dT%H%M%SZ")
        out += ["BEGIN:VEVENT", f'UID:demo-bootcamp-day{x["n"]}-{x["date"]}@infiante360techacademy.com', "DTSTAMP:20261102T000000Z", f"DTSTART:{z(st)}", f"DTEND:{z(en)}",
                f'SUMMARY:{D["name"]}: Day {x["n"]} - {x["title"]}', f"DESCRIPTION:{desc}", "LOCATION:" + (join if join else "Online (link shared after registration)"),
                "BEGIN:VALARM", "TRIGGER:-PT30M", "ACTION:DISPLAY", "DESCRIPTION:Demo starts in 30 minutes", "END:VALARM", "END:VEVENT"]
    return "\r\n".join(out + ["END:VCALENDAR", ""])


PAGES_DEMO = [dict(
    path=PATH, nav="3-day MarTech demo bootcamp",
    title=f"3-Day Adobe MarTech Demo Bootcamp: {span}, 10 PM IST, {FEE}",
    desc=f"Live 3-day Adobe MarTech demo bootcamp, {span} {last.year}, 10-11 PM IST. See AEP, journeys, CJA and Agentic AI in action. {FEE}.",
    h1="3-day Adobe MarTech demo bootcamp", kicker=f"Live online · {span} · {D['time_label']}",
    keywords=["adobe martech demo", "aep demo class", "martech bootcamp india", "adobe experience platform live demo", "agentic ai martech demo"],
    answer=(f"The Adobe MarTech demo bootcamp is a live, three-day online session on {span} {last.year}, from 10:00 to 11:00 PM IST each night. "
            f"You see Adobe Experience Platform, audiences and journeys, Customer Journey Analytics and Agentic AI demonstrated, and learn how to map your background to MarTech roles. The fee is {FEE} for the three days."),
    schema="WebPage", landing=True, interest="demo", bands=True, hero_cta=(f"Reserve your seat: {FEE}", PAY),
    sections=[
        ("Reserve your seat", f'''<div class="price-card"><div><div class="price">{FEE}<small>for the 3-day demo</small></div>
<div class="meta" style="margin-top:14px"><span>3 nights</span><span>{e(D["time_label"])}</span><span>Live online</span></div>
<p id="demo-status" role="status" aria-live="polite" class="small" style="margin-top:12px;font-weight:600" data-days="{days_json}">Seats are confirmed after payment.</p>
<p class="cta-row" style="margin-top:18px">{pay_btn} <a class="btn btn-ghost" href="#enquire-form">Ask a question first</a> <a class="btn btn-ghost" href="../assets/demo-bootcamp.ics" download>Add to calendar (.ics)</a></p>
<p class="small muted">Payment is made on a secure Cashfree form (opens in a new tab). Joining details are shared after registration.</p></div>
<ul class="checklist"><li>Three live evening sessions, one hour each</li><li>Hands-on walkthroughs in the Infinite360 practice environment</li><li>Open Q&amp;A with the instructor</li><li>A clear view of where to start in Adobe MarTech</li></ul></div>
<p class="small muted">A demo shows what the work looks like and how we teach. It is not a certification and guarantees no job, salary or certification outcome. Infinite360 is independent and not affiliated with Adobe.</p>''', "plain", "Fee and seats"),
        ("What happens each night", '<div class="grid-3">' + "".join(
            f'<div class="card"><span class="tag">Day {x["n"]} · {e(fmt(x))}</span><h3>{e(x["title"])}</h3><ul class="checklist">' + "".join(f"<li>{e(p)}</li>" for p in x["points"]) + "</ul></div>" for x in D["days"]) + "</div>", "alt", "Agenda"),
        ("Who should join", '<div class="grid-3"><div class="card"><h3>Career switchers</h3><p>Developers, data engineers, analysts and marketers curious about MarTech.</p></div><div class="card"><h3>Working practitioners</h3><p>Anyone who wants a clear mental model of AEP, journeys and CJA.</p></div><div class="card"><h3>Team leads</h3><p>Leaders deciding what skills their team needs next.</p></div></div>', "plain", "Audience"),
        ("Next step after the demo", '<p>If the demo fits, continue with the <a href="../training/">Career Accelerator (₹60,000)</a> or the self-paced <a href="../academy/programs/bronze-membership.html">Bronze Membership (₹30,000)</a>. There is no obligation to continue.</p>', "alt", "Continue"),
        ("Questions", '<div class="form-card" id="enquire-form">@@LP_FORM@@</div>' + SCRIPT, "plain", "Contact us"),
    ],
    faqs=[("When is the demo?", f"{first.strftime('%A %-d %B')} to {last.strftime('%A %-d %B %Y')}, 10:00 PM to 11:00 PM IST each night, live online."),
          ("How much does it cost?", f"{FEE} for the three-day demo, paid on the secure Cashfree registration form."),
          ("Do I need Adobe experience?", "No. It is designed for beginners and curious practitioners."),
          ("How do I get the joining link?", "After registration we share joining details by email or WhatsApp."),
          ("Is there a job or certification guarantee?", "No. The demo shows the work and how we teach; outcomes depend on your own practice.")],
    related=["academy/workshops.html"],
)]
