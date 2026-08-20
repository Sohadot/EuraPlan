# GDPR R2.3 — Verification Batch V5 (final)

**Date:** 2026-08-20  
**Scope:** `EP-CLM-000041` … `EP-CLM-000045` (5 claims)  
**Logical block:** Chapter V transfer hierarchy + Art. 83 administrative fines  
**Primary source:** EUR-Lex authentic Official Journal act — CELEX `32016R0679` / `EP-SRC-000004`  
**Reading aid:** CELEX `02016R0679-20160504` / `EP-SRC-000005` (non-replacement)  
**Lifecycle:** batch-open review → `pending_verification`; individual PASS → `verified`  
**Not done:** HTML rewrite · public `/regulation/gdpr/claims.json` · Publish Gate · R2.4

---

## Batch result

| ID | Topic | Verdict | Final state |
|---|---|---|---|
| `EP-CLM-000041` | Art. 44 general transfer principle | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000042` | Art. 45 adequacy pathway | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000043` | Art. 46 appropriate safeguards | **PASS** | `verified` |
| `EP-CLM-000044` | Art. 49(1) derogations | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000045` | Art. 83(2)/(4)/(5) fines | **PASS** | `verified` |

**Score:** 5/5 PASS after 3 pre-verification precision amendments. **VOID:** 0.

**Cumulative R2.3:** **31/31** batch-1 claims verified (pending V5 Integration Gate).

---

## Chapter V hierarchy integrity (related, not qualified_by)

| Claim | Related pathway | Edge type |
|---|---|---|
| `000041` | Chapter V gate | root |
| `000042` | → `000041` | `related_claims` |
| `000043` | → `000041`, `000042` | `related_claims` |
| `000044` | → `000041`, `000042`, `000043` | `related_claims` |

- **Graph-level:** PASS — hierarchy uses `related_claims` / related-pathway notes, **not** `qualified_by`.
- **Modelling rule preserved:** SCCs, adequacy, and Art. 49 derogations are **not** interchangeable equal options.
- **Render-level:** NOT YET TESTABLE; later Publish Gate must present hierarchy without implying equivalence.

---

## Claim-by-claim record

### EP-CLM-000041 — Article 44

- **Locator:** Article 44
- **Minted issue:** Compressed Art. 44 omitted “subject to the other provisions of this Regulation,” onward-transfer destination wording, and “level of protection of natural persons guaranteed by this Regulation.”
- **Amendment:** Restored those operative elements without inventing hierarchy among Art. 45/46/49 inside this claim.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000042 — Article 45(1), (3), (5), (8)

- **Minted issues:** (1) Locator omitted Art. 45(5) while proposition asserted repeal/amend/suspend. (2) Periodic review lacked “at least every four years.”
- **Amendment:** Locator → `Article 45(1), (3), (5), (8)`; restored four-year review cadence and Art. 45(5) repeal/amend/suspend limb; kept Art. 45(8) publication of the list. Still does **not** embed a static country list inside the claim.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000043 — Article 46(1)–(2)

- **Locator:** Article 46(1)-(2)
- **Official-text check:** Absence of Art. 45(3) adequacy; appropriate safeguards + enforceable rights/effective remedies; Art. 46(2) safeguards without specific SA authorisation (including SCCs and BCRs among others). Matches.
- **Boundary:** Does not treat SCCs as interchangeable with adequacy.
- **Verdict:** **PASS**
- **Amendment:** None
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000044 — Article 49(1)

- **Locator:** Article 49(1)
- **Minted issue:** Absence clause underspecified vs Art. 49(1) chapeau (Art. 45(3) / Art. 46 including BCRs).
- **Amendment:** Restored “adequacy decision pursuant to Art. 45(3), or … appropriate safeguards pursuant to Art. 46, including binding corporate rules,” then only Art. 49(1) conditions.
- **Boundary:** Art. 49 consent is not a default ongoing cloud-transfer strategy.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

### EP-CLM-000045 — Article 83(2), (4), (5)

- **Locator:** Article 83(2), (4), (5)
- **Official-text check:** Due regard to Art. 83(2) criteria; Art. 83(4) up to EUR 10 million / 2% turnover; Art. 83(5) up to EUR 20 million / 4% turnover; whichever higher. Preserves tiers + criteria — not a single max number.
- **Boundary:** Does not absorb Art. 83(6) into this claim (out of locator scope).
- **Verdict:** **PASS**
- **Amendment:** None
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`

---

## Integrity / gate notes

- After V5 content: **31/31** verified; **0** draft among minted batch-1 IDs.
- Deferred unminted set still unminted (Art. 3(3), Art. 9, dynamic adequacy list, broad SA architecture).
- Sources remain `EP-SRC-000004` / `EP-SRC-000005`.
- No public `regulation/gdpr/claims.json`.
- No HTML change.
- GDPR Publish Gate remains **NOT OPEN**.
- **R2.3 closes only after V5 Integration Gate PASS** (merge + main verification). Then **R2.4** may open.

---

*Workbench artifact only. Not a published website page.*
