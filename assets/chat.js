/* Website assistant widget. Loaded lazily by site.js. No cookies; the conversation is kept in sessionStorage only. */
(function () {
  if (window.__i360chat) return;
  window.__i360chat = true;
  var script = document.currentScript || document.querySelector('script[src*="chat.js"]');
  var root = (script && script.src ? script.src.replace(/assets\/chat\.js.*$/, "") : "/");
  var WA = "https://wa.me/918296893895";
  var STOP = "a an the and or of to in on for with is are was were be been it this that what how why when where who which do does can i you your we our my me about from at as by not no yes please tell give".split(" ");
  var SYN = { cost: ["fee", "fees", "price", "pricing"], price: ["fee", "fees", "cost"], fees: ["fee", "price", "cost"], fee: ["fees", "price", "cost"], jobs: ["job", "placement"], job: ["jobs", "placement"], placement: ["job", "jobs"], course: ["program", "training"], courses: ["program", "training"], program: ["course", "training"], brochures: ["brochure"], download: ["brochure"] };
  var history = [];
  var index = null;
  var open = false;

  function store(k, v) { try { if (v === undefined) return sessionStorage.getItem(k); sessionStorage.setItem(k, v); } catch (e) { return null; } }
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text) n.textContent = text; return n; }

  var btn = el("button", "chat-fab");
  btn.type = "button";
  btn.setAttribute("aria-label", "Ask our assistant");
  btn.setAttribute("aria-expanded", "false");
  btn.innerHTML = '<svg viewBox="0 0 24 24" width="26" height="26" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z"/></svg><span>Ask us</span>';

  var panel = el("section", "chat-panel");
  panel.setAttribute("role", "dialog");
  panel.setAttribute("aria-label", "Infinite360 assistant");
  panel.hidden = true;
  var head = el("div", "chat-head");
  head.appendChild(el("strong", "", "Infinite360 assistant"));
  var close = el("button", "chat-close", "×");
  close.type = "button";
  close.setAttribute("aria-label", "Close assistant");
  var callBtn = el("button", "chat-callbtn", "Call me"); callBtn.type = "button"; callBtn.setAttribute("aria-label", "Request a call back");
  callBtn.addEventListener("click", function () { chips.hidden = true; add("user", "Call me back"); callbackForm(); });
  head.appendChild(callBtn);
  head.appendChild(close);
  var log = el("div", "chat-log");
  log.setAttribute("role", "log");
  log.setAttribute("aria-live", "polite");
  var chips = el("div", "chat-chips");
  var form = el("form", "chat-form");
  var input = el("input");
  input.type = "text"; input.maxLength = 500; input.placeholder = "Ask about courses, fees, AEP, careers…";
  input.setAttribute("aria-label", "Your question"); input.autocomplete = "off";
  var send = el("button", "chat-send", "Send");
  send.type = "submit";
  form.appendChild(input); form.appendChild(send);
  var note = el("p", "chat-note", "AI-assisted answers can be wrong. Do not share passwords or payment details. Training does not guarantee jobs, salary or certification.");
  panel.appendChild(head); panel.appendChild(log); panel.appendChild(chips); panel.appendChild(form); panel.appendChild(note);

  function add(role, text, sources) {
    var m = el("div", "chat-msg chat-" + role);
    m.appendChild(el("p", "", text));
    if (sources && sources.length) {
      var ul = el("ul", "chat-src");
      sources.forEach(function (s) {
        var li = document.createElement("li"), a = document.createElement("a");
        a.href = s.url; a.textContent = s.title;
        if (/^https?:/.test(s.url) && s.url.indexOf(location.host) < 0) { a.target = "_blank"; a.rel = "noopener"; }
        li.appendChild(a); ul.appendChild(li);
      });
      m.appendChild(ul);
    }
    log.appendChild(m);
    log.scrollTop = log.scrollHeight;
    return m;
  }

  function stem(w) { return w.length > 4 && w.slice(-1) === "s" && w.slice(-2) !== "ss" ? w.slice(0, -1) : w; }
  function tok(s) { return (String(s || "").toLowerCase().match(/[a-z0-9+#.]+/g) || []).filter(function (w) { return w.length > 1 && STOP.indexOf(w) < 0; }).map(stem); }
  function localAnswer(q) {
    return fetch(root + "assets/chat-index.json").then(function (r) { return r.json(); }).then(function (idx) {
      var base = tok(q), qt = base.slice(), best = [], df = {};
      base.forEach(function (w) { (SYN[w] || []).forEach(function (x) { if (qt.indexOf(x) < 0) qt.push(x); }); });
      var docs = idx.map(function (d) { return { d: d, T: tok(d.t), K: tok(d.k), A: tok(d.a), X: tok(d.x) }; });
      qt.forEach(function (w) { df[w] = docs.filter(function (o) { return o.T.indexOf(w) >= 0 || o.K.indexOf(w) >= 0 || o.A.indexOf(w) >= 0 || o.X.indexOf(w) >= 0; }).length; });
      docs.forEach(function (o) {
        var s = 0, tm = 0;
        qt.forEach(function (w) { var i = Math.log(1 + docs.length / (1 + df[w])); if (o.T.indexOf(w) >= 0) { s += 4 * i; tm++; } if (o.K.indexOf(w) >= 0) s += 3 * i; if (o.A.indexOf(w) >= 0) s += 2 * i; if (o.X.indexOf(w) >= 0) s += i; });
        if (o.d.f) s *= 1 + 0.5 * (tm / Math.max(1, base.length));
        if (s > 0) best.push({ d: o.d, s: s });
      });
      best.sort(function (a, b) { return b.s - a.s; });
      if (!best.length || best[0].s < 4) return { reply: "I could not find that on the site. For a precise answer, message us on WhatsApp (+91 82968 93895), type 'call me' for a call back, or request a brochure.", sources: [{ title: "WhatsApp +91 82968 93895", url: WA }, { title: "Download brochures", url: root + "brochures.html" }] };
      return { reply: best[0].d.a, sources: best.slice(0, 3).map(function (o) { return { title: o.d.t, url: root + o.d.u }; }) };
    });
  }

  var MAIL = "infinate360businessconsulting@gmail.com";
  function callbackForm() {
    var m = el("div", "chat-msg chat-bot");
    m.appendChild(el("p", "", "Happy to call you. Leave your name and phone number, or tap to call us now."));
    var f = el("form", "chat-cb");
    var n = el("input"); n.type = "text"; n.required = true; n.placeholder = "Your name"; n.autocomplete = "name"; n.setAttribute("aria-label", "Your name");
    var ph = el("input"); ph.type = "tel"; ph.required = true; ph.placeholder = "Phone / WhatsApp (with country code)"; ph.autocomplete = "tel"; ph.pattern = "[+0-9 ()-]{7,20}"; ph.setAttribute("aria-label", "Phone number");
    var c = el("label", "chat-cb-consent"); var cb = document.createElement("input"); cb.type = "checkbox"; cb.required = true;
    c.appendChild(cb); c.appendChild(document.createTextNode(" I agree to be contacted about my enquiry."));
    var go = el("button", "chat-send", "Request a call"); go.type = "submit";
    var tel = el("a", "chat-tel", "Call +91 82968 93895"); tel.href = "tel:+918296893895";
    f.appendChild(n); f.appendChild(ph); f.appendChild(c); f.appendChild(go); f.appendChild(tel);
    f.addEventListener("submit", function (e) {
      e.preventDefault();
      var lastQ = ""; history.forEach(function (h) { if (h.role === "user") lastQ = h.content; });
      var data = { name: n.value.slice(0, 120), phone: ph.value.slice(0, 30), email: "", message: "Call-back request from website chat. Last question: " + lastQ.slice(0, 300), source_page: location.href, form_type: "chat_callback" };
      go.disabled = true; go.textContent = "Sending\u2026";
      var mail = fetch("https://formsubmit.co/ajax/" + MAIL, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify({ name: data.name, phone: data.phone, message: data.message, page: data.source_page, _subject: "Chat call-back request", _captcha: "false" }) }).then(function (r) { return r.ok; }).catch(function () { return false; });
      try { navigator.sendBeacon && navigator.sendBeacon(root + "api/lead", new Blob([JSON.stringify(Object.assign({ email: "callback@invalid.local" }, data))], { type: "application/json" })); } catch (x) { /* ignore */ }
      mail.then(function (ok) {
        f.remove();
        m.appendChild(el("p", "", ok ? "Thank you, " + data.name + ". We have your number and will call you back. You can also message us on WhatsApp." : "We could not send that. Please call or WhatsApp +91 82968 93895 directly."));
        log.scrollTop = log.scrollHeight;
      });
    });
    m.appendChild(f);
    log.appendChild(m);
    log.scrollTop = log.scrollHeight;
    n.focus();
  }

  function ask(q) {
    q = q.trim();
    if (!q) return;
    if (/\b(call me|call back|callback|ring me|phone me|talk to (a |some)?(one|human|person|someone)|speak to (a |some)?(one|human|person|someone)|contact me|counsel+or)\b/i.test(q)) {
      add("user", q); callbackForm(); return;
    }
    add("user", q);
    history.push({ role: "user", content: q });
    var wait = add("bot", "Thinking…");
    var done = function (res) {
      wait.remove();
      add("bot", res.reply, res.sources);
      history.push({ role: "assistant", content: res.reply });
      store("i360chat", JSON.stringify(history.slice(-12)));
    };
    fetch(root + "api/chat", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ messages: history.slice(-6) }) })
      .then(function (r) { if (!r.ok) throw new Error("x"); return r.json(); })
      .then(function (j) { if (!j || !j.reply) throw new Error("x"); done(j); })
      .catch(function () { localAnswer(q).then(done).catch(function () { done({ reply: "Sorry, I could not answer right now. Please message us on WhatsApp: +91 82968 93895.", sources: [{ title: "Open WhatsApp", url: WA }] }); }); });
  }

  ["Call me back", "What does the Career Accelerator cost?", "Which course should I start with?", "Do you guarantee a job?", "How do I get the brochure?"].forEach(function (t) {
    var c = el("button", "chat-chip", t); c.type = "button";
    c.addEventListener("click", function () { chips.hidden = true; if (t === "Call me back") { add("user", t); callbackForm(); } else ask(t); });
    chips.appendChild(c);
  });

  function toggle(v) {
    open = v === undefined ? !open : v;
    panel.hidden = !open;
    btn.setAttribute("aria-expanded", String(open));
    if (open) {
      if (!log.children.length) add("bot", "Hi! I can answer questions about Infinite360 Tech Academy and Adobe MarTech: programs, fees, timings, AEP, careers and corporate training.");
      setTimeout(function () { input.focus(); }, 30);
    } else btn.focus();
  }
  btn.addEventListener("click", function () { toggle(); });
  close.addEventListener("click", function () { toggle(false); });
  panel.addEventListener("keydown", function (e) { if (e.key === "Escape") toggle(false); });
  form.addEventListener("submit", function (e) { e.preventDefault(); var v = input.value; input.value = ""; chips.hidden = true; ask(v); });

  try { var saved = JSON.parse(store("i360chat") || "[]"); if (saved.length) { history = saved; add("bot", "Welcome back. Ask me anything."); chips.hidden = true; } } catch (e) { /* ignore */ }

  document.body.appendChild(btn);
  document.body.appendChild(panel);
})();
