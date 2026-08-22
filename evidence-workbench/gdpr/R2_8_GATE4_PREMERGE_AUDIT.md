# R2.8 Gate 4 — Pre-merge Publish Gate (audit)

**Status:** AUDIT COMPLETE — ALL PASS (25/25) / release PR AUTHORIZED (pending owner review)
**Date:** 2026-08-22
**Scope:** Gate 4 only — **audit, build nothing**; no `published`, no `active`, no live files
**Authorized by:** Gate 3 CLOSED / PASS under the DEC-054 frozen sequence (DEC-055 governs only the Gate 0 index-control decision)
**Audited package:** `release-candidate/index.html` (Gate 2) + `release-candidate/claims.json` (Gate 3), against `claims.prepublication.candidate.json` (Gate 1) and the live registry files on `main`
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE1_CANONICAL_BUILD.md`; `R2_8_GATE2_RELEASE_HTML.md`; `R2_8_GATE3_MACHINE_REGISTRATION.md`

---

## 1. What this gate does

A strict pre-release audit of the complete Gate 1–3 package. Gate 4 **produces no new content** and **mutates no live surface**. It confirms the package is internally consistent and leak-free, that all live-mutation actions remain un-executed, and — only on a full pass — authorizes the future release PR (Gate 5).

---

## 2. Audit results (25/25 PASS)

### Graph integrity / parity
- [x] 31 claims; IDs `EP-CLM-000015..000045`, ascending, unique
- [x] claims byte-identical to the Gate 1 build
- [x] all `workflow_state = publishable`; all `validity_state = null`; `_meta.published = false`
- [x] `confidence = Verified` and `last_verified_at = 2026-08-20` on all 31

### HTML ↔ JSON proposition parity
- [x] claim IDs in `claims.json` == claim anchors in the release HTML (31, identical set)
- [x] every claim proposition text appears **verbatim** in the release HTML (entity/whitespace-normalized)

### Qualification visibility (co-render)
- [x] 4 `qualified_by` edges in JSON: `024→025`, `032→033`, `035→036`, `037→038` (default → qualifier)
- [x] 4 `Co-render required` blocks in the release HTML; both pair anchors present for each

### Source resolution
- [x] `source_registry` = EP-SRC-000004 (authentic OJ act) + EP-SRC-000005 (consolidated reading aid)
- [x] every claim `source_id` resolves in the registry; every claim has ≥1 source

### Zero workbench leakage
- [x] release HTML: **zero** workbench / staging / phase / batch / candidate leakage
- [x] claims array (the shipped truth): **zero** leakage
- [x] candidate `claims.json` `_meta` still carries workbench/candidate language — **expected**; this is transformed at Gate 5 per `R2_8_GATE3_MACHINE_REGISTRATION.md` §2.1 (never raw-copied)

### Registration diffs drafted, NOT applied
- [x] live `routes.json` EP-REG-002 has **no** `alternate_representations` yet (Gate 5 applies it)
- [x] live `routes.json` EP-REG-001 (AI Act) alternate exists — pattern source
- [x] live `llms.txt` has **no** `/regulation/gdpr/claims.json` line yet (Gate 5 applies it)
- [x] live `llms.txt` AI Act claims line exists — pattern source

### Lifecycle / provenance / no live surface
- [x] **no** live `regulation/gdpr/claims.json` exists (reserved for Gate 5)
- [x] candidate `_meta` has **no** `release_sha` / `merge_sha` / `live_on_main_since`
- [x] `governed_by` carries DEC-054 & DEC-055
- [x] candidate `claims.json` parses as valid JSON

### secret-scan
- [x] `secret-scan` SUCCESS on every merged head of Gates 1–3 (PR #43, #44, #45) and on this audit branch head

**Result: ALL PASS (25/25).**

---

## 3. Planned lifecycle transitions (recorded; executed only at Gate 5)

| Field | Now (candidate) | Gate 5 |
|---|---|---|
| `workflow_state` (all 31) | `publishable` | `published` |
| `validity_state` (all 31) | `null` | `active` |
| `_meta.published` | `false` | `true` |

## 4. Provenance plan (recorded; executed only at Gate 5/6)

- `release_sha` — set on the Gate 5 release commit (real git object).
- `merge_sha` — **post-merge** provenance finalization (real merge commit on `main`), after merge and **before Gate 6**; never pre-merge.
- `live_on_main_since` — the actual publication/merge date.

---

## 5. Atomic Gate-5 mutation list (single release sequence — NOT done here)

All of the following happen together in the Gate 5 release PR; none may occur before Gate 4 passes:

1. Write `regulation/gdpr/index.html` — the Gate 2 release HTML, with the deferred live switches applied: `robots → index, follow`; visible workflow labels `publishable → published`; Article `dateModified → cutover date`.
2. Write `regulation/gdpr/claims.json` — **transform** of the Gate 3 candidate per §2.1: `publishable → published`, `null → active`, `published → true`; `_meta` rewritten to published/public wording with all Gate/workbench/candidate language and `evidence-workbench/…` paths removed; claims array / `source_registry` / graph metadata unchanged.
3. `routes.json` — add the EP-REG-002 `alternate_representations` entry.
4. `llms.txt` — add the `/regulation/gdpr/claims.json` canonical-claim-graph line.
5. `sitemap.xml` — refresh `/regulation/gdpr/` `lastmod` only; **never** list `claims.json`.
6. `robots.txt` — **no change** (index control is Gate 0 Option A at the CDN).
7. `release_sha` set on the release commit; `merge_sha` + `live_on_main_since` finalized **post-merge before Gate 6**.

---

## 6. Gate 4 exit / authorization

- Audit is **ALL PASS (25/25)**. The package is internally consistent, leak-free, and fully gated.
- **The Gate 5 release PR is AUTHORIZED.** This authorization is a governance record only — Gate 4 itself creates no release PR and performs no live mutation.
- **Until Gate 5:** no `published`, no `active`, no live files, no applied registration diffs, no provenance SHAs.

**This PR (Gate 4) is a workbench/audit PR, not the release PR.** The `regulation/gdpr/` cutover happens only in the Gate 5 release PR, which itself is what "Gate 4 — pre-merge Publish Gate" gates.

---

*Workbench Gate 4 audit. Not a publication event.*
