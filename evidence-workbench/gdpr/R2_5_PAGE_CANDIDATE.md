# R2.5 — Branch-only Page Transformation

**Status:** CLOSED / PASS  
**Opened:** 2026-08-20  
**Closed:** 2026-08-20  
**Integration merge:** PR #38 `a6b9ed0ea09e2e816b5ef5dd2a0a7dc9960105a6`  
**Prerequisite opening:** PR #37 merge `49336e581f9f088b19bafdd9733d87dfbebb47c9`

---

## What R2.5 delivered

A **GDPR Evidence Graph page candidate** under `evidence-workbench/gdpr/page-candidate/` patterned after the AI Act Claim Register / co-render model, using `claims.canonical.staging.json` as propositional source — **without** publishing it as the live public reference.

Primary inputs:
- `claims.canonical.staging.json` (31 verified claims)
- `claims.minted.draft.json` + `VERIFICATION_V1`…`V5` (provenance)
- AI Act gold page pattern (`/regulation/eu-ai-act/`) for Claim Register / co-render / citation units

---

## Hard gates retained (DEC-050 / DEC-051 / DEC-052)

| Gate | Rule |
|---|---|
| Live `/regulation/gdpr/index.html` on `main` | **DO NOT** rewrite to present the 31 claims as the public Evidence Graph reference |
| Public `/regulation/gdpr/claims.json` | **FORBIDDEN** until R2.8 Publish Gate |
| Claim workflow | Remains `verified` (not `publishable` / `published`) |
| Publish Gate | **NOT OPEN** |
| Candidate location | Workbench only — `evidence-workbench/gdpr/page-candidate/` |
| Co-render | Every `qualified_by` pair displays together (24↔25, 32↔33, 35↔36, 37↔38) |
| Chapter V | Related hierarchy without option-equivalence |
| AI Act gold | Untouched except real freshness events |

**R2.5 was not a public publication event.** Live route HTML that renders the claim graph as the canonical public reference ships only in the **R2.8 Publish Gate sequence**.

---

## Closed deliverables

1. Page candidate HTML under `evidence-workbench/gdpr/page-candidate/`
2. Citation units `#ep-clm-000015` … `#ep-clm-000045`
3. Verified Claim Register driven by staging propositions
4. Co-render blocks for the four qualification pairs + Chapter V hierarchy presentation
5. Explicit banner/meta: *workbench candidate — not live published reference*

---

## Exit to R2.6

Owner fidelity gate PASS on PR #38. Next phase: **R2.6 — Decision Utility Layer** (DEC-052). R2.7 / R2.8 remain blocked.

---

*Workbench artifact only. Not a published website page.*
