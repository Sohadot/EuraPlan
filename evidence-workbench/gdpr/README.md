# Sprint R2 — GDPR Evidence Graph-grade Upgrade
**Status:** **R2.8 COMPLETE — Gates 0–6 CLOSED / PASS; GDPR Evidence Graph reference LIVE since 2026-08-23; RGS v2 = 97.5 / 100**  
**Development state:** **FROZEN (DEC-057, 2026-08-23).** No cosmetic edits or re-wording. EP-REG-002 changes only on a real trigger — freshness trigger (FRESHNESS_ENGINE.md) · genuine correction · supersession · clear functional need — each recorded, none advancing `last_verified_at` or provenance without the corresponding real event.  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-8-publish-gate-open`  
**Canonical target:** `/regulation/gdpr/` + `/regulation/gdpr/claims.json` (EP-REG-002)  
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DEC-047…DEC-055; DISCLOSURE_BOUNDARY.md; ROUTE_GOVERNANCE.md

---

## Hard rules for this sprint

1. **No live HTML rewrite** of `/regulation/gdpr/` until R2.8 Gates 2–5 authorize the publication sequence.
2. **No** public `/regulation/gdpr/claims.json` until R2.8 Gates 1–5 authorize it. Staging stays in workbench until then.
3. **Minting fixes identity, not truth-status.** IDs `EP-CLM-000015`…`EP-CLM-000045` are permanently reserved; never recycle.
4. **No** parallel Data Act / country / expansion work before GDPR RGS ≥90 post Gate 6.
5. Claim count follows **material truth** for non-EU entry planning — not a template.
6. Global opaque ID sequence only — never `GDPR-CLM-*`.
7. Defaults with exceptions must carry `qualified_by`; a published default may never render without its qualifier.
8. No generic Commission/EDPB portfolio source nodes; pin specific instruments only when needed.
9. **R2.6 Decision Utility** is a derived planning layer. Seeds are not verified facts.
10. **R2.7** registration contracts are frozen inputs to R2.8 (`R2_7_REGISTRATION_DRAFT.md`).
11. **R2.8 is COMPLETE** — Gates 0–6 all CLOSED / PASS. The GDPR Evidence Graph reference (HTML + public `claims.json`) is **live on main since 2026-08-23**; claims `published` / `active`; provenance `release_sha=b392ba5`, `merge_sha=f97a51e`, `live_on_main_since=2026-08-23`; index control = Cloudflare exact-path `X-Robots-Tag: noindex` (verified live on a `200`); **RGS v2 = 97.5 / 100**. Governed by DEC-054 (frozen sequence), DEC-055 (Gate 0), DEC-056 (closeout). `routes.json` `indexable:false` is governance only. Expansion stays gated until all Wave 1 routes ≥ 90 (DEC-047).

---

## Phase checklist

| Phase | Name | State |
|---|---|---|
| R2.0 | Source & Claim Discovery | **CLOSED / PASS** |
| R2.1 | Claim Map & Falsification | **CLOSED / PASS** |
| R2.2 | Identity Fixation + Source Pinning + Draft Serialization | **CLOSED / PASS** |
| R2.3 | Human Literal Verification | **CLOSED / PASS** — 31/31 |
| R2.4 | Canonical Graph + Route Integration Preparation | **CLOSED / PASS** — merge `6285677…` (PR #36) |
| R2.5 | Branch-only Page Transformation | **CLOSED / PASS** — merge `a6b9ed0…` (PR #38) |
| R2.6 | Decision utility layer | **CLOSED / PASS** — merge `8168415…` (PR #39) |
| R2.7 | Citation + machine registration prep | **CLOSED / PASS** — merge `8ec08e0…` (PR #40) |
| R2.8 | GDPR Publish Gate → RGS re-score ≥90 | **CLOSED / PASS** — live 2026-08-23; RGS v2 97.5 (Gates 0–6) |

---

## Workbench files

| File | Role |
|---|---|
| `claims.minted.draft.json` | Verified mint + provenance (31/31) |
| `claims.canonical.staging.json` | Staging truth layer (not public) |
| `claims.prepublication.candidate.json` | **Gate 1** pre-publication build (`verified→publishable`; not public) |
| `decision-utility.staging.json` | Nine Decision Objects (derived) |
| `R2_7_CITATION_MACHINE_PREP.md` | R2.7 scope (closed) |
| `R2_7_REGISTRATION_DRAFT.md` | Non-executing contracts for R2.8 |
| `R2_8_PUBLISH_GATE.md` | **R2.8** gate sequence + Gate 0 freeze |
| `R2_8_GATE0_HOSTING_INDEX_CONTROL.md` | **Gate 0** serving stack + index-control investigation (CLOSED / PASS) |
| `R2_8_GATE1_CANONICAL_BUILD.md` | **Gate 1** pre-publication canonical build + transformation checks |
| `R2_8_GATE2_RELEASE_HTML.md` | **Gate 2** release HTML candidate + §E.2 sanitization checklist |
| `R2_8_GATE3_MACHINE_REGISTRATION.md` | **Gate 3** machine + registration package + planned diffs + consistency tests |
| `R2_8_GATE4_PREMERGE_AUDIT.md` | **Gate 4** pre-merge Publish Gate audit (25/25 PASS) + atomic Gate-5 mutation list |
| `R2_8_GATE5_PUBLICATION.md` | **Gate 5** publication release (Phase A cutover; Phase B provenance post-merge) |
| `R2_8_GATE6_LIVE_VERIFICATION.md` | **Gate 6** live verification + RGS v2 re-score (97.5 / 100) |
| `page-candidate/` | Non-live HTML candidate (R2.5/R2.6 workbench + verification record) |
| `release-candidate/` | **Gate 2/3** release bundle candidate — `index.html` + `claims.json` (branch-only; not live) |
| `README.md` | This status note |

---

## Current truth-status

**Verified (batch-1):** `EP-CLM-000015` … `EP-CLM-000045` (**31/31**), still `workflow_state=verified` (pre-publication).

**Qualification edges:** 24→25 · 32→33 · 35→36 · 37→38  

**Chapter V related hierarchy:** 041 ← 042 ← 043 ← 044

**Decision Utility:** `EP-DU-GDPR-001`…`009` — derived; not claims.

**Published / live since 2026-08-23:** `_meta.published=true`; live HTML + public `claims.json` (`published` / `active`) + `routes.json` alternate + `llms.txt` line all live on main; index control via Cloudflare exact-path `X-Robots-Tag: noindex` (verified on a live `200`). **Gates 0–6 CLOSED / PASS; RGS v2 = 97.5 / 100.**

---

## Success condition (end of R2)

- AI Act remains ≥90
- GDPR RGS score ≥90 for real six-layer reasons (after Gate 6)
- Data Act / CRA / EERS / Protocol remain later
- **No expansion opened** before that re-score

---

*EuraPlan.com — Sprint R2 workbench. Not a published website page.*
