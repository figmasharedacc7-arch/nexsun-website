# -*- coding: utf-8 -*-
"""Eclipse, taken further. Three refinements of the picked direction."""
import math, json

SUN, GOLD, CLAY, BRONZE = "#E0641E", "#CC9900", "#C45213", "#8C6500"
CREAM, CREAM2, NAVY, MUTED = "#FFF5DD", "#FFEFCE", "#1E1A14", "#5A554C"
FONT = "'Segoe UI', system-ui, -apple-system, sans-serif"
SERIF = "'Instrument Serif', Georgia, 'Times New Roman', serif"

AREAS = ["Materials and Manufacturing", "Distribution and Logistics",
         "Asset Owners and Investors", "Construction and Professional Services",
         "Asset Transactions and Operations", "Industry Institutions and Enablement"]
STAGES = ["Planning", "Investment", "Design", "Supply", "Construction", "Transaction",
          "Use", "Operation", "Maintenance", "Renewal", "Reuse or retirement"]
TONES = [SUN, GOLD, CLAY, BRONZE, "#D9822B", "#B07E00"]
W, H = 1000, 800


def shell(inner, extra_css="", gfont=None):
    link = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=%s&display=swap">' % gfont) if gfont else ""
    return """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  %s
  <style>
    body { margin: 0; font-family: %s; }
    a { color: %s; } a:hover { color: %s; }
    %s
  </style>
</helmet>
%s
</x-dc>
</body>
</html>
""" % (link, FONT, CLAY, BRONZE, extra_css, inner)


def pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


GRAIN = """<filter id="grain" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="4" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>"""


def suns_defs(idg="g", ido="o"):
    return """<radialGradient id="%s" cx="34%%" cy="30%%">
      <stop offset="0" stop-color="#FFFDF0"/><stop offset=".34" stop-color="#F6E4A4"/>
      <stop offset=".72" stop-color="#DFC15C"/><stop offset="1" stop-color="%s"/></radialGradient>
    <radialGradient id="%s" cx="34%%" cy="30%%">
      <stop offset="0" stop-color="#FFF4E8"/><stop offset=".32" stop-color="#FFB077"/>
      <stop offset=".70" stop-color="#F2762A"/><stop offset="1" stop-color="%s"/></radialGradient>
    <radialGradient id="corona"><stop offset=".55" stop-color="rgba(224,100,30,.22)"/>
      <stop offset="1" stop-color="rgba(224,100,30,0)"/></radialGradient>""" % (idg, GOLD, ido, SUN)


def stage_spine(mid, cy, size=10.5, gap=25, colour="#6E5F3F"):
    top = cy - (len(STAGES) - 1) * gap / 2
    out = []
    for i, st in enumerate(STAGES):
        y = top + i * gap
        out.append("""<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translate(-50%%,-50%%);
          font-size:%.1fpx;font-weight:%d;letter-spacing:.5px;color:%s;white-space:nowrap;">%s</div>"""
                   % (mid, y, size, 700 if i in (0, len(STAGES) - 1) else 600, colour, st))
    return "".join(out), top


# ---------------------------------------------------------------- MAIN: Eclipse refined
def eclipse_main():
    cx1, cx2, cy, r = 404, 596, 366, 244
    mid = (cx1 + cx2) / 2
    s = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    s.append("<defs>%s%s<clipPath id=\"lensA\"><circle cx=\"%d\" cy=\"%d\" r=\"%d\"/></clipPath></defs>"
             % (suns_defs(), GRAIN, cx1, cy, r))
    s.append('<circle cx="%.0f" cy="%d" r="430" fill="url(#corona)"/>' % (mid, cy))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="url(#g)"/>' % (cx1, cy, r))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="url(#o)" opacity=".9"/>' % (cx2, cy, r))
    # the overlap: the lifecycle, lifted out as light
    s.append('<g clip-path="url(#lensA)"><circle cx="%d" cy="%d" r="%d" fill="#FFFBF0" opacity=".96"/></g>'
             % (cx2, cy, r))
    # rim light along both edges of the lens
    s.append('<g clip-path="url(#lensA)"><circle cx="%d" cy="%d" r="%d" fill="none" stroke="#FFF6DC" '
             'stroke-width="3" opacity=".9"/></g>' % (cx2, cy, r))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(140,101,0,.45)"/>' % (cx1, cy, r))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(196,82,19,.45)"/>' % (cx2, cy, r))
    # hairline down the true centre of the lens
    s.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="rgba(140,101,0,.28)" stroke-dasharray="2 5"/>'
             % (mid, cy - 218, mid, cy + 218))

    # six areas: leader lines out to the rim
    angles = [206, 154, 244, 296, 26, 334]
    labels = []
    for i, deg in enumerate(angles):
        base = cx1 if 120 < deg < 300 else cx2
        px, py = pol(base, cy, r, deg)
        ex, ey = pol(base, cy, r + 62, deg)
        s.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="1.5" opacity=".6"/>'
                 % (px, py, ex, ey, TONES[i]))
        s.append('<circle cx="%.0f" cy="%.0f" r="5" fill="%s"/>' % (px, py, TONES[i]))
        s.append('<circle cx="%.0f" cy="%.0f" r="9.5" fill="none" stroke="%s" stroke-width="1" opacity=".4"/>'
                 % (px, py, TONES[i]))
        right = ex >= mid
        pos = ("left:%.0fpx" % (ex + 14)) if right else ("right:%.0fpx" % (W - ex + 14))
        labels.append("""<div style="position:absolute;%s;top:%.0fpx;transform:translateY(-50%%);
          width:196px;text-align:%s;">
          <div style="font-size:10px;font-weight:800;letter-spacing:2px;color:%s;">%02d</div>
          <div style="height:1px;background:%s;opacity:.45;margin:5px 0 6px;"></div>
          <div style="font-size:13px;font-weight:700;color:%s;line-height:1.36;">%s</div>
        </div>""" % (pos, ey, "left" if right else "right", TONES[i], i + 1, TONES[i], NAVY, AREAS[i]))
    s.append('<rect width="%d" height="%d" filter="url(#grain)" opacity=".055"/>' % (W, H))
    s.append("</svg>")

    spine, top = stage_spine(mid, cy)
    cap = """<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translateX(-50%%);
        text-align:center;width:230px;">
        <div style="font-size:9.5px;font-weight:800;letter-spacing:2.8px;text-transform:uppercase;color:%s;">
          Where they overlap</div>
      </div>""" % (mid, top - 46, BRONZE)
    foot = """<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translateX(-50%%);
        text-align:center;width:250px;">
        <div style="font-size:14px;font-weight:900;color:%s;line-height:1.25;">The built-asset lifecycle</div>
      </div>""" % (mid, cy + 232, NAVY)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s %s %s %s
  <div style="position:absolute;left:56px;bottom:38px;max-width:430px;">
    <div style="font-size:11px;font-weight:800;letter-spacing:2.4px;text-transform:uppercase;color:%s;">Eclipse</div>
    <div style="font-size:13.5px;line-height:1.6;color:%s;margin-top:7px;">All eleven stages now read inside
      the overlap, so the lens carries the information rather than standing in for it. Corona, rim light and
      a fine grain give the discs depth.</div>
  </div>
</div>""" % (W, H, CREAM, "".join(s), spine, cap + foot, "".join(labels), BRONZE, MUTED)
    return shell(inner)


# ---------------------------------------------------------------- Editorial
def editorial():
    cx1, cx2, cy, r = 640, 830, 372, 258
    mid = (cx1 + cx2) / 2
    s = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    s.append("<defs>%s%s<clipPath id=\"lensB\"><circle cx=\"%d\" cy=\"%d\" r=\"%d\"/></clipPath></defs>"
             % (suns_defs(), GRAIN, cx1, cy, r))
    s.append('<circle cx="%.0f" cy="%d" r="470" fill="url(#corona)"/>' % (mid, cy))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="url(#g)"/>' % (cx1, cy, r))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="url(#o)" opacity=".9"/>' % (cx2, cy, r))
    s.append('<g clip-path="url(#lensB)"><circle cx="%d" cy="%d" r="%d" fill="#FFFBF0" opacity=".96"/></g>'
             % (cx2, cy, r))
    s.append('<g clip-path="url(#lensB)"><circle cx="%d" cy="%d" r="%d" fill="none" stroke="#FFF6DC" '
             'stroke-width="3" opacity=".9"/></g>' % (cx2, cy, r))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(140,101,0,.4)"/>' % (cx1, cy, r))
    # index rules reaching from the left column to the discs
    rows = []
    for i in range(6):
        ry = 150 + i * 78
        s.append('<path d="M330 %d H%.0f" stroke="%s" stroke-width="1.2" opacity=".5"/>' % (ry, cx1 - r + 26, TONES[i]))
        s.append('<circle cx="330" cy="%d" r="4" fill="%s"/>' % (ry, TONES[i]))
        rows.append("""<div style="position:absolute;left:56px;top:%dpx;transform:translateY(-50%%);width:262px;">
          <div style="display:flex;align-items:baseline;gap:10px;">
            <span style="font-family:%s;font-size:21px;line-height:1;color:%s;">%02d</span>
            <span style="font-size:13px;font-weight:700;color:%s;line-height:1.35;">%s</span>
          </div>
        </div>""" % (ry, SERIF, TONES[i], i + 1, NAVY, AREAS[i]))
    s.append('<rect width="%d" height="%d" filter="url(#grain)" opacity=".05"/>' % (W, H))
    s.append("</svg>")

    spine, top = stage_spine(mid, cy, size=10, gap=24)
    head = """<div style="position:absolute;left:56px;top:56px;width:300px;">
      <div style="font-size:10px;font-weight:800;letter-spacing:2.6px;text-transform:uppercase;color:%s;">
        Six operating areas</div>
      <div style="font-family:%s;font-size:34px;line-height:1.08;color:%s;margin-top:10px;">One connected
        industry around the complete life of built assets.</div>
    </div>""" % (BRONZE, SERIF, NAVY)
    lens_cap = """<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translateX(-50%%);width:210px;text-align:center;">
      <div style="font-size:9px;font-weight:800;letter-spacing:2.6px;text-transform:uppercase;color:%s;">The overlap</div>
      </div>
      <div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translateX(-50%%);width:230px;text-align:center;">
      <div style="font-family:%s;font-size:17px;color:%s;line-height:1.2;">The built-asset lifecycle</div>
      </div>""" % (mid, top - 40, BRONZE, mid, cy + 224, SERIF, NAVY)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s %s %s %s %s
  <div style="position:absolute;left:56px;bottom:34px;max-width:400px;">
    <div style="font-size:11px;font-weight:800;letter-spacing:2.4px;text-transform:uppercase;color:%s;">Editorial</div>
    <div style="font-size:13px;line-height:1.6;color:%s;margin-top:6px;">Asymmetric. The suns bleed off the right
      edge, the six areas become a left-hand index with measured rules. Adds a display serif, which the site
      does not currently use.</div>
  </div>
</div>""" % (W, H, CREAM, "".join(s), head, "".join(rows), spine, lens_cap, BRONZE, MUTED)
    return shell(inner, gfont="Instrument+Serif:ital@0;1")


# ---------------------------------------------------------------- Nocturne
def nocturne():
    cx1, cx2, cy, r = 404, 596, 358, 240
    mid = (cx1 + cx2) / 2
    INK = "#171310"
    s = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    s.append("""<defs>%s%s
      <radialGradient id="halo"><stop offset=".4" stop-color="rgba(255,176,90,.30)"/>
        <stop offset="1" stop-color="rgba(23,19,16,0)"/></radialGradient>
      <clipPath id="lensC"><circle cx="%d" cy="%d" r="%d"/></clipPath></defs>""" % (suns_defs(), GRAIN, cx1, cy, r))
    s.append('<rect width="%d" height="%d" fill="%s"/>' % (W, H, INK))
    s.append('<circle cx="%.0f" cy="%d" r="500" fill="url(#halo)"/>' % (mid, cy))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="url(#g)"/>' % (cx1, cy, r))
    s.append('<circle cx="%d" cy="%d" r="%d" fill="url(#o)" opacity=".93"/>' % (cx2, cy, r))
    s.append('<g clip-path="url(#lensC)"><circle cx="%d" cy="%d" r="%d" fill="#FFF7E4" opacity=".97"/></g>'
             % (cx2, cy, r))
    s.append('<g clip-path="url(#lensC)"><circle cx="%d" cy="%d" r="%d" fill="none" stroke="#FFFDF4" '
             'stroke-width="3.5"/></g>' % (cx2, cy, r))
    angles = [206, 154, 244, 296, 26, 334]
    labels = []
    for i, deg in enumerate(angles):
        base = cx1 if 120 < deg < 300 else cx2
        px, py = pol(base, cy, r, deg)
        ex, ey = pol(base, cy, r + 66, deg)
        s.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="1.5" opacity=".85"/>'
                 % (px, py, ex, ey, TONES[i]))
        s.append('<circle cx="%.0f" cy="%.0f" r="5" fill="%s"/>' % (px, py, TONES[i]))
        right = ex >= mid
        pos = ("left:%.0fpx" % (ex + 14)) if right else ("right:%.0fpx" % (W - ex + 14))
        labels.append("""<div style="position:absolute;%s;top:%.0fpx;transform:translateY(-50%%);
          width:198px;text-align:%s;">
          <div style="font-size:10px;font-weight:800;letter-spacing:2px;color:%s;">%02d</div>
          <div style="font-size:13px;font-weight:700;color:#F6EDDC;line-height:1.36;margin-top:5px;">%s</div>
        </div>""" % (pos, ey, "left" if right else "right", TONES[i], i + 1, AREAS[i]))
    s.append('<rect width="%d" height="%d" filter="url(#grain)" opacity=".085"/>' % (W, H))
    s.append("</svg>")

    spine, top = stage_spine(mid, cy, size=10.5, gap=24, colour="#6B5B3C")
    caps = """<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translateX(-50%%);width:220px;text-align:center;">
      <div style="font-size:9.5px;font-weight:800;letter-spacing:2.8px;text-transform:uppercase;color:#8C6500;">
        Where they overlap</div></div>
      <div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translateX(-50%%);width:250px;text-align:center;">
      <div style="font-size:14px;font-weight:900;color:#FFF3DC;line-height:1.25;">The built-asset lifecycle</div>
      </div>""" % (mid, top - 42, mid, cy + 228)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s %s %s %s
  <div style="position:absolute;left:56px;bottom:38px;max-width:420px;">
    <div style="font-size:11px;font-weight:800;letter-spacing:2.4px;text-transform:uppercase;color:#B07E00;">Nocturne</div>
    <div style="font-size:13.5px;line-height:1.6;color:#B6A88C;margin-top:7px;">Same structure on near-black.
      The suns actually glow and the overlap reads as light. Highest impact, but it breaks the all-cream rule
      the rest of the site keeps.</div>
  </div>
</div>""" % (W, H, INK, "".join(s), spine, caps, "".join(labels))
    return shell(inner)


open("Main.dc.html", "w").write(eclipse_main())
open("Editorial.dc.html", "w").write(editorial())
open("Nocturne.dc.html", "w").write(nocturne())

canvas = {
  "artboards": [
    {"file": "Main.dc.html",      "x": 0,    "y": 0,   "w": W, "h": H, "title": "Eclipse refined"},
    {"file": "Editorial.dc.html", "x": 1120, "y": 0,   "w": W, "h": H},
    {"file": "Nocturne.dc.html",  "x": 0,    "y": 920, "w": W, "h": H},
    {"file": "Eclipse.dc.html",   "x": 1120, "y": 920, "w": W, "h": H, "title": "Eclipse (first pass)"},
  ],
  "annotations": [
    {"id": "brief", "x": 0, "y": -190, "w": 470,
     "text": "Eclipse taken further. The first pass is bottom right for comparison.\n\nEvery version now reads all eleven lifecycle stages inside the overlap, which the first pass only hinted at with ticks."}
  ],
  "launch": {"view": "canvas"}
}
open("canvas.json", "w").write(json.dumps(canvas, indent=2))
print("wrote 3 new artboards + canvas.json")
