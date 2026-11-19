/* Toolnex — Haituo Faux Botanicals : site interactions */
(function () {
  "use strict";

  /* ---------- Mobile navigation ---------- */
  var toggle = document.getElementById("navToggle");
  var nav = document.getElementById("primaryNav");

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Open menu");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
    document.addEventListener("click", function (e) {
      if (!nav.contains(e.target) && !toggle.contains(e.target)) closeNav();
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 900) closeNav();
    });
  }

  /* ---------- Footer year ---------- */
  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  /* ---------- Scroll reveal ---------- */
  var revealTargets = document.querySelectorAll(
    ".cat-card, .product-card, .app-card, .cert-card, .spec-card, .steps li, .factory-photo, .oem-panel, .rfq-panel, .rfq-form"
  );
  if ("IntersectionObserver" in window && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    revealTargets.forEach(function (el) { el.classList.add("reveal"); });
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    revealTargets.forEach(function (el) { revealObserver.observe(el); });
  }

  /* Show every reveal element inside a section immediately.
     This guarantees a hash-linked section is never blank on arrival. */
  function showRevealsIn(scope) {
    if (!scope) return;
    var els = scope.querySelectorAll ? scope.querySelectorAll(".reveal:not(.is-visible)") : [];
    Array.prototype.forEach.call(els, function (el) { el.classList.add("is-visible"); });
    if (scope.classList && scope.classList.contains("reveal")) scope.classList.add("is-visible");
  }

  /* Safety net: anything currently in the viewport must never stay invisible,
     even if IntersectionObserver is unavailable or fails to fire. */
  function revealFailsafe() {
    document.querySelectorAll(".reveal:not(.is-visible)").forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) el.classList.add("is-visible");
    });
  }

  /* ---------- Active nav link ---------- */
  var sectionIds = ["products", "grass-walls", "factory", "customization", "catalog", "about", "contact"];
  var sections = sectionIds
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);
  var navLinks = document.querySelectorAll(".primary-nav a");

  function setActive(hash) {
    navLinks.forEach(function (link) {
      link.classList.toggle("is-active", link.getAttribute("href") === hash);
    });
  }

  if ("IntersectionObserver" in window && sections.length) {
    var navObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        setActive("#" + entry.target.id);
      });
    }, { rootMargin: "-35% 0px -55% 0px" });
    sections.forEach(function (s) { navObserver.observe(s); });
  }

  /* ---------- Precise in-page anchor navigation ----------
     Global CSS smooth scrolling is intentionally disabled: when a URL contains
     #hash, the browser starts a smooth scroll before webfonts / lazy images
     finish, and the final position drifts. We scroll only after layout settles,
     and we reveal the destination content before scrolling. */
  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function hashTarget(hash) {
    if (!hash || hash === "#" || hash.length < 2) return null;
    try { return document.querySelector(hash); } catch (e) { return null; }
  }

  function goToHash(hash, behavior) {
    var el = hashTarget(hash);
    if (!el) return false;

    showRevealsIn(el);
    if (hash === "#top" || hash === "#main") {
      window.scrollTo({ top: 0, behavior: behavior === "smooth" ? "smooth" : "auto" });
      return true;
    }
    try {
      el.scrollIntoView({ behavior: behavior, block: "start" });
    } catch (e) {
      var y = el.getBoundingClientRect().top + window.pageYOffset - 40;
      window.scrollTo(0, y);
    }
    return true;
  }

  function settleHash() {
    if (!location.hash) return;
    /* A hash URL is a direct arrival, not a scroll journey: reveal the whole
       page at once so no section can ever appear blank on landing. */
    showRevealsIn(document.body);
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        goToHash(location.hash, "auto");
        setActive(location.hash);
      });
    });
  }

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var hash = a.getAttribute("href");
    if (!hash || hash === "#") return;
    if (!hashTarget(hash)) return;
    e.preventDefault();
    goToHash(hash, prefersReduced ? "auto" : "smooth");
    try { history.pushState(null, "", hash); } catch (err) { /* file:// or restricted */ }
    setActive(hash);
    closeNav();
  });

  window.addEventListener("load", function () {
    settleHash();
    /* Re-anchor once webfonts and hero imagery have settled the layout. */
    setTimeout(function () { if (location.hash) goToHash(location.hash, "auto"); }, 400);
    setTimeout(revealFailsafe, 1500);
  });
  window.addEventListener("hashchange", function () {
    settleHash();
    if (location.hash) showRevealsIn(hashTarget(location.hash));
  });
  window.addEventListener("pageshow", settleHash);

  /* ---------- Retire legacy Service Worker ----------
     The old game site shipped sw.js which fetched scripts from a third-party
     domain. The B2B site does not use a Service Worker; remove any stale
     registration so it cannot interfere with navigation or caching. */
  if ("serviceWorker" in navigator && navigator.serviceWorker.getRegistrations) {
    navigator.serviceWorker.getRegistrations().then(function (regs) {
      regs.forEach(function (reg) { reg.unregister(); });
    }).catch(function () { /* ignore */ });
  }

  /* ---------- RFQ form : mailto fallback ---------- */
  var form = document.getElementById("rfqForm");
  var status = document.getElementById("formStatus");
  var TO = "qiangda68@outlook.com";

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var name = (data.get("Full name") || "").trim();
      var email = (data.get("Email") || "").trim();
      var company = (data.get("Company") || "").trim();
      var market = (data.get("Country / Market") || "").trim();
      var message = (data.get("Message") || "").trim();

      var subject = "Wholesale inquiry from " + (company || name) + " — Toolnex";
      var body = [
        "Full name: " + name,
        "Email: " + email,
        "Company: " + company,
        "Country / Market: " + market,
        "",
        "Message:",
        message,
        "",
        "Sent from toolnex.xyz"
      ].join("\n");

      var href = "mailto:" + TO + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
      window.location.href = href;

      if (status) {
        status.textContent = "Your email app is opening with the inquiry ready. If nothing happens, email " + TO + " directly.";
      }
    });
  }
})();
