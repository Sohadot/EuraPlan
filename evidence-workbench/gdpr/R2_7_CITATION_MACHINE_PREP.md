# R2.7 — Citation + Machine Registration Preparation

**Status:** CLOSED / PASS  
**Opened:** 2026-08-20  
**Closed:** 2026-08-20  
**Integration merge:** PR #40 `8ec08e0b9c5315ef2f80c6b945503b5784e0788b`  
**Reviewed head:** `b3d35f6e5f91c633cdff19df3eb2986b7bd6dd8a`  
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
- inventing publication provenance SHAs before they exist

Those execute only inside **R2.8**.

---

## Inputs (frozen)

| Artifact | Role |
|---|---|
| `claims.canonical.staging.json` | Truth layer (31 verified claims) |
| `decision-utility.staging.json` | Derived Decision Utility (9 objects; not claims) |
| `page-candidate/index.html` | Citation surface + Decision Utility + Claim Register |
| Live `/regulation/gdpr/index.html` | Publication chrome baseline (canonical, robots, OG/Twitter, JSON-LD) |
| AI Act gold | Pattern for public `_meta`, `routes.json` alternate, `llms.txt` |

---

## R2.7 deliverables

1. **This prep note** — citation checklist, machine-registration draft, hard gates  
2. **`R2_7_REGISTRATION_DRAFT.md`** — transformation contract, crawl reality, HTML sanitization checklist (not applied)  
3. **DEC-053** — close R2.6; open R2.7 under the above constraints  
4. Workbench status updates (`README.md`, R2.6 closed marker)

---

## Citation integrity checklist (prep)

Candidate must retain:

- [x] Stable anchors `#ep-clm-000015` … `#ep-clm-000045` (31/31)
- [x] Co-render pairs visible: 024↔025, 032↔033, 035↔036, 037↔038
- [x] Chapter V hierarchy `44 -> 45 -> 46 -> 49` (not equal options)
- [x] Decision Utility objects `EP-DU-GDPR-001`…`009` cite claim IDs only (no new legal propositions)
- [x] **Live page citation parity contract documented** for R2.8 cutover — see `R2_7_REGISTRATION_DRAFT.md` §E.1 / §E.2 (documented; **not** executed)
- [x] **Machine graph path + transformation contract documented** for `/regulation/gdpr/claims.json` — see `R2_7_REGISTRATION_DRAFT.md` §A / §A.1 (documented; file **not** created in R2.7)

---

## Machine registration draft (design only)

When R2.8 authorizes publication, planned deltas (mirror AI Act EP-REG-001):

1. Transform staging → public canonical graph under §A.1 (lifecycle + `_meta` sanitization + real provenance SHAs only when they exist)
2. Add `alternate_representations` on EP-REG-002 in `routes.json` (`indexable:false` = **governance metadata only**, not crawler enforcement)
3. Expose in `llms.txt` with AI Act–parallel wording (static reference file, not an API)
4. **Do not** add `claims.json` to sitemap
5. Decide and record crawler/indexing mechanism under hosting capability (`robots.txt` / `X-Robots-Tag` / explicit accept-crawlability) — see draft §D.1
6. Cut over live HTML only after completing the §E.2 release-sanitization checklist
7. Decision Utility remains a page layer derived from claims — **not** a second public JSON truth file unless a later DEC explicitly authorizes it

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
| Provenance SHAs | Must not be invented before R2.8 git objects exist |
| `indexable:false` | Governance only; not assumed crawler enforcement |

---

## Exit toward R2.8

R2.7 closed after owner Citation Integrity Prep + Registration Preparation Fidelity PASS and Integration merge on `main`.

**R2.8 — Publish Gate** is OPEN under **DEC-054** with **execution BLOCKED AT GATE 0** (Hosting & Index-Control Capability). Live mutations remain forbidden until later R2.8 gates authorize them.

---

*Workbench artifact only. Not a published website page.*
