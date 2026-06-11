# ASSET_TRANSFER_MANIFEST.md
**Version:** 1.0  
**Status:** Active — Transfer-Readiness Checklist  
**Asset:** EuraPlan.com  
**Owner:** Sohadot  
**Created:** Sprint 4G — June 2026  
**Last Updated:** June 2026

---

## 1. Title and status

**EuraPlan.com — Asset Transfer Manifest**  
**Status:** Active — defines what the asset consists of and what must be reviewed or transferred in future strategic acquisition due diligence.

This manifest prepares for due diligence. It does **not** constitute a sale, listing, valuation, or binding transfer offer.

---

## 2. Purpose

Enable a strategic buyer to understand the component parts of EuraPlan.com and conduct structured technical, governance, and content review — without implying guaranteed acquisition terms or asset price.

---

## 3. Asset covered

**EuraPlan.com** — governed digital category intelligence asset for **European Regulatory Entry & Expansion Planning Intelligence**, owned and developed under Sohadot.

---

## 4. Transfer components

| Component | Included in asset scope | Notes |
|---|---|---|
| Domain name `euraplan.com` | Yes | Registrar transfer separate |
| Repository codebase | Yes | Static site + governance corpus |
| Governance documents | Yes | Full `*.md` governing layer |
| Decision register | Yes | `DECISION_LOG.md` |
| Route registry | Yes | `routes.json` |
| Public reference corpus | Yes | HTML pages in repository |
| Brand assets | Yes | `/assets/brand/` |
| Internal audit documents | Yes | Integration reviews, structured data audit |
| Security configuration notes | Yes | `_headers`, DEC-041 Transform Rule documentation |
| Cloudflare edge configuration | Documented | Account transfer or export — not automatic |
| Third-party accounts | Conditional | GitHub, Cloudflare, registrar — per agreement |

---

## 5. Repository components

- Static HTML pages (core, regulation, country, sector, funding)
- CSS (`/assets/css/main.css`)
- Brand assets (SVG, PNG, OG image)
- `_headers` (Cloudflare Pages security headers)
- `sitemap.xml`, `robots.txt`
- `routes.json`
- All governance markdown documents
- Internal audit documents (not in sitemap)
- Provenance layer (Sprint 4G): `PROVENANCE.md`, `AUTHENTICITY_CERTIFICATE.md`, `CHAIN_OF_CUSTODY.md`, `ASSET_TRANSFER_MANIFEST.md`, `RIGHTS_AND_USAGE_NOTICE.md`

---

## 6. Public site components

**17 sitemap-published URLs** (as of Sprint 4G):

- 8 core pages: `/`, `/enter/`, `/clock/`, `/standard/eers/`, `/protocol/`, `/sources/`, `/governance/`, `/acquire/`
- 4 regulation references
- 3 country references
- 1 sector reference (`/sector/ai-saas/`)
- 1 funding reference (`/funding/horizon-europe/`)

**Not publicly indexed:** `/matrix/` (disallowed), `/diagnostic` (disallowed), draft/internal routes if any.

Public acquisition context page: `/acquire/` (buyer-facing summary — not a marketplace listing).

---

## 7. Governance components

Core: `GOVERNANCE_CHARTER.md`, `DECISION_LOG.md`, `SOURCE_POLICY.md`, `CLAIM_POLICY.md`, `ROUTE_GOVERNANCE.md`, `BUYER_LOGIC.md`, `ACCEPTANCE_CRITERIA.md`, `EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md`

Operating: `TECHNICAL_STANDARD.md`, `SECURITY_POLICY.md`, `SEO_GOVERNANCE.md`, `STRUCTURED_DATA_POLICY.md`, `REFERENCE_CORPUS_GOVERNANCE.md`, and companion documents listed in `PROVENANCE.md` Section 8.

---

## 8. Brand components

- Logo mark (gold SVG)
- Favicon (SVG + PNG)
- OG default image
- Visual tokens in `VISUAL_SYSTEM_GOVERNANCE.md`
- Wordmark usage: "EuraPlan" + "European Entry Control Room"

Brand transfer subject to `RIGHTS_AND_USAGE_NOTICE.md` and separate legal agreement.

---

## 9. Route corpus components

`routes.json` entries with ontology roles:

- Core routes (EP-R-001–008 area)
- Regulation (EP-REG-001–004)
- Country (EP-COUNTRY-001–003)
- Sector (EP-SECTOR-001)
- Funding (EP-FUND-001)
- Unpublished: matrix, diagnostic

---

## 10. Source and claim governance components

- `SOURCE_POLICY.md` — tier system
- `CLAIM_POLICY.md` — claim risk classification
- Per-page source tables on reference pages
- No fabricated statistics or unsupported market claims in corpus policy

---

## 11. Security and deployment components

- `_headers` — repository security header configuration
- `SECURITY_POLICY.md` — policy and production values
- DEC-040, DEC-041 — implementation and runtime verification records
- Cloudflare Response Header Transform Rule: **EuraPlan Security Headers**
- Origin note: GitHub Pages/Fastly behind Cloudflare (per DEC-041)

Buyer should request: Cloudflare dashboard export, DNS records, SSL mode, Transform Rules.

---

## 12. Structured data and agent-readability components

- `STRUCTURED_DATA_POLICY.md`
- `STRUCTURED_DATA_COVERAGE_AUDIT.md`
- `AGENT_READABILITY_POLICY.md`
- Inline JSON-LD on core + reference pages (DEC-042)

---

## 13. Exclusions

The following are **not** automatically included or guaranteed:

- Traffic, revenue, ranking, or search performance
- Acquisition price or valuation
- EU or government endorsement
- Legal, tax, compliance, or funding advice status
- Formal notarization, trademark registration, or government certification (unless separately documented)
- Third-party service accounts unless explicitly transferred
- User data (site does not collect user data in Phase 1)
- Unpublished matrix, brief, or diagnostic functionality
- Right to republish EU official source texts — third-party sources remain institution-owned

---

## 14. Required buyer due diligence

A strategic buyer should independently verify:

1. Domain registrar WHOIS and transfer eligibility
2. Repository `git log` and current `HEAD` commit
3. `DECISION_LOG.md` completeness for major decisions
4. `routes.json` ↔ `sitemap.xml` ↔ `robots.txt` consistency
5. Production security headers (`curl -I https://euraplan.com/`)
6. JSON-LD presence on public pages
7. Source tier compliance on reference pages
8. Cloudflare and hosting account ownership
9. No secrets in repository history
10. Rights posture (`RIGHTS_AND_USAGE_NOTICE.md`)

---

## 15. Transfer caveats

- **Separate legal agreement required** — this manifest is not a contract
- **No implied warranty** — buyer conducts own technical and legal review
- **Category claim** — transferable as documented positioning; not an official EU designation
- **Monetization** — governed by `MONETIZATION_BOUNDARY.md`; future revenue not guaranteed
- **Continued governance** — asset value depends on maintaining decision log and source discipline post-transfer

---

## 16. Future acquisition packaging checklist

- [ ] Freeze repository at signed release tag
- [ ] Export `DECISION_LOG.md` + full governance corpus
- [ ] Attach `PROVENANCE.md`, `AUTHENTICITY_CERTIFICATE.md`, `CHAIN_OF_CUSTODY.md`
- [ ] Domain registrar export
- [ ] Cloudflare configuration export
- [ ] Production header verification capture
- [ ] Structured data audit snapshot
- [ ] Brand asset inventory
- [ ] Third-party account list with transfer plan
- [ ] Legal IP and rights review
- [ ] Buyer data room index

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*  
*Governed by Sohadot | Internal — not in sitemap*
