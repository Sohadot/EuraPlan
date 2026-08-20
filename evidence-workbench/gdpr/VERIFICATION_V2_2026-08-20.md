# GDPR R2.3 — Verification Batch V2

**Date:** 2026-08-20  
**Scope:** `EP-CLM-000021` … `EP-CLM-000026` (6 claims)  
**Logical block:** Roles → Representative → Lawfulness Gate  
**Primary source:** EUR-Lex authentic Official Journal act — CELEX `32016R0679` / `EP-SRC-000004`  
**Reading aid:** CELEX `02016R0679-20160504` / `EP-SRC-000005` (non-replacement)  
**Lifecycle:** batch-open review → `pending_verification`; individual PASS → `verified`  
**Not done:** HTML rewrite · public `/regulation/gdpr/claims.json` · Publish Gate · V3+

## Batch result

| ID | Topic | Verdict | Final state |
|---|---|---|---|
| `EP-CLM-000021` | Art. 4(7) controller | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000022` | Art. 4(8) processor | **PASS** | `verified` |
| `EP-CLM-000023` | Art. 26(1)–(2) joint controllers | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000024` | Art. 27(1) representative duty | **PASS** | `verified` |
| `EP-CLM-000025` | Art. 27(2) exceptions | **AMEND BEFORE VERIFICATION → PASS** | `verified` |
| `EP-CLM-000026` | Art. 6(1) lawfulness gate | **PASS** | `verified` |

**Score:** 6/6 PASS after 3 pre-verification precision amendments. **VOID:** 0.

## Qualification integrity — `000024` ↔ `000025`

`EP-CLM-000024` already carries `qualified_by: ["EP-CLM-000025"]`.

- **Graph-level test:** PASS — the qualification edge is explicit and directional.
- **Render-level test:** NOT YET TESTABLE — there is no public GDPR claim renderer or HTML in R2.3.
- **Blocking publication condition:** under `EVIDENCE_GRAPH_MODEL.md` §6, any future published rendering of `000024` must visibly co-render `000025`; standalone rendering is prohibited.

This distinction preserves honesty: V2 verifies the graph relation now and turns visible co-rendering into a later Publish Gate check rather than claiming an interface behavior that does not yet exist.

## Claim-by-claim record

### EP-CLM-000021 — Article 4(7) controller

- **Locator:** Article 4(7)
- **Official-text result:** The definition is supported, but the minted shorthand over-broadened the legal-designation clause by omitting its condition.
- **Amendment:**  
  `Controller means the natural or legal person, public authority, agency or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data; where the purposes and means of such processing are determined by Union or Member State law, the controller or the specific criteria for its nomination may be provided for by Union or Member State law.`
- **Falsifier preserved:** hosting/storing data alone does not establish controllership.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `workflow_state=verified`; `confidence=Verified`; `last_verified_at=2026-08-20`; `validity_state=null`.

### EP-CLM-000022 — Article 4(8) processor

- **Locator:** Article 4(8)
- **Official-text result:** The minted definition tracks the operative definition: processing personal data **on behalf of** the controller.
- **Boundary:** no inference that every SaaS/cloud vendor is automatically a processor.
- **Verdict:** **PASS**
- **Amendment:** None.
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`.

### EP-CLM-000023 — Article 26(1)–(2) joint controllers

- **Locator:** Article 26(1)–(2)
- **Official-text result:** Core proposition is correct, but the minted sentence did not state the Art. 26(2) requirement that the arrangement duly reflect respective roles and relationships.
- **Amendment:**  
  `Where two or more controllers jointly determine the purposes and means of processing, they are joint controllers. They shall in a transparent manner determine their respective responsibilities for compliance by arrangement, unless and in so far as those responsibilities are determined by Union or Member State law to which they are subject. The arrangement shall duly reflect their respective roles and relationships vis-à-vis data subjects, and its essence shall be made available to the data subject.`
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`.

### EP-CLM-000024 — Article 27(1) representative duty

- **Locator:** Article 27(1)
- **Official-text result:** Supported as minted.
- **Qualification:** `qualified_by → EP-CLM-000025` must remain.
- **Verdict:** **PASS**
- **Amendment:** None.
- **Publication constraint:** later human/machine rendering must co-display the Art. 27(2) exception claim.
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`.

### EP-CLM-000025 — Article 27(2) exceptions

- **Locator:** Article 27(2)(a)–(b)
- **Official-text result:** Structure is correct and conjunctive, but the minted shorthand narrowed Art. 10 and omitted “of natural persons”.
- **Amendment:**  
  `The Art. 27(1) designation obligation does not apply to (a) processing that is occasional, does not include, on a large scale, processing of special categories of data referred to in Art. 9(1) or personal data relating to criminal convictions and offences referred to in Art. 10, and is unlikely to result in a risk to the rights and freedoms of natural persons, taking into account the nature, context, scope and purposes of the processing; or (b) a public authority or body.`
- **Falsifier preserved:** occasionality alone is insufficient.
- **Verdict:** **AMEND BEFORE VERIFICATION → PASS**
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`.

### EP-CLM-000026 — Article 6(1) lawfulness structural gate

- **Locator:** Article 6(1)
- **Official-text result:** Supported as a single structural gate.
- **Boundary:** does not choose a legal basis for any company and does not imply that consent is required.
- **Verdict:** **PASS**
- **Amendment:** None.
- **Post-state:** `verified` / `Verified` / `2026-08-20` / `validity_state=null`.

## Integrity / gate notes

- V1 (`000015`–`000020`) remains unchanged and verified.
- V2 intended final state: `000021`–`000026` verified.
- `000027`–`000045` remain `draft` / `Pending` / `last_verified_at=null`.
- Deferred unminted set unchanged.
- Sources remain `EP-SRC-000004` / `EP-SRC-000005`.
- No public `regulation/gdpr/claims.json`.
- No HTML change.
- GDPR Publish Gate remains **NOT OPEN**.
- V3 remains blocked until V2 content + integration gates pass.

*Workbench artifact only. Not a published website page.*
