#!/usr/bin/env python3
"""Generates clean, obviously-placeholder SVG imagery for the Zentro Moto prototype.
Deliberately abstract line-art (not photoreal / not AI-image-style) so it reads as a
placeholder to be swapped for licensed photography, per the brief."""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets/img/placeholders")
os.makedirs(OUT, exist_ok=True)

BIKE_PATH = """
M120,300
m-58,0 a58,58 0 1,0 116,0 a58,58 0 1,0 -116,0
M470,300
m-58,0 a58,58 0 1,0 116,0 a58,58 0 1,0 -116,0
M120,300 L230,190 L340,190
M230,190 L300,300
M300,300 L470,300
M300,300 L250,150
M250,150 L340,150
L365,110 L430,110
M340,190 L400,120
M120,300 L170,255
M170,255 L230,255
"""

def svg(model, shot, w, h, big=False, watermark_size=42, id_suffix="", border=True):
    scale = min(w, h) / 620
    stroke = 2.4 if not big else 3.2
    cx, cy = w * 0.62, h * 0.52
    tx = w * 0.08
    ty_label = h - 46
    ty_model = h - 78
    tag_y = 34
    border_rect = f'<rect x="0.75" y="0.75" width="{w-1.5}" height="{h-1.5}" fill="none" stroke="#D8D6CF" stroke-width="1.5"/>' if border else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{model} placeholder image, {shot}">
  <rect width="{w}" height="{h}" fill="#EEEDE9"/>
  {border_rect}
  <g transform="translate({cx - 300*scale},{cy - 300*scale}) scale({scale})">
    <path d="{BIKE_PATH}" fill="none" stroke="#B9B7AE" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
  <text x="{tx}" y="{tag_y}" font-family="Arial, Helvetica, sans-serif" font-size="12" letter-spacing="2" fill="#8A8880">PLACEHOLDER IMAGE</text>
  <line x1="{tx}" y1="{tag_y+10}" x2="{tx+150}" y2="{tag_y+10}" stroke="#D8D6CF" stroke-width="1"/>
  <text x="{tx}" y="{ty_model}" font-family="Arial, Helvetica, sans-serif" font-weight="700" font-size="{28 if big else 22}" letter-spacing="1" fill="#1A1A18">{model.upper()}</text>
  <text x="{tx}" y="{ty_label}" font-family="Arial, Helvetica, sans-serif" font-size="13" letter-spacing="2" fill="#8A8880">{shot.upper()}</text>
</svg>'''

MODELS = ["Hyper Bee", "Light Bee 2.0", "Ultra Bee"]
SHOTS = [
    ("profile", "Full Profile"),
    ("front-3-4", "Front 3/4"),
    ("rear", "Rear"),
    ("cockpit", "Cockpit"),
    ("suspension-brakes", "Suspension & Brakes"),
    ("motor", "Motor"),
    ("battery", "Battery"),
]

# Must match the "slug" field for each bike in scripts/build.py's BIKES list.
MODEL_SLUGS = {
    "Hyper Bee": "hyper-bee",
    "Light Bee 2.0": "light-bee-2",
    "Ultra Bee": "ultra-bee",
}

def slug(m):
    return MODEL_SLUGS[m]

for model in MODELS:
    s = slug(model)
    for key, label in SHOTS:
        content = svg(model, label, 1000, 1250)
        with open(f"{OUT}/{s}-{key}.svg", "w") as f:
            f.write(content)
    # square card image (home/bikes listing)
    with open(f"{OUT}/{s}-card.svg", "w") as f:
        f.write(svg(model, "Full Profile", 1000, 1000))
    # wide hero image for product page
    with open(f"{OUT}/{s}-hero-wide.svg", "w") as f:
        f.write(svg(model, "Hero", 1600, 1000, big=True))

# Homepage hero (generic - shows the lineup, not one specific bike)
with open(f"{OUT}/home-hero.svg", "w") as f:
    f.write(svg("Zentro Moto", "Homepage Hero", 1920, 1200, big=True))

# Homepage hero, full-bleed variant: borderless and sized to cover both the
# wide desktop crop and the taller mobile crop via object-fit: cover.
with open(f"{OUT}/home-hero-bleed.svg", "w") as f:
    f.write(svg("Zentro Moto", "Homepage Hero", 2400, 1400, big=True, border=False))

# Bikes page hero
with open(f"{OUT}/bikes-hero.svg", "w") as f:
    f.write(svg("Zentro Moto", "Bikes Hero", 1920, 900, big=True))

print("done", len(os.listdir(OUT)), "files")
