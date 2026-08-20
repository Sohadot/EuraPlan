# R2.7 — Citation + Machine Registration Preparation

**Status:** OPEN  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-7-citation-machine-prep`  
**Prerequisite:** R2.6 CLOSED / PASS via PR #39 merge `81684158aeeff1f89da937e76c9e3e481ed69c34`

---

## What R2.7 is

Prepare **citation integrity** and **machine-registration packages** for the GDPR Evidence Graph so R2.8 Publish Gate can execute a controlled promotion — **without** executing public registration yet.

R2.7 is **not**:
- creation of public `/regulation/gdpr/claims.json`
- live overwrite of `/regulation/gdpr/index.html` with the Evidence Graph candidate
- `workflow_state` promotion to `publishable` / `published`
- writing `alternate_representations` for EP-REG-002 into live `routes.json`
- exposing GDPR `claims.json` in live `llms.txt`
- sitemap changes for a claims alternate
- opening Publish Gate (R2.8)

Those execute only inside **R2.8**.

---

## Inputs (frozen)

| Artifact | Role |
|---|---|
| `claims.canonical.staging.json` | Truth layer (31 verified claims) |
| `decision-utility.staging.json` | Derived Decision Utility (9 objects; not claims) |
| `page-candidate/index.html` | Citation surface + Decision Utility + Claim Register |
| AI Act gold | Pattern for `routes.json` alternate + `llms.txt` exposure |

---

## R2.7 deliverables

1. **This prep note** — citation checklist, machine-registration draft, hard gates  
2. **`R2_7_REGISTRATION_DRAFT.md`** — exact planned live deltas for R2.8 (not applied)  
3. **DEC-053** — close R2.6; open R2.7 under the above constraints  
4. Workbench status updates (`README.md`, R2.6 closed marker)

---

## Citation integrity checklist (prep)

Candidate must retain:

- [x] Stable anchors `#ep-clm-000015` … `#ep-clm-000045` (31/31)
- [x] Co-render pairs visible: 024↔025, 032↔033, 035↔036, 037↔038
- [x] Chapter V hierarchy `44 -> 45 -> 46 -> 49` (not equal options)
- [x] Decision Utility objects `EP-DU-GDPR-001`…`009` cite claim IDs only (no new legal propositions)
- [ ] Live page citation parity plan documented for R2.8 cutover (candidate → `/regulation/gdpr/`)
- [ ] Machine graph path planned: `/regulation/gdpr/claims.json` (file **not** created in R2.7)

---

## Machine registration draft (design only)

When R2.8 authorizes publication, planned deltas (mirror AI Act EP-REG-001):

1. Place canonical file at `regulation/gdpr/claims.json` from staging (after `publishable` → `published` promotion rules)
2. Add `alternate_representations` on EP-REG-002 in `routes.json`:
   - `path`: `/regulation/gdpr/claims.json`
   - `media_type`: `application/json`
   - `role`: `canonical_claim_graph`
   - `canonical_parent`: `/regulation/gdpr/`
   - `indexable`: false
   - `sitemap`: false
3. Expose in `llms.txt` with AI Act–parallel wording (static reference file, not an API)
4. **Do not** add `claims.json` to sitemap
5. Replace live HTML with the approved candidate only inside the same Publish Gate sequence
6. Decision Utility remains a page layer derived from claims — **not** a second public JSON truth file unless a later DEC explicitly authorizes it

Exact draft text lives in `R2_7_REGISTRATION_DRAFT.md`.

---

## Hard gates (DEC-053)

| Gate | Rule |
|---|---|
| Public `claims.json` | **FORBIDDEN** in R2.7 |
| Live HTML Evidence Graph cutover | **FORBIDDEN** in R2.7 |
| `routes.json` / `llms.txt` / sitemap live edits for GDPR claims | **FORBIDDEN** in R2.7 |
| Claim workflow | Remains `verified` until R2.8 |
| Publish Gate (R2.8) | **NOT OPEN** |
| New claims | None required for registration prep |
| AI Act gold | Untouched except real freshness events |
| Decision Utility | Derived only; not promoted to truth layer |

---

## Exit toward R2.8

R2.7 may close when:

1. Citation inventory PASS (anchors, co-render, hierarchy, DU traceability)
2. Registration draft complete and owner-reviewed
3. No live registration executed
4. Owner authorizes **R2.8 Publish Gate** as a separate controlled sequence

---

*Workbench artifact only. Not a published website page.*
