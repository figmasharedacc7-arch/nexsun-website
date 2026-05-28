# TwoSuns Rebrand Checklist

**Source doc:** TwoSuns Web Content v1 (provided 2026-04-30)
**Brand pivot:** Nexsun.ai → TwoSuns
**Last updated:** 2026-04-30
**Status:** Mechanical rebrand complete. Per-page content polish pending.

---

## A. Completed (live on nexsun.ai)

### A1. Brand and identity
- [x] Logo files swapped site-wide (`logo-horizontal.svg`, `logo-color.svg`) to TwoSuns wordmark (two-sun mark + Two/Suns navy/amber wordmark)
- [x] Old Nexsun horizontal logo backed up at `.logo-backups/logo-horizontal.svg.bak`
- [x] "Nexsun.ai" replaced with "TwoSuns" across 93 HTML files
- [x] Split-span `<span>Nexsun</span><span>.ai</span>` patterns cleaned up on index, about, applications, investors
- [x] Page title rewrite: "TwoSuns, Coordination Infrastructure for Complex Enterprises"

### A2. Terminology swaps (site-wide)
- [x] Personal Intelligence Assistant (PIA) → TwoSuns Assistant
- [x] System of Decision Record / SoDR → TwoSuns Core
- [x] Glassbox AI / Glassbox → Persistent Coordination
- [x] Decision Intelligence Layer / Platform → Coordination Infrastructure
- [x] Newsletter footer: "decision intelligence delivered monthly" → "enterprise insights delivered monthly"

### A3. Homepage hero rewrite
- [x] Eyebrow: "Coordination Infrastructure for the Enterprise"
- [x] Headline: "Coordination Infrastructure for Complex Enterprises"
- [x] Tagline: "Coordinate. Execute. Continue."
- [x] Subhead and body rewritten per TwoSuns brief
- [x] CTAs: "Request a Discovery Session" / "Explore the Platform"
- [x] Sun centerpiece: "Powering Decisions" → "Coordinating Execution"
- [x] Hero chips updated (earlier in session): Supply Chain Risk, Cyber Risk, Compliance Review, Geopolitical Risk

### A4. Earlier session work (also live)
- [x] Belén bio update per her April email markup
- [x] Em dash removal site-wide (CEO rule)
- [x] "in real time" / "real-time" → "continuously" / "continuous"
- [x] Credibility tweaks (Cutting-Edge, best-in-class, move faster)
- [x] Photo background darkening (Aiman, Belén, Michelle; Ryan kept original)
- [x] Site-wide nav logo swap to horizontal variant at 60px

### A5. Backup
- [x] Pre-rebrand snapshot at `/Users/mohammaddidarulalam/Documents/Claude/nexsun-backup-pre-twosuns-2026-04-30/` (87MB, full repo including git history)

---

## B. Pending, per-page content polish

These pages had brand and terminology auto-replaced, but the body copy still leans Nexsun-era. Each needs a focused content pass referencing the TwoSuns Web Content doc.

### B1. Core pages
- [ ] **index.html**, sections beyond hero: Positioning ("From Data to Decisions"), Mission/Vision, Challenge/Opportunity, Modules at a Glance, Decision Packs/Picks, Engagement Model, Industries grid
- [ ] **platform.html**, full rewrite. Currently still describes Energy Triad and decision intelligence modules
- [ ] **about.html**, founder bios, Built by Operators, Operating Model. Quotes still in Nexsun voice
- [ ] **why-nexsun.html**, structural rewrite. Filename also needs rename to `why-twosuns.html`
- [ ] **how-it-works.html**, replace Sense/Analyze/Position/Align/Commit/Record lifecycle with TwoSuns coordination model
- [ ] **applications.html**, 5 sections built around Decision Intelligence applications. Reframe around Horizon/Forge/Core
- [ ] **engage.html**, structured pilots messaging. Update to TwoSuns engagement model with 4 phases

### B2. Supporting pages
- [ ] **modules.html**, rebuild around Horizon, Forge, Core (currently shows Nexsun modules)
- [ ] **technology.html**, currently describes Nexsun's tech stack. Update to TwoSuns architecture
- [ ] **investors.html**, "What TwoSuns Owns" section, pitch deck-style content
- [ ] **partners.html**, partner program tiers
- [ ] **trust.html**, security and governance language
- [ ] **contact.html**, departmental email addresses (info@, invest@) might need TwoSuns equivalents
- [ ] **press.html**, press releases under Nexsun branding need re-dating or archival note
- [ ] **careers.html**, "Enterprise-Grade AI" value cards may need TwoSuns alignment
- [ ] **pricing.html**, pricing tiers around Decision Packs / Picks
- [ ] **use-cases.html**, 12 use cases under Nexsun framing
- [ ] **resources.html**, content hub structure
- [ ] **product.html**, currently overlaps with platform.html, may consolidate
- [ ] **industries.html**, energy/commodities-heavy. Broaden per Aiman's directive
- [ ] **book-discovery.html**, discovery call landing page
- [ ] **solutions-market-intelligence.html / solutions-contract-analytics.html / solutions-risk-management.html**, three solution-specific pages. May restructure as Horizon (market) and Forge (operations) entries

### B3. Blog and articles
- [ ] 11 blog posts under `blog/` written in Nexsun voice. Decide: keep with archival note, rewrite, or remove
- [ ] Author bios mention "Founder, Nexsun.ai" in post-10 and similar

### B4. Solar SEO pages
- [ ] 49 solar city pages built as Nexsun pSEO. Currently still pitch Nexsun decision intelligence to solar buyers
- [ ] Decide: keep with TwoSuns rebrand (auto-replaced), rewrite for new market angle, or remove entirely
- [ ] Template at `seo/solar-city-template.html` also needs review

---

## C. New TwoSuns sections to add (not yet on site)

From the TwoSuns Web Content doc, these sections are net-new and have no current page equivalent. Decide where to surface them.

- [ ] **Section 2, The Enterprise Challenge** ("Modern Organizations Operate in Fragments"). Lands well on homepage or as standalone "Why Coordination" page
- [ ] **Section 3, What is TwoSuns** ("A Persistent Coordination Layer Across the Enterprise"). Could replace the current Positioning section on homepage
- [ ] **Section 4, The TwoSuns Assistant** (persistent enterprise assistance). Slot into modules.html or new `assistant.html`
- [ ] **Section 5, Platform Structure with Core / Horizon / Forge** cards. Restructure platform.html or modules.html
- [ ] **Section 6, Iterative Operational Environments**. Could be a section on platform.html
- [ ] **Section 7, Decision Picks and Decision Packs**, expanded. Update existing "How TwoSuns Is Applied" section on homepage
- [ ] **Section 8, Enterprise Integration**. New section, could land on platform.html or technology.html
- [ ] **Section 9, Enterprise Environments** with 3 tables (Environments / Functional Areas / Strategic Sectors). New section, fits on industries.html or applications.html
- [ ] **Section 10, Engagement Model** with 4 phases. Update engage.html
- [ ] **Section 11, Closing**, "AI will not replace organizations. Organizations that coordinate execution will replace those that do not."

---

## D. Assets to refresh

- [ ] **Favicon** at `logo-mini.svg`. Currently sun-only mini, brand-neutral. Could update to TwoSuns mini-mark with both suns
- [ ] **og-image.jpg** at site root. Currently Nexsun-branded social share image. Generate TwoSuns version
- [ ] **PDFs / docs in `Logos 2/` kit folder**. Currently has Nexsun logo files. Generate TwoSuns kit
- [ ] **Press kit assets at press.html**. Reference Nexsun bios, headshots labeled with Nexsun roles

---

## E. URL and infrastructure

- [ ] Rename `why-nexsun.html` to `why-twosuns.html` and update all internal links
- [ ] Rename `book-discovery.html`? Could stay since it's generic
- [ ] Decide on domain. nexsun.ai is current. If acquiring twosuns.ai, plan redirect strategy
- [ ] Update sitemap.xml with any URL renames
- [ ] Update robots.txt if needed
- [ ] Schema.org markup on each page references "Nexsun.ai" name. Update to "TwoSuns"
- [ ] LinkedIn URL placeholder updated to `linkedin.com/company/twosuns` (page doesn't exist yet, needs to be created)
- [ ] X/Twitter URL placeholder updated to `x.com/TwoSunsAI` (handle doesn't exist yet)

---

## F. Notes and tradeoffs

- The homepage hero retune is in place but the rest of the homepage (Positioning, Why TwoSuns, Modules at a Glance, etc.) still uses Nexsun-era structure. Visually consistent (brand applied), but messaging deeper down still leans on Decision Intelligence framing rather than Coordination Infrastructure framing
- "Decision Picks" and "Decision Packs" are KEPT in the TwoSuns brief, so those terms are still valid and don't need to change
- The cinematic Tatooine reference in the TwoSuns doc is not yet surfaced anywhere. Could be a small homage in a brand film or About page
- The TwoSuns Web Content doc has design guidance (cinematic, restrained, etc.) that mostly aligns with the existing Nexsun design system. No major visual overhaul needed unless desired

---

## G. Working rules carried forward

- No em dashes anywhere. Use commas. CEO rule.
- Never false-verify. Read files back after edits.
- Brainstorm mode for new content directions. Capture, discuss, wait for go-ahead before implementing.
- Backups preserved at `nexsun-backup-pre-twosuns-2026-04-30/` and `.logo-backups/` if revert needed.
