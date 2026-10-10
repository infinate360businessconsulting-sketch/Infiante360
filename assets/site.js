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

  var y = document.getElementById("year");
  if (y) y.textContent = String(new Date().getFullYear());
})();
