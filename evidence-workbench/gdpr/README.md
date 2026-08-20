# Sprint R2 — GDPR Evidence Graph-grade Upgrade
**Status:** Open — R2.3 human literal verification in progress (V1–V4 PASS for EP-CLM-000015…000040)
**Opened:** 2026-08-20
**Branch:** `sprint-r2-gdpr-r2-3-v4-verification`
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
| R2.2 | Identity Fixation + Source Pinning + Draft Serialization | **CLOSED / PASS** (content + integration) |
| R2.3 | Human Literal Verification | **IN PROGRESS** — **V1–V4 PASS** (`000015`–`000040` = 26/31); **V5 next** |
| R2.4 | Canonical graph + routes alternate | Not started |
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
| `claims.minted.draft.json` | Minted identities — `000015`–`000040` verified; `000041`–`000045` remain draft |
| `VERIFICATION_V1_2026-08-20.md` | R2.3 V1 |
| `VERIFICATION_V2_2026-08-20.md` | R2.3 V2 |
| `VERIFICATION_V3_2026-08-20.md` | R2.3 V3 |
| `VERIFICATION_V4_2026-08-20.md` | R2.3 V4 |
| `README.md` | This status note |

---

## Current truth-status

**Verified:** `EP-CLM-000015` … `EP-CLM-000040` (26/31).

**Still draft:** `EP-CLM-000041` … `EP-CLM-000045` (5/31).

**Deferred / UNMINTED:** Art. 3(3); Art. 9; dynamic adequacy-country list; broad supervisory-authority architecture.

**Sources:** `EP-SRC-000004` (OJ `32016R0679`); `EP-SRC-000005` (consolidated `02016R0679-20160504`).

**Qualification edges retained:**
- `000024` → `000025` (Art. 27)
- `000032` → `000033` (Art. 30)
- `000035` → `000036` (Art. 33)
- `000037` → `000038` (Art. 34)

Visible co-rendering of qualified pairs remains a blocking later Publish Gate condition.

`_meta.published=false`; HTML blocked; GDPR Publish Gate **NOT OPEN**.

**Remaining R2.3 batch:**
- **V5:** `000041`–`000045` — Chapter V transfers + Art. 83 fines

---

## Success condition (end of R2)

- AI Act remains ≥90
- GDPR RGS score ≥90 for real six-layer reasons
- Data Act / CRA / EERS / Protocol remain later
- **No expansion opened**

---

*EuraPlan.com — Sprint R2 workbench. Not a published website page.*
