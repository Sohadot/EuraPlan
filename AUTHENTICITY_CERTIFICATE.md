# AUTHENTICITY_CERTIFICATE.md
**Version:** 1.0  
**Status:** Active — Repository Authenticity Record (Non-Legal)  
**Asset:** EuraPlan.com  
**Owner:** Sohadot  
**Created:** Sprint 4G — June 2026  
**Last Updated:** June 2026

---

## 1. Title and status

**EuraPlan.com — Authenticity Certificate (Repository Record)**  
**Status:** Active — internal and buyer-facing authenticity statement tied to the repository record.

---

## 2. Certificate purpose

This document certifies, at the repository governance level, that EuraPlan.com is a documented, governed digital category intelligence asset — not an anonymous static site or ungoverned content collection.

**This is not a government certificate.**  
**This is not a trademark registration.**  
**This is not a notarized document.**  
**This does not by itself transfer ownership.**  
**This does not replace a legal acquisition agreement.**  
**This is a provenance and authenticity record for due diligence.**

---

## 3. Asset covered

| Field | Value |
|---|---|
| Asset name | EuraPlan.com |
| Category | European Regulatory Entry & Expansion Planning Intelligence |
| Asset type | Governed digital category intelligence asset |
| Primary domain | `euraplan.com` |
| Repository | EuraPlan (Sohadot-governed) |
| Custodian | Sohadot |

---

## 4. Covered materials

This certificate covers the authenticity posture of:

- Public static site (`*.html`, `/assets/`)
- Route registry (`routes.json`)
- Indexation files (`sitemap.xml`, `robots.txt`)
- Security header configuration (`_headers`) and documented edge enforcement
- Governance and operating policy documents (`*.md` governing layer)
- Decision register (`DECISION_LOG.md`)
- Internal audit documents (integration reviews, structured data audit)
- Brand assets (`/assets/brand/`)
- Acquisition-readiness documents (Sprint 4G provenance layer)

---

## 5. Authorship and governance statement

EuraPlan is authored, governed, and maintained under Sohadot ownership. Public content is produced under documented governance — not as anonymous or unattributed web copy.

EuraPlan is **not** an official EU institution. EuraPlan does **not** claim endorsement by the European Commission, EU institutions, national governments, regulators, funding bodies, universities, or partners.

EuraPlan provides **planning intelligence** — not legal, tax, compliance, incorporation, funding, grant-writing, or investment advice.

---

## 6. Repository evidence

Version control history documents sequential sprint development. Representative merge and implementation commits (from repository history — not invented):

| Sprint / subject | Commit (short) | Note |
|---|---|---|
| Sprint 4F structured data | `a00d9cf` | Core page JSON-LD |
| Sprint 4F merge | `d5b95d5` | Merged to main |
| Sprint 4E-RC1 security verification | `a473bd4` | Runtime header governance |
| Sprint 4E `_headers` | `453e966` | Repository security headers |
| DECISION_LOG creation | `5d8c87e` | Sprint 4D |
| Sprint 4A AI/SaaS sector | `2385990` | EP-SECTOR-001 |
| Sprint 3A Germany | `ca1c5f9` | EP-COUNTRY-001 |
| Sprint 2A EU AI Act | `3fec275` | EP-REG-001 |
| Sprint 5A Horizon Europe | `553c7e1` | EP-FUND-001 |

Current repository HEAD at certificate creation should be verified by buyer: `git rev-parse HEAD`.

---

## 7. Decision log evidence

`DECISION_LOG.md` contains numbered Active decisions (DEC-001 through DEC-043 as of Sprint 4G). Major architecture, route, security, structured data, and provenance decisions are recorded with rationale, affected files, and reversal conditions.

Provenance-relevant entries: **DEC-040**, **DEC-041**, **DEC-042**, **DEC-043**.

---

## 8. Route and sitemap evidence

| Anchor | File | Purpose |
|---|---|---|
| Route registry | `routes.json` | 19 registered routes with IDs, ontology roles, publication status |
| Sitemap | `sitemap.xml` | 17 approved public URLs |
| Robots | `robots.txt` | Indexation allow/disallow policy |

Cross-consistency: published sitemap URLs correspond to `routes.json` entries with `sitemap: true` and `publication_status: published`.

---

## 9. Security and structured data verification evidence

| Closure | Evidence |
|---|---|
| Security policy → runtime | DEC-041; production `curl -I https://euraplan.com/` header capture; Cloudflare Transform Rule **EuraPlan Security Headers** |
| Structured data policy → implementation | DEC-042; `STRUCTURED_DATA_COVERAGE_AUDIT.md`; inline JSON-LD on 8 core pages + reference corpus |

---

## 10. Exclusions and non-claims

This certificate does **not** claim:

- Formal notarization or government certification
- Trademark registration (unless separately documented by owner)
- EU or institutional endorsement or partnership
- Legal, tax, compliance, or funding advice status
- Traffic, revenue, ranking, or search performance guarantees
- Acquisition price or valuation
- Automatic transfer of third-party services (Cloudflare, GitHub, domain registrar)
- That repository visibility grants reuse or republication rights (see `RIGHTS_AND_USAGE_NOTICE.md`)

---

## 11. Transfer relevance

In a future strategic acquisition, this certificate supports due diligence by pointing reviewers to:

- `PROVENANCE.md` — origin and development history
- `CHAIN_OF_CUSTODY.md` — custody and change-control logic
- `ASSET_TRANSFER_MANIFEST.md` — transfer component checklist
- `RIGHTS_AND_USAGE_NOTICE.md` — rights posture
- `DECISION_LOG.md` — decision audit trail
- `BUYER_LOGIC.md` — strategic acquisition framing (public `/acquire/` summarizes buyer-facing context)

Actual transfer requires separate legal documentation, domain transfer, repository access handover, and infrastructure account migration.

---

## 12. Certificate statement

As of Sprint 4G (June 2026), EuraPlan.com is represented in the Sohadot-governed repository as a governed category intelligence asset with documented provenance, decision history, route registry, source governance, verified production security headers, and completed structured data coverage for core pages.

This authenticity record is issued for **due diligence and acquisition-readiness purposes**. It is not a substitute for legal counsel, formal IP registration, or a binding transfer agreement.

---

## 13. Future hardening options

- Notarized authenticity statement (external legal process)
- Signed git release tags per sprint closure
- Timestamped archive with checksum manifest
- Domain registry export attached to certificate
- Cloudflare configuration export
- Buyer data room package with frozen commit hash
- Third-party technical due diligence report

---

## Verification Anchors

Anchor types for buyer verification (no invented data):

| Anchor type | Reference |
|---|---|
| Domain | `euraplan.com` |
| Repository | EuraPlan repository (Sohadot-governed) |
| Decision log | `DECISION_LOG.md` |
| Route registry | `routes.json` |
| Sitemap | `sitemap.xml` |
| Robots policy | `robots.txt` |
| Source governance | `SOURCE_POLICY.md` |
| Claim governance | `CLAIM_POLICY.md` |
| Security runtime verification | DEC-041 · `SECURITY_POLICY.md` Section 8 |
| Structured data closure | DEC-042 · `STRUCTURED_DATA_COVERAGE_AUDIT.md` |
| Provenance layer closure | DEC-043 · this document set |
| Representative commit (4F) | `a00d9cf` |
| Representative commit (4E-RC1) | `a473bd4` |
| Representative merge (4F → main) | `d5b95d5` |

Buyers should verify current `HEAD`, production headers, and domain registrar records independently.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*  
*Governed by Sohadot | Internal — not in sitemap*
