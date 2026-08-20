# Sprint R2 — GDPR Evidence Graph-grade Upgrade
**Status:** Open — R2.0 Source & Claim Discovery (no publish)
**Opened:** 2026-08-20
**Branch:** `sprint-r2-gdpr-evidence-graph`
**Canonical target (later):** `/regulation/gdpr/` + `/regulation/gdpr/claims.json` (EP-REG-002)
**Governed by:** REFERENCE_GRADE_ROUTE_STANDARD.md v2; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DEC-047; DISCLOSURE_BOUNDARY.md

---

## Hard rules for this sprint

1. **No HTML rewrite** of `/regulation/gdpr/` until R2.4 after verified claims exist.
2. **No** `/regulation/gdpr/claims.json` until after human verification + Publish Gate path (R2.3+).
3. **No** `EP-CLM-*` mint until a proposition survives literal reading + falsification (R2.1→R2.2). Next free ID after AI Act batch: **`EP-CLM-000015`**.
4. **No** parallel Data Act / country / expansion work.
5. Claim count follows **material truth** for non-EU entry planning — not a 14-claim template.
6. Global opaque ID sequence only — never `GDPR-CLM-*`.
7. Defaults that have exceptions (`unless` / `except` / thresholds) must carry `qualified_by` candidates — never publish a default alone.

---

## Phase checklist

| Phase | Name | State |
|---|---|---|
| R2.0 | Source & Claim Discovery | **IN PROGRESS** — see this folder |
| R2.1 | Claim Map & Falsification | Not started |
| R2.2 | Human Verification (`draft` → `pending_verification` → `verified`) | Not started |
| R2.3 | Canonical graph + routes alternate | Not started |
| R2.4 | Page transformation | Not started |
| R2.5 | Decision utility layer | Not started (draft hints in claim map) |
| R2.6 | Citation + machine + llms/routes/sitemap | Not started |
| R2.7 | GDPR Publish Gate → RGS re-score ≥90 | Not started |

---

## Workbench files (Class 2 public working evidence)

| File | Role |
|---|---|
| `SOURCE_REGISTRY.draft.json` | Candidate Tier-1/Tier-2 sources — **no** `EP-SRC-*` reserved yet |
| `CLAIM_CANDIDATES.draft.md` | Candidate propositions with provision → exception map — **no** `EP-CLM-*` |
| `README.md` | This status note |

---

## Success condition (end of R2)

- AI Act remains ≥90 (untouched except real freshness events)
- GDPR RGS score ≥90 for real six-layer reasons
- Data Act / CRA / EERS / Protocol still later
- **No expansion opened**

---

*EuraPlan.com — Sprint R2 workbench. Not a published website page.*
