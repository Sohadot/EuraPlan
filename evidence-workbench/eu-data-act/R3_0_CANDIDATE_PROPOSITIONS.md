# R3.0 — EU Data Act Candidate Proposition Inventory (Discovery Workbench)
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.0 Source & Claim Discovery
**Status:** DISCOVERY — **NO `EP-CLM-*` MINTED. NO IDs. NO live mutation.**
**Working branch:** `claude/r3-0-data-act-discovery-dqiida`
**Date:** 2026-08-24
**Primary text scanned for discovery:** Regulation (EU) 2023/2854 (Data Act), CELEX `32023R2854`, read together with corrigendum OJ L, 2024/90790 (`DATA-SRC-CAND-01`+`-02`)
**Next free claim ID when minting begins (R3.2, not now):** `EP-CLM-000046` — global opaque sequence only; **never** `DATA-CLM-*` / `DA-CLM-*`
**Audience filter:** propositions material to **non-EU company European entry / expansion planning** only

---

## How to read this workbench

Each row is a **candidate**, identified only by a **workbench row number** (e.g. `R-C1`). These are **not** claim IDs and confer no identity — identity is fixed only after R3.1 falsification, in R3.2. Row numbers may be split, merged, renumbered, or dropped freely.

Fields captured per candidate (the R3.0 contract):

`Proposition · Provision locator · Actor · Trigger/condition · Type (obligation/right/prohibition) · Exception/qualifier · Date/state (if material) · Entry-planning relevance · Source · Discovery status`

**Discovery status values:** `candidate` (clean single proposition) · `split-needed` (default + carve-out, must become a claim *pair* — never publish the default bare) · `defer` (true but not planning-material now / needs a freshness mechanism / needs an instrument not yet pinnable) · `reject` (out of ontology or not an independent legal proposition).

**Rules carried from DEC-057 / CLAIM_POLICY / precedent:**
- A default with an exception is `split-needed` and carries a `qualified_by` companion *when it becomes a claim* — a published default may never render without its qualifier.
- Recitals inform interpretation; they do **not** by themselves found a proposition.
- Article/paragraph locators below are **discovery locators to be re-verified verbatim in R3.1** against the authentic text + corrigendum. Numeric specifics (notice periods, charge dates, thresholds) are flagged `⚠ verify` and are **not** asserted as verified facts here.

---

## A. Instrument & application state

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-A1 | The instrument is Regulation (EU) 2023/2854 (Data Act), directly applicable in all Member States | Title / Art. 1 / Art. 50 | — | — | scope-fact | — | binding | Cite the correct instrument + CELEX in entry docs | CAND-01 | candidate |
| R-A2 | Entered into force 11 January 2024 | Art. 50 | — | 20th day after OJ publication | scope-fact | — | past — baseline | Anchors the 10-year legacy-contract computation | CAND-01 | candidate |
| R-A3 | **Applies generally from 12 September 2025** | Art. 50 | — | — | scope-fact | phased items below | **past — applicable NOW** | The Data Act is *live law* for planning, not a future phase | CAND-01 | candidate |
| R-A4 | Art. 3(1) product-design duty applies to connected products + related services **placed on the market after 12 September 2026** | Art. 50 + Art. 3(1) | manufacturer / designer / seller | product placed on market after the date | obligation | pre-2026-09-12 products out of Art. 3(1) design duty (but Art. 4 access duty can still bite) | **future — ~3 weeks out; roadmap-critical** | Product-design gate for hardware/IoT entrants | CAND-01 | split-needed |
| R-A5 | Chapter IV (unfair terms) applies to contracts concluded after 12.9.2025; and from **12 September 2027** to legacy contracts that are indefinite or expire ≥10y from 11.1.2024 | Art. 50 | contracting enterprises | contract date + duration test | scope-fact | legacy carve-out (a)/(b) | new: in effect; legacy: future | Contract-repapering timeline | CAND-01 | split-needed |
| R-A6 | Chapter III applies to availability obligations under Union/national law entering into force after 12.9.2025 | Art. 50 | data holders under sectoral law | future sectoral mandate | scope-fact | conditional trigger | forward-looking | Sector-specific; watch-item, not a general duty | CAND-01 | defer |
| R-A7 | Commission evaluates the Regulation by 12 September 2028 | Art. 49 | Commission | — | institutional | — | future | Not an entrant obligation | CAND-01 | reject (not planning-material) |

---

## B. Scope, actors & definitions (Chapter I)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-B1 | "Connected product" = an item obtaining, generating or collecting data about its use/environment and able to communicate that data | Art. 2 (def.) | — | — | definition | — | — | Determines whether a product is in scope at all | CAND-01 | candidate |
| R-B2 | "Related service" = digital service (other than an electronic communications service) connected at purchase such that its absence prevents the product's functions | Art. 2 (def.) | — | — | definition | — | — | Bundled-software scoping | CAND-01 | candidate |
| R-B3 | "User" vs "data holder" are distinct roles (user gains/uses the product; data holder controls the data) | Art. 2 (defs.) | user / data holder | — | definition | — | — | **The role you occupy determines every downstream duty** — planning fulcrum (→ seam S2) | CAND-01 | candidate |
| R-B4 | "Data processing service" = a cloud/edge service (IaaS/PaaS/SaaS-type) enabling on-demand network access to scalable computing resources | Art. 2 (def.) | provider | — | definition | — | — | Gate into Chapter VI (switching) | CAND-01 | candidate |
| R-B5 | Chapter II data-sharing duties **do not apply** to a connected product manufactured/designed by, or a related service provided by, a **microenterprise or small enterprise** | Art. 7(1) | data holder that is micro/small | enterprise size | scope-limit | + condition that it is not a subcontractor/partner of a larger firm ⚠ verify | applicable | SME status changes exposure to Ch II | CAND-01 | split-needed |
| R-B6 | The Regulation is **without prejudice to** Union/national data-protection law; it creates no legal basis for personal-data processing | Art. 1(3)/(5) + Art. 44 ⚠ verify | data holder / recipient | personal data involved | scope-boundary | GDPR governs the personal-data layer | applicable | **GDPR interface — do not merge authorities** (→ seam S6) | CAND-01 (+CAND-10 context) | split-needed |

---

## C. Connected products — user access to generated data (Chapter II)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-C1 | Connected products + related services must be **designed so that product/related-service data is, by default, easily, securely and (where relevant) directly accessible to the user** | Art. 3(1) | manufacturer / designer / seller | product placed on market after 12.9.2026 | obligation | date phasing (R-A4) | future (12.9.2026) | Design-by-default gate for IoT/hardware roadmaps | CAND-01 | split-needed |
| R-C2 | Before contract, the seller/provider must give the user specified **information** about the data the product generates and how to access it | Art. 3(2)–(3) ⚠ verify | seller / provider | pre-contract | obligation | — | applicable | Pre-sale disclosure / UX design | CAND-01 | candidate |
| R-C3 | Where data is not directly accessible, the **data holder must make readily available product/related-service data accessible to the user without undue delay, free of charge**, continuously and in real time where relevant | Art. 4(1) ⚠ verify | data holder | user requests / by design | obligation + right | trade-secret carve-out (R-C5); "readily available" scope | applicable | Core access right entrants can rely on / must satisfy | CAND-01 | split-needed |
| R-C4 | A data holder may **use non-personal product data only on the basis of a contract with the user**, and may not use it to derive insights that compete with the user's product | Art. 4(13)–(14) ⚠ verify | data holder | possession of product data | prohibition / limitation | contractual agreement required | applicable | Limits vendor monetisation of device data | CAND-01 | candidate |
| R-C5 | A data holder may **withhold or condition** disclosure to protect **trade secrets**, only under the Article's specified safeguards | Art. 4(6)–(8) ⚠ verify | data holder | data is a protected trade secret | qualifier (exception to R-C3) | strict conditions; not a blanket refusal | applicable | Determines what device data is actually obtainable | CAND-01 | split-needed (companion to R-C3) |
| R-C6 | The **user has the right to have the data shared with a third party** of their choice | Art. 5(1) ⚠ verify | user → data holder | user request | right | third-party-use limits (R-D2); gatekeeper exclusion (R-C7); trade-secret conditions | applicable | Ecosystem/aftermarket access design | CAND-01 | split-needed |
| R-C7 | A **DMA-designated gatekeeper may not be an eligible third-party recipient** under Art. 5 | Art. 5(3) ⚠ verify | gatekeeper | designation under DMA | prohibition | ties to DMA `32022R1925` (CAND-13) | applicable | Rules out certain platform partners as data recipients | CAND-01 | candidate |

---

## D. Third-party recipients & data-holder availability duties (Chapters II–III)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-D1 | A third party receiving data at the user's request may **use it only for the purposes and under the conditions agreed with the user**, subject to Union law | Art. 6(1) ⚠ verify | third-party recipient | receipt of shared data | obligation / limitation | — | applicable | Constrains data-driven business models built on shared data | CAND-01 | candidate |
| R-D2 | A third party **may not** coerce/deceive the user, profile beyond what is necessary, pass data to a gatekeeper, or use the data to develop a **competing connected product** | Art. 6(2) ⚠ verify | third-party recipient | possession of shared data | prohibition | itemised list | applicable | Hard limits on aftermarket data reuse | CAND-01 | candidate |
| R-D3 | Where a data holder is **obliged to make data available** (under this Reg. or other Union law), terms must be **fair, reasonable, non-discriminatory and transparent (FRAND-like)** | Art. 8(1) ⚠ verify | data holder | a legal availability obligation exists | obligation | — | applicable/conditional | Benchmark for data-access contracts | CAND-01 | candidate |
| R-D4 | Such a data holder must **not discriminate** between comparable categories of data recipients | Art. 8(3) ⚠ verify | data holder | making data available | obligation | objectively justified differences allowed | applicable | Level-playing-field guarantee for recipients | CAND-01 | candidate |
| R-D5 | Compensation for making data available must be **reasonable**; where the recipient is an **SME/not-for-profit**, it may **not exceed the costs** directly related to making the data available | Art. 9 ⚠ verify | data holder / recipient | data made available | obligation + qualifier | SME/non-profit cost-cap | applicable | Cost model for buying/selling data access | CAND-01 | split-needed |
| R-D6 | Disputes over data availability/compensation may go to a **certified dispute-settlement body** | Art. 10 ⚠ verify | parties | dispute | procedural right | — | applicable | Remedy channel; secondary to planning | CAND-01 | defer |
| R-D7 | A data holder may apply **technical protection measures** and pursue remedies against unlawful use/disclosure of data | Art. 11 ⚠ verify | data holder | unauthorised use | right | must not impede the user's Art. 4/5 rights | applicable | Protects data holders while bounded by user rights | CAND-01 | candidate |

---

## E. Unfair contractual terms between enterprises (Chapter IV — Art. 13)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-E1 | A contractual term on data access/use/liability that is **unilaterally imposed** on another enterprise and is **unfair is not binding** on that enterprise | Art. 13(1)–(2) ⚠ verify | enterprises (B2B) | term unilaterally imposed + unfair | prohibition (unenforceability) | only unilaterally-imposed terms; only the unfair term (severability) | new contracts now; legacy 12.9.2027 (R-A5) | B2B data-contract drafting/review | CAND-01 | split-needed |
| R-E2 | Terms are unfair per a **blacklist** (always unfair) and a **greylist** (presumed unfair) defined in the Article | Art. 13(3)–(4) ⚠ verify | — | assessing a term | qualifier (defines E1) | list is exhaustive as written ⚠ verify | applicable | Checklist for contract clauses | CAND-01 | candidate (companion to R-E1) |
| R-E3 | "**Unilaterally imposed**" = supplied by one party where the other could not influence the content despite attempting to negotiate | Art. 13(5)–(6) ⚠ verify | — | contract formation | condition (scopes E1) | negotiated terms fall outside | applicable | Determines which contracts are exposed | CAND-01 | candidate (companion to R-E1) |

---

## F. Public-sector exceptional access — B2G (Chapter V)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-F1 | A data holder must **make data available to a public-sector body / EU institution** where the latter demonstrates an **exceptional need** | Art. 14 ⚠ verify | data holder → PSB | exceptional need shown | obligation | micro/small enterprises excluded ⚠ verify | applicable | B2G exposure distinct from B2B (→ seam S5) | CAND-01 | split-needed |
| R-F2 | "**Exceptional need**" is **narrow**: (a) responding to a public emergency; or (b) a limited non-emergency case where lack of data prevents a statutory task | Art. 15 ⚠ verify | PSB | defining the need | condition (scopes F1) | non-emergency route tightly limited | applicable | Bounds how often B2G can be invoked | CAND-01 | candidate (companion to R-F1) |
| R-F3 | Requests must be **specific, proportionate, transparent** and meet stated content requirements; the data holder complies or objects on stated grounds | Arts. 17–18 ⚠ verify | PSB / data holder | a request is made | procedural obligation + right to object | grounds for refusal/modification | applicable | Response playbook for a B2G request | CAND-01 | candidate |
| R-F4 | Data provided for a **public emergency is free**; otherwise the data holder is entitled to **reasonable compensation** | Art. 20 ⚠ verify | data holder | data provided | qualifier | emergency = no charge | applicable | Cost/benefit of B2G exposure | CAND-01 | split-needed |
| R-F5 | Data obtained under exceptional need is subject to **use limits, deletion duties and constrained onward sharing** (incl. to research/statistical bodies) | Arts. 19, 21 ⚠ verify | PSB | holding the data | limitation on PSB | — | applicable | Reassurance that B2G is bounded | CAND-01 | defer |

---

## G. Switching between data-processing services (Chapter VI)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-G1 | Providers of data-processing services must **remove pre-commercial, commercial, technical, contractual and organisational obstacles** to effective switching to another provider or to on-prem | Art. 23 ⚠ verify | cloud/edge provider | customer switches | obligation | — | applicable | Cloud-exit / multi-cloud is now a **legal right**, not a favour (→ seam S4) | CAND-01 | candidate |
| R-G2 | Switching contracts must contain **mandatory terms**: a maximum notice period (⚠ verify ~2 months) and a maximum transition period (⚠ verify ~30 days, extendable on technical infeasibility) | Art. 25 ⚠ verify | provider / customer | contract for the service | obligation + specific limits | extension where technically unfeasible | applicable | Procurement/contract terms for cloud | CAND-01 | split-needed |
| R-G3 | Providers must give **transparent information** on switching procedures, available formats, and known obstacles | Art. 26 ⚠ verify | provider | pre/at contract | obligation | — | applicable | Vendor-diligence checklist | CAND-01 | candidate |
| R-G4 | **Switching charges are being abolished**: reduced (cost-based) charges in an interim window, then **prohibited from 12 January 2027** | Art. 29 ⚠ verify (interim boundary) | provider | switching | obligation + phased date | interim reduced-charge regime before the date | **future — 12.1.2027; egress-fee budgeting input** | Removes a major cloud lock-in cost | CAND-01 | split-needed |
| R-G5 | For **IaaS**, providers must ensure **functional equivalence** after switching; for other service types, best-effort interoperability/export of exportable data | Art. 30 ⚠ verify | provider | switching | obligation + qualifier (IaaS vs other) | functional-equivalence duty limited to IaaS | applicable | Sets realistic migration expectations by service tier | CAND-01 | split-needed |
| R-G6 | Providers must **contractually disclose** the jurisdiction of the ICT infrastructure and measures against non-EU governmental access (bridges to Ch. VII) | Art. 28 ⚠ verify | provider | contract | obligation | — | applicable | Data-sovereignty diligence input | CAND-01 | candidate |

---

## H. International governmental access & transfer safeguards (Chapter VII — Art. 32)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-H1 | Providers must take **reasonable technical, legal and organisational measures** to **prevent international/third-country governmental access or transfer of non-personal data** held in the Union where that would **conflict with Union or Member-State law** | Art. 32 ⚠ verify | data-processing-service provider | third-country access demand | obligation / safeguard | transfer allowed only under specified conditions (int'l agreement / narrow safeguards) | applicable | **Non-personal-data sovereignty** — distinct from GDPR Ch. V transfers (→ seam S8) | CAND-01 | candidate |

---

## I. Interoperability (Chapter VIII — Arts. 33–35)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-I1 | Participants in **data spaces** must meet **essential interoperability requirements** (documented datasets, structures, formats, mechanisms) | Art. 33 ⚠ verify | data-space participants | offering data in a data space | obligation | detail via specs/standards (→ CAND-06) | applicable/forward | Only if entrant joins a common data space | CAND-01 | defer |
| R-I2 | Providers of data-processing services must ensure **interoperability** via open specifications/standards (harmonised standards / common specs) | Art. 35 ⚠ verify | provider | offering the service | obligation | standards may be forthcoming (→ CAND-06) | applicable/forward | Multi-cloud portability substrate | CAND-01 | defer |
| R-I3 | Interoperability for **in-parallel use** of multiple data-processing services | Art. 34 ⚠ verify | provider | multi-service use | obligation | — | applicable/forward | Multi-cloud architecture | CAND-01 | defer |

---

## J. Smart contracts for data sharing (Chapter VIII — Art. 36)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-J1 | A vendor/party offering a **smart contract to execute a data-sharing agreement** must ensure it meets **essential requirements**: robustness/access control, **safe termination/interruption**, data archiving/continuity, and consistency with the agreement's terms | Art. 36 ⚠ verify | smart-contract vendor / deployer | smart contract executes data sharing | obligation | conformity assessment / declaration ⚠ verify | applicable | Material **only** where the entrant actually uses smart contracts to execute data sharing — otherwise defer | CAND-01 | candidate (scope-gated) |

---

## K. Enforcement, remedies & interfaces (Chapters IX–XI)

| Row | Proposition | Provision | Actor | Trigger/condition | Type | Exception/qualifier | Date/state | Entry-planning relevance | Source | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| R-K1 | Each Member State designates **competent authorities** and a **data coordinator**; enforcement is national | Art. 37 ⚠ verify | Member States | — | institutional | — | applicable | Who regulates you, per country | CAND-01 | candidate |
| R-K2 | Member States set **penalties** that are effective, proportionate, dissuasive; for infringements involving **personal data**, the **GDPR Art. 83 fine framework applies** | Art. 40 ⚠ verify | competent authority | infringement | qualifier / cross-reference | GDPR fines for the personal-data layer | applicable | Risk framing — cite accurately, avoid scare copy | CAND-01 (+CAND-10) | split-needed |
| R-K3 | Affected parties have a **right to lodge a complaint** and a **right to an effective judicial remedy** | Arts. 38–39 ⚠ verify | users / recipients | infringement | right | — | applicable | Counterparty leverage / your own remedies | CAND-01 | defer |
| R-K4 | The **sui generis database right does not apply** to databases containing data obtained from or generated by a connected product / related service | Art. 43 ⚠ verify | database maker | connected-product data | limitation on IP right | narrow to such databases | applicable | Removes an IP barrier to data access | CAND-01 (+CAND-14) | candidate |
| R-K5 | The Data Act operates **alongside other Union data law**; where it concerns personal data, **GDPR/ePrivacy prevail** on that layer | Art. 44 + Art. 1 ⚠ verify | all actors | overlap with other acts | boundary rule | GDPR prevails on personal data | applicable | **Governs how Data Act + GDPR stack** (→ seam S6) | CAND-01 | split-needed |

---

## L. Qualification structure discovered (default ↔ carve-out pairs)

Recorded explicitly per R3.0 item 6. These are **relationships noted in discovery**, **not** `qualified_by` edges yet — R3.1 tests whether each must become a claim **pair**. A published default may never render without its qualifier.

| # | Default candidate | Qualifier / exception candidate | Nature |
|---|---|---|---|
| Q1 | R-A3 general application | R-A4/R-A5/R-A6 phased & transitional dates | default + phasing |
| Q2 | R-C1/R-C3/R-C6 access & sharing duties | R-B5 micro/small exemption (Art. 7) | obligation + exemption |
| Q3 | R-C3 access duty | R-C5 trade-secret carve-out (Art. 4(6)–(8)) | right + limitation |
| Q4 | R-C6 user sharing right | R-C7 gatekeeper exclusion (Art. 5(3)) + R-D2 third-party use bans (Art. 6) | right + limitation |
| Q5 | R-D5 reasonable compensation | SME/non-profit cost-cap (Art. 9) | default + carve-out |
| Q6 | R-E1 unfair-term unenforceability | R-E3 "unilaterally imposed" condition + R-E2 fairness lists | rule + scoping condition |
| Q7 | R-F1 B2G availability duty | R-F2 narrow "exceptional need" + micro/small exclusion | obligation + narrow trigger |
| Q8 | R-F1 B2G duty | R-F4 free-in-emergency vs reasonable compensation | duty + compensation carve-out |
| Q9 | R-G4 switching charges | interim reduced-charge regime → full prohibition 12.1.2027 | default + phased carve-out |
| Q10 | R-G5 export/interoperability on switching | IaaS functional-equivalence vs other-tier best-effort | duty + tiered qualifier |
| Q11 | R-K2 national penalties | GDPR Art. 83 for personal-data infringements | default + cross-referenced regime |
| Q12 | R-K4 general sui generis DB right (external law) | Art. 43 carve-out for connected-product data | right + carve-out |
| Q13 | R-A1 Data Act applies | R-B6/R-K5 GDPR prevails on personal-data layer (Art. 1/44) | scope + boundary |

---

## M. Defer / Reject register (kept out of the R3.1 claim intake — for now)

Prevents graph bloat (R3.0 item 7). Each item is true and/or real but is **not** carried into falsification as a candidate claim in this pass.

| Item | Provision | Why deferred / rejected |
|---|---|---|
| Recitals as standalone claims | Recitals 1–130+ | Interpretive only; do not found an independent legal proposition. **Reject** as claim sources; may support wording in R3.1. |
| Commission evaluation/review duty | Art. 49 | Institutional; not an entrant obligation. **Reject** (not planning-material). |
| Dispute-settlement bodies | Art. 10 | Remedy channel; secondary to entry planning. **Defer** — possible single "remedies" claim later. |
| Mutual assistance / cross-border cooperation | Art. 22 | Authority-to-authority; not a duty on entrants. **Defer.** |
| EDIB role | Art. 42 | Governance body; not a direct obligation. **Defer.** |
| Delegation / committee procedure | Arts. 45–46 | Legislative machinery. **Reject** as claims. |
| Outbound amendments (CPC / representative actions) | Arts. 47–48 | Amend *other* acts; only a remedy-architecture footnote. **Defer.** |
| Interoperability essential requirements detail | Arts. 33–35 | Real duties but detail rests on **standards/specs not yet pinnable** (CAND-06). **Defer** — needs freshness mechanism + pinned instrument. Keep 1 high-level candidate (R-I2) alive as watch-item. |
| Smart-contract requirements | Art. 36 | **Scope-gated defer** — only material where the entrant uses smart contracts to execute data sharing. Keep R-J1 conditional. |
| Sector-specific Chapter III triggers | Art. 50 / Art. 12 | Depend on future sectoral law entering into force after 12.9.2025. **Defer** — freshness watch-item. |
| Precise numeric terms (notice/transition periods, interim charge boundary, SME thresholds) | Arts. 25, 29, 9 | Flagged `⚠ verify`; **not asserted** in discovery. Enter R3.1 as falsification targets, not as facts. |

---

## N. Analytical seams (SEEDS ONLY — not claims, not Decision Utility)

Per R3.0 item 8: places where EuraPlan can later build a **unique analytical layer**. These are **seeds**, they mint nothing, and they are **not** verified facts. Recorded separately from the legal candidates above so the two can never be confused.

| Seed | The analytical distinction | Why it is unique planning value |
|---|---|---|
| **S1 — Three access pathways are not one** | Chapter II *user access* ≠ Chapter III *legally-mandated availability* ≠ Chapter V *B2G exceptional need* | Most explainers blur "data access"; the entrant's obligations differ entirely by pathway |
| **S2 — Role allocation is the fulcrum** | Who is *user* vs *data holder* vs *third-party recipient* in a connected-product ecosystem (R-B3) | The same company can be all three across products; role mapping precedes every duty |
| **S3 — When access becomes a contract problem** | The point where a Ch. II/III access question turns into a Ch. IV unfair-terms question | Lets planning connect data architecture to contract drafting |
| **S4 — Switching as a planning obligation, not a portability feature** | Ch. VI reframes cloud-exit as a legal entitlement + a cost that disappears in 2027 (R-G1/G4) | Turns "portability" from a nice-to-have into a procurement + budgeting input |
| **S5 — B2B and B2G are separate rails** | Ch. II/III (private) vs Ch. V (public-sector exceptional need) must not be merged | Different triggers, different compensation, different risk profiles |
| **S6 — Data Act ↔ GDPR interface without merging authorities** | Art. 1/44: Data Act creates no personal-data legal basis; GDPR prevails on that layer (R-B6/R-K5) | High-value clarity; a common failure mode is conflating the two regimes |
| **S7 — Trade secrets as a structural filter on "accessible data"** | Art. 4(6)–(8) shapes what device data is *actually* obtainable (R-C5) | Explains gaps between the headline access right and real-world availability |
| **S8 — Non-personal-data sovereignty is its own axis** | Art. 32 third-country access safeguards sit *beside* GDPR Chapter V, not inside it (R-H1) | Distinct data-localisation-adjacent planning consideration |

---

## O. Coverage Matrix (systematic scan, Chapters I–XI)

Records what was examined, what produced candidates, and where R3.1 must dig deeper — so the claim set rests on the **whole** regulation, not just its famous articles.

| Chapter | Articles | Examined | Produced candidates | Notes / gaps for R3.1 |
|---|---|---|---|---|
| I — General provisions | 1–2 | ✅ | ✅ R-B1…B6, R-A1 | Verify Art. 1(3)/(5) & Art. 2 definition numbers verbatim; definitions drive everything |
| II — B2C/B2B data sharing | 3–7 | ✅ | ✅ R-C1…C7, R-D1…D2, R-B5 | Densest claim area; Art. 4/5 paragraph locators + trade-secret conditions need careful falsification |
| III — Data holders obliged under Union law | 8–12 | ✅ | ✅ R-D3…D7 | FRAND + compensation; Art. 9 SME cost-cap is a split; Art. 12 scope to confirm |
| IV — Unfair contractual terms | 13 | ✅ | ✅ R-E1…E3 | Blacklist/greylist enumeration must be pulled verbatim; transitional dates (R-A5) |
| V — Data availability on exceptional need (B2G) | 14–22 | ✅ | ✅ R-F1…F5 | Arts. 19/21/22 mostly defer; confirm micro/small exclusion + "exceptional need" wording |
| VI — Switching between data-processing services | 23–31 | ✅ | ✅ R-G1…G6 | **Numeric terms (25, 29, 30) flagged ⚠ verify** — do not assert until R3.1; Art. 31 special regime to review |
| VII — Unlawful int'l gov. access | 32 | ✅ | ✅ R-H1 | Confirm scope = non-personal data; transfer-condition safeguards |
| VIII — Interoperability | 33–36 | ✅ | ⚠ mostly defer (R-I1…I3) + R-J1 | Depend on standards/specs not yet pinnable (CAND-06); smart contracts scope-gated |
| IX — Implementation & enforcement | 37–42 | ✅ | ✅ R-K1…K3 | Art. 40 GDPR-fine cross-reference is a split; Arts. 41–42 defer |
| X — Sui generis DB right | 43 | ✅ | ✅ R-K4 | Confirm exact carve-out wording vs Directive 96/9/EC |
| XI — Final provisions | 44–50 | ✅ | ✅ R-A2…A7, R-K5 | Art. 50 dates + Art. 44 boundary are load-bearing; Arts. 45–48 reject/defer |

**Coverage conclusion:** all 11 chapters / Arts. 1–50 were scanned provision-by-provision. Candidate density is concentrated in Chapters II, III, IV, V, VI (the entrant-facing duties). Chapters VIII (interoperability) and parts of IX–XI are legitimately thin on *entry-planning* candidates and are deferred with reasons, not overlooked. No gap is silent.

---

## P. Discovery tally (for the closeout — not a target)

- **Candidate rows captured:** 39 (R-A1…R-K5), of which **candidate** ≈ 22, **split-needed** ≈ 11, **defer** ≈ 5, **reject** ≈ 3 (approximate; R3.1 will split/merge — counts are descriptive, never a quota).
- **Qualification pairs flagged:** 13 (Q1…Q13).
- **Analytical seeds recorded:** 8 (S1…S8) — seeds, not claims.
- **`EP-CLM-*` minted:** **0.** IDs assigned: **0.** Next free remains `EP-CLM-000046`.

*EuraPlan.com — Sprint R3.0 workbench. Discovery artifact. Not a published website page.*
