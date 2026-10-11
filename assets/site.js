/* Infinite360 — navigation + accessible form validation. No dependencies. */
(function () {
  "use strict";

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      toggle.setAttribute("aria-label", open ? "Open menu" : "Close menu");
      nav.classList.toggle("open", !open);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) {
        nav.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  // Forms
  var MESSAGES = {
    valueMissing: "This field is required.",
    typeMismatch: "Please enter a valid value.",
    patternMismatch: "Please check the format.",
    tooShort: "Please add a little more detail."
  };

  function errorFor(field) {
    return document.getElementById(field.id + "-error");
  }

  function validate(field) {
    var err = errorFor(field);
    if (!err) return true;
    var ok = field.checkValidity();
    var msg = "";
    if (!ok) {
      var v = field.validity;
      if (v.valueMissing) msg = field.dataset.msgRequired || MESSAGES.valueMissing;
      else if (v.typeMismatch) msg = field.type === "email" ? "Please enter a valid email address, e.g. name@company.com." : MESSAGES.typeMismatch;
      else if (v.patternMismatch) msg = field.dataset.msgPattern || MESSAGES.patternMismatch;
      else if (v.tooShort) msg = MESSAGES.tooShort;
      else msg = field.validationMessage;
    }
    field.setAttribute("aria-invalid", ok ? "false" : "true");
    err.textContent = msg;
    err.classList.toggle("show", !ok);
    return ok;
  }

  function buildSummary(form) {
    var lines = [];
    var data = new FormData(form);
    data.forEach(function (value, key) {
      if (!value || key.charAt(0) === "_" || key === "consent") return;
      lines.push(key.replace(/_/g, " ") + ": " + value);
    });
    return lines.join("\n");
  }

  Array.prototype.forEach.call(document.querySelectorAll("form.js-validate"), function (form) {
    form.setAttribute("novalidate", "");
    var fields = form.querySelectorAll("input:not([type=hidden]):not(.hp input), select, textarea");

    Array.prototype.forEach.call(fields, function (f) {
      f.addEventListener("blur", function () { if (f.value) validate(f); });
      f.addEventListener("input", function () { if (f.getAttribute("aria-invalid") === "true") validate(f); });
      f.addEventListener("change", function () { if (f.getAttribute("aria-invalid") === "true") validate(f); });
    });

    var page = form.querySelector('input[name="source_page"]');
    if (page) page.value = window.location.href;

    form.addEventListener("submit", function (e) {
      var firstBad = null;
      Array.prototype.forEach.call(fields, function (f) {
        if (!validate(f) && !firstBad) firstBad = f;
      });
      var status = form.querySelector(".form-status");
      if (firstBad) {
        e.preventDefault();
        if (status) { status.textContent = "Please fix the highlighted fields."; status.className = "form-status err"; }
        firstBad.focus();
        return;
      }
      // Attribution + webhook relay (server-side function forwards to the configured CRM/n8n webhook).
      try {
        var data = {};
        new FormData(form).forEach(function (v, k) { if (typeof v === "string") data[k] = v; });
        var attr = JSON.parse(sessionStorage.getItem("i360_attr") || "{}");
        Object.keys(attr).forEach(function (k) { if (!data[k]) data[k] = attr[k]; });
        if (navigator.sendBeacon) navigator.sendBeacon("/api/lead", new Blob([JSON.stringify(data)], { type: "application/json" }));
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push({ event: data.form_type === "testimonial" ? "review_submit" : "generate_lead", form_interest: data.interest || data.program || "" });
      } catch (err) { /* never block the form */ }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      if (status) { status.textContent = ""; status.className = "form-status"; }
    });

    var wa = form.querySelector(".js-whatsapp");
    if (wa) {
      wa.addEventListener("click", function () {
        var text = "Hello Infinite360,\n" + buildSummary(form);
        window.open("https://wa.me/918296893895?text=" + encodeURIComponent(text), "_blank", "noopener");
      });
    }
  });

  // Video facades: load the YouTube player only when the visitor presses play.
  Array.prototype.forEach.call(document.querySelectorAll(".video-facade"), function (btn) {
    btn.addEventListener("click", function () {
      var iframe = document.createElement("iframe");
      iframe.src = btn.getAttribute("data-embed") + "&autoplay=1";
      iframe.title = btn.getAttribute("aria-label").replace("Play video: ", "");
      iframe.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture";
      iframe.allowFullscreen = true;
      btn.replaceWith(iframe);
    });
  });

  // Event countdowns (start time in ISO format with offset).
  var cds = document.querySelectorAll("[data-countdown]");
  function tick() {
    Array.prototype.forEach.call(cds, function (el) {
      var diff = new Date(el.getAttribute("data-countdown")).getTime() - Date.now();
      if (isNaN(diff)) return;
      if (diff <= 0) { el.textContent = "This session has started or ended — see upcoming dates below."; return; }
      var d = Math.floor(diff / 86400000), h = Math.floor(diff % 86400000 / 3600000), m = Math.floor(diff % 3600000 / 60000);
      el.textContent = "Starts in " + (d ? d + "d " : "") + h + "h " + m + "m";
    });
  }
  if (cds.length) { tick(); setInterval(tick, 30000); }

  // Remember campaign attribution for the session (UTMs + referrer) so enquiries carry their source.
  try {
    var q = new URLSearchParams(window.location.search), attr = JSON.parse(sessionStorage.getItem("i360_attr") || "{}");
    ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content"].forEach(function (k) { if (q.get(k)) attr[k] = q.get(k).slice(0, 200); });
    if (!attr.referrer && document.referrer && document.referrer.indexOf(location.host) === -1) attr.referrer = document.referrer.slice(0, 300);
    sessionStorage.setItem("i360_attr", JSON.stringify(attr));
  } catch (err) { /* storage unavailable */ }

  // Consent banner: shown only when analytics tags are configured (gtag defined in <head>).
  if (typeof window.gtag === "function") {
    var stored = null;
    try { stored = localStorage.getItem("i360_consent"); } catch (err) { /* ignore */ }
    if (!stored) {
      var bar = document.createElement("div");
      bar.className = "consent-bar";
      bar.setAttribute("role", "region");
      bar.setAttribute("aria-label", "Cookie consent");
      bar.innerHTML = '<p>We use analytics cookies to understand which pages help visitors. They stay off unless you accept. <a href="' +
        (document.querySelector('a[href$="privacy-policy.html"]') || { getAttribute: function () { return "/privacy-policy.html"; } }).getAttribute("href") +
        '">Privacy policy</a></p><div class="cta-row"><button type="button" class="btn btn-primary" data-c="granted">Accept analytics</button><button type="button" class="btn btn-ghost" data-c="denied">Decline</button></div>';
      document.body.appendChild(bar);
      bar.addEventListener("click", function (ev) {
        var c = ev.target.getAttribute && ev.target.getAttribute("data-c");
        if (!c) return;
        try { localStorage.setItem("i360_consent", c); } catch (err) { /* ignore */ }
        window.gtag("consent", "update", { analytics_storage: c });
        bar.remove();
      });
    }
  }

  // Table filter
  Array.prototype.forEach.call(document.querySelectorAll("[data-filter-table]"), function (input) {
    var rows = document.querySelectorAll("#" + input.getAttribute("data-filter-table") + " tbody tr");
    input.addEventListener("input", function () {
      var q = input.value.toLowerCase();
      Array.prototype.forEach.call(rows, function (r) { r.hidden = q && r.textContent.toLowerCase().indexOf(q) === -1; });
    });
  });

  var y = document.getElementById("year");
  if (y) y.textContent = String(new Date().getFullYear());
})();
