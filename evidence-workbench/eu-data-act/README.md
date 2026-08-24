# Sprint R3 — EU Data Act Evidence Graph-grade Upgrade
**Status:** **R3.0 CLOSED / PASS — R3.1 AUTHORIZED.** Source & claim discovery complete; 9/9 close conditions PASS. No claims minted. No live mutation. Publish Gate NOT OPEN.  
**Discovery deliverables (closed 2026-08-24):** `R3_0_SOURCE_DISCOVERY.md`, `R3_0_CANDIDATE_PROPOSITIONS.md`, `R3_0_DISCOVERY_CLOSEOUT.md` — 54 workbench rows / 46 live corpus; Q1–Q16 qualification pairs; S1–S8 analytical seeds. **R3.1 is authorized but not started** — it becomes executable on the program corpus only once R3.0 lands on `main`.  
**Opened:** 2026-08-23 (DEC-057)  
**R3.0 discovery branch:** `claude/r3-0-data-act-discovery-dqiida` (off `main` after merge #50)  
**Canonical target:** `/regulation/eu-data-act/` + (future) `/regulation/eu-data-act/claims.json` (EP-REG-003)  
**Instrument:** Regulation (EU) 2023/2854 — EUR-Lex CELEX `32023R2854`  
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; SOURCE_POLICY.md; CLAIM_POLICY.md; FRESHNESS_ENGINE.md; ROUTE_GOVERNANCE.md; DISCLOSURE_BOUNDARY.md; DEC-047; DEC-048 (R2 precedent); DEC-057

---

## Method — governance reuse, content rediscovery

R3 is **not** a copy of the GDPR sprint. It reuses the *operating system* proven in R2 and rediscovers the *content* from the Data Act's own text.

**Reused as-is (operational precedent):**
- The RGS v2 six-layer standard (Identity & Scope · Primary Evidence · Unique Analytical Layer · Decision Utility · Machine & Citation · Maintenance Contract).
- The frozen Publish-Gate architecture: **Gate 0** hosting/index-control → **Gate 1** pre-publication canonical build → **Gate 2** release HTML → **Gate 3** machine + registration → **Gate 4** pre-merge audit → **Gate 5** publication → **Gate 6** live verification + re-score.
- The phase sequence: source discovery → claim map / falsification → human literal verification → canonical `claims.json` → page transformation → Decision Utility → citation/machine prep → Publish Gate → RGS re-score.
- The evidence-graph, claim-identity, source, claim, and freshness governance.

**Rediscovered from scratch (Data Act material truth):**
- The claim set — what the Data Act actually obligates, permits, and triggers — mapped from Regulation (EU) 2023/2854 directly, not ported from GDPR.
- The analytical layer and Decision Objects — the planning consequences that are specific to data access, connected products, cloud switching, and B2B/B2G data sharing.
- The source set — Tier-1 primary instruments and specific Commission materials pinned to canonical official locators — CELEX/ELI where applicable; stable Commission URL/document identifier otherwise.

> GDPR is the precedent for *how*, never the template for *what*. No GDPR claim, Decision Object, source node, or claim count is carried over.

---

## Hard rules for this sprint (DEC-057)

1. **No live HTML rewrite** of `/regulation/eu-data-act/` until R3's terminal Publish Gate authorizes the publication sequence.
2. **No** public `/regulation/eu-data-act/claims.json` until the Publish Gate authorizes it. Staging stays in this workbench.
3. **Minting fixes identity, not truth-status.** Next free ID is **`EP-CLM-000046`**; the global opaque sequence continues. Never recycle an ID; never mint before literal falsification.
4. Global opaque ID sequence only — never `DATA-CLM-*` / `DA-CLM-*`.
5. Claim count follows **Data Act material truth**, not a template or a target number.
6. Defaults with exceptions must carry `qualified_by`; a published default may never render without its qualifier.
7. No generic Commission/portfolio source nodes; pin specific instruments to real CELEX identifiers only when needed.
8. Decision Utility is a **derived** planning layer; seeds are not verified facts and mint no claims on their own.
9. **No** `routes.json` / `llms.txt` / sitemap alternate registration for Data Act claims until the Publish Gate.
10. **No parallel CRA / EERS / Protocol / country / sector / expansion work** while R3 is open (Wave 1 stays gated until all routes ≥ 90 — DEC-047).

---

## Phase checklist

| Phase | Name | State |
|---|---|---|
| R3.0 | Source & Claim Discovery | **CLOSED / PASS** — 9/9 close conditions; 54 rows / 46 live |
| R3.1 | Claim Map & Falsification | **AUTHORIZED / NOT STARTED** (executable after R3.0 lands on `main`) |
| R3.2 | Identity Fixation + Source Pinning + Draft Serialization | PENDING |
| R3.3 | Human Literal Verification | PENDING |
| R3.4 | Canonical Graph + Route Integration Preparation | PENDING |
| R3.5 | Branch-only Page Transformation | PENDING |
| R3.6 | Decision Utility Layer | PENDING |
| R3.7 | Citation + Machine Registration Preparation | PENDING |
| R3.8 | Data Act Publish Gate → RGS re-score ≥ 90 | PENDING |

---

## R3.0 workbench files

| File | Role |
|---|---|
| `R3_0_SOURCE_DISCOVERY.md` | Source Universe — 5 classes/buckets; authentic act + corrigendum pinned as candidates; Art. 50 application-date table; **no `EP-SRC-*` minted** |
| `R3_0_CANDIDATE_PROPOSITIONS.md` | Candidate Proposition Inventory (54 rows / 46 live, **no IDs**) + qualification pairs (Q1–Q16) + defer/reject register + analytical seeds (S1–S8) + coverage matrix (Ch. I–XI) |
| `R3_0_DISCOVERY_CLOSEOUT.md` | Closeout register — 9/9 close conditions PASS; **CLOSED / PASS — R3.1 AUTHORIZED** (review PASS 2026-08-24) |
| `README.md` | This status note |

---

## Baseline

R1 Depth Equalization audit (`governance/audits/REFERENCE_DEPTH_AUDIT_R1_2026-08-20.md`): `/regulation/eu-data-act/` = **58 / 100** (official-prose paraphrase without an analytical layer; same class as pre-R2 GDPR). Target: **≥ 90** for real six-layer reasons after the Publish Gate.

---

## Wave 1 status (DEC-047 / DEC-057)

| Route | RGS v2 | ≥ 90 |
|---|---|---|
| EU AI Act (Gold Reference) | 97 | ✅ |
| GDPR (EP-REG-002) | 97.5 | ✅ |
| **EU Data Act (EP-REG-003)** | **58** | **← R3 target** |
| CRA (EP-REG-004) | 60 | — |
| EERS (`/standard/eers/`) | 62 | — |
| Protocol (`/protocol/`) | 60 | — |

Expansion stays gated until **all** Wave 1 routes reach ≥ 90.

---

## Success condition (end of R3)

- AI Act remains ≥ 90; GDPR remains ≥ 90 (frozen — DEC-057).
- Data Act RGS score ≥ 90 for real six-layer reasons (after the Publish Gate).
- CRA / EERS / Protocol remain later, in RGS v2 order.
- **No expansion opened** before all Wave 1 routes ≥ 90.

---

*EuraPlan.com — Sprint R3 workbench. Not a published website page.*
