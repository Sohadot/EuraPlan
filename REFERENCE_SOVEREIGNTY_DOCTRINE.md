# REFERENCE_SOVEREIGNTY_DOCTRINE.md
**Version:** 1.1
**Status:** Governing Document — Constitutional Layer
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md
**Governs:** All monetization, corpus, data, and licensing decisions taken after this date

---

> *This document resolves the central strategic tension of EuraPlan:
> how an asset can be a globally cited public reference and a durable
> revenue-generating business at the same time — without sacrificing either.
> It sits directly beneath the Category Intelligence Factory Plan and above
> the operating policies.*

---

## 1. THE GOVERNING PRINCIPLE

> **Public truth. Paid application.**
>
> The reference truth is never withheld.
> Payment is charged for its application, personalization,
> monitoring, integration, and the licensing of its structure.

This single line resolves the conflict between *global reference authority* and
*recurring revenue*. Authority is built by making the reference layer open,
accurate, and citable. Revenue is earned downstream — by applying that same
maintained truth to a specific company, keeping it fresh against a moving
regulatory landscape, and licensing the structure into institutional systems.

The two are not competing goals served by separate projects. They are the same
engine. The work that keeps the public reference correct is the same work that
produces the paid monitoring signal.

---

## 2. THE THREE-ENGINE ARCHITECTURE

| Layer | Function | Access | Value Produced |
|---|---|---|---|
| **EuraPlan Reference Commons** | Reference truth — EERS, regulations, sources, matrices, datasets | Free and open | Authority and citation |
| **EuraPlan Intelligence** | Diagnostic, monitoring, EERS deltas, company profiles, briefs | Paid | Recurring revenue |
| **EuraPlan Institutional Infrastructure** | API, datasets, widgets, EERS / ontology licensing | Paid (institutional) | Sovereignty and acquisition value |

**Directional rule:** value flows downward and revenue flows upward. The Commons
generates the authority that makes Intelligence trustworthy; Intelligence proves
the demand that makes Institutional Infrastructure fundable; Institutional
Infrastructure creates the acquisition-grade value described in `BUYER_LOGIC.md`.

**Boundary rule:** nothing that belongs to the Reference Commons — a regulatory
fact, an enforcement date, the EERS specification, a published dataset snapshot —
may ever be moved behind a paywall to create revenue. Revenue is added *beside*
the reference, never *subtracted from* it. This is the non-negotiable that keeps
the authority intact.

---

## 3. WHY THE REFERENCE MUST BECOME A CORPUS, NOT A CONTENT SITE

Superior content quality here does not mean longer articles. It means the
regulatory question is decomposed down to a level that can be *reasoned from and
cited*. A reference-grade regulation page connects, for every material point:

> Provision → Article → Applicability → Actor → Effective date →
> Planning consequence → Official source → Verification state →
> Last verified → Change history.

At that resolution, six audiences are served by one artifact:

- **Researchers** can cite a specific claim, not a whole page.
- **Journalists** can verify it against a primary source.
- **Companies** can build a decision on it.
- **Analysts** can compare it across time.
- **Investors** can read a portfolio company's exposure.
- **AI agents** can extract it without inferring the relationships.

This is the operational meaning of `AGENT_READABILITY_POLICY.md` taken to its
conclusion: stable URLs, extractable heading hierarchy, real HTML for data,
visible sources, no intelligence hidden in JavaScript.

---

## 4. WHAT WE MEASURE (INSTEAD OF PAGE COUNT)

Page count is explicitly rejected as a success metric. EuraPlan is measured on
six dimensions; the asset approaches *reference inevitability* only when all six
rise together.

| Dimension | Success Signal |
|---|---|
| **Evidence authority** | 100% of high-sensitivity claims carry Tier-1 provenance |
| **Freshness** | Every material change passes verification + changelog within a defined SLA |
| **Citation** | Independent use of EERS / datasets / claims in papers, reports, and press |
| **Machine retrieval** | Engines and agents extract claims and sources with no inference |
| **Institutional use** | Companies, advisors, and researchers use EuraPlan in real workflows |
| **Economic sovereignty** | Recurring revenue comes from Intelligence / licensing, with no paywall on the reference |

Two hundred irreplaceable reference nodes outrank twenty thousand replaceable SEO
pages. Depth and citability, not volume, are the growth axis.

### 4.1 The maintenance-capacity rule (constitutional)

> **Corpus size is constrained by verified maintenance capacity, not by publishing
> capacity.**

The corpus may only grow as fast as it can be kept verified under the Freshness
Engine. A published claim is a standing liability until the day it is retired: it
must be re-verified on every trigger and every backstop cycle. Therefore even the
"200 nodes" figure is a ceiling to be earned, never a target to be filled. Any node
that cannot be maintained to Tier-1 freshness MUST NOT be published — an
unmaintained reference node is worse than an absent one, because it spends the
authority the asset exists to accumulate.

---

## 5. THE REFERENCE SOVEREIGNTY SPRINT (SEQUENCE OF RECORD)

The next phase is **not** horizontal expansion and **not** monetization. It is the
construction of the layer that makes the information itself provable, citable,
updatable, and reusable by human and machine. Horizontal growth is paused until
the foundational pieces exist and are hardened.

**Sprint 1 — Foundational layer:**
1. Freshness Engine governance (`FRESHNESS_ENGINE.md`)
2. Evidence graph data model (`EVIDENCE_GRAPH_MODEL.md`)
3. Claim identity + lifecycle (`CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md`)
4. EERS as a **candidate** specification (`EERS_1.0_CANDIDATE_SPECIFICATION.md`)
5. Machine-discovery surface (`llms.txt`)

**Sprint 1.1 — Constitutional hardening (this sprint):** freeze the one-way
decisions before any claim is minted — opaque claim identity, the two-axis
lifecycle, the claim↔source graph relation, the trigger-based SLA, the
content-date vs verification-date split, and demotion of EERS to candidate. No
claim is minted and no live-site content changes until this passes.

**Sprint 2 — Gold-standard reference implementation:**
Take one regulation — **EU AI Act** — and build it to the full
provision→source→lifecycle→change resolution, as the reference template all other
regulations follow. Every regulatory claim is re-verified against primary EU
sources before any `last_verified_at` is stamped. Begins with a **read-only
verification audit** (no claims minted, no timestamps set, no live-site edits),
reviewed before any `EP-CLM-*` object is created.

**Sprint 3 — Generalization:** apply the template to GDPR, EU Data Act, and Cyber
Resilience Act — subject to the maintenance-capacity rule (§4.1).

**Sprint 4 — Citable artifacts:** publish the first dataset, and — only after the
EERS validation gate (`EERS_1.0_CANDIDATE_SPECIFICATION.md` §11) passes — the
released EERS standard with a persistent identifier (DOI). No DOI is minted for a
candidate.

**Sprint 5 — High-value decision nodes**, then **Sprint 6 — paid Entry Monitor**.

---

## 6. REVENUE ORDER OF RECORD

Free reference builds authority. The recurring engine is built on top of it, in
this order — consistent with `MONETIZATION_BOUNDARY.md`:

1. **Entry Diagnostic** — one-off application of the corpus to a specific company (entry product).
2. **Entry Monitor** — persistent company profile + change alerts + quarterly EERS delta (recurring).
3. **Advisor Workspace** — multi-client profiles for law firms, consultancies, chambers (highest ARPU; a distribution channel, not a competitor).
4. **Institutional Infrastructure** — dataset / API access, EERS and ontology licensing.

Single reports and the newsletter are acquisition and retention channels, **not**
the economic engine. The Expert Directory and public API are deferred until the
recurring loop is proven, to protect the perception of independence.

---

## 7. WHAT KNOWLEDGE-GRAPH PRESENCE IS — AND IS NOT

EuraPlan does **not** manufacture a Wikidata item or seek a Wikipedia entry to
feed a knowledge graph. Notability is earned downstream of authority, never
manufactured upstream of it:

> EuraPlan produces something important → independent parties use it →
> papers, reports, news, and institutions cite it → EuraPlan becomes
> independently notable → knowledge-graph presence follows as a result.

Citation is engineered by producing artifacts others *need* to cite — the EERS
specification, an annual European Regulatory Entry State report, country ×
regulation datasets, amendment histories — not by backlink outreach.

---

## 8. IMMEDIATE FRESHNESS OBLIGATION

The live site currently carries a `June 2026` update stamp and an AI Act timeline
that predates recent developments. Under the principle in this document, a
reference asset that displays a stale verification date is losing authority every
day. Therefore:

- No paid Diagnostic launches before the Freshness Engine pipeline exists:
  Official Source Registry → Change Detection → Human Verification →
  Claim Impact Analysis → Corpus Update → Changelog → Subscriber Delta.
- The AI Act gold-standard implementation (Sprint 2) re-verifies every date and
  provision against primary EU sources before any `last_verified_at` stamp is set.
- Update dates are only advanced on genuine re-verification — never to simulate
  freshness. Advancing a date without verification is itself a governance breach.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
*Asset owned by Sohadot | agent@sohadot.com*
