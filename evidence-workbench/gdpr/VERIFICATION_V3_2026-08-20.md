# GDPR R2.3 — Verification Batch V3

**Date:** 2026-08-20  
**Scope:** `EP-CLM-000027` … `EP-CLM-000033` (7 claims)  
**Logical block:** Principles → Accountability → Controller Governance → Privacy by Design/Default → Processor Governance → Records (+ Art. 30(5) qualification)  
**Primary source:** EUR-Lex authentic Official Journal act — CELEX `32016R0679` / `EP-SRC-000004`  
**Reading aid:** CELEX `02016R0679-20160504` / `EP-SRC-000005` (non-replacement)  
**Lifecycle:** batch-open review → `pending_verification`; individual PASS → `verified`  
**Not done:** HTML rewrite · public `/regulation/gdpr/claims.json` · Publish Gate · V4+

---

## Batch result

| ID | Topic | Verdict | Final state |
|---|---|---|---|
| `EP-CLM-000027` | Art. 5(1) principles | **PASS** | `verified` |
| `EP-CLM-000028` | Art. 5(2) accountability | **PASS** | `verified` |
| `EP-CLM-000029` | Art. 24(1)–(2) controller responsibility | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000030` | Art. 25 design/default | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000031` | Art. 28(1)–(4) processor/subprocessor | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000032` | Art. 30(1)–(4) RoPA | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000033` | Art. 30(5) `<250` qualification | **AMEND BEFORE VERIFICATION → PASS** | `verified` |

**Score:** 7/7 PASS after 5 pre-verification precision amendments. **VOID:** 0.

---

## Qualification integrity — `000032` ↔ `000033`

`EP-CLM-000032` carries `qualified_by: ["EP-CLM-000033"]`.

- **Graph-level test:** PASS — qualification edge explicit and directional.
- **Render-level test:** NOT YET TESTABLE — no public GDPR claim renderer/HTML in R2.3.
- **Blocking publication condition:** under `EVIDENCE_GRAPH_MODEL.md`, any future published rendering of the Art. 30 default record duty must visibly co-render Art. 30(5). Standalone RoPA rendering is prohibited.
- **Substance check:** Art. 30(5) is **not** an automatic SME exemption. Fewer than 250 persons is displaced if processing is likely to result in a risk to rights and freedoms of data subjects, is not occasional, or includes Art. 9(1) special categories or Art. 10 criminal convictions and offences data.

---

## Claim-by-claim record

### EP-CLM-000027 — Article 5(1) principles

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 5(1)(a)–(f) |
| **Exact locator** | Article 5(1) |
| **Proposition reviewed** | Personal data shall be processed in accordance with the Art. 5(1) principles (lawfulness/fairness/transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality). |
| **Official-text check** | Art. 5(1) lists six requirements with those official short labels. Claim indexes all six without collapsing into a vague fairness slogan and without inventing extra principles. |
| **Qualification** | None. Companion accountability claim is `000028` (Art. 5(2)), not a qualifier of this claim. |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

### EP-CLM-000028 — Article 5(2) accountability

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 5(2) |
| **Exact locator** | Article 5(2) |
| **Proposition reviewed** | The controller shall be responsible for, and be able to demonstrate compliance with, Article 5(1) (accountability). |
| **Official-text check** | Art. 5(2): “The controller shall be responsible for, and be able to demonstrate compliance with, paragraph 1 (‘accountability’).” Near-exact. Not optional “best practice”. |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

### EP-CLM-000029 — Article 24(1)–(2)

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 24(1)–(2) |
| **Exact locator** | Article 24(1)-(2) |
| **Minted issue** | Compressed “risks” omitted “of varying likelihood and severity for the rights and freedoms of natural persons”; proportionality clause for policies was underspecified relative to Art. 24(2). |
| **Amendment** | Restored full Art. 24(1) risk formula and Art. 24(2) “where proportionate in relation to processing activities … appropriate data protection policies.” |
| **Verdict** | **AMEND BEFORE VERIFICATION → PASS** |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

### EP-CLM-000030 — Article 25 design and default

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 25(1)–(2) |
| **Exact locator** | Article 25 |
| **Minted issue** | Omitted Art. 25(1) calibration factors (state of the art, cost, nature/scope/context/purposes, risk formula) and Art. 25(2) indefinite-accessibility default. |
| **Amendment** | Restored calibration factors + dual timing (determination of means / processing itself) + by-default necessity dimensions + indefinite-accessibility default. |
| **Boundary** | Does not turn Art. 25 into a product-feature checklist beyond the Regulation text. |
| **Verdict** | **AMEND BEFORE VERIFICATION → PASS** |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

### EP-CLM-000031 — Article 28(1)–(4) processor / subprocessor

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 28(1)–(4) |
| **Minted issue** | Proposition cited Art. 28(2)/(4) flow-down/authorisation while `provision_locator` was only `Article 28(1)-(3)` — locator under-coverage. Guarantees/authorisation wording also tightened to track operative text. |
| **Amendment** | (1) Locator → `Article 28(1)-(4)`. (2) Proposition tightened: sufficient guarantees to implement appropriate TOMs meeting Regulation requirements and protecting data-subject rights; Art. 28(3) contract/legal act; prior specific or general written authorisation (28(2)); same-obligation flow-down (28(4)). |
| **Verdict** | **AMEND BEFORE VERIFICATION → PASS** |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

### EP-CLM-000032 — Article 30(1)–(4) records

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 30(1)–(4) |
| **Minted issue** | Proposition includes Art. 30(3)–(4) (writing/electronic form; make available to SA) while locator was only `Article 30(1)-(2)`. |
| **Amendment** | Locator → `Article 30(1)-(4)`. Proposition content otherwise tracks 30(1)(a)–(g), 30(2)(a)–(d), 30(3)–(4). |
| **Qualification** | `qualified_by → EP-CLM-000033` retained. |
| **Verdict** | **AMEND BEFORE VERIFICATION → PASS** |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

### EP-CLM-000033 — Article 30(5) `<250` qualification

| Field | Value |
|---|---|
| **Source viewed** | `EP-SRC-000004` Art. 30(5) |
| **Exact locator** | Article 30(5) |
| **Minted issue** | Art. 10 shorthand “criminal-conviction data” too narrow vs “personal data relating to criminal convictions and offences”. |
| **Amendment** | Aligned to Art. 30(5) wording, including “criminal convictions and offences referred to in Art. 10” and “enterprise or an organisation”. |
| **Critical boundary** | `<250` is **not** an automatic RoPA waiver. The three “unless” triggers remain disjunctive override conditions. |
| **Verdict** | **AMEND BEFORE VERIFICATION → PASS** |
| **Post-state** | `verified` / `Verified` / `2026-08-20` / `validity_state=null` |

---

## Integrity / gate notes

- V1 (`000015`–`000020`) and V2 (`000021`–`000026`) unchanged and remain verified.
- After V3: **19/31** verified (`000015`–`000033`); **12/31** still draft (`000034`–`000045`).
- Deferred unminted set unchanged.
- Sources remain `EP-SRC-000004` / `EP-SRC-000005`.
- No public `regulation/gdpr/claims.json`.
- No HTML change.
- GDPR Publish Gate remains **NOT OPEN**.
- **V4 blocked** until this V3 content + integration gates PASS.
- Planned next logical batch: **V4 = `000034`–`000040`** (security, breach, DPIA, DPO).

---

*Workbench artifact only. Not a published website page.*
