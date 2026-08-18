# FRESHNESS_ENGINE.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, SOURCE_POLICY.md, CONTENT_QUALITY_STANDARD.md, EVIDENCE_GRAPH_MODEL.md

---

## 1. Why freshness is infrastructure, not a feature

For a reference asset, a stale or incorrect regulatory fact does not merely age —
it destroys the trust the asset exists to hold. Freshness is therefore the single
existential obligation of EuraPlan, and it is also the thing the paid layer sells:
the same maintenance work that keeps the public reference correct produces the
per-archetype signal that the Entry Monitor delivers.

`CONTENT_QUALITY_STANDARD.md` §7 sets a six-month rolling review. Under this
document, six months is the **backstop maximum**, not the operating cadence. The
operating cadence is event-driven.

---

## 2. The pipeline

Every material change to EU regulatory reality flows through seven stages before
it reaches a reader or a subscriber:

```
Official Source Registry
        │
        ▼
Change Detection ──► Human Verification ──► Claim Impact Analysis
                                                    │
                                                    ▼
                          Corpus Update ──► Changelog ──► Subscriber Delta
```

| Stage | What happens | Output |
|---|---|---|
| **Source Registry** | Maintain the list of official sources per regulation (EUR-Lex ELI, Commission pages, agency guidance) | `sources/registry` |
| **Change Detection** | Monitor registered sources for amendment, new guidance, or a passing enforcement date | Candidate change |
| **Human Verification** | A person confirms the change against the primary source | Verified change |
| **Claim Impact Analysis** | Identify which Evidence Objects and EERS dimensions the change moves | Impacted `EP-CLAIM-*` list |
| **Corpus Update** | Supersede affected Evidence Objects; set new `verified_at` | Updated corpus |
| **Changelog** | Record the change with triggering event and date | Public changelog entry |
| **Subscriber Delta** | Emit EERS Deltas to affected profile archetypes | Paid signal |

---

## 3. Verification SLA

| Trigger | Verify + changelog within |
|---|---|
| An enforcement or phase date passes | 3 business days |
| A cited regulation is amended | 5 business days |
| Official guidance materially changes a claim | 10 business days |
| Routine backstop review (no trigger) | 6 months |

A claim whose `verified_at` is older than its trigger SLA is flagged `stale` in
tooling and MUST NOT carry a `Verified` confidence badge until re-checked.

---

## 4. The date-integrity rule

A `Last Updated` or `verified_at` date is a claim of verification, and is governed
as one.

- A date MUST only be advanced when a human has re-verified the underlying claim
  against its primary source.
- Advancing a date to *simulate* freshness — without re-verification — is a
  governance breach equal to publishing an unsourced statistic.
- `dateModified` in JSON-LD MUST equal the visible `Last Updated` date
  (`STRUCTURED_DATA_POLICY.md` §6). Both derive from the newest `verified_at`
  among the page's Evidence Objects.

---

## 5. Standing obligation on the live corpus

The indexed site carries a `June 2026` stamp and an AI Act timeline predating
recent developments. Under §4, the remedy is **not** to bump the date. The remedy
is the Sprint 2 re-verification pass: check each AI Act provision and date against
the primary EUR-Lex source, rebuild it as Evidence Objects, set real `verified_at`
values, and *then* advance the page date. Until that pass runs, the page date
reflects its true last-verification, not today.

No paid Diagnostic launches until this pipeline is operating for at least the EU
AI Act corpus (Doctrine §8).

---

## 6. Changelog format

The public changelog (`/sources/changelog/`, or per-regulation) records:

> Date · Triggering event · Regulation & article · Evidence IDs superseded →
> new Evidence IDs · Affected EERS dimensions · Source URL

The changelog is part of the Reference Commons — public, permanent, citable. It is
the visible proof that the asset is maintained, which is itself an authority
signal for researchers, journalists, and agents.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
