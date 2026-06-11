# TwoSuns Session Handoff

**Read this first when picking up the project in a new chat.** Last updated end of a long working session (2026-06-06).

**To start the new chat, paste:**
> Read `/Users/mohammaddidarulalam/Documents/Claude/nexsun/docs/SESSION-HANDOFF.md` then wait for my instruction.

**Live site:** https://figmasharedacc7-arch.github.io/nexsun-website/ (custom domain twosuns.ai)
**Repo:** `figmasharedacc7-arch/nexsun-website`, main auto-deploys to GitHub Pages (30-60s lag; a fresh push 404s briefly, that's normal).
**Working dir:** `/Users/mohammaddidarulalam/Documents/Claude/nexsun/`
**Latest commit at handoff:** `d129f85` (Mining industry landing page).

---

## 🔴 THE BIG OPEN DECISION (blocks a lot)

**Positioning: industrial vs organizations.** The user (Raihaan) confirmed the **industrial** direction is correct ("complex industries", verticals cement/mining/manufacturing/logistics/infrastructure) but is **checking with supervisors before we sweep the site**. Until signed off:
- The homepage hero says "the orchestration layer for **complex organizations**" (from the Website-edits deck).
- ~8 pages' titles/metas still say the OLD "coordination infrastructure" / "operational intelligence for complex industries" / "complex enterprises" (inconsistent).
- **Do NOT run the site-wide titles/metas/positioning sweep until the user confirms.** New industry pages + Trust/Technology already use the industrial framing (safe, agreed).

---

## Brand facts (from the branding doc + product guy)

- **Name:** TwoSuns.ai (company/legal), **twosuns** lowercase (product/brand). Two suns = market + operations, gold (intelligence) + orange (execution).
- **Confirmed taglines (branding doc):** Headline **"Orchestrate Better. Execute Faster."** · Short **"Structure. Control. Clarity."** · Mission: "TwoSuns empowers complex industries to make smarter, faster, and more responsible decisions by connecting people, operations, and intelligence into coordinated execution environments..."
- **Category line:** "AI-native operational intelligence layer for complex industries" / "system of decision, not system of record."
- **Product architecture (branding doc):** **Core** (continuity/governance/memory) · **Horizon** (market/GTM/commercial) · **Forge** (operations/supply chain/execution) · **Assistant** (AI coordination companion). NOTE: the live site + videos still use the OLD 5 modules (Explore, Position, Contract, Rooms, Admin). User said **keep the 5 modules for the videos** (match current site). Core/Horizon/Forge is for later.
- **Sectors:** Cement, Mining, Manufacturing, Transportation & Logistics, Clean Tech, Infrastructure, Resource industries.

### Official color palette (DEPLOYED site-wide this session)
| Role | Name | HEX | RGB |
|---|---|---|---|
| Primary | Bright Orange | #FF6600 | 255,102,0 (CTAs, accents, highlights) |
| Primary | Gold | #CC9900 | 204,153,0 (gradients, icons) |
| Primary | Light Beige | #FFF5DD | dominant background |
| Secondary | Black / Dark Grey / Steel Grey / White | #000000 / #3A3A3A / #747474 / #FFFFFF | text, neutrals (site already uses #3A3A3A text) |
| Data-viz set | Red #C00000 · Orange #FF9933 · Yellow #FFC000 · Green #336600 · Green-low #4EA72E · Navy #003366 · Blue Sky #4E95D9 | (for charts/diagrams only, never compete with core) |

**Doc errors flagged (fix at source):** Light Beige HEX `#FFF5DD` vs listed RGB `255,251,241` mismatch (deployed #FFF5DD) · Neutral White RGB wrongly listed `38,50,56` · "Red" row HEX printed `#FF6600` but RGB `192,0,0`=#C00000 · doc names a core "Deep Horizon Blue" not in the primary table (likely #003366).
**Pending palette items:** reconcile site navy `#163E64` vs doc's `#003366` ("Deep Horizon Blue"); the doc specifies **Aptos** type (site uses Segoe UI / Inter), not yet switched.

---

## Hard rules
1. **No em dashes anywhere.** Use commas. CEO rule.
2. **No "real time" / "real-time."** Use "continuous" / "continuously."
3. **Never false-verify.** Read files back / render before claiming a change landed.
4. **Brainstorm mode:** when given a doc/video, capture and discuss, do not implement until told.
5. Keep the enterprise/industrial tone: institutional, precise, no hype.
6. Don't commit token/credential files. Don't touch `nexsun-backup-*` folders.
7. Short responses by default; commit + push after substantive changes.

## Capabilities that worked this session
- **Render any page/SVG/docx-logo:** headless Chrome on `file://` (no localhost server, loopback is sandboxed off). `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --screenshot=... file://...` (use `--dangerouslyDisableSandbox` Bash flag for network/fonts).
- **Watch videos:** download (or local file) + `ffmpeg -vf "fps=1/2,scale,tile=AxB"` frame montages, then Read the montage. (No ffprobe; no tesseract/whisper, so OCR/transcription is manual via reading frames.)
- **PDF text:** `pdfplumber` (pdftoppm not installed). **docx:** `python-docx` (read + generate).
- **Google Drive MCP** connected (search_files/list_recent_files); large videos can't stream through it, have user drop files in ~/Downloads instead.

---

## What got done this session (condensed)

**Website-edits.pptx deck applied** (slides 2-11): hero copy, "Organizations Today" section, removed the founder/pedigree (energy) section, Mission line, Opportunity copy, **Why TwoSuns 3→4 cards** (added Human-in-the-Loop Governance), Decision Packs wording, Partners page metadata.

**Hero design saga** (live hero = **V1**, two CSS suns + rays + emoji chips). Explored V2 (serif craft), V3 (premium CSS), V4/V5 (real NASA sun photos, rejected "sci-fi"), V6 (sunburst), V7 (binary orchestration system, soft suns + orbit), V8 (V1 suns + orbit), V9 (V1 suns + rays + orbit), V10 (V7 spaced suns + bloom). **Shareable gallery:** https://figmasharedacc7-arch.github.io/nexsun-website/experiments/hero-showcase.html (V7/V9/V10 are the favorites). All hero experiments in `experiments/two-suns-hero-v*.html`. Live homepage is untouched V1.

**Official palette deployed** site-wide (~2,459 tokens, 37 pages).

**Video scripts** written (demo VO + 5 module clips, TwoSuns rebrand of the old Nexsun demo). Branded **`~/Downloads/TwoSuns-Demo-Video-Script.docx`** generated (two-sun logo + "Demo Video Script"). Current site videos (homepage + 5 on modules.html) are ALL still old Nexsun (Framer-hosted, blue, energy/trading) and need replacing, user is producing these separately.

---

## 🟢 SEO optimization (the ACTIVE thread)

**Term spine (confirmed with product guy):** System of Decision Records, System of Outcomes, Intelligent Ops, Human-in-the-Loop, **Glassbox AI**. Plus trend terms (agentic AI, vertical AI, physical AI, decision intelligence). Full per-page keyword map in **`docs/SEO-keyword-map.md`**.

**Done (committed + live):**
1. Technical quick wins: robots.txt sitemap → twosuns.ai (was dead nexsun.ai); added missing H1 on modules.html; trimmed technology.html title (73→58); deleted `why-nexsun.html` (duplicate); alt text already 100% (349 imgs).
2. Keyword map (`docs/SEO-keyword-map.md`).
3. Homepage structured data fixed (Organization: working logo, both founders Aiman + Ryan, 4 socials in sameAs; + WebSite schema).
4. **Trust page** optimized for glassbox/explainable/auditable/human-in-the-loop/AI-governance.
5. **Technology page** optimized for glassbox/explainable AI architecture/System of Decision Records.
6. **Cement landing page** `cement.html` ("AI operational intelligence for cement"), in sitemap, linked from industries (Infrastructure & Industrial card).
7. **Mining landing page** `mining.html`, in sitemap, linked from industries (Resource-Intensive card).

**Industry-page recipe (to repeat for manufacturing + logistics):** `cp cement.html X.html` → python-replace head SEO strings + JSON-LD + the body between `<!-- ══ HERO ══ -->` and `<!-- ══ CTA ══ -->` with X content (hero, stats, challenge cards, 6 help cards, role cards, positioning) → add `<url>` to sitemap.xml → add a "Deep dive →" link from the relevant industries.html card. Branding doc has deep content for cement + mining; manufacturing/logistics can follow the same structure.

**SEO next steps:**
- ▶ Build **manufacturing** + **logistics** landing pages (unblocked, fast, template proven). Industries set = 2 of 4 done.
- ▶ Optional: FAQ + Breadcrumb schema; make industry pages more discoverable (nav "Industries" dropdown or a sector grid on industries.html, user was asked, not yet decided).
- ⏸ **Titles/metas sweep** across ~8 pages (index, product, about, careers, investors, pricing, contact, modules) still "coordination infrastructure"/"complex enterprises", BLOCKED on positioning sign-off.
- ⏸ **User/Raihaan task:** register twosuns.ai in **Google Search Console + Bing**, submit the sitemap (so indexing actually starts). Raihaan holds the Google Cloud account.

---

## Team
- **Aiman El-Ramly** — Founder & CEO. **Ryan Arian** — co-founder/CDPO. **Belén Welch-Almeida** — CGO. **Michelle Mollineaux** — Marketing/Partnerships. **Alexa Marquez** — sent the palette deploy directive. **Raihaan** (the user, raihaan@aepg.ca) — website + Google Cloud account.

## Key files & reference docs
- `docs/SEO-keyword-map.md` — per-page keyword map
- `docs/TwoSuns-Hero-Sun-Render-Kit.md` — render-asset prompts for the hero suns
- `docs/TwoSuns-Video-Scripts.md` — full video script doc (may be uncommitted)
- `~/Downloads/TwoSuns-Demo-Video-Script.docx` — branded demo script
- `~/Downloads/DRAFT - Branding and Positioning TwoSuns.pdf` (40pp) / `.docx` — **the authoritative brand doc** (positioning, palette pp.36-38, Core/Horizon/Forge, cement + mining deep content, ICP, GTM)
- `~/Downloads/Product Branding Check-List.xlsx - Branding Phase 1.pdf` — the phase-1 task checklist
- `~/Downloads/Website-edits.pptx` — the homepage edit deck (applied)
- `experiments/hero-showcase.html` — shareable hero gallery; `experiments/two-suns-hero-v*.html` — hero versions

## Pending decisions to resurface
1. **Positioning sign-off** (industrial) — unblocks the titles/metas sweep + the homepage hero copy.
2. **Hero winner** — V1 is live; user likes V7/V9/V10 from the gallery. Ship one when chosen.
3. **Navy + typography** reconciliation to the brand doc (#003366, Aptos).
4. **Industry-page discoverability** (nav dropdown vs sector grid).
5. **Module architecture** long-term (5 modules now vs Core/Horizon/Forge in the doc).
