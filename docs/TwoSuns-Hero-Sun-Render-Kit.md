# TwoSuns Hero Sun — Render Asset Kit (Path C)

The last 10% to world-class. The hero suns are currently CSS spheres (good, but they read as "two glowing divs"). Replacing them with a single crafted render of the two-sun object is what pushes the hero from "premium" to "elite." This kit has the exact brand spec, ready-to-paste prompts for every major tool, a no-AI 3D recipe, and how I drop the file into the live hero.

I cannot generate the image inside this environment (no image model wired in). You run one prompt in your tool of choice, drop the PNG in `nexsun/assets/`, and I wire it in.

---

## 1. The brand object (read this first)

Two overlapping suns, arranged exactly like the TwoSuns logo mark:
- **Gold sun:** larger, sits **behind**, **upper-left**.
- **Orange sun:** smaller, sits **in front**, **lower-right**.
- Overlap roughly 30 to 40 percent. They "kiss," they do not eclipse.

**Exact colors:**
| | Center (hot) | Mid | Edge / limb |
|---|---|---|---|
| Gold sun | `#FFFBEA` | `#EBBE49` | `#BC8A1A` |
| Orange sun | `#FFF4E8` | `#FF8B3E` | `#DD4E0C` |

**Look:** premium 3D, soft volumetric light from upper-left, gentle corona/atmosphere, faint photosphere granulation (like a real star's surface), luminous-but-matte. **Avoid:** lens flare, cartoon/clip-art, harsh white specular, color banding, any text.

**Canvas:** square, 2048×2048, subject centered with generous padding.

**Background (pick based on hero direction):**
- **Transparent PNG** — most flexible, works on the current warm hero. Default choice.
- **Deep navy `#0A1A2F`** — if we move toward the Palantir-style dark hero.
- **Warm cream `#FFFCF6`** — if you want the glow baked into a warm plate.

---

## 2. Prompts (copy/paste)

### A. Midjourney v6.1 (best quality, transparent via `--no background` or remove after)
```
two overlapping luminous spheres forming a binary sun system, a larger soft gold sun behind upper-left and a smaller vivid orange sun in front lower-right, gentle 35% overlap, premium 3D product render, soft volumetric light from upper left, subtle photosphere granulation, faint warm corona, luminous matte surface, clean studio lighting, centered, generous padding, transparent background, ultra detailed, octane render, 8k --ar 1:1 --style raw --v 6.1
```
Dark variant: swap `transparent background` for `on a deep navy #0A1A2F background, cinematic`.
Tip: MJ does not do true alpha. Generate on a flat background, then remove it (remove.bg, or Photoshop) for a clean PNG.

### B. DALL·E 3 (ChatGPT) — prose works better here
```
A high-end 3D render of two glowing suns forming a binary system, used as a clean brand object. The larger sun is soft gold (near-white core fading to warm gold #EBBE49 and a deeper rim #BC8A1A) and sits behind, in the upper-left. The smaller sun is vivid orange (white-hot core fading to #FF8B3E and a deep rim #DD4E0C) and sits in front, lower-right, overlapping the gold sun by about a third. Soft volumetric light from the upper left, faint warm corona, subtle granular photosphere texture like a real star. No lens flare, no text, no harsh highlights. Centered with generous padding on a transparent background. Square composition, crisp and premium.
```

### C. Flux.1 / Stable Diffusion XL (with negative prompt)
```
Positive: binary sun system, two overlapping glowing spheres, large gold sun behind upper-left, smaller orange sun front lower-right, 35% overlap, volumetric soft light, photosphere granulation, warm corona, premium 3d render, centered, studio, 8k
Negative: cartoon, flat, clip art, lens flare, text, watermark, signature, harsh specular, color banding, low-res, noise, extra spheres, faces
```

---

## 3. No-AI route (full control, repeatable) — Spline

Spline is free, browser-based, and gives pixel control plus an optional interactive 3D embed:
1. Two **Sphere** objects. Gold: 1.0 scale, Orange: 0.9 scale. Position orange front/lower-right overlapping the gold.
2. Material = **Emissive** (or Matcap). Set base/emission to the hexes above. Add a touch of **Noise** to the emission for granulation.
3. One soft **Directional/Area light** from upper-left. Turn on **Bloom** in post.
4. Background: transparent. Export **PNG @2x**.
5. Bonus: Spline can export an interactive scene we embed, so the suns subtly react to cursor. That alone reads "crafted."

**Blender alternative:** two UV spheres, Emission shader + a low-strength Noise/Voronoi texture for surface, world set transparent, Cycles render, add Bloom (or glare node) in the compositor.

---

## 4. Export checklist
- Transparent PNG (or the chosen bg), **≥1600px** on the short side.
- **Trim** empty margins, keep ~8% padding.
- Compress through tinypng.com, target **< 400 KB**.
- Save to `nexsun/assets/two-suns-hero.png` (and `@2x` if you have it).

---

## 5. How I wire it in (you don't do this part)
Once `two-suns-hero.png` is in `assets/`, I swap the two CSS sphere `<div>`s for the render and keep everything else (corona glow behind it, floating pillar chips, center label, binary drift):
```html
<div class="twin-suns">
  <img class="twin-render" src="assets/two-suns-hero.png" alt="TwoSuns — two-sun system" />
  <div class="sun-inner-text">…</div>   <!-- optional overlay -->
</div>
```
```css
.twin-render { width:430px; height:auto; display:block;
  filter: drop-shadow(0 26px 70px rgba(190,80,10,0.22)); }
```
The chips and label already sit above via `z-index`, so they keep floating over the crafted suns. Net effect: same layout, same warm hero, but the centerpiece is now a real object instead of gradients.

---

## 6. Recommendation
Ship **v2 (Path B)** as the live hero now — it is a real, free upgrade. Run **one** Midjourney or DALL·E prompt from section 2 in parallel. When the PNG lands, I drop it in per section 5 and we have the elite version without touching layout or copy. Two suns, one crafted object, world-class.
