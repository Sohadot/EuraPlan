# CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md
**Version:** 1.0
**Status:** Active — Operating Governance (Foundational)
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, SOURCE_POLICY.md, CLAIM_POLICY.md, EVIDENCE_GRAPH_MODEL.md

---

## 1. Why this document exists

The identity and lifecycle of a claim are one-way decisions. Once EuraPlan
publishes claims under a public identifier scheme and a citable history, changing
either breaks external citations and the historical record. This document freezes
those rules **before** the first `EP-CLM-*` object is minted, so that the identity
is permanent and the lifecycle is auditable.

`EVIDENCE_GRAPH_MODEL.md` defines the *data* of a claim. This document defines its
*identity* and its *lifecycle*. Where the two appear to differ, this document
governs identity and lifecycle.

---

## 2. Claim identity

### 2.1 The canonical identifier is opaque

The canonical claim identifier is an **opaque, monotonic sequence** that carries no
semantic meaning:

```
EP-CLM-<NNNNNN>        e.g. EP-CLM-000042
```

- `<NNNNNN>` is a zero-padded global sequence, assigned at reservation, never reused.
- The identifier encodes **nothing** about regulation, article, actor, or position.
  Meaning lives in metadata (§2.3), never in the ID.

**Rationale.** A semantic identifier such as `EP-CLM-AIA-113-003` bakes a
provision's location into permanent identity. That location is not stable: a claim
may rest on a recital, an annex, an implementing or delegated act, Commission
guidance, or **two provisions at once**; a provision may be renumbered by an
amendment; a claim's primary instrument may be reclassified. Any of these would
force the identifier to change — which is the one thing an identifier must never
do. The instrument cluster is therefore metadata, not identity.

### 2.2 Human-readable display label (non-authoritative)

For operational readability a claim MAY carry a `display_label` derived from its
primary instrument (e.g. `AIA · Art. 113(3)`). The label is a convenience only:

- It is **not** an identifier and **not** used in citations or anchors.
- It MAY change when the underlying locator changes; the canonical ID never does.
- Citations and anchors always use the opaque ID (`/regulation/eu-ai-act/#ep-clm-000042`).

### 2.3 Locator metadata (may change without changing identity)

The claim's connection to the law lives in per-source locator metadata, held in the
`sources[]` relation (`EVIDENCE_GRAPH_MODEL.md` §3):

`instrument · provision_type (article|recital|annex|guidance|implementing_act|delegated_act) · article · paragraph · point · annex_ref · source_locator (CELEX/ELI + fragment)`

If a provision is renumbered or a source is consolidated, the locator is updated
and the change is recorded (§5) — **the identifier is untouched.**

---

## 3. Two-axis state model

A claim has two independent states at all times: an editorial **workflow state**
and, once published, a **public validity state**. Conflating them (as an earlier
draft did, with only `active | superseded | withdrawn`) loses the fact that a
published, still-correct claim can require review without being false.

### 3.1 Workflow state (editorial; pre- and at-publication)

```
draft → pending_verification → verified → publishable → published
                                                   └→ void (terminal, pre-publication only)
```

| State | Meaning | Publishable? |
|---|---|---|
| `draft` | Claim written; ID reserved | No |
| `pending_verification` | Awaiting human check against primary source | No — maps to `Pending` (SOURCE_POLICY.md §5) |
| `verified` | Human-confirmed against Tier-1/Tier-2 source | Not yet public |
| `publishable` | Meets all quality/claim/source gates | Ready |
| `published` | Live in the corpus | — |
| `void` | Abandoned before publication | Terminal; ID retired, never reused |

No claim reaches `published` from `pending_verification` — this enforces
SOURCE_POLICY.md §5 ("No content classified as Pending may be published").

### 3.2 Public validity state (only after `published`)

```
active → review_required → { superseded | withdrawn | corrected }
   ▲___________|   (review may resolve back to active, unchanged)
```

| State | Meaning | Confidence mapping (SOURCE_POLICY.md §5) |
|---|---|---|
| `active` | Published and currently valid | `Verified` or `Referenced` |
| `review_required` | A trigger fired; validity not yet re-confirmed | Under review — badge held (FRESHNESS_ENGINE.md §3) |
| `superseded` | Reality changed; replaced by a successor claim | prior object → `Deprecated` handling |
| `withdrawn` | Removed with no successor | `Deprecated` |
| `corrected` | Was wrong at publication; replaced by a correction | `Deprecated` |

A trigger (an amendment, new guidance, a passing date) moves a claim to
`review_required`, **not** directly to `superseded`. Review may confirm the claim
is still valid and return it to `active` with a fresh `last_verified_at`.

---

## 4. ID reservation rules

- An ID is **reserved** the moment a `draft` is created. Reservation burns the
  number permanently.
- A reserved-but-unpublished ID that is abandoned becomes `void`. **Void IDs are
  never reused.** The sequence only ever moves forward.
- An ID is never reassigned to a different claim, in any state, ever.

---

## 5. Change taxonomy: how a claim ends

Four distinct events retire or replace a published claim. They are not
interchangeable, and each is recorded with its `change_type`.

| Event | Definition | Successor? | The world changed? | Our record was wrong? |
|---|---|---|---|---|
| **Supersession** | Reality moved on; a successor states the new truth | Yes | Yes | No |
| **Correction** | The claim was **wrong at publication**; a correction states what was always true | Yes | No | Yes |
| **Withdrawal** | The claim is removed and not replaced | No | Either | Either |
| **Interpretation change** | Our reading (or official guidance) of unchanged law changed | Yes (supersession, `change_type: interpretation`) | No (law unchanged) | Not necessarily |

Sub-distinction inside supersession:

- `change_type: amendment` — the underlying legal instrument itself changed.
- `change_type: interpretation` — the instrument is unchanged; guidance or our
  interpretation of it changed.

**Correction is not supersession.** A superseded claim was *true when published*
and remains part of the historical record of what was true then. A corrected claim
was *never true* and is flagged as an error so the record does not mislead a
researcher reading the history.

---

## 6. History is append-only

- No published claim object is ever deleted (`EVIDENCE_GRAPH_MODEL.md` §5).
- Superseded, corrected, and withdrawn objects remain addressable at their original
  anchors, carrying `superseded_by` / `corrected_by` / `withdrawn` markers.
- The successor carries `supersedes` / `corrects` back-pointers and its own
  `change_type`.
- This append-only chain is the citable amendment history that answers "what was
  true in March 2026, and what changed?" — and distinguishes *changed* from
  *was-wrong*, which a plain summary cannot.

---

## 7. Prohibited

| Prohibited | Reason |
|---|---|
| Encoding regulation/article/position in the canonical ID | Identity would change when a locator changes |
| Reusing or recycling a `void` or retired ID | Breaks citation and history integrity |
| Publishing a claim in `pending_verification` | Violates SOURCE_POLICY.md §5 |
| Moving a triggered claim straight to `superseded` without `review_required` | Conflates "needs review" with "is false" |
| Labeling a correction as a supersession | Misrepresents the historical record |
| Deleting a superseded/withdrawn/corrected object | Destroys the append-only history |

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
