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
    ".cat-card, .product-card, .app-card, .cert-card, .steps li, .factory-photo, .oem-panel, .rfq-panel, .rfq-form"
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

  /* ---------- Active nav link ---------- */
  var sectionIds = ["products", "factory", "customization", "catalog", "about", "contact"];
  var sections = sectionIds
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);
  var navLinks = document.querySelectorAll(".primary-nav a");

  if ("IntersectionObserver" in window && sections.length) {
    var navObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (link) {
          link.classList.toggle("is-active", link.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-35% 0px -55% 0px" });
    sections.forEach(function (s) { navObserver.observe(s); });
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
