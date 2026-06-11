# STRUCTURED_DATA_COVERAGE_AUDIT.md
**Status:** Internal — Sprint 4F audit record  
**Asset:** EuraPlan.com  
**Date:** 2026-06-04  
**Sprint:** 4F — Structured Data Completion

---

## 1. Title and status

**Structured Data Coverage Audit — Sprint 4F**  
**Status:** Complete — core category pages now policy-aligned

---

## 2. Purpose

Record structured data coverage before and after Sprint 4F. Close the governance-to-implementation gap identified in due diligence: `STRUCTURED_DATA_POLICY.md` required schema by page type, but eight core category pages lacked JSON-LD while reference pages already had Article + BreadcrumbList blocks.

---

## 3. Pages audited

| Route | File |
|---|---|
| `/` | `index.html` |
| `/enter/` | `enter/index.html` |
| `/clock/` | `clock/index.html` |
| `/standard/eers/` | `standard/eers/index.html` |
| `/protocol/` | `protocol/index.html` |
| `/sources/` | `sources/index.html` |
| `/governance/` | `governance/index.html` |
| `/acquire/` | `acquire/index.html` |

Reference corpus (audited for compliance status only — not modified in Sprint 4F):

- `/regulation/eu-ai-act/`, `/regulation/gdpr/`, `/regulation/eu-data-act/`, `/regulation/cyber-resilience-act/`
- `/country/germany/`, `/country/netherlands/`, `/country/france/`
- `/sector/ai-saas/`
- `/funding/horizon-europe/`

---

## 4. Existing structured data coverage before Sprint 4F

| Page | Pre-4F JSON-LD |
|---|---|
| `/` | None |
| `/enter/` | None |
| `/clock/` | None |
| `/standard/eers/` | None |
| `/protocol/` | None |
| `/sources/` | None |
| `/governance/` | None |
| `/acquire/` | None |
| Regulation pages (4) | Article + BreadcrumbList |
| Country pages (3) | Article + BreadcrumbList |
| `/sector/ai-saas/` | Article + BreadcrumbList |
| `/funding/horizon-europe/` | Article + BreadcrumbList |

**Gap:** All eight core category/doctrine pages lacked JSON-LD despite `STRUCTURED_DATA_POLICY.md` Section 3 requirements.

---

## 5. Schema required by STRUCTURED_DATA_POLICY.md

| Page type | Primary | Secondary |
|---|---|---|
| Homepage | WebSite | Organization |
| Standard page | Article | BreadcrumbList |
| Protocol page | Article | BreadcrumbList |
| Source / Governance pages | WebPage | BreadcrumbList |
| Acquisition page | WebPage | BreadcrumbList |
| Entry gateway / Clock (core surfaces) | WebPage | BreadcrumbList (applied per Sprint 4F scope) |

---

## 6. Schema added per page (Sprint 4F)

| Route | Schema added |
|---|---|
| `/` | `WebSite`, `Organization` |
| `/enter/` | `WebPage`, `BreadcrumbList` |
| `/clock/` | `WebPage`, `BreadcrumbList` |
| `/standard/eers/` | `Article`, `BreadcrumbList` |
| `/protocol/` | `Article`, `BreadcrumbList` |
| `/sources/` | `WebPage`, `BreadcrumbList` |
| `/governance/` | `WebPage`, `BreadcrumbList` |
| `/acquire/` | `WebPage`, `BreadcrumbList` |

Implementation: inline `<script type="application/ld+json">` in `<head>`, aligned with verified baseline CSP (`script-src 'self' 'unsafe-inline'`).

---

## 7. Pages already compliant and not modified

| Route | Existing schema |
|---|---|
| `/regulation/eu-ai-act/` | Article + BreadcrumbList |
| `/regulation/gdpr/` | Article + BreadcrumbList |
| `/regulation/eu-data-act/` | Article + BreadcrumbList |
| `/regulation/cyber-resilience-act/` | Article + BreadcrumbList |
| `/country/germany/` | Article + BreadcrumbList |
| `/country/netherlands/` | Article + BreadcrumbList |
| `/country/france/` | Article + BreadcrumbList |
| `/sector/ai-saas/` | Article + BreadcrumbList |
| `/funding/horizon-europe/` | Article + BreadcrumbList |

---

## 8. Prohibited schema avoided

Sprint 4F did not add:

- `Product`, `Offer`, `Service`
- `AggregateRating`, `Review`
- `Event` (regulatory milestones as events)
- `award`, `certification`, `memberOf`
- `sameAs` to EU institutions
- Price or marketplace listing schema
- Unsupported valuation, eligibility, compliance guarantee, or endorsement claims

---

## 9. JSON validation notes

- All JSON-LD blocks use valid JSON syntax (double-quoted keys/strings, no trailing commas).
- `@context`: `https://schema.org` on all blocks.
- Canonical URLs in `url`, `mainEntityOfPage`, and `BreadcrumbList` items match page `<link rel="canonical">` values.
- `dateModified`: `2026-06-04` on WebPage and Article blocks (project convention).
- `inLanguage`: `en` on all applicable blocks.
- Repository validation: extract and `JSON.parse` each `application/ld+json` block before commit.

---

## 10. Remaining limitations

- **Acquire page:** Policy table lists WebPage only; Sprint 4F added BreadcrumbList for navigation consistency with other core pages — conservative, not commercial listing schema.
- **No `WebPage` on homepage:** Homepage uses WebSite + Organization per policy; no BreadcrumbList required.
- **Reference pages:** Not re-audited for description drift vs visible copy in this sprint.
- **No rich-result testing:** Google Rich Results Test not run in sprint — JSON validity confirmed in repository only.
- **Organization `contactPoint`:** Uses documented `agent@sohadot.com` per `STRUCTURED_DATA_POLICY.md` Section 5 — no `sameAs`.

---

## 11. Future CSP / hash-based hardening recommendation

After schema coverage stabilizes across the full public corpus:

1. Inventory all inline JSON-LD blocks and inline `style` attributes.
2. Evaluate hash-based CSP (`script-src 'sha256-…'`) or externalized JSON-LD files if hosting layer supports non-inline delivery without agent-readability loss.
3. Re-verify production headers after any CSP tightening (DEC-040, DEC-041).
4. Record superseding decision in `DECISION_LOG.md` before removing `'unsafe-inline'` from `script-src`.

**Sprint 4F decision:** Keep JSON-LD inline under current verified baseline CSP. Defer hash-based hardening to a later sprint.

---

*Internal document — not in sitemap, not linked from public navigation.*
