# R3.2 — EU Data Act Identity Register (EP-CLM minting)
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.2 Identity Fixation
**Status:** IDENTITY FIXED — **workbench identities only. No public claims.json. No EP-CLM on any live surface.**
**Opened by:** DEC-060 (DECISION_LOG.md)
**Governed by:** CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; EVIDENCE_GRAPH_MODEL.md; SOURCE_POLICY.md; CLAIM_POLICY.md; REFERENCE_GRADE_ROUTE_STANDARD.md v2; DEC-047; DEC-057; DEC-059; DEC-060
**Lineage:** R3.0 discovery → R3.1-A..F falsification (Arts 1–50, CLOSED/PASS) → **R3.2 identity fixation** (this file)
**Date:** 2026-08-31

---

## 1. What this file does (and does not)

R3.2 assigns a **permanent opaque identity** (`EP-CLM-*`) to each of the **87 live provisions** that survived R3.1 falsification, and pins the **source identities** (`EP-SRC-*`, see `R3_2_SOURCE_FIXATION.md`). It fixes identity and lineage; it does **not** write final claim prose (R3.3 human literal verification / R3.4 canonical graph), does **not** create a public `claims.json`, and does **not** touch any live surface.

**Minting rules (carried from CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md + DEC-057/059):**
- **Global opaque sequence only.** IDs are `EP-CLM-000046`..`EP-CLM-000132` — **never** `DATA-CLM-*` / `DA-CLM-*`. IDs are never recycled or renumbered.
- Every minted claim starts `workflow_state: draft`, `validity_state: null`, `published: false`. No `last_verified_at`, no provenance SHA (those are set only by real events in R3.3+).
- **No broad default is minted without its qualifier(s).** The `qualified_by / edge` column carries the R3.1-F Q1–Q16 + N1–N7 constraint edges; a default and its carve-out are minted as a bound pair and must always render together.
- Primary evidentiary basis for **every** claim is `EP-SRC-000006` (the authentic OJ act) read with `EP-SRC-000007` (the corrigendum). External-instrument dependencies (GDPR, DMA, Dir. 96/9/EC, Reg. 2018/1725, Reg. 1025/2012, Dir. 2019/770) are recorded as **dependencies**, pinned to their own `EP-SRC-*` only if/when a claim's rendering quotes them (R3.3+), never as generic nodes (DEC-057 §7).

---

## 2. Identity table (87 minted · EP-CLM-000046 … EP-CLM-000132)

| EP-CLM ID | R3.1 row | Ch | Provision locator | Draft proposition (short) | qualified_by / edge | Source | State |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000046` | R-A1 | I | Title; Art. 1(1); Art. 50 | instrument identity + direct applicability | —; qualified by Q13 (Art 1(5)) & Q14 (Art 44) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-A) |
| `EP-CLM-000047` | R-A2 | XI | Art. 50 (1st para) | entry into force 11 Jan 2024 (derived) | anchors A5b legacy test | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-A) |
| `EP-CLM-000048` | R-A3 | XI | Art. 50 (2nd para) | general application 12 Sep 2025 | Q1 default → A4/A5a/A5b/A6 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-A) |
| `EP-CLM-000049` | R-A4 | II | Art. 50 + Art. 3(1) | Art 3(1) design duty from 12 Sep 2026 | Q1 phasing of C1 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-A) |
| `EP-CLM-000050` | R-A5a | IV | Art. 50 | Ch IV new contracts after 12 Sep 2025 | Q1 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-A) |
| `EP-CLM-000051` | R-A5b | IV | Art. 50 | Ch IV legacy from 12 Sep 2027 (indefinite / ≥10y) | Q1; anchored on A2 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-A) |
| `EP-CLM-000052` | R-B1 | I | Art. 2(5) | 'connected product' definition (with primary-function limiter) | scope-gate | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000053` | R-B2 | I | Art. 2(6) | 'related service' definition (incl. later-connected) | scope-gate | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000054` | R-B3a | I | Art. 2(12) | 'user' definition | scope-gate (seam S2) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000055` | R-B3b | I | Art. 2(13) | 'data holder' definition | scope-gate (seam S2) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000056` | R-B4 | I | Art. 2(8) | 'data processing service' definition | scope-gate to Ch VI | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000057` | R-B5 | II | Art. 7(1) | micro/small exemption from Ch II | Q2 qualifies C1/C3/C6 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000058` | R-B5b | II | Art. 7(1) subpara | medium-<1yr + 1-yr product grace (inherited 7(1) qualifier) | Q2 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000059` | R-B6 | I | Art. 1(5) | data-protection/privacy law prevails on conflict | Q13 qualifies A1 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000060` | R-B6b | II | Arts. 4(12)/5(7) | personal-data legal-basis condition (user ≠ data subject) | Q16 qualifies C3/C6/D1 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000061` | R-B7 | II | Art. 7(2) | anti-waiver of user Ch II rights | Q15 qualifies C1/C3/C6 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-B) |
| `EP-CLM-000062` | R-C1 | II | Art. 3(1) | design-by-default accessibility | default; Q2 exemption, A4 phasing | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000063` | R-C2a | II | Art. 3(2) | connected-product pre-contract info | — | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000064` | R-C2b | II | Art. 3(3) | related-service pre-contract info | — | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000065` | R-C3 | II | Art. 4(1) | data-holder access duty | default; Q3 trade-secret (C5), Q16 (B6b) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000066` | R-C4a | II | Art. 4(13) | holder use limited to contract + no adverse insight | — | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000067` | R-C4b | II | Art. 4(14) | no onward provision of non-personal product data | — | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000068` | R-C5 | II | Art. 4(6)/(7)/(8) | trade-secret graduated carve-out | Q3 qualifies C3 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000069` | R-C6 | II | Art. 5(1) | user right to share with a third party | default; Q4 (C7/D2), Q16 (B6b) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) · Q4/D2 fwd-dep → R3.3-D |
| `EP-CLM-000070` | R-C7 | II | Art. 5(3) | gatekeeper not an eligible third party | Q4 qualifies C6 (DMA dep) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000071` | R-D1 | II | Art. 6(1) | third-party purpose limitation | — | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-C) |
| `EP-CLM-000072` | R-D2 | II | Art. 6(2)(a)-(h) | third-party prohibitions | Q4 qualifies C6 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D · closes C6/Q4 seam) |
| `EP-CLM-000073` | R-D3 | III | Art. 8(1) | FRAND + transparent terms | N1 gated by D9 (Art 12(1)) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000074` | R-D4 | III | Art. 8(3) | non-discrimination between recipients | N1 gated by D9 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000075` | R-D5a | III | Art. 9(1) | reasonable, non-discriminatory compensation | Q5 default | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000076` | R-D5b | III | Art. 9(4) | SME/non-profit cost-cap | Q5 carve-out of D5a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000077` | R-D7 | III | Art. 11(1)/(2)/(3)/(5) | technical protection measures + remedies | bounded by user Art 4/5 rights | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000078` | R-D8 | III | Art. 8(4) | no making-available to a recipient absent user Ch II request | N2 gates D-series (→ C6) | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000079` | R-D9 | III | Art. 12(1) | Chapter III applicability gate | N1 scope predicate for D3/D4/D5/D7 | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-D) |
| `EP-CLM-000080` | R-D10 | III | Art. 12(2) | Chapter III anti-waiver | Q15 analogue | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E · closes Ch III anti-waiver) |
| `EP-CLM-000081` | R-E1a | IV | Art. 13(1) | unenforceability of unilaterally-imposed unfair term | Q6 default; scoped by E3, defined by E2* | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) · E6/Ch IV anti-waiver fwd-dep → R3.3-F |
| `EP-CLM-000082` | R-E1b | IV | Art. 13(2) | mandatory-Union-law carve-out | Q6 qualifies E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000083` | R-E2a | IV | Art. 13(3) | general unfairness test | Q6 defines E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000084` | R-E2b | IV | Art. 13(4) | always-unfair (black) list | Q6 defines E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000085` | R-E2c | IV | Art. 13(5) | presumed-unfair (grey) list + point-(g) proviso | Q6 defines E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000086` | R-E3 | IV | Art. 13(6) | 'unilaterally imposed' definition + burden of proof | Q6 scopes E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000087` | R-E4 | IV | Art. 13(7) | severability | Q6 qualifies E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000088` | R-E5 | IV | Art. 13(8) | main-subject-matter / price-adequacy exclusion | Q6 scope limit on E1a | EP-SRC-000006 (+000007) | **verified·2026-08-31** (R3.3-E) |
| `EP-CLM-000089` | R-E6 | IV | Art. 13(9) | Chapter IV anti-waiver | Q15 analogue | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F · closes Ch IV anti-waiver; completes Q15 triad) |
| `EP-CLM-000090` | R-F1 | V | Art. 14 | B2G availability duty (legal persons other than PSBs) | Q7 default; Q8 compensation | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) · F6/Art 16 carve-out fwd-dep → R3.3-G |
| `EP-CLM-000091` | R-F2a | V | Art. 15(1)(a) | public-emergency route | Q7 qualifies F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000092` | R-F2b | V | Art. 15(1)(b) | non-emergency route (non-personal only) | Q7 qualifies F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000093` | R-F2c | V | Art. 15(2) | micro/small carve-out (15(1)(b) only) | Q7 qualifies F1 route-specifically | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000094` | R-F3a | V | Art. 17(1)/(2)/(3)-(6) | B2G request requirements | procedure on F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000095` | R-F3b | V | Art. 18(1)-(5) | data-holder compliance + decline/modify (5/30 wd) | procedure on F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000096` | R-F4a | V | Art. 20(1) | emergency data free (non micro/small) | Q8 qualifies F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000097` | R-F4b | V | Art. 20(2)/(3) | fair compensation incl. micro/small entitlement | Q8 qualifies F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000098` | R-F5a | V | Art. 19(1)-(4) | PSB use/erasure/trade-secret obligations | bounds B2G (limit on PSB) | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000099` | R-F5b | V | Art. 21(1)-(5) | bounded onward-sharing to research/statistics | bounds B2G | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-F) |
| `EP-CLM-000100` | R-F6 | V | Art. 16(1)/(2) | relationship + criminal/customs/tax carve-out | Q7 scope limit on F1 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G · closes F1/Q7 Ch V scope-limit) |
| `EP-CLM-000101` | R-G1 | VI | Art. 23(a)-(e) | remove obstacles to effective switching | default; Q9/Q10; G8 exemption | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) · G8/Art 31 exemption fwd-dep → R3.3-H |
| `EP-CLM-000102` | R-G9 | VI | Art. 24 | scope of technical obligations (source provider only) | scope-limiter | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000103` | R-G2a | VI | Art. 25(1) | written pre-signing switching contract | — | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000104` | R-G2b | VI | Art. 25(2)(a)-(i) | mandatory contract terms (notice ≤2m; transition 30d; retrieval ≥30d) | — | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000105` | R-G2c | VI | Art. 25(3)/(4)/(5) | customer options + unfeasibility (14wd / ≤7m) | — | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000106` | R-G3 | VI | Art. 26(a)/(b) | information + online register | — | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000107` | R-G7 | VI | Art. 27 | obligation of good faith | cooperation duty | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000108` | R-G6 | VI | Art. 28(1)/(2) | contractual transparency on int'l access/transfer | N3 companion to H1a | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) · N3→H1a cross-ch ref (Block 8) |
| `EP-CLM-000109` | R-G4a | VI | Art. 29(1) | switching charges abolished 12 Jan 2027 | Q9 default | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) · G8/Art 31 exemption fwd-dep → R3.3-H |
| `EP-CLM-000110` | R-G4b | VI | Art. 29(2)/(3) | interim reduced charges ≤ cost | Q9 qualifies G4a | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000111` | R-G5a | VI | Art. 30(1) | IaaS functional equivalence | Q10 default; G8 exemption | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) · G8/Art 31 exemption fwd-dep → R3.3-H |
| `EP-CLM-000112` | R-G5b | VI | Art. 30(2) | open interfaces for other services | Q10 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000113` | R-G5c | VI | Art. 30(3)/(5)/(6) | standards compatibility (≥12m) + export + limits | Q10 | EP-SRC-000006 (+000007) | **verified·2026-09-02** (R3.3-G) |
| `EP-CLM-000114` | R-G8 | VI | Art. 31(1)/(2)/(3) | bespoke + non-production exemptions | Q9/Q10 carve-out | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000115` | R-H1a | VII | Art. 32(1) | prevent third-country gov access to non-personal data | N6 default; N3 (G6) | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000116` | R-H1b | VII | Art. 32(2) | recognition only via international agreement | N6 qualifies H1a | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000117` | R-H1c | VII | Art. 32(3)-(5) | absent-agreement conditions + safeguards | N6 qualifies H1a | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000118` | R-I3a | VIII | Art. 34(1) | in-parallel-use interoperability (mutatis mutandis) | N4 reuses G1/G2b/G5 | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000119` | R-I4 | VIII | Art. 34(2) | in-parallel egress charges ≤ cost | — | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000120` | R-J1 | VIII | Art. 36(1)-(4) | smart-contract essential requirements + EU declaration | N7 scope-gated | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000121` | R-K1a | IX | Art. 37(1)/(2)/(5)/(6)/(7) | competent authorities + data coordinator | enforcement architecture | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000122` | R-K1b | IX | Art. 37(3) | GDPR-SA / EDPS personal-data supervision | interface | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000123` | R-K1c | IX | Art. 37(11)/(12)/(13) | non-EU legal-representative obligation | N5 enforcement hook | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000124` | R-K1d | IX | Art. 37(10) | jurisdiction / main-establishment rule | — | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000125` | R-K3 | IX | Arts. 38(1)-(3), 39(1)-(3) | complaint + effective judicial remedy | bounded remedy | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000126` | R-K2a | IX | Art. 40(1)/(2)/(3) | national penalties (notify 12 Sep 2025) | Q11 default | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000127` | R-K2b | IX | Art. 40(4) | GDPR Art 83 fines for Ch II/III/V (SA competence) | Q11 qualifies K2a | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000128` | R-K2c | IX | Art. 40(5) | EDPS fines for Ch V (Reg 2018/1725 Art 66) | Q11 qualifies K2a | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000129` | R-K4 | X | Art. 43 | sui generis DB-right exclusion (connected-product data) | Q12 carve-out | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000130` | R-K5a | XI | Art. 44(1) | pre-2024 sectoral acts unaffected | Q14 qualifies A1 | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000131` | R-K5b | XI | Art. 44(2) | without prejudice to further sector/data-space requirements | Q14 | EP-SRC-000006 (+000007) | draft |
| `EP-CLM-000132` | R-K5c | XI | Art. 44(3) | scientific-research carve-out (except Ch V) | Q14 | EP-SRC-000006 (+000007) | draft |

---

## 3. Mint tally

- **Minted this phase:** **87** identities — `EP-CLM-000046` … `EP-CLM-000132`.
- **Next free:** `EP-CLM-000133`.
- **By unit:** R3.1-A = 16 · R3.1-B = 16 · R3.1-C = 23 · R3.1-D = 20 · R3.1-E = 12.
- **All** `workflow_state: draft` · `validity_state: null` · `published: false`.

## 4. NOT minted (held out of identity deliberately)

- **Source-constrained / standards-pending (watch-only, internal):** R-I1 (Art. 33) and R-I2 (Art. 35) interoperability essential requirements — no identity minted; they cannot become claims until Commission delegated acts / harmonised standards are published and pinnable. Remain internal watch-items.
- **Deferred (context, not entrant obligations):** Art. 41 (non-binding MCT/SCC), Art. 42 (EDIB), Arts. 47–48 (outbound amendments) — no identity.
- **Rejected / excluded:** Arts. 45–46 (delegation/comitology), Art. 49 (evaluation), Art. 22 (mutual assistance), Art. 7 A6/A7 (defer/drop), Art. 10 (D6 defer) — no identity.
- **Merged (no new identity):** Art. 50 dates were merged into R3.1-A rows A2–A5b, which carry the identities; Art. 50 mints nothing separately.
- **Supporting locators** (definitions/detail that attach to an operative claim rather than stand alone) are not minted — they travel inside the parent claim.

## 5. Constraint carry-forward (verified)
- **Q1–Q16** and **N1–N7** edges from R3.1-F are carried into the `qualified_by / edge` column above; every default row names the carve-out row(s) it must render with. No orphan default was minted.

---

*EuraPlan.com — Sprint R3.2 workbench identity register. Internal. Not a published website page. No public claims.json.*
