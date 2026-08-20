# R2.7 — Registration Draft (not applied)

**Status:** DRAFT ONLY — do not execute on live files in R2.7  
**Target phase for execution:** R2.8 Publish Gate  
**Pattern source:** EP-REG-001 (`/regulation/eu-ai-act/claims.json`) + DEC-045 lineage

---

## A. Planned public machine file

| Field | Planned value |
|---|---|
| Path | `/regulation/gdpr/claims.json` |
| Repo file | `regulation/gdpr/claims.json` |
| Source | `evidence-workbench/gdpr/claims.canonical.staging.json` via the **§A.1 transformation contract** |
| Claim IDs | `EP-CLM-000015` … `EP-CLM-000045` (31) |
| `_meta.published` at staging | `false` |
| Promotion | Only under R2.8 rules; no stage skipping |

**R2.7 action:** none (file must not exist yet under `regulation/gdpr/`).

### A.1 Staging → public canonical transformation contract

R2.8 must produce public `regulation/gdpr/claims.json` by transforming staging — **not** by copying the workbench file verbatim.

#### Claim-level transitions (all 31; no jumps)

| Field | Staging (now) | Public (R2.8 required) |
|---|---|---|
| `workflow_state` | `verified` | `verified` → `publishable` → `published` in governed order only |
| `validity_state` | `null` | `active` at publication (`null` → `active` only) |
| `confidence` | `Verified` | unchanged unless a new verification event occurs |
| `last_verified_at` | `2026-08-20` | **retain** unless a fresh literal re-verification is recorded |
| Proposition / sources / `qualified_by` / `related_claims` / IDs | frozen verified graph | unchanged by publication housekeeping |

#### `_meta` transformation (workbench markers must not ship as public truth)

| Staging marker / field | Public rule |
|---|---|
| `published: false` | → `true` |
| `phase: R2.4` (or any sprint-phase label) | **remove** or replace with publication-status wording |
| `html: BLOCKED` | **remove** |
| `publish_gate: NOT OPEN` | replace with closed/pass publication record after R2.8 completes |
| `routes_json_alternate` / `llms_txt` / `sitemap` "NOT YET" markers | **remove**; live registration is evidenced by actual `routes.json` / `llms.txt` / sitemap state |
| `batch` / `status` / `location_note` workbench language | rewrite to AI Act–parallel **published / active — live on main** language |
| `target_public_path` / staging-only prep notes | drop or convert to factual location note for the live file |
| `co_render_blocking_pairs` / `chapter_v_related_hierarchy` | may remain as publication integrity notes if still accurate |
| `source_registry` | retain |
| `governed_by` | retain + add R2.8 Publish Gate DEC when issued |

#### Publication provenance (required; do not invent early)

Mirror AI Act public `_meta` fields:

| Field | Rule |
|---|---|
| `release_sha` | Set only when the R2.8 release commit exists |
| `merge_sha` | Set only when the R2.8 merge to `main` exists |
| `live_on_main_since` | Set to the actual publication date |
| `published` | `true` only after the governed promotion completes |

**Hard rule:** R2.7 must **not** invent, placeholder-fake, or pre-write `release_sha` / `merge_sha`. Those are filled at R2.8 execution time from real git objects, following the AI Act pattern (`release_sha` + `merge_sha` on the public graph).

---

## B. Planned `routes.json` alternate on EP-REG-002

Current EP-REG-002 has **no** `alternate_representations`. Planned addition (R2.8 only):

```json
"alternate_representations": [
  {
    "path": "/regulation/gdpr/claims.json",
    "media_type": "application/json",
    "role": "canonical_claim_graph",
    "canonical_parent": "/regulation/gdpr/",
    "indexable": false,
    "sitemap": false
  }
]
```

**Meaning of `indexable: false`:** this is **governance metadata** in the route registry (`ROUTE_GOVERNANCE.md`: alternate machine representations are not independently indexable and not sitemap entries). It is **not** an HTTP header, **not** a robots directive, and **not** crawler enforcement by itself.

**R2.7 action:** draft only — do not edit live `routes.json`.

---

## C. Planned `llms.txt` exposure

Parallel to the AI Act claims entry, planned wording (R2.8 only):

```text
- [GDPR — canonical claim graph](https://euraplan.com/regulation/gdpr/claims.json): the machine-readable canonical claim graph for the GDPR reference page — governed Evidence Objects with opaque stable identifiers (`EP-CLM-*`), source/provision locators, qualification links, and verification dates. It mirrors the visible Verified Claim Register on `/regulation/gdpr/`. This is a static reference file, not an API, and implies no external endorsement.
```

**R2.7 action:** draft only — do not edit live `llms.txt`.

---

## D. Sitemap / robots / crawl reality

| Surface | Planned R2.8 rule |
|---|---|
| `claims.json` in sitemap | **No** |
| HTML `/regulation/gdpr/` | Already sitemap-listed; refresh `lastmod` only on substantive live cutover |
| `routes.json` `indexable:false` | Governance intent only — does **not** stop crawlers |
| Current `robots.txt` | Explicitly `Allow: /regulation/` — therefore `/regulation/gdpr/claims.json` will be **technically crawlable** when the file exists unless R2.8 adds a separate crawler-control measure |

### D.1 Crawler / indexing decision required at R2.8 (not assumed here)

R2.8 must choose and record an explicit mechanism based on **hosting capability**, for example one of:

1. Add a precise `robots.txt` disallow for the claims machine path (if policy accepts it), **or**
2. Serve `X-Robots-Tag: noindex` (or equivalent) for `claims.json` at the host/CDN layer, **or**
3. Accept crawlability while keeping governance non-indexable + sitemap exclusion, with that acceptance stated in the Publish Gate DEC

**Hard rule:** Do **not** assume that `routes.json` metadata enforces crawler behavior. Do **not** invent a hosting capability that is not verified at R2.8 time.

---

## E. Live HTML cutover — release-sanitization checklist (R2.8)

| Step | Rule |
|---|---|
| Source | `evidence-workbench/gdpr/page-candidate/index.html` |
| Target | `regulation/gdpr/index.html` |
| Content preserve | Keep `#ep-clm-000015`…`#ep-clm-000045`, four co-render pairs, Chapter V hierarchy, nine Decision Utility objects |
| Decision Utility JSON | Remains workbench-derived unless a later DEC publishes a separate machine layer |

### E.1 Citation / content parity contract (candidate → live)

The live page must remain citation-equivalent to the approved candidate for:

1. All 31 claim anchors and register propositions  
2. Co-render pairing for 024↔025, 032↔033, 035↔036, 037↔038  
3. Chapter V pathway framing `44 -> 45 -> 46 -> 49` (not equal options)  
4. Decision Utility objects `EP-DU-GDPR-001`…`009` with claim-ID traceability  
5. No new legal propositions introduced during sanitization  

Sanitization may change **release chrome** (title, meta, banners, telemetry labels, footer). It must not change **graph substance**.

### E.2 R2.8 HTML release-sanitization checklist

Candidate currently lacks live publication chrome; live GDPR page currently has it. R2.8 cutover **fails** unless all of the following are completed:

| # | Requirement | Candidate now | Live now | R2.8 action |
|---|---|---|---|---|
| 1 | Live `<title>` | `... (R2.6 workbench) ...` | `GDPR Entry Planning Reference — EuraPlan` (or Evidence Graph–grade successor title approved at gate) | Replace workbench title with live publication title |
| 2 | Live meta description | Says not live / workbench candidate | Public planning-reference description | Rewrite for published Evidence Graph reference; no "not live" language |
| 3 | Canonical URL | missing | `https://euraplan.com/regulation/gdpr/` | Add canonical |
| 4 | Robots | `noindex, nofollow` | `index, follow` | Set `index, follow` only at Publish Gate completion |
| 5 | Open Graph tags | missing | `og:title/description/type/url/image/site_name` present | Restore OG set aligned to published title/description |
| 6 | Twitter card tags | missing | present | Restore Twitter set |
| 7 | Article JSON-LD | missing | present with `dateModified` | Add Article JSON-LD |
| 8 | Breadcrumb JSON-LD | missing | present | Add BreadcrumbList JSON-LD |
| 9 | `dateModified` semantics | n/a / claim verification date elsewhere | page `dateModified` on Article | Set **page-update** `dateModified` to the R2.8 publication/cutover date; do **not** conflate with claim `last_verified_at` |
| 10 | NOT LIVE / workbench banner | present | absent | Remove entirely |
| 11 | Telemetry / phase labels | `Route target (later)`, `Phase: R2.6`, pre-publication badges | live route telemetry | Replace with published EP-REG-002 telemetry; remove sprint-phase and "later" wording |
| 12 | Hero / badge candidate language | candidate / pre-publication | published reference | Remove candidate/pre-publication labels; use published workflow labels |
| 13 | Visible claim workflow labels | `verified (pre-publication)` | must become published-state labels | Update visible labels to match published claim states |
| 14 | Footer workbench disclaimer | "Workbench page candidate only..." | standard public disclaimer | Remove workbench-only footer; keep standard non-advice / verify-at-EUR-Lex public disclaimer |
| 15 | Nav parity | missing Acquire link vs live | includes Acquire | Align header nav with current live site chrome unless a DEC changes global nav |
| 16 | Favicon parity | svg only | svg + png | Match live favicon set |

**Hard fail if cutover is a raw copy** of `page-candidate/index.html` without completing §E.2.

---

## F. Explicit non-goals in this draft

- Publishing Decision Utility as a second truth graph
- Minting new `EP-CLM-*` for registration convenience
- Registering workbench paths as public routes
- Opening R2.8 from this document alone
- Inventing `release_sha` / `merge_sha` before they exist
- Assuming `routes.json` `indexable:false` enforces crawlers

---

*Draft artifact. Execution requires a separate R2.8 Publish Gate DEC.*
