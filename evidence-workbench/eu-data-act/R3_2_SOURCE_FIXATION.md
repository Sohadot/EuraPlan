# R3.2 — EU Data Act Source Fixation (EP-SRC minting)
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.2 Source Fixation
**Status:** SOURCE IDENTITIES FIXED — **workbench only. No public registration, no `routes.json`/`llms.txt`/sitemap change.**
**Opened by:** DEC-060
**Governed by:** SOURCE_POLICY.md; EVIDENCE_GRAPH_MODEL.md; DISCLOSURE_BOUNDARY.md; DEC-057 §7 (no generic source nodes); DEC-059; DEC-060
**Date:** 2026-08-31

---

## 1. Purpose

R3.2 converts the R3.0 pinned **source candidates** for the EU Data Act into permanent **`EP-SRC-*` identities**, so every `EP-CLM-*` minted in `R3_2_IDENTITY_REGISTER.md` rests on an identified evidentiary basis. Only the **two instruments that carry the authentic text** are minted here (per DEC-057 §7: no generic Commission / portfolio nodes). External-instrument dependencies are recorded but **not** minted unless and until a claim's rendering quotes them (R3.3+).

## 2. Fixed source identities (minted this phase)

| EP-SRC ID | Candidate | Role | Instrument | Official locator | Tier | Result |
|---|---|---|---|---|---|---|
| **`EP-SRC-000006`** | `DATA-SRC-CAND-01` | `authentic_oj_act` — primary evidentiary basis for **every** Data Act claim | Regulation (EU) 2023/2854 (Data Act), of 13 December 2023 | CELEX `32023R2854`; ELI `http://data.europa.eu/eli/reg/2023/2854/oj`; OJ L, 2023/2854, 22.12.2023 | 1 | **FIXED** |
| **`EP-SRC-000007`** | `DATA-SRC-CAND-02` | `corrigendum` — read **with** EP-SRC-000006; affects **Article 48 only** (renumber "68"→"(69)" in Directive (EU) 2020/1828 Annex I) | Corrigendum to Regulation (EU) 2023/2854 | OJ L, 2024/90790, 9.12.2024; ELI `http://data.europa.eu/eli/reg/2023/2854/corrigendum/2024-12-09/oj` | 1 | **FIXED** |

**Source-pack provenance (in-repo, internal):** `evidence-workbench/eu-data-act/source-pack/EU_Data_Act_Regulation_2023_2854_official_text_EN.pdf` (→ EP-SRC-000006) and `.../EU_Data_Act_Corrigendum_2024_12_09_official_text_EN.pdf` (→ EP-SRC-000007). Every R3.1 locator was read verbatim from this pack.

**Next free `EP-SRC`:** `EP-SRC-000008`.

## 3. Dependency instruments — recorded, NOT minted here

Referenced by minted claims as **external dependencies**; each pins its own `EP-SRC` only if/when a claim's rendering quotes it (R3.3+), never as a generic node:

| Instrument | CELEX | Used by (EP-CLM lineage rows) | Existing/planned EP-SRC |
|---|---|---|---|
| Regulation (EU) 2016/679 (GDPR) | `32016R0679` | B6, B6b, C3/C6 personal-data (Q16), K1b, K2b (40(4)) | already `EP-SRC-000004/000005` |
| Regulation (EU) 2022/1925 (DMA) | `32022R1925` | C7 (5(3)), D2 (6(2)(d)) gatekeeper | pin narrowly at use |
| Directive 96/9/EC (Database Directive) | `31996L0009` | K4 (Art 43 sui generis carve-out) | pin narrowly at use |
| Regulation (EU) 2018/1725 | `32018R1725` | K2c (40(5) EDPS fines), K1b | pin narrowly at use |
| Regulation (EU) 1025/2012 (Standardisation) | `32012R1025` | I1/I2 (Arts 33/35 — source-constrained, unminted), G5c/J1 standards | pin at use, standards-pending |
| Directive (EU) 2019/770 | `32019L0770` | G2a (Art 25(1) "without prejudice") | pin narrowly at use |

## 4. Guards
- **No generic source node** minted (DEC-057 §7). Only the two authentic-text instruments carry `EP-SRC` identity now.
- **Consolidated ≠ authentic:** any EUR-Lex consolidated version (`02023R2854-YYYYMMDD`) remains a reading aid, never an evidentiary basis; not minted.
- Commission FAQ / draft MCT-SCC (`DATA-SRC-CAND-07/08/09`) stay **intentionally unminted** — explanatory/non-binding, insufficient to found an operative proposition.

---

*EuraPlan.com — Sprint R3.2 workbench source fixation. Internal. Not a published website page.*
