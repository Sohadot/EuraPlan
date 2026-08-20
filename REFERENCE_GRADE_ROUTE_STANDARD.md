# REFERENCE_GRADE_ROUTE_STANDARD.md
**Version:** 2.0
**Status:** Active — Governing Standard (mandatory for all indexable published routes)
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** GOVERNANCE_CHARTER.md, REFERENCE_SOVEREIGNTY_DOCTRINE.md, EVIDENCE_GRAPH_MODEL.md, CLAIM_POLICY.md, SOURCE_POLICY.md, PAGE_BLUEPRINT_STANDARD.md, CONTENT_QUALITY_STANDARD.md, SEO_GOVERNANCE.md, FRESHNESS_ENGINE.md, DERIVATIVE_SURFACE_REGISTRY.md
**Opened by:** DEC-047

---

## 1. Purpose

EuraPlan is a sovereign reference asset. **Excellence on one route and adequacy on another is a governance failure.** Every indexable published route must meet a high reference-grade floor.

This standard does **not** equalize pages by word count or length. It equalizes them by **rigour and reference value**, scored against the ontology role of that route:

| Ontology role | Depth form |
|---|---|
| Regulation reference | Legal / Evidence-graph depth |
| Country reference | Execution-intelligence depth |
| Standard (EERS) | Formal-specification depth |
| Protocol | Methodology depth |
| Sector / Funding | Cross-regulation / eligibility decision depth |
| System pages (home, enter, clock, sources, governance, acquire) | Conceptual and functional depth |

SEO is an **outcome of quality**, not a separate content layer. Pages that only summarize official prose without information gain fail this standard.

---

## 2. The six mandatory layers

A route is **Reference-grade** only when all six layers are present and substantive for its ontology role. Absence of any layer = not Reference-grade, even if long.

### L1 — Identity & Scope
What entity is this? What are its boundaries? What is in scope / out of scope? What is this page **not**?

### L2 — Primary Evidence
Official / institutional source; provenance; provision or institutional locator; verification date; confidence. Tier rules per `SOURCE_POLICY.md` / `CLAIM_POLICY.md`.

### L3 — Unique Analytical Layer
What EuraPlan adds **above** the primary source: interpretation structure, decision model, execution map, cross-regulation reasoning — **not** a paraphrase summary.

### L4 — Decision Utility
After reading, what can a real user **do**? At least one concrete use for relevant audiences among: company, investor, researcher, journalist, analyst, advisor.

### L5 — Machine & Citation Layer
Stable anchors where claims exist; structured data; claim IDs where required; citation format; machine-readable representation when meaningful (e.g. `claims.json`). Internal links are ontology edges, not SEO decoration.

### L6 — Maintenance Contract
Freshness rule; last verified / last updated (not conflated); derivative dependencies (`DERIVATIVE_SURFACE_REGISTRY.md`); sitemap `lastmod` on substantive change (same-release rule); change history via DEC / audit / git.

---

## 3. Gate rejection criteria (hard fail)

An indexable published route **fails** Reference-grade Gate if any of the following is true:

1. Country (or peer) names are interchangeable for ~70%+ of the page.
2. The same content is available by reading the first page or two of official sources alone.
3. No decision object and no unique analytical layer.
4. A researcher or journalist cannot cite a specific part (no stable unit).
5. There is no defined re-verification / freshness contract.
6. Template repetition exceeds added knowledge.

---

## 4. Competitive moat test (per topic)

For each topic, EuraPlan should be:

1. **More structured** than official prose  
2. **More primary-source-grounded** than consultancy blogs  
3. **More decision-oriented** than legal summaries  
4. **More machine-readable** than typical research articles  
5. **More transparent** than proprietary compliance tools  

SERP position is a lagging indicator. This moat test is the leading one.

---

## 5. Scoring (Sprint R1 and later)

Score each route 0–100 across eight dimensions (equal weight 12.5 pts each unless noted in an audit):

| Dimension | Maps to |
|---|---|
| Evidence depth | L2 |
| Unique information gain | L3 |
| Conceptual depth | L1 + ontology-appropriate depth |
| Decision utility | L4 |
| Citation readiness | L5 |
| Machine readability | L5 |
| Freshness | L6 |
| SEO semantics | Entity clarity + internal ontology + real lastmod (outcome of L1–L6) |

**Core Authority threshold:** Wave 1 routes must reach **≥ 90/100** before new expansion routes are opened.

Claim-object count is **not** a template quota. Evidence Graph objects are minted from material truth, not from a fixed N.

---

## 6. Depth Equalization Program — waves

**No new expansion routes** until Wave 1 meets threshold (DEC-047).

### Wave 1 — Core Authority
`/regulation/eu-ai-act/` (Gold Reference — maintain) → GDPR → EU Data Act → CRA → EERS → Protocol  
Upgrade regulation siblings toward Evidence Graph-grade where material (proposition → source → provision → actor → applicability → exception → date/state → planning consequence → verification).

### Wave 2 — Country Execution Intelligence
Germany / Netherlands / France as **Country Execution Intelligence Nodes** (authority graph, establishment pathway, supervisory landscape, sector friction, national execution of EU stack, funding/institution interfaces, scenarios, trade-offs, verified operational sources, when this country is / is not the right first market).  
Country Evidence Objects (`EP-CTR-CLM-*` or successor) only after a designed model — do **not** freeze an ID namespace prematurely.

### Wave 3 — Supporting System Pages
Homepage, Enter, Clock, Sources, Governance, Acquire, Funding, Sector — conceptual/functional depth appropriate to role (not legal depth for its own sake).

**Upgrade order after R1 audit:** GDPR → Data Act → CRA → France → Germany → Netherlands → AI/SaaS → Horizon Europe (adjust if R1 scores dictate).

---

## 7. Relationship to existing standards

| Document | Role vs this standard |
|---|---|
| `PAGE_BLUEPRINT_STANDARD.md` | Structural skeleton per page type — still required |
| `CONTENT_QUALITY_STANDARD.md` | Base elements and prohibited patterns — still required |
| `ACCEPTANCE_CRITERIA.md` / `SCALING_AND_AUTOMATION_POLICY.md` §11 | Publication gates — Reference-grade layers are additional pass conditions for indexable routes |
| `EVIDENCE_GRAPH_MODEL.md` | How claims are modeled when Evidence Graph depth applies |
| `DERIVATIVE_SURFACE_REGISTRY.md` | L6 derivative consistency |

This document is the **depth and reference-value** overlay. Blueprints without information gain still fail §3.

---

## 8. Sprint R1

**Sprint R1 — Reference Depth Audit & Upgrade Standard**  
Audit artifact: `governance/audits/REFERENCE_DEPTH_AUDIT_R1_2026-08-20.md`  
Outcome: baseline scores for all 17 sitemap routes; Wave 1 upgrade backlog; no expansion until Core Authority ≥ 90.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
