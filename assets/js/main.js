/* ==========================================================================
   ZENTRO MOTO — Prototype interactions
   Cart is a client-side (localStorage) prototype only — a real build would
   run on Shopify's standard cart / checkout, as noted in the site brief.
   ========================================================================== */
(function () {
  "use strict";

  var CART_KEY = "zentro_cart_v1";

  /* ------------------------------ Cart storage ------------------------------ */
  function readCart() {
    try {
      var raw = window.localStorage.getItem(CART_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) {
      return [];
    }
  }

  function writeCart(items) {
    try {
      window.localStorage.setItem(CART_KEY, JSON.stringify(items));
    } catch (e) {
      /* storage unavailable — prototype still functions within the page */
    }
    updateCartCount();
  }

  function addToCart(item) {
    var items = readCart();
    var existing = items.find(function (i) {
      return i.id === item.id && i.variant === item.variant;
    });
    if (existing) {
      existing.qty += item.qty || 1;
    } else {
      items.push({
        id: item.id,
        name: item.name,
        variant: item.variant || "Standard",
        price: item.price,
        image: item.image,
        action: item.action || "Add to cart",
        qty: item.qty || 1
      });
    }
    writeCart(items);
    return items;
  }

  function removeFromCart(id, variant) {
    var items = readCart().filter(function (i) {
      return !(i.id === id && i.variant === variant);
    });
    writeCart(items);
    return items;
  }

  function updateQty(id, variant, delta) {
    var items = readCart();
    var line = items.find(function (i) {
      return i.id === id && i.variant === variant;
    });
    if (line) {
      line.qty = Math.max(1, line.qty + delta);
    }
    writeCart(items);
    return items;
  }

  function cartTotalQty() {
    return readCart().reduce(function (sum, i) {
      return sum + i.qty;
    }, 0);
  }

  function updateCartCount() {
    var count = cartTotalQty();
    document.querySelectorAll("[data-cart-count]").forEach(function (el) {
      el.textContent = String(count);
      el.setAttribute("data-count", String(count));
    });
  }

  /* -------------------------------- Header ---------------------------------- */
  function initHeader() {
    var header = document.querySelector(".site-header");
    var toggle = document.querySelector(".menu-toggle");
    var nav = document.querySelector(".main-nav");

    function onScroll() {
      if (!header) return;
      header.classList.toggle("is-scrolled", window.scrollY > 4);
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    function syncNavTop() {
      if (!header) return;
      document.documentElement.style.setProperty("--nav-top", header.getBoundingClientRect().bottom + "px");
    }
    syncNavTop();
    window.addEventListener("resize", syncNavTop);

    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        syncNavTop();
        var open = nav.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.style.overflow = open ? "hidden" : "";
      });
      nav.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () {
          nav.classList.remove("is-open");
          toggle.setAttribute("aria-expanded", "false");
          document.body.style.overflow = "";
        });
      });
    }

    updateCartCount();
  }

  /* ------------------------------ Product gallery ----------------------------- */
  function initGallery() {
    var main = document.querySelector("[data-gallery-main]");
    var thumbs = document.querySelectorAll("[data-gallery-thumb]");
    if (!main || !thumbs.length) return;

    thumbs.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var src = btn.getAttribute("data-full");
        var label = btn.getAttribute("data-label") || "";
        main.src = src;
        main.alt = label;
        thumbs.forEach(function (b) {
          b.setAttribute("aria-current", "false");
        });
        btn.setAttribute("aria-current", "true");
      });
    });
  }

  /* -------------------------------- Variants ---------------------------------- */
  function initVariants() {
    var groups = document.querySelectorAll("[data-variant-group]");
    groups.forEach(function (group) {
      var swatches = group.querySelectorAll(".swatch");
      swatches.forEach(function (sw) {
        sw.addEventListener("click", function () {
          swatches.forEach(function (s) {
            s.setAttribute("aria-pressed", "false");
          });
          sw.setAttribute("aria-pressed", "true");
          var buyBtn = document.querySelector("[data-action='add-to-cart']");
          if (buyBtn) buyBtn.setAttribute("data-variant", sw.textContent.trim());
        });
      });
    });
  }

  /* ------------------------------- Add to cart --------------------------------- */
  function initAddToCart() {
    var buttons = document.querySelectorAll("[data-action='add-to-cart']");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var variant = btn.getAttribute("data-variant") || "Standard";
        addToCart({
          id: btn.getAttribute("data-product-id"),
          name: btn.getAttribute("data-product-name"),
          variant: variant,
          price: btn.getAttribute("data-price"),
          image: btn.getAttribute("data-image"),
          action: btn.textContent.trim()
        });
        var original = btn.textContent;
        btn.textContent = "ADDED — VIEW CART";
        btn.classList.add("is-added");
        window.setTimeout(function () {
          btn.textContent = original;
          btn.classList.remove("is-added");
        }, 1800);
      });
    });
  }

  /* --------------------------- Sticky mobile buy bar ---------------------------- */
  function initMobileBuyBar() {
    var bar = document.querySelector(".mobile-buy-bar");
    var anchor = document.querySelector(".buy-actions");
    if (!bar || !anchor) return;

    function sync() {
      var passed = anchor.getBoundingClientRect().bottom < 0;
      bar.classList.toggle("is-visible", passed);
    }
    window.addEventListener("scroll", sync, { passive: true });
    window.addEventListener("resize", sync);
    sync();

    var barBtn = bar.querySelector("[data-action='add-to-cart']");
    if (barBtn) {
      barBtn.addEventListener("click", function () {
        var mainBtn = document.querySelector(".buy-actions [data-action='add-to-cart']");
        if (mainBtn) mainBtn.click();
      });
    }
  }

  /* ------------------------------- Cart page render ------------------------------ */
  function renderCartPage() {
    var root = document.querySelector("[data-cart-root]");
    if (!root) return;

    var items = readCart();
    var emptyState = document.querySelector("[data-cart-empty]");
    var filledState = document.querySelector("[data-cart-filled]");

    if (!items.length) {
      if (emptyState) emptyState.style.display = "block";
      if (filledState) filledState.style.display = "none";
      return;
    }
    if (emptyState) emptyState.style.display = "none";
    if (filledState) filledState.style.display = "grid";

    root.innerHTML = "";
    items.forEach(function (item) {
      var line = document.createElement("div");
      line.className = "cart-line";
      line.innerHTML =
        '<div class="cart-line-media"><img src="' + item.image + '" alt="" /></div>' +
        '<div class="cart-line-info">' +
          '<div class="cart-line-name">' + item.name + "</div>" +
          '<div class="cart-line-variant">' + item.variant + " · " + item.action + '</div>' +
          '<div class="qty-control" role="group" aria-label="Quantity for ' + item.name + '">' +
            '<button type="button" data-qty-down aria-label="Decrease quantity">−</button>' +
            '<span>' + item.qty + '</span>' +
            '<button type="button" data-qty-up aria-label="Increase quantity">+</button>' +
          '</div>' +
          '<button type="button" class="cart-line-remove" data-remove>Remove</button>' +
        '</div>' +
        '<div class="cart-line-price">' + item.price + '</div>';

      line.querySelector("[data-qty-up]").addEventListener("click", function () {
        updateQty(item.id, item.variant, 1);
        renderCartPage();
      });
      line.querySelector("[data-qty-down]").addEventListener("click", function () {
        updateQty(item.id, item.variant, -1);
        renderCartPage();
      });
      line.querySelector("[data-remove]").addEventListener("click", function () {
        removeFromCart(item.id, item.variant);
        renderCartPage();
      });

      root.appendChild(line);
    });

    var countEl = document.querySelector("[data-cart-item-count]");
    if (countEl) countEl.textContent = String(cartTotalQty());
  }

  function initCheckoutButton() {
    var btn = document.querySelector("[data-checkout]");
    if (!btn) return;
    btn.addEventListener("click", function () {
      window.localStorage.setItem("zentro_last_order_items", JSON.stringify(readCart()));
      writeCart([]);
      window.location.href = "checkout-confirmation.html";
    });
  }

  function renderConfirmation() {
    var el = document.querySelector("[data-confirmation-items]");
    if (!el) return;
    var items = [];
    try {
      items = JSON.parse(window.localStorage.getItem("zentro_last_order_items") || "[]");
    } catch (e) {}
    if (!items.length) return;
    el.innerHTML = items
      .map(function (i) {
        return "<li>" + i.qty + "× " + i.name + " — " + i.variant + "</li>";
      })
      .join("");
  }

  /* --------------------------------- Contact form -------------------------------- */
  function initContactForm() {
    var form = document.querySelector("[data-contact-form]");
    if (!form) return;
    var status = document.querySelector("[data-form-status]");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (status) {
        status.textContent =
          "Thanks — this is a working prototype, so no message was actually sent. In the live site this form will deliver your enquiry to Zentro Moto.";
        status.classList.add("is-visible");
        status.setAttribute("tabindex", "-1");
        status.focus();
      }
      form.reset();
    });
  }

  // Real countdown to the next weekly batch cut-off (Sunday, end of day, in
  // the visitor's own local time) — computed live from the browser clock so
  // it is always accurate for whoever is viewing the page, never a fixed or
  // stale figure baked in at build time.
  function initBatchCountdown() {
    var longEls = document.querySelectorAll("[data-countdown]");
    var shortEls = document.querySelectorAll("[data-countdown-short]");
    if (!longEls.length && !shortEls.length) return;
    var daysUntilSunday = (7 - new Date().getDay()) % 7;

    var longText;
    if (daysUntilSunday === 0) {
      longText = "Batch cut-off is today";
    } else if (daysUntilSunday === 1) {
      longText = "1 day until next batch cut-off";
    } else {
      longText = daysUntilSunday + " days until next batch cut-off";
    }
    longEls.forEach(function (el) {
      el.textContent = " — " + longText;
    });

    var shortText;
    if (daysUntilSunday === 0) {
      shortText = "Cut-off is today";
    } else if (daysUntilSunday === 1) {
      shortText = "1 day until cut-off";
    } else {
      shortText = daysUntilSunday + " days until cut-off";
    }
    shortEls.forEach(function (el) {
      el.textContent = " · " + shortText;
    });
  }

  /* ------------------------------------- Init ------------------------------------- */
  document.addEventListener("DOMContentLoaded", function () {
    initHeader();
    initGallery();
    initVariants();
    initAddToCart();
    initMobileBuyBar();
    renderCartPage();
    initCheckoutButton();
    renderConfirmation();
    initContactForm();
    initBatchCountdown();

    var year = document.querySelector("[data-year]");
    if (year) year.textContent = String(new Date().getFullYear());
  });
})();
