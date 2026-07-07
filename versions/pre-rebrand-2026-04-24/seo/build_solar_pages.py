#!/usr/bin/env python3
"""
Nexsun.ai Programmatic SEO Builder
Generates solar/[city].html pages from template + city data.

Usage:
    python3 build_solar_pages.py              # Generate all 50 pages
    python3 build_solar_pages.py toronto      # Generate single city
    python3 build_solar_pages.py --sitemap    # Regenerate sitemap only

Output: /nexsun/solar/*.html + updated sitemap.xml
"""

import csv
import os
import sys
import math
import hashlib
from datetime import datetime
from pathlib import Path

# ── Paths ──
SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent
TEMPLATE_PATH = SCRIPT_DIR / "solar-city-template.html"
CSV_PATH = SCRIPT_DIR / "cities.csv"
OUTPUT_DIR = ROOT_DIR / "solar"
SITEMAP_PATH = ROOT_DIR / "sitemap.xml"
HUB_PATH = ROOT_DIR / "solar.html"


def load_cities():
    """Load city data from CSV."""
    cities = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cities.append(row)
    return cities


def load_template():
    """Load HTML template."""
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def find_nearby_cities(target_slug, cities, max_nearby=6):
    """Find nearby cities in the same province, then fill with others."""
    target = None
    for c in cities:
        if c["slug"] == target_slug:
            target = c
            break
    if not target:
        return []

    # Same province first
    same_province = [c for c in cities if c["province"] == target["province"] and c["slug"] != target_slug]
    # Then other provinces
    other_province = [c for c in cities if c["province"] != target["province"]]

    nearby = same_province[:4] + other_province[:max_nearby - min(len(same_province), 4)]
    return nearby[:max_nearby]


def generate_nearby_links(nearby_cities):
    """Generate HTML links for nearby cities."""
    if not nearby_cities:
        return '<p style="color:var(--text-muted);">More city pages coming soon.</p>'

    links = []
    for c in nearby_cities:
        links.append(
            f'<a href="{c["slug"]}.html" class="nearby-link">'
            f'<span class="nearby-city">{c["city"]}</span>'
            f'<span class="nearby-province">{c["province"]}</span>'
            f'<span class="nearby-stat">{c["solar_irradiance"]} kWh/m\u00b2 &middot; {c["avg_sun_hours"]} hrs/day</span>'
            f'</a>'
        )
    return "\n            ".join(links)


def generate_content_body(city_data):
    """
    Generate unique, SEO-rich content body for each city.
    Uses city-specific data to produce genuinely different paragraphs.
    No em dashes, per brand rules.
    """
    city = city_data["city"]
    province = city_data["province"]
    province_abbr = city_data["province_abbr"]
    population = int(city_data["population"])
    irradiance = city_data["solar_irradiance"]
    sun_hours = city_data["avg_sun_hours"]
    elec_rate = city_data["avg_electricity_rate"]
    incentive = city_data["incentive_program"]
    incentive_detail = city_data["incentive_detail"]
    climate = city_data["climate_zone"]
    system_cost = city_data["avg_system_cost"]
    annual_savings = city_data["avg_annual_savings"]
    payback = city_data["payback_years"]
    slug = city_data["slug"]

    pop_formatted = f"{population:,}"

    # Determine solar tier description
    irr_val = int(irradiance)
    if irr_val >= 1350:
        solar_tier = "one of Canada's top-tier solar markets"
        solar_adj = "exceptional"
    elif irr_val >= 1250:
        solar_tier = "a strong solar market with above-average irradiance"
        solar_adj = "strong"
    elif irr_val >= 1150:
        solar_tier = "a solid solar candidate with moderate irradiance"
        solar_adj = "moderate"
    else:
        solar_tier = "an emerging solar market with improving economics"
        solar_adj = "growing"

    # Determine payback description
    payback_val = int(payback)
    if payback_val <= 11:
        payback_desc = "among the fastest payback periods in Canada"
        roi_desc = "excellent"
    elif payback_val <= 14:
        payback_desc = "a competitive payback period for Canadian solar"
        roi_desc = "strong"
    elif payback_val <= 18:
        payback_desc = "a reasonable payback period supported by available incentives"
        roi_desc = "moderate"
    else:
        payback_desc = "a longer payback period, though rising electricity costs and improving panel efficiency continue to shift the equation"
        roi_desc = "evolving"

    # Climate-specific content
    climate_content = {
        "Humid Continental": f"{city}'s humid continental climate brings warm summers and cold winters. Solar panels actually perform better in cooler temperatures, meaning {city}'s cold, clear winter days can generate surprisingly strong output. Summer months deliver peak generation with long daylight hours extending past 9 PM in June and July.",
        "Oceanic": f"{city}'s oceanic climate features milder temperatures year-round compared to inland cities. While cloud cover is common, modern solar panels generate electricity even on overcast days. The moderate temperatures prevent the efficiency losses that extreme heat causes in other markets, and long summer days provide extended generation windows.",
        "Semi-Arid": f"{city}'s semi-arid climate is a significant advantage for solar generation. Low humidity means clearer skies and more direct sunlight hitting panels throughout the year. Combined with minimal cloud cover and the naturally cooler temperatures at this altitude, solar panels in {city} operate near peak efficiency for much of the year.",
        "Subarctic": f"While {city}'s northern location means shorter winter days, the summer months more than compensate with extremely long daylight hours. During peak summer, {city} can receive over 17 hours of daylight, driving strong seasonal solar generation. Modern battery storage solutions help bridge the shorter winter production periods.",
    }

    climate_text = climate_content.get(climate, f"{city}'s climate supports productive solar generation across the seasons, with peak output during the longer summer months.")

    # Electricity market context by province
    elec_rate_val = float(elec_rate)
    if elec_rate_val >= 16:
        rate_context = f"At {elec_rate}\u00a2/kWh, {province}'s electricity rates are among the highest in Canada, making solar an especially compelling way to reduce energy costs."
    elif elec_rate_val >= 12:
        rate_context = f"With electricity priced at {elec_rate}\u00a2/kWh, {city} homeowners face meaningful energy costs that solar can significantly offset."
    elif elec_rate_val >= 9:
        rate_context = f"{province}'s electricity rate of {elec_rate}\u00a2/kWh is moderate by Canadian standards. As rates continue to rise, early solar adopters stand to benefit from locked-in energy production costs."
    else:
        rate_context = f"{province}'s low electricity rate of {elec_rate}\u00a2/kWh means solar payback takes longer, but rising provincial energy costs and the hedge against future rate increases make solar a strategic long-term investment."

    # Unique seed-based paragraph variations using hash
    seed = int(hashlib.md5(slug.encode()).hexdigest()[:8], 16) % 5

    opening_variants = [
        f"{city}, {province} is positioning itself as {solar_tier}. With a population of {pop_formatted} and annual solar irradiance of {irradiance} kWh/m\u00b2, the city offers {solar_adj} conditions for residential and commercial solar installations.",
        f"Homeowners in {city}, {province} are discovering that solar energy is not just viable, it is financially compelling. The city's {irradiance} kWh/m\u00b2 annual irradiance and {sun_hours} peak sun hours per day create {solar_adj} conditions for rooftop solar systems.",
        f"With {pop_formatted} residents and growing, {city} represents one of {province}'s most dynamic solar energy markets. Annual irradiance levels of {irradiance} kWh/m\u00b2 put the city firmly in the {solar_adj} range for Canadian solar generation.",
        f"Solar energy adoption is accelerating in {city}, {province}, driven by {solar_adj} irradiance levels of {irradiance} kWh/m\u00b2 per year and increasing awareness of energy independence benefits. The city's {pop_formatted} residents have access to some of the best solar economics in the region.",
        f"For the {pop_formatted} residents of {city}, {province}, solar energy represents an increasingly attractive path to energy independence. With {irradiance} kWh/m\u00b2 of annual solar irradiance and {sun_hours} peak sun hours daily, the fundamentals are {solar_adj}.",
    ]

    cost_variants = [
        f"A typical 10 kW residential solar system in {city} costs approximately ${int(system_cost):,}, with the potential to generate around ${int(annual_savings):,} in annual electricity savings. That translates to {payback_desc}.",
        f"The economics are straightforward: a 10 kW system in {city} runs approximately ${int(system_cost):,} before incentives. With estimated annual savings of ${int(annual_savings):,}, homeowners can expect {payback_desc}.",
        f"Installation costs in {city} average around ${int(system_cost):,} for a standard 10 kW residential system. At ${int(annual_savings):,} in projected annual savings, that represents {payback_desc}.",
        f"For a 10 kW system, {city} homeowners should budget approximately ${int(system_cost):,}. The estimated annual savings of ${int(annual_savings):,} deliver {payback_desc}, making the long-term financial case {roi_desc}.",
        f"Current market pricing puts a 10 kW solar installation in {city} at roughly ${int(system_cost):,}. With annual savings estimated at ${int(annual_savings):,} and {payback_desc}, the investment thesis is clear.",
    ]

    nexsun_variants = [
        f"Nexsun.ai's decision intelligence platform analyzes solar potential at the property level, incorporating {city}'s specific irradiance data, local utility rate structures, available incentive programs, and projected energy cost trajectories. Rather than relying on generic estimates, Nexsun.ai delivers data-driven recommendations tailored to each homeowner's unique situation.",
        f"This is where Nexsun.ai's platform delivers exceptional value. By modeling {city}'s specific solar conditions, electricity pricing, and incentive landscape, Nexsun.ai provides homeowners with a precise, transparent view of their solar investment potential. The platform's Glassbox AI explains every recommendation, so decisions are always clear and auditable.",
        f"Nexsun.ai brings enterprise-grade decision intelligence to {city}'s solar market. The platform models property-specific solar potential using {city}'s irradiance data, roof orientation analysis, local rate structures, and the full landscape of available incentives. Every recommendation is explainable and auditable through Nexsun.ai's Glassbox AI approach.",
        f"What sets Nexsun.ai apart in the {city} market is the depth of its analysis. The platform factors in {province}'s specific rate structures, {incentive} eligibility, roof geometry, shading analysis, and 25-year energy cost projections. All of this is delivered through an explainable AI framework that shows its reasoning at every step.",
        f"Nexsun.ai's platform is purpose-built for this kind of decision. For {city} homeowners evaluating solar, it models the full financial picture: {province} electricity rates, {incentive} incentive eligibility, projected rate increases, system degradation curves, and financing options. The AI is fully transparent, showing exactly why it recommends what it does.",
    ]

    body = f"""
        <h2>Solar Energy Landscape in {city}</h2>
        <p>{opening_variants[seed]}</p>

        <h3>Climate and Solar Performance</h3>
        <p>{climate_text}</p>

        <h3>Electricity Costs and Savings Potential</h3>
        <p>{rate_context}</p>
        <p>{cost_variants[(seed + 1) % 5]}</p>

        <h3>Incentives and Programs in {province}</h3>
        <p>{city} homeowners have access to the <strong>{incentive}</strong>. {incentive_detail}</p>
        <p>Federal programs, including the Canada Greener Homes Grant, may provide additional rebates for qualifying installations. Nexsun.ai's platform tracks all available programs to ensure homeowners capture maximum value.</p>

        <h3>Making Data-Driven Solar Decisions</h3>
        <p>{nexsun_variants[(seed + 2) % 5]}</p>
        <p>Whether you are a homeowner evaluating a rooftop system, a developer planning a commercial installation, or a municipal planner assessing community solar potential, Nexsun.ai provides the analytical foundation for confident decisions.</p>
    """

    return body


def build_page(city_data, template, all_cities):
    """Build a single city page."""
    nearby = find_nearby_cities(city_data["slug"], all_cities)
    nearby_html = generate_nearby_links(nearby)
    content_body = generate_content_body(city_data)

    page = template
    replacements = {
        "{{CITY}}": city_data["city"],
        "{{PROVINCE}}": city_data["province"],
        "{{CITY_SLUG}}": city_data["slug"],
        "{{SOLAR_IRRADIANCE}}": city_data["solar_irradiance"],
        "{{AVG_SUN_HOURS}}": city_data["avg_sun_hours"],
        "{{AVG_ELECTRICITY_RATE}}": city_data["avg_electricity_rate"],
        "{{PAYBACK_YEARS}}": city_data["payback_years"],
        "{{INCENTIVE_PROGRAM}}": city_data["incentive_program"],
        "{{INCENTIVE_DETAIL}}": city_data["incentive_detail"],
        "{{CONTENT_BODY}}": content_body,
        "{{NEARBY_CITIES_LINKS}}": nearby_html,
    }

    for placeholder, value in replacements.items():
        page = page.replace(placeholder, value)

    return page


def generate_hub_page(cities):
    """Generate the solar hub page (solar.html) linking to all city pages."""
    # Group cities by province
    provinces = {}
    for c in cities:
        prov = c["province"]
        if prov not in provinces:
            provinces[prov] = []
        provinces[prov].append(c)

    # Sort provinces by number of cities (most first)
    sorted_provinces = sorted(provinces.items(), key=lambda x: -len(x[1]))

    province_sections = []
    for prov_name, prov_cities in sorted_provinces:
        prov_cities_sorted = sorted(prov_cities, key=lambda x: -int(x["population"]))
        city_cards = []
        for c in prov_cities_sorted:
            city_cards.append(f'''
          <a href="solar/{c["slug"]}.html" class="hub-city-card">
            <h4>{c["city"]}</h4>
            <div class="hub-stats">
              <span>{c["solar_irradiance"]} kWh/m&sup2;</span>
              <span>{c["avg_sun_hours"]} hrs/day</span>
              <span>{c["payback_years"]}yr payback</span>
            </div>
          </a>''')

        province_sections.append(f'''
      <div class="hub-province">
        <h3>{prov_name} <span class="hub-count">({len(prov_cities)} cities)</span></h3>
        <div class="hub-city-grid">
          {"".join(city_cards)}
        </div>
      </div>''')

    hub_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Solar Energy Across Canada | City-by-City Solar Guide | Nexsun.ai</title>
  <meta name="description" content="Explore solar energy potential in 50+ Canadian cities. Compare solar irradiance, costs, incentives, and ROI by city and province. Powered by Nexsun.ai decision intelligence.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://nexsun.ai/solar.html">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Solar Energy Across Canada | Nexsun.ai">
  <meta property="og:description" content="City-by-city solar guide for Canada. Compare costs, incentives, and ROI across 50+ cities.">
  <meta property="og:url" content="https://nexsun.ai/solar.html">
  <meta property="og:image" content="https://nexsun.ai/og-solar-hub.jpg">
  <meta property="og:site_name" content="Nexsun.ai">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Solar Energy Across Canada | Nexsun.ai">
  <meta name="twitter:description" content="City-by-city solar guide for Canada. Compare costs, incentives, and ROI across 50+ cities.">
  <meta name="twitter:image" content="https://nexsun.ai/og-solar-hub.jpg">
  <style>
    :root {{
      --navy:#1E3A8A; --sun:#F59E0B; --sun-deep:#D97706; --sun-pale:#FEF3C7;
      --logo-green:#22C55E; --bg:#FFFBF0; --text:#0F172A; --text-mid:#334155;
      --text-muted:#64748B; --border:rgba(245,158,11,0.2); --white:#FFFFFF;
    }}
    * {{ margin:0; padding:0; box-sizing:border-box; }}
    html {{ scroll-behavior:smooth; }}
    body {{ background:var(--bg); color:var(--text); font-family:'Segoe UI',system-ui,-apple-system,sans-serif; overflow-x:hidden; }}
    a {{ color:inherit; text-decoration:none; }}
    .container {{ max-width:1200px; margin:0 auto; padding:0 32px; }}

    /* ── Topbar ── */
    .topbar {{ background:var(--navy); }}
    .topbar-inner {{
      max-width:1200px; margin:0 auto; padding:0 32px;
      display:flex; align-items:center; justify-content:flex-end;
      height:34px;
    }}
    .topbar-inner a {{
      font-size:11px; font-weight:700; letter-spacing:1.2px; text-transform:uppercase;
      color:var(--sun); padding:0 16px; transition:color .2s;
      border-right:1px solid rgba(255,255,255,0.1); line-height:34px;
    }}
    .topbar-inner a:last-child {{ border-right:none; padding-right:0; }}
    .topbar-inner a:hover {{ color:#fff; }}

    /* ── Nav ── */
    nav {{
      position:sticky; top:0; z-index:100;
      background:rgba(255,251,240,0.88); backdrop-filter:blur(16px);
      border-bottom:1px solid rgba(245,158,11,0.15);
      box-shadow:0 1px 20px rgba(245,158,11,0.08);
    }}
    .nav-inner {{ max-width:1200px; margin:0 auto; padding:0 32px; display:flex; align-items:center; height:70px; }}
    .nav-links {{ display:flex; align-items:center; gap:32px; margin-left:auto; }}
    .nav-links a {{ font-size:14px; color:var(--text-mid); font-weight:500; transition:color .2s; }}
    .nav-links a:hover {{ color:var(--sun-deep); }}
    .btn-cta {{
      background:linear-gradient(135deg,var(--sun),var(--sun-deep));
      color:#fff; font-weight:700; padding:11px 24px; border-radius:8px;
      font-size:14px; border:none; cursor:pointer; transition:all .2s;
      box-shadow:0 4px 14px rgba(245,158,11,0.4); display:inline-block;
    }}
    .btn-cta:hover {{ transform:translateY(-2px); box-shadow:0 6px 20px rgba(245,158,11,0.5); }}
    .nav-dropdown {{ position:relative; }}
    .nav-dropdown-menu {{
      display:none; position:absolute; top:100%; left:0; min-width:200px;
      background:white; border-radius:10px; box-shadow:0 8px 30px rgba(0,0,0,0.12);
      padding:10px 0; z-index:200;
    }}
    .nav-dropdown:hover .nav-dropdown-menu {{ display:block; }}
    .nav-dropdown-menu a {{ display:block; padding:8px 20px; font-size:13px; color:var(--text-mid); }}
    .nav-dropdown-menu a:hover {{ background:var(--sun-pale); color:var(--sun-deep); }}
    .menu-divider {{ height:1px; background:var(--border); margin:6px 16px; }}

    /* ── Hero ── */
    .hub-hero {{
      padding:140px 0 80px;
      background:linear-gradient(160deg, #FFFBF0 0%, #FFF3CD 30%, #E0F2FE 60%, #FEF9C3 100%);
      text-align:center;
    }}
    .hub-hero h1 {{
      font-size:clamp(36px,5vw,60px); font-weight:900; color:var(--navy); line-height:1.1; margin-bottom:20px;
    }}
    .hub-hero h1 span {{ color:var(--sun-deep); }}
    .hub-hero p {{ font-size:18px; color:var(--text-mid); max-width:700px; margin:0 auto; line-height:1.7; }}
    .hub-hero .hub-stat-row {{
      display:flex; justify-content:center; gap:48px; margin-top:40px; flex-wrap:wrap;
    }}
    .hub-hero .hub-stat-item .val {{ font-size:32px; font-weight:900; color:var(--navy); }}
    .hub-hero .hub-stat-item .lbl {{ font-size:13px; color:var(--text-muted); margin-top:4px; }}

    /* ── Province Sections ── */
    .hub-provinces {{ padding:80px 0; }}
    .hub-province {{ margin-bottom:48px; }}
    .hub-province h3 {{
      font-size:24px; font-weight:800; color:var(--navy); margin-bottom:20px;
      padding-bottom:12px; border-bottom:2px solid var(--border);
    }}
    .hub-count {{ font-size:14px; font-weight:500; color:var(--text-muted); }}
    .hub-city-grid {{
      display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:16px;
    }}
    .hub-city-card {{
      background:white; border:1px solid var(--border); border-radius:12px;
      padding:20px 24px; transition:all .2s; display:block;
    }}
    .hub-city-card:hover {{
      border-color:var(--sun); box-shadow:0 4px 20px rgba(245,158,11,0.15);
      transform:translateY(-2px);
    }}
    .hub-city-card h4 {{ font-size:17px; font-weight:700; color:var(--navy); margin-bottom:8px; }}
    .hub-stats {{
      display:flex; gap:12px; flex-wrap:wrap;
    }}
    .hub-stats span {{
      font-size:12px; color:var(--text-muted); background:var(--sun-pale);
      padding:3px 10px; border-radius:20px; white-space:nowrap;
    }}

    /* ── CTA ── */
    .hub-cta {{
      background:var(--navy); padding:80px 0; text-align:center; color:white;
    }}
    .hub-cta h2 {{ font-size:32px; font-weight:800; margin-bottom:16px; }}
    .hub-cta p {{ font-size:17px; opacity:0.85; margin-bottom:32px; max-width:600px; margin-left:auto; margin-right:auto; }}

    /* ── Footer ── */
    footer {{
      background:var(--navy); padding:60px 0 30px; color:rgba(255,255,255,0.7); font-size:13px;
    }}
    .footer-top {{ display:grid; grid-template-columns:repeat(4,1fr); gap:32px; margin-bottom:48px; }}
    .footer-col h4 {{ color:var(--sun); font-size:13px; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:16px; }}
    .footer-col ul {{ list-style:none; }}
    .footer-col li {{ margin-bottom:8px; }}
    .footer-col a {{ color:rgba(255,255,255,0.7); transition:color .2s; }}
    .footer-col a:hover {{ color:white; }}
    .footer-bottom {{
      border-top:1px solid rgba(255,255,255,0.1); padding-top:20px;
      display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;
    }}
    .footer-legal {{ display:flex; gap:24px; }}
    .footer-legal a {{ color:rgba(255,255,255,0.75); transition:color .2s; }}
    .footer-legal a:hover {{ color:white; }}

    /* ── Mobile ── */
    @media(max-width:768px) {{
      .topbar-inner {{ flex-wrap:wrap; height:auto; padding:6px 16px; justify-content:center; gap:8px; }}
      .topbar-inner a {{ border-right:none; padding:2px 8px; font-size:10px; }}
      .nav-inner {{ padding:0 16px; height:60px; }}
      .nav-links {{ display:none; }}
      .hub-hero {{ padding:100px 16px 60px; }}
      .hub-hero .hub-stat-row {{ gap:24px; }}
      .hub-hero .hub-stat-item .val {{ font-size:24px; }}
      .hub-provinces {{ padding:40px 0; }}
      .hub-city-grid {{ grid-template-columns:1fr; }}
      .footer-top {{ grid-template-columns:1fr 1fr; gap:24px; }}
      .footer-bottom {{ flex-direction:column; text-align:center; }}
      .container {{ padding:0 16px; }}
    }}
    @media(max-width:480px) {{
      .hub-hero h1 {{ font-size:28px; }}
      .hub-hero .hub-stat-row {{ flex-direction:column; gap:16px; }}
      .footer-top {{ grid-template-columns:1fr; }}
    }}
  </style>
</head>
<body>

<nav>
  <div class="topbar">
    <div class="topbar-inner">
      <a href="https://AEPG.ca" target="_blank" rel="noopener noreferrer">AEPG.ca</a>
      <a href="blog.html">Resources</a>
      <a href="investors.html">Investor Centre</a>
      <a href="partners.html">Partner Centre</a>
      <a href="trust.html">Trust Centre</a>
      <a href="contact.html">Contact Us</a>
    </div>
  </div>
  <div class="nav-inner">
    <a href="index.html">
      <img src="logo-color.svg" alt="Nexsun.ai" style="height:120px;width:auto;display:block;">
    </a>
    <div class="nav-links">
      <div class="nav-dropdown">
        <a href="platform.html">Platform</a>
        <div class="nav-dropdown-menu">
          <a href="platform.html">Platform Overview</a>
          <div class="menu-divider"></div>
          <a href="modules.html">Modules</a>
          <a href="technology.html">Technology</a>
          <div class="menu-divider"></div>
          <a href="trust.html">Trust Centre</a>
        </div>
      </div>
      <a href="how-it-works.html">How It Works</a>
      <a href="applications.html">Applications</a>
      <a href="why-nexsun.html">Why Nexsun.ai</a>
      <div class="nav-dropdown">
        <a href="about.html">Company</a>
        <div class="nav-dropdown-menu">
          <a href="about.html">About Us</a>
          <a href="investors.html">Investor Centre</a>
          <a href="press.html">Press &amp; Media</a>
          <div class="menu-divider"></div>
          <a href="contact.html">Contact</a>
        </div>
      </div>
      <a href="engage.html" class="btn-cta">Engage</a>
    </div>
  </div>
</nav>

<section class="hub-hero">
  <div class="container">
    <h1>Solar Energy Across <span>Canada</span></h1>
    <p>Explore solar potential in 50 Canadian cities. Compare irradiance, costs, incentives, and ROI, powered by Nexsun.ai's decision intelligence platform.</p>
    <div class="hub-stat-row">
      <div class="hub-stat-item">
        <div class="val">50</div>
        <div class="lbl">Cities Covered</div>
      </div>
      <div class="hub-stat-item">
        <div class="val">10</div>
        <div class="lbl">Provinces</div>
      </div>
      <div class="hub-stat-item">
        <div class="val">1,080-1,400</div>
        <div class="lbl">kWh/m&sup2; Range</div>
      </div>
    </div>
  </div>
</section>

<section class="hub-provinces">
  <div class="container">
    {"".join(province_sections)}
  </div>
</section>

<section class="hub-cta">
  <div class="container">
    <h2>Ready to make a data-driven solar decision?</h2>
    <p>Nexsun.ai's decision intelligence platform models your property's solar potential with precision. Get started today.</p>
    <a href="engage.html" class="btn-cta" style="font-size:16px;padding:16px 36px;">Get Started</a>
  </div>
</section>

<footer>
  <div class="container">
    <div class="footer-top">
      <div class="footer-col">
        <h4>Platform</h4>
        <ul>
          <li><a href="platform.html">Platform Overview</a></li>
          <li><a href="how-it-works.html">How It Works</a></li>
          <li><a href="modules.html">Modules</a></li>
          <li><a href="technology.html">Technology</a></li>
          <li><a href="trust.html">Trust Centre</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="why-nexsun.html">Why Nexsun.ai</a></li>
          <li><a href="applications.html">Applications</a></li>
          <li><a href="partners.html">Partner Centre</a></li>
          <li><a href="investors.html">Investor Centre</a></li>
          <li><a href="press.html">Press &amp; Media</a></li>
          <li><a href="careers.html">Careers</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Resources</h4>
        <ul>
          <li><a href="blog.html">Insights</a></li>
          <li><a href="solar.html">Solar Guide</a></li>
          <li><a href="blog.html">Case Studies</a></li>
          <li><a href="blog.html">Events &amp; Media</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Contact Us</h4>
        <div style="margin-bottom:8px;">130, 5920 No. Two Road<br>Richmond BC V7C 4R9</div>
        <div style="margin-bottom:8px;"><a href="mailto:info@nexsun.ai" style="color:var(--sun);">info@nexsun.ai</a></div>
        <div><a href="tel:6047609015">1-604-760-9015</a></div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-legal">
        <a href="privacy.html">Privacy Policy</a>
        <a href="cookies.html">Cookie Policy</a>
        <a href="terms.html">Terms &amp; Conditions</a>
      </div>
      <p>&copy; 2026 Nexsun.ai. All rights reserved.</p>
    </div>
  </div>
</footer>

</body>
</html>'''
    return hub_html


def update_sitemap(cities):
    """Update sitemap.xml with solar pages."""
    # Read existing sitemap
    existing_urls = set()
    existing_entries = []

    if SITEMAP_PATH.exists():
        content = SITEMAP_PATH.read_text()
        # Extract existing non-solar URLs
        import re
        urls = re.findall(r'<url>\s*<loc>(.*?)</loc>.*?</url>', content, re.DOTALL)
        for url in urls:
            if '/solar/' not in url and url != 'https://nexsun.ai/solar.html':
                existing_urls.add(url)
                # Find the full <url> block
                pattern = f'<url>\\s*<loc>{re.escape(url)}</loc>.*?</url>'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    existing_entries.append(match.group())

    today = datetime.now().strftime("%Y-%m-%d")

    # Build new sitemap
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    # Keep existing entries
    for entry in existing_entries:
        lines.append(f"  {entry}")

    # Add hub page
    lines.append(f"""  <url>
    <loc>https://nexsun.ai/solar.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""")

    # Add city pages
    for city in cities:
        lines.append(f"""  <url>
    <loc>https://nexsun.ai/solar/{city['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""")

    lines.append('</urlset>')

    SITEMAP_PATH.write_text("\n".join(lines), encoding="utf-8")
    return len(cities) + 1  # +1 for hub page


def main():
    cities = load_cities()
    template = load_template()

    # Parse args
    single_city = None
    sitemap_only = False

    if len(sys.argv) > 1:
        if sys.argv[1] == "--sitemap":
            sitemap_only = True
        else:
            single_city = sys.argv[1]

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if sitemap_only:
        count = update_sitemap(cities)
        print(f"Sitemap updated with {count} solar URLs.")
        return

    if single_city:
        # Build single city
        city_data = None
        for c in cities:
            if c["slug"] == single_city:
                city_data = c
                break
        if not city_data:
            print(f"City '{single_city}' not found in CSV.")
            sys.exit(1)

        page = build_page(city_data, template, cities)
        out_path = OUTPUT_DIR / f"{city_data['slug']}.html"
        out_path.write_text(page, encoding="utf-8")
        print(f"Generated: {out_path}")
    else:
        # Build all cities
        count = 0
        for city_data in cities:
            page = build_page(city_data, template, cities)
            out_path = OUTPUT_DIR / f"{city_data['slug']}.html"
            out_path.write_text(page, encoding="utf-8")
            count += 1
            print(f"  [{count}/{len(cities)}] {city_data['city']}, {city_data['province']}")

        print(f"\nGenerated {count} solar city pages in {OUTPUT_DIR}/")

        # Generate hub page
        hub_html = generate_hub_page(cities)
        HUB_PATH.write_text(hub_html, encoding="utf-8")
        print(f"Generated hub page: {HUB_PATH}")

        # Update sitemap
        sitemap_count = update_sitemap(cities)
        print(f"Sitemap updated with {sitemap_count} solar URLs.")

        print(f"\nDone! {count} city pages + 1 hub page + sitemap updated.")


if __name__ == "__main__":
    main()
