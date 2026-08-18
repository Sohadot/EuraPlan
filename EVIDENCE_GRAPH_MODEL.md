# EVIDENCE_GRAPH_MODEL.md
**Version:** 1.1
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
an explicit evidence relation — not a single flat record.

This is the layer that makes a future API valuable (it exposes a graph, not
articles), makes AI extraction lossless (relationships are explicit, not inferred),
and makes EERS deltas computable (a change to a claim propagates to the EERS
dimensions it affects).

**Identity and lifecycle are governed separately** by
`CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md`; this document does not redefine
them. It defines the node/relation data and how the graph is exposed.

---

## 2. Three node/relation types

The graph is not a list of claim records. It has three parts:

| Type | Is | Cardinality |
|---|---|---|
| **Claim** | A single asserted planning-relevant proposition | — |
| **Source** | An official document/provision that can support claims | — |
| **Evidence relation** | A typed link: a source *supports / amends / clarifies* a claim | **many-to-many** |

One claim MAY rest on several sources (legislative text + a consolidated version +
Commission guidance); one source MAY support many claims. Modelling this as a
relation — rather than a single `source_url` on the claim — is what makes it a
graph.

---

## 3. The Claim node

| Field | Description |
|---|---|
| `id` | Opaque canonical identifier, e.g. `EP-CLM-000042` (see identity spec) |
| `display_label` | Non-authoritative human label, e.g. `AIA · Art. 113(3)` — never used in citations |
| `claim` | The single assertion, in one sentence |
| `jurisdiction` | e.g. `EU` |
| `actor` | Entry Ontology actor, e.g. `AI system provider` |
| `effective_date` | ISO date the proposition takes effect, if applicable |
| `sources` | Array of evidence relations (see §4) — **at least one** for any High-risk claim |
| `workflow_state` | `draft` … `published` \| `void` (identity spec §3.1) |
| `validity_state` | `active` \| `review_required` \| `superseded` \| `withdrawn` \| `corrected` (identity spec §3.2) |
| `confidence` | `Verified` \| `Referenced` \| `Pending` \| `Deprecated` (SOURCE_POLICY.md §5) |
| `claim_risk` | `Low` \| `Medium` \| `High` \| `Blocked` (CLAIM_POLICY.md §6) |
| `affected_eers_dimensions` | List of EERS dimension IDs the claim informs |
| `last_verified_at` | ISO date a human last verified the claim against its sources |
| `supersedes` / `superseded_by` / `corrects` / `corrected_by` | Chain pointers (identity spec §5–6) |
| `change_type` | `amendment` \| `interpretation` \| `correction` \| `withdrawal`, when applicable |

**Risk/tier coupling (from CLAIM_POLICY.md §6 + SOURCE_POLICY.md §2):** a `High`
claim — any regulatory deadline, compliance requirement, or funding eligibility —
MUST carry at least one Tier-1 source and MUST reach `confidence: Verified` before
`workflow_state: publishable`. A `Blocked` claim is never published.

---

## 4. The Source node and evidence relation

Each entry in a claim's `sources[]` is an evidence relation carrying its own source
node and a locator:

```json
{
  "source_id": "EP-SRC-000007",
  "instrument_id": "EU-2024-1689",
  "official_title": "Regulation (EU) 2024/1689 (Artificial Intelligence Act)",
  "celex": "32024R1689",
  "eli": "http://data.europa.eu/eli/reg/2024/1689/oj",
  "provision_locator": "Art. 113",
  "source_version_date": "YYYY-MM-DD",
  "retrieved_at": "YYYY-MM-DD",
  "source_tier": 1,
  "relationship": "supports"
}
```

`relationship` is one of `supports` | `amends` | `clarifies`. This is what lets the
graph express, for one claim, that the AI Act text *supports* it while a later
Commission guidance *clarifies* it — each with its own tier and retrieval date.

---

## 5. Canonical Claim node — machine form

Exposed both as an in-page `<script type="application/json">` block and, per
regulation, as a downloadable `/regulation/<slug>/claims.json`.

```json
{
  "id": "EP-CLM-000042",
  "display_label": "PLACEHOLDER · not a real provision",
  "claim": "PLACEHOLDER claim used to show schema shape only — carries no regulatory assertion.",
  "jurisdiction": "EU",
  "actor": "AI system provider",
  "effective_date": null,
  "sources": [
    {
      "source_id": "EP-SRC-000001",
      "instrument_id": "EU-0000-0000",
      "official_title": "PLACEHOLDER — replaced by a real Tier-1 source at verification",
      "celex": null,
      "eli": null,
      "provision_locator": "PLACEHOLDER",
      "source_version_date": null,
      "retrieved_at": null,
      "source_tier": 1,
      "relationship": "supports"
    }
  ],
  "workflow_state": "draft",
  "validity_state": null,
  "confidence": "Pending",
  "claim_risk": "High",
  "affected_eers_dimensions": ["DIM-01", "DIM-02"],
  "last_verified_at": null,
  "supersedes": null,
  "superseded_by": null,
  "change_type": null
}
```

> **This is a schema placeholder, not a claim.** It deliberately contains **no real
> regulation, article, or date**, so it cannot be mistaken for verified content. It
> is shown in the governance-correct state for an unverified High-risk claim:
> `workflow_state: draft`, `confidence: Pending`, `claim_risk: High` (a regulatory
> proposition is High per CLAIM_POLICY.md §6), and therefore **not publishable**
> until a human sets a real Tier-1 source and `last_verified_at`.

---

## 6. The Citation Unit (human form)

Every published claim renders on the page with a permanent anchor and a copy-ready
citation, so a researcher can quote a single fact, not a page.

- **Anchor:** `/regulation/eu-ai-act/#ep-clm-000042` — the opaque ID, stable per
  `AGENT_READABILITY_POLICY.md` §2; it does not change when the page is edited or
  when a locator is renumbered.
- **Citation format:**

  > EuraPlan. "EU AI Act — [claim summary]." `EP-CLM-000042`.
  > Verified [date]. https://euraplan.com/regulation/eu-ai-act/#ep-clm-000042

The visible rendering shows the claim, its source link(s), its `last_verified_at`
date, and its validity state — satisfying the visible-source requirement of
`AGENT_READABILITY_POLICY.md` §6 and the per-claim confidence/risk requirement of
`CONTENT_QUALITY_STANDARD.md` §2.

---

## 7. Page dates vs claim verification (do not conflate)

Two different dates exist and MUST be kept distinct:

- **Page last content update** — when the page's content/markup last changed. This
  is the value that `dateModified` (JSON-LD) and the visible "Last Updated" date
  mirror (`STRUCTURED_DATA_POLICY.md` §6).
- **Regulatory verification date** — the newest `last_verified_at` among the page's
  published claims.

A re-verification that confirms an unchanged claim advances the verification date
without changing the page content; an accessibility or wording edit advances the
content date without re-verifying anything. Merging the two would corrupt
provenance. See `FRESHNESS_ENGINE.md` §4.

---

## 8. How this feeds the paid layer (without paywalling truth)

The graph is public. The paid layer consumes it:

- **Change detection** watches `validity_state` / `last_verified_at` transitions.
- Each transition maps — via `affected_eers_dimensions` — to the EERS dimensions it moves.
- A subscriber's **Entry Profile** references a set of **profile archetypes**
  (e.g. `US · AI provider · high-risk`), not the company individually. A change is
  analyzed **once per archetype** and inherited by every profile in that archetype.

This archetype indirection keeps the Freshness Engine's cost sublinear in
subscriber count — the difference between a scalable product and a consultancy. It
is mandatory, not optional.

---

## 9. Prohibited

| Prohibited | Reason |
|---|---|
| A single `source_url` in place of the `sources[]` relation | Collapses the graph back to a flat record |
| A `High` claim with no Tier-1 source | Violates CLAIM_POLICY.md §6 / SOURCE_POLICY.md §2 |
| Setting `last_verified_at` without a human checking the primary source | Violates SOURCE_POLICY.md §4 and Doctrine §8 |
| A real-looking legal example that is not a verified claim | Risks mistaking illustration for verified content |
| Encoding a claim only in prose with no Claim node | Defeats machine retrieval |
| Putting graph data only behind JavaScript | Violates AGENT_READABILITY_POLICY.md §8 |

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
