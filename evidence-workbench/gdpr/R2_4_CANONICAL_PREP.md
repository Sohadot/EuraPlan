# R2.4 — Canonical Graph + Route Integration Preparation

**Status:** OPEN  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-4-canonical-prep`  
**Prerequisite:** R2.3 CLOSED / PASS — merge `d02979b5bf48741bc1f2563ea5ee117877778d0f` (PR #35)

---

## What R2.4 is

Convert the verified GDPR workbench graph into a **canonical-shaped staging candidate** and prepare route/machine integration **without** public publication.

R2.4 is **not**:
- HTML rewrite of `/regulation/gdpr/`
- creation of public `/regulation/gdpr/claims.json`
- `workflow_state` promotion to `publishable` / `published`
- Publish Gate opening
- `routes.json` / `llms.txt` / sitemap registration of a GDPR claims alternate

Those belong to later phases (R2.5–R2.8), after staging integrity and co-render design are ready.

---

## Inputs (frozen from R2.3)

| Artifact | Role |
|---|---|
| `claims.minted.draft.json` | Verified propositions + provenance (31/31) |
| `VERIFICATION_V1`…`V5` | Claim-by-claim literal records |
| `SOURCE_REGISTRY.minted.draft.json` | `EP-SRC-000004` / `EP-SRC-000005` |

---

## R2.4 deliverables (this opening)

1. **`claims.canonical.staging.json`** — workbench-only staging graph:
   - AI Act–aligned field set (no R2.1 falsifier / candidate_key baggage in the public-facing shape)
   - Still `workflow_state=verified`, `validity_state=null`, `confidence=Verified`, `_meta.published=false`
   - Target path recorded as `/regulation/gdpr/claims.json` but **file not created there**
2. **This prep note** — gates, co-render blockers, route integration checklist
3. **DEC-050** — close R2.3; open R2.4 under the above constraints

---

## Hard gates during R2.4

| Gate | Rule |
|---|---|
| Public `claims.json` | FORBIDDEN until Publish Gate path |
| HTML rewrite on live `/regulation/gdpr/` | FORBIDDEN in R2.4 and R2.5 until Publish Gate sequence |
| Publish Gate | NOT OPEN |
| Co-render pairs | Must remain design-blocking: 24↔25, 32↔33, 35↔36, 37↔38 |
| Chapter V | related hierarchy, not `qualified_by` equivalence |
| AI Act gold | Untouched except real freshness events |
| Claim→Source edges | Exactly `source_id` + `provision_locator` + `relationship` — no edge-local `note` (EVIDENCE_GRAPH_MODEL.md §4) |

### R2.5 boundary (fixed before page work)

**R2.5 produces a page transformation candidate that is branch-only / non-public.** It must not merge live HTML onto `main` that presents these claims as a public reference surface while they remain `workflow_state=verified` (pre-publication).

Public HTML on `/regulation/gdpr/` that renders the Evidence Graph as the live reference may ship only inside the **Publish Gate sequence (R2.8)** when claims move `publishable → published` and `_meta.published` becomes true — consistent with DEC-050.

R2.5 may still design citation anchors, co-render layout, and hierarchy presentation on a feature branch; it must not treat that branch as a public publication event.

---

## Route integration preparation checklist (design only in R2.4)

When a later phase authorizes public machine representation:

- [ ] Place verified canonical file at `regulation/gdpr/claims.json`
- [ ] Register `alternate_representations` on EP-REG-002 in `routes.json` (mirror AI Act pattern)
- [ ] Expose in `llms.txt` if policy requires
- [ ] **Do not** add `claims.json` to sitemap
- [ ] Citation units `#ep-clm-000015`…`#ep-clm-000045` planned for page anchors in R2.5
- [ ] Page must co-render every `qualified_by` pair; Chapter V must show hierarchy without implying option-equivalence

---

## Exit toward R2.5

R2.4 may close when:

1. Staging graph integrity PASS (31 IDs; edges; sources; published=false; no mojibake; no illegal edge keys)
2. Co-render / hierarchy constraints documented as Publish Gate blockers
3. Route alternate registration plan written (not executed)
4. Owner authorizes R2.5 **branch-only** page transformation work — with explicit understanding that live public HTML + public `claims.json` wait for R2.8 Publish Gate

---

*Workbench artifact only. Not a published website page.*
