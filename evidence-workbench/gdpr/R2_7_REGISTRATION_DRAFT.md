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
| Source | `evidence-workbench/gdpr/claims.canonical.staging.json` |
| Claim IDs | `EP-CLM-000015` … `EP-CLM-000045` (31) |
| `_meta.published` at staging | `false` |
| Promotion | Only under R2.8 rules (`verified` → `publishable` → `published` as governed) |

**R2.7 action:** none (file must not exist yet under `regulation/gdpr/`).

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

**R2.7 action:** draft only — do not edit live `routes.json`.

---

## C. Planned `llms.txt` exposure

Parallel to the AI Act claims entry, planned wording (R2.8 only):

```text
- [GDPR — canonical claim graph](https://euraplan.com/regulation/gdpr/claims.json): the machine-readable canonical claim graph for the GDPR reference page — governed Evidence Objects with opaque stable identifiers (`EP-CLM-*`), source/provision locators, qualification links, and verification dates. It mirrors the visible Verified Claim Register on `/regulation/gdpr/`. This is a static reference file, not an API, and implies no external endorsement.
```

**R2.7 action:** draft only — do not edit live `llms.txt`.

---

## D. Sitemap / robots

| Surface | Planned R2.8 rule |
|---|---|
| `claims.json` in sitemap | **No** |
| HTML `/regulation/gdpr/` | Already sitemap-listed; refresh `lastmod` only on substantive live cutover |
| robots | No special disallow required for `claims.json` if non-indexable via routes policy; do not invent new crawl rules without DEC |

---

## E. Live HTML cutover plan (R2.8)

| Step | Rule |
|---|---|
| Source | `evidence-workbench/gdpr/page-candidate/index.html` |
| Target | `regulation/gdpr/index.html` |
| Banner / robots | Remove workbench NOT LIVE / `noindex` only when Publish Gate completes |
| Citation anchors | Preserve `#ep-clm-000015` … `#ep-clm-000045` |
| Co-render / Chapter V / Decision Utility | Must survive cutover without dilution |
| Decision Utility JSON | Remains workbench-derived unless a later DEC publishes a separate machine layer |

---

## F. Explicit non-goals in this draft

- Publishing Decision Utility as a second truth graph
- Minting new `EP-CLM-*` for registration convenience
- Registering workbench paths as public routes
- Opening R2.8 from this document alone

---

*Draft artifact. Execution requires a separate R2.8 Publish Gate DEC.*
