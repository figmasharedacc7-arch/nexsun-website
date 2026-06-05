# TwoSuns Session Handoff

**Read this first when picking up the project in a new Claude session.**

Last updated: 2026-06-03. Live site at https://nexsun.ai (custom domain) and https://figmasharedacc7-arch.github.io/nexsun-website/ (GitHub Pages).

---

## 1. What TwoSuns is right now

**Brand:** TwoSuns (formerly Nexsun.ai, rebranded April 30, 2026)

**Current positioning (per Branding & Positioning TwoSuns doc, June 2026):**
- Tagline: **"Structure. Control. Clarity."**
- Headline: **"Orchestrate Better. Execute Faster."**
- Positioning: **AI-native operational intelligence layer for complex industrial organizations**
- Target verticals: **Cement, Mining, Manufacturing, Logistics, Infrastructure, Resource industries**
- ICP: Mid-market and enterprise (250 to 10,000 employees), complex operational environments
- Mission: "TwoSuns empowers complex industries to make smarter, faster, and more responsible decisions by connecting people, operations, and intelligence into coordinated execution environments that drive productivity, innovation, and sustainable economic growth."

**Platform structure (Core / Horizon / Forge / Assistant):**
- **Core** — Continuity layer (persistent organizational memory, governance, the Assistant)
- **Horizon** — Market and revenue execution (GTM, RevOps, pipeline, commercial workflows)
- **Forge** — Operations and execution (supply chain, procurement, infrastructure planning, operational diagnostics)
- **Assistant** — AI-enhanced coordination companion (preserves continuity and organizational awareness)

## 2. Workspace topology

Working dir: `/Users/mohammaddidarulalam/Documents/Claude/nexsun/`

| Path | Purpose |
|---|---|
| `nexsun/` (this folder) | Live site, deploys to nexsun.ai via GitHub Pages |
| `nexsun-backup-pre-twosuns-2026-04-30/` | Snapshot before the rebrand. Reference only |
| `nexsun-backup-pre-aiman-edits/` | Older backup. Reference only |
| `nexsun-backup-pre-rebrand-2026-04-24/` | Older backup. Reference only |
| `omnigtm-clone/`, `omnigtm-mirror/` | Sibling projects, not the TwoSuns site |

**Git:** `figmasharedacc7-arch/nexsun-website` on GitHub. Main branch deploys automatically to GitHub Pages.

## 3. Team

- **Aiman El-Ramly** — Founder & CEO. Drives content + messaging direction.
- **Belén Welch-Almeida** — Chief Growth Officer (commercial strategy, market positioning).
- **Ryan Arian** — Chief Digital Product Officer (product architecture, AI systems).
- **Michelle Mollineaux** — Director, Marketing & Partnerships.
- **Raihaan** — Google Cloud account holder (raihaan@aepg.ca).

## 4. Brand kit (Logos 4 — official kit, June 1, 2026)

All in `nexsun/logos-v4/` (kebab-case names, SVG + PNG, regular + white variants):
- `twosuns-logo` — master wordmark + dual-sun mark
- `assistant-logo` — Assistant module lockup
- `core-logo` — Core module lockup
- `horizon-logo` — Horizon module lockup
- `forge-logo` — Forge module lockup

**Site-wide logo files at nexsun/ root all use the official TwoSuns wordmark:**
- `logo-horizontal.svg` (nav across 93 pages), `logo-color.svg`, `logo-black.svg`, `logo-white.svg`, `logo-registered.svg`, `logo-horizontal-white.svg`, `twosuns-logo-horizontal.svg`
- `logo-mini.svg` — favicon (custom two-sun mark using kit's official colors and gradient style)

**Important:** all wordmark SVGs have a viewBox extended to include 35-40 units of padding on all sides (to prevent the gold sun mark or 's' letter from clipping). Don't revert this. Format: `viewBox="-40 -40 1472 443"` for color, `viewBox="-35 -35 1227 386"` for white.

## 5. Color palette (established)

| Token | Hex | Usage |
|---|---|---|
| Sun gold | `#E6C063` → `#D9B252` | Primary sun mark |
| Sun gold deep | `#B8932E` → `#CC9900` | Deeper amber accents |
| Sun orange | `#E85D2F` → `#FF6600` | Secondary sun, CTAs |
| Sun orange deep | `#B33B12` → `#C2410C` | Hover states |
| Navy | `#163E64` / `#0A2540` | Body text, brand mark |
| Navy deep | `#0D1B3E` | Dark sections |
| Cream | `#FAF7F0` → `#FFFBF0` | Light backgrounds |
| Sky | `#215F9A` | Secondary accent (use sparingly) |

## 6. Hard rules (apply to every edit)

1. **No em dashes anywhere.** Use commas. CEO rule, enforced site-wide.
2. **Never false-verify.** After editing a file, read it back word-by-word before claiming the change landed.
3. **Brainstorm mode:** when the user shares a doc, capture and discuss, don't implement until they say go.
4. **Keep TwoSuns enterprise tone:** institutional, operational, restrained, quietly ambitious. NOT consumer-AI, NOT startup hype.
5. **Don't touch backup folders** (`nexsun-backup-pre-*`).
6. **Don't commit** `token_raihaan.json`, `credentials.json`, or `.env` files.
7. **Short responses by default.** No trailing summaries.

## 7. Major work history

### April 2026 - Initial rebrand
- Apr 27: Belén bio update from her email markup
- Apr 28: Initial Nexsun.ai improvements (proofreading, em dash removal, logo refresh)
- Apr 30: **Full TwoSuns rebrand** from Nexsun.ai (commit cfdd986). All 93 pages, terminology swaps (PIA → TwoSuns Assistant, SoDR → TwoSuns Core, Glassbox → Persistent Coordination), homepage hero rewritten.

### May to June 2026 - Polish + sector pivot
- May 28: Partner page rewrite + new "Built for Partnership. Designed for Impact." colored-circle lifecycle visualization
- June 1: Official Logos 4 kit imported, all logo files updated, viewBox padding fixed to prevent clipping
- June 2: Energy-sector content removal (49 solar SEO pages deleted, 7 energy blog posts deleted, mechanical sweep replacing "energy markets" / "commodity trading" / "LNG" / "TTF" / "Brent" with industrial/enterprise framing)
- June 3: **Industrial repositioning applied** (commit fdadea2) — homepage hero, industries page, about mission, site-wide titles/meta all updated to the new "Operational Intelligence for Complex Industries" / "Structure. Control. Clarity." positioning from the Branding doc

### Hero design exploration (still in experiments folder, not live)
Built 11 hero concepts at `nexsun/experiments/concepts/` exploring different directions. None applied to live site, kept as reference:
1. Cinematic Minimal (Anthropic / Cohere)
2. Dark Cosmic (Palantir / Arc)
3. Data Observatory (Scale / Observable)
4. Flow Architecture (Databricks)
5. Animated Grid (Vercel / Linear)
6. Gradient Mastery (Stripe)
7. Playful Enterprise (Dust)
8. Coordinating Execution (refined live-hero pattern)
9. Two-Sun Composition (photoreal spheres + orbital + chips)
10. Editorial Restraint (response to "stock 3D, cheap motion, template vibe" feedback)
11. **Industrial Focus** — aligned with new branding doc (most recent, still preview only at `experiments/concepts/11-industrial-focus.html`)

User's quality-bar feedback: **CSS-only hand-built spheres look "stock 3D"** and **SaaS hero patterns (eyebrow pill, chips, breathing gradient bg, dual CTAs) read as templates**. Next direction if iterating: hire a real designer (`docs/Designer-Brief-TwoSuns-Hero.md` ready to send) or use AI image generation (`docs/AI-Image-Prompts-TwoSuns.md` ready to paste into Midjourney/DALL-E).

## 8. Current live site state

**Homepage `index.html`:**
- Hero: "Orchestrate Better. Execute Faster." / "Structure. Control. Clarity." / industrial framing
- Positioning section: "Complex Industries Operate in Fragments"
- Closing statement: "The next industrial leaders won't be defined by who has the most data..."
- Existing sun-orb visualization with rotating rays + 4 floating chips (Geopolitical Risk, Supply Chain Risk, Cyber Risk, Compliance Review), "COORDINATING Execution" centerpiece

**Industries page `industries.html`:**
- Hero: "Built for Complex Industrial Operations"
- 7 sector cards (already restructured to industrial-broad sectors)

**Platform page `platform.html`:**
- Platform Structure section with Core / Horizon / Forge cards using module logos from logos-v4/
- Below: existing 6-tab system components (Home, Explore, Position, Rooms, Contracts, Connect)
- TwoSuns Assistant section

**Partners page `partners.html`:**
- New Partner Lifecycle section: 6 colored circles (Align purple → Validate blue → Agree teal → Activate amber → Deliver orange → Scale purple) with chevron connectors, dashed outer rings, line-art SVG icons
- 4 partner categories: Technology, Data & Intelligence, System Integrators & Advisors, Industry & Strategic

**Other pages**: about, applications, how-it-works, engage, modules, technology, why-twosuns, trust, contact, careers, pricing, use-cases, resources, product, book-discovery, 3 solutions pages, blog (4 remaining posts), press, investors, terms, privacy, cookies, 404. All carry the TwoSuns brand. Energy/commodity references largely stripped.

**404 file count:** ~30 main pages + 4 blog posts + experiments/. Solar pages and energy blog posts deleted.

## 9. What's still pending (judgment calls)

1. **Platform.html Core/Horizon/Forge body copy** — could be reframed industrial-specific (cement plant coordination, mining ops, manufacturing workflows)
2. **Applications.html** — currently uses general "Coordination Owners" framing; could reframe around the 6 named verticals
3. **Cement-specific landing page** — the branding doc has a deep cement section, could become its own page (cement.html)
4. **Hero visual** — current sun-orb is fine but the user has questioned its quality. Hero design fundamentally needs a real designer (brief is ready). Holding pattern.
5. **og-image.jpg** — currently the auto-generated TwoSuns image, could be refreshed with the official kit
6. **LinkedIn + X handles** — placeholders, accounts don't exist yet
7. **Domain decision** — site lives at both nexsun.ai (custom) and figmasharedacc7-arch.github.io/nexsun-website/ (GitHub Pages). If acquiring twosuns.ai, plan redirect strategy

## 10. Key reference docs

In `nexsun/docs/`:
- `TwoSuns-Rebrand-Checklist.md` / `.docx` — Full rebrand task list with status
- `Designer-Brief-TwoSuns-Hero.md` — Ready-to-send brief for hiring a Figma designer
- `AI-Image-Prompts-TwoSuns.md` — Midjourney/DALL-E prompts across 9 aesthetic categories
- `CEO-Website-Edits-Checklist.md` — Aiman's original edits (already applied)
- `SESSION-HANDOFF.md` — This file

In `~/Downloads/` (user's reference docs):
- `Two Suns Logo v1.pptx` — Original logo presentation
- `DRAFT - Branding and Positioning TwoSuns.docx` — **Latest positioning doc (June 2026), drives the current site copy**
- `TwoSuns Web Content v1.docx` — Earlier content draft
- `Partner with TwoSuns.docx` — Partnership content (already applied)
- `Nexsun.ai Website Edits 3.docx` — Aiman's earlier site edits (already applied)

## 11. How to start the next session

The user will paste content from a new doc, ask for a design change, or request a specific fix. Default workflow:

1. **Read this handoff first** to know where things stand
2. **Verify current state** by reading the relevant file(s), don't assume from memory
3. **Apply the change locally**, read it back to verify
4. **Commit with descriptive message** ending with the `Co-Authored-By` line
5. **Push** so GitHub Pages auto-deploys in 30 to 60 seconds
6. **Confirm with HTTP 200 check** via curl if the user reports 404 (it's almost always deployment lag, not a real failure)

For brainstorming new content directions, use the `product-management:brainstorm` skill. For polishing specific pages, just apply edits directly.

---

**Live URL:** https://figmasharedacc7-arch.github.io/nexsun-website/

**Repo:** https://github.com/figmasharedacc7-arch/nexsun-website

**Latest commit at handoff time:** `fdadea2` (Apply new branding doc positioning to live site)
