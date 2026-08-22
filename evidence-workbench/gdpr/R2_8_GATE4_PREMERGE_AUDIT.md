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

## 2. Audit results — automated checks (25/25 PASS)

Each row is an independent assertion, numbered so an auditor can reproduce it one-for-one. Inputs: `release-candidate/claims.json` (Gate 3), `release-candidate/index.html` (Gate 2), `claims.prepublication.candidate.json` (Gate 1), and the live `routes.json` / `llms.txt` / `regulation/gdpr/` on `main`.

**Graph integrity / parity**
- [x] **G4-01** — 31 claims; IDs `EP-CLM-000015..000045`, ascending, unique
- [x] **G4-02** — claims byte-identical to the Gate 1 build
- [x] **G4-03** — all `workflow_state = publishable`
- [x] **G4-04** — all `validity_state = null`
- [x] **G4-05** — `_meta.published = false`
- [x] **G4-06** — `confidence = Verified` and `last_verified_at = 2026-08-20` on all 31

**HTML ↔ JSON proposition parity**
- [x] **G4-07** — claim IDs in `claims.json` == claim anchors in the release HTML (31, identical set)
- [x] **G4-08** — every claim proposition text appears **verbatim** in the release HTML (entity/whitespace-normalized)

**Qualification visibility (co-render)**
- [x] **G4-09** — 4 `qualified_by` edges in JSON: `024→025`, `032→033`, `035→036`, `037→038` (default → qualifier)
- [x] **G4-10** — 4 `Co-render required` blocks in the release HTML
- [x] **G4-11** — both pair anchors present in the HTML for each of the 4 pairs

**Source resolution**
- [x] **G4-12** — `source_registry` = EP-SRC-000004 (authentic OJ act) + EP-SRC-000005 (consolidated reading aid)
- [x] **G4-13** — every claim `source_id` resolves in the registry
- [x] **G4-14** — every claim has ≥1 source

**Zero workbench leakage**
- [x] **G4-15** — release HTML: **zero** workbench / staging / phase / batch / candidate leakage
- [x] **G4-16** — claims array (the shipped truth): **zero** leakage
- [x] **G4-17** — candidate `claims.json` `_meta` still carries workbench/candidate language — **expected**; transformed at Gate 5 per `R2_8_GATE3_MACHINE_REGISTRATION.md` §2.1 (never raw-copied)

**Registration diffs drafted, NOT applied**
- [x] **G4-18** — live `routes.json` EP-REG-002 has **no** `alternate_representations` yet (Gate 5 applies it)
- [x] **G4-19** — live `routes.json` EP-REG-001 (AI Act) alternate exists — pattern source
- [x] **G4-20** — live `llms.txt` has **no** `/regulation/gdpr/claims.json` line yet (Gate 5 applies it)
- [x] **G4-21** — live `llms.txt` AI Act claims line exists — pattern source

**Lifecycle / provenance / no live surface**
- [x] **G4-22** — **no** live `regulation/gdpr/claims.json` exists (reserved for Gate 5)
- [x] **G4-23** — candidate `_meta` has **no** `release_sha` / `merge_sha` / `live_on_main_since`
- [x] **G4-24** — `governed_by` carries DEC-054 & DEC-055
- [x] **G4-25** — candidate `claims.json` parses as valid JSON

**Automated result: 25 / 25 PASS (G4-01 … G4-25).**

### External check (not part of the 25 static assertions)
- [x] **secret-scan** SUCCESS on every merged head of Gates 1–3 (PR #43, #44, #45) and on this audit branch head.

---

## 3. Planned lifecycle transitions (recorded; executed only at Gate 5)

| Field | Now (candidate) | Gate 5 |
|---|---|---|
| `workflow_state` (all 31) | `publishable` | `published` |
| `validity_state` (all 31) | `null` | `active` |
| `_meta.published` | `false` | `true` |

## 4. Provenance plan (recorded; executed only post-merge)

A commit's SHA is a hash of its own tree, so a commit can **never contain its own SHA**. All three provenance fields are therefore written in a **post-merge finalization** commit, after the SHAs they reference exist — mirroring the AI Act precedent (its live graph records `release_sha = 1cc02e…` and `merge_sha = 3322e6…`, neither of which was self-referenced inside its own commit):

- `release_sha` — the SHA of the Gate-5 **release-state commit**, recorded **after that SHA exists**; it must **never** self-reference inside the same commit.
- `merge_sha` — the SHA of the real **merge commit on `main`**, recorded post-merge.
- `live_on_main_since` — the actual publication/merge date, recorded post-merge.

**Practical rule:** the post-merge finalization commit adds all three together — `release_sha` pointing to the real release-state commit and `merge_sha` to the real merge commit — after merge and **before the Gate 6 closeout**.

---

## 5. Gate-5 mutation list (two phases — NOT done here)

The publication is **not** a single in-PR event: content and registration land in the release PR, but provenance can only be finalized after the commits exist. Two phases:

### Phase A — Gate 5 release PR (pre-merge, one release sequence)

1. Write `regulation/gdpr/index.html` — the Gate 2 release HTML, with the deferred live switches applied: `robots → index, follow`; visible workflow labels `publishable → published`; Article `dateModified → cutover date`.
2. Write `regulation/gdpr/claims.json` — **transform** of the Gate 3 candidate per §2.1: `publishable → published`, `null → active`, `published → true`; `_meta` rewritten to published/public wording with all Gate/workbench/candidate language and `evidence-workbench/…` paths removed; claims array / `source_registry` / graph metadata unchanged. **No provenance SHAs yet** (they don't exist pre-merge).
3. `routes.json` — add the EP-REG-002 `alternate_representations` entry.
4. `llms.txt` — add the `/regulation/gdpr/claims.json` canonical-claim-graph line.
5. `sitemap.xml` — refresh `/regulation/gdpr/` `lastmod` only; **never** list `claims.json`.
6. `robots.txt` — **no change** (index control is Gate 0 Option A at the CDN).

### Phase B — Post-merge provenance finalization (before Gate 6)

7. In a follow-up commit on `main`, fill `_meta`: `release_sha` = the real release-state commit SHA, `merge_sha` = the real merge commit SHA, `live_on_main_since` = the actual publication date. Never pre-merge; never self-referencing (see §4).

---

## 6. Gate 4 exit / authorization

- Automated audit is **25 / 25 PASS (G4-01 … G4-25)**; secret-scan green. The package is internally consistent, leak-free, and fully gated.
- **Gate 5 release-PR authorization is PENDING owner review of this PR (#46).** On owner approval + merge, this becomes **Gate 4 CLOSED / PASS; Gate 5 AUTHORIZED**. The authorization is a governance record only — Gate 4 itself creates no release PR and performs no live mutation.
- **Until Gate 5:** no `published`, no `active`, no live files, no applied registration diffs, no provenance SHAs.

**This PR (Gate 4) is a workbench/audit PR, not the release PR.** The `regulation/gdpr/` cutover happens only in the Gate 5 release PR, which itself is what "Gate 4 — pre-merge Publish Gate" gates.

---

*Workbench Gate 4 audit. Not a publication event.*
