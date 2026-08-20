# R2.6 — Decision Utility Layer

**Status:** OPEN — Decision Objects staged + candidate integrated (workbench only)  
**Opened:** 2026-08-20  
**Branch:** `sprint-r2-gdpr-r2-6-decision-utility`  
**Prerequisite:** R2.5 CLOSED / PASS via PR #38 merge `a6b9ed0ea09e2e816b5ef5dd2a0a7dc9960105a6`

---

## What R2.6 is

Convert the verified Evidence Graph into **planning decisions** without minting new legal facts.

Operational transform:

`Verified claim -> planning question -> consequence -> dependency/qualification -> action to investigate`

EuraPlan does **not** issue a legal judgment about an unknown company. It surfaces:

1. the **decision that must be closed**, and  
2. the **evidence that governs it**.

Example (correct form):

> **Representative gate**  
> Does Art. 3(2) apply to the activity?  
> If yes, inspect the default duty in `EP-CLM-000024` together with the exception in `EP-CLM-000025`.  
> **Planning consequence:** representative status must be closed before freezing the European operating model.

Anti-example (forbidden):

> "Your company needs an EU representative."

---

## Layer contract

| Layer | Artifact | Truth-status |
|---|---|---|
| Truth | 31 claims `EP-CLM-000015`…`000045` | `workflow_state=verified` |
| Analytical seeds | `r2_1_planning_consequence` in minted draft | **Not** verified facts; workbench seeds only |
| Decision Utility | 9 Decision Objects in `decision-utility.staging.json` | Derived staging; not claims; not publishable facts |

If a utility sentence needs a **new legal proposition**, it does **not** enter the page until it passes an independent claim-governance path. R2.6 mints **no** new `EP-CLM-*` IDs.

---

## Nine Decision Objects

| Decision object | Primary claims |
|---|---|
| Territorial applicability | 018-020 |
| Operating role | 021-023 |
| EU representative | 024-025 |
| Lawfulness baseline | 026-028 |
| Governance readiness | 029-034 |
| Breach response | 035-038 |
| DPIA / DPO triggers | 039-040 |
| International transfer path | 041-044 |
| Enforcement exposure | 045 |

Each object contains **four substantive fields** plus **governance metadata**.

**Substantive fields (Decision Utility content):**

1. **Question** — the planning decision to close  
2. **Evidence** — claim IDs (+ co-render / hierarchy constraints)  
3. **Planning consequence** — what must be decided before a named entry freeze point  
4. **What remains fact-specific** — facts that cannot be closed from the graph alone  

**Governance metadata (not additional utility propositions):** `id`, `title`, `primary_claims`, `co_render`, `related_hierarchy`, `seed_refs`, `hard_rules`  

---

## Hard gates (DEC-052)

| Gate | Rule |
|---|---|
| Live `/regulation/gdpr/index.html` | **DO NOT** overwrite |
| Public `/regulation/gdpr/claims.json` | **FORBIDDEN** until R2.8 |
| Claim workflow | Remains `verified` |
| Publish Gate / R2.7 / R2.8 | **NOT OPEN** |
| New claims | **None** for utility alone |
| Seeds | May inform wording; must not be treated as verified propositions |
| Co-render | 024↔025, 032↔033, 035↔036, 037↔038 stay paired |
| Chapter V | `44 -> 45 -> 46 -> 49` hierarchy; not equal options; not `qualified_by` |
| Art. 6 | Structural lawfulness gate — **not** "consent is required" |
| Art. 30 | Default + Art. 30(5) qualification — **not** automatic <250 exemption |
| Art. 37 | Trigger model — **not** a universal DPO duty |

---

## Deliverables

1. `DEC-052` — close R2.5; open R2.6 under this contract  
2. `R2_6_DECISION_UTILITY.md` — this scope note  
3. `decision-utility.staging.json` — nine Decision Objects  
4. Candidate integration — Decision Utility section in `page-candidate/index.html`  
5. Utility fidelity audit against the Exit Gate below (owner review)

---

## Exit Gate (hard fail)

R2.6 **fails** if any of the following appears:

1. Unsupported legal conclusion about a specific unknown actor  
2. Missing qualification / co-render for a qualified default  
3. Adequacy / SCC / Art. 49 framed as interchangeable equal options  
4. Personal recommendation disguised as a verified fact  
5. Planning consequence that cannot be traced to specific claim IDs  
6. New legal proposition introduced only to make the page "useful"  
7. Live route rewrite, public `claims.json`, or claim promotion beyond `verified`

---

## Exit toward R2.7 / R2.8

R2.6 may close when owner fidelity audit PASSes against the Exit Gate.

Then only:

- **R2.7** — citation + machine registration prep (still gated)  
- **R2.8** — Publish Gate (`publishable` / `published` + live HTML + public `claims.json`)

---

*Workbench artifact only. Not a published website page. Not legal advice.*
