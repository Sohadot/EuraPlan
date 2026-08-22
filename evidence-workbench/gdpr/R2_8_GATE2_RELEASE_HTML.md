# R2.8 Gate 2 — Release HTML Candidate

**Status:** BUILD COMPLETE (branch-only) / AWAITING REVIEW
**Date:** 2026-08-22
**Scope:** Gate 2 only — no Gate 3–6 execution; no live mutation
**Authorized by:** DEC-055 (Gate 1 CLOSED / PASS → Gate 2 may begin)
**Governed by:** `R2_7_REGISTRATION_DRAFT.md` §E (E.1 parity contract, E.2 sanitization checklist)
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE1_CANONICAL_BUILD.md`

---

## 1. What this gate does

Produce a **release-sanitized HTML candidate** from the R2.6 workbench page candidate, applying the §E.2 checklist. This is **not** the live cutover: it is a branch-only artifact that Gate 4 verifies and Gate 5 publishes.

- **Source:** `evidence-workbench/gdpr/page-candidate/index.html` (unchanged — remains the R2.6 verification / Decision-Utility record)
- **Output:** `evidence-workbench/gdpr/release-candidate/index.html` (new artifact)
- **Not created:** no `regulation/gdpr/index.html`; the live route is written only at Gate 5.

The workbench candidate is **not** overwritten (avoids the §E.2 "hard fail if cutover is a raw copy").

---

## 2. §E.1 substance parity (candidate → release) — PRESERVED

| Item | Source | Release | Result |
|---|---|---|---|
| Claim anchors `#ep-clm-000015…000045` | 31 | 31 | ✅ identical |
| Co-render pairs (024↔025, 032↔033, 035↔036, 037↔038) | 4 blocks | 4 blocks | ✅ |
| Chapter V hierarchy `44 -> 45 -> 46 -> 49` | present | present | ✅ (framed as pathway, not equal options) |
| Decision Utility objects `EP-DU-GDPR-001…009` | 9 | 9 | ✅ |
| Claim bodies (`clock-reg-item`) | 31 | 31 | ✅ |
| New legal propositions introduced | — | none | ✅ (chrome only) |

---

## 3. §E.2 release-sanitization checklist

| # | Requirement | Gate 2 action | State |
|---|---|---|---|
| 1 | Live `<title>` | `GDPR Entry Planning Reference — EuraPlan` | ✅ done |
| 2 | Live meta description | Published planning-reference description; no "not live" language | ✅ done |
| 3 | Canonical URL | `https://euraplan.com/regulation/gdpr/` added | ✅ done |
| 4 | Robots `index, follow` | **DEFERRED to Gate 5** — kept `noindex, nofollow` (page is not live) | 🟡 deferred |
| 5 | Open Graph tags | `og:title/description/type/url/image/image:alt/site_name` | ✅ done |
| 6 | Twitter card tags | `twitter:card/title/description/image` | ✅ done |
| 7 | Article JSON-LD | added | ✅ done |
| 8 | Breadcrumb JSON-LD | added | ✅ done |
| 9 | `dateModified` semantics | page-update date on Article = `2026-08-22` (build date placeholder); **Gate 5 sets the real cutover date**; not conflated with claim `last_verified_at` | 🟡 finalized at Gate 5 |
| 10 | NOT LIVE / workbench banner | removed entirely | ✅ done |
| 11 | Telemetry / phase labels | removed `Route target (later)`, `Phase: R2.6`, `blocked until R2.8`; replaced with published EP-REG-002 telemetry | ✅ done |
| 12 | Hero / badge candidate language | removed `candidate` / `Pre-publication candidate` / "not the live public GDPR page" | ✅ done |
| 13 | Visible claim workflow labels | `verified (pre-publication)` → `publishable` (×31 + hero + sources); **Gate 5 flips to `published`** | 🟡 `publishable` now |
| 14 | Footer workbench disclaimer | removed workbench-only line; kept standard non-advice + verify-at-EUR-Lex disclaimer | ✅ done |
| 15 | Nav parity (Acquire) | added `/acquire/` to header **and** footer nav | ✅ done |
| 16 | Favicon parity | added `favicon.png` alongside `favicon.svg` | ✅ done |

### Items intentionally deferred to Gate 5 cutover (not applied here)

These are the atomic **live-switch** steps; applying them now would misrepresent the current lifecycle or create a live surface:

- **Robots → `index, follow`** (step 4): flipped only when the page goes live.
- **Visible workflow label → `published`** (step 13): claims are `publishable` at Gate 1/2; `publishable → published` is Gate 5.
- **`dateModified` → real cutover date** (step 9): build-date placeholder now.
- **Placement at `regulation/gdpr/index.html`**: the live route is written only in the Gate 5 release sequence.

---

## 4. Build method + checks

Deterministic transform (`page-candidate/index.html` → `release-candidate/index.html`); every chrome replacement was count-asserted, and substance was re-counted independently:

- [x] 31 anchors, 9 DU objects, 4 co-render blocks, 31 claim bodies — parity with source
- [x] **Zero sprint / workbench / governance-implementation language in the release candidate** (verified by sweep): no `R2.x` phase tags, `Publish Gate` / `Gate N`, `staging`, `DEC-0xx`, `workbench`, `pre-publication`, `V1–V5`, governance-doc filenames (e.g. `FRESHNESS_ENGINE.md`), or workbench field names (e.g. `r2_1_planning_consequence` / `decision-utility.staging.json`); NOT LIVE banner, candidate/phase labels, and the internal `<head>` build comment all removed
- [x] Live chrome present: canonical, OG set, Twitter set, Article JSON-LD, Breadcrumb JSON-LD, `dateModified`, `favicon.png`, header+footer `Acquire`
- [x] Both `application/ld+json` blocks parse as valid JSON
- [x] `robots` stays `noindex, nofollow` (deferred)
- [x] File ends with a trailing newline
- [x] Source workbench candidate unchanged; **no file under `regulation/gdpr/**`**
- [x] No `routes.json` / `llms.txt` / sitemap / robots.txt / live HTML mutation

---

## 5. Gate 2 exit criteria

Gate 2 is satisfied when:

1. A release-sanitized HTML candidate exists as a **transform** of the workbench candidate (not a raw copy). ✅
2. §E.1 substance parity holds (anchors, co-render pairs, Chapter V, Decision Utility). ✅
3. §E.2 chrome steps are applied except the documented Gate-5 live switches. ✅
4. No live surface created and no graph substance changed. ✅

**Exit:** on review PASS, Gate 2 is CLOSED / PASS. **Gate 3** (Machine + registration package) may then begin — **not** started here.

---

## 6. Non-goals of this build

- No Gate 3+ work (no `routes.json` alternate, no `llms.txt`, no sitemap, no public `claims.json`)
- No live HTML cutover, no `regulation/gdpr/**` file
- No robots `index,follow`, no `published` state, no `active` validity, no provenance SHAs

---

*Workbench Gate 2 build. Not a publication event.*
