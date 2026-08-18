# EERS_1.0_SPECIFICATION.md
**Standard:** European Entry Readiness Standard (EERS)
**Specification version:** 1.0
**Status:** Stable — Citable Public Standard
**Asset:** EuraPlan.com
**Publisher:** EuraPlan (Sohadot)
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, CLAIM_POLICY.md, EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md

---

> The European Entry Readiness Standard (EERS) defines the minimum conditions
> under which a non-EU company can be considered ready to enter the European
> market. This document is the stable, versioned, citable specification of the
> standard. It is published openly as part of the EuraPlan Reference Commons.

**Suggested citation:**
> EuraPlan. *European Entry Readiness Standard (EERS 1.0).* Sohadot, 2026.
> https://euraplan.com/standard/eers/

---

## 1. Scope and status

EERS is a **planning-readiness** standard. It assesses whether a company has done
the mapping, sequencing, and decision work required before a European market
entry. It is **not** a legal compliance certification, and a passing assessment is
**not** a statement that a company is legally compliant. This boundary is
normative and governed by `CLAIM_POLICY.md`.

- **Reference form (public):** the specification, dimensions, and criteria below.
- **Assessment form (applied):** a company-specific EERS score, produced only
  through a EuraPlan Entry Planning Protocol run. The assessment form is part of
  the paid Intelligence layer; the specification form is free and citable.

Both forms exist at all times. The public reference is never withheld to create
the paid assessment (Doctrine §2).

---

## 2. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** in this document are
to be interpreted as requirement levels for a conforming EERS assessment.

---

## 3. The eight readiness dimensions

Each dimension has a stable ID, a definition, and the condition that MUST hold for
the dimension to be scored as met.

| ID | Dimension | The dimension is met when… |
|---|---|---|
| **DIM-01** | Regulatory Mapping | All EU regulations applicable to the company's entity type, product, and role have been identified and enumerated. |
| **DIM-02** | Compliance Timeline | The applicable enforcement and phase dates are known and placed on the company's entry timeline. |
| **DIM-03** | Country Selection | A target entry country has been chosen with stated evidence and rationale. |
| **DIM-04** | Entity & Legal Structure | The legal setup for EU operations is defined (entity form, location, representation). |
| **DIM-05** | Funding Awareness | EU funding eligibility relevant to the sector, country, and stage has been assessed. |
| **DIM-06** | Product Compliance | The product or service is mapped against the specific EU requirements that apply to it. |
| **DIM-07** | Risk Classification | Entry risks are identified and categorized (regulatory, market, execution). |
| **DIM-08** | Execution Plan | A concrete 30/90/180-day entry plan with sequenced steps exists. |

Each dimension MUST cite the Evidence Objects (`EVIDENCE_GRAPH_MODEL.md`) that
inform it. A dimension asserted without supporting evidence is scored `unassessed`.

---

## 4. Dimension states

Each dimension resolves to exactly one state:

| State | Meaning |
|---|---|
| `met` | The condition in §3 holds, supported by evidence. |
| `partial` | The work is begun but the condition is not fully satisfied. |
| `gap` | The condition is not satisfied. |
| `unassessed` | No company-specific assessment has been run for this dimension. |

In the **public reference form**, all eight dimensions display as `unassessed` —
the standard describes what readiness means but makes no claim about any specific
company. States other than `unassessed` MUST NOT appear outside a protocol run.

---

## 5. Readiness determination

- A company is **Entry-Ready** only when **all eight** dimensions are `met`.
- A company scoring `gap` on **any** dimension is **not** entry-ready, regardless
  of market ambition or scores on other dimensions. There is no averaging across
  a `gap` — readiness is conjunctive, not additive.
- A numeric aggregate (0–100) MAY be reported as a communication aid, but the
  conjunctive rule above governs the readiness determination. The numeric score
  MUST NOT be used to overrule a `gap`.

---

## 6. The EERS Delta (change over time)

Because the regulatory landscape moves, an EERS assessment is a point-in-time
result. An **EERS Delta** reports how a company's dimension states have changed
between two assessments, and why.

A conforming Delta entry MUST contain:

> Affected dimension → previous state → current state →
> the Evidence Object whose change caused it → official source → verified date →
> the planning implication.

The Delta describes *what changed and which planning assumption it affects*. It
MUST NOT prescribe a legal action. Where action is warranted, the assessment
refers the company to a qualified advisor (`CLAIM_POLICY.md`). This is the atomic
unit of the paid monitoring product and is computed per **profile archetype**
(`EVIDENCE_GRAPH_MODEL.md` §6), not per individual company.

---

## 7. Versioning

- This specification is **EERS 1.0**. Version numbers are `MAJOR.MINOR`.
- A **MAJOR** increment changes dimension definitions, the dimension set, or the
  readiness determination rule.
- A **MINOR** increment clarifies criteria or wording without changing meaning.
- Each published version is immutable once released; changes ship as a new version
  with a changelog. Assessments cite the specification version they were run
  against (e.g. "assessed under EERS 1.0").
- A citable snapshot of each released version SHOULD be deposited with a
  persistent identifier (DOI) so external papers and reports can cite a fixed
  version (`concept` DOI for all versions, `version` DOI for a specific one).

---

## 8. Worked example (illustrative, not a real assessment)

> A US-origin AI system provider, high-risk classification, targeting Germany.
>
> - DIM-01 Regulatory Mapping — `met` (EU AI Act, GDPR, EU Data Act enumerated).
> - DIM-02 Compliance Timeline — `partial` (AI Act phase dates placed; CRA dates not yet mapped).
> - DIM-03 Country Selection — `met` (Germany, with rationale).
> - DIM-04 Entity & Legal Structure — `gap` (no EU entity or representative defined).
> - DIM-05–08 — `unassessed` pending protocol run.
>
> Determination: **not entry-ready** — DIM-04 is a `gap`. The numeric aid is
> irrelevant to that determination.

---

## 9. Boundaries (normative)

- EERS assesses **planning readiness**, not legal compliance.
- A EuraPlan EERS assessment is **planning intelligence**, not legal advice.
- EERS does **not** guarantee market success, funding award, or regulatory approval.
- Conformance claims ("assessed under EERS 1.0") MUST reference this specification
  version and MUST NOT imply EuraPlan endorsement of the company.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
*Asset owned by Sohadot | agent@sohadot.com*
