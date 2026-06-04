# REFERENCE_CORPUS_GOVERNANCE.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, ROUTE_GOVERNANCE.md, CONTENT_QUALITY_STANDARD.md

---

## 1. Corpus Identity

EuraPlan may eventually contain thousands of pages. That is not a goal — it is a consequence of governing the category at sufficient depth.

The reference corpus exists to make EuraPlan the most authoritative, most structured, most source-governed intelligence resource in the category: European Regulatory Entry Planning. Volume without depth is a content farm. Depth without volume is incomplete. Governed depth at scale is the category claim.

No page is added to the corpus to fill space, chase a keyword, or generate impressions. Every page added must close a genuine intelligence gap for the non-EU company entering Europe.

---

## 2. Corpus Layers

The EuraPlan reference corpus is organised into nine layers. Lower layers must be structurally sound before higher layers build on them.

| Layer | Type | Example Routes | Prerequisite |
|---|---|---|---|
| 0 | Doctrine pages | `/`, `/standard/eers/`, `/protocol/`, `/governance/` | Sprint 0B (complete) |
| 1 | Regulation reference pages | `/regulation/eu-ai-act/`, `/regulation/gdpr/` | Layer 0 |
| 2 | Country reference pages | `/country/germany/`, `/country/france/` | Layer 0 |
| 3 | Sector reference pages | `/sector/ai-saas/`, `/sector/medtech/` | Layer 1 |
| 4 | Origin reference pages | `/origin/us/`, `/origin/gcc/` | Layer 1 + Layer 2 |
| 5 | Funding reference pages | `/funding/horizon-europe/`, `/funding/eic/` | Layer 2 |
| 6 | Matrix pages | `/matrix/country-sector-regulation/` | Layers 1 + 2 + 3 |
| 7 | Pre-composed briefs | `/brief/us-saas-eu-ai-act-entry-2026/` | Layers 1–4 for that combination |
| 8 | Audience layer pages | `/for/lawyers/`, `/for/investors/` | Layers 1–5 |
| 9 | Multilingual versions | `/fr/regulation/eu-ai-act/` | Layers 1–8 + multilingual gate |

---

## 3. Page Status Lifecycle

All corpus pages follow this lifecycle. Skipping the Review step before publishing is a governance failure.

1. **Proposed** — Route identified in `routes.json` as `planned`, content brief drafted
2. **Approved** — All route approval requirements met, sources identified, blueprint confirmed
3. **In Development** — Content being written, sources being captured
4. **Review** — Content complete, source and claim review performed, acceptance criteria checked
5. **Published** — Live, indexable, in sitemap
6. **Under Review** — Active update in progress; page remains live
7. **Deprecated** — Removed from sitemap, redirected (301) to nearest live equivalent; no 404 for previously indexed pages

---

## 4. Expansion Waves

Expansion happens in governed waves, not continuously. Each wave requires a sprint document defining scope, source requirements, and quality gates before work begins.

**Wave 1 (Sprint 1) — Regulatory Foundation + Primary Markets:**
- 4 core regulation pages: EU AI Act, GDPR, CRA, EU Data Act
- 3 country pages: Germany, Netherlands, France
- 2 sector pages: AI/SaaS, FinTech or HealthTech
- 1 funding page: Horizon Europe
- Matrix page (built from above)

**Wave 2 (Sprint 2+) — Extended Regulatory + Market Layer:**
- 4 regulations: NIS2, DSA, DMA, MDR or PSD3
- 3 country pages: Ireland, Spain, Poland
- 3 origin pages: US, GCC, UK
- 2 sector pages: additional sectors

**Wave 3 (Sprint 3+) — Funding Depth + Brief Layer:**
- Funding pages: EIC Accelerator, ERDF, InvestEU
- First pre-composed briefs (confirmed demand from diagnostics or search data)
- Audience layer pages for primary profiles

**Wave 4+ — Scaling Layer:**
- Remaining regulation, country, sector, origin pages
- Multilingual layer (French and German first)
- API and licensing support documentation

No wave may begin before the previous wave passes its quality gate.

---

## 5. Quality Gates

**Before a new wave begins:**
- All previous wave pages have `publication_status: published`
- All previous wave pages have passed source review
- No broken internal links from previous wave
- Sitemap updated and validated
- Google Search Console shows no indexation errors for previous wave pages

**Before a single page publishes:**
- All ACCEPTANCE_CRITERIA.md requirements satisfied
- All SOURCE_POLICY.md requirements satisfied
- All CONTENT_QUALITY_STANDARD.md requirements satisfied
- All SEO_GOVERNANCE.md technical requirements satisfied
- All ACCESSIBILITY_STANDARD.md requirements satisfied
- PAGE_BLUEPRINT_STANDARD.md blueprint for the page type followed

---

## 6. Prohibited Corpus Patterns

- **Mass generation:** Generating 500 country-sector pages in one sprint without per-page source review
- **Placeholder scaling:** Publishing pages with any "content coming" sections
- **Combinatorial URL generation:** `/regulation/gdpr/country/germany/sector/saas/` — this is matrix content, not a URL tree
- **Thin reference pages:** A regulation page with three paragraphs and no source citations
- **Unreviewed translations:** Machine-translated versions without editorial governance review
- **Topic drift:** Pages on subjects that serve general EU interest but not the non-EU company planning audience
- **Automated bulk publishing:** Any automated system publishing pages to the live site without per-page human review

---

## 7. Corpus Integrity Rules

- Every page in the corpus must link to at least one other page in the corpus (no orphans)
- Every page in the corpus must be reachable from the homepage within three clicks
- No page may be published without its layer prerequisites being published first
- When a regulation is superseded or repealed, all pages citing it must be reviewed within 30 days

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
