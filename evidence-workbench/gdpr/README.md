# Sprint R2 — GDPR Evidence Graph-grade Upgrade
**Status:** Open — **R2.4** Canonical Graph + Route Integration Preparation  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-4-canonical-prep`  
**Canonical target (later):** `/regulation/gdpr/` + `/regulation/gdpr/claims.json` (EP-REG-002)  
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DEC-047; DEC-048; DEC-049; DEC-050; DISCLOSURE_BOUNDARY.md

---

## Hard rules for this sprint

1. **No live HTML rewrite** of `/regulation/gdpr/` until the Publish Gate sequence (R2.8). R2.5 may produce a **branch-only / non-public** page candidate only.
2. **No** public `/regulation/gdpr/claims.json` until Publish Gate path (R2.8). R2.4 staging stays in workbench.
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
| R2.3 | Human Literal Verification | **CLOSED / PASS** — 31/31 on `main` @ `d02979b…` (PR #35) |
| R2.4 | Canonical Graph + Route Integration Preparation | **OPEN** |
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
| `claims.minted.draft.json` | Verified mint + provenance record (31/31) |
| `claims.canonical.staging.json` | **R2.4** canonical-shaped staging candidate (workbench only) |
| `VERIFICATION_V1`…`V5_2026-08-20.md` | R2.3 literal verification records |
| `R2_4_CANONICAL_PREP.md` | R2.4 scope, gates, route-integration checklist |
| `README.md` | This status note |

---

## Current truth-status

**Verified (batch-1):** `EP-CLM-000015` … `EP-CLM-000045` (**31/31**).

**Deferred / UNMINTED:** Art. 3(3); Art. 9; dynamic adequacy-country list; broad supervisory-authority architecture.

**Sources:** `EP-SRC-000004` (OJ `32016R0679`); `EP-SRC-000005` (consolidated `02016R0679-20160504`).

**Qualification edges (`qualified_by`):** 24→25 · 32→33 · 35→36 · 37→38  

**Chapter V related hierarchy (not `qualified_by`):** 041 ← 042 ← 043 ← 044

`_meta.published=false`; HTML blocked; GDPR Publish Gate **NOT OPEN**.  
**No** public `regulation/gdpr/claims.json`.

---

## Success condition (end of R2)

- AI Act remains ≥90
- GDPR RGS score ≥90 for real six-layer reasons
- Data Act / CRA / EERS / Protocol remain later
- **No expansion opened**

---

*EuraPlan.com — Sprint R2 workbench. Not a published website page.*
