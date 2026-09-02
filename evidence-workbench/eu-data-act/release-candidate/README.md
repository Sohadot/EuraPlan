# EU Data Act — production release-candidate (R3.4 → R3.5 staging)

**Status:** Staging artifacts present — machine graph built; page transform in progress.
**Live route:** `/regulation/eu-data-act/` must **not** be overwritten by this folder until the **R3.8 Publish Gate** publication sequence, which is a separate, explicitly-authorised production PR.

## Contents

| File | Role |
|---|---|
| `claims.json` | R3.4 canonical claim-graph machine package candidate for the public path `/regulation/eu-data-act/claims.json` — assembled from the R3.3 verification (87/87 `VERIFIED_LITERAL`). `workflow_state=publishable`, `validity_state=null`, `published=false`. **Not the live file.** |
| `index.html` | R3.5 release-sanitized Evidence Graph page candidate (transform of the current thin `/regulation/eu-data-act/` page) — *pending in this staging pass.* |
| `build_claims.py` | Deterministic generator for `claims.json` (reads `../R3_2_IDENTITY_REGISTER.md`; claim prose is the verified-literal proposition). Re-runnable; byte-stable. |
| `README.md` | This note. |

## What this is

The staged, review-ready production candidate for the EU Data Act reference route (`EP-REG-003`). It carries the full **87-claim canonical graph** (`EP-CLM-000046..000132`) with `qualified_by` / `related_claims` edges, `co_render_blocking_pairs`, EERS-dimension mapping, source registry (`EP-SRC-000006` read with `EP-SRC-000007`), and per-claim `last_verified_at` — all at `published:false`. It is the machine spine the public page will render from.

## Guardrails — still CLOSED here (deferred to the R3.8 Publish Gate)

1. **No live-path write.** Do **not** copy any file over `regulation/eu-data-act/index.html`, and do **not** create `regulation/eu-data-act/claims.json`, before the Publish Gate.
2. **No registration.** No `routes.json` / `sitemap.xml` / `llms.txt` / `robots.txt` mutation here (`routes.json` `indexable:false` remains governance metadata only; `claims.json` is never listed in the sitemap).
3. **State stays staged.** Visible/graph `workflow_state` is `publishable` and `validity_state` is `null` — they become `published` / `active` (and `published:true`) only at the Publish Gate.
4. **No invented provenance.** `release_sha` / `merge_sha` / `live_on_main_since` are set only at the Publish Gate release sequence.
5. **Index control at cutover.** `robots` stays `noindex` until the live cutover; exact-path `X-Robots-Tag: noindex` on `/regulation/eu-data-act/claims.json` per DEC-055.

## Excluded by design

- **I1 (Art. 33)** and **I2 (Art. 35)** interoperability essential requirements carry no `EP-CLM` identity (source-constrained / standards-pending) and are **not** in the graph.
- The corrigendum (`EP-SRC-000007`) affects **Article 48 only** and has no effect on any claim; recorded per-claim as `read_with`.

See `../R3_3_VERBATIM_VERIFICATION.md` (87/87), `../R3_2_IDENTITY_REGISTER.md`, `../../gdpr/release-candidate/` (the proven GDPR staging precedent), `CLAIM_POLICY.md`, and `DISCLOSURE_BOUNDARY.md`.
