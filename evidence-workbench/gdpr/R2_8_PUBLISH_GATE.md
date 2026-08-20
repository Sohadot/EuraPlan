# R2.8 — GDPR Publish Gate

**Status:** OPEN / EXECUTION BLOCKED AT GATE 0  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-8-publish-gate-open`  
**Prerequisite:** R2.7 CLOSED / PASS via PR #40 merge `8ec08e0b9c5315ef2f80c6b945503b5784e0788b` (head `b3d35f6e5f91c633cdff19df3eb2986b7bd6dd8a`)  
**Governing DEC:** DEC-054  
**Registration contracts:** `R2_7_REGISTRATION_DRAFT.md` (§A.1, §D.1, §E.1–E.2)

---

## What opening R2.8 means

Opening this phase authorizes the **Publish Gate sequence** for EP-REG-002. It does **not** mean:

- claims are already `publishable` or `published`
- public `/regulation/gdpr/claims.json` may be created yet
- live `/regulation/gdpr/index.html` may be overwritten yet
- live `routes.json` / `llms.txt` / sitemap / robots may be edited yet
- provenance SHAs may be invented

**Current freeze:** execution is **BLOCKED AT GATE 0** until Hosting & Index-Control Capability is verified and recorded.

---

## Gate sequence (frozen by DEC-054)

### Gate 0 — Hosting & Index-Control Capability (ACTIVE BLOCKER)

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

**Prefer** `X-Robots-Tag: noindex` for index control if the host/CDN supports it. `robots.txt Disallow` alone is crawl guidance, not a guarantee of `noindex`.

**Exit Gate 0:** written capability decision recorded in this file (or a linked Gate 0 note) before any Gate 1+ work that prepares live-bound artifacts.

---

### Gate 1 — Pre-publication canonical build

Workbench / branch only until later gates authorize live placement.

- Transform staging → pre-publication canonical build (**not** raw copy) per `R2_7_REGISTRATION_DRAFT.md` §A.1.
- All 31 claims: `verified` → `publishable` only at this gate.
- `validity_state` remains `null` here — **not** `active` before publication.
- Clean `_meta` of workbench markers (`phase`, `html=BLOCKED`, `publish_gate=NOT OPEN`, staging location language, etc.).
- **No invented `merge_sha` / `release_sha`.**

---

### Gate 2 — Release HTML candidate

- Execute full §E.2 release-sanitization checklist.
- Remove all R2.6 / workbench / pre-publication chrome.
- Add/restore: live title/description, canonical, robots (`index, follow` only when publication completes), OG/Twitter, Article + Breadcrumb JSON-LD, page `dateModified` (independent of claim `last_verified_at`).
- Preserve without dilution: 31 anchors, four co-render pairs, Chapter V hierarchy, nine Decision Utility objects.
- Graph substance parity with Gate 1 build (§E.1).

---

### Gate 3 — Machine + registration package

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
- Fill `release_sha` / `merge_sha` only from **real** git objects after they exist (AI Act pattern)

---

### Gate 6 — Post-merge live verification

- Use the **real merge SHA**
- Verify live HTML, anchors, JSON, routes, llms, sitemap, and crawler/index behavior against Gate 0 decision
- RGS v2 re-score — target **≥ 90** before any Data Act / expansion work

---

## Hard rules while OPEN / BLOCKED AT GATE 0

| Rule | Status |
|---|---|
| Public `claims.json` | **FORBIDDEN** until Gate 3–5 sequence |
| Live GDPR HTML cutover | **FORBIDDEN** until Gate 2–5 sequence |
| Live `routes.json` / `llms.txt` / sitemap / robots mutation | **FORBIDDEN** until Gate 0 decision + Gate 3–5 |
| Claim promotion beyond `verified` | **FORBIDDEN** until Gate 1+ |
| Invented provenance SHAs | **FORBIDDEN** always |
| Opening PR content | Gates + DEC + status notes only |

---

## Exit of this opening PR

This opening PR may merge when it correctly:

1. Records DEC-054
2. Freezes the Gate 0→6 sequence above
3. Leaves execution blocked at Gate 0
4. Contains **no** live mutations

Next work after merge: execute **Gate 0** investigation and record the hosting/index-control decision.

---

*Workbench / governance artifact. Not a publication event.*
