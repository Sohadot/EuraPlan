# FRESHNESS_ENGINE.md
**Version:** 1.1
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, SOURCE_POLICY.md, CONTENT_QUALITY_STANDARD.md, EVIDENCE_GRAPH_MODEL.md, CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md

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

Every material change to EU regulatory reality flows through seven stages before it
reaches a reader or a subscriber:

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
| **Source Registry** | Maintain the list of official sources per regulation (EUR-Lex ELI/CELEX, Commission pages, agency guidance) | `sources/registry` |
| **Change Detection** | Monitor registered sources for amendment, new guidance, or a passing enforcement date | Candidate change, stamped `detected_at` |
| **Human Verification** | A person confirms the change against the primary source | Verified change |
| **Claim Impact Analysis** | Identify which Claim nodes and EERS dimensions the change moves | Impacted `EP-CLM-*` list |
| **Corpus Update** | Move affected claims through `review_required` → resolution (identity spec §3.2); set new `last_verified_at` | Updated corpus |
| **Changelog** | Record the change with triggering event and date | Public changelog entry |
| **Subscriber Delta** | Emit EERS Deltas to affected profile archetypes | Paid signal |

When a trigger fires, the affected claim moves to `validity_state: review_required`
— **not** straight to `superseded`. Review either returns it to `active` with a
fresh `last_verified_at`, or resolves it to `superseded` / `corrected` /
`withdrawn` per the change taxonomy (identity spec §5).

---

## 3. Freshness timestamps and the SLA

The SLA is measured from **when a trigger is detected**, not from when the claim was
last verified. A claim verified yesterday can acquire a same-day obligation if an
amendment lands today. Each claim under a trigger therefore carries:

| Field | Meaning |
|---|---|
| `triggered_at` | When the triggering event occurred in the world (e.g. amendment adopted) |
| `detected_at` | When EuraPlan's Change Detection registered it |
| `verification_due_at` | `detected_at` + the SLA window for that trigger type (below) |
| `last_verified_at` | When a human last verified the claim against its sources |
| `next_backstop_review_at` | The scheduled routine review, independent of any trigger |

### 3.1 SLA windows (measured from `detected_at`)

| Trigger | Window |
|---|---|
| An enforcement or phase date passes | 3 business days |
| A cited regulation is amended | 5 business days |
| Official guidance materially changes a claim | 10 business days |
| Routine backstop review (no trigger) | governed by `next_backstop_review_at`, max 6 months |

### 3.2 The breach rule (corrected)

> **Overdue / review breach** when: a trigger exists **AND** `now > verification_due_at`
> **AND** the claim is still unresolved (`review_required`).

Absent any trigger, routine freshness is governed solely by
`next_backstop_review_at`. A claim in `review_required` past its
`verification_due_at` MUST NOT display a `Verified` confidence badge until
re-verified. (The earlier "stale if `last_verified_at` older than the SLA" rule was
wrong: the SLA clock starts at `detected_at`, not at last verification.)

---

## 4. Two dates, never merged: content update vs verification

A `Last Updated` (page-content) date and a regulatory-verification date are
different claims and are governed separately (`EVIDENCE_GRAPH_MODEL.md` §7).

- **Page last content update** — mirrors `dateModified` in JSON-LD and the visible
  "Last Updated" line (`STRUCTURED_DATA_POLICY.md` §6). Advances on any content or
  markup change.
- **Regulatory verification** — the newest `last_verified_at` among the page's
  published claims. Advances only on genuine re-verification.

Both SHOULD be shown, distinctly, e.g.:

```
Last content update: 2026-08-18
Regulatory verification: 2026-08-17
```

Re-verifying an unchanged claim advances the verification date but not the content
date; an accessibility or wording edit advances the content date but not the
verification date. Merging them corrupts provenance.

### 4.1 The date-integrity rule

- A verification date MUST only advance when a human has re-verified the claim
  against its primary source.
- Advancing any date to *simulate* freshness — without the corresponding real event
  — is a governance breach equal to publishing an unsourced statistic.

---

## 5. Standing obligation on the live corpus

The indexed site carries a `June 2026` stamp and an AI Act timeline predating recent
developments. Under §4.1 the remedy is **not** to bump the date. The remedy is the
Sprint 2 re-verification pass: check each AI Act provision and date against the
primary EUR-Lex source, rebuild it as Claim nodes, set real `last_verified_at`
values, and *then* advance the page's verification date.

No paid Diagnostic launches until this pipeline is operating for at least the EU AI
Act corpus (Doctrine §8).

---

## 6. Changelog format

The public changelog (`/sources/changelog/`, or per-regulation) records:

> Date · Triggering event · Regulation & provision · Claim IDs moved to
> `review_required` → resolution (`superseded`/`corrected`/`withdrawn`/back to
> `active`) · `change_type` · Affected EERS dimensions · Source URL

The changelog is part of the Reference Commons — public, permanent, citable. It is
the visible proof that the asset is maintained, which is itself an authority signal
for researchers, journalists, and agents.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
