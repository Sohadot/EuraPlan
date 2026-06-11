# FUNDING_LAYER_INTEGRATION_REVIEW.md

**Sprint:** 5B — Funding Layer Integration Review  
**Asset:** EuraPlan.com  
**Review date:** 2026-06-06  
**Status:** Internal — not published, not in sitemap, not linked from public navigation  
**Governed by:** ROUTE_GOVERNANCE.md, REFERENCE_CORPUS_GOVERNANCE.md, DEC-039, DEC-043, ACCEPTANCE_CRITERIA.md

---

## 1. Title and status

**Funding Layer Integration Review — Sprint 5B**  
**Status:** Complete — funding layer accepted as part of governed corpus

Horizon Europe page (`EP-FUND-001`) was created in Sprint 5A (DEC-039). This sprint audits integration without rebuilding the page.

---

## 2. Purpose

Confirm that `/funding/horizon-europe/` integrates cleanly with the existing EuraPlan system after Layer 4 (Funding Reference) activation:

**Regulation × Country × Sector × Funding**

Verify route registry, indexation, internal links, sources, claim boundaries, structured data, accessibility, security, and provenance alignment. Apply minimal corrections only where defects are found.

---

## 3. Scope

**Primary audit target:**

| Route ID | Path |
|---|---|
| EP-FUND-001 | `/funding/horizon-europe/` |

**Inbound / outbound link audit:**

- `index.html`, `enter/index.html`, `standard/eers/index.html`, `protocol/index.html`
- `sector/ai-saas/index.html`
- `country/germany/index.html`, `country/netherlands/index.html`, `country/france/index.html`
- `sources/index.html`, `governance/index.html`
- `routes.json`, `sitemap.xml`, `robots.txt`
- `DECISION_LOG.md`, `PROVENANCE.md`, `CHAIN_OF_CUSTODY.md`, `ASSET_TRANSFER_MANIFEST.md`, `STRUCTURED_DATA_COVERAGE_AUDIT.md`

**Excluded from scope:** New funding pages, EIC/ERDF references, matrix publication, public HTML redesign.

---

## 4. Funding route inventory

| Route ID | Path | Ontology | Publication |
|---|---|---|---|
| EP-FUND-001 | `/funding/horizon-europe/` | `funding_reference` | published |

No other funding routes published. No EIC, ERDF, or Digital Europe pages in corpus.

---

## 5. Route registry audit — PASS (fixes applied)

**EP-FUND-001 fields verified:**

| Field | Status |
|---|---|
| `route_id` | EP-FUND-001 ✓ |
| `path` | `/funding/horizon-europe/` ✓ |
| `title` | Horizon Europe Entry Planning Reference ✓ |
| `ontology_role` | `funding_reference` ✓ |
| `indexable` | true ✓ |
| `sitemap` | true ✓ |
| `publication_status` | published ✓ |
| `content_status` | complete ✓ |
| `source_requirement` | Tier 1 official / official institutional ✓ |
| `required_internal_links` | Core, regulations, countries, sector, doctrine routes ✓ |

**Fix applied (Sprint 5B):** `required_internal_links` parity — added `/funding/horizon-europe/` to routes that link to funding in HTML but lacked registry entry: EP-R-002 (enter), EP-R-005 (eers), EP-R-006 (protocol), EP-SECTOR-001, EP-COUNTRY-001/002/003.

---

## 6. Sitemap audit — PASS

`sitemap.xml` contains **17** approved public URLs.

Funding URL present:

`https://euraplan.com/funding/horizon-europe/` (`lastmod: 2026-06-06`)

**Breakdown:** Core 8 · Regulation 4 · Country 3 · Sector 1 · Funding 1

**Excluded (confirmed absent):** `/matrix/`, `/brief/`, `/diagnostic`, draft/internal routes.

No sitemap changes required in Sprint 5B.

---

## 7. Robots audit — PASS

- `Allow: /funding/` — present ✓
- `/funding/horizon-europe/` not blocked ✓
- Existing disallows unchanged: `/diagnostic?`, `/draft/`, `/internal/`, `/brief/`, `/matrix/` ✓
- `Sitemap: https://euraplan.com/sitemap.xml` ✓

No robots changes required in Sprint 5B.

---

## 8. Internal link audit — PASS (fix applied)

### Outbound from EP-FUND-001

| Target class | Status |
|---|---|
| Core: `/`, `/enter/`, `/clock/`, `/standard/eers/`, `/protocol/`, `/sources/`, `/governance/` | PRESENT ✓ |
| Regulations (4) | PRESENT ✓ |
| Countries (3) | PRESENT ✓ |
| Sector `/sector/ai-saas/` | PRESENT ✓ |

### Inbound to EP-FUND-001

| Page | Link context | Status |
|---|---|---|
| `/enter/` | Intelligence outputs nav + funding situation card | PRESENT ✓ (card link added Sprint 5B) |
| `/standard/eers/` | DIM-05 + funding readiness section | PRESENT ✓ |
| `/protocol/` | Step 08 pathway + step detail | PRESENT ✓ |
| `/sector/ai-saas/` | Control room nav | PRESENT ✓ |
| `/country/germany/` | Control room nav | PRESENT ✓ |
| `/country/netherlands/` | Control room nav | PRESENT ✓ |
| `/country/france/` | Control room nav | PRESENT ✓ |
| `/` (homepage) | — | Not linked (optional; not cluttered) ✓ |

Regulation pages: no funding links required — regulation-first layering preserved ✓

**Fix applied:** `/enter/` "Exploring EU funding" situation card — added Horizon Europe reference link; softened "eligibility conditions" to "planning context".

---

## 9. Source governance audit — PASS

**5 Tier 1 official sources** on EP-FUND-001:

1. EUR-Lex CELEX:32021R0695 (Horizon Europe Regulation)
2. EC Horizon Europe programme page
3. EC Funding and Tenders Portal
4. Horizon Europe Strategic Plan 2025–2027
5. European Innovation Council (official)

| Check | Status |
|---|---|
| Official / official-institutional only | PASS ✓ |
| Source table `<caption>` | PASS ✓ |
| Scoped `<th scope="col">` | PASS ✓ |
| Source confidence badges with readable text | PASS ✓ |
| External links `rel="noopener noreferrer"` | PASS ✓ |
| No grant-writing / SEO / consultancy sources | PASS ✓ |
| No AI-generated summaries as sources | PASS ✓ |

**Defects found: none.**

---

## 10. Claim and advice-boundary audit — PASS (fix applied)

| Prohibited pattern | Status |
|---|---|
| Eligibility determination | Not claimed — explicitly disclaimed ✓ |
| Funding / grant guarantee | Not claimed — "does not guarantee funding outcomes" ✓ |
| Official endorsement | Not claimed ✓ |
| Legal / tax / compliance / investment advice | Disclaimed in hero + scope limits ✓ |
| Country recommendation / "best country" | FRD-04 used "optimal" — **FIXED** to planning language |

**Fix applied:** FRD-04 description — removed "optimal" ranking implication; added "not a country recommendation".

Protocol step 08 uses "eligibility" in planning-mapping context (assess relevance, not determine outcome) — acceptable under `CLAIM_POLICY.md` ✓

**Defects found: 1 (corrected).**

---

## 11. Structured data audit — PASS

| Check | Status |
|---|---|
| Schema: Article + BreadcrumbList | PASS ✓ |
| Valid JSON (2 blocks) | PASS ✓ |
| `canonical` matches `url` / `mainEntityOfPage` | `https://euraplan.com/funding/horizon-europe/` ✓ |
| `dateModified` | 2026-06-06 ✓ |
| `inLanguage` | en ✓ |
| No Offer, Product, Review, Rating, Service schema | PASS ✓ |
| No fake endorsement schema | PASS ✓ |

Recorded in `STRUCTURED_DATA_COVERAGE_AUDIT.md` as compliant (not modified in Sprint 5B).

**Defects found: none.**

---

## 12. Accessibility audit — PASS

| Check | Status |
|---|---|
| One clear `<h1>` | PASS — "Horizon Europe Entry Planning Reference" ✓ |
| Semantic heading order | PASS ✓ |
| Matrix table `<caption>` | PASS ✓ |
| Source table `<caption>` | PASS ✓ |
| Table headers `scope="col"` | PASS ✓ |
| Badges text-readable | PASS ✓ |
| No important content in images only | PASS ✓ |
| No new overflow / focus defects introduced | PASS ✓ |

**Defects found: none.**

---

## 13. Security and dependency audit — PASS

| Check | Status |
|---|---|
| No external scripts (JSON-LD only) | PASS ✓ |
| No trackers / forms / cookies | PASS ✓ |
| No iframe embeds | PASS ✓ |
| No inline event handlers | PASS ✓ |
| No API keys | PASS ✓ |
| Local CSS/assets only | PASS ✓ |

Production security headers remain governed by DEC-041 — unchanged by funding layer.

**Defects found: none.**

---

## 14. Provenance / custody audit — PASS

| Document | Funding layer coverage | Status |
|---|---|---|
| `PROVENANCE.md` | Route corpus map includes funding (1 URL) | CURRENT ✓ |
| `CHAIN_OF_CUSTODY.md` | Sprint 5A Horizon Europe milestone recorded | CURRENT ✓ |
| `ASSET_TRANSFER_MANIFEST.md` | Funding reference in transfer components | CURRENT ✓ |
| `DECISION_LOG.md` | DEC-039 records Sprint 5A activation | CURRENT ✓ |

No provenance document updates required in Sprint 5B.

---

## 15. Defects found

| # | Defect | Severity | Location |
|---|---|---|---|
| 1 | FRD-04 used "optimal" — implied country ranking | Medium | `funding/horizon-europe/index.html` |
| 2 | `/enter/` funding situation card lacked direct Horizon Europe link | Low | `enter/index.html` |
| 3 | `routes.json` missing `/funding/horizon-europe/` in `required_internal_links` for pages that link to funding | Low | `routes.json` (7 routes) |

---

## 16. Fixes applied

| Fix | File(s) |
|---|---|
| FRD-04 wording — planning context, no country recommendation | `funding/horizon-europe/index.html` |
| Enter funding card — Horizon Europe link + "planning context" wording | `enter/index.html` |
| Route registry link parity for funding inbound routes | `routes.json` |

No sitemap, robots, or new public page changes.

---

## 17. Final sign-off

| Audit area | Result |
|---|---|
| Route registry | **PASS** (parity fixes applied) |
| Sitemap | **PASS** |
| Robots | **PASS** |
| Internal links | **PASS** (enter card fix) |
| Source governance | **PASS** |
| Claim / advice boundary | **PASS** (FRD-04 fix) |
| Structured data | **PASS** |
| Accessibility | **PASS** |
| Security / dependencies | **PASS** |
| Provenance / custody | **PASS** |

**Funding layer integration: APPROVED**

Layer 4 (Funding Reference) is accepted as part of the governed public corpus. Horizon Europe (`EP-FUND-001`) integrates with regulation, country, and sector layers without advice framing, unsupported claims, or indexation defects.

---

## 18. Recommendation for next sprint

**Option A (recommended): Sprint 5C — EuraPlan Agent Readability / Machine Trust Hardening**

Harden agent-facing readability: `llms.txt` or equivalent discovery file, machine-readable corpus index, conservative expansion of `AGENT_READABILITY_POLICY.md` implementation — builds on DEC-042 structured data closure.

**Option B: Sprint 6A — Second Sector Reference (Cloud/Data Infrastructure)**

Only after funding layer sign-off (this review). Requires new DEC entry and Wave 1 sector expansion decision.

**Not recommended immediately:** Second funding page (EIC, ERDF) — expand funding layer only after agent-readability hardening or explicit owner decision.

---

*Internal document — not in sitemap, not linked from public navigation.*
