# Sprint R2 — GDPR Evidence Graph-grade Upgrade
**Status:** Open — R2.3 V5 content complete (31/31 verified pending V5 Integration Gate)
**Opened:** 2026-08-20
**Branch:** `sprint-r2-gdpr-r2-3-v5-verification`
**Canonical target (later):** `/regulation/gdpr/` + `/regulation/gdpr/claims.json` (EP-REG-002)
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DEC-047; DEC-048; DEC-049; DISCLOSURE_BOUNDARY.md

---

## Hard rules for this sprint

1. **No HTML rewrite** of `/regulation/gdpr/` until R2.4 after verified claims exist.
2. **No** `/regulation/gdpr/claims.json` until after human verification + Publish Gate path.
3. **Minting fixes identity, not truth-status.** IDs `EP-CLM-000015`…`EP-CLM-000045` are permanently reserved; never recycle.
4. **No** parallel Data Act / country / expansion work.
5. Claim count follows **material truth** for non-EU entry planning — not a template.
6. Global opaque ID sequence only — never `GDPR-CLM-*`.
7. Defaults with exceptions must carry `qualified_by`; a published default may never render without its qualifier.
8. No generic Commission/EDPB portfolio source nodes; pin specific instruments only when needed.

---

## Phase checklist

| Phase | Name | State |
|---|---|---|
| R2.0 | Source & Claim Discovery | **CLOSED / PASS** |
| R2.1 | Claim Map & Falsification | **CLOSED / PASS** |
| R2.2 | Identity Fixation + Source Pinning + Draft Serialization | **CLOSED / PASS** |
| R2.3 | Human Literal Verification | **V1–V5 content PASS (31/31)** — **V5 Integration Gate pending** |
| R2.4 | Canonical graph + routes alternate | Not started — opens only after V5 Integration Gate |
| R2.5 | Page transformation | Not started |
| R2.6 | Decision utility layer | Hints in claim map; deepen at page stage |
| R2.7 | Citation + machine + llms/routes/sitemap | Not started |
| R2.8 | GDPR Publish Gate → RGS re-score ≥90 | Not started |

---

## Workbench files

| File | Role |
|---|---|
| `SOURCE_REGISTRY.draft.json` | R2.0 candidate sources |
| `SOURCE_REGISTRY.minted.draft.json` | R2.2 pinned sources + freshness watch |
| `CLAIM_CANDIDATES.draft.md` | R2.0 discovery intake |
| `CLAIM_MAP_R2_1.draft.json` | R2.1 truth filter |
| `claims.minted.draft.json` | Minted identities — **31/31 verified** after V1–V5 (pending V5 merge) |
| `VERIFICATION_V1_2026-08-20.md` … `VERIFICATION_V5_2026-08-20.md` | R2.3 literal verification records |
| `README.md` | This status note |

---

## Current truth-status

**Verified (batch-1):** `EP-CLM-000015` … `EP-CLM-000045` (**31/31**).

**Deferred / UNMINTED:** Art. 3(3); Art. 9; dynamic adequacy-country list; broad supervisory-authority architecture.

**Sources:** `EP-SRC-000004` (OJ `32016R0679`); `EP-SRC-000005` (consolidated `02016R0679-20160504`).

**Qualification edges (`qualified_by`):**
- `000024` → `000025` (Art. 27)
- `000032` → `000033` (Art. 30)
- `000035` → `000036` (Art. 33)
- `000037` → `000038` (Art. 34)

**Chapter V related hierarchy (not `qualified_by`):**
- `000042`/`000043`/`000044` → related pathway to `000041`

`_meta.published=false`; HTML blocked; GDPR Publish Gate **NOT OPEN**.

---

## Success condition (end of R2)

- AI Act remains ≥90
- GDPR RGS score ≥90 for real six-layer reasons
- Data Act / CRA / EERS / Protocol remain later
- **No expansion opened**

---

*EuraPlan.com — Sprint R2 workbench. Not a published website page.*
