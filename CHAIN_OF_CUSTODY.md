# CHAIN_OF_CUSTODY.md
**Version:** 1.0  
**Status:** Active — Custody and Change-Control Record  
**Asset:** EuraPlan.com  
**Owner:** Sohadot  
**Created:** Sprint 4G — June 2026  
**Last Updated:** June 2026

---

## 1. Title and status

**EuraPlan.com — Chain of Custody**  
**Status:** Active — documents custody history and change-control logic of the governed digital asset.

---

## 2. Purpose

Establish who holds the asset, how changes are controlled, and which governance layers protect corpus integrity across sprints. Supports acquisition due diligence and internal audit.

---

## 3. Custody principle

EuraPlan is not maintained as an ungoverned static site. Changes flow through:

1. Sprint-scoped work on feature branches
2. Pull request merge to `main`
3. `DECISION_LOG.md` entry for major decisions
4. `routes.json` / `sitemap.xml` / `robots.txt` updates only when route or indexation policy requires
5. Acceptance criteria and governing document compliance

Ad hoc public page creation, combinatorial URLs, and unlogged policy changes are prohibited.

---

## 4. Current custodian

| Role | Entity |
|---|---|
| Asset owner | Sohadot |
| Governing contact | agent@sohadot.com |
| Repository custody | Sohadot-governed EuraPlan repository |
| Domain custody | Sohadot (registrar records external to repository) |

---

## 5. Repository custody

- **Primary record:** Git version control on `main` branch
- **Change mechanism:** Branch → PR → merge commit
- **Evidence:** `git log`, merge commits, sprint-named commits
- **Prohibited:** Force-push to `main` without owner approval; secrets in repository; unlogged major policy reversals

---

## 6. Decision custody

- **Register:** `DECISION_LOG.md` (Sprint 4D onward)
- **Rule:** Major decisions recorded as DEC-NNN before or during implementation
- **Reversal:** Superseded entries remain visible; no silent deletion
- **Provenance closure:** DEC-043 (Sprint 4G)

---

## 7. Route custody

- **Registry:** `routes.json` — authoritative route IDs, paths, publication status
- **Indexation:** `sitemap.xml` — approved public URLs only
- **Crawl policy:** `robots.txt` — allow/disallow rules
- **Doctrine:** No combinatorial URLs (`ROUTE_GOVERNANCE.md`)

---

## 8. Source custody

- **Policy:** `SOURCE_POLICY.md`, `CLAIM_POLICY.md`
- **Practice:** Tier 1 official sources on reference pages; visible source tables on regulation/country/sector/funding pages
- **Rule:** No commercial SEO blogs as primary authority; no AI-generated summaries as sources

---

## 9. Interface custody

- **Visual system:** `VISUAL_SYSTEM_GOVERNANCE.md`, `INTERFACE_COMPONENT_POLICY.md`
- **Assets:** `/assets/brand/`, `/assets/css/main.css`
- **Doctrine:** European Entry Control Room interface — not generic consulting aesthetic

---

## 10. Security custody

- **Policy:** `SECURITY_POLICY.md`
- **Repository artifact:** `_headers` (Cloudflare Pages-compatible)
- **Verified runtime:** Cloudflare Response Header Transform Rule **EuraPlan Security Headers** (DEC-041)
- **Verification:** Live HTTP header capture required after deployment changes

---

## 11. Structured data custody

- **Policy:** `STRUCTURED_DATA_POLICY.md`
- **Audit:** `STRUCTURED_DATA_COVERAGE_AUDIT.md`
- **Implementation:** Inline JSON-LD on core and reference pages (DEC-042)
- **Future:** Hash-based CSP hardening deferred until schema stabilizes

---

## 12. Transfer custody requirements

On future strategic transfer, custody handover should include:

| Component | Handover requirement |
|---|---|
| Repository | Access transfer or fork to buyer-controlled org |
| Domain | Registrar transfer per legal agreement |
| Cloudflare | Account/zone access or configuration export |
| GitHub Pages / origin | Hosting account or migration plan |
| Decision log | Continuity — no deletion of historical DEC entries |
| Governance docs | Full markdown corpus transfer |
| Brand assets | `/assets/brand/` with usage terms |
| Third-party services | Explicitly listed — not assumed transferred |

---

## 13. Custody event log

Major lifecycle milestones (sprint names from repository history; dates not invented beyond document conventions):

| Milestone | Sprint | Custody note |
|---|---|---|
| Governance foundation | Sprint 0A / 0B / 1 Batch 4 | `GOVERNANCE_CHARTER.md`, `ACCEPTANCE_CRITERIA.md`, operating governance layer established |
| Public static foundation | Sprint 1A | Core public pages published |
| Brand integration | Sprint 1B | Brand assets integrated (`ddf6117`) |
| Conceptual interface foundation | Sprint 1C | European Entry Control Room interface (`088fdbd`) |
| Mobile stabilization | Sprint 1D / 1D-RC2 | Mobile layout hardening |
| Regulation layer | Sprints 2A–2D | Four regulation references (EP-REG-001–004) |
| Regulatory stack integration | Sprint 2E | `REGULATORY_STACK_INTEGRATION_REVIEW.md` |
| Country layer | Sprints 3A–3D | Germany, Netherlands, France + integration review |
| Sector layer | Sprint 4A | AI/SaaS sector reference (EP-SECTOR-001) |
| Decision log creation | Sprint 4D | `DECISION_LOG.md` (`5d8c87e`) |
| Security headers implementation | Sprint 4E | `_headers` (`453e966`) |
| Security runtime verification | Sprint 4E-RC1 | DEC-041; Transform Rule verified (`a473bd4`) |
| Structured data completion | Sprint 4F | DEC-042; core JSON-LD (`a00d9cf`, merge `d5b95d5`) |
| Funding layer (Horizon Europe) | Sprint 5A | EP-FUND-001 (`553c7e1`, DEC-039) |
| Provenance layer creation | Sprint 4G | DEC-043; this document set |
| Funding layer integration review | Sprint 5B | `FUNDING_LAYER_INTEGRATION_REVIEW.md`; DEC-044; registry/link parity fixes |

---

## 14. Future custody hardening

- Signed release tags per sprint closure
- Immutable archive snapshots for buyer data room
- Dual-control merge policy for `main`
- Automated custody report from git + `routes.json` + `DECISION_LOG.md`
- External audit log for domain and Cloudflare changes
- Documented backup and disaster-recovery procedure

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*  
*Governed by Sohadot | Internal — not in sitemap*
