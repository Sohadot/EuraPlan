# GDPR release HTML candidate (R2.8 Gate 2)

**Status:** Release-sanitized candidate present — `index.html`
**Live route:** `/regulation/gdpr/` must **not** be overwritten by this folder until the R2.8 **Gate 5** publication sequence.

## Contents

| File | Role |
|---|---|
| `index.html` | Gate 2 release-sanitized Evidence Graph page (transform of `../page-candidate/index.html`) |
| `README.md` | This note |

## What this is

The §E.2 release-sanitized version of the workbench page candidate: live `<title>`/description, canonical, Open Graph + Twitter, Article + Breadcrumb JSON-LD, published telemetry, and header/footer `Acquire` nav — with all R2.6 workbench chrome removed. §E.1 substance is preserved: 31 anchors `#ep-clm-000015…000045`, four co-render pairs, Chapter V hierarchy, nine Decision Utility objects.

## Still deferred to Gate 5 (do not apply here)

1. `robots` stays `noindex, nofollow` — flipped to `index, follow` only at the live cutover.
2. Visible workflow labels are `publishable` — become `published` only at Gate 5.
3. Article `dateModified` is a build-date placeholder (`2026-08-22`) — set to the real cutover date at Gate 5.
4. **Do not** copy this file over `regulation/gdpr/index.html`, and **do not** create `regulation/gdpr/claims.json`, before the Gate 3–5 sequence.

See `../R2_8_GATE2_RELEASE_HTML.md`, `../R2_7_REGISTRATION_DRAFT.md` §E, `../R2_8_PUBLISH_GATE.md`, and DEC-055.
