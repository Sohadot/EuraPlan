# R2.8 Gate 1 — Pre-publication Canonical Build

**Status:** BUILD COMPLETE (branch-only) / AWAITING REVIEW
**Date:** 2026-08-22
**Scope:** Gate 1 only — no Gate 2–6 execution; no live mutation
**Authorized by:** DEC-055 (Gate 0 CLOSED / PASS → Gate 1 AUTHORIZED / ACTIVE)
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE0_HOSTING_INDEX_CONTROL.md`; DEC-054; `R2_7_REGISTRATION_DRAFT.md` §A.1

---

## 1. What this gate does

Produce a **pre-publication canonical build** of the GDPR claim graph as a **transform** (not a raw copy) of the workbench staging graph, with claim lifecycle advanced exactly one legal step (`verified → publishable`) and **nothing published**.

- **Input:** `evidence-workbench/gdpr/claims.canonical.staging.json` (unchanged — remains the staging truth layer)
- **Output:** `evidence-workbench/gdpr/claims.prepublication.candidate.json` (new artifact)

The original staging file is **not** overwritten; the candidate is a separate artifact.

---

## 2. Transformation performed

| Field | Staging | Candidate | Rule |
|---|---|---|---|
| `workflow_state` (all 31) | `verified` | **`publishable`** | Gate 1 promotion (§A.1) — one step only |
| `validity_state` (all 31) | `null` | `null` | **Unchanged** — `null → active` only at Gate 5 |
| `confidence` (all 31) | `Verified` | `Verified` | Unchanged |
| `last_verified_at` (all 31) | `2026-08-20` | `2026-08-20` | Unchanged |
| claim text / `id` / `effective_date` / `sources` / `qualified_by` / `claim_risk` / EERS dims | — | — | **Byte-identical** (no edits) |
| `_meta.published` | `false` | `false` | Unchanged — not published |

**Workbench chrome removed from `_meta`:** `phase` (`R2.4`), `html` (`BLOCKED`), `publish_gate` (`NOT OPEN`), `routes_json_alternate` (`NOT YET`), `llms_txt` (`NOT YET`), `sitemap` (`NOT YET`), `integrity_fix`, `source_of_truth_for_propositions`, and staging `location_note`/`batch`/`status` language.

**Preserved substantive graph metadata:** `route_id` (EP-REG-002), `target_public_path`, `target_route`, `schema_version`, `claim_count` (31), `id_range` (EP-CLM-000015..000045), `co_render_blocking_pairs`, `chapter_v_related_hierarchy`, `source_registry` (EP-SRC-000004, EP-SRC-000005).

**`governed_by` updated (per `R2_7_REGISTRATION_DRAFT.md` §A.1 — "retain + add R2.8 Publish Gate DEC when issued"):** existing entries retained; **`DEC-054` and `DEC-055` added** so the build reflects the DECs that actually govern R2.8 (previously the list ended at `DEC-050`). No other `_meta` field and no claim changed.

**No invented provenance:** `release_sha` / `merge_sha` are **absent** from `_meta`; they are set only from real git objects at Gate 5 (never guessed here). The `_meta.notes` references to them are documentation of that deferral, not values.

---

## 3. Transformation checks (all PASS)

Verified by a deterministic transform + independent re-diff of output vs input:

- [x] Exactly **31/31** claims present; IDs `EP-CLM-000015…EP-CLM-000045`, ascending, no duplicates
- [x] **Only** differing per-claim field across all 31 is `workflow_state` (`verified → publishable`)
- [x] `validity_state = null` on all 31 (no premature `active`)
- [x] `confidence = Verified` and `last_verified_at = 2026-08-20` on all 31 (unchanged)
- [x] `_meta.published = false`
- [x] `_meta.governed_by` retained and updated to reflect R2.8 governance — **`DEC-054` and `DEC-055` added** (§A.1: retain + add the R2.8 Publish Gate DEC when issued)
- [x] No `phase` / `html=BLOCKED` / `publish_gate=NOT OPEN` / `NOT YET` markers in output
- [x] No `release_sha` / `merge_sha` keys invented in `_meta`
- [x] No file created under `regulation/gdpr/**`
- [x] No `routes.json` / `llms.txt` / sitemap / robots / live HTML change in this build
- [x] Propositions, sources, qualifications, and IDs unchanged

---

## 4. Hard boundaries honored (still gated)

| Rule | Status |
|---|---|
| Public `claims.json` under `regulation/gdpr/**` | **NOT created** (Gate 3–5) |
| Live GDPR HTML cutover | **NOT touched** (Gate 2–5) |
| Live `routes.json` / `llms.txt` / sitemap / robots | **NOT touched** (Gate 3–5) |
| `validity_state → active` | **NOT done** (Gate 5) |
| `_meta.published → true` | **NOT done** (Gate 5) |
| Invented provenance SHAs | **None** |

---

## 5. Gate 1 exit criteria

Gate 1 is satisfied when:

1. `claims.prepublication.candidate.json` exists as a **transform** of staging with `verified → publishable` and `validity_state = null`. ✅
2. No claim substance (text, IDs, sources, qualifications, EERS, risk, dates) changed. ✅
3. Workbench-only `_meta` markers are removed; no publication fields (`published=true`, SHAs, `active`) introduced. ✅
4. No live-surface mutation and no `regulation/gdpr/**` file created. ✅

**Exit:** on review PASS, Gate 1 is CLOSED / PASS. **Gate 2** (Release HTML candidate, §E.2) may then begin — **not** started here.

---

## 6. Non-goals of this build

- No Gate 2 / Gate 3 work (no release HTML, no machine/registration package) in parallel
- No public graph, no live HTML, no registration mutations
- No promotion of `validity_state`, no `published=true`, no provenance SHAs

---

*Workbench Gate 1 build. Not a publication event.*
