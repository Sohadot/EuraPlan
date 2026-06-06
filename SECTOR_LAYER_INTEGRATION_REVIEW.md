# SECTOR_LAYER_INTEGRATION_REVIEW.md

Sprint: Sprint 4B — Sector Layer Integration Review  
Reviewed: 2026-06-06  
Branch: claude/sector-layer-integration-audit-Umx6V  
Governing document: ROUTE_GOVERNANCE.md and all bound governance files  

---

## Sector Route Reviewed

| Field | Value |
|---|---|
| Route ID | EP-SECTOR-001 |
| Path | /sector/ai-saas/ |
| Ontology role | sector_reference |
| Publication status | published |
| Content status | complete |
| Indexable | yes |
| Sitemap | yes |

---

## 1. Route Registry Audit

**Result: PASS**

- EP-SECTOR-001 exists in routes.json ✓
- Route ID is unique across the registry ✓
- Path /sector/ai-saas/ is unique ✓
- ontology_role = sector_reference ✓
- indexable: true ✓
- sitemap: true ✓
- publication_status: published; content_status: complete ✓
- All 14 required_internal_links are accurate and resolve to published routes ✓
- No accidental additional sector, funding, matrix, brief, diagnostic, country, regulation, or combinatorial routes present ✓
- /matrix/country-sector-regulation/ correctly marked draft, indexable:false, sitemap:false ✓
- /diagnostic correctly marked planned, sitemap:false; robots disallows only query states (/diagnostic?) not the base path ✓

**Defects found: none.**

---

## 2. Sitemap Audit

**Result: PASS**

Contains exactly the 16 approved public routes:

| Route |
|---|
| https://euraplan.com/ |
| https://euraplan.com/enter/ |
| https://euraplan.com/clock/ |
| https://euraplan.com/regulation/eu-ai-act/ |
| https://euraplan.com/regulation/gdpr/ |
| https://euraplan.com/regulation/eu-data-act/ |
| https://euraplan.com/regulation/cyber-resilience-act/ |
| https://euraplan.com/country/germany/ |
| https://euraplan.com/country/netherlands/ |
| https://euraplan.com/country/france/ |
| https://euraplan.com/sector/ai-saas/ |
| https://euraplan.com/standard/eers/ |
| https://euraplan.com/protocol/ |
| https://euraplan.com/sources/ |
| https://euraplan.com/governance/ |
| https://euraplan.com/acquire/ |

Does not contain: /diagnostic, diagnostic query URLs, /matrix/, /brief/, /draft/, /internal/, funding routes, additional sector routes, additional country routes, additional regulation routes ✓

All lastmod dates consistent at 2026-06-04 ✓

**Defects found: none.**

---

## 3. Robots Audit

**Result: PASS**

- /sector/ is explicitly Allowed ✓
- /country/ is explicitly Allowed ✓
- /regulation/ is explicitly Allowed ✓
- /assets/ is explicitly Allowed ✓
- /diagnostic? (query states) is Disallowed ✓
- /draft/ is Disallowed ✓
- /internal/ is Disallowed ✓
- /brief/ is Disallowed ✓
- /matrix/ is Disallowed ✓
- Sitemap URL is correct: https://euraplan.com/sitemap.xml ✓
- No published sector page is blocked ✓

**Defects found: none.**

---

## 4. Sector Differentiation Audit

**Result: PASS**

| Check | Status |
|---|---|
| Not a generic AI/SaaS article | PASS — framed as sector execution reference node throughout |
| Functions as sector execution reference node | PASS — maps regulatory exposure category, role mapping, country sequencing, planning gates |
| Links to four regulation nodes without duplicating | PASS — "Detail lives on each regulation node — not duplicated here" stated explicitly |
| Links to DE/NL/FR without ranking | PASS — "EuraPlan does not rank Germany, Netherlands, or France for AI/SaaS" stated explicitly |
| Does not claim all AI/SaaS is high-risk | PASS — "Not all SaaS is AI. Not all AI/SaaS is high-risk under the EU AI Act." |
| Does not claim all SaaS automatically subject to CRA or Data Act | PASS — conditional framing throughout: "where software/product context requires" |
| No final applicability determinations | PASS — consistent "requires mapping" framing; "does not determine applicability for any specific product or reader" |
| No unsupported market-size claims | PASS — no market statistics |
| No legal advice framing | PASS — explicit disclaimer present in hero and footer |
| No compliance advice framing | PASS — explicit disclaimer present |
| Planning-intelligence framing | PASS — consistent throughout |

**Defects found: none.**

---

## 5. Internal Link Graph Status

**Result: PASS — all required links verified present and contextually appropriate**

### Outbound from /sector/ai-saas/

| Required link | Location on sector page | Status |
|---|---|---|
| /regulation/eu-ai-act/ | Control panel card, role panels, gates, clock, matrix, nav | PRESENT ✓ |
| /regulation/gdpr/ | Control panel card, role panels, gates, matrix, nav | PRESENT ✓ |
| /regulation/eu-data-act/ | Control panel card, gates, matrix, clock footnote, nav | PRESENT ✓ |
| /regulation/cyber-resilience-act/ | Control panel card, gates, matrix, nav | PRESENT ✓ |
| /country/germany/ | Country sequencing section, S-GATE-05 | PRESENT ✓ |
| /country/netherlands/ | Country sequencing section, S-GATE-05 | PRESENT ✓ |
| /country/france/ | Country sequencing section, S-GATE-05, matrix | PRESENT ✓ |
| /enter/ | Hero CTA, nav, page footer CTA | PRESENT ✓ |
| /clock/ | Hero CTA, sector clock section, clock footnote, nav | PRESENT ✓ |
| /standard/eers/ | EERS section, multiple in-text refs | PRESENT ✓ |
| /protocol/ | Multiple in-text: protocol steps 04, 05, 12 | PRESENT ✓ |
| /sources/ | Sources section footnote, nav | PRESENT ✓ |
| /governance/ | Nav links section | PRESENT ✓ |
| / | Wordmark, nav links section | PRESENT ✓ |

### Inbound to /sector/ai-saas/

| Source page | Location | Context | Status |
|---|---|---|---|
| /enter/ | GATE-01 regulatory exposure section | "AI/SaaS companies: AI/SaaS sector reference" | PRESENT ✓ |
| /standard/eers/ | DIM-06 Product Compliance | "Sector example: AI/SaaS reference" | PRESENT ✓ |
| /regulation/eu-ai-act/ | Hero CTA (btn-secondary) | "AI/SaaS Sector Reference" | PRESENT ✓ |
| /regulation/eu-ai-act/ | DIM-01 EERS section | alongside other regulation links | PRESENT ✓ |
| /regulation/gdpr/ | DIM-01 EERS section | SaaS user-data context | PRESENT ✓ |
| /regulation/eu-data-act/ | DIM-01 EERS section | SaaS/cloud/data context | PRESENT ✓ |
| /regulation/cyber-resilience-act/ | DIM-01 EERS section | software with digital elements context | PRESENT ✓ |
| /country/germany/ | Technology Entry Planning section | enterprise/AI governance documentation context | PRESENT ✓ |
| /country/netherlands/ | Technology Entry Planning section | digital-infrastructure / EU HQ context | PRESENT ✓ |
| /country/france/ | Technology Entry Planning section | industrial-policy / AI/data/cybersecurity context | PRESENT ✓ |

Homepage: routes.json does not require homepage → sector link; not cluttered ✓  
No broken internal links detected ✓  
No over-linking or SEO-spam patterns ✓

**Defects found: none.**

---

## 6. Source / Claim Governance Status

**Result: PASS**

- 7 Tier 1 official sources listed with badges, EUR-Lex citations, and official Commission policy links ✓
- Source confidence badges present: Tier 1 institutional + Verified ✓
- No commercial SEO/SaaS blogs or secondary sources used as primary authority ✓
- No fake statistics; no market-size claims ✓
- No partnership claims; no official endorsement implication ✓
- No legal advice framing; no compliance advice framing ✓
- No final sector classification or applicability conclusion ✓
- Claim risk badge: Medium-High (sector regulatory interpretation) — appropriate ✓

**Defects found: none.**

---

## 7. Structured Data Status

**Result: PASS**

| Check | Status |
|---|---|
| Schema type: Article | PASS — conservative ✓ |
| BreadcrumbList present | PASS — 2-item list (EuraPlan root → sector page) ✓ |
| dateModified matches visible page date | PASS — both show 2026-06-04 ✓ |
| Sitemap lastmod consistent | PASS — 2026-06-04 ✓ |
| Canonical URL correct | PASS — https://euraplan.com/sector/ai-saas/ ✓ |
| No fake reviews | PASS ✓ |
| No ratings | PASS ✓ |
| No endorsement implication | PASS ✓ |
| No unsupported sector-ranking schema | PASS ✓ |
| No executable JS (JSON-LD blocks only) | PASS ✓ |

**Defects found: none.**

---

## 8. Mobile / Accessibility Status

**Result: PASS WITH ONE DEFECT FIXED**

| Check | Status |
|---|---|
| One h1 per page | PASS — single h1 #sector-heading ✓ |
| Heading hierarchy | PASS — h1 → h2 (sections) → h3 (cards, roles, gates, dimensions) ✓ |
| Matrix table: caption present | PASS — caption: "AI/SaaS planning cross-reference snippet — EP-SECTOR-001" ✓ |
| Matrix table: scope="col" on headers | PASS ✓ |
| Source table: caption present | FIXED — was missing; added in this sprint ✓ |
| Source table: scope="col" on headers | PASS ✓ |
| Color not sole carrier of meaning | PASS — all badges carry text labels alongside colour ✓ |
| role="group" + aria-label on telemetry strip | PASS ✓ |
| role="list" / role="listitem" on readiness-grid | PASS ✓ |
| role="region" + aria-label on clock preview | PASS ✓ |
| matrix-snippet-wrap scroll containment | PASS — structural ✓ |
| Telemetry panels readable structure | PASS — dl/dt/dd structure ✓ |
| aria-hidden on decorative brand marks | PASS ✓ |
| No unintended horizontal overflow | PASS — matrix-snippet-wrap contains table scroll ✓ |

**Defect fixed:** Source list table (`ep-table`) lacked a `<caption>` element. Caption added: "Official Tier 1 sources — AI/SaaS Europe Entry Planning Reference".

Note: The `ep-table` source tables on regulation and country pages also lack captions — this is a pre-existing site-wide pattern not introduced by the sector sprint. Flagged here for the next accessibility hardening pass; not actioned in this sprint to stay within scope.

---

## 9. Security / Technical Status

**Result: PASS**

| Check | Status |
|---|---|
| No JavaScript except JSON-LD script blocks | PASS — two `<script type="application/ld+json">` blocks only ✓ |
| No third-party scripts | PASS ✓ |
| No trackers | PASS ✓ |
| No forms | PASS ✓ |
| No cookies | PASS ✓ |
| No API keys | PASS ✓ |
| No external dependencies | PASS ✓ |
| No inline event handlers | PASS ✓ |
| No unsafe embeds | PASS ✓ |
| No dynamic user input | PASS ✓ |
| No WebGL, canvas, or 3D | PASS ✓ |
| No new public pages added | PASS ✓ |
| No new sector/country/regulation/funding/matrix routes | PASS ✓ |

**Defects found: none.**

---

## 10. Defects Fixed

### Defect 1 — AI Act clock lane missing GPAI phase marker (FIXED)

**Severity:** Medium  
**Location:** `sector/ai-saas/index.html` — AI/SaaS Entry Clock section, EU AI Act lane  
**Problem:** The `aria-label` on the AI Act clock-lane-track explicitly referenced "Aug 2025" (the Art. 113.2 GPAI phase), but no visual `clock-marker` element existed for it. The sector page's role-mapping section identifies GPAI model provider as a key AI/SaaS role — this created an inconsistency between content and the timeline representation. The clock showed only 3 markers (Aug 2024, Feb 2025, Aug 2026) despite 4 being referenced in the aria label.  
**Fix:** Added a fourth `clock-marker--signal` element for Aug 2025 (Art. 113.2 GPAI); repositioned Feb 2025 from 42% → 32% and GPAI at 54% for improved visual distribution; updated the `aria-label` to precisely name all four phases.  
**Source authority:** Article 113(2) of Regulation (EU) 2024/1689 — same authority already cited on the AI Act regulation reference page.

### Defect 2 — Source table missing caption (FIXED)

**Severity:** Minor (accessibility)  
**Location:** `sector/ai-saas/index.html` — Tier 1 Source List table (`ep-table`)  
**Problem:** The `<table class="ep-table">` element lacked a `<caption>` element. The matrix table on the same page correctly had a caption. Omission creates a minor accessibility inconsistency for screen-reader users navigating directly to the table.  
**Fix:** Added `<caption>Official Tier 1 sources — AI/SaaS Europe Entry Planning Reference</caption>`.

---

## 11. Remaining Blockers

None. All audit dimensions pass. Two minor defects identified and fixed in this sprint.

**Deferred observation (not a blocker):**  
The `ep-table` source tables on the four regulation pages and three country pages consistently lack `<caption>` elements — the same accessibility gap as Defect 2 above. This is a pre-existing pattern from prior sprints, not introduced by EP-SECTOR-001. It should be addressed in a dedicated accessibility hardening pass, not in this integration sprint.

---

## 12. Approval to Begin Next Work

**Approved to begin /funding/horizon-europe/:** YES — with conditions below  
**Approved to begin a second sector:** YES — with conditions below

### Conditions

Both approvals are conditional on the following governance gates being satisfied before work begins:

1. This branch (`claude/sector-layer-integration-audit-Umx6V`) must be merged to main.
2. routes.json must be updated to register the new route (EP-FUND-001 for Horizon Europe or EP-SECTOR-002 for the next sector) before any page file is created.
3. The new route must satisfy all ROUTE_GOVERNANCE.md requirements: unique route ID, unique path, correct ontology_role, indexable/sitemap flags, and required_internal_links defined.
4. The new page must comply with all bound governance documents before publication.
5. No new routes may be registered that are not explicitly approved — do not create additional sector, country, regulation, or diagnostic routes in the same sprint.

### Recommendation

The sector layer integration is stable. EP-SECTOR-001 (/sector/ai-saas/) is correctly integrated without weakening SEO, internal link governance, route discipline, source governance, technical security, accessibility, or the European Entry Control Room interface. The two defects found were minor and have been corrected.

The site is ready to extend to either /funding/horizon-europe/ or a second sector page in the next sprint. The funding route is likely higher-value as a unique intelligence layer not yet represented in the site architecture.
