# R3.1 — EU Data Act Claim Map & Falsification Register
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.1 Claim Map & Falsification
**Status:** IN PROGRESS — falsification only. **NO `EP-CLM-*` / `EP-SRC-*` minted. No IDs. No live mutation.**
**Branch:** `claude/r3-1-data-act-falsification` (fresh from `main@dd7dc866ed7855428d4bbfe2e50f3fa053d215eb`, Merge #51 — no merge/cherry-pick from the R3.0 branch)
**Intake baseline (frozen):** R3.0 corpus on `main` — **54 workbench rows / 46 live** (30 candidate + 16 split-needed) + 8 parked (7 defer + 1 reject)
**Primary text (authentic):** Regulation (EU) 2023/2854, CELEX `32023R2854`, read with corrigendum OJ L, 2024/90790 (`DATA-SRC-CAND-01`+`-02`)
**Date:** 2026-08-24

---

## Method (per the R3.1 contract)

Each live candidate is tested **literally against the authentic text**, not against R3.0 wording. Exactly one verdict per candidate:

- **KEEP** — true, atomic, material for entry planning, stands as one proposition.
- **SPLIT** — carries two or more distinct facts; must be decomposed.
- **MERGE** — duplicate of, or not independent from, another candidate.
- **DROP** — unsupported, inaccurate, immaterial, or outside EuraPlan's ontology.
- **DEFER** — true but not fixable now (dependency / freshness / external instrument not yet pinnable).

Every surviving proposition carries an **exact locator** (Article + paragraph + point where the text is pointed), the **reason** for the verdict, and any **dependency** on GDPR / DMA / sectoral law recorded explicitly (never absorbed into the Data Act). **No mint** anywhere in R3.1 — identity (`EP-CLM-000046`+) begins only in R3.2 on survivors.

**Units** (reviewed one at a time): **R3.1-A** Scope & temporal baseline · R3.1-B Ch. II–III · R3.1-C Ch. IV–V · R3.1-D Ch. VI–VIII · R3.1-E Enforcement & boundaries · R3.1-F Qualification audit (Q1–Q16) → closeout.

**Definitions-handling rule (set here, applied throughout):** a defined term becomes a *standalone* proposition only when the definition is itself scope-gating for entry planning (what is in/out of the regime). Other definitions are **locator-confirmed supporting terms** that attach to the operative claim that uses them — recorded, not minted as separate claims, to prevent definitional bloat.

---

## R3.1-A — Scope & temporal baseline (§A instrument/dates + §B definitions/scope/GDPR boundary)

**Live intake this unit:** 14 (A1–A5, B1–B7 incl. B5b/B6b) · **Parked carried in:** A6 (defer), A7 (reject).
**Locators resolved verbatim this unit:** Art. 50 (all dates); Art. 2 points (1)/(5)/(6)/(8)/(12)–(18); Art. 1(5); Art. 4(12); Art. 5(7); Art. 7(1)/(2). All `⚠ verify` flags for §A/§B are now **cleared**.

### A. Instrument & application state

| Row | Verdict | Exact locator | Reason | Dependency |
|---|---|---|---|---|
| **R-A1** instrument identity + direct applicability | **KEEP** | Title; Art. 1(1); Art. 50 final sentence ("binding in its entirety and directly applicable in all Member States") | True, atomic, material — the correct instrument/CELEX must anchor entry docs | — |
| **R-A2** entry into force 11 Jan 2024 | **KEEP** | Art. 50, 1st para ("twentieth day following … publication"; OJ 22.12.2023 → **11.1.2024**) | Atomic; anchors the Art. 50 legacy-contract "≥10 years from 11 January 2024" computation. Calendar date is *derived* from the OJ publication date — record as derived, not quoted | — |
| **R-A3** general application 12 Sept 2025 | **KEEP** | Art. 50, 2nd para ("It shall apply from 12 September 2025") | Highest-salience temporal fact — the Data Act is **live law now**, not a future phase | — |
| **R-A4** Art. 3(1) design duty applies to connected products/related services placed on market **after 12 Sept 2026** | **KEEP** | Art. 50 (phasing sentence) + operative Art. 3(1) | Atomic temporal-scope rule. (Its default↔phasing relationship to A3 is a qualifier edge → tested in R3.1-F, Q1 — not a reason to split the row) | — |
| **R-A5** Chapter IV temporal application | **SPLIT** | Art. 50 (Chapter IV sentence) | Row carries **two distinct temporal rules** → split: | — |
| → **R-A5a** Ch. IV applies to contracts concluded **after 12 Sept 2025** | *(KEEP, post-split)* | Art. 50 | New-contract rule | — |
| → **R-A5b** Ch. IV applies **from 12 Sept 2027** to contracts concluded on/before 12.9.2025 that are (a) indefinite **or** (b) due to expire ≥10 years from 11.1.2024 | *(KEEP, post-split)* | Art. 50 | Legacy-contract rule with its own duration test | anchored on R-A2 date |
| **R-A6** Ch. III applies to availability duties under Union/national law entering into force **after 12.9.2025** | **DEFER** (confirmed) | Art. 50 (Chapter III sentence) | True. DEFER stands at the general-route level, but the trigger is **not "future law" per se** — Art. 50 keys off Union/qualifying national law *entering into force after 12.9.2025*, some of which may already be in force as of 2026; **applicability must be resolved per sector** — freshness/dependency watch-item, not a live claim | external/sector-specific Union or qualifying national law entering into force after 12.9.2025; applicability resolved per sector |
| **R-A7** Commission evaluation by 12.9.2028 | **DROP** (confirmed) | Art. 49 | Institutional duty on the Commission; not an entrant obligation, immaterial to entry planning | — |

### B. Scope, actors & definitions

| Row | Verdict | Exact locator | Reason | Dependency |
|---|---|---|---|---|
| **R-B1** "connected product" definition | **KEEP** | Art. 2, point **(5)** | Scope-gating definition — decides whether a product is in the regime at all. **Survivor wording is normalized to carry *all* Art. 2(5) elements, including the primary-function limiter — a product whose primary function is the storing, processing or transmission of data on behalf of any party other than the user is excluded. R3.0's obtain/generate/collect-and-communicate shorthand must not be inherited without this limiter** | — |
| **R-B2** "related service" definition (incl. **later-connected** services) | **KEEP** | Art. 2, point **(6)** | Scope-gating; corrected in R3.0 hardening to include services connected subsequently to add/update/adapt functions | — |
| **R-B3** user vs data holder distinct roles | **SPLIT** | Art. 2 points **(12)** / **(13)** | Two defined terms = two atomic scope-gating definitions → split (the *distinction itself* is analytical seam S2, not a legal claim): | — |
| → **R-B3a** "user" definition | *(KEEP, post-split)* | Art. 2, point **(12)** | Scope-gating actor definition | — |
| → **R-B3b** "data holder" definition | *(KEEP, post-split)* | Art. 2, point **(13)** | Scope-gating actor definition | — |
| **R-B4** "data processing service" definition | **KEEP** | Art. 2, point **(8)** | Scope-gating — the gate into Chapter VI (switching). **Canonical proposition = the full Art. 2(8) wording: a digital service provided to a customer that enables ubiquitous and on-demand network access to a shared pool of configurable, scalable and elastic computing resources of a centralised, distributed or highly distributed nature, that can be rapidly provisioned and released. The "IaaS/PaaS/SaaS-type cloud/edge service" gloss is an explanatory annotation only, not part of the canonical legal proposition** | — |
| **R-B5** Ch. II obligations do not apply to micro/small enterprise's products/services | **KEEP** | Art. 7(1), 1st subpara | Scope-limit; actor = enterprise that manufactures/designs the product or provides the related service; includes the partner/linked/sub-contract condition | enterprise-size classification (SME Recommendation 2003/361/EC) |
| **R-B5b** exemption extends to medium-sized <1yr + connected products for 1 year after placing | **KEEP** | Art. 7(1), later subpara ("The same shall apply") | Distinct transitional grace with its own beneficiaries/triggers — a scale-up timing input. **Not unconditional: inherits the Art. 7(1) qualification (per recital 41 the 1-year grace does not apply where a partner/linked enterprise is not itself micro/small, or where manufacture/design/service is subcontracted in the specified case). Carries the inherited qualifier into Q2 → to be resolved in R3.1-F; survivor must not later surface as "medium-sized <1yr = exempt" unconditionally** | Art. 7(1) inherited qualification (partner/linked/subcontract — recital 41) |
| **R-B6** without prejudice to data-protection/privacy law; on conflict it prevails | **KEEP** | Art. **1(5)** | Boundary rule; distinct from the sectoral savings clause (Art. 44, §E) | GDPR 2016/679; ePrivacy 2002/58 (external — prevail on their layer) |
| **R-B6b** where user ≠ data subject, personal data is made available only on a valid legal basis under GDPR Art. 6 (Art. 9 conditions where applicable; ePrivacy Art. 5(3) where applicable) | **KEEP** (dual-anchor) | Art. **4(12)** (holder→user) **and** Art. **5(7)** (holder→third party) | **Operative proposition = the valid-basis condition founded on 4(12)/5(7)** — single principle in two operative flows, kept as one proposition citing both anchors (per-flow application surfaces in R3.1-B at C3/C6). **"The Data Act creates no legal basis" is retained as an interpretive note from recital 7 — not folded into the operative proposition founded on 4(12)/5(7)** | GDPR Art. 6 / Art. 9; Directive 2002/58 (ePrivacy) Art. 5(3) — all external (required basis / consent layer) |
| **R-B7** anti-waiver: term detrimental to user's Ch. II rights not binding on the user | **KEEP** | Art. **7(2)** | Atomic unenforceability rule; user access rights cannot be contracted away (links to Ch. II C-series, cross-ref) | — |

**Supporting definitions locator-confirmed this unit (not standalone claims — attach to operative claims later):** "data" 2(1); "data recipient" 2(14); "product data" 2(15); "related service data" 2(16); "readily available data" 2(17); "trade secret" 2(18) (= Dir. (EU) 2016/943 Art. 2(1)).

### R3.1-A verdict tally

**Live intake (14 rows) — verdicts:**

| Verdict | Count | Rows |
|---|---|---|
| KEEP | 12 | A1, A2, A3, A4, B1, B2, B4, B5, B5b, B6, B6b, B7 |
| SPLIT | 2 → 4 | A5 → A5a/A5b · B3 → B3a/B3b |
| MERGE | 0 | — |
| DROP | 0 | — |
| DEFER | 0 | — |

**Parked reconfirmed** (carried in, *outside* the 14 live intake): **A6 = DEFER, A7 = DROP.**

**Net propositions surviving R3.1-A:** 12 KEEP + 4 from splits = **16 live provisions** (from 14 live intake rows; 0 DROP / 0 DEFER *within* intake). Parked, accounted separately: A6 (DEFER) + A7 (DROP).

### Qualifier edges this unit touches (full test in R3.1-F)

- **Q1** A3 (general application) ↔ A4 (Art. 3(1) phasing) / A5a/A5b (Ch. IV phasing) — **temporal-scope dependency**, likely a `scope/temporal` qualifier rather than a substantive `qualified_by` exception. Flag for F.
- **Q13** A1 (Data Act applies) ↔ B6 (Art. 1(5) data-protection prevails) — **real boundary** qualifier.
- **Q16** B6b (personal-data legal-basis) qualifies the Ch. II sharing rights (C-series) — carries into R3.1-B.
- **Q2** B5/B5b (Art. 7 exemption, **incl. B5b's inherited Art. 7(1) partner/linked/subcontract qualification**) qualifies the Ch. II duties (C-series) — carries into R3.1-B; the unconditional-exemption reading is resolved in R3.1-F.

### Semantic-overreach guard (this unit)

- No general "access" rule asserted from a scope-gating definition — definitions stated as definitions.
- The GDPR interface (B6/B6b) is recorded as an **external dependency**, never restated as a Data Act-created data-protection rule.
- Derived calendar dates (A2) flagged as derived, not quoted.

---

## Running tally (all units)

| Unit | Intake (live) | KEEP | SPLIT (→net) | MERGE | DROP | DEFER | Status |
|---|---|---|---|---|---|---|---|
| R3.1-A Scope & temporal | 14 | 12 | 2 (→4) | 0 | 0 | 0 | **complete — awaiting review** |
| R3.1-B Ch. II–III | — | — | — | — | — | — | pending |
| R3.1-C Ch. IV–V | — | — | — | — | — | — | pending |
| R3.1-D Ch. VI–VIII | — | — | — | — | — | — | pending |
| R3.1-E Enforcement & boundaries | — | — | — | — | — | — | pending |
| R3.1-F Qualification audit (Q1–Q16) | — | — | — | — | — | — | pending |

> Live-intake counts only. R3.1-A parked rows (carried in, outside live intake, not counted in the columns above): **A6 = DEFER, A7 = DROP.**

**Mint counter: `EP-CLM-*` = 0 · `EP-SRC-*` = 0.** Next free remains `EP-CLM-000046` / `EP-SRC-000006`.

*EuraPlan.com — Sprint R3.1 workbench. Falsification register (living). Not a published website page.*
