#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generates the Zentro Moto static prototype pages from shared components."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# Shared copy (kept word-for-word consistent across pages per the brief)
# --------------------------------------------------------------------------
WARRANTY_HEADLINE = "12-MONTH FACTORY WARRANTY"
WARRANTY_BODY = "The bike is supplied with a 12-month factory warranty covering core powertrain components: battery, controller, motor and frame, subject to the applicable warranty terms and exclusions."
WARRANTY_BODY_LONG = "The bike is supplied with a 12-month factory warranty on core powertrain components: battery, controller, motor and frame, subject to the applicable factory warranty terms, exclusions and claim requirements."
PARTS_HEADLINE = "SPARE PARTS & SUPPORT"
PARTS_BODY = "Zentro Moto supplies genuine OEM replacement parts, common wear-and-tear items and selected performance upgrades, helping customers keep their bikes supported and minimise downtime."
PARTS_BODY_ALT = "Zentro Moto supplies genuine OEM replacement parts, common wear-and-tear items and selected performance upgrades. This helps customers obtain the parts they need without relying solely on third-party sourcing."
ACL_HEADLINE = "AUSTRALIAN CONSUMER LAW"
ACL_BODY = "Any factory warranty is in addition to rights that may apply under the Australian Consumer Law. Zentro Moto remains the customer’s first point of contact for products purchased from Zentro Moto."
INDEPENDENT_STATEMENT = "Zentro Moto is an independent Australian retailer and is not an authorised Australian Surron distributor or representative."
FOOTER_DISCLOSURE = "Zentro Moto is an independent retailer and is not an authorised distributor or representative of Surron."
PRICE_PLACEHOLDER = "$X,XXX"

BIKES = [
    {
        "id": "hyper-bee",
        "slug": "hyper-bee",
        "name": "Hyper Bee",
        "url": "product-hyper-bee.html",
        "size": "Smallest",
        "availability": "in-stock",
        "availability_label": "IN STOCK",
        "primary_action": "ADD TO CART",
        "action_kind": "add-to-cart",
        "one_liner": "The compact, playful entry point into the Surron electric line-up.",
        "intro": "Hyper Bee is the smallest bike in the Zentro Moto range — a compact, electric-powered ride built for fun, easy handling and everyday accessibility. It’s the natural starting point for riders who want genuine Surron engineering in the most approachable size.",
        "features": [
            ("Compact chassis", "A smaller frame designed for easy handling and confident control in tight spaces."),
            ("Electric power", "Fully electric powertrain with the direct, responsive power delivery Surron is known for."),
            ("Removable battery", "Battery designed for removal, making charging and storage straightforward."),
            ("Suspension", "Suspension set up for a comfortable, controlled ride across everyday terrain."),
            ("Lightweight handling", "A light, manageable package that’s easy to ride, load and move around."),
        ],
    },
    {
        "id": "light-bee-2",
        "slug": "light-bee-2",
        "name": "Light Bee 2.0",
        "url": "product-light-bee-2.html",
        "size": "Mid-size",
        "availability": "incoming",
        "availability_label": "INCOMING",
        "primary_action": "RESERVE BIKE",
        "action_kind": "reserve",
        "one_liner": "The mid-size all-rounder, built for riders who want more from every ride.",
        "intro": "Light Bee 2.0 sits in the middle of the Zentro Moto range — a lightweight, electric-powered motorcycle built to go further and do more than the Hyper Bee, without stepping up to full size. It suits riders who want a capable, versatile everyday bike.",
        "features": [
            ("Lightweight chassis", "A light frame that keeps the bike manageable without giving up capability."),
            ("Electric powertrain", "A responsive electric powertrain suited to everyday and recreational riding."),
            ("Battery system", "A battery system designed for real-world range and dependable performance."),
            ("Suspension", "Suspension tuned for a controlled, comfortable ride across varied terrain."),
            ("Braking system", "A braking system built to match the bike’s performance and everyday use."),
        ],
    },
    {
        "id": "ultra-bee",
        "slug": "ultra-bee",
        "name": "Ultra Bee",
        "url": "product-ultra-bee.html",
        "size": "Largest",
        "availability": "order",
        "availability_label": "AVAILABLE TO ORDER",
        "primary_action": "ORDER YOURS",
        "action_kind": "order",
        "one_liner": "The full-size flagship, built for riders who want maximum performance.",
        "intro": "Ultra Bee is the largest and most capable bike in the Zentro Moto range — a full-size electric motorcycle built for riders who want the most performance Surron offers. It’s the flagship choice for serious everyday and off-road riding.",
        "features": [
            ("Full-size chassis", "A larger frame built to suit taller riders and more demanding riding conditions."),
            ("Higher-output powertrain", "A higher-output electric powertrain built for stronger, sustained performance."),
            ("Larger battery", "A larger battery designed to support the bike’s increased performance and use."),
            ("Advanced suspension", "A more advanced suspension setup built to handle demanding terrain."),
            ("Stronger braking", "A stronger braking package matched to the bike’s size and performance."),
        ],
    },
]

SHOTS = [
    ("profile", "Full Profile"),
    ("front-3-4", "Front 3/4"),
    ("rear", "Rear"),
    ("cockpit", "Cockpit"),
    ("suspension-brakes", "Suspension & Brakes"),
    ("motor", "Motor"),
    ("battery", "Battery"),
]

SPEC_ROWS = [
    "Peak power", "Rated power", "Battery", "Top speed", "Claimed range",
    "Weight", "Seat height", "Front suspension", "Rear suspension",
    "Front brake", "Rear brake", "Wheel size", "Charging time", "Dimensions",
]


def img(name):
    return f"assets/img/placeholders/{name}.svg"


# --------------------------------------------------------------------------
# Shared chrome: <head>, header, footer, page shell
# --------------------------------------------------------------------------

def head(title, description, canonical=""):
    return f"""<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | Zentro Moto</title>
  <meta name="description" content="{description}" />
  <link rel="icon" href="data:," />
  <link rel="stylesheet" href="assets/css/styles.css" />"""


NAV_ITEMS = [
    ("Bikes", "bikes.html", "bikes"),
    ("About", "about.html", "about"),
    ("Support", "support.html", "support"),
    ("Contact", "contact.html", "contact"),
]


def header_html(active=""):
    links = []
    for label, url, key in NAV_ITEMS:
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{url}"{current}>{label}</a>')
    nav = "\n        ".join(links)
    cart_current = ' aria-current="page"' if active == "cart" else ""
    return f"""  <div class="announce">Light Bee 2.0 now available to reserve — <a href="bikes.html">View bikes</a></div>
  <header class="site-header">
    <div class="container header-inner">
      <a href="index.html" class="wordmark">ZENTRO MOTO</a>
      <nav class="main-nav" aria-label="Primary">
        {nav}
      </nav>
      <div class="header-actions">
        <a href="cart.html" class="icon-btn"{cart_current} aria-label="Cart">
          Cart <span class="cart-count" data-cart-count data-count="0">0</span>
        </a>
        <button class="menu-toggle" aria-label="Menu" aria-expanded="false" aria-controls="primary-nav">
          <span class="bar"></span><span class="bar"></span><span class="bar"></span>
        </button>
      </div>
    </div>
  </header>"""


def footer_html():
    return f"""  <footer class="site-footer">
    <div class="container">
      <div class="footer-top">
        <div class="footer-brand">
          <a href="index.html" class="wordmark">ZENTRO MOTO</a>
          <p>Genuine Surron electric motorcycles, independently sourced and supplied in Australia. Newcastle, NSW.</p>
        </div>
        <div class="footer-col">
          <h4>Bikes</h4>
          <ul>
            <li><a href="product-hyper-bee.html">Hyper Bee</a></li>
            <li><a href="product-light-bee-2.html">Light Bee 2.0</a></li>
            <li><a href="product-ultra-bee.html">Ultra Bee</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="support.html">Support</a></li>
            <li><a href="shipping.html">Shipping &amp; Collection</a></li>
            <li><a href="warranty.html">Warranty &amp; Returns</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About Zentro Moto</a></li>
            <li><a href="about.html#location">Newcastle, NSW</a></li>
            <li><a href="about.html#business-details">ABN</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Legal</h4>
          <ul>
            <li><a href="legal-terms.html">Terms</a></li>
            <li><a href="legal-privacy.html">Privacy</a></li>
            <li><a href="legal-reservation-terms.html">Reservation Terms</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p class="footer-legal-note">{FOOTER_DISCLOSURE}</p>
        <p class="footer-copyright">&copy; <span data-year>2026</span> Zentro Moto. Prototype build.</p>
      </div>
    </div>
  </footer>"""


def page(title, description, active, body, body_class=""):
    cls = f' class="{body_class}"' if body_class else ""
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
{head(title, description)}
</head>
<body{cls}>
  <a class="skip-link" href="#main">Skip to content</a>
{header_html(active)}
  <main id="main">
{body}
  </main>
{footer_html()}
  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)


def badge(bike):
    return f'<span class="badge badge--{bike["availability"]}">{bike["availability_label"]}</span>'


def bike_card(bike, ctx="home"):
    return f"""        <article class="bike-card">
          <a class="bike-card-media" href="{bike['url']}">
            <img src="{img(bike['slug'] + '-card')}" alt="{bike['name']} placeholder image" loading="lazy" />
          </a>
          <div class="bike-card-body">
            <div class="bike-card-top">
              <div>
                <div class="bike-card-size">{bike['size']}</div>
                <div class="bike-card-name">{bike['name']}</div>
              </div>
              {badge(bike)}
            </div>
            <div class="bike-card-price">{PRICE_PLACEHOLDER}</div>
            <p class="bike-card-desc">{bike['one_liner']}</p>
            <div class="bike-card-cta"><a class="btn btn-secondary" href="{bike['url']}">VIEW {bike['name'].upper()}</a></div>
          </div>
        </article>"""


def trust_strip_html():
    return f"""  <section class="trust-strip">
    <div class="trust-grid container">
      <div class="trust-item">
        <h3>Genuine Bikes</h3>
        <p>Authentic Surron products.</p>
      </div>
      <div class="trust-item">
        <h3>12-Month Warranty</h3>
        <p>Factory warranty on battery, controller, motor and frame, subject to warranty terms.</p>
      </div>
      <div class="trust-item">
        <h3>Parts Support</h3>
        <p>Genuine OEM replacement parts, wear items and selected upgrades available.</p>
      </div>
      <div class="trust-item">
        <h3>Australian Support</h3>
        <p>Deal directly with Zentro Moto before and after purchase.</p>
      </div>
    </div>
  </section>"""


# --------------------------------------------------------------------------
# 1. Home page
# --------------------------------------------------------------------------

def build_home():
    bikes_grid = "\n".join(bike_card(b) for b in BIKES)
    body = f"""    <!-- 03 Hero -->
    <section class="hero hero--home container">
      <div class="hero-copy">
        <span class="eyebrow">Genuine Surron &middot; Newcastle, NSW</span>
        <h1 class="h1">Genuine Surron. Straightforward buying.</h1>
        <p class="lede">Genuine Surron electric motorcycles, independently sourced and supplied in Australia.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary btn-lg" href="bikes.html">SHOP BIKES</a>
          <a class="btn btn-secondary btn-lg" href="#how-it-works">HOW IT WORKS</a>
        </div>
      </div>
      <div class="hero-media">
        <img src="{img('home-hero')}" alt="Zentro Moto placeholder hero image" />
      </div>
    </section>

    <!-- 04 Trust strip -->
{trust_strip_html()}

    <!-- 05 The three bikes -->
    <section class="section container" id="bikes">
      <div class="section-head section-head--center">
        <h2 class="h2">Choose your Surron</h2>
        <p class="lede" style="margin:16px auto 0;">Three bikes. From compact electric fun to full-size performance.</p>
      </div>
      <div class="bike-grid">
{bikes_grid}
      </div>
    </section>

    <!-- 06 Why Zentro Moto -->
    <section class="section section--grey">
      <div class="container">
        <div class="section-head">
          <h2 class="h2">A simpler way to buy.</h2>
        </div>
        <div class="reasons">
          <div class="reason">
            <h3>Genuine Surron</h3>
            <p>Genuine bikes sourced through established international wholesale supply channels.</p>
          </div>
          <div class="reason">
            <h3>Clear availability</h3>
            <p>Know whether each bike is in stock, incoming or available to order.</p>
          </div>
          <div class="reason">
            <h3>Support after purchase</h3>
            <p>Local contact, 12-month factory warranty on core components, and access to genuine OEM parts.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 07 How buying works -->
    <section class="section container" id="how-it-works">
      <div class="section-head">
        <h2 class="h2">Simple from order to ride.</h2>
      </div>
      <div class="steps">
        <div class="step">
          <div class="step-num">01</div>
          <h3>Choose</h3>
          <p>Pick the model that suits you.</p>
        </div>
        <div class="step">
          <div class="step-num">02</div>
          <h3>Buy or reserve</h3>
          <p>Purchase an available bike or reserve an incoming / order-in bike.</p>
        </div>
        <div class="step">
          <div class="step-num">03</div>
          <h3>We organise the rest</h3>
          <p>Zentro Moto handles sourcing and keeps you updated.</p>
        </div>
        <div class="step">
          <div class="step-num">04</div>
          <h3>Get your bike</h3>
          <p>Collect in Newcastle or arrange delivery.</p>
        </div>
      </div>
      <div style="margin-top:40px;">
        <a class="btn btn-primary" href="bikes.html">SHOP BIKES</a>
      </div>
    </section>

    <!-- 08 Newcastle / delivery -->
    <section class="section section--black">
      <div class="container split">
        <div>
          <span class="eyebrow" style="color:rgba(255,255,255,0.6);">Delivery</span>
          <h2 class="h2">Newcastle pickup or delivery.</h2>
          <p class="lede" style="color:rgba(255,255,255,0.75); margin:20px 0 28px;">Collect from Zentro Moto in Newcastle, NSW, or arrange delivery to eligible locations.</p>
          <a class="btn btn-primary btn-on-black" href="shipping.html">SHIPPING &amp; COLLECTION &rarr;</a>
        </div>
        <div class="split-media">
          <img src="{img('bikes-hero')}" alt="Newcastle collection placeholder image" />
        </div>
      </div>
    </section>

    <!-- 09 Homepage FAQ -->
    <section class="section container">
      <div class="section-head">
        <h2 class="h2">Frequently asked questions</h2>
      </div>
      <div class="faq-list">
        <details class="faq-item" open>
          <summary>Are the bikes genuine Surrons?<span class="faq-icon"></span></summary>
          <div class="faq-body">Yes. Zentro Moto sells genuine Surron products sourced through international wholesale supply channels.</div>
        </details>
        <details class="faq-item">
          <summary>Is Zentro Moto an authorised Surron distributor?<span class="faq-icon"></span></summary>
          <div class="faq-body">No. Zentro Moto is an independent Australian retailer and is not an authorised Australian Surron distributor or representative.</div>
        </details>
        <details class="faq-item">
          <summary>What warranty support is included?<span class="faq-icon"></span></summary>
          <div class="faq-body">A 12-month factory warranty applies to the battery, controller, motor and frame, subject to the applicable warranty terms. Zentro Moto is your first point of contact.</div>
        </details>
        <details class="faq-item">
          <summary>Can I get replacement parts?<span class="faq-icon"></span></summary>
          <div class="faq-body">Yes. Zentro Moto supplies genuine OEM replacement parts, common wear items and selected performance upgrades.</div>
        </details>
      </div>
      <div style="margin-top:28px;">
        <a class="btn-link" href="support.html">VISIT SUPPORT &rarr;</a>
      </div>
    </section>

    <!-- 10 Final CTA -->
    <section class="section section--grey">
      <div class="container section-head--center">
        <h2 class="h2">Find your Surron.</h2>
        <p class="lede" style="margin:16px auto 32px;">Explore the Hyper Bee, Light Bee 2.0 and Ultra Bee.</p>
        <a class="btn btn-primary btn-lg" href="bikes.html">SHOP BIKES</a>
      </div>
    </section>"""
    write("index.html", page(
        "Home",
        "Genuine Surron electric motorcycles, independently sourced and supplied in Australia. Hyper Bee, Light Bee 2.0 and Ultra Bee — Newcastle, NSW.",
        "home", body,
    ))


# --------------------------------------------------------------------------
# 2. Bikes page
# --------------------------------------------------------------------------

def build_bikes():
    bikes_grid = "\n".join(bike_card(b) for b in BIKES)
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">The range</span>
      <h1 class="h1">Find your Surron.</h1>
      <p class="lede" style="margin-top:16px;">Three bikes. Three sizes. Choose the one that suits you.</p>
    </section>
    <section class="section container">
      <div class="bike-grid">
{bikes_grid}
      </div>
    </section>"""
    write("bikes.html", page(
        "Bikes",
        "Hyper Bee, Light Bee 2.0 and Ultra Bee — the complete Zentro Moto range of genuine Surron electric motorcycles.",
        "bikes", body,
    ))


# --------------------------------------------------------------------------
# 3. Product page template (used for all three bikes)
# --------------------------------------------------------------------------

def build_product(bike):
    other_bikes = [b for b in BIKES if b["id"] != bike["id"]]

    # Gallery
    thumbs = []
    for i, (key, label) in enumerate(SHOTS):
        current = "true" if i == 0 else "false"
        thumbs.append(
            f'          <button type="button" data-gallery-thumb data-full="{img(bike["slug"] + "-" + key)}" '
            f'data-label="{bike["name"]} — {label} (placeholder image)" aria-current="{current}">'
            f'<img src="{img(bike["slug"] + "-" + key)}" alt="{bike["name"]} — {label} (placeholder image) thumbnail" loading="lazy" /></button>'
        )
    thumbs_html = "\n".join(thumbs)

    features_html = "\n".join(
        f"""          <div class="feature-item">
            <div class="feature-num">0{i+1}</div>
            <div>
              <h3>{name}</h3>
              <p>{desc}</p>
            </div>
          </div>"""
        for i, (name, desc) in enumerate(bike["features"])
    )

    spec_rows_html = "\n".join(
        f"""            <tr><th scope="row">{row}</th><td><span class="spec-placeholder">SPEC TO CONFIRM</span></td></tr>"""
        for row in SPEC_ROWS
    )

    action_kind = bike["action_kind"]
    if action_kind == "add-to-cart":
        trust_notes_extra = ""
    else:
        trust_notes_extra = ""

    body = f"""    <section class="container">
      <div class="product-top">
        <div class="product-gallery">
          <div class="gallery-main">
            <img data-gallery-main src="{img(bike['slug'] + '-profile')}" alt="{bike['name']} — Full Profile (placeholder image)" />
          </div>
          <div class="gallery-thumbs" role="group" aria-label="{bike['name']} image gallery">
{thumbs_html}
          </div>
        </div>

        <div class="buy-panel">
          <span class="eyebrow">{bike['size']} &middot; Zentro Moto</span>
          <h1 class="h2">{bike['name']}</h1>
          {badge(bike)}
          <div class="buy-price">{PRICE_PLACEHOLDER}</div>
          <p class="buy-desc">{bike['one_liner']}</p>

          <div class="variant-block" data-variant-group>
            <span class="variant-label">Colour / Variant</span>
            <div class="swatch-row">
              <button type="button" class="swatch" aria-pressed="true">Standard &mdash; colour to confirm</button>
            </div>
          </div>

          <div class="buy-actions">
            <button type="button" class="btn btn-primary btn-lg btn-block"
              data-action="add-to-cart"
              data-product-id="{bike['id']}"
              data-product-name="{bike['name']}"
              data-price="{PRICE_PLACEHOLDER}"
              data-image="{img(bike['slug'] + '-card')}"
              data-variant="Standard">
              {bike['primary_action']}
            </button>
          </div>

          <ul class="trust-notes">
            <li><span class="dot"></span> Genuine Surron</li>
            <li><span class="dot"></span> 12-month factory warranty on core components</li>
            <li><span class="dot"></span> OEM parts support</li>
            <li><span class="dot"></span> Newcastle collection / delivery</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- Mobile sticky buy bar -->
    <div class="mobile-buy-bar" aria-hidden="false">
      <div class="mobile-buy-bar-info">
        <div class="mobile-buy-bar-name">{bike['name']}</div>
        <div class="mobile-buy-bar-price">{PRICE_PLACEHOLDER} &middot; {bike['availability_label']}</div>
      </div>
      <button type="button" class="btn btn-primary" data-action="add-to-cart">{bike['primary_action']}</button>
    </div>

    <!-- Section 2: Short introduction -->
    <section class="section container" style="padding-bottom:0;">
      <p class="lede">{bike['intro']}</p>
    </section>

    <!-- Section 3: Key features -->
    <section class="section container">
      <div class="section-head">
        <span class="eyebrow">Key features</span>
        <h2 class="h2">What makes it different.</h2>
      </div>
      <div class="feature-list">
{features_html}
      </div>
    </section>

    <!-- Section 4: Specifications -->
    <section class="section section--grey">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Specifications</span>
          <h2 class="h2">{bike['name']} specifications</h2>
        </div>
        <table class="spec-table">
          <caption class="visually-hidden">{bike['name']} technical specifications</caption>
          <tbody>
{spec_rows_html}
          </tbody>
        </table>
        <p class="spec-note">Specifications shown are placeholders pending confirmation for the exact model and market version sold by Zentro Moto, and will be published once verified.</p>
      </div>
    </section>

    <!-- Section 5: Warranty & parts support -->
    <section class="section container">
      <div class="section-head">
        <h2 class="h2">Support after your purchase.</h2>
      </div>
      <div class="info-cols">
        <div class="info-col">
          <h3>{WARRANTY_HEADLINE}</h3>
          <p>{WARRANTY_BODY}</p>
        </div>
        <div class="info-col">
          <h3>{PARTS_HEADLINE}</h3>
          <p>{PARTS_BODY}</p>
        </div>
        <div class="info-col">
          <h3>{ACL_HEADLINE}</h3>
          <p>{ACL_BODY}</p>
        </div>
      </div>
      <div style="margin-top:32px;">
        <a class="btn-link" href="warranty.html">VIEW WARRANTY &amp; RETURNS &rarr;</a>
      </div>
    </section>

    <!-- Section 6: What's included -->
    <section class="section section--grey">
      <div class="container">
        <div class="section-head">
          <h2 class="h2">What&rsquo;s included.</h2>
        </div>
        <ul class="included-list">
          <li><span class="dot"></span> {bike['name']}</li>
          <li><span class="dot"></span> Battery</li>
          <li><span class="dot"></span> Charger</li>
          <li><span class="dot"></span> Documentation</li>
          <li><span class="dot"></span> Included factory accessories &mdash; SPEC TO CONFIRM</li>
          <li><span class="dot"></span> Assembly required &mdash; SPEC TO CONFIRM</li>
        </ul>
      </div>
    </section>

    <!-- Section 7: Delivery & support -->
    <section class="section container">
      <div class="section-head">
        <h2 class="h2">Delivery &amp; support.</h2>
      </div>
      <div class="info-cols">
        <div class="info-col">
          <h3>Newcastle collection</h3>
          <p>Collect directly from Zentro Moto.</p>
        </div>
        <div class="info-col">
          <h3>Delivery</h3>
          <p>Freight can be arranged to eligible Australian locations.</p>
        </div>
        <div class="info-col">
          <h3>Support</h3>
          <p>Questions after purchase are handled through Zentro Moto.</p>
        </div>
      </div>
      <div style="margin-top:32px; display:flex; gap:28px; flex-wrap:wrap;">
        <a class="btn-link" href="shipping.html">SHIPPING INFORMATION</a>
        <a class="btn-link" href="warranty.html">WARRANTY &amp; RETURNS</a>
      </div>
    </section>

    <!-- Cross-links to other bikes -->
    <section class="section container">
      <div class="section-head">
        <h2 class="h3">Explore the range.</h2>
      </div>
      <div class="bike-grid">
{chr(10).join(bike_card(b) for b in other_bikes)}
      </div>
    </section>"""
    write(bike["url"], page(
        bike["name"],
        f"{bike['name']} — genuine Surron electric motorcycle. {bike['one_liner']}",
        "bikes", body,
    ))


# --------------------------------------------------------------------------
# 4. About page
# --------------------------------------------------------------------------

def build_about():
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">About</span>
      <h1 class="h1">Zentro Moto</h1>
      <p class="lede" style="margin-top:16px;">A focused Australian retailer specialising in genuine Surron electric motorcycles.</p>
    </section>

    <section class="section container">
      <div class="content-grid">
        <nav class="side-nav" aria-label="On this page">
          <a href="#what-we-do">What we do</a>
          <a href="#focused-range">Why the focused range</a>
          <a href="#independent">Independent retailer</a>
          <a href="#business-details" id="business-details-link">Business details</a>
        </nav>
        <div>
          <div class="content-block" id="what-we-do">
            <h2 class="h3">What we do</h2>
            <p>Zentro Moto independently sources genuine Surron motorcycles through established international wholesale supply channels. The range is deliberately limited to the Hyper Bee, Light Bee 2.0 and Ultra Bee.</p>
          </div>

          <div class="content-block" id="focused-range">
            <h2 class="h3">Why the focused range</h2>
            <p>Three bikes. Clear availability. Direct support. Keeping the range focused means every model is well understood, well supported and easy to compare &mdash; rather than a large catalogue that’s hard to trust.</p>
          </div>

          <div class="content-block" id="independent">
            <h2 class="h3">Independent retailer statement</h2>
            <p>Zentro Moto is independently owned and operated and is not an authorised distributor or representative of Surron.</p>
          </div>

          <div class="content-block" id="business-details">
            <h2 class="h3">Business details</h2>
            <ul class="bullet">
              <li id="location">Newcastle, NSW</li>
              <li>Business name: Zentro Moto &mdash; BUSINESS NAME TO CONFIRM</li>
              <li>ABN: ABN TO CONFIRM</li>
              <li>Contact: see <a href="contact.html">Contact Zentro Moto</a> for phone and email details</li>
            </ul>
          </div>
        </div>
      </div>
    </section>"""
    write("about.html", page(
        "About",
        "Zentro Moto is a focused Australian retailer specialising in genuine Surron electric motorcycles, based in Newcastle, NSW.",
        "about", body,
    ))


# --------------------------------------------------------------------------
# 5. Support / FAQ page
# --------------------------------------------------------------------------

def faq(q, a):
    return f"""        <details class="faq-item">
          <summary>{q}<span class="faq-icon"></span></summary>
          <div class="faq-body">{a}</div>
        </details>"""


def build_support():
    ordering = "\n".join([
        faq("What does IN STOCK mean?", "The bike is physically available at Zentro Moto in Newcastle and ready to purchase now."),
        faq("What does INCOMING mean?", "The bike is confirmed and on its way to Zentro Moto. You can reserve one ahead of arrival."),
        faq("What does AVAILABLE TO ORDER mean?", "The bike can be ordered in. Zentro Moto will confirm sourcing and an estimated lead time with you."),
        faq("How do reservations work?", "A reservation secures your bike ahead of arrival. See <a href=\"legal-reservation-terms.html\">Reservation / Order Terms</a> for deposit, refund and lead-time details."),
    ])
    delivery = "\n".join([
        faq("Newcastle collection", "Collect your bike directly from Zentro Moto in Newcastle, NSW. See <a href=\"shipping.html\">Shipping &amp; Collection</a> for details."),
        faq("Delivery areas", "Freight can be arranged to eligible Australian locations. See <a href=\"shipping.html\">Shipping &amp; Collection</a>."),
        faq("Delivery timing", "Timing depends on the bike’s availability status and your location. Zentro Moto will confirm an estimate with you directly."),
    ])
    your_bike = "\n".join([
        faq("What is included?", "Each bike is supplied with its battery, charger and documentation, plus any included factory accessories for that model."),
        faq("Setup / assembly", "Whether assembly is required is noted on each bike’s product page."),
        faq("Documentation", "Documentation is included with every bike."),
    ])
    warranty_parts = "\n".join([
        faq(WARRANTY_HEADLINE.title(), WARRANTY_BODY),
        faq("How to make a warranty claim", "See <a href=\"warranty.html\">Warranty &amp; Returns</a> for the full claims process, including what information to provide."),
        faq("Genuine OEM replacement parts", "Zentro Moto supplies genuine OEM replacement parts for supported models."),
        faq("Wear-and-tear items", "Common wear-and-tear items are available through Zentro Moto."),
        faq("Selected performance upgrades", "A selection of performance upgrades is available &mdash; contact Zentro Moto for current options."),
        faq("Australian Consumer Law rights", ACL_BODY),
    ])
    returns = "\n".join([
        faq("Faulty products", "Contact Zentro Moto as soon as possible if you believe your bike has a fault. See <a href=\"warranty.html\">Warranty &amp; Returns</a>."),
        faq("Returns / cancellations", "See <a href=\"warranty.html\">Warranty &amp; Returns</a> for the current returns and cancellation process."),
        faq("Change-of-mind policy", "Any change-of-mind policy offered by Zentro Moto is set out in <a href=\"warranty.html\">Warranty &amp; Returns</a>."),
    ])

    body = f"""    <section class="page-hero container">
      <span class="eyebrow">Help centre</span>
      <h1 class="h1">Support &amp; FAQ</h1>
      <p class="lede" style="margin-top:16px;">Everything you need to know about ordering, delivery, your bike and warranty &mdash; in one place.</p>
    </section>

    <section class="section container">
      <div class="content-grid">
        <nav class="side-nav" aria-label="FAQ categories">
          <a href="#ordering">Ordering</a>
          <a href="#delivery">Delivery &amp; Collection</a>
          <a href="#your-bike">Your Bike</a>
          <a href="#warranty-parts">Warranty &amp; Parts</a>
          <a href="#returns">Returns</a>
        </nav>
        <div>
          <div class="faq-category" id="ordering">
            <h3>Ordering</h3>
            <div class="faq-list">{ordering}
            </div>
          </div>
          <div class="faq-category" id="delivery">
            <h3>Delivery &amp; Collection</h3>
            <div class="faq-list">{delivery}
            </div>
          </div>
          <div class="faq-category" id="your-bike">
            <h3>Your Bike</h3>
            <div class="faq-list">{your_bike}
            </div>
          </div>
          <div class="faq-category" id="warranty-parts">
            <h3>Warranty &amp; Parts</h3>
            <div class="faq-list">{warranty_parts}
            </div>
          </div>
          <div class="faq-category" id="returns">
            <h3>Returns</h3>
            <div class="faq-list">{returns}
            </div>
          </div>
          <div class="content-block">
            <p>Still need help?</p>
            <a class="btn btn-primary" href="contact.html" style="margin-top:16px;">CONTACT ZENTRO MOTO</a>
          </div>
        </div>
      </div>
    </section>"""
    write("support.html", page(
        "Support & FAQ",
        "Answers to common questions about ordering, delivery, your bike, warranty and returns at Zentro Moto.",
        "support", body,
    ))


# --------------------------------------------------------------------------
# 6. Shipping & Collection page
# --------------------------------------------------------------------------

def build_shipping():
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">Support</span>
      <h1 class="h1">Shipping &amp; Collection</h1>
      <p class="lede" style="margin-top:16px;">How to collect your bike from Newcastle, or arrange delivery Australia-wide.</p>
    </section>

    <section class="section container">
      <div class="content-grid">
        <nav class="side-nav" aria-label="On this page">
          <a href="#collection">Newcastle collection</a>
          <a href="#delivery">Australian delivery</a>
          <a href="#freight-damage">Freight damage</a>
        </nav>
        <div>
          <div class="content-block" id="collection">
            <h2 class="h3">Newcastle collection</h2>
            <p>Bikes can be collected directly from Zentro Moto in Newcastle, NSW.</p>
            <ul class="bullet">
              <li>Collection location: Newcastle, NSW &mdash; full address confirmed on booking</li>
              <li>Appointment required: PROCESS TO CONFIRM</li>
              <li>Identification requirements: TO CONFIRM</li>
              <li>Assembly status on collection: confirmed per bike on its product page</li>
              <li>What to bring: TO CONFIRM</li>
            </ul>
          </div>

          <div class="content-block" id="delivery">
            <h2 class="h3">Australian delivery</h2>
            <p>Freight can be arranged to eligible Australian locations.</p>
            <ul class="bullet">
              <li>Eligible locations: AREAS TO CONFIRM</li>
              <li>Freight pricing: calculated and confirmed per order &mdash; SPEC TO CONFIRM</li>
              <li>Typical timing: TIMEFRAME TO CONFIRM</li>
              <li>Packaging: bikes are freighted securely packaged &mdash; PROCESS TO CONFIRM</li>
              <li>Receiving your bike: PROCESS TO CONFIRM</li>
            </ul>
          </div>

          <div class="content-block" id="freight-damage">
            <h2 class="h3">Freight damage</h2>
            <p>If your bike arrives with visible freight damage, contact Zentro Moto as soon as possible.</p>
            <ul class="bullet">
              <li>Reporting process: PROCESS TO CONFIRM</li>
              <li>Timeframe to notify Zentro Moto: TIMEFRAME TO CONFIRM</li>
            </ul>
            <div class="callout"><p>Have photos of the packaging and any damage ready when you contact Zentro Moto — this helps resolve freight damage claims quickly.</p></div>
          </div>

          <div class="content-block">
            <p>Questions about delivery?</p>
            <a class="btn btn-primary" href="contact.html" style="margin-top:16px;">CONTACT US</a>
          </div>
        </div>
      </div>
    </section>"""
    write("shipping.html", page(
        "Shipping & Collection",
        "Newcastle collection and Australian delivery information for Zentro Moto electric motorcycles.",
        "", body,
    ))


# --------------------------------------------------------------------------
# 7. Warranty & Returns page
# --------------------------------------------------------------------------

def build_warranty():
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">Support</span>
      <h1 class="h1">Warranty &amp; Returns</h1>
      <p class="lede" style="margin-top:16px;">Your first point of contact for products purchased through Zentro Moto is Zentro Moto.</p>
    </section>

    <section class="section container">
      <div class="content-grid">
        <nav class="side-nav" aria-label="On this page">
          <a href="#warranty">12-month factory warranty</a>
          <a href="#parts">Spare parts support</a>
          <a href="#claims">Warranty claims</a>
          <a href="#acl">Australian Consumer Law</a>
          <a href="#returns">Returns</a>
        </nav>
        <div>
          <div class="content-block" id="warranty">
            <h2 class="h3">12-month factory warranty</h2>
            <p>{WARRANTY_BODY_LONG}</p>
          </div>

          <div class="content-block" id="parts">
            <h2 class="h3">Spare parts support</h2>
            <p>{PARTS_BODY_ALT}</p>
          </div>

          <div class="content-block" id="claims">
            <h2 class="h3">Warranty claims</h2>
            <p>To start a warranty claim, contact Zentro Moto with the following:</p>
            <ul class="bullet">
              <li>Your order number</li>
              <li>Your customer details</li>
              <li>A description of the issue</li>
              <li>Photos or video of the issue</li>
              <li>Any diagnostic information requested by Zentro Moto</li>
            </ul>
            <div style="margin-top:20px;"><a class="btn btn-secondary" href="contact.html">CONTACT ZENTRO MOTO</a></div>
          </div>

          <div class="content-block" id="acl">
            <h2 class="h3">Australian Consumer Law</h2>
            <p>Any factory warranty is in addition to rights that may apply under the Australian Consumer Law. The 12-month factory warranty term does not limit your statutory consumer guarantees.</p>
          </div>

          <div class="content-block" id="returns">
            <h2 class="h3">Returns</h2>
            <ul class="bullet">
              <li>Faulty products: PROCESS TO CONFIRM</li>
              <li>Returns / cancellations: PROCESS TO CONFIRM</li>
              <li>Change-of-mind policy: POLICY TO CONFIRM (if offered)</li>
            </ul>
          </div>

          <div class="callout">
            <p><strong>Important:</strong> Have the final legal wording reviewed before launch, especially the relationship between the factory warranty, supplier arrangements and Australian Consumer Law obligations.</p>
          </div>
        </div>
      </div>
    </section>"""
    write("warranty.html", page(
        "Warranty & Returns",
        "Warranty, spare parts, claims and returns information for Zentro Moto electric motorcycles.",
        "", body,
    ))


# --------------------------------------------------------------------------
# 8. Contact page
# --------------------------------------------------------------------------

def build_contact():
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">Get in touch</span>
      <h1 class="h1">Contact Zentro Moto</h1>
      <p class="lede" style="margin-top:16px;">Questions about a bike, availability, parts or an existing order? Get in touch.</p>
    </section>

    <section class="section container">
      <div class="contact-layout">
        <div class="contact-details">
          <div class="contact-detail">
            <h3>Email</h3>
            <p>EMAIL TO CONFIRM</p>
          </div>
          <div class="contact-detail">
            <h3>Phone</h3>
            <p>PHONE TO CONFIRM</p>
          </div>
          <div class="contact-detail">
            <h3>Location</h3>
            <p>Newcastle, NSW</p>
          </div>
          <div class="contact-detail">
            <h3>Support</h3>
            <p><a href="support.html">Visit the Support &amp; FAQ page &rarr;</a></p>
          </div>
        </div>

        <form class="contact-form" data-contact-form novalidate>
          <div class="form-grid">
            <div class="field">
              <label for="name">Name <span class="req">(required)</span></label>
              <input id="name" name="name" type="text" required autocomplete="name" />
            </div>
            <div class="field">
              <label for="email">Email <span class="req">(required)</span></label>
              <input id="email" name="email" type="email" required autocomplete="email" />
            </div>
            <div class="field">
              <label for="phone">Phone</label>
              <input id="phone" name="phone" type="tel" autocomplete="tel" />
            </div>
            <div class="field">
              <label for="topic">Topic <span class="req">(required)</span></label>
              <select id="topic" name="topic" required>
                <option value="">Select a topic</option>
                <option>Hyper Bee</option>
                <option>Light Bee 2.0</option>
                <option>Ultra Bee</option>
                <option>Parts</option>
                <option>Existing order</option>
                <option>Warranty / support</option>
                <option>Other</option>
              </select>
            </div>
            <div class="field field--full">
              <label for="message">Message <span class="req">(required)</span></label>
              <textarea id="message" name="message" required></textarea>
            </div>
          </div>
          <div class="form-actions">
            <button type="submit" class="btn btn-primary btn-lg">SEND MESSAGE</button>
            <span class="form-note">We aim to respond within 1&ndash;2 business days.</span>
          </div>
          <div class="form-status" data-form-status role="status"></div>
        </form>
      </div>
    </section>"""
    write("contact.html", page(
        "Contact",
        "Contact Zentro Moto about a bike, availability, parts or an existing order.",
        "contact", body,
    ))


# --------------------------------------------------------------------------
# 9. Cart, checkout & confirmation
# --------------------------------------------------------------------------

def build_cart():
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">Your cart</span>
      <h1 class="h1">Cart</h1>
    </section>

    <section class="section container">
      <div data-cart-empty class="empty-cart">
        <p>Your cart is empty.</p>
        <a class="btn btn-primary" href="bikes.html">SHOP BIKES</a>
      </div>

      <div data-cart-filled class="cart-layout" style="display:none;">
        <div>
          <div data-cart-root></div>
        </div>
        <div class="cart-summary">
          <h2 class="h4" style="margin-bottom:16px;">Order summary</h2>
          <div class="summary-row"><span>Items</span><span data-cart-item-count>0</span></div>
          <div class="summary-row"><span>Subtotal</span><span>{PRICE_PLACEHOLDER}</span></div>
          <div class="summary-row"><span>Shipping</span><span>Calculated at checkout</span></div>
          <div class="summary-row total"><span>Total</span><span>{PRICE_PLACEHOLDER}</span></div>
          <button type="button" class="btn btn-primary btn-block btn-lg" data-checkout style="margin-top:20px;">CHECKOUT</button>
          <ul class="cart-trust">
            <li><span class="dot"></span> Secure payment</li>
            <li><span class="dot"></span> Support from Zentro Moto</li>
          </ul>
        </div>
      </div>
    </section>"""
    write("cart.html", page("Cart", "Your Zentro Moto cart.", "cart", body))


def build_checkout_confirmation():
    body = f"""    <section class="section container">
      <div class="checkout-confirm">
        <p class="order-num">Order confirmed</p>
        <h1 class="h2">Thank you for your order.</h1>
        <p class="text-body" style="margin:20px auto;">This is a prototype confirmation screen. In the live site, checkout runs on Shopify’s standard Information &rarr; Delivery &rarr; Payment &rarr; Confirmation flow.</p>
        <ul class="bullet" data-confirmation-items style="text-align:left; max-width: 28em; margin: 24px auto;"></ul>
        <div class="callout" style="text-align:left;">
          <p><strong>What happens next?</strong> If your bike is in stock, Zentro Moto will prepare it for collection or delivery. If it’s incoming or available to order, Zentro Moto will be in touch to confirm sourcing and timing.</p>
        </div>
        <div style="margin-top:32px;">
          <a class="btn btn-secondary" href="index.html">BACK TO HOME</a>
        </div>
      </div>
    </section>"""
    write("checkout-confirmation.html", page("Order Confirmation", "Your Zentro Moto order confirmation.", "", body))


# --------------------------------------------------------------------------
# 10 / Legal pages
# --------------------------------------------------------------------------

def legal_shell(title, active_id, nav, body_blocks):
    side = "\n          ".join(
        f'<a href="#{bid}">{label}</a>' for bid, label in nav
    )
    blocks = "\n\n".join(body_blocks)
    return f"""    <section class="page-hero container">
      <span class="eyebrow">Legal</span>
      <h1 class="h1">{title}</h1>
    </section>
    <section class="section container">
      <div class="content-grid">
        <nav class="side-nav" aria-label="On this page">
          {side}
        </nav>
        <div>
{blocks}
        </div>
      </div>
    </section>"""


def build_legal_terms():
    nav = [("acceptance", "Acceptance of terms"), ("orders", "Orders & payment"),
           ("pricing", "Pricing & availability"), ("warranty", "Warranty"),
           ("liability", "Liability"), ("governing-law", "Governing law")]
    blocks = [
        """          <div class="content-block" id="acceptance">
            <h2 class="h3">Acceptance of terms</h2>
            <p>PLACEHOLDER — full Terms of Sale to be drafted and reviewed before launch. By purchasing from Zentro Moto, customers agree to these terms.</p>
          </div>""",
        """          <div class="content-block" id="orders">
            <h2 class="h3">Orders &amp; payment</h2>
            <p>PLACEHOLDER — TERMS TO CONFIRM. Covers how orders are placed and confirmed, accepted payment methods, and when payment is taken for in-stock, incoming and order-in bikes.</p>
          </div>""",
        f"""          <div class="content-block" id="pricing">
            <h2 class="h3">Pricing &amp; availability</h2>
            <p>Prices are shown in Australian dollars and are current at the time of publishing. Availability is shown against each bike as IN STOCK, INCOMING or AVAILABLE TO ORDER. {INDEPENDENT_STATEMENT}</p>
          </div>""",
        f"""          <div class="content-block" id="warranty">
            <h2 class="h3">Warranty</h2>
            <p>{WARRANTY_BODY} {ACL_BODY}</p>
          </div>""",
        """          <div class="content-block" id="liability">
            <h2 class="h3">Liability</h2>
            <p>PLACEHOLDER — TERMS TO CONFIRM. Have this section reviewed by a qualified professional before launch.</p>
          </div>""",
        """          <div class="content-block" id="governing-law">
            <h2 class="h3">Governing law</h2>
            <p>PLACEHOLDER — These terms are governed by the laws of New South Wales, Australia — TO CONFIRM.</p>
            <div class="callout"><p>This Terms of Sale page is a structural placeholder. Have the final legal wording reviewed by a qualified professional before launch.</p></div>
          </div>""",
    ]
    write("legal-terms.html", page("Terms of Sale", "Zentro Moto Terms of Sale.", "", legal_shell("Terms of Sale", "terms", nav, blocks)))


def build_legal_privacy():
    nav = [("collection", "Information we collect"), ("use", "How we use it"),
           ("sharing", "Sharing"), ("security", "Security"), ("contact-privacy", "Contact")]
    blocks = [
        """          <div class="content-block" id="collection">
            <h2 class="h3">Information we collect</h2>
            <p>PLACEHOLDER — TERMS TO CONFIRM. Typically includes name, contact details, delivery address and order information provided when browsing, enquiring or purchasing.</p>
          </div>""",
        """          <div class="content-block" id="use">
            <h2 class="h3">How we use it</h2>
            <p>PLACEHOLDER — TERMS TO CONFIRM. Used to process orders, arrange delivery or collection, and provide warranty and customer support.</p>
          </div>""",
        """          <div class="content-block" id="sharing">
            <h2 class="h3">Sharing</h2>
            <p>PLACEHOLDER — TERMS TO CONFIRM. Any sharing with delivery partners, payment processors or platform providers (e.g. Shopify) to be detailed here.</p>
          </div>""",
        """          <div class="content-block" id="security">
            <h2 class="h3">Security</h2>
            <p>PLACEHOLDER — TERMS TO CONFIRM.</p>
          </div>""",
        """          <div class="content-block" id="contact-privacy">
            <h2 class="h3">Contact</h2>
            <p>Questions about this policy can be sent via the <a href="contact.html">Contact page</a>.</p>
            <div class="callout"><p>This Privacy Policy page is a structural placeholder. Have the final legal wording reviewed by a qualified professional before launch.</p></div>
          </div>""",
    ]
    write("legal-privacy.html", page("Privacy Policy", "Zentro Moto Privacy Policy.", "", legal_shell("Privacy Policy", "privacy", nav, blocks)))


def build_legal_reservation():
    nav = [("deposit", "Deposit amount"), ("refundable", "Refundable?"),
           ("lead-time", "Estimated lead time"), ("balance", "Remaining balance"),
           ("delay", "If there is a delay"), ("cancellation", "Cancellation rules"),
           ("cannot-source", "If Zentro Moto cannot source the bike")]
    rows = [
        ("deposit", "Deposit amount", "AMOUNT TO CONFIRM"),
        ("refundable", "Is the deposit refundable?", "TO CONFIRM"),
        ("lead-time", "Estimated lead time", "TIMEFRAME TO CONFIRM"),
        ("balance", "When the remaining balance is due", "TO CONFIRM"),
        ("delay", "What happens if there is a delay", "PROCESS TO CONFIRM"),
        ("cancellation", "Cancellation rules", "TERMS TO CONFIRM"),
        ("cannot-source", "What happens if Zentro Moto cannot source the bike", "PROCESS TO CONFIRM — typically a full deposit refund"),
    ]
    blocks = [
        """          <div class="content-block">
            <p>This page applies only to bikes purchased on a reservation or order-in basis (INCOMING or AVAILABLE TO ORDER). It has no effect on bikes purchased IN STOCK.</p>
          </div>"""
    ]
    for bid, label, value in rows:
        blocks.append(f"""          <div class="content-block" id="{bid}">
            <h2 class="h3">{label}</h2>
            <p>{value}</p>
          </div>""")
    blocks.append("""          <div class="callout"><p>This Reservation / Order Terms page is a structural placeholder. Have the final deposit, refund and cancellation terms reviewed by a qualified professional before launch.</p></div>""")
    write("legal-reservation-terms.html", page(
        "Reservation / Order Terms",
        "Zentro Moto Reservation and Order Terms for incoming and order-in bikes.",
        "", legal_shell("Reservation / Order Terms", "reservation", nav, blocks),
    ))


# --------------------------------------------------------------------------
if __name__ == "__main__":
    build_home()
    build_bikes()
    for b in BIKES:
        build_product(b)
    build_about()
    build_support()
    build_shipping()
    build_warranty()
    build_contact()
    build_cart()
    build_checkout_confirmation()
    build_legal_terms()
    build_legal_privacy()
    build_legal_reservation()
    print("ALL PAGES BUILT")
