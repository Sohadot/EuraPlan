# R2.8 — GDPR Publish Gate

**Status:** OPEN — Gates 0–2 CLOSED / PASS; Gate 3 AUTHORIZED / ACTIVE  
**Opened:** 2026-08-20  
**Gates 0–2 closed:** 2026-08-22  
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

**Current state:** **Gates 0–2 are CLOSED / PASS** — Gate 0 (Option A — Cloudflare exact-path `X-Robots-Tag: noindex`, verified live 2026-08-22, DEC-055), Gate 1 (pre-publication canonical build, PR #43), Gate 2 (release HTML candidate, PR #44). **Gate 3 is AUTHORIZED / ACTIVE.** Gates 4–6 remain unexecuted, and every live-mutation rule below still holds until its own gate authorizes it. Each gate proceeds under the DEC-054 frozen sequence as the prior gate closes; DEC-055 governs only the Gate 0 index-control decision.

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

### Gate 3 — Machine + registration package (AUTHORIZED / ACTIVE)

Prepare (still gated from merge until Gate 4/5):

- `regulation/gdpr/claims.json` package from Gate 1 build
- EP-REG-002 `alternate_representations` entry
- `llms.txt` exposure wording
- sitemap: HTML `lastmod` only — **never** list `claims.json`
- Apply crawler/index decision from Gate 0

---

### Gate 4 — Pre-merge Publish Gate

Must PASS before any release PR may merge:

- Graph integrity / parity
- HTML ↔ JSON proposition parity
- Qualification visibility (co-render pairs)
- Source registry resolution
- No staging/workbench leakage
- `secret-scan` SUCCESS
- Only then: authorize the release PR

---

### Gate 5 — Publication (single release sequence)

In one controlled release sequence:

- Lifecycle final: `publishable` → `published`
- `validity_state`: `null` → `active`
- `_meta.published=true`
- Live HTML + public graph + registrations together
- `release_sha` may be set on the release commit; **`merge_sha` is post-merge provenance finalization** (real merge commit on `main`) — typically immediately after merge and before Gate 6 closeout. Do **not** invent or guess `merge_sha` inside the pre-merge release PR.

---

### Gate 6 — Post-merge live verification

- Use the **real merge SHA**
- Verify live HTML, anchors, JSON, routes, llms, sitemap, and crawler/index behavior against Gate 0 decision
- RGS v2 re-score — target **≥ 90** before any Data Act / expansion work

---

## Hard rules while OPEN (Gates 0–2 CLOSED / PASS; Gate 3 ACTIVE)

| Rule | Status |
|---|---|
| Public `claims.json` live placement (`regulation/gdpr/**`) | **FORBIDDEN** until Gate 5 |
| Live GDPR HTML cutover (`regulation/gdpr/index.html`) | **FORBIDDEN** until Gate 5 |
| Live `routes.json` / `llms.txt` / sitemap / robots mutation | **FORBIDDEN** until Gate 5 (Gate 3 drafts the diffs only; no live edit) |
| Claim promotion beyond `publishable` (→ `published`) / `validity_state → active` | **FORBIDDEN** until Gate 5 |
| Invented provenance SHAs | **FORBIDDEN** always (`release_sha` at Gate 5 release; `merge_sha` post-merge before Gate 6) |

---

## Historical — opening PR criteria (satisfied)

*This section records the criteria the original opening PR met when R2.8 was first opened. It is historical; it does **not** describe the current state (see the status header and "Current state" above).* The opening PR correctly:

1. Recorded DEC-054
2. Froze the Gate 0→6 sequence above
3. Left execution blocked at Gate 0 (its state at the time)
4. Contained **no** live mutations

**Current progress:** Gates 0–2 are CLOSED / PASS. Gate 3 is AUTHORIZED / ACTIVE. Gates 4–6 remain unexecuted.

---

*Workbench / governance artifact. Not a publication event.*
