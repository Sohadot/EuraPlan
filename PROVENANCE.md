# PROVENANCE.md
**Version:** 1.0  
**Status:** Active — Acquisition-Readiness / Internal Governance  
**Asset:** EuraPlan.com  
**Owner:** Sohadot  
**Created:** Sprint 4G — June 2026  
**Last Updated:** June 2026

---

## 1. Title and status

**EuraPlan.com — Provenance Record**  
**Status:** Active — documents origin, identity, governance basis, and development history of the governed digital asset.

This document is not a public page. It is not in `sitemap.xml` and is not linked from public navigation.

---

## 2. Asset identity

**EuraPlan.com** is a governed digital category intelligence asset focused on **European Regulatory Entry & Expansion Planning Intelligence**.

It is a **Category Intelligence Factory** — not a generic website, consulting firm, legal advice provider, or EU institution.

EuraPlan produces structured, source-governed planning intelligence for non-EU companies entering the European market. Its strategic value derives from the governed system: domain, category thesis, route architecture, source policy, decision log, reference corpus, interface system, and acquisition-readiness governance.

---

## 3. Domain

| Field | Value |
|---|---|
| Primary domain | `euraplan.com` |
| Canonical base URL | `https://euraplan.com/` |
| Public site type | Static HTML/CSS, repository-served |
| Edge layer | Cloudflare (production) |

Domain registration records are maintained outside this repository. Future due diligence should request domain registry export separately.

---

## 4. Category definition

EuraPlan claims ownership of the category: **European Regulatory Entry Planning**.

Defined as the structured, intelligence-driven process of mapping, planning, and executing market entry into Europe — accounting for regulatory exposure, country selection, funding readiness, compliance obligations, and national execution differences — before a non-EU company makes its first irreversible move.

This claim is defended through proprietary architecture (EERS, Entry Planning Protocol, Entry Ontology) and a governed reference corpus — not through institutional endorsement.

---

## 5. Core thesis

> Europe punishes absence. Europe rewards planning.

EuraPlan turns Europe's rule system into executable market, funding, and compliance entry plans — as planning intelligence, not legal, tax, compliance, incorporation, funding, grant-writing, or investment advice.

---

## 6. Conceptual origin

EuraPlan emerged from the strategic observation that non-EU AI, SaaS, and technology companies entering Europe face overlapping regulatory, country, sector, and funding planning problems — and that generic "doing business in Europe" content does not provide governed, auditable entry planning infrastructure.

The asset was conceived as **category infrastructure**: a defensible position in European Regulatory Entry Planning, built through sovereign reference pages, proprietary standards, documented governance, and source-governed claims — rather than volume content or combinatorial URL expansion.

Conceptual framing is documented in `EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md` and ratified in `GOVERNANCE_CHARTER.md`.

---

## 7. Strategic doctrine relationship

EuraPlan's strategic doctrine is recorded across governing documents:

| Doctrine element | Primary document |
|---|---|
| Category Intelligence Factory identity | `GOVERNANCE_CHARTER.md` |
| Route architecture — no combinatorial URLs | `ROUTE_GOVERNANCE.md` |
| Source tiers and citation discipline | `SOURCE_POLICY.md` |
| Claim risk classification | `CLAIM_POLICY.md` |
| European Entry Control Room interface | `INTERFACE_COMPONENT_POLICY.md`, `VISUAL_SYSTEM_GOVERNANCE.md` |
| Reference corpus waves | `REFERENCE_CORPUS_GOVERNANCE.md` |
| Acquisition thesis | `BUYER_LOGIC.md` |
| Major decisions | `DECISION_LOG.md` |

Doctrine is enforced through sprint-gated publication, `routes.json` registry, acceptance criteria, and integration review documents — not through ad hoc page creation.

---

## 8. Governance document map

### Core governing documents

`GOVERNANCE_CHARTER.md` · `DECISION_LOG.md` · `SOURCE_POLICY.md` · `CLAIM_POLICY.md` · `ROUTE_GOVERNANCE.md` · `INTERNAL_LINK_POLICY.md` · `MONETIZATION_BOUNDARY.md` · `BUYER_LOGIC.md` · `FIRST_PUBLIC_RELEASE_PLAN.md` · `ACCEPTANCE_CRITERIA.md` · `EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md`

### Companion operating documents

`TECHNICAL_STANDARD.md` · `SECURITY_POLICY.md` · `SEO_GOVERNANCE.md` · `CONTENT_QUALITY_STANDARD.md` · `REFERENCE_CORPUS_GOVERNANCE.md` · `PAGE_BLUEPRINT_STANDARD.md` · `STRUCTURED_DATA_POLICY.md` · `AGENT_READABILITY_POLICY.md` · `ACCESSIBILITY_STANDARD.md` · `PERFORMANCE_BUDGET.md` · `VISUAL_SYSTEM_GOVERNANCE.md` · `INTERFACE_COMPONENT_POLICY.md` · `SCALING_AND_AUTOMATION_POLICY.md` · `ANALYTICS_AND_INDEXATION_POLICY.md` · `MULTILINGUAL_GOVERNANCE.md`

### Internal audit / integration documents

`REGULATORY_STACK_INTEGRATION_REVIEW.md` · `COUNTRY_LAYER_INTEGRATION_REVIEW.md` · `SECTOR_LAYER_INTEGRATION_REVIEW.md` · `STRUCTURED_DATA_COVERAGE_AUDIT.md`

### Acquisition-readiness documents (Sprint 4G)

`PROVENANCE.md` · `AUTHENTICITY_CERTIFICATE.md` · `CHAIN_OF_CUSTODY.md` · `ASSET_TRANSFER_MANIFEST.md` · `RIGHTS_AND_USAGE_NOTICE.md`

---

## 9. Route corpus map

Authoritative route registry: `routes.json` (19 registered routes as of Sprint 4G).

**Published public corpus** (in `sitemap.xml`, 17 URLs):

| Layer | Routes |
|---|---|
| Core (8) | `/`, `/enter/`, `/clock/`, `/standard/eers/`, `/protocol/`, `/sources/`, `/governance/`, `/acquire/` |
| Regulation (4) | `/regulation/eu-ai-act/`, `/regulation/gdpr/`, `/regulation/eu-data-act/`, `/regulation/cyber-resilience-act/` |
| Country (3) | `/country/germany/`, `/country/netherlands/`, `/country/france/` |
| Sector (1) | `/sector/ai-saas/` |
| Funding (1) | `/funding/horizon-europe/` |

**Registered but not sitemap-published:** `/matrix/country-sector-regulation/` (unpublished), `/diagnostic` (disallowed in `robots.txt`).

Route admission, indexation, and publication status are governed by `ROUTE_GOVERNANCE.md` and `SEO_GOVERNANCE.md`.

---

## 10. Decision log relationship

`DECISION_LOG.md` is the official audit-ready decision register (established Sprint 4D). All major strategic, technical, route, source, interface, and expansion decisions are recorded as DEC-NNN entries.

Provenance-relevant closures:

| Decision | Subject |
|---|---|
| DEC-040 | Security headers — `_headers` repository artifact |
| DEC-041 | Security headers — production runtime verification (Cloudflare Transform Rule) |
| DEC-042 | Structured data — core page JSON-LD completion |
| DEC-043 | Provenance and authenticity layer (this sprint) |

No major route or policy change is governance-complete without a corresponding `DECISION_LOG.md` entry.

---

## 11. Source policy relationship

All regulatory, funding, and institutional claims on public pages trace to tiered sources defined in `SOURCE_POLICY.md`. Reference pages require Tier 1 official or official-institutional sources for regulatory applicability claims.

EuraPlan does not claim ownership of EU or government source material. EuraPlan's original contribution is framing, governance, route architecture, source organization, planning-intelligence commentary, and category system design — applied to publicly available official sources.

---

## 12. Security and structured data closure notes

### Security (Sprint 4E / 4E-RC1) — CLOSED

Production security headers verified via live HTTP capture. Runtime enforcement: Cloudflare Response Header Transform Rule **EuraPlan Security Headers**. Repository `_headers` file is Cloudflare Pages-compatible configuration; not proven as sole runtime mechanism while GitHub Pages/Fastly origin remains behind Cloudflare.

See: `SECURITY_POLICY.md` Section 8 · DEC-040 · DEC-041

### Structured data (Sprint 4F) — CLOSED

Eight core category pages received conservative inline JSON-LD per `STRUCTURED_DATA_POLICY.md`. Reference corpus pages already had Article + BreadcrumbList. Internal audit: `STRUCTURED_DATA_COVERAGE_AUDIT.md`.

See: DEC-042

---

## 13. Current limitations

- **Not an EU institution** — EuraPlan does not claim endorsement by the European Commission, EU institutions, national governments, regulators, funding bodies, universities, or partners.
- **Not legal/compliance advice** — Public pages provide planning intelligence only.
- **No formal notarization** — Provenance records are repository-level, not notarized legal documents.
- **No trademark registration claimed** — Unless separately documented by owner outside this repository.
- **Domain/registry custody** — Domain WHOIS and registrar records are not embedded in this file.
- **Hosting path** — Origin may be GitHub Pages/Fastly behind Cloudflare; full infrastructure export requires separate due diligence.
- **Matrix and diagnostic** — Unpublished or disallowed routes remain in registry for architecture continuity.

---

## 14. Provenance statement

EuraPlan.com, as represented in the Sohadot-governed repository, is a deliberately constructed category intelligence asset. Its provenance is established through:

1. Documented category identity and thesis (`GOVERNANCE_CHARTER.md`)
2. Sequential sprint development with merge commits in version control
3. A numbered decision register (`DECISION_LOG.md`)
4. A route registry (`routes.json`) aligned with `sitemap.xml` and `robots.txt`
5. Source-governed reference corpus with Tier 1 institutional citations
6. Security header runtime verification (DEC-041)
7. Structured data implementation audit (DEC-042)
8. Acquisition-readiness provenance layer (DEC-043)

This statement describes what the asset is and how it was built. It does not constitute a legal ownership transfer, valuation, or institutional endorsement.

---

## 15. Future provenance hardening

Recommended future improvements (not implemented in Sprint 4G):

- Signed release tags per major sprint closure
- Timestamped repository archive export for buyer data room
- Domain registry WHOIS/export attached to transfer package
- Cloudflare configuration export (Transform Rules, DNS, SSL)
- Optional notarized authenticity certificate (external legal process)
- Cryptographic signing of release manifests
- Automated provenance report generation from `routes.json` + `DECISION_LOG.md` + git log

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*  
*Governed by Sohadot | Internal — not in sitemap*
