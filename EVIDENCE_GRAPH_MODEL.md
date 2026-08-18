# EVIDENCE_GRAPH_MODEL.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, SOURCE_POLICY.md, CLAIM_POLICY.md, AGENT_READABILITY_POLICY.md, STRUCTURED_DATA_POLICY.md

---

## 1. Purpose

This policy converts EuraPlan's corpus from written prose into a **knowledge
infrastructure**. Every material regulatory claim becomes a stable, addressable
**Evidence Object** with a machine-readable representation, a human-readable
rendering on the page, and a permanent citation identity.

This is the layer that makes a future API valuable (it wraps structured evidence,
not articles), makes AI extraction lossless (relationships are explicit, not
inferred), and makes EERS deltas computable (a change to an Evidence Object
propagates to the EERS dimensions it affects).

---

## 2. The Evidence Object

Each high-value claim is assigned a stable Evidence ID and the following fields.
The ID never changes once assigned, even if the claim is later superseded.

| Field | Description | Source of truth |
|---|---|---|
| `id` | Stable claim identifier, e.g. `EP-CLAIM-AIA-113-001` | Assigned once, permanent |
| `claim` | The single assertion, in one sentence | Page author |
| `jurisdiction` | e.g. `EU` | Ontology |
| `regulation` | Regulation identifier, e.g. `EU-2024-1689` | `STRUCTURED_DATA_POLICY.md` §10 |
| `article` | Provision reference, e.g. `Art. 113(3)` | Primary source |
| `actor` | Ontology actor, e.g. `AI system provider` | Entry Ontology |
| `effective_date` | ISO date the provision applies, if applicable | Primary source |
| `source_url` | Official source URL (EUR-Lex preferred) | `SOURCE_POLICY.md` |
| `source_tier` | `1` \| `2` | `SOURCE_POLICY.md` |
| `verified_at` | ISO date a human last verified against source | Verification step |
| `status` | `active` \| `superseded` \| `withdrawn` | Freshness Engine |
| `supersedes` | ID of the claim this one replaces, if any | Change control |
| `superseded_by` | ID of the claim that replaced this one, if any | Change control |
| `affected_eers_dimensions` | List of EERS dimension IDs the claim informs | `EERS_1.0_SPECIFICATION.md` |
| `claim_risk` | `Low` \| `Medium` \| `High` \| `Blocked` | `CLAIM_POLICY.md` |

### Evidence ID grammar

```
EP-CLAIM-<REG>-<ARTICLE>-<SEQ>
             │      │        └─ zero-padded sequence within the article
             │      └────────── article number (no punctuation)
             └───────────────── regulation short code (AIA, GDPR, DATA, CRA, …)
```

Example: `EP-CLAIM-AIA-113-003` — the third distinct claim EuraPlan makes about
Article 113 of the EU AI Act.

---

## 3. Canonical Evidence Object — machine form

Each reference page carries an evidence array as JSON-LD-adjacent data. It is
exposed both as an in-page `<script type="application/json">` block and, per
regulation, as a downloadable `/regulation/<slug>/claims.json`.

```json
{
  "id": "EP-CLAIM-AIA-113-003",
  "claim": "GPAI model obligations under the EU AI Act apply from 2 August 2025.",
  "jurisdiction": "EU",
  "regulation": "EU-2024-1689",
  "article": "Art. 113(2)",
  "actor": "GPAI model provider",
  "effective_date": "2025-08-02",
  "source_url": "https://eur-lex.europa.eu/eli/reg/2024/1689/oj",
  "source_tier": 1,
  "verified_at": "2026-08-18",
  "status": "active",
  "supersedes": null,
  "superseded_by": null,
  "affected_eers_dimensions": ["DIM-01", "DIM-02"],
  "claim_risk": "Medium"
}
```

> **Illustrative structure only.** The `effective_date` and `article` values in
> this example are not published as verified until Sprint 2 re-verifies them
> against the primary source and sets a real `verified_at`.

---

## 4. The Citation Unit (human form)

Every Evidence Object renders on the page with a permanent anchor and a
copy-ready citation, so a researcher can quote a single fact, not a page.

- **Anchor:** `/regulation/eu-ai-act/#ep-claim-aia-113-003` — stable per
  `AGENT_READABILITY_POLICY.md` §2; it does not change when the page is edited.
- **Citation format:**

  > EuraPlan. "EU AI Act — GPAI obligation timeline." `EP-CLAIM-AIA-113-003`.
  > Verified 18 Aug 2026. https://euraplan.com/regulation/eu-ai-act/#ep-claim-aia-113-003

The visible rendering shows the claim, its article, its source link, its
`verified_at` date, and its status — satisfying the visible-source requirement of
`AGENT_READABILITY_POLICY.md` §6 and the per-claim confidence/risk requirement of
`CONTENT_QUALITY_STANDARD.md` §2.

---

## 5. Versioning and the historical record

Regulatory truth changes. EuraPlan never deletes history — it supersedes it.

- When a claim changes, a **new** Evidence Object is created with a new `SEQ`.
- The prior object's `status` becomes `superseded`, its `superseded_by` is set,
  and it remains addressable at its original anchor.
- The new object's `supersedes` points back to the prior ID.

This produces a durable **amendment history**, which answers a question ordinary
regulatory summaries cannot: *what was expected in March 2026, and what changed
later?* That historical record is itself a citable asset for researchers,
journalists, and economists.

---

## 6. How this feeds the paid layer (without paywalling truth)

The Evidence Graph is public. The paid layer consumes it:

- **Change detection** watches `verified_at` / `status` transitions across the graph.
- Each transition maps — via `affected_eers_dimensions` — to the EERS dimensions it moves.
- A subscriber's **Entry Profile** references a set of **profile archetypes**
  (e.g. `US · AI provider · high-risk`), not the company individually. A change is
  analyzed **once per archetype** and inherited by every profile in that archetype.

This archetype indirection is the architectural rule that keeps the Freshness
Engine's cost sublinear in subscriber count — the difference between a scalable
product and a consultancy. It is mandatory, not optional.

---

## 7. Prohibited

| Prohibited | Reason |
|---|---|
| Reusing an Evidence ID for a different claim | Breaks the historical record and citations |
| Deleting a superseded object | Destroys the amendment history |
| Setting `verified_at` without a human checking the primary source | Violates `SOURCE_POLICY.md` and §8 of the Doctrine |
| `source_tier: 1` on a non-primary source | Source integrity violation |
| Encoding a claim only in prose with no Evidence Object | Defeats machine retrieval |
| Putting Evidence data only behind JavaScript | Violates `AGENT_READABILITY_POLICY.md` §8 |

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
