# REFERENCE_DEPTH_AUDIT_R1_2026-08-20.md
**Status:** Public working evidence — Sprint R1 baseline (Depth Equalization Program)
**Asset:** EuraPlan.com
**Audit date:** 2026-08-20
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2.0 (DEC-047)
**Corpus:** 17 sitemap-published routes
**Method:** Honest baseline against the six layers; scores are diagnostic, not a rewrite of live pages in this sprint

---

## 1. Rubric

Each dimension 0–12.5 (sum 100). Threshold for Wave 1 Core Authority: **≥ 90** before expansion.

| Code | Dimension |
|---|---|
| Ev | Evidence depth |
| IG | Unique information gain |
| CD | Conceptual depth (ontology-appropriate) |
| DU | Decision utility |
| CR | Citation readiness |
| MR | Machine readability |
| Fr | Freshness / maintenance contract |
| SEO | SEO semantics (entity + ontology edges + real lastmod) |

---

## 2. Baseline scores (17 routes)

| Route | Ev | IG | CD | DU | CR | MR | Fr | SEO | **Total** | Wave | Notes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| `/regulation/eu-ai-act/` | 12.5 | 12.0 | 12.0 | 11.5 | 12.5 | 12.5 | 12.0 | 12.0 | **97** | 1 | Gold Reference — Evidence Graph live; maintain |
| `/regulation/gdpr/` | 8.0 | 7.0 | 8.5 | 8.0 | 6.0 | 5.5 | 6.5 | 8.0 | **58** | 1 | Structured summary; needs Evidence Graph-grade claims |
| `/regulation/eu-data-act/` | 8.0 | 7.0 | 8.5 | 8.0 | 6.0 | 5.5 | 6.5 | 8.0 | **58** | 1 | Same class as GDPR |
| `/regulation/cyber-resilience-act/` | 8.5 | 7.5 | 8.5 | 8.0 | 6.5 | 5.5 | 7.0 | 8.0 | **60** | 1 | Dates corrected historically; still not claim-graph grade |
| `/standard/eers/` | 7.0 | 9.0 | 10.0 | 8.5 | 7.0 | 6.0 | 6.5 | 8.0 | **62** | 1 | Strong proprietary framing; Candidate spec depth incomplete |
| `/protocol/` | 6.5 | 8.5 | 9.5 | 9.0 | 6.5 | 5.5 | 6.5 | 8.0 | **60** | 1 | Methodology present; citeable step-objects weak |
| `/country/germany/` | 7.5 | 7.0 | 8.0 | 7.5 | 6.0 | 5.0 | 6.0 | 7.5 | **55** | 2 | Risk of peer-substitutable structure |
| `/country/netherlands/` | 7.5 | 7.0 | 8.0 | 7.5 | 6.0 | 5.0 | 6.0 | 7.5 | **55** | 2 | Same |
| `/country/france/` | 7.5 | 7.5 | 8.0 | 7.5 | 6.0 | 5.0 | 6.0 | 7.5 | **55** | 2 | Same — upgrade to Execution Intelligence Node |
| `/sector/ai-saas/` | 7.0 | 7.5 | 8.0 | 8.0 | 5.5 | 5.0 | 6.0 | 7.5 | **55** | 3 | Cross-reg links exist; not yet reasoning node |
| `/funding/horizon-europe/` | 7.5 | 7.0 | 7.5 | 7.5 | 6.0 | 5.0 | 6.5 | 7.5 | **55** | 3 | Needs eligibility logic / decision boundaries |
| `/` | 5.0 | 8.0 | 9.0 | 7.5 | 5.0 | 5.5 | 9.0 | 8.5 | **58** | 3 | Category thesis strong after clock hotfix; keep lean |
| `/enter/` | 5.0 | 6.5 | 7.5 | 7.0 | 4.5 | 4.5 | 6.0 | 7.0 | **48** | 3 | Still navigation-heavy vs decision gateway |
| `/clock/` | 9.0 | 8.0 | 8.5 | 8.5 | 7.0 | 6.5 | 10.0 | 9.0 | **67** | 3 | Canonical timeline surface; derivative of claims for AI Act |
| `/sources/` | 8.0 | 7.0 | 8.0 | 6.5 | 6.0 | 5.0 | 7.0 | 7.0 | **55** | 3 | Doctrine transparency; deepen tier examples |
| `/governance/` | 6.5 | 7.0 | 8.0 | 6.0 | 5.5 | 5.0 | 7.0 | 7.0 | **52** | 3 | Architecture disclosure; link to RGS v2 |
| `/acquire/` | 5.0 | 7.5 | 8.0 | 7.0 | 5.0 | 4.5 | 6.0 | 6.5 | **50** | 3 | Buyer thesis; not legal depth |

**Wave 1 at threshold (≥90):** EU AI Act only (1/6).  
**Program rule:** no new expansion routes until Wave 1 Core Authority pages reach ≥90.

---

## 3. Hard-fail scan (qualitative)

| Risk | Routes most exposed |
|---|---|
| Peer-substitutable country copy | Germany / Netherlands / France |
| Official-prose paraphrase without analytical layer | GDPR / Data Act / CRA (relative to AI Act) |
| Weak citeable units | Protocol, EERS, sector, funding |
| Navigation without decision object | Enter |

---

## 4. Upgrade backlog (order)

1. GDPR → Evidence Graph-grade material claims (mint only what truth requires)  
2. EU Data Act → same  
3. CRA → same  
4. EERS → formal Candidate→Stable path without false “published standard” claims  
5. Protocol → citeable methodology objects / step anchors  
6. France → Country Execution Intelligence Node (template for DE/NL)  
7. Germany → same pattern  
8. Netherlands → same pattern  
9. AI/SaaS → cross-regulation reasoning node  
10. Horizon Europe → eligibility / decision boundaries  
11. Enter → decision gateway  
12. Remaining system pages as capacity allows  

Do **not** freeze `EP-CTR-CLM-*` until a country evidence model is designed.

---

## 5. Out of scope for R1

- No claim proposition changes to EU AI Act v1  
- No expansion routes  
- No mass word-count inflation  

R1 **delivers:** Standard v2 adopted; baseline scores; backlog; claims.json `_meta` live-status housekeeping (separate file in same program commit).

---

*EuraPlan.com — Sprint R1 Reference Depth Audit. Not a published website page.*
