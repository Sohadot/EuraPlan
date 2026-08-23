# R2.8 Gate 5 — Publication (release sequence)

**Status:** PHASE A LIVE (PR #47 merged `f97a51e`, publication 2026-08-23) + PHASE B PROVENANCE FINALIZED. Gate 5 CLOSED / PASS. Gate 6 next.
**Date:** 2026-08-23
**Scope:** Gate 5 Phase A — the release cutover for EP-REG-002 (now live on main); Phase B — post-merge provenance (now finalized). Gate 6 (live verification + RGS) remains unexecuted.
**Authorized by:** Gate 4 CLOSED / PASS (audit 25/25, PR #46) under the DEC-054 frozen sequence; DEC-055 governs the Gate 0 index-control decision
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE4_PREMERGE_AUDIT.md`; `R2_8_GATE3_MACHINE_REGISTRATION.md` §2.1

---

## 1. What this PR does (Phase A — pre-merge)

This is the **release PR**: it **stages** the GDPR Evidence Graph reference in the release-state tree. Nothing here is live yet — **merging it (owner action) is the publication event** that makes it effective on the live site. Phase A does **not** write provenance SHAs (those do not exist until the commits do — Phase B).

| # | Release-state change (effective on merge) | From | Transform |
|---|---|---|---|
| 1 | `regulation/gdpr/index.html` | `release-candidate/index.html` (Gate 2) | deferred switches applied: `robots → index, follow`; visible workflow labels `publishable → published` (31 claims + hero + sources + telemetry); Article `dateModified = 2026-08-23` (cutover). Substance unchanged: 31 anchors, 4 co-render pairs, Chapter V, 9 Decision Utility objects. |
| 2 | `regulation/gdpr/claims.json` (new) | `release-candidate/claims.json` (Gate 3) | **transform** per §2.1: `workflow_state publishable → published`; `validity_state null → active`; `_meta.published → true`; `_meta` rewritten to published/public wording with all Gate/workbench/candidate language and `evidence-workbench/…` paths removed. Claims array text/IDs/sources/`qualified_by` and `source_registry` unchanged. **No provenance SHAs.** |
| 3 | `routes.json` | — | EP-REG-002 `alternate_representations` entry added (parallel to EP-REG-001), `indexable:false` / `sitemap:false`. |
| 4 | `llms.txt` | — | GDPR canonical-claim-graph line added after the AI Act line. |
| 5 | `sitemap.xml` | — | `/regulation/gdpr/` `lastmod → 2026-08-23`; `claims.json` **not** listed. |
| 6 | `robots.txt` | — | **No change** (index control is Gate 0 Option A at the CDN). |

---

## 2. Phase-A verification — 20 / 20 PASS (reproducible)

Each row is an independent assertion, numbered so an auditor can reproduce it one-for-one against the release-state tree.

**Published `claims.json`**
- [x] **G5A-01** — valid JSON; 31 claims
- [x] **G5A-02** — all `workflow_state = published`
- [x] **G5A-03** — all `validity_state = active`
- [x] **G5A-04** — `_meta.published = true`
- [x] **G5A-05** — `confidence = Verified` and `last_verified_at = 2026-08-20` unchanged on all 31
- [x] **G5A-06** — claims array text/IDs/sources/`qualified_by` identical to the Gate 3 candidate (only the two lifecycle fields changed)
- [x] **G5A-07** — published `_meta` carries **no** Gate/workbench/candidate language and no `evidence-workbench/…` paths
- [x] **G5A-08** — published `_meta` has **no** `release_sha` / `merge_sha` / `live_on_main_since`
- [x] **G5A-09** — `governed_by` carries DEC-054 & DEC-055

**Published `index.html`**
- [x] **G5A-10** — `robots = index, follow`
- [x] **G5A-11** — zero `publishable` labels remain (all `published`)
- [x] **G5A-12** — 31 claim anchors present
- [x] **G5A-13** — 9 Decision Utility objects present
- [x] **G5A-14** — 4 co-render blocks present
- [x] **G5A-15** — Article `dateModified = 2026-08-23`
- [x] **G5A-16** — claim IDs in `claims.json` == claim anchors in the HTML (31, identical set)
- [x] **G5A-17** — every claim proposition text present verbatim in the HTML

**Registration surfaces**
- [x] **G5A-18** — `routes.json` valid JSON; EP-REG-002 `alternate_representations` present
- [x] **G5A-19** — `llms.txt` GDPR claims line present, after the AI Act line
- [x] **G5A-20** — `sitemap.xml` well-formed; `/regulation/gdpr/` `lastmod = 2026-08-23`; `claims.json` **not** listed; `robots.txt` unchanged

**Result: 20 / 20 PASS (G5A-01 … G5A-20).** secret-scan is a separate external check (green on this head).

---

## 2a. Merge-time condition — publication date

`index.html` Article `dateModified` and `sitemap.xml` `lastmod` are set to **2026-08-23**, which assumes this PR is merged on 2026-08-23. **If the merge slips to a later date, update both to the actual merge/publication date before merging** — the publication date must reflect the real event, not the PR-preparation date.

---

## 3. Phase B — post-merge provenance finalization (DONE)

Filled in the published `_meta` from real git objects after PR #47 merged:

- `release_sha` = `b392ba50015e98b273a458320c5bd3201732a590` (release-state commit — PR #47 head)
- `merge_sha` = `f97a51ed438e1b00c689ffe22b682a05d11f9704` (merge commit on `main`)
- `live_on_main_since` = `2026-08-23`

Both SHAs are real, pre-existing objects (no self-reference). The pre-merge `merge_commit_sha` GitHub preview was **not** used. `_meta.batch`/`status` also updated from release-state to **published / active — live on main**.

---

## 4. Reserved for Gate 6 (post-merge live verification)

- Verify live HTML, anchors, JSON, routes, llms, sitemap, and crawler/index behavior against the Gate 0 decision.
- Re-test the Cloudflare `X-Robots-Tag: noindex` on a **live `200`** response for `/regulation/gdpr/claims.json` (Gate 0 verified it against a pre-publication `404`).
- RGS v2 re-score, target ≥ 90.

---

*Gate 5 release PR. Merging this PR is the publication event.*
