# GDPR Claim Candidates — Sprint R2.0 / R2.1 intake
**Status:** Discovery + falsification prep — **NO `EP-CLM-*` minted**
**Date:** 2026-08-20
**Primary text reviewed for discovery:** Regulation (EU) 2016/679 — CELEX `32016R0679` (EUR-Lex TXT retrieval 2026-08-20)
**Next free claim ID when minting begins:** `EP-CLM-000015`
**Audience filter:** propositions material to **non-EU company European entry planning** only

---

## How to read this map

Each row is a **candidate**, not a claim.

Required falsification fields (R2.1) before any ID reservation:

`Provision → Actor → Condition → Exception → Current state → Planning consequence → Primary source → locator → risk`

Rules:

- If the Article has `unless` / `except` / thresholds / Member State options → list **qualification candidates** in the same row.
- Do not mint a default without its exception companion.
- EDPB/Commission may later `clarify` — they do not replace the Regulation for direct legal propositions.
- Decision utility hints are planning questions, not advice.

---

## Candidate propositions

### A. Instrument & application state

| Cand | Working label | Provision (locator to verify) | Actor | Condition | Known exceptions / qualifications to verify | Planning consequence (entry) | Risk (est.) | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-01 | Instrument identity | Title / CELEX 32016R0679 | — | — | None expected | Cite correct instrument in entry docs | Low | Pending R2.1 |
| GDPR-PROP-CAND-02 | Entry into force | Art. 99(1) | — | 20th day after OJ publication | Confirm calendar date against OJ L 119 | Historical; baseline already active | Low | Pending R2.1 |
| GDPR-PROP-CAND-03 | Application date | Art. 99(2) | — | Applies from **25 May 2018** | None for general application date | GDPR is **baseline active** for entry planning — not a future phase like AI Act Art. 113 | High | Pending R2.1 |

### B. Territorial scope (critical for non-EU)

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-04 | Establishment criterion | Art. 3(1) | Controller / processor with establishment in Union | Processing in context of establishment activities | Regardless of whether processing takes place in the Union | EU entity / branch design changes exposure | High | Pending |
| GDPR-PROP-CAND-05 | Targeting criterion | Art. 3(2)(a) | Controller / processor **not** established in Union | Offering goods/services to data subjects in the Union | Payment not required; factual “offering” test — do not overclaim | Market offer / website / pricing design is an entry gate | High | Pending |
| GDPR-PROP-CAND-06 | Monitoring criterion | Art. 3(2)(b) | Same | Monitoring behaviour of data subjects in the Union | Behaviour must take place within the Union | Analytics / tracking / profiling architecture | High | Pending |
| GDPR-PROP-CAND-07 | Public international law place | Art. 3(3) | Controller not established in Union | Place where Member State law applies by public international law | Narrow; verify before using | Rare; avoid speculative claims | Medium | Maybe defer |

**Qualification note:** Art. 3(2) is **not** “any contact with an EU person.” Candidates 05–06 must stay tethered to (a)/(b) text. Recitals may later clarify but do not expand the operative test without care.

### C. Roles

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-08 | Controller definition | Art. 4(7) | Controller | Determines purposes and means (alone or jointly) | Union/MS law may determine controller | Role map before vendor contracts | High | Pending |
| GDPR-PROP-CAND-09 | Processor definition | Art. 4(8) | Processor | Processes **on behalf of** a controller | Not a controller merely by processing | SaaS/cloud often processor — not automatic | High | Pending |
| GDPR-PROP-CAND-10 | Joint controllers | Art. 26(1)–(2) | Joint controllers | Jointly determine purposes and means | Arrangement required **unless** responsibilities determined by Union/MS law; essence available to data subject | Partnership / marketplace / multi-party products | High | Pending |
| GDPR-PROP-CAND-11 | Representative (definition) | Art. 4(17) + Art. 27 | Representative | Designated in writing when Art. 3(2) applies | **Art. 27(2)** exceptions (public authorities; occasional processing + other conditions — verify full text before minting default duty) | Non-EU entry structure: representative gate | High | Pending — **must split default vs exception** |

### D. Lawful processing architecture

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-12 | Lawfulness bases | Art. 6(1)(a)–(f) | Controller | Processing lawful only if a basis applies | Each basis has its own limits; consent withdrawability; legitimate interests balancing; MS options under 6(2)(3) | Legal-basis matrix per processing activity | High | Pending — likely **multiple claims or one + qualifications** |
| GDPR-PROP-CAND-13 | Principles | Art. 5 | Controller (accountability 5(2)) | Processing must respect principles | Art. 23 may restrict corresponding rights/obligations | Design constraint on product data model | High | Pending |

**Defer for R2 batch-1?** Special categories Art. 9 — material for some sectors; include only if entry planning for AI/SaaS health/biometric paths is in Wave 1 scope. Mark as **CAND-14 deferred** unless product context requires.

| GDPR-PROP-CAND-14 | Special categories | Art. 9 | Controller | Prohibition + exceptions in 9(2) | Extensive exception list — do not publish bare prohibition | Sector-sensitive products | High | **Defer unless needed** |

### E. Accountability / design / processors / records

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-15 | Responsibility of controller | Art. 24 | Controller | Implement appropriate measures; demonstrate compliance | Risk-based; Art. 24(3) codes/cert may be element | Governance / evidence pack for entry | High | Pending |
| GDPR-PROP-CAND-16 | Data protection by design/default | Art. 25 | Controller | Design + default measures | Risk-based; state of the art | Product architecture before EU launch | High | Pending |
| GDPR-PROP-CAND-17 | Processor | Art. 28 | Controller + processor | Only processors providing sufficient guarantees; contract Art. 28(3) | Sub-processors Art. 28(2)(4); standard clauses 28(8) | Vendor / sub-processor graph | High | Pending |
| GDPR-PROP-CAND-18 | Records of processing | Art. 30(1)(2) | Controller / processor | Maintain records | **Art. 30(5)** enterprise/organisation with fewer than 250 employees — exemption **with** conditions (not occasional / risk / special categories — verify full text) | RoPA as entry deliverable; SME gate needs qualification claim | High | Pending — **split default/exception** |

### F. Security, breach, DPIA, DPO

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-19 | Security of processing | Art. 32 | Controller + processor | Appropriate TOMs | Risk-based; Art. 32(1)(a)–(d) list | Security architecture / vendor diligence | High | Pending |
| GDPR-PROP-CAND-20 | Breach → SA | Art. 33(1) | Controller | Notify SA without undue delay / 72h where feasible | **Unless** unlikely to result in a risk to rights/freedoms | Incident playbook before EU ops | High | Pending — **qualified_by** companion |
| GDPR-PROP-CAND-21 | Breach → data subject | Art. 34 | Controller | Communicate when high risk | Exceptions Art. 34(3) | Comms / IR plan | High | Pending |
| GDPR-PROP-CAND-22 | DPIA | Art. 35(1) | Controller | DPIA when high risk (esp. new tech) | Art. 35(3) examples; lists 35(4)(5); Art. 35(10) carve-out for legal basis assessments | Gate before high-risk features | High | Pending |
| GDPR-PROP-CAND-23 | DPO designation | Art. 37(1) | Controller / processor | Designate when (a) public authority (except courts); (b) regular/systematic large-scale monitoring; or (c) large-scale special categories / criminal data | Thresholds are conditional — not universal DPO duty | Org design for non-EU scale-up | High | Pending — **do not claim universal DPO** |

### G. International transfers

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-24 | General principle for transfers | Art. 44 | Controller / processor | Transfer only if Chapter V conditions met | Entire Chapter V is the qualification stack | Transfer architecture before US/cloud stack freeze | High | Pending |
| GDPR-PROP-CAND-25 | Adequacy | Art. 45 | — | Transfer permitted where adequacy decision | Decisions monitored/amended; legacy 95/46 decisions Art. 45(9) | Country / service region selection | High | Pending — state is **time-sensitive** (freshness) |
| GDPR-PROP-CAND-26 | Appropriate safeguards | Art. 46 | Controller / processor | In absence of adequacy, safeguards (incl. SCCs, BCRs, etc.) | Art. 46(2) list; authorisations | Contract / SCC / BCR planning | High | Pending |
| GDPR-PROP-CAND-27 | Derogations for specific situations | Art. 49 | Controller / processor | Narrow derogations | Explicitly exceptional — do not present as primary transfer tool | Avoid “consent for all US transfers” framing | High | Pending — **strict wording** |

### H. Enforcement / penalties (planning signal, not scare copy)

| Cand | Working label | Provision | Actor | Condition | Exceptions / qualifications | Planning consequence | Risk | Mint? |
|---|---|---|---|---|---|---|---|---|
| GDPR-PROP-CAND-28 | Administrative fines framework | Art. 83 | Supervisory authority | Fines up to tiers in Art. 83(4)(5); criteria 83(2) | Turnover / € ceilings; each case facts | Risk register / board framing — cite tiers accurately | High | Pending |
| GDPR-PROP-CAND-29 | Supervisory authority | Art. 51 et seq. (pin minimal set) | SA | Independent SA per Member State | One-stop-shop Art. 56 — complex; may need separate candidates | Country sequencing interacts with lead SA questions | Medium | Split in R2.1 |

---

## Explicitly out of R2 batch-1 (unless discovery forces)

- Full catalogue of data-subject rights Arts. 12–22 as separate claims (may add a **rights-architecture** claim later)
- Codes of conduct / certification deep dive (Arts. 40–43)
- Cooperation / consistency mechanism detail
- Law enforcement Directive border topics

---

## Qualification pairs flagged for R2.1 (mandatory before mint)

| Default candidate | Exception / qualifier candidate |
|---|---|
| CAND-11 representative duty (Art. 27(1)) | Art. 27(2) exceptions |
| CAND-18 records (Art. 30) | Art. 30(5) SME-conditioned exemption |
| CAND-20 breach notify SA (Art. 33(1)) | “unless unlikely to result in a risk…” |
| CAND-23 DPO (Art. 37(1)) | Only when (a)/(b)/(c) — not universal |
| CAND-24–26 transfers | Chapter V stack; Art. 49 not a shortcut |

---

## Decision utility checklist (for each mint in R2.5)

For every minted claim, answer which entry-plan lever it moves:

- [ ] Entity / establishment architecture  
- [ ] Vendor / processor stack  
- [ ] Data-flow / RoPA mapping  
- [ ] Country sequencing / lead SA  
- [ ] EU representative requirement  
- [ ] Transfer design  
- [ ] Procurement / security readiness  
- [ ] High-risk feature / DPIA gate  

---

## R2.0 exit criteria

- [x] Primary CELEX retrieved for discovery  
- [x] Candidate source registry drafted (no EP-SRC minted)  
- [x] Candidate proposition map with exception flags (no EP-CLM minted)  
- [ ] R2.1: complete falsification table per candidate kept for batch-1  
- [ ] Human owner selects batch-1 mint list → then R2.2 verification  

**No page HTML and no `claims.json` in this phase.**

---

*EuraPlan.com — GDPR claim candidates. Not published claims. Not legal advice.*
