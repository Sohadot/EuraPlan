# R2.8 Gate 6 — Post-merge Live Verification + RGS v2 Re-score

**Status:** COMPLETE / PASS — GDPR reference verified live; RGS v2 = **97.5 / 100** (≥ 90)
**Date:** 2026-08-23
**Scope:** Gate 6 — verify the live EP-REG-002 surfaces after publication, confirm the Gate 0 index-control decision on a live `200`, and re-score the route against `REFERENCE_GRADE_ROUTE_STANDARD.md` v2.
**Authorized by:** Gate 5 CLOSED / PASS (publication PR #47 `f97a51e`; Phase B provenance PR #48 `9faabcc`) under the DEC-054 frozen sequence
**Related:** `R2_8_PUBLISH_GATE.md`; `R2_8_GATE5_PUBLICATION.md`; `R2_8_GATE0_HOSTING_INDEX_CONTROL.md`; `governance/audits/REFERENCE_DEPTH_AUDIT_R1_2026-08-20.md`

---

## 1. Live index-control re-test (Gate 0 deferral resolved)

Gate 0 verified Option A against a pre-publication **404**; Gate 6 re-tests on a live **200**.

| URL | HTTP | `X-Robots-Tag` | Result |
|---|---|---|---|
| `https://euraplan.com/regulation/gdpr/claims.json` (target) | **200** | **`noindex`** | ✅ index control live on a real `200` (`content-type: application/json`, `server: cloudflare`) |
| `https://euraplan.com/regulation/gdpr/` (negative control) | **200** | **absent** | ✅ scope isolation holds live — rule is exact-path, not site-wide |

Cloudflare exact-path `X-Robots-Tag: noindex` (Gate 0 Option A, DEC-055) is confirmed on the live `200` response. `robots.txt` unchanged; `routes.json` `indexable:false` remains governance metadata only.

---

## 2. Live-surface integrity (all PASS)

Fetched from `https://euraplan.com` and compared to `main`:

- [x] `regulation/gdpr/claims.json` live is **byte-identical to `main`**; 31 claims `published` / `active`; `_meta.published=true`; provenance `release_sha=b392ba5`, `merge_sha=f97a51e`, `live_on_main_since=2026-08-23`; `last_verified_at=2026-08-20` unchanged
- [x] `regulation/gdpr/` HTML live: `robots = index, follow`; 31 claim anchors; 9 Decision Utility objects; 4 co-render blocks; `dateModified = 2026-08-23`; zero `publishable` labels
- [x] `routes.json` live: EP-REG-002 `alternate_representations` → `/regulation/gdpr/claims.json`; `last_updated = 2026-08-23`
- [x] `llms.txt` live: GDPR canonical-claim-graph line present
- [x] `sitemap.xml` live: `/regulation/gdpr/` `lastmod = 2026-08-23`; `claims.json` **not** listed
- [x] `robots.txt` live: unchanged (`Allow: /regulation/`)

---

## 3. RGS v2 re-score — 97.5 / 100

Scored per `REFERENCE_GRADE_ROUTE_STANDARD.md` §5 (8 dimensions × 12.5), same methodology as the Sprint R1 baseline audit. All six mandatory layers (L1–L6) are present and substantive; no hard-fail criterion triggered.

| Dimension | Layer | R1 baseline | **Gate 6 re-score** | Basis |
|---|---|---:|---:|---|
| Evidence depth | L2 | 8.0 | **12.5** | 31 Tier-1 claims; dual sources (OJ authentic act EP-SRC-000004 + consolidated reading aid EP-SRC-000005); provision locators |
| Unique information gain | L3 | 7.0 | **12.0** | Co-render qualification (Art 27(1)/(2); Art 30(5) <250; Art 33/34 breach exceptions); Chapter V as a hierarchy, not interchangeable options; controller/processor role model |
| Conceptual depth | L1 | 8.5 | **12.0** | Identity & scope; entry-into-force vs application distinction; Art 3 territorial reach |
| Decision utility | L4 | 8.0 | **12.0** | Nine Decision Utility objects `EP-DU-GDPR-001…009` (question / evidence / planning consequence / what-remains-fact-specific) |
| Citation readiness | L5 | 6.0 | **12.5** | 31 stable anchors `#ep-clm-000015…000045`; cite-by-claim-ID |
| Machine readability | L5 | 5.5 | **12.5** | Published canonical `claims.json` (published/active); Article + Breadcrumb JSON-LD; `routes.json` alternate; `llms.txt` exposure |
| Freshness | L6 | 6.5 | **12.0** | `last_verified_at=2026-08-20`; page `dateModified=2026-08-23`; freshness watch (Reg (EU) 2025/2518); provenance SHAs; maintenance contract |
| SEO semantics | — | 8.0 | **12.0** | Canonical + OG/Twitter; entity clarity; internal ontology links; real `lastmod`; `index, follow` |
| **Total** | | **58** | **97.5** | Parity with the EU AI Act Gold Reference (97); GDPR is now Evidence Graph-grade |

**Result: 97.5 / 100 ≥ 90.** GDPR Core Authority threshold met.

---

## 4. Gate 6 exit / R2.8 outcome

- [x] Live index control verified on a `200` (Gate 0 deferral resolved)
- [x] Live-surface integrity confirmed (HTML, JSON, routes, llms, sitemap, robots)
- [x] RGS v2 ≥ 90 (97.5)

**Gate 6 CLOSED / PASS. R2.8 GDPR Publish Gate COMPLETE — Gates 0–6 all CLOSED / PASS.**

### Expansion still gated
Per DEC-047, no new expansion routes open until **all** Wave 1 Core Authority routes reach ≥ 90. Wave 1 now has EU AI Act (97) + GDPR (97.5) at threshold; **Data Act, CRA, EERS, Protocol remain < 90**. No Data Act / country / sector / expansion work is unblocked by this closeout.

---

*Gate 6 live verification. R2.8 complete.*
