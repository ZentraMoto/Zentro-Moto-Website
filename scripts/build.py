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
            ("8 kW Electric Performance", "Up to 8 kW of peak power and 185 Nm of torque at the wheel for responsive acceleration."),
            ("Three Adjustable Riding Modes", "Three riding modes plus reverse allow the bike's response to be adjusted to the rider and conditions."),
            ("Removable 58V Battery", "The 58V/22Ah lithium-ion battery is removable, with an approximate 20–80% charging time of 2.5 hours."),
            ("Adjustable Suspension", "35 mm inverted front suspension with 170 mm travel and adjustable rebound and compression damping."),
            ("Rider Safety & Remote Control", "Remote power control, magnetic emergency shut-off and tilt protection provide additional rider-management features."),
        ],
    },
    {
        "id": "light-bee-x",
        "slug": "light-bee-x",
        "name": "Light Bee X",
        "url": "product-light-bee-x.html",
        "size": "Lightweight",
        "availability": "unconfirmed",
        "availability_label": "AVAILABILITY TO CONFIRM",
        "primary_action": "ENQUIRE NOW",
        "action_kind": "enquire",
        "one_liner": "Lightweight off-road performance with 10 kW of peak power and an agile 59 kg chassis.",
        "intro": "The MY26 Light Bee X builds on Surron's lightweight off-road platform with stronger performance and updated rider technology. A 10 kW power system, 295 Nm of rear-wheel torque and a 59 kg ready-to-ride weight keep it fast, agile and easy to control across off-road terrain.",
        "features": [
            ("10 kW Power System", "The latest electric powertrain delivers up to 10 kW of peak power and 295 Nm of rear-wheel torque for stronger, more responsive acceleration."),
            ("Lightweight 59 kg Chassis", "At just 59 kg ready to ride, the Light Bee X retains the lightweight, agile handling that has defined the platform."),
            ("72V Removable Battery", "The removable 72V / 35Ah lithium-ion battery provides up to 75 km of manufacturer-claimed range at 40 km/h, with approximately two-hour charging from 20–80%."),
            ("Adjustable Off-Road Suspension", "Fully adjustable KKE suspension provides 200 mm of front travel and 210 mm of rear wheel travel for controlled off-road performance."),
            ("Advanced Rider Technology", "Surron Wheelie Control, app connectivity, adjustable throttle response, regenerative braking and electronic rider-assistance features add greater control and customisation."),
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
            ("24 kW EVO-2 Power System", "The EVO-2 powertrain delivers up to 24 kW of peak power and 410 Nm of wheel torque for strong, responsive acceleration."),
            ("Semi-Solid-State Battery", "A 78.54V / 45Ah, 3.53 kWh battery delivers up to 108 km of manufacturer-claimed range at 40 km/h and approximately two-hour charging from 20–80%."),
            ("Seven Riding Modes", "E, D, S, M, T, R and L modes give the rider a wide range of control, including a customisable M mode."),
            ("Performance Suspension", "KKE suspension provides 240 mm of front and rear wheel travel for greater control across demanding off-road terrain."),
            ("Advanced Rider Control", "Surron Wheelie Control, Auto Hold, traction control and adjustable regenerative braking provide additional control across different riding conditions."),
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
            ("24.5 kW Next-Generation Power", "The latest Hairpin motor system delivers up to 24.5 kW of peak power and 520 Nm of torque for strong, responsive acceleration."),
            ("74V / 60Ah High-Performance Battery", "The removable 4.44 kWh lithium-ion battery provides manufacturer-claimed range of up to 115 km at 50 km/h, with approximately 2.5-hour charging from 20–80%."),
            ("Advanced Riding Modes & Traction Control", "Eco, Daily, Sports, Reverse, Turbo and Crawl modes are supported by adjustable traction control, regenerative braking and throttle response."),
            ("Performance Suspension & Brakes", "KKE suspension provides 240 mm of front and rear wheel travel, paired with four-piston hydraulic brakes and 240 mm wave discs."),
            ("Connected Rider Technology", "Surron App connectivity supports bike status monitoring, GPS information, parameter adjustment and over-the-air software updates, alongside Surron Wheelie Control."),
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

# Confirmed specification for the Hyper Bee only (see build_hyper_bee()).
# Rows follow the supplied spec sheet; no row is invented — anything not
# supplied (e.g. rear suspension) is simply omitted rather than shown as
# an unconfirmed placeholder.
HYPER_BEE_SPECS = [
    ("Motor", "Permanent Magnet Synchronous Motor"),
    ("Peak power", "8 kW"),
    ("Rated power", "4 kW"),
    ("Maximum torque", "185 Nm at wheel"),
    ("Top speed", "65 km/h"),
    ("Claimed range", "56 km at 40 km/h"),
    ("Battery", "Removable 58V / 22Ah lithium-ion"),
    ("Charging time", "Approx. 2.5 hours, 20–80%"),
    ("Riding modes", "1 / 2 / 3 / Reverse"),
    ("Weight", "39 kg"),
    ("Seat height", "Adjustable 665–705 mm"),
    ("Ground clearance", "240–260 mm"),
    ("Wheel size", "14&Prime; front / 12&Prime; rear"),
    ("Front suspension", "35 mm inverted fork, adjustable rebound &amp; compression, 170 mm travel"),
    ("Front brake", "Hydraulic disc"),
    ("Rear brake", "Hydraulic disc"),
    ("Dimensions", "1500 &times; 680 &times; 885 mm"),
    ("Carrying capacity", "65 kg"),
]

HYPER_BEE_PERFORMANCE = [
    ("8 kW", "Peak power"),
    ("65 km/h", "Top speed"),
    ("56 km", "Range @ 40 km/h"),
    ("39 kg", "Weight"),
    ("58V / 22Ah", "Removable battery"),
]

# Confirmed specification for the Light Bee X only (see build_light_bee_x()).
LIGHT_BEE_X_SPECS = [
    ("Motor", "Permanent Magnet Synchronous Motor (PMSM)"),
    ("Controller", "MTPA/MTPV FOC Sinewave Controller"),
    ("Peak power", "10 kW"),
    ("Maximum torque", "295 Nm"),
    ("Transmission", "Belt and chain, 1:7.6 ratio"),
    ("Throttle", "Ride-by-wire, 3-level adjustable"),
    ("Top speed", "80 km/h"),
    ("Maximum range", "75 km @ 40 km/h"),
    ("Riding modes", "Eco / Sport"),
    ("Battery", "72V / 35Ah removable lithium-ion, approx. 2.5 kWh"),
    ("Charging time", "Approx. 2 hours, 20&ndash;80%"),
    ("Display", "LCD multi-function display"),
    ("Front brake", "4-piston hydraulic / 203 mm vented disc"),
    ("Rear brake", "4-piston hydraulic / 203 mm vented disc"),
    ("Front suspension", "KKE inverted fork / 200 mm travel"),
    ("Rear suspension", "KKE rear shock / 210 mm wheel travel"),
    ("Front wheel/tyre", "70/100-19 CST off-road"),
    ("Rear wheel/tyre", "3.00-18 CST off-road"),
    ("Dimensions", "1850 &times; 780 &times; 1080 mm"),
    ("Wet weight", "59 kg"),
    ("Carrying capacity", "100 kg"),
    ("Wheelbase", "1255 mm"),
    ("Seat height", "830 mm"),
    ("Ground clearance", "270 mm"),
]

LIGHT_BEE_X_PERFORMANCE = [
    ("10 kW", "Peak power"),
    ("80 km/h", "Top speed"),
    ("75 km", "Range @ 40 km/h"),
    ("59 kg", "Wet weight"),
    ("72V / 35Ah", "Removable battery"),
]

# Confirmed specification for the Light Bee 2.0 only (see build_light_bee_2()).
LIGHT_BEE_2_SPECS = [
    ("Motor", "Hairpin motor"),
    ("Controller", "PMSM + MTPA/MTPV FOC Controller"),
    ("Peak power", "24 kW"),
    ("Maximum torque", "410 Nm"),
    ("Transmission", "Two-stage gear drive"),
    ("Throttle", "Ride-by-wire, 3-level adjustable"),
    ("Top speed", "90 km/h"),
    ("Maximum range", "160 km @ 25 km/h / 108 km @ 40 km/h"),
    ("Riding modes", "E / D / S / M / T / R / L"),
    ("Battery", "78.54V / 45Ah (3.53 kWh)"),
    ("Charging time", "Approx. 2 hours, 20&ndash;80%"),
    ("Battery life", "Up to 1,200+ charge cycles"),
    ("Display", "2.86-inch fully laminated TFT"),
    ("Front brake", "Opposed four-piston caliper / 220 mm disc"),
    ("Rear brake", "Opposed four-piston caliper / 203 mm disc"),
    ("Front suspension", "37 mm KKE inverted fork / 240 mm travel"),
    ("Rear suspension", "KKE rear shock / 240 mm wheel travel"),
    ("Front wheel/tyre", "70/100-19 CST off-road"),
    ("Rear wheel/tyre", "3.00-18 CST off-road"),
    ("Dimensions", "1900 &times; 790 &times; 1080 mm"),
    ("Wet weight", "65 kg"),
    ("Carrying capacity", "100 kg"),
    ("Wheelbase", "1280 mm"),
    ("Seat height", "830 mm"),
    ("Ground clearance", "280 mm"),
]

LIGHT_BEE_2_PERFORMANCE = [
    ("24 kW", "Peak power"),
    ("90 km/h", "Top speed"),
    ("108 km", "Range @ 40 km/h"),
    ("65 kg", "Wet weight"),
    ("78.54V / 45Ah", "Battery"),
]

# Confirmed specification for the Ultra Bee only (see build_ultra_bee()).
# Wheel/tyre configuration is genuinely unconfirmed (not invented) and is
# rendered with the same .spec-placeholder muted style the generic
# template uses for unconfirmed rows.
ULTRA_BEE_SPECS = [
    ("Motor", "Hairpin motor"),
    ("Controller", "MTPA/MTPV FOC Sinewave Controller"),
    ("Peak power", "24.5 kW"),
    ("Maximum torque", "520 Nm"),
    ("Transmission", "Belt and chain"),
    ("Throttle", "Ride-by-wire, 3-level adjustable"),
    ("Top speed", "95 km/h"),
    ("Maximum range", "115 km @ 50 km/h"),
    ("Riding modes", "Eco / Daily / Sports / Reverse / Turbo / Crawl"),
    ("Battery", "74V / 60Ah, 4,440 Wh removable lithium-ion"),
    ("Charging time", "Approx. 2.5 hours, 20&ndash;80%"),
    ("Battery life", "Up to 1,500+ charge cycles"),
    ("Display", "LCD multi-function display"),
    ("Front brake", "4-piston hydraulic / 240 mm wave disc"),
    ("Rear brake", "4-piston hydraulic / 240 mm wave disc"),
    ("Front suspension", "37 mm KKE inverted fork / 240 mm travel"),
    ("Rear suspension", "KKE rear shock / 240 mm wheel travel"),
    ("Front wheel/tyre", '<span class="spec-placeholder">TO CONFIRM</span>'),
    ("Rear wheel/tyre", '<span class="spec-placeholder">TO CONFIRM</span>'),
    ("Dimensions", "2010 &times; 850 &times; 1180 mm"),
    ("Wet weight", "Approx. 91&ndash;93 kg, variant dependent"),
    ("Carrying capacity", "100 kg"),
    ("Wheelbase", "1380 mm"),
    ("Seat height", "910 mm"),
    ("Ground clearance", "318 mm"),
]

ULTRA_BEE_PERFORMANCE = [
    ("24.5 kW", "Peak power"),
    ("95 km/h", "Top speed"),
    ("115 km", "Range @ 50 km/h"),
    ("520 Nm", "Max torque"),
    ("74V / 60Ah", "Removable battery"),
]

# Swatch colours for the paint colour selector on the product pages.
PAINT_COLOUR_HEX = {
    "Blue": "#2C4A78",
    "Yellow": "#E7B928",
    "Green": "#3E6B4A",
    "Brown": "#6B4A34",
    "Black": "#141414",
    "White": "#FFFFFF",
    "Purple": "#5B3F6B",
}


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


def header_html(active="", announce=None):
    links = []
    for label, url, key in NAV_ITEMS:
        current = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{url}"{current}>{label}</a>')
    nav = "\n        ".join(links)
    cart_current = ' aria-current="page"' if active == "cart" else ""
    announce_html = announce if announce is not None else 'Light Bee 2.0 now available to reserve — <a href="bikes.html">View bikes</a>'
    return f"""  <div class="announce">{announce_html}</div>
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


def footer_html(shipping_label="Shipping &amp; Collection", location_label="Newcastle, NSW"):
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
            <li><a href="product-light-bee-x.html">Light Bee X</a></li>
            <li><a href="product-light-bee-2.html">Light Bee 2.0</a></li>
            <li><a href="product-ultra-bee.html">Ultra Bee</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Support</h4>
          <ul>
            <li><a href="support.html">Support</a></li>
            <li><a href="shipping.html">{shipping_label}</a></li>
            <li><a href="warranty.html">Warranty &amp; Returns</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About Zentro Moto</a></li>
            <li><a href="about.html#location">{location_label}</a></li>
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


def page(title, description, active, body, body_class="", footer=None, header=None):
    cls = f' class="{body_class}"' if body_class else ""
    footer_block = footer if footer is not None else footer_html()
    header_block = header if header is not None else header_html(active)
    return f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
{head(title, description)}
</head>
<body{cls}>
  <a class="skip-link" href="#main">Skip to content</a>
{header_block}
  <main id="main">
{body}
  </main>
{footer_block}
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
        <p>Battery, controller, motor and frame.</p>
      </div>
      <div class="trust-item">
        <h3>OEM Parts Support</h3>
        <p>Genuine replacement and wear parts.</p>
      </div>
      <div class="trust-item">
        <h3>Australia-wide Delivery</h3>
        <p>Crated delivery available nationwide.</p>
      </div>
    </div>
  </section>"""


# Homepage-only bike card: a distinct, more editorial treatment than the
# bordered grid card used on the Bikes page and product cross-links (kept
# untouched via bike_card() above). Category labels and one-line
# descriptions here are homepage-specific per request.
HOME_SIZE_LABELS = {
    "hyper-bee": "Compact",
    "light-bee-x": "Lightweight",
    "light-bee-2": "Lightweight",
    "ultra-bee": "Full-Size",
}

HOME_ONE_LINERS = {
    "hyper-bee": "The compact, playful way into electric riding.",
    "light-bee-x": "Lightweight off-road performance with 10 kW of peak power and an agile 59 kg chassis.",
    "light-bee-2": "The versatile all-rounder for everyday riding.",
    "ultra-bee": "The full-size flagship for maximum performance.",
}


def home_bike_card(bike):
    # Uses the -profile shot (already 4:5) rather than the square -card
    # image, so object-fit: cover doesn't crop the baked-in placeholder
    # label text against this taller frame.
    return f"""        <article class="spotlight-card">
          <a class="spotlight-media" href="{bike['url']}">
            <img src="{img(bike['slug'] + '-profile')}" alt="{bike['name']} placeholder image" loading="lazy" />
          </a>
          <div class="spotlight-eyebrow">{HOME_SIZE_LABELS[bike['id']]}</div>
          <h3 class="spotlight-name">{bike['name']}</h3>
          <div class="spotlight-meta">
            {badge(bike)}
            <span class="spotlight-price">{PRICE_PLACEHOLDER}</span>
          </div>
          <p class="spotlight-desc">{HOME_ONE_LINERS[bike['id']]}</p>
          <a class="btn-link" href="{bike['url']}">VIEW {bike['name'].upper()}</a>
        </article>"""


# --------------------------------------------------------------------------
# 1. Home page
# --------------------------------------------------------------------------

def build_home():
    bikes_grid = "\n".join(home_bike_card(b) for b in BIKES)
    body = f"""    <!-- 03 Hero -->
    <section class="hero hero--home">
      <div class="hero-copy container">
        <span class="eyebrow">Genuine Surron &middot; Newcastle, NSW</span>
        <h1 class="h1">Genuine Surron. Straightforward buying.</h1>
        <p class="lede">Genuine Surron electric motorcycles, independently sourced and supplied in Australia.</p>
        <div class="hero-ctas">
          <a class="btn btn-primary btn-lg" href="bikes.html">SHOP BIKES</a>
          <a class="btn btn-secondary btn-lg" href="#how-it-works">HOW IT WORKS</a>
        </div>
      </div>
      <div class="hero-media">
        <img src="{img('home-hero-bleed')}" alt="Zentro Moto placeholder hero image" />
      </div>
    </section>

    <!-- 04 Trust strip -->
{trust_strip_html()}

    <!-- 05 The four bikes -->
    <section class="section container" id="bikes">
      <div class="section-head section-head--center">
        <h2 class="h2">Choose your Surron</h2>
        <p class="lede" style="margin:16px auto 0;">Four bikes. From compact electric fun to full-size performance.</p>
      </div>
      <div class="bike-grid bike-grid--4up">
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
          <div class="reason-card">
            <span class="reason-num">01</span>
            <h3>Genuine. Traceable. Properly sourced.</h3>
            <p>Genuine Surron motorcycles sourced directly from Surron in Shenzhen, with VIN identification, documented specifications, battery/DG paperwork and access to genuine OEM parts.</p>
          </div>
          <div class="reason-card">
            <span class="reason-num">02</span>
            <h3>Better value</h3>
            <p>By consolidating customer orders into supplier batches instead of holding large volumes of local stock, Zentro Moto keeps overheads lower and passes more of the savings directly on to customers.</p>
          </div>
          <div class="reason-card">
            <span class="reason-num">03</span>
            <h3>More choice</h3>
            <p>Choose the model and paint colour you actually want, rather than being limited to local showroom stock.</p>
          </div>
          <div class="reason-card">
            <span class="reason-num">04</span>
            <h3>Clear availability</h3>
            <p>Know whether each bike is in stock, incoming or available to order.</p>
          </div>
          <div class="reason-card">
            <span class="reason-num">05</span>
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
      <div class="timeline">
        <div class="timeline-step">
          <div class="timeline-num-wrap"><span class="timeline-num">01</span></div>
          <h3>Choose your bike</h3>
          <p>Pick the model and paint colour that suits you.</p>
        </div>
        <div class="timeline-step">
          <div class="timeline-num-wrap"><span class="timeline-num">02</span></div>
          <h3>Buy or reserve</h3>
          <p>Purchase an available bike or reserve an incoming / order-in bike.</p>
        </div>
        <div class="timeline-step">
          <div class="timeline-num-wrap"><span class="timeline-num">03</span></div>
          <h3>We handle the sourcing</h3>
          <p>We arrange sourcing and keep you updated.</p>
        </div>
        <div class="timeline-step">
          <div class="timeline-num-wrap"><span class="timeline-num">04</span></div>
          <h3>Receive your bike</h3>
          <p>Your bike is delivered Australia-wide in its crate.</p>
        </div>
      </div>
      <div style="margin-top:40px;">
        <a class="btn btn-primary" href="bikes.html">SHOP BIKES</a>
      </div>
    </section>

    <!-- 08 Delivery -->
    <section class="section section--black">
      <div class="container split">
        <div>
          <span class="eyebrow" style="color:rgba(255,255,255,0.6);">Delivery</span>
          <h2 class="h2">Australia-wide crated delivery.</h2>
          <p class="lede" style="color:rgba(255,255,255,0.75); margin:20px 0 28px;">Your bike is shipped securely in a crate to eligible locations across Australia.</p>
          <a class="btn btn-primary btn-on-black" href="shipping.html">SHIPPING INFORMATION</a>
        </div>
        <div class="split-media">
          <img src="{img('bikes-hero')}" alt="Australia-wide delivery placeholder image" />
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
          <div class="faq-body">Yes. Zentro Moto supplies genuine Surron motorcycles sourced directly from Surron in Shenzhen. Bikes have VIN identification, documented specifications and the required battery/DG documentation, giving customers clear traceability of what they are buying.</div>
        </details>
        <details class="faq-item">
          <summary>What warranty and support is included?<span class="faq-icon"></span></summary>
          <div class="faq-body">Bikes are supplied with a 12-month factory warranty covering core components including the battery, controller, motor and frame, subject to the applicable warranty terms and exclusions. Zentro Moto also provides access to genuine OEM replacement parts, common wear items and direct after-sales support.</div>
        </details>
        <details class="faq-item">
          <summary>Do you deliver Australia-wide?<span class="faq-icon"></span></summary>
          <div class="faq-body">Yes. Zentro Moto ships bikes securely in crates to eligible locations across Australia. Freight pricing and delivery details are provided during the ordering process.</div>
        </details>
        <details class="faq-item">
          <summary>Does the bike arrive assembled?<span class="faq-icon"></span></summary>
          <div class="faq-body">Bikes arrive approximately 90% assembled from Surron. Final assembly is typically limited to items such as fitting the handlebars, attaching the front wheel and installing the fender. Assembly requirements can vary slightly by model.</div>
        </details>
        <details class="faq-item">
          <summary>How does Zentro Moto keep prices lower than traditional dealerships?<span class="faq-icon"></span></summary>
          <div class="faq-body">Zentro Moto operates with a lean, low-overhead model. Rather than carrying large volumes of local stock and the cost base of a traditional dealership, customer orders are consolidated into supplier batches. This helps reduce overheads and allows us to pass more of the savings directly on to customers while still providing genuine Surron bikes, a 12-month factory warranty on core components, OEM parts support and Australia-wide delivery.</div>
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
        <p class="lede" style="margin:16px auto 32px;">Explore the Hyper Bee, Light Bee X, Light Bee 2.0 and Ultra Bee.</p>
        <a class="btn btn-primary btn-lg" href="bikes.html">SHOP BIKES</a>
      </div>
    </section>"""
    write("index.html", page(
        "Home",
        "Genuine Surron electric motorcycles, independently sourced and supplied in Australia. Hyper Bee, Light Bee X, Light Bee 2.0 and Ultra Bee — Newcastle, NSW.",
        "home", body,
        header=header_html("home", announce='Order before Sunday to secure your place in the next consolidated batch.<span class="countdown-badge" data-countdown></span>'),
    ))


# --------------------------------------------------------------------------
# 2. Bikes page
# --------------------------------------------------------------------------

def build_bikes():
    bikes_grid = "\n".join(bike_card(b) for b in BIKES)
    body = f"""    <section class="page-hero container">
      <span class="eyebrow">The range</span>
      <h1 class="h1">Find your Surron.</h1>
      <p class="lede" style="margin-top:16px;">Four bikes. From compact electric fun to full-size performance.</p>
    </section>
    <section class="section container">
      <div class="bike-grid bike-grid--4up">
{bikes_grid}
      </div>
    </section>"""
    write("bikes.html", page(
        "Bikes",
        "Hyper Bee, Light Bee X, Light Bee 2.0 and Ultra Bee — the complete Zentro Moto range of genuine Surron electric motorcycles.",
        "bikes", body,
    ))


# --------------------------------------------------------------------------
# 3. Product page template (used for all four bikes)
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


def batch_notice_html():
    """Shared weekly consolidated batch notice — used near the buy button on
    every product page so the wording and layout stay in sync."""
    return """          <div class="batch-notice">
            <p class="batch-notice-title">Next order cut-off: Sunday<span class="countdown-badge" data-countdown></span></p>
            <p class="batch-notice-body">Orders placed before Sunday are allocated to the next available consolidated supplier batch. Orders placed after the cut-off move into the following batch cycle.</p>
            <p class="batch-notice-body">Secure your place in the next batch before Sunday.</p>
            <p class="batch-notice-body">This low-overhead batch model helps Zentro Moto keep bike prices lower than a traditional dealership model.</p>
            <p class="batch-notice-delivery">Estimated delivery: 4&ndash;6 weeks.</p>
          </div>"""


def build_master_product(bike, *, category_label, short_description, performance, intro_heading, intro_body, specs, paint_colours,
                          assembly_body="Bikes are supplied crated and require assembly before use."):
    """Shared master template used by all four product pages (Hyper Bee,
    Light Bee X, Light Bee 2.0, Ultra Bee). Keeping this as one function —
    rather than separate hand-written builders per bike — is what
    guarantees the pages share the exact same width, section order,
    spacing and components; only the values passed in differ."""
    other_bikes = [b for b in BIKES if b["id"] != bike["id"]]

    def swatch_chip(colour):
        return f'<span class="swatch-chip" style="background:{PAINT_COLOUR_HEX[colour]};"></span>'

    if not paint_colours:
        # Colour range not yet confirmed by the supplier — show a plain
        # "to confirm" label instead of inventing swatches.
        default_colour = "To confirm"
        paint_colour_html = """          <div class="variant-block">
            <span class="variant-label">Paint colour &mdash; <span class="spec-placeholder">to confirm</span></span>
          </div>"""
    else:
        default_colour = paint_colours[0]
        if len(paint_colours) > 1:
            swatches_html = "\n".join(
                f'              <button type="button" class="swatch" aria-pressed="{"true" if i == 0 else "false"}">'
                f'{swatch_chip(colour)}<span class="swatch-name">{colour}</span></button>'
                for i, colour in enumerate(paint_colours)
            )
            paint_colour_html = f"""          <div class="variant-block" data-variant-group>
            <span class="variant-label">Paint colour</span>
            <div class="swatch-row">
{swatches_html}
            </div>
          </div>"""
        else:
            paint_colour_html = f"""          <div class="variant-block">
            <span class="variant-label">Paint colour</span>
            <div class="swatch-row">
              <span class="swatch is-selected">{swatch_chip(default_colour)}<span class="swatch-name">{default_colour}</span></span>
            </div>
          </div>"""

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

    perf_html = "\n".join(
        f"""          <div class="perf-item">
            <div class="perf-figure">{figure}</div>
            <div class="perf-label">{label}</div>
          </div>"""
        for figure, label in performance
    )

    spec_rows_html = "\n".join(
        f"""            <tr><th scope="row">{label}</th><td>{value}</td></tr>"""
        for label, value in specs
    )

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
          <span class="eyebrow">{category_label} &middot; Zentro Moto</span>
          <h1 class="h2">{bike['name']}</h1>
          {badge(bike)}
          <div class="buy-price">{PRICE_PLACEHOLDER}</div>
          <p class="buy-desc">{short_description}</p>
          <p class="text-sm" style="font-weight:700; margin-bottom:24px;">Off-road use only &middot; Not street legal</p>

{paint_colour_html}

          <div class="buy-actions">
            <button type="button" class="btn btn-primary btn-lg btn-block"
              data-action="add-to-cart"
              data-product-id="{bike['id']}"
              data-product-name="{bike['name']}"
              data-price="{PRICE_PLACEHOLDER}"
              data-image="{img(bike['slug'] + '-card')}"
              data-variant="{default_colour}">
              {bike['primary_action']}
            </button>
          </div>

{batch_notice_html()}

          <ul class="trust-notes">
            <li><span class="dot"></span> Genuine Surron &middot; Direct Shenzhen supply</li>
            <li><span class="dot"></span> 12-month factory warranty on core components</li>
            <li><span class="dot"></span> OEM parts support</li>
            <li><span class="dot"></span> Australia-wide crated delivery</li>
            <li><span class="dot"></span> Assembly required</li>
          </ul>
          <p class="trust-subline">VIN identified &middot; Documented specifications &middot; UN38.3 / battery documentation</p>
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

    <!-- Performance strip -->
    <section class="container" style="padding:0;">
      <div class="perf-strip">
{perf_html}
      </div>
    </section>

    <!-- Section 2: Short introduction -->
    <section class="section container" style="padding-bottom:0;">
      <p class="lede"><strong>{intro_heading}</strong></p>
      <p class="text-body" style="margin-top:12px;">{intro_body}</p>
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
        <p class="spec-note">Range, speed and charging figures are manufacturer-stated figures and can vary with rider weight, terrain, conditions and riding style.</p>
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
          <li><span class="dot"></span> Included factory accessories</li>
          <li><span class="dot"></span> Delivered crated &mdash; assembly required</li>
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
          <h3>Australia-wide crated delivery</h3>
          <p>Your {bike['name']} is shipped securely in a crate to eligible locations across Australia.</p>
        </div>
        <div class="info-col">
          <h3>Assembly required</h3>
          <p>{assembly_body}</p>
        </div>
        <div class="info-col">
          <h3>Support</h3>
          <p>Questions after purchase are handled directly through Zentro Moto.</p>
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


def build_hyper_bee():
    bike = next(b for b in BIKES if b["id"] == "hyper-bee")
    build_master_product(
        bike,
        category_label=bike["size"],
        short_description=bike["one_liner"],
        performance=HYPER_BEE_PERFORMANCE,
        intro_heading="Compact size. Serious performance.",
        intro_body="The Hyper Bee is Surron's compact off-road electric motorcycle, combining a lightweight 39 kg chassis with up to 8 kW of peak power. Adjustable riding modes, a removable battery and rider-assistance features make it suited to younger riders progressing from their first motorcycle through to more experienced off-road riding.",
        specs=HYPER_BEE_SPECS,
        paint_colours=["Blue", "Yellow", "Green"],
    )


def build_light_bee_x():
    bike = next(b for b in BIKES if b["id"] == "light-bee-x")
    build_master_product(
        bike,
        category_label="Lightweight",
        short_description="The iconic lightweight Surron, upgraded with stronger power, rider technology and off-road performance.",
        performance=LIGHT_BEE_X_PERFORMANCE,
        intro_heading="The Light Bee, evolved.",
        intro_body="The MY26 Light Bee X builds on Surron's lightweight off-road platform with stronger performance and updated rider technology. A 10 kW power system, 295 Nm of rear-wheel torque and a 59 kg ready-to-ride weight keep it fast, agile and easy to control across off-road terrain.",
        specs=LIGHT_BEE_X_SPECS,
        paint_colours=["White", "Purple", "Black", "Green"],
        assembly_body="Bikes arrive approximately 90% assembled from Surron. Final assembly typically includes fitting the handlebars, attaching the front wheel and installing items such as the fender.",
    )


def build_light_bee_2():
    bike = next(b for b in BIKES if b["id"] == "light-bee-2")
    build_master_product(
        bike,
        category_label="Lightweight",
        short_description="Next-generation lightweight electric performance, built for serious off-road riding.",
        performance=LIGHT_BEE_2_PERFORMANCE,
        intro_heading="Lightweight. Rebuilt for serious performance.",
        intro_body="The Light Bee 2.0 is a ground-up reinvention of Surron's lightweight off-road platform. With up to 24 kW of peak power, 410 Nm of wheel torque and a 65 kg chassis, it combines serious electric performance with the agile character the Light Bee is known for.",
        specs=LIGHT_BEE_2_SPECS,
        paint_colours=["Brown", "Black", "White", "Green"],
    )


def build_ultra_bee():
    bike = next(b for b in BIKES if b["id"] == "ultra-bee")
    build_master_product(
        bike,
        category_label="Full-Size",
        short_description="Full-size electric performance with serious power, suspension and rider technology.",
        performance=ULTRA_BEE_PERFORMANCE,
        intro_heading="Full-size power. Precise control.",
        intro_body="The Ultra Bee brings Surron's electric performance into a larger, more capable off-road platform. With up to 24.5 kW of peak power, 520 Nm of torque and advanced rider-control technology, it is built for riders wanting stronger performance, greater stability and serious off-road capability.",
        specs=ULTRA_BEE_SPECS,
        paint_colours=["Black"],
    )


# --------------------------------------------------------------------------
# 4. About page
# --------------------------------------------------------------------------

def build_about():
    body = f"""    <!-- 1. Hero — two column, reduced height -->
    <section class="section about-hero-section container">
      <div class="split">
        <div>
          <span class="eyebrow">About</span>
          <h1 class="h1">Zentro Moto</h1>
          <p class="lede" style="margin-top:16px;">A focused Australian retailer supplying genuine Surron electric motorcycles Australia-wide.</p>
        </div>
        <div class="split-media about-hero-media">
          <img src="{img('about-hero')}" alt="Zentro Moto placeholder image" />
        </div>
      </div>
    </section>

    <!-- 2. What we do + Why Zentro Moto — combined, grey -->
    <section class="section section--grey">
      <div class="container">
        <div class="about-combined">
          <div>
            <h2 class="h3">What we do</h2>
            <p class="text-body" style="margin-top:16px;">Zentro Moto independently supplies genuine Surron motorcycles sourced directly from Surron in Shenzhen, with VIN identification, documented specifications and the required battery/DG documentation.</p>
            <p class="text-body" style="margin-top:14px;">Our range is deliberately focused on the Hyper Bee, Light Bee X, Light Bee 2.0 and Ultra Bee.</p>
          </div>
          <div>
            <h2 class="h3">Why Zentro Moto</h2>
            <div class="about-benefits">
              <div class="about-benefit">
                <h3>Better value</h3>
                <p>A lean, low-overhead batch-order model lets us pass more of the savings directly on to customers.</p>
              </div>
              <div class="about-benefit">
                <h3>Direct, traceable supply</h3>
                <p>Genuine Surron motorcycles sourced directly from Surron in Shenzhen, with VIN identification, documented specifications and the required battery/DG documentation.</p>
              </div>
              <div class="about-benefit">
                <h3>More choice</h3>
                <p>Choose the model and paint colour you actually want rather than being limited to local showroom stock.</p>
              </div>
              <div class="about-benefit">
                <h3>Support after purchase</h3>
                <p>12-month factory warranty on core components, genuine OEM parts access and direct Zentro Moto support.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 3. Independent Australian retailer — secondary, full-width disclosure strip -->
    <section class="section section--tight about-disclosure">
      <div class="container">
        <h2 class="h4">Independent Australian retailer</h2>
        <p class="text-sm text-muted" style="max-width:60em; margin-top:10px;">Zentro Moto is independently owned and operated and is not an authorised distributor or representative of Surron. All motorcycles sold by Zentro Moto are genuine Surron products sourced through international wholesale channels.</p>
      </div>
    </section>

    <!-- 4. Australia-wide delivery — black feature section, larger image -->
    <section class="section section--black">
      <div class="container split about-delivery-split">
        <div>
          <span class="eyebrow" style="color:rgba(255,255,255,0.6);">Delivery</span>
          <h2 class="h2">Australia-wide crated delivery.</h2>
          <p class="lede" style="color:rgba(255,255,255,0.75); margin:20px 0 28px;">Every bike is shipped securely in a crate to eligible locations across Australia. Bikes are supplied crated and require assembly before use.</p>
          <a class="btn btn-primary btn-on-black" href="shipping.html">SHIPPING INFORMATION</a>
        </div>
        <div class="split-media">
          <img src="{img('about-delivery')}" alt="Australia-wide delivery placeholder image" />
        </div>
      </div>
    </section>

    <!-- 5. Business details — compact panel -->
    <section class="section section--tight container" id="business-details">
      <div class="section-head">
        <h2 class="h3">Business details</h2>
      </div>
      <div class="detail-panel">
        <div class="detail-grid">
          <div>
            <div class="detail-item-label">Based in</div>
            <div class="detail-item-value" id="location">Newcastle, NSW</div>
          </div>
          <div>
            <div class="detail-item-label">Delivery</div>
            <div class="detail-item-value">Australia-wide</div>
          </div>
          <div>
            <div class="detail-item-label">Business name</div>
            <div class="detail-item-value">Zentro Moto &mdash; BUSINESS NAME TO CONFIRM</div>
          </div>
          <div>
            <div class="detail-item-label">ABN</div>
            <div class="detail-item-value">ABN TO CONFIRM</div>
          </div>
        </div>
        <div style="margin-top:24px;">
          <a class="btn btn-primary" href="contact.html">CONTACT ZENTRO MOTO</a>
        </div>
      </div>
    </section>"""
    about_footer = footer_html(
        shipping_label="Shipping Information",
        location_label="Based in Newcastle, NSW &middot; Australia-wide delivery",
    )
    write("about.html", page(
        "About",
        "Zentro Moto is a focused Australian retailer supplying genuine Surron electric motorcycles Australia-wide.",
        "about", body,
        footer=about_footer,
    ))


# --------------------------------------------------------------------------
# 5. Support / FAQ page
# --------------------------------------------------------------------------

def faq(q, a, link=None):
    link_html = (
        f'<div style="margin-top:12px;"><a class="btn-link" href="{link[1]}">{link[0]}</a></div>'
        if link else ""
    )
    return f"""        <details class="faq-item">
          <summary>{q}<span class="faq-icon"></span></summary>
          <div class="faq-body">{a}{link_html}</div>
        </details>"""


def build_support():
    ordering = "\n".join([
        faq("What does “Incoming” mean?", "Incoming means the bike is part of a batch that has already been ordered from our supplier and is on its way to Zentro Moto. Where available, an estimated arrival timeframe will be shown on the product page."),
        faq("What does “Available to Order” mean?", "Available to Order means the bike is not currently held in stock or already incoming, but Zentro Moto can source it through our international wholesale supply network. Once your order is placed, we arrange sourcing and keep you updated throughout the process."),
        faq("How do reservations work?", "Some incoming or order-in bikes may be available to reserve with a deposit rather than full payment upfront. The deposit amount, remaining balance and relevant reservation terms will be clearly shown before you place the order.",
            link=("VIEW RESERVATION TERMS", "legal-reservation-terms.html")),
        faq("How does the weekly batch system work?", "Zentro Moto consolidates customer orders into supplier batches rather than holding large volumes of local stock. Orders placed before Sunday are allocated to the next available batch, while orders placed after the cut-off move into the following batch cycle. This leaner model helps reduce overheads and allows us to pass more of the savings directly on to customers. We&rsquo;ll keep you updated throughout the process, with the estimated delivery timeframe shown at the time of purchase."),
    ])
    delivery = "\n".join([
        faq("Do you deliver Australia-wide?", "Yes. Zentro Moto ships bikes securely in crates to eligible locations across Australia. Freight pricing and delivery details are provided during the ordering process.",
            link=("SHIPPING INFORMATION", "shipping.html")),
        faq("Does the bike arrive assembled?", "The bikes arrive approximately 90% assembled from Surron and are shipped securely in their crate. Final assembly is still required before riding, typically including fitting the handlebars, attaching the front wheel and installing items such as the front fender. Assembly requirements can vary slightly by model, so the bike should be correctly assembled and checked before use."),
        faq("Are the bikes road legal?", "No. The Hyper Bee, Light Bee X, Light Bee 2.0 and Ultra Bee sold by Zentro Moto are supplied for off-road use only and are not street legal."),
    ])
    warranty_support = "\n".join([
        faq("Are the bikes genuine Surron products?", "Yes. Zentro Moto supplies genuine Surron motorcycles sourced directly from Surron in Shenzhen, with VIN identification, documented specifications and the required battery/DG documentation."),
        faq("What warranty is included?", "Bikes are supplied with a 12-month factory warranty covering core components including the battery, controller, motor and frame, subject to the applicable warranty terms and exclusions. Your rights under Australian Consumer Law also continue to apply where applicable.",
            link=("WARRANTY & RETURNS", "warranty.html")),
        faq("Can I get spare parts and support after purchase?", "Yes. Zentro Moto supplies genuine OEM replacement parts, common wear-and-tear items and selected performance upgrades. If you need assistance after purchase, contact Zentro Moto directly."),
    ])

    body = f"""    <section class="page-hero container">
      <span class="eyebrow">Help centre</span>
      <h1 class="h1">Support &amp; FAQ</h1>
      <p class="lede" style="margin-top:16px;">Answers to the most common questions about ordering, delivery, warranty and owning your Zentro Moto bike.</p>
    </section>

    <section class="section container">
      <div class="narrow-content">
        <div class="faq-category">
          <h3>Ordering</h3>
          <div class="faq-list">{ordering}
          </div>
        </div>
        <div class="faq-category">
          <h3>Delivery &amp; Your Bike</h3>
          <div class="faq-list">{delivery}
          </div>
        </div>
        <div class="faq-category">
          <h3>Warranty &amp; Support</h3>
          <div class="faq-list">{warranty_support}
          </div>
        </div>
      </div>
    </section>

    <section class="section section--grey">
      <div class="container section-head--center">
        <h2 class="h3">Still have a question?</h2>
        <p class="text-body" style="margin:12px auto 0;">Contact Zentro Moto and we&rsquo;ll help with your bike, order or support enquiry.</p>
        <div style="margin-top:24px;">
          <a class="btn btn-primary" href="contact.html">CONTACT ZENTRO MOTO</a>
        </div>
      </div>
    </section>"""
    write("support.html", page(
        "Support & FAQ",
        "Answers to the most common questions about ordering, delivery, warranty and owning your Zentro Moto bike.",
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
                <option>Light Bee X</option>
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
    build_hyper_bee()
    build_light_bee_x()
    build_light_bee_2()
    build_ultra_bee()
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
