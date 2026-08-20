# EU_AI_ACT_PUBLISH_GATE_2026-08-20.md
**Status:** Public working evidence — Publish Gate audit (Release Candidate)
**Asset:** EuraPlan.com
**Route:** `/regulation/eu-ai-act/` (+ `/clock/` consistency)
**Gate date:** 2026-08-20
**Branch:** `claude/euraplan-strategic-digital-asset-sr2h1e` (PR #24, open, unmerged)
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, EVIDENCE_GRAPH_MODEL.md, CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md, FRESHNESS_ENGINE.md, SOURCE_POLICY.md, CLAIM_POLICY.md, DISCLOSURE_BOUNDARY.md

---

> **Release Candidate only — NOT yet live on `main`.** The 14 Claim Objects are
> `workflow_state: publishable`, `validity_state: null` — publication candidates, not
> `published`/`active`. Nothing in this gate is merged to `main`.

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
- `clock/index.html` (AI Act lane/list corrected; dates)
- `llms.txt` (expose `claims.json`)
- `DECISION_LOG.md` (DEC-045)
- `governance/audits/EU_AI_ACT_PUBLISH_GATE_2026-08-20.md` (this record)

## 4. Remaining to go live (separate gate — owner)
RC review → merge PR #24 to `main` → only then `publishable → published` / `validity_state: active`. Routes/sitemap registration of `claims.json` and any hreflang/multilingual work are out of scope for this AI-Act-only RC.

---

*EuraPlan.com — EU AI Act Publish Gate audit (Release Candidate). Not a published website page.*
