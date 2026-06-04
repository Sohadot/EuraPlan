# REGULATORY_STACK_INTEGRATION_REVIEW.md

**Sprint:** 2E — Regulatory Stack Integration Review  
**Asset:** EuraPlan.com  
**Review date:** 2026-06-04  
**Status:** Internal — not published, not in sitemap, not linked from public navigation  
**Governed by:** ROUTE_GOVERNANCE.md, REFERENCE_CORPUS_GOVERNANCE.md, ACCEPTANCE_CRITERIA.md

---

## 1. Stack Routes Reviewed

| Route ID | Path | Publication |
|----------|------|-------------|
| EP-REG-001 | `/regulation/eu-ai-act/` | published |
| EP-REG-002 | `/regulation/gdpr/` | published |
| EP-REG-003 | `/regulation/eu-data-act/` | published |
| EP-REG-004 | `/regulation/cyber-resilience-act/` | published |

Supporting integration routes audited: `EP-R-003` (`/clock/`), `EP-R-002` (`/enter/`), `EP-R-001` (`/`), plus `sitemap.xml` and `robots.txt`.

---

## 2. Route Registry Audit — PASS

- All four regulation `route_id` values are unique (EP-REG-001 through EP-REG-004).
- All four paths are unique under `/regulation/`.
- `ontology_role`: `regulation_reference` on all four.
- `indexable`: true, `sitemap`: true, `content_status`: complete, `publication_status`: published on all four.
- `required_internal_links` on each regulation page include `/`, `/enter/`, `/clock/`, peer regulation paths, `/standard/eers/`, `/protocol/`, `/sources/`, `/governance/`.
- No combinatorial, country, sector, funding, brief, or published matrix routes.
- `EP-R-004` matrix remains `indexable: false`, `publication_status: draft`.
- `EP-R-010` diagnostic remains `sitemap: false`, `publication_status: planned`.

**Fix applied (Sprint 2E):** `EP-R-003` (`/clock/`) `content_status` and `source_requirement` updated to reference all four Wave 1 regulation pages (previously cited only AI Act and GDPR).

---

## 3. Sitemap Audit — PASS

`sitemap.xml` contains exactly **12** approved public URLs:

**Core (8):** `/`, `/enter/`, `/clock/`, `/standard/eers/`, `/protocol/`, `/sources/`, `/governance/`, `/acquire/`

**Regulation (4):** `/regulation/eu-ai-act/`, `/regulation/gdpr/`, `/regulation/eu-data-act/`, `/regulation/cyber-resilience-act/`

**Excluded (confirmed absent):** `/diagnostic`, `/matrix/`, `/brief/`, `/draft/`, `/internal/`, country, sector, funding routes.

No sitemap changes required in Sprint 2E.

---

## 4. Robots Audit — PASS

- `Allow: /regulation/` — all four regulation pages crawlable.
- `Allow: /assets/` — present.
- `Disallow: /diagnostic?`, `/draft/`, `/internal/`, `/brief/`, `/matrix/` — present.
- `Sitemap: https://euraplan.com/sitemap.xml` — correct.

No robots changes required in Sprint 2E.

---

## 5. Regulatory Clock / Date Audit — PASS

### CRA (post Sprint 2D-RC1)

Repository search for incorrect variants (`10 September 2026`, `September 10, 2026`, `2026-09-10`): **no matches**.

Official timing consistent on `/clock/` and `EP-REG-004`:

| Phase | Date |
|-------|------|
| Entry into force | 10 December 2024 |
| Chapter IV (CAB notification) | 11 June 2026 |
| Article 14 reporting | 11 September 2026 |
| Full application (Art. 71.1) | 11 December 2027 |

### EU Data Act

- Entry into force: 11 January 2024 — consistent (`/clock/`, EP-REG-003).
- Full application: 12 September 2025 (Art. 50) — consistent.

### EU AI Act

- Article 113 phases on `/clock/` and EP-REG-001 align (Aug 2024 entry; Feb 2025, Aug 2025, Aug 2026, Aug 2027 milestones).

### GDPR

- Treated as baseline applicable since May 25, 2018 — no future countdown invented on regulation pages.
- `/clock/` lists Art. 83 maximum fines with regulation citation — sourced administrative fine framework, not unsupported penalty marketing.

No date defects found requiring correction in Sprint 2E.

---

## 6. Internal Link Graph — PASS (minor fixes applied)

### Reciprocal stack links

| Page | GDPR | Data Act | CRA | AI Act |
|------|------|----------|-----|--------|
| EP-REG-001 | Yes | Yes | Yes | — |
| EP-REG-002 | — | Yes | Yes | Yes |
| EP-REG-003 | Yes | — | Yes | Yes |
| EP-REG-004 | Yes | Yes | — | Yes |

Each page includes contextual body links (coordination, EERS, role panels, matrix snippet) plus nav block listing peer references. Links are contextual, not footer spam.

### Integration routes

- `/clock/`: all four regulation references in lane labels and timeline list.
- `/enter/`: all four regulation gate links on regulatory exposure gate.
- `/`: single contextual CRA link in clock preview paragraph (not cluttered).

**Fixes applied (Sprint 2E):**

- EP-REG-003: EERS DIM-01 peer links completed (AI Act, GDPR).
- EP-REG-003: Tier 1 sources footer — CRA added.
- EP-REG-001: Cross-regulation coordination — CRA parallel-track sentence added.
- EP-REG-002: Tier 1 sources footer — full stack related links (was AI Act only).

No broken internal links identified.

---

## 7. Source and Claim Governance — PASS

All four regulation pages include:

- Visible Tier 1 source tables with confidence badges.
- Planning-intelligence disclaimers (not legal advice).
- No commercial blogs as primary authority.
- No fake statistics, partnership claims, or EU endorsement implication.
- No final applicability determinations for readers.

No claim defects requiring correction.

---

## 8. Structured Data — PASS

All four regulation pages use:

- `Article` JSON-LD with `dateModified: 2026-06-04` matching visible Last Updated telemetry.
- `BreadcrumbList` JSON-LD (2 items).
- Canonical URLs match published paths.
- No `AggregateRating`, reviews, or unsupported regulatory classification schema.

No structured data defects requiring correction.

---

## 9. Mobile and Accessibility — PASS (no code changes)

Reviewed against existing Sprint 1C control-room CSS:

- One `<h1>` per regulation page and `/clock/`.
- Matrix snippets use `.matrix-snippet-wrap` scroll containers.
- Clock preview lanes use established responsive patterns.
- Tables include `<caption>` and `scope` on headers.
- Badges include text labels (Tier 1, claim risk, verified).
- No additional CSS changes required for Sprint 2E gate.

---

## 10. Security and Technical — PASS

- JavaScript limited to JSON-LD `<script type="application/ld+json">` blocks on regulation pages.
- No third-party scripts, trackers, forms, cookies, API keys, inline event handlers, canvas, WebGL, or 3D.
- External links use `rel="noopener noreferrer"` on official EU sources.

---

## 11. Defects Found and Fixed (Sprint 2E)

| Defect | Fix |
|--------|-----|
| `/clock/` route metadata cited only AI Act + GDPR | `routes.json` EP-R-003 updated for all four regulation references |
| EP-REG-003 EERS DIM-01: AI Act/GDPR unlinked while CRA linked | Added links to `/regulation/eu-ai-act/` and `/regulation/gdpr/` |
| EP-REG-003 sources footer missing CRA | Added CRA to Related links |
| EP-REG-001 coordination section omitted CRA for digital products | Added CRA parallel-track sentence with link |
| EP-REG-002 sources footer listed only AI Act reciprocally | Expanded to AI Act, Data Act, CRA |

---

## 12. Defects Deferred (intentional)

| Item | Rationale |
|------|-----------|
| `EP-R-002` `/enter/` `required_internal_links` omits regulation paths | HTML provides all four gate links; registry list is minimum set — expand in a future route-registry pass if policy requires parity |
| GDPR Art. 83 fine text on `/clock/` | Sourced to Regulation (EU) 2016/679 Art. 83; administrative fine framework, not marketing claim — retained |
| `EP-R-010` diagnostic `indexable: true` while planned | Pre-existing Phase 3 registry state; blocked by robots `Disallow: /diagnostic?` and absent from sitemap |

---

## 13. Country Layer Gate Decision

**APPROVED** to begin `/country/germany/` (Sprint 2F or next country sprint per REFERENCE_CORPUS_GOVERNANCE.md Wave 1).

**Prerequisites met:**

- Wave 1 core four regulation references published and integrated.
- Route registry, sitemap, and robots aligned.
- CRA date integrity verified (Sprint 2D-RC1 + Sprint 2E re-audit).
- Internal link graph coherent across regulation stack, `/clock/`, and `/enter/`.
- No blockers identified.

**Country sprint must not:** publish matrix, brief, diagnostic, or combinatorial URLs; must follow PAGE_BLUEPRINT_STANDARD.md and Tier 1 country sourcing.

---

*Internal document — EuraPlan.com — Asset owned by Sohadot.*
