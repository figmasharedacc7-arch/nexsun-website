# -*- coding: utf-8 -*-
"""Author four diagram treatments as Design Component artboards."""
import math

SUN, GOLD, CLAY, BRONZE = "#E0641E", "#CC9900", "#C45213", "#8C6500"
CREAM, CREAM2, NAVY, MUTED = "#FFF5DD", "#FFEFCE", "#1E1A14", "#5A554C"
FONT = "'Segoe UI', system-ui, -apple-system, sans-serif"
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"

AREAS = ["Materials and Manufacturing", "Distribution and Logistics",
         "Asset Owners and Investors", "Construction and Professional Services",
         "Asset Transactions and Operations", "Industry Institutions and Enablement"]
CODES = ["MAT", "DIS", "OWN", "CON", "OPS", "INS"]
STAGES = ["Planning", "Investment", "Design", "Supply", "Construction", "Transaction",
          "Use", "Operation", "Maintenance", "Renewal", "Reuse or retirement"]
TONES = [SUN, GOLD, CLAY, BRONZE, "#D9822B", "#B07E00"]
W, H = 1000, 800


def shell(inner, style=""):
    return """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
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
""" % (FONT, CLAY, BRONZE, style, inner)


def pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def caption(title, line):
    return ("""<div style="position:absolute;left:56px;bottom:44px;max-width:420px;">
      <div style="font-size:11px;font-weight:800;letter-spacing:2.4px;text-transform:uppercase;color:%s;">%s</div>
      <div style="font-size:13.5px;line-height:1.6;color:%s;margin-top:7px;">%s</div>
    </div>""" % (BRONZE, title, MUTED, line))


# ---------------------------------------------------------------- A. ECLIPSE
def eclipse():
    cx1, cx2, cy, r = 415, 585, 372, 236
    svg = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    svg.append("""<defs>
      <radialGradient id="gsun" cx="36%%" cy="34%%"><stop offset="0" stop-color="#FFFDF2"/>
        <stop offset=".45" stop-color="#F0D77E"/><stop offset="1" stop-color="%s"/></radialGradient>
      <radialGradient id="osun" cx="36%%" cy="34%%"><stop offset="0" stop-color="#FFF3E6"/>
        <stop offset=".42" stop-color="#FF9A52"/><stop offset="1" stop-color="%s"/></radialGradient>
      <clipPath id="lens"><circle cx="%d" cy="%d" r="%d"/></clipPath>
    </defs>""" % (GOLD, SUN, cx1, cy, r))
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="url(#gsun)" opacity=".93"/>' % (cx1, cy, r))
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="url(#osun)" opacity=".82"/>' % (cx2, cy, r))
    # the overlap reads as the lifecycle
    svg.append('<g clip-path="url(#lens)"><circle cx="%d" cy="%d" r="%d" fill="#FFF9EA" opacity=".92"/></g>'
               % (cx2, cy, r))
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(140,101,0,.35)"/>' % (cx1, cy, r))
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(196,82,19,.35)"/>' % (cx2, cy, r))
    # stage ticks running down the lens
    mid = (cx1 + cx2) / 2
    for i, st in enumerate(STAGES):
        y = cy - 150 + i * 30
        svg.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="rgba(140,101,0,.5)" stroke-width="1.5"/>'
                   % (mid - 26, y, mid + 26, y))
    # six areas on the outer silhouette, leader lines to the rim
    angles = [200, 160, 250, 290, 20, 340]
    labels = []
    for i, deg in enumerate(angles):
        base = cx1 if deg > 120 and deg < 290 else cx2
        px, py = pol(base, cy, r, deg)
        ex, ey = pol(base, cy, r + 74, deg)
        svg.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" stroke="%s" stroke-width="1.6" opacity=".55"/>'
                   % (px, py, ex, ey, TONES[i]))
        svg.append('<circle cx="%.0f" cy="%.0f" r="4.5" fill="%s"/>' % (px, py, TONES[i]))
        anchor = "right" if ex < mid else "left"
        pos = ("right:%.0fpx" % (W - ex + 12)) if anchor == "right" else ("left:%.0fpx" % (ex + 12))
        labels.append("""<div style="position:absolute;%s;top:%.0fpx;transform:translateY(-50%%);
          max-width:190px;text-align:%s;">
          <div style="font-size:10px;font-weight:800;letter-spacing:1.8px;color:%s;">0%d</div>
          <div style="font-size:13px;font-weight:700;color:%s;line-height:1.35;margin-top:2px;">%s</div>
        </div>""" % (pos, ey, "right" if anchor == "right" else "left", TONES[i], i + 1, NAVY, AREAS[i]))
    svg.append("</svg>")

    core = """<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translate(-50%%,-50%%);
      width:230px;text-align:center;">
      <div style="font-size:9.5px;font-weight:800;letter-spacing:2.6px;text-transform:uppercase;color:%s;">Where they meet</div>
      <div style="font-size:19px;font-weight:900;color:%s;line-height:1.2;margin-top:5px;">The built-asset lifecycle</div>
      <div style="font-size:11.5px;color:%s;margin-top:5px;">Eleven stages</div>
    </div>""" % (mid, cy, BRONZE, NAVY, MUTED)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s
  %s
  %s
  %s
</div>""" % (W, H, CREAM, "".join(svg), core, "".join(labels),
             caption("Eclipse", "The brand mark is the diagram. Two suns overlap and the overlap is the "
                                "lifecycle, so the structure is unmistakably TwoSuns rather than a stock hub."))
    return shell(inner)


# ---------------------------------------------------------------- B. STRATA
def strata():
    cx, cy = W / 2, 372
    svg = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    # outer ring: six area bands
    r_in, r_out = 196, 286
    for i in range(6):
        a0, a1 = -90 + i * 60 + 1.6, -90 + (i + 1) * 60 - 1.6
        x0, y0 = pol(cx, cy, r_out, a0); x1, y1 = pol(cx, cy, r_out, a1)
        x2, y2 = pol(cx, cy, r_in, a1); x3, y3 = pol(cx, cy, r_in, a0)
        svg.append('<path d="M%.1f %.1f A%d %d 0 0 1 %.1f %.1f L%.1f %.1f A%d %d 0 0 0 %.1f %.1f Z" '
                   'fill="%s" opacity=".92"/>' % (x0, y0, r_out, r_out, x1, y1, x2, y2, r_in, r_in, x3, y3, TONES[i]))
    # stage ring
    r_s0, r_s1 = 150, 186
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="#FFF9EA" stroke="rgba(140,101,0,.30)"/>' % (cx, cy, r_s1))
    step = 360.0 / len(STAGES)
    for j in range(len(STAGES)):
        d = -90 + j * step
        a, b = pol(cx, cy, r_s0, d), pol(cx, cy, r_s1, d)
        svg.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="rgba(140,101,0,.45)" stroke-width="1.4"/>'
                   % (a[0], a[1], b[0], b[1]))
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="%s" stroke="rgba(140,101,0,.30)"/>' % (cx, cy, r_s0, CREAM2))
    # radial exchange hairlines through every band
    for k in range(36):
        d = k * 10
        a, b = pol(cx, cy, r_s1 + 4, d), pol(cx, cy, r_out + 16, d)
        svg.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="rgba(30,26,20,.13)" stroke-width="1"/>'
                   % (a[0], a[1], b[0], b[1]))
    svg.append('<circle cx="%d" cy="%d" r="92" fill="#FFFDF6" stroke="rgba(196,82,19,.35)" stroke-width="1.5"/>'
               % (cx, cy))
    svg.append("</svg>")

    labels = []
    for i in range(6):
        d = -90 + i * 60 + 30
        lx, ly = pol(cx, cy, 350, d)
        align = "left" if lx > cx else ("right" if lx < cx - 6 else "center")
        style = ("left:%.0fpx" % lx) if align == "left" else (
                "right:%.0fpx" % (W - lx)) if align == "right" else ("left:%.0fpx;transform:translateX(-50%%)" % lx)
        labels.append("""<div style="position:absolute;%s;top:%.0fpx;max-width:200px;text-align:%s;">
          <div style="display:inline-block;width:9px;height:9px;border-radius:2px;background:%s;"></div>
          <div style="font-size:12.5px;font-weight:700;color:%s;line-height:1.35;margin-top:5px;">%s</div>
        </div>""" % (style, ly - 18, align if align != "center" else "center", TONES[i], NAVY, AREAS[i]))

    core = """<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translate(-50%%,-50%%);
      width:180px;text-align:center;">
      <div style="font-size:9.5px;font-weight:800;letter-spacing:2.6px;text-transform:uppercase;color:%s;">Core</div>
      <div style="font-size:17px;font-weight:900;color:%s;line-height:1.22;margin-top:5px;">The built-asset lifecycle</div>
    </div>""" % (cx, cy, BRONZE, NAVY)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s %s %s %s
</div>""" % (W, H, CREAM, "".join(svg), core, "".join(labels),
             caption("Strata", "Read as a core sample. The lifecycle is the innermost layer, the six areas "
                               "are the outer stratum, and hairlines cut through every band. Material, not abstract."))
    return shell(inner)


# ---------------------------------------------------------------- C. BLUEPRINT
def blueprint():
    cx, cy, r = 470, 358, 150
    svg = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    svg.append('<defs><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse">'
               '<path d="M28 0H0V28" fill="none" stroke="rgba(140,101,0,.13)" stroke-width="1"/></pattern></defs>')
    svg.append('<rect width="%d" height="%d" fill="url(#grid)"/>' % (W, H))
    # registration marks
    for x, y in [(40, 40), (W - 40, 40), (40, H - 40), (W - 40, H - 40)]:
        svg.append('<path d="M%d %d h18 M%d %d v18" stroke="%s" stroke-width="1.4" fill="none" opacity=".6"/>'
                   % (x - 9, y, x, y - 9, BRONZE))
    # centre wheel with crosshair and dimension ring
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="#FFFCF3" stroke="%s" stroke-width="1.6"/>' % (cx, cy, r, CLAY))
    svg.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="rgba(140,101,0,.35)" stroke-dasharray="4 6"/>'
               % (cx, cy, r + 26))
    svg.append('<path d="M%d %d h%d M%d %d v%d" stroke="rgba(140,101,0,.4)" stroke-width="1"/>'
               % (cx - r - 40, cy, 2 * r + 80, cx, cy - r - 40, 2 * r + 80))
    step = 360.0 / len(STAGES)
    stage_labels = []
    for j, st in enumerate(STAGES):
        d = -90 + j * step
        a, b = pol(cx, cy, r - 12, d), pol(cx, cy, r, d)
        svg.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6"/>'
                   % (a[0], a[1], b[0], b[1], CLAY))
        lx, ly = pol(cx, cy, r + 46, d)
        stage_labels.append("""<div style="position:absolute;left:%.0fpx;top:%.0fpx;transform:translate(-50%%,-50%%);
          font-family:%s;font-size:9px;letter-spacing:.4px;color:#7A6A4A;white-space:nowrap;">%02d %s</div>"""
                            % (lx, ly, MONO, j + 1, st.upper()))
    # six callouts on an orthogonal ladder down the right
    boxes = []
    for i in range(6):
        by = 96 + i * 100
        svg.append('<path d="M%d %d H%d" stroke="%s" stroke-width="1.3" opacity=".7"/>' % (cx + r + 30, by + 26, 700, TONES[i]))
        svg.append('<circle cx="%d" cy="%d" r="3.5" fill="%s"/>' % (cx + r + 30, by + 26, TONES[i]))
        boxes.append("""<div style="position:absolute;left:712px;top:%dpx;width:238px;
          border:1.4px solid %s;border-radius:2px;background:rgba(255,253,243,.9);padding:9px 12px;">
          <div style="font-family:%s;font-size:9.5px;letter-spacing:1.4px;color:%s;">%02d / %s</div>
          <div style="font-size:12.5px;font-weight:700;color:%s;line-height:1.35;margin-top:3px;">%s</div>
        </div>""" % (by, TONES[i], MONO, TONES[i], i + 1, CODES[i], NAVY, AREAS[i]))
    svg.append("</svg>")

    core = """<div style="position:absolute;left:%dpx;top:%dpx;transform:translate(-50%%,-50%%);
      width:186px;text-align:center;">
      <div style="font-family:%s;font-size:9px;letter-spacing:2px;color:%s;">CENTRE</div>
      <div style="font-size:16.5px;font-weight:900;color:%s;line-height:1.22;margin-top:5px;">The built-asset lifecycle</div>
      <div style="font-family:%s;font-size:9.5px;color:%s;margin-top:6px;">11 STAGES / CONTINUOUS</div>
    </div>""" % (cx, cy, MONO, BRONZE, NAVY, MONO, MUTED)

    block = """<div style="position:absolute;left:56px;top:600px;border:1.4px solid rgba(140,101,0,.45);
      background:rgba(255,253,243,.9);padding:12px 16px;font-family:%s;font-size:9.5px;letter-spacing:1px;color:%s;">
      <div style="color:%s;font-weight:700;">TWOSUNS / BUILT INDUSTRY</div>
      <div style="margin-top:4px;">SHEET 01 &nbsp;&middot;&nbsp; LIFECYCLE AND OPERATING AREAS</div>
    </div>""" % (MONO, MUTED, NAVY)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s %s %s %s %s %s
</div>""" % (W, H, "#FFFAEE", "".join(svg), core, "".join(stage_labels), "".join(boxes), block,
             caption("Blueprint", "Speaks the industry's own language. Drawing grid, registration marks, "
                                  "leader lines, a title block. Reads as a technical sheet, not a slide."))
    return shell(inner)


# ---------------------------------------------------------------- D. ORBIT
def orbit():
    cx, cy = W / 2, 368
    svg = ['<svg viewBox="0 0 %d %d" style="position:absolute;inset:0;width:100%%;height:100%%;">' % (W, H)]
    svg.append("""<defs>
      <radialGradient id="glow"><stop offset="0" stop-color="rgba(224,100,30,.34)"/>
        <stop offset=".55" stop-color="rgba(204,153,0,.12)"/><stop offset="1" stop-color="rgba(255,245,221,0)"/></radialGradient>
      <radialGradient id="cg" cx="36%%" cy="32%%"><stop offset="0" stop-color="#FFFDF3"/>
        <stop offset=".4" stop-color="#F2D887"/><stop offset="1" stop-color="%s"/></radialGradient>
    </defs>""" % GOLD)
    svg.append('<circle cx="%d" cy="%d" r="330" fill="url(#glow)"/>' % (cx, cy))
    orbits = [(300, 130, -14), (240, 104, 12), (368, 156, 4)]
    for rx, ry, rot in orbits:
        svg.append('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" transform="rotate(%d %d %d)" fill="none" '
                   'stroke="rgba(140,101,0,.30)" stroke-dasharray="3 8"/>' % (cx, cy, rx, ry, rot, cx, cy))
    # two suns at the centre
    svg.append('<circle cx="%d" cy="%d" r="60" fill="url(#cg)" opacity=".95"/>' % (cx - 22, cy))
    svg.append('<circle cx="%d" cy="%d" r="54" fill="%s" opacity=".88"/>' % (cx + 24, cy, SUN))
    # six bodies with trailing arcs
    place = [(0, 168), (0, 348), (1, 40), (1, 214), (2, 96), (2, 288)]
    labels = []
    for i, (oi, deg) in enumerate(place):
        rx, ry, rot = orbits[oi]
        a = math.radians(deg); rr = math.radians(rot)
        ux, uy = rx * math.cos(a), ry * math.sin(a)
        x = cx + ux * math.cos(rr) - uy * math.sin(rr)
        y = cy + ux * math.sin(rr) + uy * math.cos(rr)
        # trail
        pts = []
        for t in range(0, 26, 3):
            aa = math.radians(deg - t)
            vx, vy = rx * math.cos(aa), ry * math.sin(aa)
            pts.append("%.1f,%.1f" % (cx + vx * math.cos(rr) - vy * math.sin(rr),
                                      cy + vx * math.sin(rr) + vy * math.cos(rr)))
        svg.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4" opacity=".38" stroke-linecap="round"/>'
                   % (" ".join(pts), TONES[i]))
        svg.append('<circle cx="%.1f" cy="%.1f" r="9" fill="%s"/>' % (x, y, TONES[i]))
        svg.append('<circle cx="%.1f" cy="%.1f" r="15" fill="none" stroke="%s" stroke-width="1.2" opacity=".45"/>'
                   % (x, y, TONES[i]))
        left = x < cx
        style = ("right:%.0fpx;text-align:right" % (W - x + 26)) if left else ("left:%.0fpx" % (x + 26))
        labels.append("""<div style="position:absolute;%s;top:%.0fpx;transform:translateY(-50%%);max-width:186px;">
          <div style="font-size:12.5px;font-weight:700;color:%s;line-height:1.35;">%s</div>
        </div>""" % (style, y, NAVY, AREAS[i]))
    svg.append("</svg>")

    core = """<div style="position:absolute;left:%dpx;top:%dpx;transform:translate(-50%%,-50%%);
      width:210px;text-align:center;pointer-events:none;">
      <div style="font-size:15.5px;font-weight:900;color:#FFF9EC;line-height:1.2;
        text-shadow:0 2px 6px rgba(120,45,0,.85);">The built-asset lifecycle</div>
    </div>""" % (cx, cy)

    stages = """<div style="position:absolute;left:56px;top:640px;right:56px;display:flex;flex-wrap:wrap;gap:7px;">
      %s
    </div>""" % "".join(
        '<span style="font-size:10px;font-weight:700;letter-spacing:.4px;color:#7A6A4A;'
        'border:1px solid rgba(140,101,0,.30);border-radius:20px;padding:4px 11px;">%s</span>' % s
        for s in STAGES)

    inner = """<div style="position:relative;width:%dpx;height:%dpx;background:%s;overflow:hidden;">
  %s %s %s %s %s
</div>""" % (W, H, CREAM, "".join(svg), core, "".join(labels), stages,
             caption("Orbit", "The sun metaphor taken literally. Six areas travel elliptical paths around the "
                              "lifecycle, trails showing continuous exchange. Most atmospheric, least literal."))
    return shell(inner)


import json, io
open("Main.dc.html", "w").write(blueprint())
open("Eclipse.dc.html", "w").write(eclipse())
open("Strata.dc.html", "w").write(strata())
open("Orbit.dc.html", "w").write(orbit())

canvas = {
  "artboards": [
    {"file": "Main.dc.html",    "x": 0,    "y": 0,   "w": W, "h": H, "title": "Blueprint"},
    {"file": "Eclipse.dc.html", "x": 1120, "y": 0,   "w": W, "h": H},
    {"file": "Strata.dc.html",  "x": 0,    "y": 920, "w": W, "h": H},
    {"file": "Orbit.dc.html",   "x": 1120, "y": 920, "w": W, "h": H},
  ],
  "annotations": [
    {"id": "brief", "x": 0, "y": -180, "w": 460,
     "text": "Built-asset lifecycle at the centre, six operating areas around it, connecting lines showing continuous exchange.\n\nFour directions. Pick one and it gets rebuilt as production SVG on the Built Industry page."}
  ],
  "launch": {"view": "canvas"}
}
open("canvas.json", "w").write(json.dumps(canvas, indent=2))
print("wrote 4 artboards + canvas.json")
