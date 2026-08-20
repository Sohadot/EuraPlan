# GDPR R2.3 — Verification Batch V1
**Date:** 2026-08-20  
**Scope:** `EP-CLM-000015` … `EP-CLM-000020` (6 claims)  
**Primary source viewed:** EUR-Lex authentic Official Journal act — CELEX `32016R0679` / `EP-SRC-000004`  
**Retrieval URL:** https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679  
**Reading aid (non-replacement):** CELEX `02016R0679-20160504` / `EP-SRC-000005`  
**Reviewer:** Agent (literal check against OJ EN text) + owner-directed batch opening  
**Lifecycle rule applied:** at batch open → `pending_verification`; after independent PASS → `verified`  
**Not done:** HTML rewrite · public `/regulation/gdpr/claims.json` · Publish Gate · remaining 25 claims

---

## Batch result

| ID | Verdict | Post-state |
|---|---|---|
| `EP-CLM-000015` | **PASS** | `verified` |
| `EP-CLM-000016` | **AMEND BEFORE VERIFICATION** (encoding only) → **PASS** | `verified` |
| `EP-CLM-000017` | **PASS** | `verified` |
| `EP-CLM-000018` | **PASS** | `verified` |
| `EP-CLM-000019` | **PASS** | `verified` |
| `EP-CLM-000020` | **PASS** | `verified` |

**Score:** 6/6 PASS (1 non-material amend). **VOID:** 0.  
**Identity rule:** no ID recycled. Truth-status updated only for these six.

---

## Critical separation (V1 emphasis)

| Event | Date | Source |
|---|---|---|
| Entry into force (Art. 99(1)) | **24 May 2016** (20th day after OJ publication 4 May 2016) | Art. 99(1) + OJ L 119, 4.5.2016 |
| Application (Art. 99(2)) | **25 May 2018** | Art. 99(2) |

These must never be conflated on clock or planning surfaces.

---

## Claim-by-claim record

### EP-CLM-000015 — Instrument identity / CELEX

| Field | Value |
|---|---|
| **ID** | `EP-CLM-000015` |
| **Candidate** | `GDPR-PROP-CAND-01` |
| **Source viewed** | `EP-SRC-000004` CELEX `32016R0679` (title block + OJ citation) |
| **Exact locator** | Instrument title / CELEX `32016R0679`; OJ L 119, 4.5.2016 |
| **Proposition reviewed** | The GDPR is Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016, CELEX 32016R0679. |
| **Qualification checked** | None required (identity proposition). |
| **Official text check** | Title matches: “REGULATION (EU) 2016/679 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 27 April 2016 … (General Data Protection Regulation)”. CELEX `32016R0679` is the correct EUR-Lex identifier for the authentic OJ act (bibliographic, not a body article). |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Reviewer / date** | Agent literal review · 2026-08-20 |
| **Post-verification state** | `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`; `published=false` |

---

### EP-CLM-000016 — Article 99(1) entry into force

| Field | Value |
|---|---|
| **ID** | `EP-CLM-000016` |
| **Candidate** | `GDPR-PROP-CAND-02` |
| **Source viewed** | `EP-SRC-000004` Art. 99(1); OJ L 119, 4.5.2016 |
| **Exact locator** | Article 99(1); OJ L 119, 4.5.2016 |
| **Proposition reviewed (as minted)** | Entered into force on the twentieth day following OJ publication (published 4 May 2016 → 24 May 2016). |
| **Qualification checked** | None for the entry-into-force rule itself. Must not be read as application date. |
| **Official text check** | Art. 99(1): “This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.” Publication: OJ L 119, **4.5.2016**. Twentieth day → **24 May 2016**. Distinct from Art. 99(2) application date. |
| **Verdict** | **AMEND BEFORE VERIFICATION** → **PASS** |
| **Amendment** | Non-material encoding repair only: mint-time UTF-8 corruption of the arrow character (`â†’`) replaced with ASCII `->` so the date calculation remains human-readable. **No change to dates, locator, or legal meaning.** |
| **Proposition after amend** | `… (published 4 May 2016 -> 24 May 2016).` |
| **Reviewer / date** | Agent literal review · 2026-08-20 |
| **Post-verification state** | `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`; `published=false` |

---

### EP-CLM-000017 — Article 99(2) application

| Field | Value |
|---|---|
| **ID** | `EP-CLM-000017` |
| **Candidate** | `GDPR-PROP-CAND-03` |
| **Source viewed** | `EP-SRC-000004` Art. 99(2) |
| **Exact locator** | Article 99(2) |
| **Proposition reviewed** | Regulation (EU) 2016/679 applies from 25 May 2018. |
| **Qualification checked** | None for the general application date. |
| **Official text check** | Art. 99(2): “It shall apply from 25 May 2018.” Exact match. Not entry into force. |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Reviewer / date** | Agent literal review · 2026-08-20 |
| **Post-verification state** | `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`; `published=false` |

---

### EP-CLM-000018 — Article 3(1) Union establishment

| Field | Value |
|---|---|
| **ID** | `EP-CLM-000018` |
| **Candidate** | `GDPR-PROP-CAND-04` |
| **Source viewed** | `EP-SRC-000004` Art. 3(1) |
| **Exact locator** | Article 3(1) |
| **Proposition reviewed** | GDPR applies to processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union. |
| **Qualification checked** | Not a substitute for Art. 3(2) non-establishment limbs (`000019`/`000020`). No `qualified_by` edge required. |
| **Official text check** | Art. 3(1): “This Regulation applies to the processing of personal data in the context of the activities of an establishment of a controller or a processor in the Union, regardless of whether the processing takes place in the Union or not.” Claim is faithful; “The GDPR” naming and omission of trailing “or not” are non-expansive. Does not exceed text. |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Reviewer / date** | Agent literal review · 2026-08-20 |
| **Post-verification state** | `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`; `published=false` |

---

### EP-CLM-000019 — Article 3(2)(a) offering goods/services

| Field | Value |
|---|---|
| **ID** | `EP-CLM-000019` |
| **Candidate** | `GDPR-PROP-CAND-05` |
| **Source viewed** | `EP-SRC-000004` Art. 3(2) chapeau + (a) |
| **Exact locator** | Article 3(2)(a) |
| **Proposition reviewed** | Applies to processing of personal data of data subjects who are in the Union by a controller or processor not established in the Union where processing activities are related to the offering of goods or services to such data subjects in the Union, irrespective of whether a payment is required. |
| **Qualification checked** | Limb-limited to offering-related activities; not a catch-all EU contact rule. Sibling limb is Art. 3(2)(b) (`000020`), not a qualifier of this claim. |
| **Official text check** | Art. 3(2)+(a) matches: data subjects in the Union; controller/processor not established in the Union; activities related to offering of goods or services to such data subjects in the Union; irrespective of payment. Meaning does not exceed text. |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Reviewer / date** | Agent literal review · 2026-08-20 |
| **Post-verification state** | `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`; `published=false` |

---

### EP-CLM-000020 — Article 3(2)(b) monitoring behaviour

| Field | Value |
|---|---|
| **ID** | `EP-CLM-000020` |
| **Candidate** | `GDPR-PROP-CAND-06` |
| **Source viewed** | `EP-SRC-000004` Art. 3(2) chapeau + (b) |
| **Exact locator** | Article 3(2)(b) |
| **Proposition reviewed** | Applies to processing of personal data of data subjects who are in the Union by a controller or processor not established in the Union where processing activities are related to the monitoring of their behaviour as far as their behaviour takes place within the Union. |
| **Qualification checked** | Limited to behaviour monitoring within the Union; not every analytics cookie worldwide. Sibling limb is Art. 3(2)(a) (`000019`). |
| **Official text check** | Art. 3(2)+(b): “the monitoring of their behaviour as far as their behaviour takes place within the Union.” Claim tracks chapeau + (b) without expansion. |
| **Verdict** | **PASS** |
| **Amendment** | None |
| **Reviewer / date** | Agent literal review · 2026-08-20 |
| **Post-verification state** | `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`; `published=false` |

---

## Integrity / gate notes

- Remaining claims `EP-CLM-000021`…`EP-CLM-000045`: still `draft` / `Pending` / `last_verified_at=null`.
- Deferred unminted set unchanged (Art. 3(3), Art. 9, dynamic adequacy list, broad SA architecture).
- Sources still only `EP-SRC-000004` / `EP-SRC-000005` for evidentiary pins.
- No public `regulation/gdpr/claims.json`.
- No HTML change.
- GDPR Publish Gate: **NOT OPEN**.
- Next free verification batch: **V2** (recommend roles / Art. 4–27 cluster or next contiguous IDs per owner).

---

*Workbench artifact only. Not a published website page.*
