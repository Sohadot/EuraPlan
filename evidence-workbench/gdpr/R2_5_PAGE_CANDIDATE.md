# R2.5 — Branch-only Page Transformation

**Status:** OPEN — HTML candidate delivered in workbench (`page-candidate/index.html`)  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-5-html-candidate`  
**Prerequisite:** R2.5 opening CLOSED on `main` via PR #37 merge `49336e581f9f088b19bafdd9733d87dfbebb47c9`

---

## What R2.5 is

Design and build a **GDPR Evidence Graph page candidate** that can later replace the summary-grade `/regulation/gdpr/` surface — **without** publishing it as the live public reference yet.

Primary inputs:
- `claims.canonical.staging.json` (31 verified claims)
- `claims.minted.draft.json` + `VERIFICATION_V1`…`V5` (provenance)
- AI Act gold page pattern (`/regulation/eu-ai-act/`) for Claim Register / co-render / citation units

---

## Hard gates (DEC-050 / DEC-051)

| Gate | Rule |
|---|---|
| Live `/regulation/gdpr/index.html` on `main` | **DO NOT** rewrite to present the 31 claims as the public Evidence Graph reference |
| Public `/regulation/gdpr/claims.json` | **FORBIDDEN** until R2.8 Publish Gate |
| Claim workflow | Remains `verified` (not `publishable` / `published`) |
| Publish Gate | **NOT OPEN** |
| Candidate location | Workbench / feature branch only — e.g. `evidence-workbench/gdpr/page-candidate/` |
| Co-render | Every `qualified_by` pair must display together (24↔25, 32↔33, 35↔36, 37↔38) |
| Chapter V | Show related hierarchy without implying option-equivalence |
| AI Act gold | Untouched except real freshness events |

**R2.5 is not a public publication event.** Merging an R2.5 PR to `main` may update workbench candidate artifacts and governance notes only. Live route HTML that renders the claim graph as the canonical public reference ships only in the **R2.8 Publish Gate sequence** when claims move `publishable → published`.

---

## Intended candidate deliverables

1. **Page candidate HTML** under `evidence-workbench/gdpr/page-candidate/` (not `regulation/gdpr/`).
2. **Citation units** `#ep-clm-000015` … `#ep-clm-000045`.
3. **Verified Claim Register** section patterned after AI Act, driven by staging propositions.
4. **Co-render blocks** for the four qualification pairs + Chapter V related pathway presentation.
5. **Planning utility** sections that stay non-advisory and source-bound.
6. Explicit banner/meta on the candidate: *workbench candidate — not live published reference*.

---

## Exit toward R2.6 / R2.7 / R2.8

R2.5 may close when the branch-only candidate is owner-reviewed for:
- proposition fidelity to staging claims
- co-render / hierarchy integrity
- no live-route pollution
- no premature `claims.json` / routes / llms / sitemap registration

Then:
- **R2.6** decision-utility deepen (still gated)
- **R2.7** citation + machine registration prep
- **R2.8** Publish Gate → `publishable`/`published` + live HTML + public `claims.json`

---

*Workbench artifact only. Not a published website page.*
