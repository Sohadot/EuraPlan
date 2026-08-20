# Sprint R2 — GDPR Evidence Graph-grade Upgrade
**Status:** Open — R2.2 Draft Minting & Source Pinning complete locally; human verification not started
**Opened:** 2026-08-20
**Branch:** `sprint-r2-gdpr-r2-2-draft-mint`
**Canonical target (later):** `/regulation/gdpr/` + `/regulation/gdpr/claims.json` (EP-REG-002)
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DEC-047; DEC-048; DEC-049; DISCLOSURE_BOUNDARY.md

---

## Hard rules for this sprint

1. **No HTML rewrite** of `/regulation/gdpr/` until R2.4 after verified claims exist.
2. **No** `/regulation/gdpr/claims.json` until after human verification + Publish Gate path (R2.3+).
3. **Minting fixes identity, not truth-status.** Draft IDs `EP-CLM-000015`…`EP-CLM-000045` are permanently reserved for their R2.2 propositions. Do not recycle; use `void` + new ID if a proposition fails before publish.
4. **No** parallel Data Act / country / expansion work.
5. Claim count follows **material truth** for non-EU entry planning — not a 14-claim template.
6. Global opaque ID sequence only — never `GDPR-CLM-*`.
7. Defaults that have exceptions (`unless` / `except` / thresholds) must carry `qualified_by` — never publish a default alone.
8. **No** generic Commission overview or EDPB guidelines-portfolio `EP-SRC-*`. Pin specific instruments only when a claim needs them at verification.

---

## Phase checklist

| Phase | Name | State |
|---|---|---|
| R2.0 | Source & Claim Discovery | **CLOSED / PASS** |
| R2.1 | Claim Map & Falsification | **CLOSED / PASS** — `CLAIM_MAP_R2_1.draft.json` (31 keep / 4 defer) |
| R2.2 | Identity Fixation + Source Pinning + Draft Serialization | **CLOSED / PASS (workbench)** — `claims.minted.draft.json` + `SOURCE_REGISTRY.minted.draft.json` |
| R2.3 | Human Literal Verification (`draft` → `pending_verification` → `verified`) | **NEXT — NOT STARTED** |
| R2.4 | Canonical graph + routes alternate | Not started |
| R2.5 | Page transformation | Not started |
| R2.6 | Decision utility layer | Hints in claim map; deepen at page stage |
| R2.7 | Citation + machine + llms/routes/sitemap | Not started |
| R2.8 | GDPR Publish Gate → RGS re-score ≥90 | Not started |

---

## Workbench files (Class 2 public working evidence)

| File | Role |
|---|---|
| `SOURCE_REGISTRY.draft.json` | R2.0 candidate sources (Commission/EDPB remain unminted) |
| `SOURCE_REGISTRY.minted.draft.json` | **R2.2** pinned `EP-SRC-000004` / `EP-SRC-000005` + freshness watch |
| `CLAIM_CANDIDATES.draft.md` | R2.0 discovery intake |
| `CLAIM_MAP_R2_1.draft.json` | R2.1 truth filter — falsification + KEEP/SPLIT/DEFER |
| `claims.minted.draft.json` | **R2.2** draft identity fixation — 31 claims; `_meta.published: false` |
| `README.md` | This status note |

---

## R2.2 identity range (owner-approved Batch-1)

| Permanent ID | Candidate key |
|---|---|
| `EP-CLM-000015` … `EP-CLM-000045` | 31 KEEP from R2.1 (see `_meta.candidate_to_claim_id`) |

**Deferred / UNMINTED (no IDs):** Art. 3(3); Art. 9; dynamic adequacy-country list; broad supervisory-authority architecture.

**Sources minted:** `EP-SRC-000004` (OJ `32016R0679`); `EP-SRC-000005` (consolidated `02016R0679-20160504`).

**Draft state (all 31):** `workflow_state=draft`; `validity_state=null`; `last_verified_at=null`; `confidence=Pending`; `_meta.published=false`.

---

## Success condition (end of R2)

- AI Act remains ≥90 (untouched except real freshness events)
- GDPR RGS score ≥90 for real six-layer reasons
- Data Act / CRA / EERS / Protocol still later
- **No expansion opened**

---

*EuraPlan.com — Sprint R2 workbench. Not a published website page.*
