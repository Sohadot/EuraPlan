# R2.8 Gate 5 — Publication (release sequence)

**Status:** PHASE A COMPLETE (this release PR) / PENDING owner review + merge; PHASE B (provenance) reserved
**Date:** 2026-08-22
**Scope:** Gate 5 Phase A — the live cutover for EP-REG-002. Phase B (provenance) is post-merge; Gate 6 remains unexecuted.
**Authorized by:** Gate 4 CLOSED / PASS (audit 25/25, PR #46) under the DEC-054 frozen sequence; DEC-055 governs the Gate 0 index-control decision
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE4_PREMERGE_AUDIT.md`; `R2_8_GATE3_MACHINE_REGISTRATION.md` §2.1

---

## 1. What this PR does (Phase A — pre-merge)

This is the **release PR**: merging it (owner action) publishes the GDPR Evidence Graph reference to the live site. Phase A applies the live cutover; it does **not** write provenance SHAs (those do not exist until the commits do — Phase B).

| # | Live change | From | Transform |
|---|---|---|---|
| 1 | `regulation/gdpr/index.html` | `release-candidate/index.html` (Gate 2) | deferred switches applied: `robots → index, follow`; visible workflow labels `publishable → published` (31 claims + hero + sources + telemetry); Article `dateModified = 2026-08-22` (cutover). Substance unchanged: 31 anchors, 4 co-render pairs, Chapter V, 9 Decision Utility objects. |
| 2 | `regulation/gdpr/claims.json` (new) | `release-candidate/claims.json` (Gate 3) | **transform** per §2.1: `workflow_state publishable → published`; `validity_state null → active`; `_meta.published → true`; `_meta` rewritten to published/public wording with all Gate/workbench/candidate language and `evidence-workbench/…` paths removed. Claims array text/IDs/sources/`qualified_by` and `source_registry` unchanged. **No provenance SHAs.** |
| 3 | `routes.json` | — | EP-REG-002 `alternate_representations` entry added (parallel to EP-REG-001), `indexable:false` / `sitemap:false`. |
| 4 | `llms.txt` | — | GDPR canonical-claim-graph line added after the AI Act line. |
| 5 | `sitemap.xml` | — | `/regulation/gdpr/` `lastmod → 2026-08-22`; `claims.json` **not** listed. |
| 6 | `robots.txt` | — | **No change** (index control is Gate 0 Option A at the CDN). |

---

## 2. Phase-A verification (all PASS)

- [x] `regulation/gdpr/claims.json`: valid JSON; 31 claims; all `workflow_state = published`; all `validity_state = active`; `_meta.published = true`
- [x] claims array text/IDs/sources/`qualified_by` identical to the Gate 3 candidate (only the two lifecycle fields changed)
- [x] `confidence = Verified` and `last_verified_at = 2026-08-20` unchanged on all 31
- [x] published `_meta` carries **no** Gate/workbench/candidate language, no `evidence-workbench/…` paths, no `release_sha`/`merge_sha`/`live_on_main_since`
- [x] `regulation/gdpr/index.html`: `robots = index, follow`; zero `publishable` labels remain (all `published`); 31 anchors, 9 Decision Utility objects, 4 co-render blocks intact; `dateModified = 2026-08-22`
- [x] claim IDs in `claims.json` == claim anchors in the live HTML (31, identical set)
- [x] `routes.json` valid JSON; EP-REG-002 `alternate_representations` present; parses
- [x] `llms.txt` GDPR claims line present, after the AI Act line
- [x] `sitemap.xml` `/regulation/gdpr/` `lastmod = 2026-08-22`; `claims.json` absent from sitemap
- [x] `robots.txt` unchanged

---

## 3. Phase B — post-merge provenance finalization (NOT done here; before Gate 6)

A commit cannot contain its own SHA, so after this release PR merges, a follow-up provenance PR/commit merged to `main` fills the published `_meta`:

- `release_sha` = the real release-state commit SHA
- `merge_sha` = the real merge commit SHA (both from real git objects)
- `live_on_main_since` = the actual publication date

Never pre-merge; never self-referencing. (AI Act precedent: `release_sha` + `merge_sha` recorded this way.)

**Do not** use the pre-merge `merge_commit_sha` shown on this PR as provenance — it is a non-final GitHub preview value.

---

## 4. Reserved for Gate 6 (post-merge live verification)

- Verify live HTML, anchors, JSON, routes, llms, sitemap, and crawler/index behavior against the Gate 0 decision.
- Re-test the Cloudflare `X-Robots-Tag: noindex` on a **live `200`** response for `/regulation/gdpr/claims.json` (Gate 0 verified it against a pre-publication `404`).
- RGS v2 re-score, target ≥ 90.

---

*Gate 5 release PR. Merging this PR is the publication event.*
