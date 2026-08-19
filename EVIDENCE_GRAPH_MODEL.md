# EVIDENCE_GRAPH_MODEL.md
**Version:** 1.3
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md, SOURCE_POLICY.md, CLAIM_POLICY.md, AGENT_READABILITY_POLICY.md, STRUCTURED_DATA_POLICY.md

---

## 1. Purpose

This policy converts EuraPlan's corpus from written prose into a **knowledge
graph**. Every material regulatory claim becomes a stable, addressable node with a
machine-readable representation, a human-readable rendering on the page, and a
permanent citation identity. Claims and sources are distinct node types joined by
explicit, typed edges — not a single flat record.

**Identity and lifecycle are governed separately** by
`CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md`. This document defines the
node/relation data, the canonical serialization, and how the graph is exposed.

### Changelog
- **v1.3** — Clarified §4.1: a single Source MAY carry multiple typed edges (e.g. `supports` + `amends`) to the same Claim when it performs both functions. No structural change; closes an ambiguity found on first real application.
- **v1.2** — Normalized serialization made canonical (§4): Source nodes live once in a source registry; edges carry no `source_tier`. Added Claim→Claim `qualified_by` relation (§3.1). Froze `amends` semantics (§4.1). Added append-only source rule and a forward date-field split (§4.2).
- **v1.1** — Introduced the many-to-many Claim↔Source relation and opaque identity.

---

## 2. Node and relation types

The graph has two node types and two relation families:

| Element | Is | Cardinality |
|---|---|---|
| **Claim** node | A single asserted planning-relevant proposition | — |
| **Source** node | An official document/provision that can support claims | — |
| **Claim→Source** edge | A source *supports / amends / clarifies* a claim | many-to-many |
| **Claim→Claim** edge | A claim *qualifies* another claim (e.g. an exception to a default) | many-to-many |

One claim MAY rest on several sources; one source MAY support many claims; one
source MAY carry more than one edge to the *same* claim (§4.1). One claim MAY be
qualified by several others. Modelling these as edges — not as fields baked into a
single record — is what makes it a graph.

---

## 3. The Claim node

| Field | Description |
|---|---|
| `id` | Opaque canonical identifier, e.g. `EP-CLM-000042` (see identity spec) |
| `display_label` | Non-authoritative human label — never used in citations |
| `claim` | The single assertion, in one sentence |
| `jurisdiction` | e.g. `EU` |
| `actor` | Entry Ontology actor, or `null` for non-actor-scoped facts |
| `effective_date` | ISO date the proposition takes effect, or `null` |
| `sources` | Array of Claim→Source **edges** (see §4) — at least one for any High-risk claim |
| `qualified_by` | Array of Claim IDs that qualify this claim (see §3.1); `null` if none |
| `workflow_state` | `draft` … `published` \| `void` (identity spec §3.1) |
| `validity_state` | `active` \| `review_required` \| `superseded` \| `withdrawn` \| `corrected` (identity spec §3.2) |
| `confidence` | `Verified` \| `Referenced` \| `Pending` \| `Deprecated` (SOURCE_POLICY.md §5) |
| `claim_risk` | `Low` \| `Medium` \| `High` \| `Blocked` (CLAIM_POLICY.md §6) |
| `affected_eers_dimensions` | List of EERS dimension IDs the claim informs |
| `last_verified_at` | ISO date a human last verified the claim against its sources |
| `supersedes` / `superseded_by` / `corrects` / `corrected_by` | Chain pointers (identity spec §5–6) |
| `change_type` | `amendment` \| `interpretation` \| `correction` \| `withdrawal`, when applicable |

**Risk/tier coupling (CLAIM_POLICY.md §6 + SOURCE_POLICY.md §2):** a `High` claim
MUST carry at least one Tier-1 source and MUST reach `confidence: Verified` before
`workflow_state: publishable`. A `Blocked` claim is never published.

### 3.1 Claim→Claim: `qualified_by`

`qualified_by` records that another claim **narrows, excepts, or conditions** this
one. It exists so that a claim which is safe in isolation is never quoted without
its exception attached.

- `qualified_by` is **directional** and stored on the qualified claim only. Its
  inverse (`qualifies`) is **derived**, not stored — storing both invites drift.
- Example: a "default application date" claim is `qualified_by` an "exception
  applies from a later date" claim. A retrieval agent reading the default MUST be
  able to follow the edge to the exception.
- A `qualified_by` edge is **not** supersession. Both claims are simultaneously
  true; one bounds the other. Supersession (identity spec §5) replaces a claim
  across time; qualification bounds a claim at the same point in time.

---

## 4. Source nodes and the canonical serialization

**Canonical serialization is normalized.** Source nodes are stored **once**, in a
`source_registry` (in the per-regulation claims file's `_meta`). Each claim's
`sources[]` entry is an **edge** that references a registry node by `source_id` and
adds only edge-local data:

```json
"sources": [
  { "source_id": "EP-SRC-000002",
    "provision_locator": "Article 1, point (40)(b) (replaces Article 113 third paragraph point (c))",
    "relationship": "amends" }
]
```

A Source **node** in the registry carries the source's own properties:

```json
"EP-SRC-000001": {
  "instrument_id": "EU-2024-1689",
  "official_title": "Regulation (EU) 2024/1689 … (Artificial Intelligence Act)",
  "celex": "32024R1689",
  "eli": "http://data.europa.eu/eli/reg/2024/1689/oj",
  "source_version_date": "2024-07-12",
  "retrieved_at": "2026-08-19",
  "source_tier": 1
}
```

**`source_tier` is a property of the Source node only.** It MUST NOT be duplicated
onto the edge — a node property carried in two places drifts. Edges carry exactly
`source_id`, `provision_locator`, and `relationship`.

### 4.1 `relationship` values (frozen semantics)

| Value | Meaning |
|---|---|
| `supports` | The source substantiates the claim's proposition. |
| `amends` | The source **changes or replaces the operative legal basis on which the claim rests** — *even if the claim's value is unchanged.* `amends` does **not** assert that the claim's value changed; it asserts that the carrying provision was altered. |
| `clarifies` | The source (e.g. official guidance) interprets or explains the claim without changing the operative provision. |

> Worked case: a date that did not change but whose carrying point was rewritten by
> an amendment carries **both** a `supports` edge to the original instrument and an
> `amends` edge to the amending instrument. The `amends` edge does not imply the
> date moved — only that the legal basis was replaced.

**Dual-role edges.** A single Source MAY carry **multiple typed edges to the same
Claim** when it performs two functions at once — e.g. it both substantiates the
proposition (`supports`) and changes the operative legal basis on which the claim
rests (`amends`). This is the correct encoding whenever an amending instrument is
itself the source that states the claim's current value: the `supports` edge
records that the value lives in that instrument, and the `amends` edge records that
it replaced or added the carrying provision. A `High` claim whose current value
originates in an amending instrument MUST carry a `supports` edge to that
instrument — an `amends` edge alone does not substantiate a proposition.

### 4.2 Source append-only rule and date fields

- Source nodes are **append-only**, like claims. When EUR-Lex publishes a **new
  consolidated version**, add a **new** Source node (e.g. `EP-SRC-000003`) for it;
  **never rewrite** an existing node (e.g. do not retro-fit a 2026 consolidation
  date onto the 2024 OJ node). Amended claims draw current-law provenance from the
  original node (`supports`) plus the amending node (`amends` and, where it states
  the current value, also `supports`) together.
- **Forward refinement (recommended):** `source_version_date` currently overloads
  several meanings. Future source nodes SHOULD split it into `document_date` (the
  act's own date), `publication_date` (OJ date), and `consolidated_as_of` (the
  consolidation snapshot date), rather than a single overloaded field.

---

## 5. Canonical Claim node — machine form (normalized)

```json
{
  "id": "EP-CLM-000003",
  "display_label": "AI Act · Art. 113(3)(a) · Chapters I & II",
  "claim": "The default application date for Chapters I and II of Regulation (EU) 2024/1689 is 2 February 2025.",
  "jurisdiction": "EU",
  "actor": null,
  "effective_date": "2025-02-02",
  "sources": [
    { "source_id": "EP-SRC-000001", "provision_locator": "Article 113, third paragraph, point (a)", "relationship": "supports" },
    { "source_id": "EP-SRC-000002", "provision_locator": "Article 1, point (40)(a) (amended point (a) retains 2 February 2025)", "relationship": "supports" },
    { "source_id": "EP-SRC-000002", "provision_locator": "Article 1, point (40)(a) (replaces Article 113 third paragraph point (a))", "relationship": "amends" }
  ],
  "qualified_by": ["EP-CLM-000006"],
  "workflow_state": "pending_verification",
  "validity_state": null,
  "confidence": "Pending",
  "claim_risk": "High",
  "affected_eers_dimensions": ["DIM-01", "DIM-02"],
  "last_verified_at": null,
  "supersedes": null, "superseded_by": null, "corrects": null, "corrected_by": null, "change_type": null
}
```

The Source nodes referenced by `source_id` live once in `_meta.source_registry`.

---

## 6. The Citation Unit (human form)

Every published claim renders with a permanent anchor and a copy-ready citation, so
a researcher can quote a single fact, not a page.

- **Anchor:** `/regulation/eu-ai-act/#ep-clm-000003` — the opaque ID, stable per
  `AGENT_READABILITY_POLICY.md` §2; unchanged when the page is edited or a locator
  is renumbered.
- A claim rendered with a `qualified_by` edge MUST render its qualification
  visibly alongside it — never the default without its exception.

---

## 7. Page dates vs claim verification (do not conflate)

- **Page last content update** — mirrors `dateModified` (JSON-LD) and the visible
  "Last Updated" date (`STRUCTURED_DATA_POLICY.md` §6).
- **Regulatory verification date** — the newest `last_verified_at` among the page's
  published claims.

Merging them corrupts provenance. See `FRESHNESS_ENGINE.md` §4.

---

## 8. How this feeds the paid layer (without paywalling truth)

The graph is public. The paid layer consumes it: change detection watches
`validity_state` / `last_verified_at` transitions; each maps via
`affected_eers_dimensions` to the dimensions it moves; a subscriber's Entry Profile
references **profile archetypes**, not the company individually, so a change is
analyzed once per archetype and inherited. This keeps the Freshness Engine's cost
sublinear in subscriber count.

---

## 9. Prohibited

| Prohibited | Reason |
|---|---|
| A flat `source_url`/`source_tier` on a claim in place of the registry+edge model | Collapses the graph and duplicates node properties |
| Duplicating `source_tier` (or other node properties) onto an edge | Drifts against the registry node |
| Rewriting an existing Source node for a new consolidation | Violates the append-only rule |
| A `High` claim whose current value comes from an amending instrument carrying only an `amends` edge to it | `amends` does not substantiate; a `supports` edge is required (§4.1) |
| A `High` claim with no Tier-1 source | Violates CLAIM_POLICY.md §6 / SOURCE_POLICY.md §2 |
| Setting `last_verified_at` without a human checking the primary source | Violates SOURCE_POLICY.md §4 and Doctrine §8 |
| Encoding a claim, or a Claim→Claim qualification, only in prose | Defeats machine retrieval; risks quoting a default without its exception |
| A real-looking legal example that is not a verified claim | Risks mistaking illustration for verified content |

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
