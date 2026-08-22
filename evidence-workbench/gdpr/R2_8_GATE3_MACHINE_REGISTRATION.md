# R2.8 Gate 3 — Machine + Registration Package

**Status:** PREPARED (branch-only) / AWAITING REVIEW
**Date:** 2026-08-22
**Scope:** Gate 3 only — **prepare, do not publish**; no Gate 4–6 execution; no live mutation
**Authorized by:** Gate 2 CLOSED / PASS under the DEC-054 frozen sequence (DEC-055 governs only the Gate 0 index-control decision)
**Governed by:** `R2_7_REGISTRATION_DRAFT.md` §A–D; `ROUTE_GOVERNANCE.md`
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE1_CANONICAL_BUILD.md`; `R2_8_GATE2_RELEASE_HTML.md`

---

## 1. What this gate does

Assemble the machine + registration **package** so Gate 4 can verify it and Gate 5 can publish it in one atomic sequence. Everything here is a **candidate / planned diff** — no live surface is created or edited.

| Deliverable | Form at Gate 3 | Applied at |
|---|---|---|
| Public `claims.json` | Candidate `evidence-workbench/gdpr/release-candidate/claims.json` (assembled from the Gate 1 build) | Gate 5 → `regulation/gdpr/claims.json` |
| `routes.json` EP-REG-002 `alternate_representations` | **Planned diff** (below) — not applied to live `routes.json` | Gate 5 |
| `llms.txt` claim-graph line | **Planned wording** (below) — not applied to live `llms.txt` | Gate 5 |
| Sitemap / robots | **Rule recorded** (below) — no edit | Gate 5 (HTML `lastmod` only) |

---

## 2. Public `claims.json` candidate

- **File:** `evidence-workbench/gdpr/release-candidate/claims.json`
- **Source:** the Gate 1 build `claims.prepublication.candidate.json` — the 31-claim array is **byte-identical**.
- **Lifecycle:** `workflow_state = publishable` (all 31), `validity_state = null`, `_meta.published = false`.
- **`_meta`:** machine-package framing for the public path; `governed_by` retains R2.8 DECs (DEC-054, DEC-055); `source_registry` (EP-SRC-000004, EP-SRC-000005) retained.
- **No provenance SHAs:** `release_sha` / `merge_sha` / `live_on_main_since` are absent. Per the frozen contract (`R2_8_PUBLISH_GATE.md` Gate 5): `release_sha` is set on the Gate 5 release commit; **`merge_sha` is post-merge provenance finalization** — the real merge commit on `main`, added after merge and before the Gate 6 closeout, **never pre-merge**; `live_on_main_since` is set to the actual publication/merge event. None are invented here.
- **Not the live file:** no file under `regulation/gdpr/**` is created; the live `regulation/gdpr/claims.json` is written only in the Gate 5 release sequence.

### 2.1 Gate 5 public `_meta` transformation contract (no raw-copy publication)

At Gate 5 the candidate becomes the live `regulation/gdpr/claims.json` by **transformation, never a byte-for-byte copy** (per `R2_7_REGISTRATION_DRAFT.md` §A.1):

| Element | Gate 5 rule |
|---|---|
| 31-claim array, `source_registry`, graph-integrity metadata (`co_render_blocking_pairs`, `chapter_v_related_hierarchy`, `id_range`, `claim_count`, `route_id`, `schema_version`) | **Unchanged** |
| `workflow_state` (all 31) | `publishable → published` |
| `validity_state` (all 31) | `null → active` |
| `_meta.published` | `false → true` |
| `batch` / `status` / `location_note` / `notes` | Rewrite to AI Act–parallel **published / active — live on main** wording; **remove every Gate / workbench / candidate / "NOT live" phrase** and all `evidence-workbench/…` path references |
| `governed_by` | Retain (with the R2.8 DECs) |
| Provenance | Add `release_sha` (release commit), then `merge_sha` + `live_on_main_since` **post-merge** |

**Hard rule:** a straight copy of this candidate to the live path (with Gate/workbench/candidate `_meta` language intact) is a **Gate 5 hard fail**.

---

## 3. Planned `routes.json` diff (EP-REG-002 — NOT applied here)

EP-REG-002 currently has **no** `alternate_representations`. The Gate 5 addition (parallel to EP-REG-001 / the AI Act, per §B):

```json
"alternate_representations": [
  {
    "path": "/regulation/gdpr/claims.json",
    "media_type": "application/json",
    "role": "canonical_claim_graph",
    "canonical_parent": "/regulation/gdpr/",
    "indexable": false,
    "sitemap": false
  }
]
```

`indexable: false` is **governance metadata** in the route registry — not an HTTP header, not a robots directive, not crawler enforcement. Crawler-level index control is handled by the Gate 0 decision (§5).

---

## 4. Planned `llms.txt` line (NOT applied here)

To be added under the canonical-claim-graph section, directly after the AI Act line (§C):

```text
- [GDPR — canonical claim graph](https://euraplan.com/regulation/gdpr/claims.json): the machine-readable canonical claim graph for the GDPR reference page — governed Evidence Objects with opaque stable identifiers (`EP-CLM-*`), source/provision locators, qualification links, and verification dates. It mirrors the visible Verified Claim Register on `/regulation/gdpr/`. This is a static reference file, not an API, and implies no external endorsement.
```

---

## 5. Sitemap / robots / crawl decision (recorded — NOT applied here)

| Surface | Gate 5 rule |
|---|---|
| `claims.json` in sitemap | **Never listed** |
| HTML `/regulation/gdpr/` in sitemap | Already listed; refresh `lastmod` only on the live cutover |
| `routes.json` `indexable:false` | Governance intent only — does not stop crawlers |
| `robots.txt` | **No change** — stays `Allow: /regulation/`; a path `Disallow` is **not** used |
| Index control | **Gate 0 Option A** (DEC-055): Cloudflare exact-path `X-Robots-Tag: noindex` on `/regulation/gdpr/claims.json`, already configured and verified live 2026-08-22 (Gate 6 re-tests on a live `200`) |

No `robots.txt` / sitemap edit is required at Gate 3 or Gate 5 for index control: Option A is a CDN-layer control (out of git).

---

## 6. Consistency tests (candidate `claims.json` ↔ Gate 2 release HTML) — all PASS

- [x] `claims.json` valid JSON; 31 claims
- [x] all 31 `workflow_state = publishable`; `validity_state = null`; `_meta.published = false`
- [x] no invented `release_sha` / `merge_sha`
- [x] claim IDs in `claims.json` == claim anchors in the release HTML (31, identical set)
- [x] every claim `source_id` resolves in `_meta.source_registry`
- [x] `source_registry` = EP-SRC-000004 (authentic OJ act) + EP-SRC-000005 (consolidated reading aid)
- [x] four co-render pairs (024↔025, 032↔033, 035↔036, 037↔038) anchored in HTML and present in JSON
- [x] Chapter V hierarchy 041–044 present in HTML and JSON
- [x] `governed_by` carries DEC-054 and DEC-055

---

## 7. Gate 3 exit criteria

Gate 3 is satisfied when:

1. A public `claims.json` **candidate** exists (assembled from the Gate 1 build; not under `regulation/gdpr/`). ✅
2. The `routes.json` alternate entry and `llms.txt` line are **drafted verbatim**, not applied. ✅
3. Sitemap/robots rule and the Gate 0 index-control decision are recorded. ✅
4. HTML ↔ JSON consistency tests pass. ✅
5. No live surface created or edited. ✅

**Exit:** on review PASS, Gate 3 is CLOSED / PASS. **Gate 4** (pre-merge Publish Gate checks) may then begin — **not** started here.

---

## 8. Reserved for Gate 5 (publication) — NOT done here

- Write `regulation/gdpr/claims.json` (transform of this candidate per §2.1) with `publishable → published`, `null → active`, `published → true`
- Apply the `routes.json` alternate entry and the `llms.txt` line to the live files
- Refresh HTML `lastmod` in the sitemap
- Set `release_sha` on the Gate 5 release commit (real git object)
- Finalize `merge_sha` **post-merge** (real merge commit on `main`) and set `live_on_main_since` to the actual publication date — after merge, before the Gate 6 closeout; **never pre-merge**
- Live HTML cutover to `regulation/gdpr/index.html`

---

*Workbench Gate 3 package. Not a publication event.*
