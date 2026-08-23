# R2.8 — GDPR Publish Gate

**Status:** OPEN — Gates 0–4 CLOSED / PASS; Gate 5 Phase A LIVE (2026-08-23), Phase B STAGED / PENDING MERGE (PR #48); Gate 6 UNEXECUTED / NOT YET AUTHORIZED  
**Opened:** 2026-08-20  
**Gates 0–4 closed:** 2026-08-22  
**Opening merge:** PR #41 `cb893438c65438b4aaa7673990ea432798fc535c`  
**Prerequisite:** R2.7 CLOSED / PASS via PR #40 merge `8ec08e0b9c5315ef2f80c6b945503b5784e0788b`  
**Governing DEC:** DEC-054; DEC-055  
**Registration contracts:** `R2_7_REGISTRATION_DRAFT.md` (§A.1, §D.1, §E.1–E.2)  
**Gate 0 investigation:** `R2_8_GATE0_HOSTING_INDEX_CONTROL.md` (CLOSED / PASS — Option A implemented)

---

## What opening R2.8 means

Opening this phase authorizes the **Publish Gate sequence** for EP-REG-002. It does **not** mean:

- claims are already `publishable` or `published`
- public `/regulation/gdpr/claims.json` may be created yet
- live `/regulation/gdpr/index.html` may be overwritten yet
- live `routes.json` / `llms.txt` / sitemap / robots may be edited yet
- provenance SHAs may be invented

**Current state:** **Gates 0–4 are CLOSED / PASS** — Gate 0 (Option A — Cloudflare exact-path `X-Robots-Tag: noindex`, verified live 2026-08-22, DEC-055), Gate 1 (pre-publication canonical build, PR #43), Gate 2 (release HTML candidate, PR #44), Gate 3 (machine + registration package, PR #45), Gate 4 (pre-merge audit 25/25, PR #46). **Gate 5 Phase A is LIVE** — PR #47 merged `f97a51e`, **GDPR reference live on main since 2026-08-23**. **Gate 5 Phase B is STAGED / PENDING MERGE** in PR #48 (provenance `release_sha=b392ba5`, `merge_sha=f97a51e`, `live_on_main_since=2026-08-23`); Gate 5 closes when PR #48 merges. **Gate 6 is NOT YET AUTHORIZED** — it becomes authorized on the PR #48 merge (post-merge live verification + RGS v2 re-score). Each gate proceeds under the DEC-054 frozen sequence as the prior gate closes; DEC-055 governs only the Gate 0 index-control decision.

---

## Gate sequence (frozen by DEC-054)

### Gate 0 — Hosting & Index-Control Capability (CLOSED / PASS)

Determine the actual serving stack for `euraplan.com` and whether path-specific index control is possible.

Required determinations:

1. Which layer actually serves the site (GitHub Pages alone vs Pages + CDN/proxy such as Cloudflare, etc.).
2. Whether `X-Robots-Tag: noindex` can be emitted **specifically** for `/regulation/gdpr/claims.json`.
3. If not: document the explicit alternative — precise `robots.txt` rule, or accept crawlability with sitemap exclusion — distinguishing **crawl control** from **index control**.
4. Do **not** assume unproven capability.

#### Gate 0 starting observations (not conclusions)

| Fact | Value | Implication |
|---|---|---|
| GitHub `has_pages` | `true` | Pages is enabled; do not assume arbitrary per-path HTTP headers |
| Repo `CNAME` | `euraplan.com` | Custom domain on Pages |
| `robots.txt` | `Allow: /regulation/` | When `claims.json` exists under `/regulation/gdpr/`, it is **technically crawlable** unless Gate 0 chooses another control |
| `routes.json` `indexable:false` | governance metadata only | Not crawler/index enforcement |

#### Gate 0 investigation result (2026-08-20) + closeout (2026-08-22)

See `R2_8_GATE0_HOSTING_INDEX_CONTROL.md`.

| Determination | Result |
|---|---|
| Serving stack | **Cloudflare-proxied GitHub Pages** (NS + `Server: cloudflare` + `X-GitHub-Request-Id` / Fastly origin markers) |
| `X-Robots-Tag` via GitHub Pages alone | **Not available** |
| `X-Robots-Tag` via Cloudflare | **CONFIGURED / VERIFIED LIVE** (2026-08-22): target `/regulation/gdpr/claims.json` → **404** pre-publication + `X-Robots-Tag: noindex` **present**; negative control `/regulation/gdpr/` → **200** + header **absent** (scope isolation PASS) |
| Owner decision | **Option A SELECTED / IMPLEMENTED** |

**Selected** Option A: `X-Robots-Tag: noindex` via a Cloudflare **exact-path** rule; configured and verified live 2026-08-22. `robots.txt Disallow` alone is crawl guidance, not a guarantee of `noindex` — not used.

**Gate 0 exit:** **CLOSED / PASS.** Option A implemented and scope-isolated (positive + negative controls). **Gate 6** re-tests the header on a live `200` response after publication (current verification is against a pre-publication `404`). Gate 1 was authorized at Gate 0 closeout and is now **CLOSED / PASS** (PR #43).

---

### Gate 1 — Pre-publication canonical build (CLOSED / PASS)

Workbench / branch only until later gates authorize live placement.

- Transform staging → pre-publication canonical build (**not** raw copy) per `R2_7_REGISTRATION_DRAFT.md` §A.1.
- All 31 claims: `verified` → `publishable` only at this gate.
- `validity_state` remains `null` here — **not** `active` before publication.
- Clean `_meta` of workbench markers (`phase`, `html=BLOCKED`, `publish_gate=NOT OPEN`, staging location language, etc.).
- **No invented `merge_sha` / `release_sha`.**

---

### Gate 2 — Release HTML candidate (CLOSED / PASS)

- Execute full §E.2 release-sanitization checklist.
- Remove all R2.6 / workbench / pre-publication chrome.
- Add/restore: live title/description, canonical, robots (`index, follow` only when publication completes), OG/Twitter, Article + Breadcrumb JSON-LD, page `dateModified` (independent of claim `last_verified_at`).
- Preserve without dilution: 31 anchors, four co-render pairs, Chapter V hierarchy, nine Decision Utility objects.
- Graph substance parity with Gate 1 build (§E.1).

---

### Gate 3 — Machine + registration package (CLOSED / PASS)

Prepare (still gated from merge until Gate 4/5):

- `regulation/gdpr/claims.json` package from Gate 1 build
- EP-REG-002 `alternate_representations` entry
- `llms.txt` exposure wording
- sitemap: HTML `lastmod` only — **never** list `claims.json`
- Apply crawler/index decision from Gate 0

---

### Gate 4 — Pre-merge Publish Gate (CLOSED / PASS)

Must PASS before any release PR may merge:

- Graph integrity / parity
- HTML ↔ JSON proposition parity
- Qualification visibility (co-render pairs)
- Source registry resolution
- No staging/workbench leakage
- `secret-scan` SUCCESS
- Only then: authorize the release PR

---

### Gate 5 — Publication (release sequence + post-merge provenance) (Phase A LIVE; Phase B STAGED / PENDING MERGE — PR #48)

Content and registration land together in one controlled release sequence (Phase A); provenance is finalized post-merge (Phase B):

Phase A (release PR, pre-merge):
- Lifecycle final: `publishable` → `published`
- `validity_state`: `null` → `active`
- `_meta.published=true`
- Live HTML + public graph + registrations together
- **No provenance SHAs in the release PR** (they do not exist pre-merge)

Phase B (post-merge provenance finalization, before Gate 6):
- A commit cannot contain its own SHA, so provenance is written **after** the commits exist, in a follow-up provenance PR/commit merged to `main` before Gate 6: `release_sha` = the real release-state commit SHA and **`merge_sha` = the real merge commit on `main`** (both from real git objects); `live_on_main_since` = the actual publication event. Never pre-merge, never self-referencing. (AI Act precedent: `release_sha` and `merge_sha` recorded this way.)

---

### Gate 6 — Post-merge live verification (AUTHORIZED ON MERGE OF PR #48)

- Use the **real merge SHA**
- Verify live HTML, anchors, JSON, routes, llms, sitemap, and crawler/index behavior against Gate 0 decision
- RGS v2 re-score — target **≥ 90** before any Data Act / expansion work

---

## Hard rules while OPEN (Gates 0–4 CLOSED / PASS; Gate 5 Phase A LIVE, Phase B pending PR #48; Gate 6 not yet authorized)

| Rule | Status |
|---|---|
| Public `claims.json` live placement (`regulation/gdpr/**`) | **LIVE** (Gate 5, PR #47 merged `f97a51e`, 2026-08-23) |
| Live GDPR HTML cutover (`regulation/gdpr/index.html`) | **LIVE** (Gate 5, 2026-08-23) |
| Live `routes.json` / `llms.txt` / sitemap mutation | **LIVE** (Gate 5: `routes.json` alternate, `llms.txt` line, sitemap `lastmod`); `robots.txt` unchanged |
| Claim promotion beyond `publishable` (→ `published`) / `validity_state → active` | **DONE** (published / active, Gate 5) |
| Invented provenance SHAs | **FORBIDDEN** always — Phase B provenance (`release_sha=b392ba5`, `merge_sha=f97a51e`, `live_on_main_since=2026-08-23`) is **staged in PR #48** from real git objects, effective on merge; never invented, never self-referencing |

---

## Historical — opening PR criteria (satisfied)

*This section records the criteria the original opening PR met when R2.8 was first opened. It is historical; it does **not** describe the current state (see the status header and "Current state" above).* The opening PR correctly:

1. Recorded DEC-054
2. Froze the Gate 0→6 sequence above
3. Left execution blocked at Gate 0 (its state at the time)
4. Contained **no** live mutations

**Current progress:** Gates 0–4 are CLOSED / PASS. Gate 5 Phase A is LIVE (GDPR reference live on main since 2026-08-23); Phase B provenance is staged in PR #48 (pending merge). Gate 6 is authorized on the PR #48 merge (live verification + RGS re-score).

---

*Workbench / governance artifact. Not a publication event.*
