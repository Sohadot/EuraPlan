# R3.0 — Discovery Closeout Register
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.0 Source & Claim Discovery
**Recommended state:** **CLOSED / PASS — R3.1 AUTHORIZED** *(recommendation only — the README status flip and the R3.1 authorization stand **pending human review**, per the R3.0 instruction)*
**Working branch:** `claude/r3-0-data-act-discovery-dqiida` (independent R3.0 branch off `main` after merge #50 / DEC-057)
**Date:** 2026-08-24
**Governed by:** DEC-057 · REFERENCE_GRADE_ROUTE_STANDARD.md v2 · EVIDENCE_GRAPH_MODEL.md · CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md · SOURCE_POLICY.md · CLAIM_POLICY.md · FRESHNESS_ENGINE.md · DISCLOSURE_BOUNDARY.md

---

## 1. What R3.0 was asked to answer

Not "write a Data Act page." Two questions:

1. **What is the legal universe** a Data Act claim may rest on? → answered in `R3_0_SOURCE_DISCOVERY.md`.
2. **What material facts deserve to become claims** later? → answered in `R3_0_CANDIDATE_PROPOSITIONS.md`.

R3.0 is discovery + source-pinning-candidate only. It mints nothing and touches no live surface.

---

## 2. Deliverables produced

| Artifact | Role | State |
|---|---|---|
| `R3_0_SOURCE_DISCOVERY.md` | Source Universe — 5 tiers (primary binding · amending/implementing/corrigendum · specific Commission materials · not-yet-admissible · rejected) + Article 50 application-date table | Complete |
| `R3_0_CANDIDATE_PROPOSITIONS.md` | Candidate Proposition Inventory (44 rows, no IDs) + qualification structure (Q1–Q16) + defer/reject register + analytical seeds (S1–S8) + coverage matrix (Ch. I–XI) | Complete |
| `R3_0_DISCOVERY_CLOSEOUT.md` | This register | Complete |
| `evidence-workbench/eu-data-act/README.md` | Workbench status note — branch reference corrected, file table added; **status left OPEN pending review** (no CLOSED flip) | Updated |

No other file was created or modified. No file outside `evidence-workbench/eu-data-act/` was touched.

---

## 3. Close-condition checklist (the R3.0 gate)

R3.0 closes **only** if every condition below holds. Each is verified against the artifacts.

| # | Close condition | Verdict | Evidence |
|---|---|---|---|
| 1 | **Source universe bounded** | ✅ PASS | `SOURCE_DISCOVERY §6`: admissible basis = CAND-01 (authentic act) + CAND-02 (corrigendum); everything else placed below the line with a reason |
| 2 | **Regulation scanned systematically** (not just famous articles) | ✅ PASS | `CANDIDATE_PROPOSITIONS §O` coverage matrix — all 11 chapters / Arts. 1–50 examined; thin chapters deferred *with reasons*, not skipped |
| 3 | **Every candidate carries a provisional provision locator sufficient for literal falsification; exact paragraph/point fixation is an R3.1 exit condition** | ✅ PASS | Every row R-A1…R-K5 (44 rows) carries an Article-level locator adequate to falsify; paragraph/point precision and numeric specifics are flagged `⚠ verify` and are deliberately deferred to R3.1 — this condition no longer over-claims "exact" locators in a discovery phase that still holds `⚠ verify` flags |
| 4 | **No claim IDs minted** | ✅ PASS | 0 `EP-CLM-*` assigned; next free remains `EP-CLM-000046`; rows use non-identity workbench numbers only |
| 5 | **Qualifiers / exceptions identified** | ✅ PASS | `CANDIDATE_PROPOSITIONS §L` — 16 default↔carve-out pairs (Q1–Q16); no default carried without its qualifier flagged |
| 6 | **Deferred / rejected items recorded** | ✅ PASS | `CANDIDATE_PROPOSITIONS §M` register + `SOURCE_DISCOVERY §4–§5` |
| 7 | **Analytical seeds separated from legal claims** | ✅ PASS | `CANDIDATE_PROPOSITIONS §N` — 8 seeds (S1–S8) explicitly marked "not claims, not Decision Utility" and kept in their own section |
| 8 | **No live mutation** | ✅ PASS | No edit to `/regulation/eu-data-act/`, `routes.json`, `llms.txt`, `sitemap.xml`, or any published surface (see §5 non-mutation attestation) |
| 9 | **Candidate corpus valid for R3.1 falsification** | ✅ PASS | 44 located candidates + 16 qualification pairs + a fixed evidentiary target (authentic text + corrigendum) give R3.1 a complete intake |

Additional DEC-057 guardrails confirmed:

| Guardrail | Verdict |
|---|---|
| No `EP-SRC-*` minted (source pinning is candidate-only) | ✅ 0 minted; `EP-SRC-000006` reserved, not consumed |
| Global opaque ID scheme respected; no `DATA-CLM-*` / `DA-CLM-*` invented | ✅ no domain-prefixed IDs anywhere |
| No generic Commission/portfolio source node | ✅ Commission material Tier-2, specific-locator-only, intentionally unminted |
| Claim count follows material truth, not a template/target | ✅ tally in §P labelled descriptive, never a quota |
| Consolidated version separated from authentic act | ✅ CAND-03 reading-aid-only |
| No Publish Gate opened; no parallel CRA/EERS/Protocol/country/sector work | ✅ none |

**Gate result: 9/9 close conditions PASS + all DEC-057 guardrails held.**

---

## 4. Legal facts pinned in this phase (carried into R3.1 as the fixed target)

- **Instrument:** Regulation (EU) 2023/2854 (Data Act) — CELEX `32023R2854`, ELI `http://data.europa.eu/eli/reg/2023/2854/oj`, OJ L, 2023/2854, 22.12.2023; act of 13 December 2023.
- **Corrigendum:** OJ L, 2024/90790, 9.12.2024 — read together with the authentic act before any verbatim locator is trusted.
- **Application state (Art. 50):** in force 11.1.2024; **applies generally from 12.9.2025 (live now)**; Art. 3(1) design duty for products placed on market after **12.9.2026**; Chapter IV legacy contracts from **12.9.2027**; switching charges prohibited from **12.1.2027** (⚠ interim boundary to falsify); Commission review by 12.9.2028.
- **Structure:** 11 chapters, Arts. 1–50, official titles captured in the coverage matrix.
- **Provisions verified verbatim during micro-hardening (§8):** Art. 1(5) (data-protection conflict-prevalence), Art. 2 "related service" (incl. later-connected services), Art. 7(1) (micro/small exemption + partner/linked/sub-contract condition + medium-sized <1yr and 1-year-after-placing transitional grace), Art. 7(2) (anti-waiver), Art. 40(4) (GDPR Art. 83 fines tied to Chapters II/III/V within GDPR-SA competence), Art. 44 (sectoral/research savings clause). Corrigendum `2024/90790` confirmed narrow (renumbers an Art. 48 point 68→69; no substantive obligation change).

---

## 5. Non-mutation attestation

R3.0 produced **only** the three discovery `.md` artifacts and a README status-note update, all inside `evidence-workbench/eu-data-act/`. It did **not**:

- rewrite or create `/regulation/eu-data-act/` HTML;
- create or modify a public `/regulation/eu-data-act/claims.json`;
- add any `routes.json` / `llms.txt` / `sitemap.xml` entry for Data Act claims;
- mint any `EP-CLM-*` or `EP-SRC-*`;
- open any Publish Gate;
- touch the frozen GDPR (EP-REG-002) or AI Act routes, or any CRA/EERS/Protocol/country/sector surface.

*(A `git diff --stat` at commit time is the machine record of this attestation.)*

---

## 6. Handoff to R3.1 (Claim Map & Falsification) — what R3.1 inherits

1. **Fixed evidentiary target:** authentic EUR-Lex text of `32023R2854` **+** corrigendum `2024/90790`. Re-pull verbatim; resolve every `⚠ verify` flag (Arts. 4, 5, 9, 13, 15, 25, 29, 30, 32, 36, 40 paragraph-level specifics and numeric terms).
2. **Candidate corpus:** 44 rows (R-A1…R-K5) to falsify literally — split, merge, or drop; assign identity **only after** falsification, starting at `EP-CLM-000046`.
3. **Qualification pairs:** test Q1–Q16 — decide which become published claim **pairs** with `qualified_by`; no bare default may publish.
4. **Defer/reject register:** revisit §M items only if falsification forces them in.
5. **Analytical seeds (S1–S8):** remain seeds through R3.1; they inform the R3.6 Decision Utility layer, mint nothing, and are not verified facts.
6. **Freshness watch-items:** Art. 3(1) (12.9.2026), switching charges (12.1.2027), Chapter IV legacy (12.9.2027), and standards/implementing acts (CAND-06) need a FRESHNESS_ENGINE.md hook before any claim depending on them is published.

---

## 7. Micro-hardening applied post-review (same branch, no rebuild)

The first-pass review returned **CONDITIONAL PASS — micro-hardening required**. Five corrections were applied on this same branch (no rebuild, no branch rename); the candidate count moved 39 → 44, which is correct, not a regression.

| # | Review point | Correction |
|---|---|---|
| 1 | Commission materials mis-tiered | `SOURCE_DISCOVERY §3/§6`: relabelled **SOURCE_POLICY Tier 1** but **explanatory / non-binding / insufficient alone** for an operative proposition — policy-tier and evidentiary-role split without amending the policy |
| 2 | Source Universe behind current Commission state | Pinned the **real, dated** unminted context candidates: FAQ **v1.4 (22.1.2026)** and the **draft MCT/SCC recommendation (19–20.11.2025)** with official `digital-strategy.ec.europa.eu` locators — no longer "pin when it exists" |
| 3 | Article 7 scope omission | `PROPOSITIONS`: corrected actor (enterprise manufacturing/designing the product or providing the related service, **not** "data holder"); added **R-B5b** (medium-sized <1yr + 1-year-after-placing transitional grace) and **R-B7** (Art. 7(2) anti-waiver) |
| 4 | Three propositions mis-stated | **R-B2** related-service def now includes **later-connected** services; **R-K2** Art. 40(4) now tied to **Chapters II/III/V within GDPR-SA competence** (not "any personal-data infringement"); **R-B6** split from **R-B6b** — Art. 1(5) conflict-prevalence vs Arts. 4(12)/5(7) legal-basis nuance (recital 7 interpretive only); **R-K5** reframed to Art. 44 **sectoral/research savings clause** |
| 5 | Closeout condition #3 over-precise | Reworded to "provisional locator sufficient for literal falsification; exact paragraph/point fixation is an R3.1 exit condition" (§3, condition #3) |

All corrections were made against **verbatim official text** (Arts. 1(5), 2, 7, 40(4), 44 re-pulled 2026-08-24). Qualification pairs updated to 16 (Q1–Q16). No mint, no `EP-SRC-*`, no live mutation introduced by the hardening.

---

## 8. Recommendation

R3.0 meets all nine close conditions (as reworded) and every DEC-057 guardrail, with the five review corrections applied. **Recommended disposition: R3.0 CLOSED / PASS; R3.1 (Claim Map & Falsification) AUTHORIZED.**

Per the governing instruction, the workbench README status flip (`R3.0 OPEN` → `R3.0 CLOSED / PASS — R3.1 AUTHORIZED`) and the actual start of R3.1 are held **pending your review of this delta**. On approval, the README line is flipped, a PR for R3.0 is opened to `main` and merged so the inherited artifacts are authoritative on `main`, and only then does R3.1 begin against the fixed target above.

*EuraPlan.com — Sprint R3.0 workbench. Discovery closeout. Not a published website page.*
