# EERS_1.0_CANDIDATE_SPECIFICATION.md
**Standard:** European Entry Readiness Standard (EERS)
**Specification version:** 1.0 **Candidate**
**Status:** Candidate — Not Yet a Released Standard
**Asset:** EuraPlan.com
**Publisher:** EuraPlan (Sohadot)
**Last Updated:** August 2026
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, CLAIM_POLICY.md, EVIDENCE_GRAPH_MODEL.md, EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md

---

> The European Entry Readiness Standard (EERS) defines the minimum conditions
> under which a non-EU company can be considered ready to enter the European
> market. **This is a candidate specification.** It is published for development
> and validation. It is **not** a released standard, it does **not** yet carry a
> persistent identifier (DOI), and no external party should yet claim conformance
> to it. It is released as EERS 1.0 only after the validation gate in §11 passes.

**Do not cite this as a released standard.** Until §11 passes, cite it — if at all
— as *"EERS 1.0 (Candidate)"* with this document's URL, never as a fixed released
version.

---

## 1. Scope and status

EERS is a **planning-readiness** standard. It assesses whether a company has done
the mapping, sequencing, and decision work required before a European market
entry. It is **not** a legal compliance certification, and a passing assessment is
**not** a statement that a company is legally compliant. This boundary is normative
and governed by `CLAIM_POLICY.md`.

- **Reference form (public):** the specification, dimensions, and criteria below.
- **Assessment form (applied):** a company-specific EERS result, produced only
  through a EuraPlan Entry Planning Protocol run. The assessment form is part of
  the paid Intelligence layer; the specification form is free and citable once
  released.

Both forms exist at all times. The public reference is never withheld to create
the paid assessment (Doctrine §2).

---

## 2. Normative language

The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are to be interpreted
as requirement levels for a conforming EERS assessment. During the candidate phase
these requirements are themselves under test and MAY change before release.

---

## 3. The eight readiness dimensions (candidate)

Each dimension has a stable ID, a definition, and the condition that MUST hold for
the dimension to be scored as met.

| ID | Dimension | The dimension is met when… |
|---|---|---|
| **DIM-01** | Regulatory Mapping | All EU regulations applicable to the company's entity type, product, and role have been identified and enumerated. |
| **DIM-02** | Compliance Timeline | The applicable enforcement and phase dates are known and placed on the company's entry timeline. |
| **DIM-03** | Country Selection | A target entry country has been chosen with stated evidence and rationale. |
| **DIM-04** | Entity & Legal Structure | The legal setup for EU operations is defined (entity form, location, representation). |
| **DIM-05** | Funding Awareness | EU funding eligibility relevant to the sector, country, and stage has been assessed **— including an explicit "funding not sought" determination where applicable** (see §5.1). |
| **DIM-06** | Product Compliance | The product or service is mapped against the specific EU requirements that apply to it. |
| **DIM-07** | Risk Classification | Entry risks are identified and categorized (regulatory, market, execution). |
| **DIM-08** | Execution Plan | A concrete 30/90/180-day entry plan with sequenced steps exists. |

Each dimension MUST cite the Claim nodes (`EVIDENCE_GRAPH_MODEL.md`) that inform
it. A dimension asserted without supporting evidence is scored `unassessed`.

> **Open validation questions (candidate).** Each "met" condition still needs a
> tested *evidence threshold* (how much evidence is enough). DIM-05 needs the
> not-applicable path below. `partial`/`gap` need reproducibility rules (§4.1).
> These are resolved during §11 validation, not asserted now.

---

## 4. Dimension states

Each dimension resolves to exactly one state:

| State | Meaning |
|---|---|
| `met` | The condition in §3 holds, supported by evidence. |
| `partial` | The work is begun but the condition is not fully satisfied. |
| `gap` | The condition is not satisfied. |
| `not_applicable` | The dimension does not apply to this company (e.g. DIM-05 for a company not seeking EU funding), with a stated reason. |
| `unassessed` | No company-specific assessment has been run for this dimension. |

In the **public reference form**, all dimensions display as `unassessed`. States
other than `unassessed` MUST NOT appear outside a protocol run.

### 4.1 Reproducibility (candidate requirement)

`partial` and `gap` MUST be reproducible: two assessors given the same inputs and
the same evidence MUST reach the same state. The candidate phase must produce the
decision rules that make this true before release.

---

## 5. Readiness determination

- A company is **Entry-Ready** only when every **applicable** dimension is `met`
  (a `not_applicable` dimension does not block).
- A company scoring `gap` on **any** applicable dimension is **not** entry-ready,
  regardless of ambition or other scores. Readiness is conjunctive, not additive.
- A numeric aggregate (0–100) is **not defined in this candidate** and MUST NOT be
  reported until a scoring function is specified and validated (§11). The earlier
  claim that a 0–100 score "MAY be reported" is withdrawn pending that work.

### 5.1 DIM-05 not-applicable path

A company that is genuinely not pursuing EU funding scores DIM-05 `not_applicable`
with a recorded reason. This MUST NOT be used to bypass a real funding-awareness
gap; the not-applicable determination is itself evidence-backed.

---

## 6. The EERS Delta (change over time)

An EERS assessment is a point-in-time result. An **EERS Delta** reports how a
company's dimension states changed between two assessments, and why.

A conforming Delta entry MUST contain:

> Affected dimension → previous state → current state →
> the Claim node whose change caused it → official source → verified date →
> the planning implication.

The Delta describes *what changed and which planning assumption it affects*. It
MUST NOT prescribe a legal action; where action is warranted it refers the company
to a qualified advisor (`CLAIM_POLICY.md`). It is computed per **profile
archetype** (`EVIDENCE_GRAPH_MODEL.md` §8), not per individual company.

---

## 7. Versioning and release path

- Version numbers are `MAJOR.MINOR`; this document is the **1.0 Candidate**.
- A **MAJOR** increment changes dimension definitions, the dimension set, or the
  readiness determination rule; a **MINOR** increment clarifies wording.
- A released version is immutable once released; changes ship as a new version.
- **DOI is deferred.** A persistent identifier (DOI) is minted only for a
  **released** version, never for a candidate. Concept vs version DOI semantics
  apply at release time, not now.

---

## 8. Worked example (illustrative, not a real assessment)

> A US-origin AI system provider targeting Germany.
>
> - DIM-01 — `met` (applicable regulations enumerated).
> - DIM-02 — `partial` (some phase dates placed; others not yet mapped).
> - DIM-03 — `met` (Germany, with rationale).
> - DIM-04 — `gap` (no EU entity or representative defined).
> - DIM-05 — `not_applicable` (company states it is not seeking EU funding, with reason).
> - DIM-06–08 — `unassessed` pending protocol run.
>
> Determination: **not entry-ready** — DIM-04 is a `gap`.

---

## 9. Boundaries (normative)

- EERS assesses **planning readiness**, not legal compliance.
- A EuraPlan EERS assessment is **planning intelligence**, not legal advice.
- EERS does **not** guarantee market success, funding award, or regulatory approval.
- No external party may claim "conforms to EERS 1.0" until §11 passes and the
  standard is released.

---

## 10. Conformance claims are frozen until release

During the candidate phase, EuraPlan MUST NOT publish, and MUST NOT invite others
to publish, any "conforms to / assessed under EERS 1.0" statement as if against a
released standard. This prevents external citations forming around a definition
that may still change.

---

## 11. Validation gate (the condition for release)

EERS 1.0 is released — status `Stable`, DOI minted, conformance permitted — only
after a pre-registered validation set passes:

1. A fixed set of **validation cases** (real, varied legitimate entry profiles:
   different origins, entity types, sectors, and objectives) is defined **before**
   assessment.
2. Each dimension's `met` threshold and each `partial`/`gap` boundary is exercised
   against those cases.
3. Reproducibility (§4.1) is demonstrated across independent assessors.
4. The DIM-05 not-applicable path and the conjunctive readiness rule are tested on
   cases designed to break them.
5. If a scoring function is introduced, it is specified and validated here — not
   assumed.

Only when this gate passes does a successor document, `EERS_1.0_SPECIFICATION.md`
(status `Stable`), supersede this candidate.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
*Asset owned by Sohadot | agent@sohadot.com*
