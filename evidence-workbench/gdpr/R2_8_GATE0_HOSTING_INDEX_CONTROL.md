# R2.8 Gate 0 — Hosting & Index-Control Investigation

**Status:** INVESTIGATION COMPLETE / OWNER DECISION REQUIRED  
**Date:** 2026-08-20  
**Scope:** Gate 0 only — no Gates 1–6 execution  
**Related:** DEC-054; `R2_8_PUBLISH_GATE.md`; `R2_7_REGISTRATION_DRAFT.md` §D.1

---

## 1. Serving stack (verified)

Request path for `https://euraplan.com/` and existing machine JSON:

`Client → Cloudflare (DNS + reverse proxy) → GitHub Pages origin (Fastly edge markers) → repo publish from main`

| Layer | Evidence | Role |
|---|---|---|
| DNS NS | `serena.ns.cloudflare.com`, `brodie.ns.cloudflare.com` | Cloudflare authoritative DNS |
| Apex / www A | `104.21.58.180`, `172.67.162.106` (Cloudflare anycast) | Cloudflare-proxied |
| HTTP `Server` | `cloudflare` | Edge terminates TLS / proxy |
| Cloudflare markers | `CF-Ray`, `cf-cache-status`, `cf-nel` | Active CF edge |
| Origin markers | `X-GitHub-Request-Id`, `x-github-edge-region`, `x-fastly-request-id`, `Via: 1.1 varnish` | GitHub Pages origin behind CF |
| Pages API | `status=built`, `cname=euraplan.com`, `source.branch=main`, `source.path=/` | Pages publishes from `main` root |
| Repo | `has_pages=true`, `CNAME=euraplan.com` | Matches live domain |

**Conclusion:** Not GitHub Pages alone. Production is **Cloudflare-proxied GitHub Pages**.

---

## 2. Path-specific `X-Robots-Tag` capability

### 2.1 GitHub Pages alone

**Not capable** of arbitrary per-path custom response headers for standard github.io / Pages sites. Repo `_headers` conventions (Netlify / Cloudflare Pages) are **inert** on GitHub Pages.

### 2.2 Cloudflare edge (present on this site)

**Capable in principle** via Cloudflare dashboard controls (e.g. Transform Rules / HTTP Response Header Modification) to attach:

`X-Robots-Tag: noindex`

to URI path `/regulation/gdpr/claims.json` (and optionally the AI Act twin path later under a separate DEC).

### 2.3 Live verification (current state)

Probed 2026-08-20 (HEAD requests):

| URL | `X-Robots-Tag` |
|---|---|
| `https://euraplan.com/` | **absent** |
| `https://euraplan.com/regulation/gdpr/` | **absent** |
| `https://euraplan.com/regulation/eu-ai-act/claims.json` | **absent** |

**Conclusion:** Path-specific index-control header is **possible at Cloudflare**, but **not currently configured**. Capability is not proven as "already live"; it requires an explicit Cloudflare operator action + post-config curl verification.

### 2.4 Crawl vs index (required distinction)

| Control | Mechanism | What it does |
|---|---|---|
| Crawl control | `robots.txt` `Disallow` | Asks compliant crawlers not to fetch; does **not** guarantee `noindex` |
| Index control | `X-Robots-Tag: noindex` (preferred) | Instructs indexers after fetch; preferred for non-HTML JSON |
| Governance | `routes.json` `indexable:false` + no sitemap entry | Registry intent only — not enforcement |

Current `robots.txt` has `Allow: /regulation/`, so a future `/regulation/gdpr/claims.json` is **technically crawlable** unless Gate 0 chooses otherwise.

---

## 3. Decision options (owner must pick one)

### Option A — Preferred (index control)

1. Configure Cloudflare Transform Rule (or equivalent) for  
   `https://euraplan.com/regulation/gdpr/claims.json` → `X-Robots-Tag: noindex`
2. Keep file **crawlable** enough for crawlers to see the header (do **not** Disallow the path if relying on `X-Robots-Tag`)
3. Keep `claims.json` out of sitemap; keep `routes.json` `indexable:false`
4. Verify with `HEAD`/`GET` that the header is present before Gate 5 publication
5. Record PASS only after live header verification

### Option B — Crawl control fallback

1. Add precise `robots.txt` `Disallow` for `/regulation/gdpr/claims.json` (and only that path unless separately decided)
2. Keep sitemap exclusion + governance `indexable:false`
3. Explicitly accept that this is **crawl guidance**, not guaranteed index control
4. Residual risk: URL may still appear in results if discovered via links without a revisit that honors Disallow/noindex semantics

### Option C — Accept crawlability

1. No robots Disallow; no `X-Robots-Tag`
2. Sitemap exclusion + governance `indexable:false` only
3. Explicit acceptance that the machine graph is crawlable/indexable by technical HTTP reality

---

## 4. Gate 0 status

| Item | State |
|---|---|
| Serving stack identified | **PASS** |
| GH Pages header capability alone | **FAIL** (as sole mechanism) |
| Cloudflare path-specific `X-Robots-Tag` | **CAPABLE / NOT CONFIGURED** |
| Owner decision among A/B/C | **PENDING** |
| Gate 0 overall | **BLOCKED** until owner selects and (for A) verifies header live |

**Gates 1–6 remain forbidden** until Gate 0 records a chosen option and any required verification.

---

## 5. Non-goals of this note

- No public `claims.json`
- No live HTML cutover
- No `routes.json` / `llms.txt` / sitemap / robots mutations in the investigation PR unless Option B is chosen later in a dedicated Gate 0 closeout change
- No Cloudflare dashboard mutation from this repo PR (Transform Rules are outside git)

---

*Workbench investigation only. Not a publication event.*
