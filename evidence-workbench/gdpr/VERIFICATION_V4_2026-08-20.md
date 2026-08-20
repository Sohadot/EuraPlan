# GDPR R2.3 — Verification Batch V4

**Date:** 2026-08-20  
**Scope:** `EP-CLM-000034` … `EP-CLM-000040` (7 claims)  
**Logical block:** Security → Breach SA Notification → Data-Subject Communication → DPIA → DPO triggers  
**Primary source:** EUR-Lex authentic Official Journal act — CELEX `32016R0679` / `EP-SRC-000004`  
**Reading aid:** CELEX `02016R0679-20160504` / `EP-SRC-000005` (non-replacement)  
**Lifecycle:** batch-open review → `pending_verification`; individual PASS → `verified`  
**Not done:** HTML rewrite · public `/regulation/gdpr/claims.json` · Publish Gate · V5

---

## Batch result

| ID | Topic | Verdict | Final state |
|---|---|---|---|
| `EP-CLM-000034` | Art. 32(1)–(2) security | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000035` | Art. 33(1) SA notification | **PASS** | `verified` |
| `EP-CLM-000036` | Art. 33(1) unlikely-risk exception | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000037` | Art. 34(1)–(2) data-subject communication | **PASS** | `verified` |
| `EP-CLM-000038` | Art. 34(3) communication exceptions | **PASS** | `verified` |
| `EP-CLM-000039` | Art. 35(1), (3) DPIA | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000040` | Art. 37(1)(a)–(c) DPO triggers | **AMEND BEFORE VERIFICATION → PASS** | `verified` |

**Score:** 7/7 PASS after 4 pre-verification precision amendments. **VOID:** 0.

---

## Qualification integrity

### `000035` ↔ `000036` (Art. 33)

- Graph-level: PASS — `000035.qualified_by = ["EP-CLM-000036"]`.
- Substance: default 72-hour/undue-delay SA notification is qualified by the unlikely-risk non-notification limb embedded in Art. 33(1).
- Render-level: NOT YET TESTABLE; co-rendering is a blocking later Publish Gate condition.

### `000037` ↔ `000038` (Art. 34)

- Graph-level: PASS — `000037.qualified_by = ["EP-CLM-000038"]`.
- Substance: high-risk data-subject communication is qualified by Art. 34(3)(a)–(c) exceptions.
- Render-level: NOT YET TESTABLE; co-rendering is a blocking later Publish Gate condition.

---

## Claim-by-claim record

### EP-CLM-000034 — Article 32(1)–(2)

- **Locator:** Article 32(1)-(2)
- **Minted issue:** Compressed risk language (“and risk”) understated Art. 32(1) “risk of varying likelihood and severity for the rights and freedoms of natural persons,” and Art. 32(2) was summarized too loosely.
- **Amendment:** Restored full Art. 32(1) calibration formula (state of the art, costs, nature/scope/context/purposes, risk formula), “including inter alia as appropriate” for (a)–(d), and Art. 32(2) breach-type risk catalogue.
- **Boundary:** Encryption alone is not Art. 32 compliance.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000035 — Article 33(1) default SA notification

- **Locator:** Article 33(1)
- **Official-text check:** Without undue delay and, where feasible, not later than 72 hours after becoming aware; reasons if later. “Competent … Article 55” matches. Unless-clause correctly deferred to `000036` via `qualified_by`.
- **Verdict:** **PASS**
- **Amendment:** None
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000036 — Article 33(1) unlikely-risk exception

- **Locator (after amend):** Article 33(1) unless clause
- **Official-text check:** Non-notification where breach is unlikely to result in a risk to the rights and freedoms of natural persons — exact.
- **Amendment:** Cleaned mint-time locator encoding corruption only (no legal-meaning change).
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000037 — Article 34(1)–(2)

- **Locator:** Article 34(1)-(2)
- **Official-text check:** High-risk threshold; communicate without undue delay; clear and plain language; at least Art. 33(3)(b)–(d). Does not equate every Art. 33 SA notification with data-subject communication.
- **Qualification:** `qualified_by → 000038`
- **Verdict:** **PASS**
- **Amendment:** None
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000038 — Article 34(3)

- **Locator:** Article 34(3)
- **Official-text check:** Exceptions (a) TOMs/encryption rendering unintelligible; (b) subsequent measures ending high-risk likelihood; (c) disproportionate effort → public communication or similarly effective measure. Matches operative text without expanding beyond it.
- **Verdict:** **PASS**
- **Amendment:** None
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000039 — Article 35(1), (3)

- **Locator:** Article 35(1), (3)
- **Minted issues:** Encoding corruption around dashes; Art. 35(3) shorthand “Art. 9/10 data” too loose vs Art. 10 “criminal convictions and offences”; missing clarity that DPIA is of envisaged processing operations prior to processing.
- **Amendment:** Restored Art. 35(1) high-risk gate + prior-to-processing DPIA; expanded Art. 35(3)(a)–(c) to track official particular cases, including Art. 10 wording.
- **Boundary:** New technology alone does not force DPIA without high-risk analysis.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000040 — Article 37(1)(a)–(c)

- **Locator:** Article 37(1)(a)-(c)
- **Minted issues:** (b) omitted “by virtue of their nature, their scope and/or their purposes”; (c) used “criminal-conviction data” shorthand.
- **Amendment:** Restored full trigger disjunction (a)/(b)/(c) tracking Art. 37(1), including nature/scope/purposes in (b) and Art. 10 “criminal convictions and offences” in (c).
- **Modelling note:** Remains trigger-based — no invented universal DPO duty + fake qualifiers.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

---

## Integrity / gate notes

- V1–V3 remain verified (`000015`–`000033`).
- After V4: **26/31** verified (`000015`–`000040`); **5/31** still draft (`000041`–`000045`).
- Qualification edges retained: 24→25, 32→33, **35→36**, **37→38**.
- No public `regulation/gdpr/claims.json`; no HTML change; Publish Gate **NOT OPEN**.
- **V5 blocked** until V4 content + integration PASS.
- Planned V5: `000041`–`000045` — Chapter V transfers + Art. 83 fines.

---

*Workbench artifact only. Not a published website page.*
