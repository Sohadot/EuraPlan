# EU_AI_ACT_PUBLISH_GATE_2026-08-20.md
**Status:** Public working evidence — Publish Gate audit (Final Publication Release merged; Post-Merge Verification CLOSED after homepage derivative-drift hotfix)
**Asset:** EuraPlan.com
**Route:** `/regulation/eu-ai-act/` (+ `/clock/` consistency)
**Gate date:** 2026-08-20
**Branch:** `claude/euraplan-strategic-digital-asset-sr2h1e` (PR #24, open, unmerged)
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, EVIDENCE_GRAPH_MODEL.md, CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md, FRESHNESS_ENGINE.md, SOURCE_POLICY.md, CLAIM_POLICY.md, DISCLOSURE_BOUNDARY.md

---

> **Final Publication Release merged to `main`.** Release SHA
> `1cc02e1a6fe3ec3764e7e234c6ffb943eebfea3e` via merge commit
> `3322e6befd9e3f0c86fc993cad0d4fbe4d4f15aa`. RC.2 CLOSED / PASS. The 14 Claim
> Objects are `workflow_state: published`, `validity_state: active`,
> `_meta.published: true`. Post-Merge Live Verification initially failed on
> homepage derivative drift; closed PASS after the homepage-only hotfix (DEC-046).

## 1. Gate results

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Claim equality (only `verified → publishable`) | **PASS** | No `claim`, `id`, `effective_date`, `sources`, `qualified_by`, `claim_risk`, `EERS`, or lifecycle field changed vs the verified workbench copy; only `workflow_state` differs. |
| 2 | Sources (append-only) | **PASS** | `EP-SRC-000003` added (EUR-Lex consolidated text, CELEX `02024R1689-20260727`, current-reading aid); `EP-SRC-000001`/`000002` byte-identical to the workbench, remain authoritative. |
| 3 | Qualifications rendered | **PASS** | `003 → 006`, `005 → 003,004,006,007,008,010`, `012 → 014` render as visible anchor links inside each claim block; no default shown without its qualification. |
| 4 | Stable anchors | **PASS** | `id="ep-clm-000001"` … `id="ep-clm-000014"` present, 14 unique. |
| 5 | HTML ↔ JSON agreement | **PASS** | Every claim's effective date appears in the Verified Claim Register; register mirrors `claims.json`. |
| 6 | `/clock/` agreement | **PASS** | AI Act lane, aria-label, role panel, and established-date list match the canonical graph (2 Dec 2027 Annex III; 2 Aug 2028 Annex I; general 2 Aug 2026 qualified). |
| 7 | Stale-date removal | **PASS** | Removed: Annex III = 2 Aug 2026; Annex I = 2 Aug 2027; "full application" wording absorbing the staggered high-risk exceptions; old `Art. 113(4)` framing. Verified absent on both pages. |
| 8 | Visible sources | **PASS** | Tier-1 source table adds Reg (EU) 2026/1744 and the consolidated text (marked convenience-only; authentic OJ acts authoritative). |
| 9 | Structured-data date equality | **PASS** | Visible `Last Updated` = JSON-LD `dateModified` = `2026-08-20` on both pages; verification date `2026-08-19` shown separately (page date ≠ verification date). |
| 10 | Disclaimer | **PASS** | "This is not legal advice" retained on the page and per-claim confidence shown. |
| 11 | Internal links | **PASS** | All `#ep-clm-*` references resolve to existing anchors; `claims.json` alternate link present. |
| 12 | Agent readability | **PASS** | `<link rel="alternate" type="application/json" href="/regulation/eu-ai-act/claims.json">`; `llms.txt` exposes the canonical graph narrowly (no API/endorsement claim); claims in real HTML, not JS-only. |
| 13 | Secret-scan | **PASS** | Gitleaks working-tree scan (~1 MB) — 0 findings; the `secret-scan` GitHub Action re-verifies on push/PR. |
| 14 | Disclosure boundary | **PASS** | All changed files are public governance / public evidence-data / reference HTML — no private operational intelligence, no credentials. |

**Overall: PASS (Release Candidate).**

## 2. Hard prohibitions — confirmed honoured
- PR #24 **not merged**; branch only.
- No `publishable → published`; no `validity_state: active`.
- No new claims minted; the 14 verified propositions unchanged.
- Article 111(4) **not** published in this batch (deferred).
- EERS remains **Candidate**.
- No manufactured changelog assigning `EP-CLM` identities to legacy prose.
- `EP-SRC-000001`/`000002` not mutated; consolidated text added as a new node only.

## 3. Files in this gate
- `regulation/eu-ai-act/claims.json` (new, canonical, 14 `publishable`)
- `regulation/eu-ai-act/index.html` (timeline corrected; Verified Claim Register; sources; dates; alternate link)
- `clock/index.html` (AI Act lane/list corrected; dates; RC.2 visual scale)
- `llms.txt` (expose `claims.json`)
- `routes.json` (RC.2: `claims.json` registered as alternate machine representation of EP-REG-001)
- `assets/css/main.css` (five-year clock surface; RC.2 scale comment)
- `ROUTE_GOVERNANCE.md` (RC.2: alternate machine representation registry rule)
- `DECISION_LOG.md` (DEC-045)
- `governance/audits/EU_AI_ACT_PUBLISH_GATE_2026-08-20.md` (this record)

## 4. Remaining to go live (separate gate — owner) — corrected order

If `main` is the publication source, merging **before** flipping state would make the
HTML and `claims.json` live while the graph still says `publishable` /
`validity_state: null` — the public reality would run ahead of the governed state.
Correct order after RC.1 PASS:

1. Final **release-state commit on the branch**: all 14 → `workflow_state: published`,
   `validity_state: active`, `_meta.published: true`.
2. Merge **that same SHA** to `main`.
3. Live verification of euraplan.com.

Public effectiveness begins at the merge to `main`; there is no moment where `main`
serves a live corpus in a `publishable` state. `claims.json` is registered in
`routes.json` as an alternate machine representation of EP-REG-001 (not a new
Layer, not independently indexed, not a sitemap URL). Hreflang/multilingual work
remains out of scope for this AI-Act-only RC.

## 5. RC.1 — Final Consistency Closure (2026-08-20)

Four bounded fixes after RC review; no claim proposition, ID, source edge, or
`qualified_by` changed.

| Fix | Result |
|---|---|
| `claims.json` `_meta` self-contradiction (stale "verified" note; false "publishable is a CLOSED gate — no claims.json/anchors/HTML" note) | **PASS** — removed; `_meta` now describes the RC only; `generated: 2026-08-20`. |
| Legacy `Article 113(2)` on the AI Act page (GPAI role panel + matrix question) | **PASS** — both corrected to `Article 113, third paragraph, point (b)`, linked to `#ep-clm-000004`; no `113(2)` remains. |
| `/clock/` over-broad high-risk wording + incomplete ARIA | **PASS** — role panel narrowed to "Chapter III Sections 1–3, except Article 6(5) …"; AI Act lane `aria-label` now includes the 2 Dec 2026 Article 5 exception and marks 2 Aug 2026 as qualified. |
| `/clock/` axis/track visual regression (6 axis cells vs 4-period CSS grid) | **PASS** — scoped, opt-in modifiers `clock-preview-axis--five-years` (`repeat(5,1fr)`) and `clock-lane-track--five-years` (20% gridlines) added; global 4-period grid unchanged for all other components/pages. |

Overall after RC.1: **PASS (Release Candidate).** Still not merged; still `publishable`, not `published`/`active`.

## 6. RC.2 — Final Release Preflight (2026-08-20)

Three bounded preflight fixes after RC.1; no `EP-CLM-*`, source edge, effective
date, or `qualified_by` changed.

| Fix | Result |
|---|---|
| `/clock/` marker `left:%` still on the old 4-year visual scale after RC.1 stretched the axis to 2024–2028 | **PASS** — markers recalibrated to a fixed scale `2024-01-01 = 0%`, `2029-01-01 = 100%`. Regulatory dates unchanged; only visual position. GDPR remains a pre-window baseline on the leading edge (`pre-2024 — ongoing`). CSS comment corrected: the five-year modifier applies to all lanes on the 2024–2028 Clock surface. |
| `claims.json` announced as the canonical public graph but unregistered in `routes.json` | **PASS** — registered as `alternate_representations[]` on EP-REG-001 (`path` `/regulation/eu-ai-act/claims.json`, `media_type` `application/json`, `role` `canonical_claim_graph`, `canonical_parent` `/regulation/eu-ai-act/`, `indexable`/`sitemap` false). No new Layer. `ROUTE_GOVERNANCE.md` §4/§7 record the pattern. |
| Release-semantics wording (`_meta.publish_gate`; DEC-045 Rationale) still described the RC as if already published | **PASS** — `publish_gate` now: final release-state commit gated on RC approval; public effectiveness begins when that release SHA is merged to `main`. DEC-045 Rationale: `publishes` → `authorizes the publication candidate`. |

Overall after RC.2: **PASS (Release Candidate).** Still not merged; still `publishable`, not `published`/`active`. No further conceptual round; remaining owner action is Final Publication Release then the release-state commit and merge.

## 7. Final Publication Release (2026-08-20)

RC.2 approved. Final Publication Release **AUTHORIZED**. Merge to `main` is **not** authorized.

| Check | Result |
|---|---|
| RC.2 approved | **PASS** — Clock scale, route governance, release semantics, claim integrity, secret-scan, PR state, and this audit's RC.2 section all PASS. |
| 14/14 `publishable` → `published` | **PASS** — workflow-state only. Spec meaning `published` = Live in the corpus takes public effect at merge of this exact SHA to `main`. |
| 14/14 `null` → `active` | **PASS** — validity-state only. Spec meaning `active` = public validity after publication takes public effect at the same merge. |
| Semantic Claim mutation | **NONE** — no `claim` text, ID, display label, effective date, source registry node, source edge, `qualified_by`, risk, EERS dimension, or lifecycle pointer changed. `confidence` remains `Verified`; every `last_verified_at` remains `2026-08-19`. HTML/CSS/`/clock/` untouched. Article 111(4) still deferred; EERS still Candidate. |
| Release staging | **PASS** — this is a release-state tree staged for atomic publication on the branch. It is not live merely by existing on the development branch. |
| Public effectiveness | Begins only when the exact release SHA is merged to `main`. |
| Post-merge live verification | **Still required** after merge: euraplan.com, `claims.json`, and the 14 anchors. |

**Overall after Final Publication Release commit: PASS (staged).** PR #24 remains open and unmerged. Merge to `main` = NOT YET AUTHORIZED.

## 8. Post-Merge Live Verification (2026-08-20)

Merge commit `3322e6befd9e3f0c86fc993cad0d4fbe4d4f15aa` (parents: prior `main` + release SHA `1cc02e1a6fe3ec3764e7e234c6ffb943eebfea3e`). Public effectiveness of the release-state tree begins at this merge.

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | `main` contains release SHA `1cc02e1…` | **PASS** | `1cc02e1` is an ancestor of `origin/main` / merge commit `3322e6b`. |
| 2 | Live / repo `claims.json`: `_meta.published: true`; 14/14 `published` / `active` | **PASS** | Canonical graph unchanged by hotfix; state transition intact. |
| 3 | `/regulation/eu-ai-act/` — 14 anchors | **PASS** | Verified Claim Register anchors present; not modified by hotfix. |
| 4 | `/clock/` — correct AI Act dates / scale | **PASS** | Canonical clock surface unchanged by hotfix. |
| 5 | Homepage Regulatory Clock Preview ↔ canonical AI Act timeline | **FAIL → PASS** | **FAIL at first post-merge check:** homepage still showed 2024–2027 axis and Aug 2027 / Art. 113.4 while claims + AI Act page + `/clock/` were correct (derivative drift). **PASS after hotfix** `fix/homepage-ai-act-derivative-drift`: `index.html` only — five-year axis, calibrated markers, qualifications, Article 5 exception (2 Dec 2026) mentioned; Aug 2027 removed. No claim / source / AI Act page / `/clock/` change. |

**Architectural follow-up (DEC-046):** `DERIVATIVE_SURFACE_REGISTRY.md` + `EVIDENCE_GRAPH_MODEL.md` §10 — any surface displaying Evidence Graph dates must derive from the canonical graph or be registered with a consistency check.

**Overall after hotfix: Post-Merge Publication Verification = PASS / CLOSED.**

## 9. Post-merge `_meta` live-status housekeeping (2026-08-20)

Metadata-only cleanup of `claims.json` `_meta` (DEC-047). Pre-merge “staged / effectiveness begins at merge” wording replaced with **published / active — live on main since 2026-08-20**, with `release_sha` / `merge_sha` retained as provenance. **No** claim proposition, workflow_state, validity_state, source, or `qualified_by` change. Publish Gate remains CLOSED / PASS.

---

*EuraPlan.com — EU AI Act Publish Gate audit (RC closed; Final Publication Release merged; Post-Merge Verification CLOSED; `_meta` live-status housekeeping recorded). Not a published website page.*
