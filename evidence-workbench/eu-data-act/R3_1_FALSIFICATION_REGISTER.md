# R3.1 — EU Data Act Claim Map & Falsification Register
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.1 Claim Map & Falsification
**Status:** IN PROGRESS — falsification only. R3.1-A reviewed (PASS) · R3.1-B reviewed · R3.1-C reviewed (merged PR #59) · R3.1-D reviewed (merged PR #60) · **R3.1-E complete — awaiting review** · **R3.1-F (Q-audit) next — closes R3.1**. All 50 articles now falsified verbatim. **NO `EP-CLM-*` / `EP-SRC-*` minted. No IDs. No live mutation.**
**Source pack (from R3.1-C onward):** `evidence-workbench/eu-data-act/source-pack/` — authentic OJ act `EU_Data_Act_Regulation_2023_2854_official_text_EN.pdf` + `EU_Data_Act_Corrigendum_2024_12_09_official_text_EN.pdf`. R3.1-C locators were read verbatim from this pack.
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

## R3.1-B — Chapters II–III (B2C/B2B data sharing + data-holder availability duties)

**Live intake this unit:** 13 (C1–C7, D1–D5, D7) · **Parked carried in:** D6 (defer). *(Art. 7 rows B5/B5b/B7 were resolved in R3.1-A as scope; they are qualifier inputs here, not re-verdicted.)*
**Locators resolved verbatim this unit (all `⚠ verify` flags for Ch. II–III now cleared):** Art. 3(1)/(2)/(3); Art. 4(1)/(6)/(7)/(8)/(12)/(13)/(14); Art. 5(1)/(3)/(7)/(9)/(10)/(11); Art. 6(1)/(2) points (a)–(h); Art. 8(1)/(3)/(4); Art. 9(1)/(2)/(4); Art. 11(1)/(2)–(5); Art. 12(1)/(2). Verified against the authentic text (CELEX `32023R2854`, corrigendum OJ L, 2024/90790).

### C. Chapter II — connected-product data: user access & third-party sharing (Arts. 3–6)

| Row | Verdict | Exact locator | Reason | Dependency |
|---|---|---|---|---|
| **R-C1** design-by-default accessibility | **KEEP** | Art. **3(1)** | Atomic design duty: connected products/related services designed and manufactured so that product data + related-service data (incl. relevant metadata) are, **by default, easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format** and — where relevant and technically feasible — **directly accessible to the user**. Temporal phasing (placed on market after 12.9.2026, R-A4) is a `scope/temporal` qualifier → Q1 (tested in F), not a reason to split | — |
| **R-C2** pre-contract information | **SPLIT** | Art. 3, **(2)** / **(3)** | Row carries **two distinct pre-contract disclosure duties** — different actor, different itemised content → split: | — |
| → **R-C2a** connected-product pre-contract info | *(KEEP, post-split)* | Art. **3(2)** | Seller/rentor/lessor discloses, before a purchase/rent/lease contract, the specified items (data type/format/estimated volume; whether generated continuously/in real time; on-device vs remote storage; how to access, retrieve, erase) | — |
| → **R-C2b** related-service pre-contract info | *(KEEP, post-split)* | Art. **3(3)** | Prospective data holder / related-service provider discloses, before the service contract, its own (broader) itemised set (nature/volume; generation; intended data use; holder identity + contact; third-party sharing; complaint route; trade-secret/IP status; duration/termination) | — |
| **R-C3** data-holder access duty (data not directly accessible) | **KEEP** | Art. **4(1)** | Core access right: where data is not directly accessible from the product/related service, the data holder makes **readily available data + relevant metadata** accessible to the user **without undue delay, free of charge, of the same quality** available to the holder, and — where relevant and technically feasible — **continuously and in real time**. Rendered only with its trade-secret carve-out (R-C5, Q3) and personal-data condition (R-B6b / Art. 4(12), Q16) — never bare | trade-secret (R-C5); GDPR basis (R-B6b) |
| **R-C4** data-holder use / onward-sharing limits on non-personal data | **SPLIT** | Art. 4, **(13)** / **(14)** | R3.0 text captured only the 4(13) use-limb; **4(14) is a distinct onward-sharing prohibition** → split: | — |
| → **R-C4a** use limited to contract + no adverse insights | *(KEEP, post-split)* | Art. **4(13)** | Data holder uses readily-available **non-personal** data only on the basis of a **contract with the user**, and shall not use it to derive insights (economic situation/assets/production methods/use) that could **undermine the user's commercial position** | — |
| → **R-C4b** no onward provision of non-personal product data to third parties | *(KEEP, post-split)* | Art. **4(14)** | Data holder shall **not make non-personal product data available to third parties** except to fulfil its contract with the user, and shall bind any such third party against further sharing | — |
| **R-C5** trade-secret carve-out (user-access flow) | **KEEP** | Art. 4, **(6)/(7)/(8)** | Single **graduated** carve-out qualifying R-C3: (6) preserve + agree protective measures; (7) withhold/suspend where measures unmet or confidentiality breached; (8) refuse **case-by-case** in exceptional serious-economic-damage cases. Not a blanket refusal — strict conditions. Companion to R-C3 = Q3 | trade-secret protection (Dir. (EU) 2016/943) |
| **R-C6** user right to share data with a third party | **KEEP** | Art. **5(1)** | Atomic sharing right: on the user's (or a proxy's) request, the data holder makes readily available data + metadata available to a third party without undue delay, **free of charge to the user**, same quality, and — where relevant/technically feasible — continuously and in real time. Rendered with gatekeeper exclusion (R-C7 / 5(3)), third-party-use limits (R-D2 / Art. 6(2)), the third-party trade-secret regime (Art. 5(9)–(11), mirror of R-C5) and the personal-data condition (R-B6b / Art. 5(7)) → Q4/Q16 | third-party trade-secret (Art. 5(9)–(11)); GDPR basis (R-B6b) |
| **R-C7** gatekeeper not an eligible third party | **KEEP** | Art. **5(3)** | A DMA-designated gatekeeper is **not an eligible Art. 5 recipient** and may not solicit/incentivise the user to route data to it, nor receive Art. 4(1) data | DMA Reg. (EU) 2022/1925 Art. 3 (external — gatekeeper designation) |
| **R-D1** third-party purpose limitation | **KEEP** | Art. **6(1)** | A third party processes data received under Art. 5 **only for the purposes and under the conditions agreed with the user**, subject to data-protection law, and **erases** it when no longer necessary (unless otherwise agreed for non-personal data) | GDPR 2016/679 (external — personal-data limb) |
| **R-D2** third-party prohibitions | **KEEP** | Art. **6(2)** points (a)–(h) | Itemised bans: (a) no dark-pattern/coercion; (b) no profiling beyond the service the user requested; (c) no onward sharing without a user contract + trade-secret safeguards; (d) **no provision to a gatekeeper**; (e) **no competing-product development** or competitive sharing; (f) no security-impairing use; (g) no undermining trade-secret confidentiality; (h) no blocking a **consumer's** onward sharing | DMA 2022/1925 (point (d), external) |

### D. Chapter III — data-holder availability duties where obliged by law (Arts. 8–12)

| Row | Verdict | Exact locator | Reason | Dependency |
|---|---|---|---|---|
| **R-D3** FRAND + transparent terms | **KEEP** | Art. **8(1)** | Where a data holder is **obliged** to make data available (Art. 5 or other Union/national law), it does so on **fair, reasonable and non-discriminatory terms and in a transparent manner**. Conditional on an existing availability obligation — **gated by Art. 12(1)**; not a freestanding duty to sell data | availability-obligation source (Art. 5 / sectoral law — Art. 12(1) gate) |
| **R-D4** non-discrimination between recipients | **KEEP** | Art. **8(3)** | Data holder shall **not discriminate** between **comparable categories** of data recipients in the arrangements for making data available; objectively justified differences allowed; reasoned-request justification duty | — |
| **R-D5** compensation | **SPLIT** | Art. 9, **(1)** / **(4)** | Default compensation rule and the SME/non-profit **cost-cap** are distinct provisions → split: | — |
| → **R-D5a** reasonable, non-discriminatory compensation | *(KEEP, post-split)* | Art. **9(1)** | Compensation agreed in B2B for making data available shall be **non-discriminatory and reasonable and may include a margin** | — |
| → **R-D5b** SME / not-for-profit research cost-cap | *(KEEP, post-split)* | Art. **9(4)** | Where the recipient is an SME or not-for-profit research organisation (with no non-SME partner/linked enterprise), compensation **shall not exceed the costs in Art. 9(2)(a)** (formatting, dissemination, storage) — no investment-recovery margin. Default↔cap pair = Q5 | SME classification (Rec. 2003/361/EC) |
| **R-D7** technical protection measures + remedies | **KEEP** | Art. **11(1)** (measures + limit); **11(2)/(3)/(5)** (remedies) | Data holder may apply **appropriate TPM** (incl. encryption, smart contracts) against unauthorised access, but they **shall not discriminate** between recipients or **hinder the user's Art. 4/5 rights**; breach triggers erase / end-production / inform / compensate remedies, also available to the user | bounded by the user's Art. 4/5 rights |
| **R-D6** dispute-settlement bodies *(parked — outside live intake)* | **DEFER** (confirmed) | Art. **10** | True remedy channel (certified dispute-settlement bodies for availability/compensation disputes); secondary to entry planning — a possible single "remedies" claim later | — |

**Supporting locators confirmed this unit (attach to operative claims — not minted):** third-party-flow trade-secret regime Art. 5(9)/(10)/(11) (mirror of R-C5, attaches to R-C6); Art. 8(5)/(6) and Art. 9(2)/(3)/(5)/(7) as detail on the D-series; Art. 11(2)–(5) remedy detail on R-D7.

### R3.1-B verdict tally

**Live intake (13 rows) — verdicts:**

| Verdict | Count | Rows |
|---|---|---|
| KEEP | 10 | C1, C3, C5, C6, C7, D1, D2, D3, D4, D7 |
| SPLIT | 3 → 6 | C2 → C2a/C2b · C4 → C4a/C4b · D5 → D5a/D5b |
| MERGE | 0 | — |
| DROP | 0 | — |
| DEFER | 0 | — |

**Parked reconfirmed** (carried in, *outside* the 13 live intake): **D6 = DEFER.**

**Net propositions surviving R3.1-B:** 10 KEEP + 6 from splits = **16 live provisions** (from 13 live intake rows; 0 DROP / 0 DEFER *within* intake). Parked, accounted separately: D6 (DEFER).

### Coverage delta vs R3.0 intake (falsification finding — **no mint**; carried to R3.1-F / closeout for an intake decision)

Literal reading against the authentic text surfaced **three operative Chapter II–III provisions absent from the R3.0 row set**. Recorded transparently, not minted, not counted above:

- **Art. 8(4) — exclusivity ban.** A data holder shall **not make data available to a recipient on an exclusive basis** unless the user so requests under Chapter II. Operative and planning-material (blocks single-recipient data lock-in) → recommend carrying as a new Chapter III candidate.
- **Art. 12(1) — Chapter III applicability gate.** The scope predicate ("obliged under Art. 5 or other Union/national law to make data available in B2B") that triggers the whole D3–D5/D7 series; presently embedded in row *triggers*, not its own row → recommend recording as the Chapter III scope gate (parallel to R-B4 for Ch. VI).
- **Art. 12(2) — Chapter III anti-waiver.** A contractual term that, to a party's (or the user's) detriment, excludes, derogates from or varies Chapter III is **not binding** — the Chapter III analogue of Art. 7(2)/R-B7 → recommend carrying as a new candidate.

### Qualifier edges this unit touches (full test in R3.1-F)

- **Q2** B5/B5b (Art. 7 exemption + B5b's inherited Art. 7(1) qualification) ↔ **C1/C3/C6** Ch. II duties — obligation + exemption.
- **Q3** C3 access duty ↔ C5 trade-secret carve-out (Art. 4(6)–(8)) — right + limitation.
- **Q4** C6 sharing right ↔ C7 gatekeeper (Art. 5(3)) + D2 third-party bans (Art. 6(2)) + Art. 5(9)–(11) trade secrets — right + limitations.
- **Q5** D5a compensation ↔ D5b SME/non-profit cost-cap (Art. 9(4)) — default + carve-out.
- **Q15** C1/C3/C6 Ch. II rights ↔ B7 anti-waiver (Art. 7(2)) — right + non-derogation; its **Chapter III analogue is Art. 12(2)** (coverage-delta above).
- **Q16** C3/C6/D1 ↔ B6b personal-data legal-basis condition (Art. 4(12)/5(7)) — right + personal-data condition.
- **New edge (flag for F):** Art. 12(1) Chapter III gate ↔ D3/D4/D5/D7 — scope predicate for the entire Chapter III series.

### Semantic-overreach guard (this unit)

- Access/sharing duties (C3/C6) are never stated bare — each is rendered with its trade-secret carve-out and personal-data condition.
- Chapter III duties (D3/D5) are stated as **conditional on an existing availability obligation** (Art. 12(1) gate), not as a freestanding duty to sell data.
- The gatekeeper exclusion (C7) and third-party ban (D2 point (d)) are recorded with their **DMA dependency** (external), not restated as Data Act-internal designations.
- The coverage-delta provisions (Art. 8(4), 12(1), 12(2)) are recorded as **observations for an intake decision**, not minted as claims.

---

## R3.1-C — Chapters IV–V (unfair terms + B2G exceptional need) + ratification of the R3.1-B Chapter III coverage-delta

**Live intake this unit:** 7 (E1–E3, F1–F4) · **Parked carried in:** F5 (defer, R3.0). **Plus** a formal **intake decision** on the three Chapter III coverage-delta provisions surfaced (already verified) in R3.1-B: Art. 8(4), Art. 12(1), Art. 12(2).
**Source basis (this unit):** the official source pack merged to `main` — `evidence-workbench/eu-data-act/source-pack/EU_Data_Act_Regulation_2023_2854_official_text_EN.pdf` (authentic OJ act, ELI `.../2023/2854/oj`, 71 pp.) read with `EU_Data_Act_Corrigendum_2024_12_09_official_text_EN.pdf`. **Every locator below was read verbatim from that pack — not from memory and not from R3.0 wording.**
**Corrigendum effect on this unit:** **none.** The corrigendum (OJ L, 2024/90790) amends **Article 48 only** (renumbers an item in the Directive (EU) 2020/1828 annex, "68"→"(69)"); it does not touch Art. 8, 12, 13, or 14–22. Recorded so the "read with corrigendum" duty is discharged, not skipped.
**Locators resolved verbatim this unit:** Art. 8(4); Art. 12(1)/(2); Art. 13(1)–(9) (incl. the (4) always-unfair list, the (5) presumed-unfair list + point-(g) proviso, and the (6) "unilaterally imposed" definition); Arts. 14; 15(1)(a)/(1)(b)/(2)/(3); 16(1)/(2); 17(1)/(2)/(3)/(4)/(5)/(6); 18(1)/(2)/(3)/(4)/(5); 19(1)/(2)/(3)/(4); 20(1)/(2)/(3)/(4)/(5); 21(1)–(5); 22.

### C-III. Chapter III coverage-delta intake decision (from R3.1-B — Art. 8(4), 12(1), 12(2))

R3.1-B read Chapter III against the authentic text and surfaced three operative provisions absent from the R3.0 row set, routing the **intake decision** forward. Per that route (and re-verified against the source pack here), all three are **ADOPTED** into the R3.1 live corpus as new Chapter III rows. Identity (`EP-CLM-*`) is still **not** minted — adoption fixes intake, not identity.

| New row | Verdict | Exact locator | Verbatim-grounded proposition | Reason / correction | Dependency |
|---|---|---|---|---|---|
| **R-D8** (Art. 8(4)) | **ADOPT / KEEP** | Art. **8(4)** | "A data holder **shall not make data available to a data recipient, including on an exclusive basis, unless requested to do so by the user under Chapter II**." | **Correction to R3.1-B's shorthand:** this is **not** merely an "exclusivity ban." Literally it bars a data holder from making data available to a recipient **at all** — exclusivity is the *a fortiori* case ("including on an exclusive basis") — unless a **user request under Chapter II** is the origin. Anchors the whole Ch. III availability duty to a user-initiated Ch. II request. | Chapter II user request (R-C6 / Art. 5) |
| **R-D9** (Art. 12(1)) | **ADOPT / KEEP (scope-gate)** | Art. **12(1)** | "This Chapter shall apply where, in business-to-business relations, a data holder **is obliged under Article 5 or under applicable Union law or national legislation** … to make data available to a data recipient." | The **Chapter III applicability gate** — the scope predicate that triggers the entire D-series (R-D3/D4/D5/D7). Not a freestanding duty; the gate for them. Parallel to R-B4 (Ch. VI gate). | Art. 5 / sectoral availability obligation |
| **R-D10** (Art. 12(2)) | **ADOPT / KEEP** | Art. **12(2)** | "A contractual term in a data sharing agreement which, to the detriment of one party, or, where applicable, to the detriment of the user, **excludes the application of this Chapter, derogates from it, or varies its effect, shall not be binding** on that party." | Chapter III **anti-waiver** — the Ch. III analogue of Art. 7(2)/R-B7. Confirmed verbatim. | — |

> This closes the R3.1-B open coverage-delta item ahead of R3.1-F. R3.1-F still runs the full Q-audit; these three now enter it as live rows, not as observations.

### C-IV. Chapter IV — Article 13 (unfair contractual terms unilaterally imposed on another enterprise)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-E1** | **SPLIT** | Art. 13(1) / 13(2) | R3.0 conflated the operative rule with a carve-out, and mislabelled severability as "13(2)". Split: | — |
| → **R-E1a** unenforceability of a unilaterally-imposed **unfair** term | *(KEEP, post-split)* | Art. **13(1)** | "A contractual term … which has been **unilaterally imposed** by an enterprise on another enterprise, **shall not be binding** on the latter enterprise **if it is unfair**." The operative Ch. IV rule. | scoped by R-E3 (13(6)); defined by R-E2a/b/c | 
| → **R-E1b** mandatory-Union-law carve-out | *(KEEP, post-split)* | Art. **13(2)** | "A contractual term which **reflects mandatory provisions of Union law**, or provisions of Union law which would apply if the contractual terms did not regulate the matter, **shall not be considered to be unfair**." A distinct carve-out, not part of 13(1). | — |
| **R-E2** | **SPLIT** | Art. 13(3) / 13(4) / 13(5) | R3.0 said "blacklist/greylist per 13(3)–(4)" — **locator error**: the general test is 13(3), the **always-unfair (black) list is 13(4)**, the **presumed-unfair (grey) list is 13(5)**. Split into three: | — |
| → **R-E2a** general unfairness test | *(KEEP, post-split)* | Art. **13(3)** | A term is unfair if "it is of such a nature that its use **grossly deviates from good commercial practice in data access and use, contrary to good faith and fair dealing**." | — |
| → **R-E2b** always-unfair list (blacklist) | *(KEEP, post-split)* | Art. **13(4)** points (a)–(c) | "a contractual term **shall be unfair** … if its object or effect is to": (a) exclude/limit liability for intentional acts or gross negligence; (b) exclude remedies for non-performance / liability for breach; (c) give the imposing party the exclusive right to determine data conformity or interpret any term. **Exhaustive as written.** | — |
| → **R-E2c** presumed-unfair list (greylist) + point-(g) proviso | *(KEEP, post-split)* | Art. **13(5)** points (a)–(g) + 2nd subpara. | "shall be **presumed to be unfair** … if its object or effect is to": (a) inappropriately limit remedies/liability or extend the imposed party's liability; (b) allow access/use of the other party's data significantly detrimentally (esp. commercially sensitive / trade-secret / IP data); (c) prevent the imposed party from using its own data / adequately exploiting it; (d) prevent termination within a reasonable period; (e) prevent obtaining a copy of its data; (f) enable termination at unreasonably short notice; (g) enable substantial unilateral change to price or substantive data conditions with no valid reason and no termination right. **Proviso:** point (g) does not affect a reserved right to change an indefinite-duration contract where a valid reason is specified, reasonable notice is given, and the counterparty may terminate at no cost. | — |
| **R-E3** unilaterally-imposed definition + burden of proof | **KEEP (locator corrected)** | Art. **13(6)** *(was "13(5)–(6)")* | "A contractual term shall be considered to be **unilaterally imposed** … if it has been **supplied by one contracting party and the other contracting party has not been able to influence its content despite an attempt to negotiate it**." **Plus:** the supplier **bears the burden** of proving the term was not unilaterally imposed, and may not itself argue the term is unfair. Scopes R-E1a. | — |
| **R-E4** severability | **ADOPT / KEEP (new)** | Art. **13(7)** | "Where the unfair contractual term is **severable** from the remaining terms of the contract, those remaining terms **shall be binding**." R3.0 loosely folded this into E1; it is its own provision. | — |
| **R-E5** main-subject-matter / price-adequacy exclusion | **ADOPT / KEEP (new)** | Art. **13(8)** | "This Article **does not apply** to contractual terms **defining the main subject matter of the contract or to the adequacy of the price**, as against the data supplied in exchange." A material **scope limit** absent from R3.0. | — |
| **R-E6** Chapter IV anti-waiver | **ADOPT / KEEP (new)** | Art. **13(9)** | "The parties to a contract covered by paragraph 1 **shall not exclude the application of this Article, derogate from it, or vary its effects**." Ch. IV analogue of Art. 7(2)/12(2). | — |

**Chapter IV note (semantic-overreach guard):** the black/grey distinction is preserved literally — 13(4) items are unfair *per se*; 13(5) items are *presumptions* rebuttable in principle; the two lists must never be rendered as one flat "unfair terms" list. The unenforceability rule (R-E1a) is never stated without its "unilaterally imposed" scope (R-E3) and its carve-outs (R-E1b/13(2), R-E5/13(8)).

### C-V. Chapter V — Articles 14–22 (B2G data availability on exceptional need)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-F1** B2G availability duty | **KEEP (exclusion corrected & relocated)** | Art. **14** | Where a PSB / Commission / ECB / Union body **demonstrates an exceptional need (per Art. 15)** to use certain data to carry out statutory duties in the public interest, "**data holders that are legal persons, other than public sector bodies**, which hold those data **shall make them available upon a duly reasoned request**." **Correction:** Art. 14 contains **no** micro/small exclusion (R3.0's ⚠verify was wrong to attach it here); the micro/small carve-out is Art. 15(2) and is **route-specific** (see R-F2c). | Art. 15 (need); Art. 17 (request) |
| **R-F2** exceptional need | **SPLIT** | Art. 15 | Two distinct routes + a carve-out + a detail. Split: | — |
| → **R-F2a** public-emergency route | *(KEEP)* | Art. **15(1)(a)** | Data "**necessary to respond to a public emergency**" and the body "is **unable to obtain such data by alternative means** in a timely and effective manner under equivalent conditions." | — |
| → **R-F2b** non-emergency route (non-personal only) | *(KEEP)* | Art. **15(1)(b)(i)–(ii)** | Only **non-personal data**; body acts on Union/national law and has identified **specific data the lack of which prevents a specific public-interest task explicitly provided by law** (e.g. official statistics / emergency mitigation), **and has exhausted all other means** incl. market purchase at market rates. Tightly limited. | — |
| → **R-F2c** micro/small carve-out | *(KEEP)* | Art. **15(2)** | "**Paragraph 1, point (b), shall not apply to microenterprises and small enterprises.**" Carve-out applies **only to the 15(1)(b) non-emergency route** — micro/small remain within the 15(1)(a) emergency route (with compensation under Art. 20(3)). This is the corrected, relocated "micro/small exclusion." | — |
| **R-F6** relationship / criminal-customs-tax carve-out | **ADOPT / KEEP (new)** | Art. **16(1)/(2)** | Ch. V does not affect other reporting/access obligations (16(1)); and **does not apply** to bodies carrying out prevention/investigation/detection/prosecution of criminal or administrative offences, penalty execution, or **customs/taxation administration** (16(2)). A material scope limit on when B2G bites — absent from R3.0. | — |
| **R-F3** requests & compliance | **SPLIT** | Arts. 17 / 18 | R3.0 merged "17–18." Split by actor/function: | — |
| → **R-F3a** request requirements | *(KEEP)* | Art. **17(1)(a)–(j), 17(2)(a)–(i), 17(3)–(6)** | The requesting body must specify data + demonstrate the Art. 15 need + purpose/use/duration + erasure timing + data-protection measures for personal data, etc. (17(1)); requests must be written, clear, specific, **proportionate**, trade-secret-respecting (17(2)); reuse limits (17(3)); delegation/onward to third parties bound by Art. 19 (17(4)); model template (17(6)). | Art. 15; Art. 19 |
| → **R-F3b** data-holder compliance + right to decline/modify | *(KEEP; deadlines now verified)* | Art. **18(1)/(2)/(3)/(4)/(5)** | Data holder makes data available without undue delay (18(1)); may **decline or seek modification** — verified deadlines: **no later than 5 working days** for public-emergency requests, **30 working days** otherwise — on grounds (a) no control, (b) duplicate request, (c) request fails Art. 17(1)/(2) (18(2)); anonymise/pseudonymise personal data (18(4)); disputes → competent authority Art. 37 (18(5)). The R3.0 ⚠verify on the periods is **cleared**. | Art. 17; Art. 37 |
| **R-F4** compensation | **SPLIT** | Art. 20 | Emergency-free vs compensation are distinct; plus a micro/small nuance R3.0 missed. Split: | — |
| → **R-F4a** emergency data free | *(KEEP)* | Art. **20(1)** | "**Data holders other than microenterprises and small enterprises** shall make available data necessary to respond to a public emergency … **free of charge**." | — |
| → **R-F4b** fair compensation (non-emergency) + micro/small entitlement | *(KEEP)* | Art. **20(2)/(3)** | For 15(1)(b) requests the data holder is entitled to **fair compensation** covering technical/organisational costs (incl. anonymisation/pseudonymisation/adaptation) **plus a reasonable margin** (20(2)); **20(3)**: this also applies where a **micro/small** enterprise claims compensation — a nuance R3.0's simplification lost. (20(4) removes compensation for official-statistics where market purchase is barred by national law.) | — |
| **R-F5** PSB obligations & bounded onward-sharing | **SPLIT + UN-DEFER** | Arts. 19 / 21 | R3.0 parked "Arts. 19, 21" as a single **defer**. Verbatim reading shows both are operative, planning-material limits ("B2G is bounded"). Un-defer and split: | — |
| → **R-F5a** PSB use / erasure / trade-secret obligations | *(KEEP; was defer)* | Art. **19(1)/(2)/(3)/(4)** | PSB must not use data incompatibly with purpose, must secure it, and **erase when no longer necessary** (19(1)); must **not** use it to develop a competing connected product/service or share it onward for that purpose (19(2)); trade-secret disclosure only **strictly necessary** with safeguards (19(3)); PSB responsible for security (19(4)). | — |
| → **R-F5b** onward-sharing to research / statistics | *(KEEP; was defer)* | Art. **21(1)–(5)** | PSB may share received data with not-for-profit research/analytics or with national statistical institutes/Eurostat (21(1)), only to not-for-profit / public-interest recipients (21(2)), under the same Art. 17(3)/19 obligations (21(3)), ≤ 6-month retention (21(4)), with notice to the data holder (21(5)). Bounded onward-sharing. | — |
| **Art. 22** mutual assistance / cross-border | **DEFER (confirmed)** | Art. **22** | Authority-to-authority cooperation and cross-border request routing (notify competent authority of the data holder's Member State, Art. 37). Not an entrant obligation; not planning-material as a claim. Confirms the R3.0 §M defer. | — |

**Supporting locators confirmed this unit (attach to operative rows — not minted):** Art. 15(3) (official-statistics market-purchase exception, detail on R-F2b); Art. 17(4) third-party delegation binding under Art. 19 (detail on R-F3a/R-F5a); Art. 19(3) trade-secret safeguard (attaches to R-F5a and to the R-F3a request duty).

### R3.1-C verdict tally

**Chapter IV (3 live intake → 9 provisions):** KEEP 1 (E3) · SPLIT 2 (E1→2, E2→3) · **ADOPT-new 3** (E4/13(7), E5/13(8), E6/13(9)) · DROP 0 · DEFER 0.
**Chapter V (4 live intake + 1 parked-in → 11 provisions):** KEEP 1 (F1) · SPLIT 3 (F2→3, F3→2, F4→2) · **ADOPT-new 1** (F6/Art 16) · **UN-DEFER→KEEP 2** (F5a/Art 19, F5b/Art 21, from parked F5) · DEFER 1 (Art 22).
**Chapter III coverage-delta intake:** ADOPT 3 (R-D8/8(4), R-D9/12(1), R-D10/12(2)).

**Net provisions surviving R3.1-C:** **23** (9 Ch. IV + 11 Ch. V + 3 Ch. III delta). **0 minted.** Next free remains `EP-CLM-000046`.

### Qualifier edges this unit touches (full test in R3.1-F)

- **Q6** R-E1a (13(1) unenforceability) ↔ R-E3 (13(6) "unilaterally imposed" scope) + R-E2a/b/c (13(3)/(4)/(5) fairness tests) + carve-outs R-E1b (13(2)) / R-E5 (13(8)) + severability R-E4 (13(7)). Refined from the R3.0 single edge.
- **Q7** R-F1 (Art 14 duty) ↔ R-F2a/b (Art 15 narrow need) + R-F2c (15(2) micro/small carve-out, 15(1)(b) only) + R-F6 (Art 16(2) criminal/customs/tax carve-out).
- **Q8** R-F1 ↔ R-F4a (20(1) emergency-free) vs R-F4b (20(2)/(3) compensation) — duty + compensation split.
- **New edge (flag for F):** R-D9 (Art 12(1) Ch. III gate) ↔ R-D3/D4/D5/D7 — scope predicate for the whole Ch. III D-series; and R-D8 (Art 8(4)) ↔ R-C6 (Art 5 user request) — availability gated on a user Ch. II request.

### Semantic-overreach guard (this unit)

- Chapter V duties are stated as **conditional on a demonstrated Art. 15 exceptional need** and the Art. 14 "legal persons other than PSBs" actor scope — never as a general "government can demand your data" claim.
- The micro/small carve-out is stated **route-specifically** (15(1)(b) only), not as a blanket B2G exemption.
- Art. 13 black-list (13(4)) vs grey-list (13(5)) kept distinct; presumptions never rendered as *per se* unfairness.
- Art. 8(4) rendered as a **user-request-gated availability limit** (its literal breadth), not narrowed to "exclusivity" as R3.1-B's shorthand had it.
- Authority-to-authority machinery (Art. 22) and pure detail (15(3), 17 procedural minutiae) are recorded as defer/supporting, not inflated into entrant-facing claims.

---

## R3.1-D — Chapters VI–VIII (switching · unlawful third-country access · interoperability & smart contracts)

**Live intake this unit:** 8 (G1–G6, J1, and Art. 34 via I3) · **Parked carried in:** I1 (Art 33), I2 (Art 35) — R3.0 defers.
**Source basis (this unit):** the official source pack on `main` — `source-pack/EU_Data_Act_Regulation_2023_2854_official_text_EN.pdf` (authentic OJ act) read with `source-pack/EU_Data_Act_Corrigendum_2024_12_09_official_text_EN.pdf`. **Every locator and every numeric value below was read verbatim from that pack.**
**Corrigendum effect on this unit:** **none (verified).** The corrigendum (OJ L, 2024/90790) amends **Article 48 only**; it does not touch Arts. 23–36. Re-checked against the corrigendum PDF for this unit.
**Locators resolved verbatim this unit:** Art. 23(a)–(e); 24; 25(1)/(2)(a)(i)–(iv),(b)–(i)/(3)/(4)/(5); 26(a)/(b); 27; 28(1)/(2); 29(1)/(2)/(3)/(4)/(5)/(6)/(7); 30(1)/(2)/(3)/(5)/(6); 31(1)/(2)/(3); 32(1)/(2)/(3)(a)–(c)/(4)/(5); 33(1)(a)–(d)/(2)–(11); 34(1)/(2); 35(1)/(2)/(8); 36(1)(a)–(e)/(2)/(3)/(4).

### Numeric / timing values verified verbatim (the R3.0 ⚠verify set — now cleared)

| Value | Verbatim | Locator |
|---|---|---|
| Max **notice period** to initiate switching | "**shall not exceed two months**" | Art. **25(2)(d)** |
| Mandatory **maximum transitional period** | "**not after the mandatory maximum transitional period of 30 calendar days**" | Art. **25(2)(a)** |
| Minimum **data-retrieval period** | "**at least 30 calendar days**, starting after the termination of the transitional period" | Art. **25(2)(g)** |
| Technical-unfeasibility notice + alternative | notify "**within 14 working days**"; alternative transitional period "**shall not exceed seven months**" | Art. **25(4)** |
| Customer extension of transitional period | "right to extend the transitional period **once**" | Art. **25(5)** |
| **Switching charges abolished** | "**From 12 January 2027**, providers … shall not impose any switching charges" | Art. **29(1)** |
| **Reduced** switching charges (interim) | "**From 11 January 2024 to 12 January 2027** … may impose reduced switching charges" ≤ "**costs … directly linked to the switching process**" | Art. **29(2)/(3)** |
| Standards-compatibility lead time | "**at least 12 months after** the references … were published in the central Union standards repository" | Art. **30(3)** |
| Third-country-access national-body reply window | "**If the addressee has not received a reply within one month**" | Art. **32(3)** |
| In-parallel **egress charges** | "**may impose data egress charges, but only for the purpose of passing on egress costs incurred, without exceeding such costs**" | Art. **34(2)** |

### D-VI. Chapter VI — Switching between data processing services (Arts. 23–31)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-G1** remove obstacles to effective switching | **KEEP** | Art. **23(a)–(e)** | Providers shall take the measures in Arts. 25, 26, 27, 29, 30 and **not impose / shall remove** pre-commercial, commercial, technical, contractual and organisational obstacles inhibiting: (a) termination after the notice period; (b) new contract with a different provider; (c) porting exportable data + digital assets (incl. after a free tier); (d) functional equivalence (Art. 24); (e) unbundling where technically feasible. | Arts. 25/26/27/29/30 |
| **R-G9** scope of the technical obligations | **ADOPT / KEEP (scope-limiter, new)** | Art. **24** | The responsibilities in Arts. 23, 25, 29, 30 and 34 apply **only to the source provider's** services/contracts/commercial practices. Bounds who owes the duties — absent from R3.0. | — |
| **R-G2** contractual switching terms | **SPLIT** | Art. 25 | Multiple distinct rules incl. hard numerics → split: | — |
| → **R-G2a** written pre-signing contract | *(KEEP)* | Art. **25(1)** | Customer rights + provider obligations on switching set out in a **written contract** made available before signing, storable/reproducible. | — |
| → **R-G2b** mandatory contract contents (with numerics) | *(KEEP)* | Art. **25(2)(a)–(i)** | Must include: switch/port clause within the **30-calendar-day** mandatory max transitional period after the notice period, with assistance/continuity/security duties (a); exit-strategy support (b); termination clause (c); **max notice period ≤ 2 months (d)**; exhaustive exportable-data spec (e)/(f); **≥ 30-calendar-day retrieval period (g)**; full-erasure clause (h); switching charges per Art. 29 (i). | Art. 29 (charges) |
| → **R-G2c** customer options + technical-unfeasibility route | *(KEEP)* | Art. **25(3)/(4)/(5)** | Customer may switch to another provider / to on-prem / erase (3); if the 30-day transition is technically unfeasible, provider notifies **within 14 working days**, justifies, and offers an alternative period **≤ 7 months** with continuity (4); customer may **extend once** (5). | — |
| **R-G3** information obligation | **KEEP** | Art. **26(a)/(b)** | Provider gives the customer info on switching/porting procedures, methods, formats, known restrictions (a), and a reference to an up-to-date **online register** of data structures/formats/standards for the exportable data (b). | — |
| **R-G7** obligation of good faith | **ADOPT / KEEP (new)** | Art. **27** | **All parties, including destination providers,** shall **cooperate in good faith** to make switching effective, enable timely data transfer, and maintain service continuity. Operative duty R3.0 folded into G1's cross-ref. | — |
| **R-G6** contractual transparency on international access/transfer | **KEEP** | Art. **28(1)/(2)** | Providers publish on their websites, kept current: (a) the **jurisdiction** of the ICT infrastructure; (b) a general description of measures to **prevent international governmental access to / transfer of non-personal data** held in the Union where that conflicts with Union/MS law; the websites are listed in all service contracts. Companion to Art. 32 (Ch. VII). | Art. 32 |
| **R-G4** switching-charge phase-out | **SPLIT** | Art. 29 | Distinct interim vs abolition rules → split: | — |
| → **R-G4a** abolition | *(KEEP)* | Art. **29(1)** | **From 12 January 2027**, no switching charges. | — |
| → **R-G4b** interim reduced charges | *(KEEP)* | Art. **29(2)/(3)** | **11 January 2024 → 12 January 2027**, reduced charges permitted, **not exceeding the costs directly linked** to the switching; plus pre-contract fee/penalty/reduced-charge transparency (29(4)–(6)). | — |
| **R-G5** technical aspects of switching | **SPLIT** | Art. 30 | Tiered by service type → split: | — |
| → **R-G5a** IaaS functional equivalence | *(KEEP)* | Art. **30(1)** | Providers of **infrastructural** services (scalable/elastic compute limited to infra elements, no operating services/software/apps) take all reasonable measures to help the customer **achieve functional equivalence** after switching to the same service type; source provider facilitates with capabilities/info/docs/support/tools. | — |
| → **R-G5b** open interfaces for other services | *(KEEP)* | Art. **30(2)** | **Other** providers make **open interfaces free of charge** to all customers and destination providers, sufficient for portability/interoperability. | — |
| → **R-G5c** standards compatibility + export fallback + limits | *(KEEP)* | Art. **30(3)/(5)/(6)** | Other providers ensure compatibility with common specs/harmonised standards **≥ 12 months after** their publication in the central Union standards repository (3); absent such standards, **export all exportable data in a structured, commonly used, machine-readable format** on request (5); **no duty to develop new tech or disclose IP/trade-secret assets** or compromise security (6). | Art. 35(8) repository |
| **R-G8** specific-regime exemptions | **ADOPT / KEEP (scope carve-out, new)** | Art. **31(1)/(2)/(3)** | Arts. 23(d), 29 and 30(1)&(3) **do not apply** to **custom-built/bespoke** services not offered at broad commercial scale (1); the whole Chapter does not apply to **non-production test/eval** versions for a limited period (2); provider must disclose the non-applicable obligations pre-contract (3). Material scope carve-out absent from R3.0. | — |

### D-VII. Chapter VII — Unlawful third-country governmental access (Art. 32)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-H1** international governmental access safeguard | **SPLIT (wording corrected)** | Art. 32 | R3.0 said "reasonable" measures — literal text is **"all adequate"**. Split into the duty + the two-tier recognition test: | — |
| → **R-H1a** prevention duty | *(KEEP)* | Art. **32(1)** | Providers take **all adequate technical, organisational and legal measures, including contracts**, to **prevent international / third-country governmental access and transfer of non-personal data held in the Union** where that would conflict with Union or Member-State law. | — |
| → **R-H1b** recognition only via international agreement | *(KEEP)* | Art. **32(2)** | A third-country court/tribunal/administrative-authority order to transfer/give access is **recognised or enforceable only if based on an international agreement** (e.g. an MLAT) in force between the third country and the Union or a Member State. | — |
| → **R-H1c** absent-agreement conditions + safeguards | *(KEEP)* | Art. **32(3)(a)–(c), (4), (5)** | Absent such agreement, access/transfer only where the third-country decision is reasoned/proportionate/specific (a), the reasoned objection is court-reviewable (b), and the court can weigh Union-law-protected interests (c); with a national-body opinion mechanism (**one-month** reply window), **minimum-data** disclosure (32(4)), and a duty to **inform the customer before complying** except where law-enforcement necessity requires otherwise (32(5)). | — |

### D-VIII. Chapter VIII — Interoperability & smart contracts (Arts. 33–36)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-I1** data-space essential interoperability requirements | **DEFER — SOURCE-CONSTRAINED (confirmed)** | Art. **33(1)(a)–(d), 33(2)–(11)** | The essential requirements (dataset description; structures/formats; technical access means/APIs; means to enable smart-contract interoperability) bind **participants in data spaces that offer data/services**. Operative detail rests on **delegated acts, harmonised standards and common specifications not yet published** (central repository / OJ, 33(2)–(11)). Material only if the entrant joins a common data space, and the binding specifics are **standards-pending**. Confirms R3.0 defer; flagged source-constrained (freshness watch-item). | forthcoming standards/delegated acts (Reg. (EU) 1025/2012) |
| **R-I3** in-parallel-use interoperability | **SPLIT** | Art. 34 | R3.0 deferred as one row; 34 carries an operative charge rule → split: | — |
| → **R-I3a** switching duties applied mutatis mutandis | *(KEEP)* | Art. **34(1)** | Arts. 23, 24, 25(2)(a)(ii)/(a)(iv)/(e)/(f) and 30(2)–(5) apply **mutatis mutandis** to facilitate interoperability for **in-parallel use** of data processing services. Pointer to already-verified Ch. VI duties. | R-G1/G2b/G5 |
| **R-I4** in-parallel egress charges | **ADOPT / KEEP (new)** | Art. **34(2)** | Where a data processing service is used in parallel with another, providers **may impose data egress charges only to pass on egress costs incurred, without exceeding such costs**. Operative now (no standards dependency); a multi-cloud cost input absent from R3.0. | — |
| **R-I2** interoperability of data-processing-service standards | **DEFER — SOURCE-CONSTRAINED (confirmed)** | Art. **35(1)/(2)/(8)** | Art. 35 sets what open interop specs/harmonised standards **shall** achieve (interoperability, portability, functional equivalence for 30(1) services) and the cloud interop/portability aspects they must address, but the operative standards are **Commission-driven and not yet published** (central repository per 35(8)). Standards-pending watch-item. Confirms R3.0 defer; source-constrained. | forthcoming standards (Reg. (EU) 1025/2012) |
| **R-J1** smart-contract essential requirements + conformity | **KEEP (scope-gated)** | Art. **36(1)(a)–(e), 36(2)/(3)/(4)** | A **vendor/deployer of a smart contract that executes a data-sharing agreement** shall ensure it meets five essential requirements — (a) robustness & access control; (b) safe termination/interruption; (c) data archiving & continuity (auditability); (d) rigorous access control; (e) consistency with the agreement's terms — and shall **perform a conformity assessment and issue an EU declaration of conformity** (36(2)/(3)); harmonised-standards conformity presumption (36(4)). The essential requirements + declaration duty are **operative in the Regulation text itself** (not deferred to standards), so KEEP — scope-gated to entrants that actually deploy smart contracts to execute data sharing. | (conformity presumption) forthcoming harmonised standards |

**Supporting locators confirmed this unit (attach, not minted):** Art. 25(2)(f) trade-secret export exemption (detail on R-G2b); Art. 29(4)–(7) fee-transparency + Commission monitoring delegated act (detail on R-G4b); Art. 30(4) online-register update (detail on R-G5c); Art. 32(3) EDIB guidelines + national-security opinion route (detail on R-H1c).

### R3.1-D verdict tally

**Chapter VI (6 live intake → 14 provisions):** KEEP 3 (G1, G3, G6) · SPLIT 3 (G2→3, G4→2, G5→3) · **ADOPT-new 3** (G7/Art 27, G8/Art 31, G9/Art 24) · DROP 0 · DEFER 0.
**Chapter VII (1 live intake → 3 provisions):** SPLIT 1 (H1→3, wording "reasonable"→"all adequate" corrected).
**Chapter VIII (1 live intake + 2 parked-in):** KEEP 1 scope-gated (J1) · SPLIT 1 (I3→I3a + new I4/Art 34(2)) · **DEFER — SOURCE-CONSTRAINED 2** (I1/Art 33, I2/Art 35 — standards-pending).

**Net live provisions surviving R3.1-D:** **20** (14 Ch. VI + 3 Ch. VII + 3 Ch. VIII). **Source-constrained/deferred:** 2 (I1, I2). **0 minted.** Next free remains `EP-CLM-000046`.

### Qualifier edges this unit touches (full test in R3.1-F)

- **Q9** R-G4a (29(1) abolition 12.1.2027) ↔ R-G4b (29(2)/(3) interim reduced charges) — default + phased carve-out; and ↔ R-G8 (Art 31 bespoke/test-version exemptions from Art 29).
- **Q10** R-G5a (30(1) IaaS functional equivalence) ↔ R-G5b (30(2) other-tier open interfaces) ↔ R-G5c (30(3)/(5) standards/export) — tiered duty; and ↔ R-G8 (Art 31 exemption from 30(1)&(3)).
- **New edge (flag for F):** R-G6 (Art 28 transparency) ↔ R-H1a (Art 32(1) prevention) — disclosure companion to the substantive non-personal-data-sovereignty duty; and R-I3a (Art 34(1)) ↔ R-G1/G2b/G5 — parallel-use reuse of the switching duties.

### Semantic-overreach guard (this unit)

- All Chapter VI numerics are quoted **verbatim** with their exact units (calendar days vs working days vs months) and never approximated; the "~2 months / ~30 days" R3.0 shorthands are replaced by the exact "≤ two months", "30 calendar days", "≥ 30 calendar days", "14 working days", "≤ seven months".
- The switching-charge rule is stated as a **two-phase** rule (reduced until, then abolished on, **12 January 2027**), never as a flat "no fees" claim.
- Functional equivalence is stated as **IaaS/infrastructural-only** (Art. 30(1)); other tiers get open-interfaces/export duties — never a blanket "functional equivalence for all cloud."
- Art. 32 is rendered as a **non-personal-data** safeguard with a two-tier recognition test (international agreement, else conditions), distinct from GDPR Chapter V personal-data transfers (seam S8); "all adequate" not "reasonable".
- Interoperability (Arts. 33, 35) is marked **source-constrained** — the binding specifics depend on standards/common specs **not yet published**; no present-tense obligation is asserted beyond the Regulation's own text.
- Smart-contract requirements (Art. 36) are stated **scope-gated** to entrants deploying smart contracts to execute data sharing — not as a general obligation.

---

## R3.1-E — Chapters IX–XI (enforcement · sui generis carve-out · final provisions)

**Live intake this unit:** 4 (K1, K2, K4, K5) · **Parked carried in:** K3 (Arts 38–39, R3.0 defer) · **plus §M register items confirmed** (Arts 41, 42, 45–46, 47–48, 49).
**Source basis (this unit):** the official source pack on `main` — `source-pack/EU_Data_Act_Regulation_2023_2854_official_text_EN.pdf` (authentic OJ act) read with `source-pack/EU_Data_Act_Corrigendum_2024_12_09_official_text_EN.pdf`. **Every locator, date and penalty reference below was read verbatim from that pack.**
**Corrigendum effect on this unit — precise finding: YES, one article in scope is touched.** The corrigendum (OJ L, 2024/90790) amends **Article 48** — it corrects the numbering of the point added to **Annex I of Directive (EU) 2020/1828** from "`68.`" to "`(69)`". Article 48 **is** within R3.1-E scope; however Art. 48 is an **outbound amendment** (it edits another instrument's annex, not a Data Act entrant obligation) and is **excluded/deferred for planning intelligence** (R-K9). So the corrigendum has **no substantive effect on any entrant-facing claim** in R3.1-E — but the touchpoint is recorded here precisely rather than dismissed. (Arts. 37–47, 49–50 are unaffected by the corrigendum.)
**Locators resolved verbatim this unit:** Art. 37(1)–(16) (esp. (2) data coordinator, (3) GDPR-SA/EDPS, (5) tasks, (6)/(7) coordinator + register, (10) main-establishment jurisdiction, (11)/(12)/(13) legal representative); 38(1)–(3); 39(1)–(3); 40(1)/(2)/(3)/(4)/(5); 41; 42(a)–(c); 43; 44(1)/(2)/(3); 45(2)/(6); 46; 47; 48; 49(1)/(2); 50.

### Key procedural / penalty / date values verified verbatim

| Value | Verbatim | Locator |
|---|---|---|
| MS penalty-rules notification deadline | "Member States shall **by 12 September 2025** notify the Commission" | Art. **40(2)** |
| GDPR-fine route scope | fines under GDPR "**Article 83** … up to the amount referred to in **Article 83(5)**" for "infringements of the obligations laid down in **Chapter II, III and V**", by GDPR supervisory authorities "**within their scope of competence**" | Art. **40(4)** |
| EDPS-fine route (new vs R3.0) | for "infringements … in **Chapter V**", the EDPS may impose fines under "**Article 66** of Regulation (EU) 2018/1725 up to the amount referred to in **Article 66(3)**" | Art. **40(5)** |
| Model terms status | Commission "**before 12 September 2025** … develop and recommend **non-binding** model contractual terms … and **non-binding** standard contractual clauses for cloud computing" | Art. **41** |
| Non-EU legal-representative duty | a non-EU entity making connected products available / offering services in the Union "**shall designate a legal representative** in one of the Member States" | Art. **37(11)** |
| Delegated-act objection period | "**within a period of three months** … extended by three months" | Art. **45(6)** |
| Commission evaluation deadline | "**By 12 September 2028**, the Commission shall carry out an evaluation" | Art. **49(1)/(2)** |
| Application dates (Art. 50, re-confirmed) | in force 20th day after OJ (→ 11 Jan 2024); "**It shall apply from 12 September 2025**"; Art. 3(1) after **12 Sept 2026**; Ch. IV contracts after **12 Sept 2025**, legacy from **12 Sept 2027** (indefinite / ≥ 10 y from 11 Jan 2024) | Art. **50** |

### E-IX. Chapter IX — Implementation and enforcement (Arts. 37–42)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-K1** competent authorities & enforcement architecture | **SPLIT** | Art. 37 | R3.0's single "national enforcement" row hides several planning-material rules → split: | — |
| → **R-K1a** competent authorities + data coordinator | *(KEEP)* | Art. **37(1)/(2)/(5)/(6)/(7)** | Each MS designates one+ competent authorities (new or existing); if several, a **data coordinator** as single point of contact facilitating cooperation and assisting in-scope entities; Commission maintains a **public register** of authorities. | — |
| → **R-K1b** personal-data supervision interface | *(KEEP)* | Art. **37(3)** | GDPR **supervisory authorities** monitor this Regulation insofar as personal-data protection is concerned (GDPR Ch. VI/VII mutatis mutandis); the **EDPS** monitors as regards the Commission/ECB/Union bodies. | GDPR 2016/679; Reg. 2018/1725 |
| → **R-K1c** non-EU legal-representative obligation | **ADOPT / KEEP (new — high entrant relevance)** | Art. **37(11)/(12)/(13)** | **A non-EU entity that makes connected products available or offers services in the Union shall designate a legal representative in a Member State**, mandated to be addressed by authorities; until designation, the entity is under the competence of **all** Member States. Directly material to EuraPlan's non-EU audience — absent from R3.0. | — |
| → **R-K1d** jurisdiction / main-establishment rule | *(KEEP)* | Art. **37(10)** | An in-scope entity is under the competence of the MS where it is **established**; if in several, its **main establishment** (head/registered office with principal financial + operational control). | — |
| **R-K3** complaint + effective judicial remedy | **KEEP (un-defer, bounded)** | Arts. **38(1)–(3), 39(1)–(3)** | Affected natural/legal persons may **lodge a complaint** (individually or collectively) with the competent authority of their residence/work/establishment (38); and have a **right to an effective judicial remedy** against binding authority decisions and where an authority fails to act (39). R3.0 deferred; un-deferred as a bounded counterparty-leverage / own-remedy input. Not framed as legal advice. | — |
| **R-K2** penalties | **SPLIT** | Art. 40 | Distinct national + GDPR + EDPS fine routes → split, stated **exactly** (no generalisation): | — |
| → **R-K2a** national penalties | *(KEEP)* | Art. **40(1)/(2)/(3)** | MS lay down **effective, proportionate, dissuasive** penalties; notify the Commission **by 12 September 2025**; a non-exhaustive criteria list (nature/gravity/duration, mitigation, prior infringements, financial benefit, Union annual turnover). | — |
| → **R-K2b** GDPR Art. 83 fine route (Ch. II/III/V) | *(KEEP)* | Art. **40(4)** | For infringements of **Chapters II, III and V**, GDPR **supervisory authorities**, **within their competence**, may impose administrative fines under **GDPR Art. 83 up to the Art. 83(5)** amount. **Not** "any personal-data infringement" — chapter-scoped + SA-competence-scoped. | GDPR 2016/679 |
| → **R-K2c** EDPS fine route (Ch. V) | **ADOPT / KEEP (new)** | Art. **40(5)** | For infringements of **Chapter V**, the **EDPS** may, within its competence, impose fines under **Reg. (EU) 2018/1725 Art. 66 up to Art. 66(3)**. Coverage-delta absent from R3.0. | Reg. 2018/1725 |
| **R-K6** model contractual terms & SCCs | **DEFER (context — non-binding aid)** | Art. **41** | The Commission, **before 12 September 2025**, develops and recommends **non-binding** MCTs (data access/use, incl. reasonable compensation + trade-secret protection) and **non-binding** SCCs for cloud contracts. A drafting aid, **not** an entrant obligation and non-binding → defer/context (ties to source `DATA-SRC-CAND-09`); never render as a mandatory requirement. | — |
| **R-K7** role of the EDIB | **DEFER (confirmed)** | Art. **42(a)–(c)** | EDIB (expert group under Reg. 2022/868 Art. 29) supports consistent application — advises the Commission on Ch. II/III/V/VII enforcement, facilitates cross-border cooperation, advises on standards/implementing/delegated acts. Governance body; not an entrant obligation. | — |

### E-X. Chapter X — Sui generis right under Directive 96/9/EC (Art. 43)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-K4** sui generis DB-right exclusion | **KEEP** | Art. **43** | "The sui generis right provided for in **Article 7 of Directive 96/9/EC shall not apply** when data is **obtained from or generated by a connected product or related service** falling within the scope of this Regulation, in particular in relation to **Articles 4 and 5**." Removes an IP barrier to the Ch. II access/sharing rights. Exact boundary = connected-product/related-service data in scope. | Dir. 96/9/EC Art. 7; Arts. 4/5 |

### E-XI. Chapter XI — Final provisions (Arts. 44–50)

| Row | Verdict | Exact locator | Reason (verbatim-grounded) | Dependency |
|---|---|---|---|---|
| **R-K5** savings clause | **SPLIT** | Art. 44 | Three distinct boundary rules → split: | — |
| → **R-K5a** pre-existing sectoral acts unaffected | *(KEEP)* | Art. **44(1)** | Specific B2B / B2C / (exceptional) B2G data-availability obligations in Union acts **in force on or before 11 January 2024** (and their delegated/implementing acts) **remain unaffected**. | — |
| → **R-K5b** without prejudice to further sector/data-space requirements | *(KEEP)* | Art. **44(2)** | Without prejudice to Union law specifying, for a sector / common European data space / public-interest area, **further requirements** (technical access aspects; limits on data-holder rights over user-provided data; aspects beyond access/use). The Data Act is a **general** layer under sector-specific law. | — |
| → **R-K5c** scientific-research carve-out (except Ch. V) | *(KEEP)* | Art. **44(3)** | **With the exception of Chapter V**, without prejudice to Union/national law providing for access to and use of data for **scientific research** purposes. | — |
| **R-K8** delegation & committee procedure | **REJECT / EXCLUDE** | Arts. **45, 46** | Delegated-act mechanics (45; objection period **3 months** +3) and comitology (46, Committee under Reg. 2022/868 / Reg. 182/2011). Legislative machinery; not an entrant obligation or planning-intelligence claim. Confirms R3.0 §M reject. | — |
| **R-K9** outbound amendments (CPC / representative actions) | **DEFER / EXCLUDE (context)** | Arts. **47, 48** | Art. 47 adds the Data Act to the Annex of Reg. (EU) 2017/2394 (CPC); Art. 48 adds it to Annex I of Directive (EU) 2020/1828 (representative actions). **These amend *other* acts** — a remedy-architecture footnote, not a Data Act obligation. **Corrigendum touches Art. 48 only** (renumber "68"→"(69)"); no substantive effect. Confirms R3.0 §M defer. | — |
| **R-K10** evaluation & review | **REJECT / EXCLUDE** | Art. **49(1)/(2)** | Commission evaluation **by 12 September 2028** (incl. a focused review of Arts. 23–31, 34, 35 on cloud pricing/diversity). Institutional duty on the Commission; not an entrant obligation. Confirms R3.0 A7 / §M. | — |
| **Art. 50** entry into force & application | **MERGE → R3.1-A (dates re-confirmed)** | Art. **50** | Art. 50 is the **source** of the R3.1-A temporal rows (A1–A5); its dates are re-read verbatim here (apply 12.9.2025; Art. 3(1) 12.9.2026; Ch. III post-12.9.2025 law; Ch. IV new post-12.9.2025, legacy from 12.9.2027 with the indefinite / ≥10-y test) and **confirmed unchanged** — no re-verdict, merged into the R3.1-A rows to avoid double-counting. | R3.1-A A1–A5 |

**Supporting locators confirmed this unit (attach, not minted):** Art. 37(5)(a)–(j) authority tasks/powers, 37(14)–(16) info powers + assistance + confidentiality (detail on R-K1a); Art. 37(6)(b)/(c) coordinator publishes Ch. V requests + annual refusal reporting (detail on R-K1a); Art. 45(2)–(5) delegation conditions (detail on R-K8).

### R3.1-E verdict tally

**Chapter IX (2 live intake + 1 parked-in → 8 live provisions + 2 defers):** SPLIT 2 (K1→4, K2→3) · KEEP 1 (K3, un-deferred) · **ADOPT-new 2** (K1c/Art 37(11), K2c/Art 40(5)) · DEFER 2 (K6/Art 41, K7/Art 42).
**Chapter X (1 live intake → 1 provision):** KEEP 1 (K4/Art 43).
**Chapter XI (1 live intake → 3 provisions + machinery):** SPLIT 1 (K5→3) · REJECT/EXCLUDE 2 (K8/Arts 45–46, K10/Art 49) · DEFER/EXCLUDE 1 (K9/Arts 47–48) · MERGE 1 (Art 50 → R3.1-A).

**Net live provisions surviving R3.1-E:** **12** (8 Ch. IX + 1 Ch. X + 3 Ch. XI). **Deferred (context):** 3 (Art 41, Art 42, Arts 47–48). **Rejected/excluded:** Arts 45–46, Art 49. **Merged:** Art 50 → R3.1-A. **0 minted.** Next free remains `EP-CLM-000046`.

### Qualifier edges this unit touches (full test in R3.1-F)

- **Q11** R-K2a (Art 40(1) national penalties) ↔ R-K2b (Art 40(4) GDPR Art 83 fines for Ch. II/III/V, within GDPR-SA competence) ↔ R-K2c (Art 40(5) EDPS fines for Ch. V) — default + two chapter-scoped cross-referenced fine regimes. **Refined** to add the 40(5) EDPS route.
- **Q12** R-K4 (Art 43 carve-out) ↔ the external sui generis DB right (Dir. 96/9/EC Art. 7) — right + carve-out.
- **Q14** R-A1 (Data Act as general layer) ↔ R-K5a/b/c (Art 44 sectoral + research savings) — general + sector-specific carve-out.
- **New edge (flag for F):** R-K1c (Art 37(11) legal representative) ↔ every substantive duty — the enforcement hook by which a non-EU entrant is reached at all.

### Semantic-overreach guard (this unit)

- Penalties are stated **exactly** by route (national 40(1)–(3); GDPR-SA fines for Ch. II/III/V only, 40(4); EDPS fines for Ch. V only, 40(5)) — never a blanket "GDPR-level fines for any Data Act breach."
- The model contractual terms (Art. 41) are stated **non-binding** and as a Commission aid — never as a mandatory requirement.
- The sui generis carve-out (Art. 43) is bounded to **connected-product / related-service data in scope**, not a general abolition of database rights.
- The Art. 44 savings clause is kept **distinct** from the Art. 1(5) GDPR-prevalence boundary (R-B6) — sectoral/research savings, not the personal-data interface.
- Institutional / legislative machinery (Arts. 42, 45, 46, 49) and outbound amendments (Arts. 47, 48) are recorded as defer/reject with reasons, not inflated into entrant-facing claims; the Art. 48 corrigendum touchpoint is recorded, not hidden.
- Art. 50 dates are **not re-verdicted** — merged into the already-falsified R3.1-A rows to prevent double-counting, with the values re-confirmed verbatim.

---

## Running tally (all units)

| Unit | Intake (live) | KEEP | SPLIT (→net) | MERGE | DROP | DEFER | Status |
|---|---|---|---|---|---|---|---|
| R3.1-A Scope & temporal | 14 | 12 | 2 (→4) | 0 | 0 | 0 | **PASS (reviewed)** |
| R3.1-B Ch. II–III | 13 | 10 | 3 (→6) | 0 | 0 | 0 | **complete — reviewed; coverage-delta ratified in R3.1-C** |
| R3.1-C Ch. IV–V (+Ch. III delta) | 7 (+3 delta) | 2 | 5 (→12) | 0 | 0 | 1 | **complete — reviewed (merged PR #59)** |
| R3.1-D Ch. VI–VIII | 8 (+2 parked) | 4 | 5 (→13) | 0 | 0 | 2 | **complete — reviewed (merged PR #60)** |
| R3.1-E Ch. IX–XI | 4 (+1 parked) | 1 | 3 (→10) | 1 | 0 | 3 | **complete — awaiting review** |
| R3.1-F Qualification audit (Q1–Q16) | — | — | — | — | — | — | pending |

> Live-intake counts only. **R3.1-C** additionally **adopts 9 new provisions** not in the R3.0 live-intake columns: 3 Chapter III coverage-delta (R-D8/8(4), R-D9/12(1), R-D10/12(2)), 3 within-Article-13 (R-E4/13(7), R-E5/13(8), R-E6/13(9)), 2 un-deferred Chapter V (R-F5a/Art 19, R-F5b/Art 21), and 1 new Chapter V scope carve-out (R-F6/Art 16) — net **23 provisions** surviving R3.1-C. **R3.1-D** additionally **adopts 4 new provisions** (R-G7/Art 27, R-G8/Art 31, R-G9/Art 24, R-I4/Art 34(2)) — net **20 live provisions** surviving R3.1-D. **R3.1-E** additionally **adopts 2 new provisions** (R-K1c/Art 37(11) non-EU legal representative, R-K2c/Art 40(5) EDPS Ch. V fines), MERGEs Art 50 into R3.1-A, and REJECTs Arts 45–46 + Art 49 — net **12 live provisions** surviving R3.1-E. Parked / deferred rows (carried in or confirmed, outside live intake): **R3.1-A** — A6 = DEFER, A7 = DROP; **R3.1-B** — D6 = DEFER; **R3.1-C** — Art. 22 = DEFER; **R3.1-D** — Art. 33 (I1) + Art. 35 (I2) = DEFER / SOURCE-CONSTRAINED; **R3.1-E** — Art. 41, Art. 42, Arts. 47–48 = DEFER (context); Arts. 45–46, Art. 49 = REJECT / EXCLUDE. **With R3.1-E, all 50 articles (Chapters I–XI) have been falsified verbatim; R3.1-F (Q-audit) closes R3.1.**

**Mint counter: `EP-CLM-*` = 0 · `EP-SRC-*` = 0.** Next free remains `EP-CLM-000046` / `EP-SRC-000006`.

*EuraPlan.com — Sprint R3.1 workbench. Falsification register (living). Not a published website page.*
