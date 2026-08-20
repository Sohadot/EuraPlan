# GDPR page candidate (R2.5)

**Status:** HTML candidate present — `index.html`  
**Live route:** `/regulation/gdpr/` must **not** be overwritten by this folder until R2.8 Publish Gate.

## Contents

| File | Role |
|---|---|
| `index.html` | Branch-only Evidence Graph page candidate (31 claims, co-render pairs, Chapter V hierarchy) |
| `README.md` | This note |

## Rules

1. Do not copy this candidate over `regulation/gdpr/index.html` on `main` during R2.5.
2. Do not create `regulation/gdpr/claims.json`.
3. Candidate carries `noindex,nofollow` and an explicit NOT LIVE banner.
4. Co-render all `qualified_by` pairs; present Chapter V as hierarchy, not interchangeable options.
5. Proposition text is driven from `../claims.canonical.staging.json` (verified 2026-08-20).

See `../R2_5_PAGE_CANDIDATE.md` and DEC-051.
