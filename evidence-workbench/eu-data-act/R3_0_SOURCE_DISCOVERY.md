# R3.0 — EU Data Act Source Universe (Discovery)
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.0 Source & Claim Discovery
**Status:** DISCOVERY / SOURCE-PINNING CANDIDATE ONLY — **no `EP-SRC-*` minted, no live mutation**
**Working branch:** `claude/r3-0-data-act-discovery-dqiida` (independent R3.0 branch off `main` after merge #50 / DEC-057)
**Date:** 2026-08-24
**Governed by:** SOURCE_POLICY.md · EVIDENCE_GRAPH_MODEL.md · DISCLOSURE_BOUNDARY.md · REFERENCE_GRADE_ROUTE_STANDARD.md v2 · DEC-057
**Next free source slot when/if minting begins (R3.2, not now):** `EP-SRC-000006` — reserved for a **specific pinned instrument** only, never a generic portfolio page.

---

## 0. What this file is (and is not)

This is the **bounded legal universe** for the Data Act reference route. Its single job is to answer R3.0's first question — *what legal material may a Data Act claim rest on?* — and to fence off everything else.

- It **pins candidate sources**; it does **not** mint `EP-SRC-*`. Identity is fixed in R3.2 after falsification (R3.1), not here.
- Each instrument is placed in exactly one of five tiers. A source that is "interesting" but cannot carry a High-risk legal proposition is placed **below** the admissibility line and labelled as such.
- Per DEC-057 §7 and SOURCE_POLICY.md §2–3: **no generic Commission / portfolio / overview node** may ever become an `EP-SRC-*`. Commission material is admitted only by **specific title + official locator**, and only as Tier-2 explanatory context — never in place of the Regulation text for a direct legal proposition.

---

## 1. Primary binding instrument (Tier 1 — authentic act)

The one instrument on which every direct Data Act legal proposition must rest.

| Field | Value |
|---|---|
| **Candidate key** | `DATA-SRC-CAND-01` |
| **Proposed role** | `authentic_oj_act` (primary evidentiary basis) |
| **Official title** | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data and amending Regulation (EU) 2017/2394 and Directive (EU) 2020/1828 (Data Act) |
| **Short name** | Data Act |
| **CELEX** | `32023R2854` |
| **ELI (canonical locator)** | `http://data.europa.eu/eli/reg/2023/2854/oj` |
| **OJ reference** | OJ L, 2023/2854, 22.12.2023 (new-format OJ; act number = publication number) |
| **Date of act (adoption)** | 13 December 2023 |
| **Retrieval** | EUR-Lex `CELEX:32023R2854`, retrieved 2026-08-24 for discovery (structure + Article 50 corroborated against per-article official-text mirrors; **verbatim locator + text re-pull is an R3.1/R3.3 step**) |
| **Source tier** | 1 |
| **Proposed EP-SRC** | none yet — candidate for `EP-SRC-000006` at R3.2 **iff** a minted claim needs it |
| **Discovery status** | **PIN — primary binding instrument** |

### 1a. Application state (the dates that actually change planning — Article 50)

The Data Act does **not** apply as a single flat switch. These are the material dates. (Row A of the candidate inventory falsifies each against the authentic text in R3.1.)

| Event | Date | State as of 2026-08-24 | Locator |
|---|---|---|---|
| Entry into force | **11 January 2024** (20th day after OJ publication 22.12.2023) | past — in force | Art. 50 |
| **General application** | **12 September 2025** | **past — the Data Act is applicable now** | Art. 50 |
| Art. 3(1) product-design obligation | applies to connected products + related services **placed on the market after 12 September 2026** | **future — ~3 weeks out; roadmap-critical** | Art. 50 |
| Chapter III (data-holder availability duties) | applies to availability obligations under Union/national law **entering into force after 12 September 2025** | conditional / forward-looking | Art. 50 |
| Chapter IV (unfair terms, Art. 13) — new contracts | contracts concluded **after 12 September 2025** | in effect | Art. 50 |
| Chapter IV — legacy contracts | from **12 September 2027** for contracts concluded on/before 12.9.2025 that are (a) of indefinite duration **or** (b) due to expire ≥ 10 years from 11 January 2024 | future — transitional carve-out | Art. 50 |
| Switching charges fully prohibited (Art. 29) | from **12 January 2027** (interim reduced-charge regime before that — **exact interim boundary to falsify in R3.1**) | future — cloud-exit budgeting input | Art. 29 |
| Commission evaluation / review | by **12 September 2028** | future — not an entrant obligation (defer) | Art. 49 |

> **Consolidated-version rule (SOURCE_POLICY.md / R2 precedent):** a EUR-Lex *consolidated* text (`02023R2854-YYYYMMDD`) is a **reading aid only** and is kept strictly separate from the authentic OJ act above. It is **not** a substitute evidentiary basis for any High-risk proposition. Tracked as `DATA-SRC-CAND-03` in §2. As of this discovery pass no consolidated version need be pinned; the authentic act + corrigendum are the basis.

---

## 2. Amending / implementing / corrigendum instruments (Tier 1 — affect the text)

Instruments that **modify or complete** the binding text. These are the only "affects the text" candidates found in discovery.

| Candidate key | Role | Instrument | Locator | Discovery status |
|---|---|---|---|---|
| `DATA-SRC-CAND-02` | **corrigendum to the authentic act** | Corrigendum to Regulation (EU) 2023/2854 | OJ L, 2024/90790, 9.12.2024 · ELI `http://data.europa.eu/eli/reg/2023/2854/corrigendum/2024-12-09/oj` | **PIN as candidate** — must be read *together with* CAND-01 before any verbatim locator is trusted in R3.1/R3.3. Affects the authentic text; not optional. |
| `DATA-SRC-CAND-03` | current reading aid only | EUR-Lex consolidated text of 2023/2854 (version pinned at verification time) | CELEX pattern `02023R2854-YYYYMMDD` | **candidate — do not mint now.** Reading aid; never replaces authentic act (§1a note). |
| `DATA-SRC-CAND-04` | **outbound** amendment by the Data Act | Regulation (EU) 2017/2394 (CPC Regulation) — *amended by* Art. 47 Data Act | CELEX `32017R2394` | **defer / context only.** The Data Act amends *it*; it does not govern Data Act obligations. Relevant only to the enforcement-cooperation seam. |
| `DATA-SRC-CAND-05` | **outbound** amendment by the Data Act | Directive (EU) 2020/1828 (Representative actions) — *amended by* Art. 48 Data Act | CELEX `32020L1828` | **defer / context only.** Adds Data Act to the collective-redress annex; a remedy-architecture note, not a primary obligation source. |
| `DATA-SRC-CAND-06` | implementing / delegated acts empowered by the Data Act | e.g. model contractual terms & standard contractual clauses (Art. 41); harmonised standards / common specs for interoperability & switching (Arts. 33, 35, 36); delegation (Art. 45) | **no specific instrument pinned** | **candidate — pin the specific act only if/when a minted claim needs it (R3.2+).** No generic "future implementing acts" node. Several were still forthcoming/nascent at discovery; a claim that depends on one is **deferred** until the instrument exists and can be pinned by identifier. |

---

## 3. Specific Commission materials (Tier 2 — explanatory only, admitted by exact locator)

Tier-2 context under SOURCE_POLICY.md §2. **May not** support any High-risk legal proposition in place of the Regulation. Admitted only if named specifically; **intentionally unminted** (mirrors the GDPR precedent where the Commission overview and EDPB portfolio were deliberately left without `EP-SRC-*`).

| Candidate key | Material | Locator | Discovery status |
|---|---|---|---|
| `DATA-SRC-CAND-07` | European Commission — Data Act explanatory page ("Data Act" / data-economy policy) | Commission `digital-strategy` official page (pin exact URL + retrieval date at use) | **INTENTIONALLY UNMINTED.** Orientation only; never the basis of a legal claim. No generic-overview `EP-SRC-*`. |
| `DATA-SRC-CAND-08` | European Commission — Data Act FAQ / Q&A | Commission official FAQ (pin exact URL + version/date at use) | **INTENTIONALLY UNMINTED.** Interpretive aid; if a claim needs it at R3.3, pin the specific FAQ item by date. |
| `DATA-SRC-CAND-09` | Commission model contractual terms (MCTs) & standard contractual clauses (SCCs) for data sharing / cloud switching (Art. 41 deliverable) | pin specific published instrument + date when it exists | **candidate — defer.** Becomes Tier-1/implementing (→ CAND-06) if adopted as an act; Tier-2 if a recommendation. Do not pin from a draft. |

---

## 4. Potentially relevant but NOT yet admissible (below the line)

Real, authoritative instruments in the **data acquis** that touch the Data Act's subject matter but are **not** the Data Act's own text and must not be conflated with it. Held out of the Data Act claim basis; each is its **own** future route/source decision, not an R3 input.

| Candidate key | Instrument | Why relevant | Why NOT admissible into R3 claim basis |
|---|---|---|---|
| `DATA-SRC-CAND-10` | Regulation (EU) 2016/679 (GDPR) — CELEX `32016R0679` (already `EP-SRC-000004/000005`) | Data Act Art. 44 / recitals: Data Act is **without prejudice** to GDPR; personal-data access rests on GDPR, not the Data Act | Governs the *personal-data* interface only. The GDPR↔Data Act boundary is an **analytical seam** (see propositions file), **not** a merge of authorities. No GDPR claim is ported. |
| `DATA-SRC-CAND-11` | Regulation (EU) 2022/868 (Data Governance Act) — CELEX `32022R0868` | Same data-strategy family; data intermediation / altruism / public-sector data reuse | Different instrument, different obligations. Not a source for Data Act propositions. Possible **future** EP-REG route. |
| `DATA-SRC-CAND-12` | Regulation (EU) 2018/1807 (Free flow of non-personal data) — CELEX `32018R1807` | Non-personal data localisation baseline; interacts with Arts. 32 & Ch. VI | Superseded/complemented in parts by the Data Act on switching; itself not a Data Act obligation source. Context only. |
| `DATA-SRC-CAND-13` | Regulation (EU) 2023/1543 / (EU) 2022/2065 (DSA) / (EU) 2022/1925 (DMA) | DMA "gatekeeper" definition is *used* by Data Act Art. 5(3) third-party carve-out | Only the **cross-reference** matters; pin DMA (`32022R1925`) narrowly *iff* a minted claim quotes the gatekeeper exclusion. Not a general Data Act source. |
| `DATA-SRC-CAND-14` | Directive 96/9/EC (Database Directive, sui generis right) — CELEX `31996L0009` | Data Act Art. 43 carves the sui generis right out of connected-product data | Only the **Art. 43 interaction** is in scope; the Directive itself is not a Data Act obligation source. |

---

## 5. Rejected / unnecessary (never a source node)

Explicitly excluded so the graph cannot silently absorb them (SOURCE_POLICY.md §3; DEC-057 §7).

| Item | Reason for rejection |
|---|---|
| Law-firm / Big-Four Data Act alerts & client briefings | Tier-3 at best; **never** valid for a regulatory/compliance claim. Discovery orientation only, uncited. |
| Vendor / cloud-provider "Data Act readiness" marketing | Marketing material; not a source. |
| Undated press releases, blog posts, news explainers, Wikipedia | Rejected under SOURCE_POLICY.md §3. Wikipedia = orientation, never citation. |
| Third-party per-article mirror sites (e.g. structured legal-text reproductions) used during discovery | Convenience mirrors for **discovery navigation only**. Every locator they suggested is re-pulled against the **authentic EUR-Lex text + corrigendum** before any claim mint. Not citable. |
| Generic "European Commission — data" / portfolio / topic hub pages | Prohibited generic node (DEC-057 §7). Only specific, dated, titled Commission items may be Tier-2. |
| Recitals treated as standalone obligation sources | Recitals inform interpretation of the operative Articles; they do **not** by themselves found a legal proposition (see defer/reject register in propositions file). |

---

## 6. Source universe — closure statement

- **Bounded:** the admissible Data Act claim basis is **CAND-01 (authentic act)** read with **CAND-02 (corrigendum)**; everything in §3–§5 sits below the admissibility line with an explicit reason.
- **No identity fixed:** zero `EP-SRC-*` minted in R3.0. `EP-SRC-000006` remains the next free slot, reserved for a specific pinned instrument at R3.2 only if a falsified claim requires it.
- **Consolidated ≠ authentic:** kept separate (CAND-03).
- **Commission material fenced:** Tier-2, specific-locator-only, intentionally unminted (CAND-07…09).
- **Adjacent acquis fenced out:** GDPR / DGA / FFD / DMA / Database Directive are related-not-admissible; only narrow cross-references (Art. 5(3) gatekeeper; Art. 43 sui generis; Art. 44 GDPR boundary) may pin those instruments narrowly, later.
- **Ready for R3.1:** the falsification phase has a fixed, minimal evidentiary target — the authentic text + corrigendum — against which every candidate proposition is tested.

*EuraPlan.com — Sprint R3.0 workbench. Discovery artifact. Not a published website page.*
