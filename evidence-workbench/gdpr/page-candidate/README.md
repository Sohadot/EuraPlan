# GDPR page candidate (R2.5 structure + R2.6 Decision Utility)

**Status:** HTML candidate present — `index.html`  
**Live route:** `/regulation/gdpr/` must **not** be overwritten by this folder until R2.8 Publish Gate.

## Contents

| File | Role |
|---|---|
| `index.html` | Workbench Evidence Graph page candidate + nine Decision Objects |
| `README.md` | This note |

## Rules

1. Do not copy this candidate over `regulation/gdpr/index.html` on `main` during R2.6.
2. Do not create `regulation/gdpr/claims.json`.
3. Candidate carries `noindex,nofollow` and an explicit NOT LIVE banner.
4. Co-render all `qualified_by` pairs; present Chapter V as hierarchy, not interchangeable options.
5. Proposition text is driven from `../claims.canonical.staging.json` (verified 2026-08-20).
6. Decision Utility is driven from `../decision-utility.staging.json` (derived layer; seeds are not verified facts).
7. No new `EP-CLM-*` for utility alone. R2.7 / R2.8 remain blocked.

See `../R2_5_PAGE_CANDIDATE.md`, `../R2_6_DECISION_UTILITY.md`, DEC-051, and DEC-052.
