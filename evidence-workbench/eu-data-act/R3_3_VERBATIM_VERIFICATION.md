# R3.3 — EU Data Act Human Literal (Verbatim) Verification
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.3 Human Literal Verification
**Status:** **R3.3 COMPLETE / PASS — ALL BLOCKS 1–10** — 87/87 `VERIFIED_LITERAL` (Block 1 = 6, Block 2 = 10, Block 3 = 10, Block 4 = 8, Block 5 = 9, Block 6 = 11, Block 7 = 14, Terminal Closeout Blocks 8–10 = 19). Every `EP-CLM-000046..000132` verified; every Q1–Q16 + N1–N7 edge closed. **Internal workbench only — no public claims.json, no live surface, no publication-state advance.**
**Opened by:** DEC-060 (identity minting) → R3.3 verification is the real-event stage that may set `last_verified_at`.
**Governed by:** CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; EVIDENCE_GRAPH_MODEL.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DEC-047; DEC-057; DEC-059; DEC-060
**Method:** each `EP-CLM` located to its exact Article/paragraph in `EP-SRC-000006`, read **with** `EP-SRC-000007`, compared literally, checked for over-breadth and for carried qualifiers.
**Date:** 2026-08-31

---

## 1. Scope of this unit — R3.3-A (Block 1 only)

Verifies **Block 1** of `R3_2_DRAFT_CLAIM_SEQUENCE.md` — *Instrument & temporal scope* (Chapters I / XI, Art. 50) — i.e. the six identities **`EP-CLM-000046` … `EP-CLM-000051`** (rows R-A1 … R-A5b). **No later block is touched.** R3.3 is split per draft-sequence block (owner decision, 2026-08-31) so each verification is literal, not formal.

**Verdict vocabulary:** `VERIFIED_LITERAL` · `NEEDS_REWRITE` · `NEEDS_QUALIFIER` · `SOURCE_CONSTRAINED` · `BLOCKED`. Only `VERIFIED_LITERAL` may receive `last_verified_at`.

**Primary basis:** `EP-SRC-000006` (authentic OJ act, CELEX `32023R2854`, OJ L, 2023/2854, 22.12.2023). **Read with** `EP-SRC-000007` (corrigendum, OJ L, 2024/90790, 9.12.2024). Locators read verbatim from `source-pack/EU_Data_Act_Regulation_2023_2854_official_text_EN.pdf` (Art. 50 at p. 71; Art. 1 at p. 32; Art. 44 at p. 68).

---

## 2. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 50 — "Entry into force and application":**
> "This Regulation shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union." *(para 1)*
> "It shall apply from 12 September 2025." *(para 2)*
> "The obligation resulting from Article 3(1) shall apply to connected products and the services related to them placed on the market after 12 September 2026." *(para 3)*
> "Chapter III shall apply in relation to obligations to make data available under Union law or national legislation adopted in accordance with Union law, which enters into force after 12 September 2025." *(para 4)*
> "Chapter IV shall apply to contracts concluded after 12 September 2025." *(para 5)*
> "Chapter IV shall apply from 12 September 2027 to contracts concluded on or before 12 September 2025 provided that they are: (a) of indefinite duration; or (b) due to expire at least 10 years from 11 January 2024." *(para 6)*
> "This Regulation shall be binding in its entirety and directly applicable in all Member States." *(final sentence)*
> "Done at Strasbourg, 13 December 2023."

**Article 1(1) — "Subject matter and scope":**
> "This Regulation lays down harmonised rules, inter alia, on: (a) the making available of product data and related service data to the user … (b) … by data holders to data recipients; (c) … to public sector bodies, the Commission, the European Central Bank and Union bodies, where there is an exceptional need …; (d) facilitating switching between data processing services; (e) introducing safeguards against unlawful third-party access to non-personal data; and (f) the development of interoperability standards …".

**Article 1(5) — conflict rule (grounds Q13 → R-B6 / EP-CLM-000059):**
> "This Regulation is without prejudice to Union and national law on the protection of personal data, privacy and confidentiality of communications … In the event of a conflict between this Regulation and Union law on the protection of personal data or privacy, or national legislation adopted in accordance with such Union law, the relevant Union or national law on the protection of personal data or privacy shall prevail."

**Article 44 — savings (grounds Q14 → R-K5a/b/c / EP-CLM-000130-132):**
> 44(1): "The specific obligations for the making available of data … in Union legal acts that entered into force on or before 11 January 2024, and delegated or implementing acts pursuant thereto, shall remain unaffected."
> 44(2): "This Regulation is without prejudice to Union law specifying, in light of the needs of a sector, a common European data space, or an area of public interest, further requirements …".
> 44(3): "This Regulation, with the exception of Chapter V, is without prejudice to Union and national law providing for access to and authorising the use of data for scientific research purposes."

---

## 3. Block 1 verification table (6 identities · EP-CLM-000046 … 000051)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Qualifier carried | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000046` | R-A1 | Title; Art. 1(1); Art. 50 final sentence | "binding in its entirety and directly applicable in all Member States" (Art. 50) + Art. 1(1) subject-matter list — identity + direct applicability match source exactly | Not broader — claim asserts only instrument identity + direct applicability, both quoted | **Q13** (Art. 1(5) conflict rule) **and Q14** (Art. 44(1)/(2)/(3) savings) — both located verbatim §2, carried in identity table | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000047` | R-A2 | Art. 50, 1st para | "twentieth day following … publication"; publication OJ L, 2023/2854 of **22.12.2023** → **11 January 2024**. Date is *derived* from para 1 + OJ date, and independently **corroborated verbatim** in Art. 50(6)(b) and Art. 44(1) ("11 January 2024") | Not broader — recorded as *derived* date, not quoted from para 1; corroboration cited | anchors A5b ≥10-year test | **VERIFIED_LITERAL** *(derived, corroborated)* | 2026-08-31 |
| `EP-CLM-000048` | R-A3 | Art. 50, 2nd para | "It shall apply from 12 September 2025." — verbatim | Not broader | **Q1** default; phasing carve-outs A4/A5a/A5b (all Block 1, all VERIFIED below); A6 (Ch. III future-law) is DEFER / unminted watch-item — no minted carve-out omitted | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000049` | R-A4 | Art. 50, 3rd para + Art. 3(1) | "The obligation resulting from Article 3(1) shall apply to connected products and the services related to them **placed on the market after 12 September 2026**." — verbatim; R3.4 prose must keep "placed on the market after" (not a bare "from 12 Sep 2026") | Not broader — full "placed on the market after" trigger retained | Q1 phasing of C1 | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000050` | R-A5a | Art. 50, 5th para | "Chapter IV shall apply to contracts concluded after 12 September 2025." — verbatim | Not broader | Q1 | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000051` | R-A5b | Art. 50, 6th para | "Chapter IV shall apply from 12 September 2027 to contracts concluded on or before 12 September 2025 provided that they are: (a) of indefinite duration; or (b) due to expire at least 10 years from 11 January 2024." — verbatim | Not broader — both limbs (a)/(b) retained; the ≥10-year test anchored on A2 (11.1.2024) | Q1; anchored on A2 | **VERIFIED_LITERAL** | 2026-08-31 |

---

## 4. Tally — R3.3-A (Block 1)

- **Reviewed:** 6 (`EP-CLM-000046` … `EP-CLM-000051`, rows R-A1 … R-A5b).
- **`VERIFIED_LITERAL`:** **6** — `last_verified_at = 2026-08-31` set on all six.
- **`NEEDS_REWRITE`:** 0.
- **`NEEDS_QUALIFIER`:** 0.
- **`SOURCE_CONSTRAINED`:** 0.
- **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the six; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.

## 5. Corrigendum (EP-SRC-000007) effect on Block 1

**NONE.** The corrigendum (OJ L, 2024/90790, 9.12.2024) reads, verbatim: *"On page 70, Article 48: for: '68. …' read: '(69) …'."* — a single recital-numbering fix (**Article 48 only**, in the list amending Directive (EU) 2020/1828). Block 1 covers **Arts. 1, 3(1), 44, 50**; none is touched. Block 1 verification rests on `EP-SRC-000006` unmodified.

## 6. Qualifier / edge check for Block 1

- **Q1** (temporal phasing: A3 default → A4 / A5a / A5b): all four rows are in Block 1; the three minted carve-outs (A4/A5a/A5b) are each `VERIFIED_LITERAL`. **A6** (Ch. III future-law, Art. 50 para 4) is DEFER / unminted (freshness watch-item) — no minted default rendered without a minted carve-out. **PASS.**
- **Q13** (A1 ↔ B6, Art. 1(5)): conflict-prevails text located verbatim (§2). Carried on `EP-CLM-000046`. **PASS.**
- **Q14** (A1 ↔ K5a/K5b/K5c, Art. 44(1)/(2)/(3)): savings text located verbatim (§2). Carried on `EP-CLM-000046`. **PASS.**
- **N1–N7:** none of the N-edges attach to Block 1 rows (they attach to Ch. III/VI/VII/VIII/IX rows in Blocks 4–10). Nothing due in Block 1. **N/A this unit.**

## 7. Guards honoured

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. No claim verified outside Block 1.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed.

## 8. Recommendation — R3.3-B

Proceed to **R3.3-B = Block 2** (*Definitions & boundaries*, Chapters I / II, `EP-CLM-000052` … `EP-CLM-000061`, rows B1–B7) on a fresh branch off `main` after this unit merges. Block 2 introduces the scope-gating definitions plus the GDPR boundary (Q16/B6b) and the anti-waiver rule (Q15/B7) — verify each definition literally and confirm no definition is rendered broader than its Art. 2 text before the Chapter II duties that depend on them (Blocks 3–4) are reached.

---

# R3.3-B — Block 2 (Definitions & boundaries · Chapters I / II)

**Unit status:** **COMPLETE / PASS** — 10/10 `VERIFIED_LITERAL`. **Date:** 2026-08-31. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Block 1 untouched.

## 9. Scope of this unit — R3.3-B (Block 2 only)

Verifies **Block 2** of `R3_2_DRAFT_CLAIM_SEQUENCE.md` — *Definitions & boundaries* (Chapters I / II) — the ten identities **`EP-CLM-000052` … `EP-CLM-000061`** (rows B1, B2, B3a, B3b, B4, B5, B5b, B6, B6b, B7). No Block 3+ claim is touched. Block 2 is entirely **scope-gating definitions (B1–B4)**, **micro/small + medium-sized exemptions (B5/B5b = Q2)**, and **boundary / anti-waiver qualifiers (B6 = Q13, B6b = Q16, B7 = Q15)** — i.e. it verifies the carve-outs and boundaries **ahead of** the Chapter II duties (Block 3) they qualify, per the draft-sequence invariant. **No Block 2 row is a bare default.**

## 10. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 2 — "Definitions":**
> 2(5): "'connected product' means an item that obtains, generates or collects data concerning its use or environment and that is able to communicate product data via an electronic communications service, physical connection or on-device access, and whose primary function is not the storing, processing or transmission of data on behalf of any party other than the user;"
> 2(6): "'related service' means a digital service, other than an electronic communications service, including software, which is connected with the product at the time of the purchase, rent or lease in such a way that its absence would prevent the connected product from performing one or more of its functions, or which is subsequently connected to the product by the manufacturer or a third party to add to, update or adapt the functions of the connected product;"
> 2(8): "'data processing service' means a digital service that is provided to a customer and that enables ubiquitous and on-demand network access to a shared pool of configurable, scalable and elastic computing resources of a centralised, distributed or highly distributed nature that can be rapidly provisioned and released with minimal management effort or service provider interaction;"
> 2(12): "'user' means a natural or legal person that owns a connected product or to whom temporary rights to use that connected product have been contractually transferred, or that receives related services;"
> 2(13): "'data holder' means a natural or legal person that has the right or obligation, in accordance with this Regulation, applicable Union law or national legislation adopted in accordance with Union law, to use and make available data, including, where contractually agreed, product data or related service data which it has retrieved or generated during the provision of a related service;"

**Article 7 — "Scope of business-to-consumer and business-to-business data sharing obligations":**
> 7(1) 1st subpara: "The obligations of this Chapter shall not apply to data generated through the use of connected products manufactured or designed or related services provided by a microenterprise or a small enterprise, provided that that enterprise does not have a partner enterprise or a linked enterprise within the meaning of Article 3 of the Annex to Recommendation 2003/361/EC that does not qualify as a microenterprise or a small enterprise and where the microenterprise and small enterprise is not subcontracted to manufacture or design a connected product or to provide a related service."
> 7(1) 2nd subpara: "The same shall apply to data generated through the use of connected products manufactured by or related services provided by an enterprise that has qualified as a medium-sized enterprise under Article 2 of the Annex to Recommendation 2003/361/EC for less than one year and to connected products for one year after the date on which they were placed on the market by a medium-sized enterprise."
> 7(2): "Any contractual term which, to the detriment of the user, excludes the application of, derogates from or varies the effect of the user's rights under this Chapter shall not be binding on the user."

**Article 4(12) / Article 5(7) — personal-data legal-basis condition (user ≠ data subject):**
> 4(12): "Where the user is not the data subject whose personal data is requested, any personal data generated by the use of a connected product or related service shall be made available by the data holder to the user only where there is a valid legal basis for processing under Article 6 of Regulation (EU) 2016/679 and, where relevant, the conditions of Article 9 of that Regulation and of Article 5(3) of Directive 2002/58/EC are fulfilled."
> 5(7): "Where the user is not the data subject whose personal data is requested, any personal data generated by the use of a connected product or related service shall be made available by the data holder to the third party only where there is a valid legal basis for processing under Article 6 of Regulation (EU) 2016/679 and, where relevant, the conditions of Article 9 of that Regulation and of Article 5(3) of Directive 2002/58/EC are fulfilled."

**Article 1(5) — conflict rule** *(quoted in §2 above; re-used as the B6 anchor)*: "… In the event of a conflict between this Regulation and Union law on the protection of personal data or privacy, or national legislation adopted in accordance with such Union law, the relevant Union or national law on the protection of personal data or privacy shall prevail."

## 11. Block 2 verification table (10 identities · EP-CLM-000052 … 000061)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / qualifier & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000052` | R-B1 | Art. 2(5) | 'connected product' def verbatim incl. primary-function limiter ("whose primary function is not the storing, processing or transmission of data on behalf of any party other than the user") | Not broader — limiter retained | scope-gating **definition** (not a default) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000053` | R-B2 | Art. 2(6) | 'related service' def verbatim incl. later-connected limb ("or which is subsequently connected to the product by the manufacturer or a third party to add to, update or adapt …") | Not broader — both limbs retained | scope-gating **definition** | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000054` | R-B3a | Art. 2(12) | 'user' def verbatim (owner / contractually-transferred temporary user / recipient of related services) | Not broader | scope-gating **definition** (seam S2) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000055` | R-B3b | Art. 2(13) | 'data holder' def verbatim (right/obligation to use and make available data incl. contractually agreed product/related-service data) | Not broader | scope-gating **definition** (seam S2) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000056` | R-B4 | Art. 2(8) | 'data processing service' def verbatim (ubiquitous on-demand access to configurable/scalable/elastic computing resources …) | Not broader | scope-gating **definition** (gates Ch. VI) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000057` | R-B5 | Art. 7(1) 1st subpara | micro/small **exemption** from Ch. II verbatim, incl. full proviso (no disqualifying partner/linked enterprise; not subcontracted) — proviso must be retained in R3.4 prose | Not broader — proviso retained | **Q2** exemption; qualifies **C1/C3/C6 (Block 3, pending)** — carve-out verified ahead of its defaults | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000058` | R-B5b | Art. 7(1) 2nd subpara | medium-sized grace verbatim ("qualified as a medium-sized enterprise … for less than one year and to connected products for one year after … placed on the market") | Not broader | **Q2** (extends B5); qualifies **C1/C3/C6 (Block 3, pending)** | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000059` | R-B6 | Art. 1(5) | data-protection/privacy law **prevails on conflict** verbatim | Not broader | **Q13** boundary; qualifies **A1 (`EP-CLM-000046`, Block 1 — VERIFIED)** — downward dependency satisfied | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000060` | R-B6b | Arts. 4(12) & 5(7) | personal-data legal-basis **condition** verbatim on **both** limbs (user≠data subject → GDPR Art 6 basis + where relevant Art 9 / Art 5(3) e-Privacy) | Not broader — both Art 4(12) & 5(7) carried | **Q16** boundary; qualifies **C3/C6/D1 (Block 3, pending)** — condition verified ahead of its defaults | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000061` | R-B7 | Art. 7(2) | **anti-waiver** of user Ch. II rights verbatim ("Any contractual term which, to the detriment of the user, excludes … derogates from or varies … shall not be binding") | Not broader | **Q15** anti-waiver; qualifies **C1/C3/C6 (Block 3, pending)** | **VERIFIED_LITERAL** | 2026-08-31 |

## 12. Tally — R3.3-B (Block 2)

- **Reviewed:** 10 (`EP-CLM-000052` … `EP-CLM-000061`, rows B1/B2/B3a/B3b/B4/B5/B5b/B6/B6b/B7).
- **`VERIFIED_LITERAL`:** **10** — `last_verified_at = 2026-08-31` set on all ten.
- **`NEEDS_REWRITE`:** 0 · **`NEEDS_QUALIFIER`:** 0 · **`SOURCE_CONSTRAINED`:** 0 · **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the ten; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.
- **Running R3.3 total:** 16/16 `VERIFIED_LITERAL` across Blocks 1–2 (`EP-CLM-000046..000061`).

## 13. Corrigendum (EP-SRC-000007) effect on Block 2

**NONE.** The corrigendum touches **Article 48 only** (recital renumber "68"→"(69)"). Block 2 covers **Arts. 1(5), 2, 4(12), 5(7), 7**; none is touched. Block 2 rests on `EP-SRC-000006` unmodified.

## 14. Qualifier / edge check for Block 2

- **Q2** (micro/small + medium-sized exemption, B5/B5b): both located verbatim (Art. 7(1) two subparas). They are the carve-outs for C1/C3/C6 (Block 3) — verified now, will render with those defaults when Block 3 is reached. **PASS.**
- **Q13** (B6 ↔ A1, Art. 1(5)): boundary located verbatim; qualifies A1, already `VERIFIED` in Block 1. **PASS.**
- **Q15** (B7 anti-waiver, Art. 7(2)): located verbatim; qualifies C1/C3/C6 (Block 3). **PASS.**
- **Q16** (B6b personal-data condition, Arts. 4(12)/5(7)): located verbatim on both limbs; qualifies C3/C6/D1 (Block 3). **PASS.**
- **Other Q1–Q16:** none other attach to Block 2 rows.
- **N1–N7:** none attach to Block 2 rows (they attach to Ch. III/VI/VII/VIII/IX in Blocks 4–10). **N/A this unit.**
- **Default-without-carve-out check:** **N/A** — Block 2 contains no default duty; it is definitions + exemptions + boundaries. Forward dependencies (Q2/Q15/Q16 → Block 3 defaults C1/C3/C6/D1) are recorded above and will be enforced when those defaults are verified. No default was verified as a bare standalone.

## 15. Guards honoured (R3.3-B)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. No claim verified outside Block 2. Block 1 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed.

## 16. Recommendation — R3.3-C

Proceed to **R3.3-C = Block 3** (*Connected-product access, Chapter II*, `EP-CLM-000062` … `EP-CLM-000071`, rows C1–D2) on a fresh branch off `main` after this unit merges. Block 3 carries the **first Chapter II defaults** (Art. 3(1) design-by-default C1, Art. 4(1) access duty C3, Art. 5(1) third-party-sharing right C6) — each must render with the Block 2 carve-outs now verified: **Q2** (B5/B5b exemption), **Q3** (trade-secret C5, in Block 3), **Q15** (B7 anti-waiver), **Q16** (B6b personal-data condition). Verify no Block 3 default without its carve-out present.

---

# R3.3-C — Block 3 (Connected-product access · Chapter II)

**Unit status:** **COMPLETE / PASS** — 10/10 `VERIFIED_LITERAL`. **Date:** 2026-08-31. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Blocks 1–2 untouched.

## 17. Scope of this unit — R3.3-C (Block 3 only)

Verifies **Block 3** of `R3_2_DRAFT_CLAIM_SEQUENCE.md` — *Connected-product access* (Chapter II) — by its **authoritative numeric range `EP-CLM-000062` … `EP-CLM-000071`** (ten identities: rows C1, C2a, C2b, C3, C4a, C4b, C5, C6, C7, **D1**). This is the first block carrying **Chapter II defaults** (C1 design-by-default, C3 access duty, C6 third-party-sharing right); each is checked with its carve-outs.

**⚠ Block-boundary seam recorded (not resolved here):** the draft sequence labels Block 3 "**C1–D2**", but the block's own numeric range `…062`–`…071` ends at **D1** (`EP-CLM-000071` = R-D1 = Art. 6(1)). **D2 = R-D2 = Art. 6(2)(a)–(h) = `EP-CLM-000072`**, which sits in Block 4's numeric range (`…072`–`…079`). The prompt's authoritative range for this unit is `…062`–`…071`, so **D2 is NOT verified here** — it is carried to R3.3-D. This matters because **D2 is one limb of C6's Q4 carve-out** (see C6 below): C6's companion prohibition set is completed only when D2 is verified in R3.3-D. Recommend R3.3-D begin at `…072` (D2).

## 18. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 3 — "Obligation to make product data and related service data accessible to the user":**
> 3(1): "Connected products shall be designed and manufactured, and related services shall be designed and provided, in such a manner that product data and related service data, including the relevant metadata necessary to interpret and use those data, are, by default, easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format, and, where relevant and technically feasible, directly accessible to the user."
> 3(2): "Before concluding a contract for the purchase, rent or lease of a connected product, the seller, rentor or lessor, which may be the manufacturer, shall provide at least the following information to the user, in a clear and comprehensible manner: (a) the type, format and estimated volume of product data …; (b) whether … continuously and in real-time; (c) whether … store data on-device or on a remote server … duration of retention; (d) how the user may access, retrieve or … erase the data …".
> 3(3): "Before concluding a contract for the provision of a related service, the provider … shall provide at least the following information … (a)–(i)" [nature/volume of product & related-service data; use/third-party purposes; identity & address; contact means; how to request sharing/end it; right to complain (Art 37); trade-secret holder identity; contract duration & termination].

**Article 4 — user↔data-holder access:**
> 4(1): "Where data cannot be directly accessed by the user from the connected product or related service, data holders shall make readily available data, as well as the relevant metadata necessary to interpret and use those data, accessible to the user without undue delay, of the same quality as is available to the data holder, easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format and, where relevant and technically feasible, continuously and in real-time. This shall be done on the basis of a simple request through electronic means where technically feasible."
> 4(6): "Trade secrets shall be preserved and shall be disclosed only where the data holder and the user take all necessary measures prior to the disclosure to preserve their confidentiality …" [identify trade-secret data, agree proportionate technical/organisational measures].
> 4(7): "Where there is no agreement on the necessary measures referred to in paragraph 6, or if the user fails to implement the measures … or undermines the confidentiality …, the data holder may withhold or … suspend the sharing of data identified as trade secrets. The decision … shall be duly substantiated and provided in writing … notify the competent authority …".
> 4(8): "In exceptional circumstances, where the data holder who is a trade secret holder is able to demonstrate that it is highly likely to suffer serious economic damage from the disclosure of trade secrets, despite the … measures taken by the user …, that data holder may refuse on a case-by-case basis a request for access to the specific data in question. That demonstration shall be duly substantiated on the basis of objective elements …".
> 4(13): "A data holder shall only use any readily available data that is non-personal data on the basis of a contract with the user. A data holder shall not use such data to derive insights about the economic situation, assets and production methods of, or the use by, the user in any other manner that could undermine the commercial position of that user …".
> 4(14): "Data holders shall not make available non-personal product data to third parties for commercial or non-commercial purposes other than the fulfilment of their contract with the user. Where relevant, data holders shall contractually bind third parties not to further share data received from them."

**Article 5 — user right to share with third parties:**
> 5(1): "Upon request by a user, or by a party acting on behalf of a user, the data holder shall make available readily available data, as well as the relevant metadata … to a third party without undue delay, of the same quality as is available to the data holder, easily, securely, free of charge to the user, in a comprehensive, structured, commonly used and machine-readable format and, where relevant and technically feasible, continuously and in real-time. The data shall be made available by the data holder to the third party in accordance with Articles 8 and 9."
> 5(3): "Any undertaking designated as a gatekeeper, pursuant to Article 3 of Regulation (EU) 2022/1925, shall not be an eligible third party under this Article and therefore shall not: (a) solicit or commercially incentivise a user … to make data available to one of its services …; (b) solicit or commercially incentivise a user to request the data holder to make data available to one of its services …; (c) receive data from a user that the user has obtained pursuant to a request under Article 4(1)."

**Article 6(1) — third-party purpose limitation:**
> 6(1): "A third party shall process the data made available to it pursuant to Article 5 only for the purposes and under the conditions agreed with the user and subject to Union and national law on the protection of personal data including the rights of the data subject insofar as personal data are concerned. The third party shall erase the data when they are no longer necessary for the agreed purpose, unless otherwise agreed with the user in relation to non-personal data."

## 19. Block 3 verification table (10 identities · EP-CLM-000062 … 000071)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / qualifier & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000062` | R-C1 | Art. 3(1) | design-by-default accessibility verbatim ("by default, easily, securely, free of charge … machine-readable … where relevant and technically feasible, directly accessible") | Not broader — "where relevant and technically feasible" limiter on direct access retained | **DEFAULT**; carve-outs **present**: Q2 (B5/B5b micro/small exemption, Block 2 — VERIFIED), A4 phasing (`EP-CLM-000049`, placed-on-market-after-12.9.2026, Block 1 — VERIFIED), Q15 (B7 anti-waiver, Block 2 — VERIFIED) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000063` | R-C2a | Art. 3(2) | connected-product pre-contract info duty verbatim, points (a)–(d) | Not broader — "at least the following" retained | information duty (no external carve-out) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000064` | R-C2b | Art. 3(3) | related-service pre-contract info duty verbatim, points (a)–(i) | Not broader | information duty (no external carve-out) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000065` | R-C3 | Art. 4(1) | data-holder access duty verbatim, incl. "Where data cannot be directly accessed …" scope condition | Not broader — scope condition + "where … technically feasible" retained | **DEFAULT**; carve-outs **present**: **Q3** trade-secret (C5 = `EP-CLM-000068`, this block — VERIFIED below), **Q16** (B6b personal-data condition, Block 2 — VERIFIED), Q15 (B7 anti-waiver, Block 2 — VERIFIED) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000066` | R-C4a | Art. 4(13) | holder use limited to contract + no adverse-insight verbatim | Not broader | limit on data holder (no external carve-out) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000067` | R-C4b | Art. 4(14) | no onward provision of non-personal product data verbatim (+ contractual bind on third parties) | Not broader | limit on data holder | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000068` | R-C5 | Art. 4(6)/(7)/(8) | trade-secret graduated carve-out verbatim: (6) preserve/measures → (7) withhold/suspend on non-agreement/undermining → (8) refuse on serious-economic-damage, case-by-case, substantiated | Not broader — all three tiers + notify-Art 37 duty retained | **Q3** carve-out **of C3** (bound pair, both this block) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000069` | R-C6 | Art. 5(1) | user right to share with third party verbatim (+ "in accordance with Articles 8 and 9" Ch III forward-ref) | Not broader | **DEFAULT**; carve-outs: **Q4** = C7 (`EP-CLM-000070`, this block — VERIFIED) **+ D2** (Art 6(2) prohibitions = `EP-CLM-000072`, **Block 4 — PENDING**, forward dependency ⚠); **Q16** (B6b, Block 2 — VERIFIED); Q15 (B7, Block 2 — VERIFIED). **C6 must not render without both C7 and D2 present** — D2 verified in R3.3-D | **VERIFIED_LITERAL** *(Q4/D2 forward-dependency flagged)* | 2026-08-31 |
| `EP-CLM-000070` | R-C7 | Art. 5(3) | gatekeeper (Reg (EU) 2022/1925 Art 3) not an eligible third party verbatim, incl. (a)/(b)/(c) | Not broader | **Q4** carve-out of C6 (this block). DMA = external dependency, recorded not minted (SOURCE_FIXATION §3) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000071` | R-D1 | Art. 6(1) | third-party purpose limitation verbatim (+ embedded personal-data boundary + erase-when-no-longer-necessary) | Not broader | limit on third party; embeds GDPR/data-subject boundary | **VERIFIED_LITERAL** | 2026-08-31 |

## 20. Tally — R3.3-C (Block 3)

- **Reviewed:** 10 (`EP-CLM-000062` … `EP-CLM-000071`, rows C1/C2a/C2b/C3/C4a/C4b/C5/C6/C7/D1).
- **`VERIFIED_LITERAL`:** **10** — `last_verified_at = 2026-08-31` set on all ten.
- **`NEEDS_REWRITE`:** 0 · **`NEEDS_QUALIFIER`:** 0 · **`SOURCE_CONSTRAINED`:** 0 · **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the ten; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.
- **Running R3.3 total:** 26/26 `VERIFIED_LITERAL` across Blocks 1–3 (`EP-CLM-000046..000071`).

## 21. Corrigendum (EP-SRC-000007) effect on Block 3

**NONE.** The corrigendum touches **Article 48 only**. Block 3 covers **Arts. 3, 4, 5, 6(1)**; none is touched. Block 3 rests on `EP-SRC-000006` unmodified.

## 22. Qualifier / edge check for Block 3

- **Default-with-carve-out (the key Block 3 check):**
  - **C1** (Art 3(1)) default → Q2 exemption (B5/B5b, Block 2 ✓), A4 phasing (`…049`, Block 1 ✓), Q15 anti-waiver (B7, Block 2 ✓). **All present. PASS.**
  - **C3** (Art 4(1)) default → **Q3** trade-secret (C5, this block ✓), **Q16** personal-data (B6b, Block 2 ✓), Q15 (B7, Block 2 ✓). **All present. PASS.**
  - **C6** (Art 5(1)) default → **Q4** = C7 (this block ✓) **+ D2** (Art 6(2), `…072`, **Block 4 — pending**), Q16 (B6b ✓), Q15 (B7 ✓). **One Q4 limb (D2) is a forward dependency to R3.3-D — recorded; C6 must render with both C7 and D2. PASS-with-flag.**
- **Q3** (C5 ↔ C3, Art 4(6)/(7)/(8)): both located verbatim, bound pair both in this block. **PASS.**
- **Q4** (C7 + D2 ↔ C6, Arts 5(3) + 6(2)): C7 located verbatim this block; D2 deferred to Block 4 (numeric-range seam §17). **PASS-with-flag.**
- **Q2 / Q15 / Q16 / A4** (from Blocks 1–2): all already `VERIFIED`; carried onto the Block 3 defaults they qualify. **PASS.**
- **N1–N7:** none attach to Block 3 rows (they attach to Ch. III/VI/VII/VIII/IX in Blocks 4–10). **N/A this unit.**
- **External dependencies recorded (not minted):** DMA `32022R1925` (C7/Art 5(3)); GDPR `32016R0679` / e-Privacy `32002L0058` (D1/Art 6(1), C3/C6 personal-data via B6b) — pinned narrowly only if a rendering quotes them (R3.4+), per `R3_2_SOURCE_FIXATION.md` §3.

## 23. Guards honoured (R3.3-C)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. No claim verified outside Block 3 (D2/`…072` explicitly deferred). Blocks 1–2 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed.

## 24. Recommendation — R3.3-D

Proceed to **R3.3-D = Block 4** (*Data-holder availability, Chapter III*, `EP-CLM-000072` … `EP-CLM-000079`, rows **D2**, D3–D10) on a fresh branch off `main` after this unit merges. **Begin at `EP-CLM-000072` (R-D2 = Art 6(2)(a)–(h) third-party prohibitions)** — it is the deferred limb of C6's Q4 carve-out (§17 seam) and must be verified first so C6's companion set is complete. Then Ch III: N1 (D3/D4 gated by D9/Art 12(1)), N2 (D8/Art 8(4) gate), Q5 (D5a/D5b compensation) — the **N-edges become active from Block 4 onward**; verify each Ch III duty with its Art 12(1) applicability gate (D9) and Art 8(4) user-request gate (D8) present.

---

# R3.3-D — Block 4 (Data-holder availability · Chapter III + C6/Q4 seam close)

**Unit status:** **COMPLETE / PASS** — 8/8 `VERIFIED_LITERAL`. **Date:** 2026-08-31. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Blocks 1–3 untouched. **D2 verified FIRST** to close the C6/Q4 seam carried from R3.3-C.

## 25. Scope of this unit — R3.3-D (Block 4 only)

Verifies **Block 4** by its **authoritative numeric range `EP-CLM-000072` … `EP-CLM-000079`** (eight identities). **First item = D2 (`EP-CLM-000072`, Art. 6(2))** — the deferred limb of C6's Q4 carve-out from R3.3-C — then the Chapter III availability duties. Rows in numeric order: **D2, D3, D4, D5a, D5b, D7, D8, D9**.

**Block-boundary note (continuation of the R3.3-C §17 seam):** numeric range `…072`–`…079` = rows **D2–D9**. The draft-sequence label for Block 4 reads "D3–D10", now **superseded** by the seam correction: **D2** was pulled into this block (its natural numeric home), and **D10 = R-D10 = Art. 12(2) Chapter III anti-waiver = `EP-CLM-000080`** falls in Block 5's numeric range — **not** verified here; it begins R3.3-E. (No D6: R-D6 / Art. 10 dispute settlement was DEFER in R3.1, unminted.)

## 26. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 6(2) — third-party prohibitions (D2):**
> 6(2): "The third party shall not: (a) make the exercise of choices or rights under Article 5 and this Article by the user unduly difficult, including by offering choices … in a non-neutral manner, or by coercing, deceiving or manipulating the user …; (b) notwithstanding Article 22(2), points (a) and (c), of Regulation (EU) 2016/679, use the data it receives for the profiling, unless it is necessary to provide the service requested by the user; (c) make the data it receives available to another third party, unless … on the basis of a contract with the user, and provided that the other third party takes all necessary measures … to preserve the confidentiality of trade secrets; (d) make the data it receives available to an undertaking designated as a gatekeeper pursuant to Article 3 of Regulation (EU) 2022/1925; (e) use the data … to develop a product that competes with the connected product … or share the data … for that purpose; … not … derive insights about the economic situation, assets and production methods of, or use by, the data holder; (f) use the data … in a manner that has an adverse impact on the security of the connected product or related service; (g) disregard the specific measures agreed … pursuant to Article 5(9) and undermine the confidentiality of trade secrets; (h) prevent the user that is a consumer … from making the data it receives available to other parties."

**Article 8 — availability conditions (D3, D4, D8):**
> 8(1) [D3]: "Where, in business-to-business relations, a data holder is obliged to make data available to a data recipient under Article 5 or under other applicable Union law or national legislation adopted in accordance with Union law, it shall agree with a data recipient the arrangements for making the data available and shall do so under fair, reasonable and non-discriminatory terms and conditions and in a transparent manner in accordance with this Chapter and Chapter IV."
> 8(3) [D4]: "A data holder shall not discriminate regarding the arrangements for making data available between comparable categories of data recipients, including partner enterprises or linked enterprises of the data holder … Where a data recipient considers that the conditions … are discriminatory, the data holder shall without undue delay provide … upon its reasoned request … information showing that there has been no discrimination."
> 8(4) [D8]: "A data holder shall not make data available to a data recipient, including on an exclusive basis, unless requested to do so by the user under Chapter II."

**Article 9 — compensation (D5a, D5b):**
> 9(1) [D5a]: "Any compensation agreed upon between a data holder and a data recipient for making data available in business-to-business relations shall be non-discriminatory and reasonable and may include a margin."
> 9(4) [D5b]: "Where the data recipient is an SME or a not-for-profit research organisation and where such a data recipient does not have partner enterprises or linked enterprises that do not qualify as SMEs, any compensation agreed shall not exceed the costs referred to in paragraph 2, point (a)."

**Article 11 — technical protection measures + remedies (D7):**
> 11(1): "A data holder may apply appropriate technical protection measures, including smart contracts and encryption, to prevent unauthorised access to data … and to ensure compliance with Articles 4, 5, 6, 8 and 9 … Such technical protection measures shall not discriminate between data recipients or hinder a user's right to obtain a copy of, retrieve, use or access data, to provide data to third parties pursuant to Article 5 … Users, third parties and data recipients shall not alter or remove such technical protection measures unless agreed by the data holder."
> 11(2): "In the circumstances referred to in paragraph 3, the third party or data recipient shall comply, without undue delay, with the requests of the data holder … (a) to erase the data …; (b) to end the production, offering or placing on the market … and destroy any infringing goods, where there is a serious risk … significant harm …; (c) to inform the user …; (d) to compensate the party suffering from the misuse or disclosure …".
> 11(3): "Paragraph 2 shall apply where a third party or a data recipient has: (a) … provided false information … deployed deceptive or coercive means or abused gaps …; (b) used the data … for unauthorised purposes, including the development of a competing connected product within the meaning of Article 6(2), point (e); (c) unlawfully disclosed data …; (d) not maintained the … measures agreed pursuant to Article 5(9); or (e) altered or removed technical protection measures … without the agreement of the data holder."
> 11(5): "Where the data recipient infringes Article 6(2), point (a) or (b), users shall have the same rights as data holders under paragraph 2 of this Article."

**Article 12(1) — Chapter III applicability gate (D9):**
> 12(1): "This Chapter shall apply where, in business-to-business relations, a data holder is obliged under Article 5 or under applicable Union law or national legislation adopted in accordance with Union law, to make data available to a data recipient."

## 27. Block 4 verification table (8 identities · EP-CLM-000072 … 000079)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / qualifier & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000072` | R-D2 | Art. 6(2)(a)–(h) | third-party prohibitions verbatim, all eight points (a)–(h) | Not broader — all eight limbs retained incl. profiling/GDPR-22 & gatekeeper cross-refs | **Q4 companion of C6** (`…069`). **Verified FIRST.** With C7 (`…070`, R3.3-C ✓) this **closes C6's Q4 carve-out set** | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000073` | R-D3 | Art. 8(1) | FRAND + transparent terms verbatim | Not broader — "Where … obliged … under Article 5 or … Union/national law" applicability condition retained | **N1** duty, gated by **D9** (Art 12(1), this block ✓) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000074` | R-D4 | Art. 8(3) | non-discrimination between comparable recipients + reasoned-request info verbatim | Not broader | **N1** duty, gated by **D9** (this block ✓) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000075` | R-D5a | Art. 9(1) | compensation "non-discriminatory and reasonable and may include a margin" verbatim | Not broader — "may include a margin" retained | **Q5 default**; carve-out D5b (this block ✓) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000076` | R-D5b | Art. 9(4) | SME/not-for-profit cost-cap verbatim (compensation ≤ Art 9(2)(a) costs), incl. no-disqualifying-partner condition | Not broader — full SME condition retained | **Q5 carve-out of D5a** (bound pair, both this block) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000077` | R-D7 | Art. 11(1)/(2)/(3)/(5) | technical protection measures + graduated remedies verbatim: (1) TPM may apply, must not hinder user Art 4/5 rights, no unilateral removal; (2) erase/end/inform/compensate; (3) trigger conditions; (5) user gets holder-rights on Art 6(2)(a)/(b) infringement | Not broader — the "shall not … hinder a user's right … to provide data to third parties pursuant to Article 5" bound retained | bounded by user Art 4/5 rights; references Art 5(9)/6(2) (this block/Block 3 ✓). Art 11(4) is a supporting locator (travels with parent) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000078` | R-D8 | Art. 8(4) | "shall not make data available to a data recipient, including on an exclusive basis, unless requested to do so by the user under Chapter II" verbatim | Not broader | **N2 gate** of the D-series → back to **C6** (user Ch II request, `…069` R3.3-C ✓) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000079` | R-D9 | Art. 12(1) | Chapter III applicability gate verbatim ("This Chapter shall apply where … a data holder is obliged under Article 5 or … Union/national law, to make data available …") | Not broader | **N1 scope predicate** for D3/D4/D5(a/b)/D7 (all this block ✓) | **VERIFIED_LITERAL** | 2026-08-31 |

## 28. Tally — R3.3-D (Block 4)

- **Reviewed:** 8 (`EP-CLM-000072` … `EP-CLM-000079`, rows D2/D3/D4/D5a/D5b/D7/D8/D9).
- **`VERIFIED_LITERAL`:** **8** — `last_verified_at = 2026-08-31` set on all eight.
- **`NEEDS_REWRITE`:** 0 · **`NEEDS_QUALIFIER`:** 0 · **`SOURCE_CONSTRAINED`:** 0 · **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the eight; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.
- **Running R3.3 total:** 34/34 `VERIFIED_LITERAL` across Blocks 1–4 (`EP-CLM-000046..000079`).

## 29. C6 / Q4 seam closure (the reason D2 was verified first)

**CLOSED.** C6 (`EP-CLM-000069`, Art. 5(1) user third-party-sharing right) carries **Q4 = C7 + D2**. C7 (`…070`, Art. 5(3) gatekeeper exclusion) was `VERIFIED` in R3.3-C; **D2 (`…072`, Art. 6(2) prohibitions) is now `VERIFIED` in this unit.** Both limbs of C6's Q4 carve-out are therefore verified — **C6's companion prohibition set is complete.** The R3.3-C forward-dependency flag is resolved: C6 may proceed to R3.4 with C7 **and** D2 present.

## 30. Corrigendum (EP-SRC-000007) effect on Block 4

**NONE.** The corrigendum touches **Article 48 only**. Block 4 covers **Arts. 6(2), 8, 9, 11, 12(1)**; none is touched. Block 4 rests on `EP-SRC-000006` unmodified.

## 31. Qualifier / edge check for Block 4 (N-edges now active)

- **N1** (Ch III duties gated by the Art 12(1) applicability predicate): **D9** (`…079`, Art 12(1)) verified this block; the gated duties **D3/D4/D5a/D5b/D7** all verified this block. Scope predicate present for each. **PASS.**
- **N2** (Art 8(4) gate → Chapter II request): **D8** (`…078`, Art 8(4)) verified this block; its target **C6** (user Ch II request, `…069`) verified in R3.3-C. Gate + target present. **PASS.**
- **Q4** (C6 ↔ C7 + D2): **COMPLETE** — both limbs verified (§29). **PASS.**
- **Q5** (D5a ↔ D5b, Art 9(1)/(4)): default + cost-cap carve-out, both this block. **PASS.**
- **Ch III anti-waiver (D10 / Art 12(2), `…080`):** **NOT in this unit** — begins R3.3-E (Block 5). Recorded so the Ch III duties render with their anti-waiver once D10 is verified.
- **N3–N7:** none attach to Block 4 rows (N3 companion H1a/G6 in Ch VI/VII; N4–N7 in Ch VIII–IX). **N/A this unit.**
- **External dependencies recorded (not minted):** DMA `32022R1925` (D2/Art 6(2)(d) gatekeeper); GDPR `32016R0679` (D2/Art 6(2)(b) profiling / Art 22); EDIB Art 42 (D5a lineage via Art 9(5), deferred/context) — pinned narrowly only if a rendering quotes them (R3.4+), per `R3_2_SOURCE_FIXATION.md` §3.

## 32. Guards honoured (R3.3-D)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. No claim verified outside Block 4 (D10/`…080` explicitly deferred). Blocks 1–3 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed.

## 33. Recommendation — R3.3-E

Proceed to **R3.3-E = Block 5** (*Unfair terms, Chapter IV*, `EP-CLM-000080` … `EP-CLM-000088`, rows **D10**, E1a–E6) on a fresh branch off `main` after this unit merges. **Begin at `EP-CLM-000080` (R-D10 = Art. 12(2) Chapter III anti-waiver)** — the deferred Ch III anti-waiver from this unit — so the Chapter III duties (D3/D4/D5/D7) gain their non-derogation boundary before Chapter IV. Then Ch IV: E1a (Art 13(1)) default unenforceability scoped by E3 (Art 13(6)), defined by the fairness tests E2a/E2b/E2c (Art 13(3)/(4)/(5)), carved by E1b (Art 13(2)) and E5 (Art 13(8)), severability E4 (Art 13(7)) — all under **Q6**.

---

# R3.3-E — Block 5 (Ch III anti-waiver close + Unfair terms · Chapter IV)

**Unit status:** **COMPLETE / PASS** — 9/9 `VERIFIED_LITERAL`. **Date:** 2026-08-31. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Blocks 1–4 untouched. **D10 verified FIRST** to close the Chapter III non-derogation boundary over the R3.3-D duties.

## 34. Scope of this unit — R3.3-E (Block 5 only)

Verifies **Block 5** by its **authoritative numeric range `EP-CLM-000080` … `EP-CLM-000088`** (nine identities). **First item = D10 (`EP-CLM-000080`, Art. 12(2))** — the Chapter III anti-waiver deferred from R3.3-D — then the Chapter IV unfair-terms claims. Rows in numeric order: **D10, E1a, E1b, E2a, E2b, E2c, E3, E4, E5**.

**Block-boundary seam recorded (continuation of the §17/§25 pattern):** numeric range `…080`–`…088` = rows **D10 + E1a–E5**. The draft-sequence label for Block 5 reads "E1a–E6", off on **both** ends: **D10** was pulled into this block (Ch III anti-waiver, per the R3.3-D §33 recommendation), and **E6 = R-E6 = Art. 13(9) Chapter IV anti-waiver = `EP-CLM-000089`** falls in Block 6's numeric range — **not** verified here; it begins R3.3-F. **E6 is E1a's Chapter IV non-derogation boundary** (Q15-analogue), so it is a forward dependency exactly as D10 was for Ch III (see E1a below).

## 35. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 12(2) — Chapter III anti-waiver (D10):**
> 12(2): "A contractual term in a data sharing agreement which, to the detriment of one party, or, where applicable, to the detriment of the user, excludes the application of this Chapter, derogates from it, or varies its effect, shall not be binding on that party."

**Article 13 — "Unfair contractual terms unilaterally imposed on another enterprise":**
> 13(1) [E1a]: "A contractual term concerning access to and the use of data or liability and remedies for the breach or the termination of data related obligations, which has been unilaterally imposed by an enterprise on another enterprise, shall not be binding on the latter enterprise if it is unfair."
> 13(2) [E1b]: "A contractual term which reflects mandatory provisions of Union law, or provisions of Union law which would apply if the contractual terms did not regulate the matter, shall not be considered to be unfair."
> 13(3) [E2a — general test]: "A contractual term is unfair if it is of such a nature that its use grossly deviates from good commercial practice in data access and use, contrary to good faith and fair dealing."
> 13(4) [E2b — always-unfair / black list]: "In particular, a contractual term shall be unfair for the purposes of paragraph 3, if its object or effect is to: (a) exclude or limit the liability of the party that unilaterally imposed the term for intentional acts or gross negligence; (b) exclude the remedies available to the party upon whom the term has been unilaterally imposed in the case of non-performance … or the liability … in the case of a breach …; (c) give the party that unilaterally imposed the term the exclusive right to determine whether the data supplied are in conformity with the contract or to interpret any contractual term."
> 13(5) [E2c — presumed-unfair / grey list + point-(g) proviso]: "A contractual term shall be presumed to be unfair for the purposes of paragraph 3 if its object or effect is to: (a) inappropriately limit remedies … or extend the liability …; (b) allow … access and use the data … in a manner that is significantly detrimental to the legitimate interests … in particular when such data contain commercially sensitive data or are protected by trade secrets or … intellectual property rights; (c) prevent … from using the data provided or generated …; (d) prevent … from terminating the agreement within a reasonable period; (e) prevent … from obtaining a copy of the data …; (f) enable … to terminate the contract at unreasonably short notice …; (g) enable … to substantially change the price … or any other substantive condition … where no valid reason and no right … to terminate … is specified …". Proviso: "Point (g) of the first subparagraph shall not affect terms by which the party that unilaterally imposed the term reserves the right to unilaterally change the terms of a contract of an indeterminate duration, provided that the contract specified a valid reason …, reasonable notice …, and that the other contracting party is free to terminate the contract at no cost …".
> 13(6) [E3 — 'unilaterally imposed' definition + burden of proof]: "A contractual term shall be considered to be unilaterally imposed within the meaning of this Article if it has been supplied by one contracting party and the other contracting party has not been able to influence its content despite an attempt to negotiate it. The contracting party that supplied the contractual term bears the burden of proving that that term has not been unilaterally imposed. The contracting party that supplied the contested contractual term may not argue that the term is an unfair contractual term."
> 13(7) [E4 — severability]: "Where the unfair contractual term is severable from the remaining terms of the contract, those remaining terms shall be binding."
> 13(8) [E5 — main-subject / price-adequacy exclusion]: "This Article does not apply to contractual terms defining the main subject matter of the contract or to the adequacy of the price, as against the data supplied in exchange."
> 13(9) [E6 — Chapter IV anti-waiver, `…089`, **NOT this unit**]: "The parties to a contract covered by paragraph 1 shall not exclude the application of this Article, derogate from it, or vary its effects." *(quoted for the forward-dependency record only)*

## 36. Block 5 verification table (9 identities · EP-CLM-000080 … 000088)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / qualifier & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000080` | R-D10 | Art. 12(2) | Chapter III anti-waiver verbatim ("excludes the application of this Chapter, derogates from it, or varies its effect, shall not be binding") | Not broader — scoped to a data-sharing-agreement term, "to the detriment of one party / the user" | **Q15-analogue**; **Verified FIRST.** Closes Ch III non-derogation over D3/D4/D5a/D5b/D7/D8/D9 (all R3.3-D ✓) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000081` | R-E1a | Art. 13(1) | unenforceability default verbatim, carrying **all four boundaries**: B2B ("by an enterprise on another enterprise"), data-access/use scope ("concerning access to and the use of data or liability and remedies …"), unilateral imposition ("unilaterally imposed"), unfairness ("if it is unfair") | **Not broader** — no bare "unfair terms are invalid"; all four boundaries retained | **Q6 DEFAULT**; scoped by E3 (13(6)), defined by E2a/E2b/E2c (13(3)/(4)/(5)), carved by E1b (13(2)) + E5 (13(8)), severability E4 (13(7)) — all this block ✓; **Ch IV anti-waiver E6 (13(9), `…089`) = forward dependency → R3.3-F ⚠** | **VERIFIED_LITERAL** *(E6/Ch IV anti-waiver forward-dependency flagged)* | 2026-08-31 |
| `EP-CLM-000082` | R-E1b | Art. 13(2) | mandatory-Union-law carve-out verbatim ("reflects mandatory provisions of Union law … shall not be considered to be unfair") | Not broader | **Q6 carve-out of E1a** (this block) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000083` | R-E2a | Art. 13(3) | **general unfairness test** verbatim ("grossly deviates from good commercial practice … contrary to good faith and fair dealing") | Not broader | **Q6 defines E1a** — the general standard | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000084` | R-E2b | Art. 13(4) | **always-unfair (black) list** verbatim, "shall be unfair", points (a)–(c) | Not broader — kept distinct from the grey list (E2c); "shall be" (not "presumed") | **Q6 defines E1a** — conclusive category | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000085` | R-E2c | Art. 13(5) | **presumed-unfair (grey) list** verbatim, "presumed to be unfair", points (a)–(g) **+ point-(g) proviso** subpara | Not broader — kept distinct from black list (E2b); "presumed"; proviso retained | **Q6 defines E1a** — rebuttable category | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000086` | R-E3 | Art. 13(6) | 'unilaterally imposed' definition + **burden of proof on supplier** + no-self-challenge verbatim | Not broader | **Q6 scopes E1a** (defines the trigger) | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000087` | R-E4 | Art. 13(7) | **severability** verbatim ("remaining terms shall be binding") | Not broader | **Q6 qualifies E1a** | **VERIFIED_LITERAL** | 2026-08-31 |
| `EP-CLM-000088` | R-E5 | Art. 13(8) | **main-subject-matter / price-adequacy exclusion** verbatim ("does not apply to contractual terms defining the main subject matter … or to the adequacy of the price, as against the data supplied in exchange") | Not broader | **Q6 scope limit on E1a** | **VERIFIED_LITERAL** | 2026-08-31 |

## 37. Tally — R3.3-E (Block 5)

- **Reviewed:** 9 (`EP-CLM-000080` … `EP-CLM-000088`, rows D10/E1a/E1b/E2a/E2b/E2c/E3/E4/E5).
- **`VERIFIED_LITERAL`:** **9** — `last_verified_at = 2026-08-31` set on all nine.
- **`NEEDS_REWRITE`:** 0 · **`NEEDS_QUALIFIER`:** 0 · **`SOURCE_CONSTRAINED`:** 0 · **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the nine; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.
- **Running R3.3 total:** 43/43 `VERIFIED_LITERAL` across Blocks 1–5 (`EP-CLM-000046..000088`).

## 38. Chapter III anti-waiver closure (the reason D10 was verified first)

**CLOSED.** D10 (`EP-CLM-000080`, Art. 12(2)) is now `VERIFIED`. The Chapter III availability duties verified in R3.3-D — **D3, D4, D5a, D5b, D7, D8, D9** — now carry their **non-derogation boundary**: a data-sharing-agreement term that excludes/derogates/varies Chapter III is not binding. The R3.3-D deferral is resolved; Chapter III duties may proceed to R3.4 with their anti-waiver present.

## 39. Corrigendum (EP-SRC-000007) effect on Block 5

**NONE.** The corrigendum touches **Article 48 only**. Block 5 covers **Arts. 12(2), 13(1)–(8)**; none is touched. Block 5 rests on `EP-SRC-000006` unmodified.

## 40. Qualifier / edge check for Block 5 (Q6 the key check)

- **Q6** (E1a default ↔ its scope/definition/carve-outs): E1a (Art 13(1)) rendered with **E3** (13(6) unilateral-imposition definition + burden ✓), **E2a/E2b/E2c** (13(3)/(4)/(5) general/black/grey tests ✓, three-way distinction preserved), **E1b** (13(2) mandatory-law carve-out ✓), **E5** (13(8) main-subject/price exclusion ✓), **E4** (13(7) severability ✓) — all this block. **The only outstanding limb is the Chapter IV anti-waiver E6 (13(9), `…089`), deferred to R3.3-F** — E1a must render with E6 present. **PASS-with-flag.**
- **Ch III anti-waiver (D10 / Art 12(2)):** verified this block; closes the R3.3-D boundary (§38). **PASS.**
- **Q15 analogues:** B7 (Ch II, Block 2 ✓), D10 (Ch III, this block ✓), E6 (Ch IV, `…089`, R3.3-F). Ch II & Ch III closed; Ch IV pending E6.
- **N1–N7:** none attach to Block 5 rows (D10 is a Ch III anti-waiver, not an N-edge; the E-series is Ch IV). **N/A this unit.**
- **No unfair-terms default rendered bare:** E1a carries B2B + data-access/use + unilateral-imposition + unfairness boundaries and its Q6 carve-out set (E1b/E2*/E3/E4/E5 in-block; E6 flagged forward). **No broad "unfair terms are invalid" wording verified.**

## 41. Guards honoured (R3.3-E)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. No claim verified outside Block 5 (E6/`…089` explicitly deferred). Blocks 1–4 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed.

## 42. Recommendation — R3.3-F

Proceed to **R3.3-F = Block 6** (*B2G exceptional need, Chapter V*, `EP-CLM-000089` … `EP-CLM-000099`, rows **E6**, F1–F6) on a fresh branch off `main` after this unit merges. **Begin at `EP-CLM-000089` (R-E6 = Art. 13(9) Chapter IV anti-waiver)** — the deferred Ch IV non-derogation boundary from this unit — so E1a (and the Chapter IV unfair-terms regime) gains its anti-waiver before Chapter V. Then Ch V under **Q7** (F1 B2G availability default ↔ F2a/F2b/F2c exceptional-need routes + micro/small carve-out) and **Q8** (F4a/F4b compensation split): verify the B2G duty with its exceptional-need routes, PSB limits (F5a/F5b), and criminal/customs/tax carve-out (F6) present.

---

# R3.3-F — Block 6 (Ch IV anti-waiver close + B2G exceptional need · Chapter V)

**Unit status:** **COMPLETE / PASS** — 11/11 `VERIFIED_LITERAL`. **Date:** 2026-09-02. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Blocks 1–5 untouched. **E6 verified FIRST** to close the Chapter IV non-derogation boundary over the R3.3-E unfair-terms regime.

## 43. Scope of this unit — R3.3-F (Block 6 only)

Verifies **Block 6** by its **authoritative numeric range `EP-CLM-000089` … `EP-CLM-000099`** (eleven identities). **First item = E6 (`EP-CLM-000089`, Art. 13(9))** — the Chapter IV anti-waiver deferred from R3.3-E — then the Chapter V B2G exceptional-need claims. Rows in numeric order: **E6, F1, F2a, F2b, F2c, F3a, F3b, F4a, F4b, F5a, F5b**.

**Block-boundary seam recorded (continuation of the §17/§25/§34 pattern):** numeric range `…089`–`…099` = rows **E6 + F1–F5b**. The draft-sequence label for Block 6 reads "F1–F6", off on **both** ends: **E6** was pulled into this block (Ch IV anti-waiver, per the R3.3-E §42 recommendation), and **F6 = R-F6 = Art. 16 (relationship + criminal/customs/tax carve-out) = `EP-CLM-000100`** falls in Block 7's numeric range — **not** verified here; it begins R3.3-G. **F6 is F1's Chapter V scope-limit (Q7 carve-out limb)**, so it is a forward dependency exactly as E6 was for Ch IV and D10 was for Ch III (see F1 below).

## 44. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 13(9) — Chapter IV anti-waiver (E6):**
> 13(9) [E6]: "The parties to a contract covered by paragraph 1 shall not exclude the application of this Article, derogate from it, or vary its effects."

**CHAPTER V heading:** "MAKING DATA AVAILABLE TO PUBLIC SECTOR BODIES, THE COMMISSION, THE EUROPEAN CENTRAL BANK AND UNION BODIES ON THE BASIS OF AN EXCEPTIONAL NEED".

**Article 14 — Obligation to make data available on the basis of an exceptional need (F1):**
> 14 [F1]: "Where a public sector body, the Commission, the European Central Bank or a Union body demonstrates an exceptional need, as set out in Article 15, to use certain data, including the relevant metadata necessary to interpret and use those data, to carry out its statutory duties in the public interest, data holders that are legal persons, other than public sectors bodies, which hold those data shall make them available upon a duly reasoned request." *(quoted verbatim, incl. the OJ text's "public sectors bodies")*

**Article 15 — Exceptional need to use data (F2a/F2b/F2c):**
> 15(1) chapeau: "An exceptional need to use certain data within the meaning of this Chapter shall be limited in time and scope and shall be considered to exist only in any of the following circumstances:"
> 15(1)(a) [F2a — public-emergency route]: "where the data requested is necessary to respond to a public emergency and the public sector body, the Commission, the European Central Bank or the Union body is unable to obtain such data by alternative means in a timely and effective manner under equivalent conditions;"
> 15(1)(b) [F2b — non-emergency route, **non-personal only**]: "in circumstances not covered by point (a) and only insofar as non-personal data is concerned, where: (i) a public sector body … is acting on the basis of Union or national law and has identified specific data, the lack of which prevents it from fulfilling a specific task carried out in the public interest, that has been explicitly provided for by law, such as the production of official statistics or the mitigation of or recovery from a public emergency; and (ii) the public sector body … has exhausted all other means at its disposal to obtain such data, including purchase of non-personal data on the market by offering market rates, or by relying on existing obligations to make data available or the adoption of new legislative measures which could guarantee the timely availability of the data."
> 15(2) [F2c — micro/small carve-out, 15(1)(b) only]: "Paragraph 1, point (b), shall not apply to microenterprises and small enterprises."
> 15(3) [supporting, travels with F2b/F2c]: "The obligation to demonstrate that the public sector body was unable to obtain non-personal data by purchasing them on the market shall not apply where the specific task carried out in the public interest is the production of official statistics and where the purchase of such data is not allowed by national law."

**Article 17 — Requests for data to be made available (F3a):**
> 17(1) [F3a]: "When requesting data pursuant to Article 14, a public sector body … shall: (a) specify the data required …; (b) demonstrate that the conditions necessary for the existence of an exceptional need as referred to in Article 15 … are met; (c) explain the purpose of the request, the intended use of the data requested …; (d) specify, if possible, when the data are expected to be erased …; (e) justify the choice of data holder to which the request is addressed; (f) specify any other public sector bodies … and the third parties with which the data requested is expected to be shared with; (g) where personal data are requested, specify any technical and organisational measures necessary and proportionate …; (h) state the legal provision allocating … the specific task carried out in the public interest …; (i) specify the deadline by which the data are to be made available and the deadline referred to in Article 18(2) …; (j) make its best efforts to avoid compliance with the data request resulting in the data holders' liability …"
> 17(2): "A request … shall: (a) be made in writing and expressed in clear, concise and plain language …; (b) be specific regarding the type of data requested …; (c) be proportionate to the exceptional need and duly justified …; (d) respect the legitimate aims of the data holder, committing to ensuring the protection of trade secrets in accordance with Article 19(3) …; (e) concern non-personal data, and only if this is demonstrated to be insufficient … request personal data in pseudonymised form …" [routing/notification points (f)–(i)].
> 17(3): "A public sector body … shall not make data obtained pursuant to this Chapter available for reuse …" · 17(4) [exchange with another public body / delegation to a third party, with the Art. 19 safeguards extended to that third party] · 17(5) [complaint] · 17(6): "The Commission shall develop a model template for requests pursuant to this Article."

**Article 18 — Compliance with requests for data (F3b):**
> 18(1) [F3b]: "A data holder receiving a request to make data available under this Chapter shall make the data available … without undue delay, taking into account necessary technical, organisational and legal measures."
> 18(2): "… a data holder may decline or seek the modification of a request … without undue delay and, in any event, no later than **five working days** after the receipt of a request for the data necessary to respond to a public emergency and without undue delay and, in any event, no later than **30 working days** after the receipt of such a request in other cases of an exceptional need, on any of the following grounds: (a) the data holder does not have control over the data requested; (b) a similar request for the same purpose has been previously submitted …; (c) the request does not meet the conditions laid down in Article 17(1) and (2)."
> 18(3) [prior-requester identity] · 18(4): "Where the data requested includes personal data, the data holder shall properly anonymise the data, unless … requires the disclosure of personal data. In such cases, the data holder shall pseudonymise the data." · 18(5) [challenge referred to the competent authority under Art. 37].

**Article 19 — Obligations of public sector bodies … (F5a):**
> 19(1) [F5a]: "A public sector body … receiving data pursuant to a request made under Article 14 shall: (a) not use the data in a manner incompatible with the purpose for which they were requested; (b) have implemented technical and organisational measures that preserve the confidentiality and integrity of the requested data …; (c) erase the data as soon as they are no longer necessary for the stated purpose and inform the data holder and individuals or organisations that received the data pursuant to Article 21(1) … unless archiving of the data is required …"
> 19(2): "… shall not: (a) use the data or insights … to develop or enhance a connected product or related service that competes with the connected product or related service of the data holder; (b) share the data with another third party for any of the purposes referred to in point (a)."
> 19(3): "Disclosure of trade secrets … shall be required only to the extent that it is strictly necessary to achieve the purpose of a request under Article 15. …"
> 19(4): "A public sector body … shall be responsible for the security of the data it receives."

**Article 20 — Compensation in cases of an exceptional need (F4a/F4b):**
> 20(1) [F4a — emergency free, non micro/small]: "Data holders other than microenterprises and small enterprises shall make available data necessary to respond to a public emergency pursuant to Article 15(1), point (a), free of charge. …"
> 20(2) [F4b — fair compensation, 15(1)(b) route]: "The data holder shall be entitled to fair compensation for making data available in compliance with a request made pursuant to Article 15(1), point (b). Such compensation shall cover the technical and organisational costs incurred to comply with the request including, where applicable, the costs of anonymisation, pseudonymisation, aggregation and of technical adaptation, and a reasonable margin. …"
> 20(3) [F4b — micro/small entitlement]: "Paragraph 2 shall also apply where a microenterprise and small enterprise claims compensation for making data available." *(20(4) official-statistics no-compensation proviso + 20(5) complaint travel with F4b as supporting detail.)*

**Article 21 — Sharing of data obtained in the context of an exceptional need with research organisations or statistical bodies (F5b):**
> 21(1) [F5b]: "A public sector body … shall be entitled to share data received under this Chapter: (a) with individuals or organisations in view of carrying out scientific research or analytics compatible with the purpose for which the data was requested; or (b) with national statistical institutes and Eurostat for the production of official statistics."
> 21(2): "Individuals or organisations receiving the data … shall act on a not-for-profit basis or in the context of a public-interest mission recognised in Union or national law. They shall not include organisations upon which commercial undertakings have a significant influence which is likely to result in preferential access to the results of the research."
> 21(3): "… shall comply with the same obligations that are applicable to the public sector bodies … pursuant to Article 17(3) and Article 19." · 21(4): "Notwithstanding Article 19(1), point (c), individuals or organisations … may keep the data received … for up to **six months** following erasure …" · 21(5) [notification to data holder + complaint].

**Article 16 — Relationship with other obligations … (F6, `…100`, **NOT this unit**):**
> 16(1) [F6]: "This Chapter shall not affect the obligations laid down in Union or national law for the purposes of reporting, complying with requests for access to information or demonstrating or verifying compliance with legal obligations."
> 16(2) [F6]: "This Chapter shall not apply to public sector bodies … carrying out activities for the prevention, investigation, detection or prosecution of criminal or administrative offences or the execution of criminal penalties, or to customs or taxation administration. …" *(quoted for the forward-dependency record only)*

## 45. Block 6 verification table (11 identities · EP-CLM-000089 … 000099)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / qualifier & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000089` | R-E6 | Art. 13(9) | Chapter IV anti-waiver verbatim ("shall not exclude the application of this Article, derogate from it, or vary its effects") | Not broader — scoped to "parties to a contract covered by paragraph 1" (the 13(1) unilateral-imposition regime) | **Q15-analogue**; **Verified FIRST.** Closes Ch IV non-derogation over E1a + E1b/E2a/E2b/E2c/E3/E4/E5 (all R3.3-E ✓); completes the Q15 anti-waiver triad (Ch II B7 ✓ / Ch III D10 ✓ / Ch IV E6) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000090` | R-F1 | Art. 14 | B2G availability duty verbatim, carrying **all four boundaries**: requester set (PSB/Commission/ECB/Union body), **demonstrated exceptional need "as set out in Article 15"**, statutory-duty-in-the-public-interest purpose, duty-holder limit ("legal persons, other than public sectors bodies"), "duly reasoned request" | **Not broader** — no bare "data holders must give data to the state"; the Art. 15 exceptional-need gate and the legal-person/non-PSB limiter are retained | **Q7 DEFAULT**; routed by F2a/F2b (15(1)(a)/(b)), micro/small-carved by F2c (15(2)), procedure F3a/F3b (17/18), compensation split F4a/F4b (20) under **Q8**, PSB limits F5a/F5b (19/21) — all this block ✓; **Ch V scope-limit / criminal-customs-tax carve-out F6 (Art 16, `…100`) = forward dependency → R3.3-G ⚠** | **VERIFIED_LITERAL** *(F6/Art 16 forward-dependency flagged)* | 2026-09-02 |
| `EP-CLM-000091` | R-F2a | Art. 15(1)(a) | **public-emergency route** verbatim ("necessary to respond to a public emergency … unable to obtain such data by alternative means in a timely and effective manner under equivalent conditions") | Not broader — kept distinct from the 15(1)(b) route; carries the "limited in time and scope" chapeau | **Q7 qualifies F1** — emergency route (personal data reachable, per 17(2)(e)) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000092` | R-F2b | Art. 15(1)(b) | **non-emergency route** verbatim, "**only insofar as non-personal data is concerned**", two-limb test (i) specific-task-provided-by-law + (ii) exhausted-all-other-means incl. market purchase | Not broader — non-personal-only limiter and both cumulative limbs retained; kept distinct from 15(1)(a) | **Q7 qualifies F1** — non-emergency route | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000093` | R-F2c | Art. 15(2) | **micro/small carve-out** verbatim ("Paragraph 1, point (b), shall not apply to microenterprises and small enterprises") | Not broader — carve-out is **route-specific to 15(1)(b) only**; does not touch the 15(1)(a) emergency route | **Q7 qualifies F1 route-specifically**; 15(3) official-statistics proviso travels with it | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000094` | R-F3a | Art. 17(1)/(2)/(3)-(6) | **B2G request requirements** verbatim: content list 17(1)(a)-(j), form list 17(2)(a)-(i), no-reuse 17(3), exchange/delegation-with-Art-19-safeguards 17(4), complaint 17(5), model template 17(6) | Not broader — a request is bounded by the (a)-(j)/(a)-(i) requirements; no free-form state demand | **Procedure on F1** (defines a valid request) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000095` | R-F3b | Art. 18(1)-(5) | **data-holder compliance** verbatim: make available without undue delay 18(1); **decline/modify no later than 5 wd (public emergency) / 30 wd (other exceptional need)** on grounds (a)-(c) 18(2); prior-requester identity 18(3); anonymise-else-pseudonymise 18(4); challenge referral 18(5) | Not broader — the two numeric deadlines (5 wd / 30 wd) and the closed ground-set (a)-(c) retained; personal-data anonymisation default kept | **Procedure on F1** (defines compliance + refusal) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000096` | R-F4a | Art. 20(1) | **emergency data free** verbatim ("Data holders other than microenterprises and small enterprises shall make available data necessary to respond to a public emergency pursuant to Article 15(1), point (a), free of charge") | Not broader — free-of-charge is scoped to the **15(1)(a) emergency route** and excludes micro/small holders | **Q8 qualifies F1** — no-compensation limb (emergency) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000097` | R-F4b | Art. 20(2)/(3) | **fair compensation** verbatim ("entitled to fair compensation … pursuant to Article 15(1), point (b) … technical and organisational costs … and a reasonable margin"); **micro/small entitlement** 20(3) ("Paragraph 2 shall also apply where a microenterprise and small enterprise claims compensation") | Not broader — compensation is scoped to the **15(1)(b) route**; kept distinct from the 15(1)(a) free-of-charge rule; 20(4) statistics no-comp proviso retained | **Q8 qualifies F1** — compensation limb (non-emergency) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000098` | R-F5a | Art. 19(1)-(4) | **PSB use/erasure/trade-secret** verbatim: purpose-compatible use + confidentiality measures + erase-when-done 19(1)(a)-(c); no competing product / no onward share 19(2); trade-secret strict-necessity disclosure 19(3); security responsibility 19(4) | Not broader — the received data is bounded by the purpose, the erasure duty, and the anti-competitive-use ban | **Bounds B2G** (limit on the requesting PSB) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000099` | R-F5b | Art. 21(1)-(5) | **bounded onward-sharing to research/statistics** verbatim: entitled to share with (a) scientific research/analytics + (b) national statistical institutes/Eurostat 21(1); not-for-profit / no significant commercial influence 21(2); same Art 17(3)/19 obligations 21(3); **six-month** retention 21(4); data-holder notification + complaint 21(5) | Not broader — onward sharing is confined to the two named recipient classes under the not-for-profit + purpose-compatibility limits | **Bounds B2G** (confines onward re-use) | **VERIFIED_LITERAL** | 2026-09-02 |

## 46. Tally — R3.3-F (Block 6)

- **Reviewed:** 11 (`EP-CLM-000089` … `EP-CLM-000099`, rows E6/F1/F2a/F2b/F2c/F3a/F3b/F4a/F4b/F5a/F5b).
- **`VERIFIED_LITERAL`:** **11** — `last_verified_at = 2026-09-02` set on all eleven.
- **`NEEDS_REWRITE`:** 0 · **`NEEDS_QUALIFIER`:** 0 · **`SOURCE_CONSTRAINED`:** 0 · **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the eleven; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.
- **Running R3.3 total:** 54/54 `VERIFIED_LITERAL` across Blocks 1–6 (`EP-CLM-000046..000099`).

## 47. Chapter IV anti-waiver closure (the reason E6 was verified first) — and Q15 triad completion

**CLOSED.** E6 (`EP-CLM-000089`, Art. 13(9)) is now `VERIFIED`. The Chapter IV unfair-terms regime verified in R3.3-E — **E1a, E1b, E2a, E2b, E2c, E3, E4, E5** — now carries its **non-derogation boundary**: parties to a contract covered by Art. 13(1) may not exclude/derogate/vary Article 13. The R3.3-E forward dependency flagged on E1a is resolved; the Chapter IV regime may proceed to R3.4 with its anti-waiver present.

**Q15 anti-waiver triad now COMPLETE:** the three chapter-scoped non-derogation analogues are all verified — **Ch II = B7 (Art. 7(2), R3.3-B ✓)**, **Ch III = D10 (Art. 12(2), R3.3-E ✓)**, **Ch IV = E6 (Art. 13(9), this unit ✓)**. No further Q15 analogue is outstanding (Chapter V carries no user-right anti-waiver of this form; its guardrails are the PSB obligations F5a/F5b and the Art. 16 scope-limit F6).

## 48. Corrigendum (EP-SRC-000007) effect on Block 6

**NONE.** The corrigendum touches **Article 48 only**. Block 6 covers **Arts. 13(9), 14, 15, 17, 18, 19, 20, 21**; none is touched. Block 6 rests on `EP-SRC-000006` unmodified.

## 49. Qualifier / edge check for Block 6 (Q7 + Q8 the key checks)

- **Q7** (F1 B2G availability default ↔ its routes / carve-outs / scope-limit): F1 (Art 14) rendered with **F2a/F2b** (15(1)(a)/(b) emergency vs non-emergency-non-personal routes ✓, kept distinct), **F2c** (15(2) micro/small carve-out, route-specific to 15(1)(b) ✓), the request/compliance procedure **F3a/F3b** (Arts 17/18 ✓) and PSB limits **F5a/F5b** (Arts 19/21 ✓) — all this block. **The only outstanding limb is the Chapter V scope-limit / criminal-customs-tax carve-out F6 (Art 16, `…100`), deferred to R3.3-G** — F1 must render with F6 present. **PASS-with-flag.**
- **Q8** (F1 ↔ compensation split): F4a (20(1) emergency free, non micro/small) vs F4b (20(2)/(3) fair compensation incl. micro/small entitlement) — both this block, kept route-distinct (15(1)(a) free vs 15(1)(b) compensated). **PASS.**
- **Ch IV anti-waiver (E6 / Art 13(9)):** verified this block; closes the R3.3-E boundary and completes the Q15 triad (§47). **PASS.**
- **Q15 analogues:** B7 (Ch II, Block 2 ✓), D10 (Ch III, Block 5 ✓), E6 (Ch IV, this block ✓). **All three CLOSED.**
- **N1–N7:** none attach to Block 6 rows (E6 is a Ch IV anti-waiver; the F-series is the Ch V B2G regime, self-contained — F5a/F5b bound it internally). **N/A this unit.**
- **No B2G duty rendered bare:** F1 carries the requester-set + Art. 15 exceptional-need gate + legal-person/non-PSB limiter + duly-reasoned-request boundaries and its Q7/Q8 route/carve-out/compensation set (F2a/F2b/F2c/F3a/F3b/F4a/F4b/F5a/F5b in-block; F6 flagged forward). **No broad "the state can demand data" wording verified.**

## 50. Guards honoured (R3.3-F)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. No claim verified outside Block 6 (F6/`…100` explicitly deferred). Blocks 1–5 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed.

## 51. Recommendation — R3.3-G

Proceed to **R3.3-G = Block 7** (*Switching between data processing services, Chapter VI*, `EP-CLM-000100` … `EP-CLM-000113`, rows **F6**, G1–G8/G9) on a fresh branch off `main` after this unit merges. **Begin at `EP-CLM-000100` (R-F6 = Art. 16 relationship + criminal/customs/tax carve-out)** — the deferred Chapter V scope-limit from this unit — so F1 (and the whole Chapter V B2G regime) gains its Art. 16 carve-out before Chapter VI, exactly as this unit opened with E6 and R3.3-E opened with D10. Then Ch VI under **Q9** (G4a/G4b switching-charge phase-out) and **Q10** (G5a/G5b/G5c functional-equivalence / open-interface / standards limits) with the **G8** bespoke/non-production exemption: verify the switching-obstacle-removal duty (G1) with its numeric contract terms (G2b: notice ≤2m, transition 30d, retrieval ≥30d), the Art. 24 scope-limiter (G9), and the charge and service-tier carve-outs present.

---

# R3.3-G — Block 7 (Ch V scope-limit close + Switching between data processing services · Chapter VI)

**Unit status:** **COMPLETE / PASS** — 14/14 `VERIFIED_LITERAL`. **Date:** 2026-09-02. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Blocks 1–6 untouched. **F6 verified FIRST** to close the Chapter V scope-limit / criminal-customs-tax carve-out over the R3.3-F B2G regime — resolving the F1 → F6 forward dependency before any Chapter VI switching claim.

## 52. Scope of this unit — R3.3-G (Block 7 only)

Verifies **Block 7** by its **authoritative numeric range `EP-CLM-000100` … `EP-CLM-000113`** (fourteen identities). **First item = F6 (`EP-CLM-000100`, Art. 16)** — the Chapter V scope-limit deferred from R3.3-F — then the Chapter VI switching claims. Rows in numeric order: **F6, G1, G9, G2a, G2b, G2c, G3, G7, G6, G4a, G4b, G5a, G5b, G5c**.

**Block-boundary seam recorded (continuation of the §17/§25/§34/§43 pattern) — numeric range is authoritative:** numeric range `…100`–`…113` = rows **F6 + G1/G9/G2a/G2b/G2c/G3/G7/G6/G4a/G4b/G5a/G5b/G5c**. The draft-sequence label for Block 7 reads "G1–G8", off on **both** ends: **F6** was pulled into this block (Ch V scope-limit, per the R3.3-F §51 recommendation), and **G8 = R-G8 = Art. 31 (bespoke / non-production exemptions) = `EP-CLM-000114`** falls in Block 8's numeric range — **not** verified here; it begins R3.3-H. **G8 (Art. 31) carries two distinct exemption layers that must be kept apart:** (i) **Art. 31(1)** — the *limited bespoke / custom-built* exemption, which disapplies **only Art. 23(d), Art. 29, and Art. 30(1) and (3)** (i.e. the Q9 charge duties G4a/G4b and the Q10 IaaS/standards limbs G5a/G5c, plus G1's functional-equivalence limb 23(d)); and (ii) **Art. 31(2)** — the broader *whole-of-Chapter-VI scope exemption*, under which the obligations of the **entire Chapter VI** do not apply to qualifying **non-production testing/evaluation** services provided for a limited period. **Art. 31(3)** carries the pre-contract information duty as to which Chapter VI obligations do not apply. So G8 is **not merely a Q9/Q10 carve-out**: it is a Q9/Q10 carve-out *through 31(1)* **and** a Chapter-VI-wide scope exemption *through 31(2)*. It is a forward dependency exactly as F6 was for Ch V, E6 for Ch IV, and D10 for Ch III (see G1/G4a/G5a below). **Per instruction, the numeric range governs; no `EP-CLM` is renumbered to absorb the label mismatch — the mismatch is recorded here.** (Note: `EP-CLM-000102` carries the draft label "G9" (Art. 24 scope-limiter) sitting between G1 and G2a in numeric order — an intra-series ordering artefact, not a seam; it is verified here in numeric position.)

## 53. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 16 — Relationship with other obligations … (F6, Ch V scope-limit):**
> 16(1) [F6]: "This Chapter shall not affect the obligations laid down in Union or national law for the purposes of reporting, complying with requests for access to information or demonstrating or verifying compliance with legal obligations."
> 16(2) [F6]: "This Chapter shall not apply to public sector bodies, the Commission, the European Central Bank or Union bodies carrying out activities for the prevention, investigation, detection or prosecution of criminal or administrative offences or the execution of criminal penalties, or to customs or taxation administration. This Chapter does not affect applicable Union and national law on the prevention, investigation, detection or prosecution of criminal or administrative offences or the execution of criminal or administrative penalties, or for customs or taxation administration."

**CHAPTER VI heading:** "SWITCHING BETWEEN DATA PROCESSING SERVICES".

**Article 23 — Removing obstacles to effective switching (G1):**
> 23 [G1]: "Providers of data processing services shall take the measures provided for in Articles 25, 26, 27, 29 and 30 to enable customers to switch to a data processing service, covering the same service type, which is provided by a different provider … or to on-premises ICT infrastructure, or, where relevant, to use several providers … at the same time. In particular, providers … shall not impose and shall remove pre-commercial, commercial, technical, contractual and organisational obstacles, which inhibit customers from: (a) terminating … the contract …; (b) concluding new contracts with a different provider … covering the same service type; (c) porting the customer's exportable data and digital assets …; (d) in accordance with Article 24, achieving functional equivalence …; (e) unbundling, where technically feasible, data processing services referred to in Article 30(1) …"

**Article 24 — Scope of the technical obligations (G9):**
> 24 [G9]: "The responsibilities of providers of data processing services laid down in Articles 23, 25, 29, 30 and 34 shall apply only to the services, contracts or commercial practices provided by the source provider of data processing services."

**Article 25 — Contractual terms concerning switching (G2a/G2b/G2c):**
> 25(1) [G2a]: "The rights of the customer and the obligations of the provider … in relation to switching … shall be clearly set out in a written contract. The provider … shall make that contract available to the customer prior to signing the contract in a way that allows the customer to store and reproduce the contract."
> 25(2) [G2b]: "Without prejudice to Directive (EU) 2019/770, the contract … shall include at least the following: (a) clauses allowing the customer … to switch … or to port all exportable data and digital assets to an on-premises ICT infrastructure, without undue delay and in any event not after the mandatory maximum transitional period of **30 calendar days** …; … (d) a maximum notice period for initiation of the switching process, which shall **not exceed two months**; (e) an exhaustive specification of all categories of data and digital assets that can be ported …; (f) an exhaustive specification of categories of data specific to the internal functioning … to be exempted … where a risk of breach of trade secrets … exists, provided that such exemptions do not impede or delay the switching process …; (g) a minimum period for data retrieval of **at least 30 calendar days** …; (h) a clause guaranteeing full erasure … after the expiry of the retrieval period …; (i) switching charges, that may be imposed … in accordance with Article 29."
> 25(3) [G2c]: "The contract … shall include clauses providing that the customer may notify … its decision to perform one or more of the following actions …: (a) switch to a different provider …; (b) switch to an on-premises ICT infrastructure; (c) erase its exportable data and digital assets."
> 25(4) [G2c]: "Where the mandatory maximum transitional period … is technically unfeasible, the provider … shall notify the customer within **14 working days** … and shall duly justify the technical unfeasibility and indicate an alternative transitional period, which shall **not exceed seven months** …"
> 25(5) [G2c]: "… the contract … shall include clauses providing the customer with the right to extend the transitional period once for a period that the customer considers more appropriate for its own purposes."

**Article 26 — Information obligation (G3):**
> 26 [G3]: "The provider … shall provide the customer with: (a) information on available procedures for switching and porting …, including … methods and formats as well as restrictions and technical limitations …; (b) a reference to an up-to-date online register hosted by the provider …, with details of all the data structures and data formats as well as the relevant standards and open interoperability specifications, in which the exportable data referred to in Article 25(2), point (e), are available."

**Article 27 — Obligation of good faith (G7):**
> 27 [G7]: "All parties involved, including destination providers of data processing services, shall cooperate in good faith to make the switching process effective, enable the timely transfer of data and maintain the continuity of the data processing service."

**Article 28 — Contractual transparency on international access and transfer (G6):**
> 28(1) [G6]: "Providers … shall make the following information available on their websites, and keep that information up to date: (a) the jurisdiction to which the ICT infrastructure deployed for data processing of their individual services is subject; (b) a general description of the technical, organisational and contractual measures adopted … to prevent international governmental access to or transfer of non-personal data held in the Union where such access or transfer would create a conflict with Union law or the national law of the relevant Member State."
> 28(2) [G6]: "The websites referred to in paragraph 1 shall be listed in contracts for all data processing services offered …"

**Article 29 — Gradual withdrawal of switching charges (G4a/G4b):**
> 29(1) [G4a]: "From **12 January 2027**, providers of data processing services shall not impose any switching charges on the customer for the switching process."
> 29(2) [G4b]: "From 11 January 2024 to 12 January 2027, providers … may impose reduced switching charges on the customer for the switching process."
> 29(3) [G4b]: "The reduced switching charges referred to in paragraph 2 shall not exceed the costs incurred by the provider … that are directly linked to the switching process concerned."

**Article 30 — Technical aspects of switching (G5a/G5b/G5c):**
> 30(1) [G5a]: "Providers of data processing services that concern scalable and elastic computing resources limited to infrastructural elements such as servers, networks and the virtual resources … but that do not provide access to the operating services, software and applications … shall, in accordance with Article 27, take all reasonable measures in their power to facilitate that the customer, after switching to a service covering the same service type, achieves functional equivalence …"
> 30(2) [G5b]: "Providers … other than those referred to in paragraph 1, shall make open interfaces available to an equal extent to all their customers and the concerned destination providers … free of charge to facilitate the switching process. …"
> 30(3) [G5c]: "… providers … shall ensure compatibility with common specifications based on open interoperability specifications or harmonised standards for interoperability **at least 12 months** after the references … were published in the central Union standards repository …"
> 30(5) [G5c]: "… where common specifications or … harmonised standards … have not been published …, the provider … shall, at the request of the customer, export all exportable data in a structured, commonly used and machine-readable format."
> 30(6) [G5c]: "Providers … shall not be required to develop new technologies or services, or disclose or transfer digital assets that are protected by intellectual property rights or that constitute a trade secret … or compromise the customer's or provider's security and integrity of service."

**Article 31 — Specific regime for certain data processing services (G8, `…114`, **NOT this unit**):**
> 31(1) [G8]: "The obligations laid down in Article 23, point (d), Article 29 and Article 30(1) and (3) shall not apply to data processing services of which the majority of main features has been custom-built to accommodate the specific needs of an individual customer or where all components have been developed for the purposes of an individual customer, and where those data processing services are not offered at broad commercial scale …"
> 31(2) [G8]: "The obligations laid down in this Chapter shall not apply to data processing services provided as a non-production version for testing and evaluation purposes and for a limited period of time." *(31(3) pre-contract information duty. Quoted for the forward-dependency record only.)*

## 54. Block 7 verification table (14 identities · EP-CLM-000100 … 000113)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / qualifier & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000100` | R-F6 | Art. 16(1)/(2) | Ch V relationship + carve-out verbatim: 16(1) reporting/access/compliance obligations unaffected; 16(2) **criminal / administrative-offence / penalties** carve-out **and** **customs / taxation administration** carve-out (both the "shall not apply" and the "does not affect applicable law" limbs) | Not broader — carve-out is confined to the named enforcement/customs/tax activities; the B2G duty otherwise stands | **Q7 scope-limit on F1**; **Verified FIRST.** Closes the R3.3-F F1 → F6 forward dependency (§56) over F1 + F2a/F2b/F2c/F3a/F3b/F4a/F4b/F5a/F5b (all R3.3-F ✓) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000101` | R-G1 | Art. 23(a)-(e) | switching-obstacle-removal duty verbatim: measures per Arts 25/26/27/29/30; "shall not impose and shall remove pre-commercial, commercial, technical, contractual and organisational obstacles" inhibiting (a) termination, (b) new contract same service type, (c) porting exportable data/digital assets, (d) functional equivalence (per Art 24), (e) unbundling (per Art 30(1)) | **Not broader** — bounded to "same service type" / on-premises / multi-provider; obstacles enumerated (a)-(e); no bare "must let customers leave" | **Chapter VI umbrella switching duty; Q9/Q10 attach through G4*/G5*** (Q9 default = G4a, Q10 default = G5a — G1 is not the default node of either edge); **G8 forward scope dependency**; procedure G2a/G2b/G2c (25), info G3 (26), good faith G7 (27), charges G4a/G4b (29), technical G5a/G5b/G5c (30) — all this block ✓; **G8 (Art 31, `…114`) forward dependency → R3.3-H ⚠** — 31(1) bespoke carve-out reaches G1 only as to Art 23(d); 31(2) exempts the whole of Ch VI for non-production test/eval services | **VERIFIED_LITERAL** *(G8/Art 31 forward-dependency flagged)* | 2026-09-02 |
| `EP-CLM-000102` | R-G9 | Art. 24 | scope-limiter verbatim ("responsibilities … laid down in Articles 23, 25, 29, 30 and 34 shall apply only to the services, contracts or commercial practices provided by the **source provider**") | Not broader — expressly narrows Arts 23/25/29/30/34 to the source provider | **Scope-limiter** on G1/G2*/G4*/G5* (and Ch VIII Art 34) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000103` | R-G2a | Art. 25(1) | written pre-signing contract verbatim ("clearly set out in a written contract … available to the customer prior to signing … store and reproduce") | Not broader | **Procedure on G1** (contract form) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000104` | R-G2b | Art. 25(2)(a)-(i) | mandatory contract terms verbatim incl. the numeric limits: **transition ≤ 30 calendar days** (a), **notice ≤ two months** (d), **retrieval ≥ 30 calendar days** (g), trade-secret exemption not to impede switching (f), switching charges per Art 29 (i) | **Not broader** — "at least the following"; all three numeric bounds retained exactly; trade-secret carve-out kept switch-preserving | **Procedure on G1** (contract content) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000105` | R-G2c | Art. 25(3)/(4)/(5) | customer options (switch/on-prem/erase) 25(3); **unfeasibility: notify within 14 working days, alternative period ≤ seven months** 25(4); right to extend once 25(5) | Not broader — the 14 wd / ≤ 7 month bounds and the single customer-initiated extension retained | **Procedure on G1** (customer election + unfeasibility) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000106` | R-G3 | Art. 26(a)/(b) | information duty verbatim: (a) switching/porting procedures, methods, formats, restrictions/limits; (b) up-to-date online register of data structures/formats + standards/open interoperability specs | Not broader | **Info duty supporting G1** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000107` | R-G7 | Art. 27 | good-faith cooperation verbatim ("All parties involved, including destination providers … shall cooperate in good faith … enable the timely transfer of data and maintain … continuity") | Not broader — binds all parties incl. destination provider | **Cooperation duty supporting G1** (referenced by Art 30(1)) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000108` | R-G6 | Art. 28(1)/(2) | contractual transparency verbatim: 28(1)(a) jurisdiction of ICT infrastructure; (b) measures to prevent international governmental access/transfer of non-personal data conflicting with Union/MS law; 28(2) websites listed in contracts | Not broader — a transparency/disclosure duty, not a substantive transfer ban | **N3 companion to H1a** (Art 32, Ch VII, Block 8) — cross-chapter forward reference; G6 stands as its own operative transparency duty | **VERIFIED_LITERAL** *(N3 → H1a cross-chapter reference noted; not a blocking dependency)* | 2026-09-02 |
| `EP-CLM-000109` | R-G4a | Art. 29(1) | charge-abolition verbatim ("**From 12 January 2027**, providers … shall not impose any switching charges … for the switching process") | Not broader — dated abolition, scoped to switching charges | **Q9 DEFAULT**; interim carve-out G4b (29(2)/(3)); **bespoke exemption G8 (Art 31, `…114`) forward ⚠** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000110` | R-G4b | Art. 29(2)/(3) | interim reduced-charge verbatim ("From 11 January 2024 to 12 January 2027 … may impose reduced switching charges") + cost cap ("shall not exceed the costs … directly linked to the switching process") | Not broader — window-bounded and cost-capped | **Q9 qualifies G4a** (interim phase) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000111` | R-G5a | Art. 30(1) | IaaS functional-equivalence verbatim ("scalable and elastic computing resources limited to infrastructural elements … take all reasonable measures in their power to facilitate that the customer … achieves functional equivalence") | Not broader — bounded to the infrastructural tier + "reasonable measures … in their power" | **Q10 DEFAULT**; **bespoke exemption G8 (Art 31, `…114`) forward ⚠** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000112` | R-G5b | Art. 30(2) | open-interface verbatim ("Providers … other than those referred to in paragraph 1 … make open interfaces available … free of charge … for … data portability and interoperability") | Not broader — non-IaaS tier; distinct from 30(1) | **Q10 qualifies G5a** (other-tier duty) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000113` | R-G5c | Art. 30(3)/(5)/(6) | standards verbatim: **≥ 12 months** compatibility with common specs / harmonised standards 30(3); machine-readable export absent standards 30(5); **limits** — no duty to develop new tech / disclose IP or trade secrets / compromise security 30(6) | Not broader — the standards duty is bounded by the 12-month trigger and the 30(6) IP/trade-secret/security limits | **Q10 qualifies G5a** (standards/export + limits) | **VERIFIED_LITERAL** | 2026-09-02 |

## 55. Tally — R3.3-G (Block 7)

- **Reviewed:** 14 (`EP-CLM-000100` … `EP-CLM-000113`, rows F6/G1/G9/G2a/G2b/G2c/G3/G7/G6/G4a/G4b/G5a/G5b/G5c).
- **`VERIFIED_LITERAL`:** **14** — `last_verified_at = 2026-09-02` set on all fourteen.
- **`NEEDS_REWRITE`:** 0 · **`NEEDS_QUALIFIER`:** 0 · **`SOURCE_CONSTRAINED`:** 0 · **`BLOCKED`:** 0.
- **State advance:** `workflow_state: draft → verified` (internal) on the fourteen; **`validity_state` stays `null`, `published` stays `false`** — no publication-state advance, no Freshness/Publish Gate.
- **Running R3.3 total:** 68/68 `VERIFIED_LITERAL` across Blocks 1–7 (`EP-CLM-000046..000113`).

## 56. Chapter V scope-limit closure — the F1 → F6 forward dependency (the reason F6 was verified first)

**CLOSED.** F6 (`EP-CLM-000100`, Art. 16) is now `VERIFIED`. The Chapter V B2G regime verified in R3.3-F — **F1** and its routes/procedure/compensation/limits **F2a, F2b, F2c, F3a, F3b, F4a, F4b, F5a, F5b** — now carries its **Art. 16 scope-limit**: Chapter V does not affect other reporting/access/compliance obligations (16(1)) and does not apply to criminal/administrative-offence enforcement or to customs/taxation administration (16(2)). **The R3.3-F forward dependency flagged on F1 (`…090`) is resolved**; the Chapter V regime may proceed to R3.4 with its Q7 carve-out present. This mirrors the anti-waiver closures of R3.3-E (D10 → Ch III) and R3.3-F (E6 → Ch IV): each block opens by closing the prior chapter's deferred boundary item.

## 57. Corrigendum (EP-SRC-000007) effect on Block 7

**NONE.** The corrigendum touches **Article 48 only**. Block 7 covers **Arts. 16, 23, 24, 25, 26, 27, 28, 29, 30**; none is touched. Block 7 rests on `EP-SRC-000006` unmodified.

## 58. Qualifier / edge check for Block 7 (Q9 + Q10 the key checks)

- **Q7 (F1 ↔ F6 scope-limit):** F6 verified this block; closes the R3.3-F F1 → F6 forward dependency (§56). **PASS.**
- **Q9** (G4a switching-charge abolition ↔ its carve-outs): G4a (29(1) abolition from 12 Jan 2027) rendered with **G4b** (29(2)/(3) interim reduced ≤ cost, 11 Jan 2024 – 12 Jan 2027 ✓) — both this block. **The bespoke/test-version exemption G8 (Art 31, `…114`) is the outstanding limb, deferred to R3.3-H.** **PASS-with-flag.**
- **Q10** (G5a IaaS functional equivalence ↔ tiered duties): G5a (30(1)) rendered with **G5b** (30(2) open interfaces other tier ✓) and **G5c** (30(3)/(5)/(6) standards/export + IP/trade-secret/security limits ✓) — all this block. **The Art 31 exemption G8 (`…114`) is the outstanding limb, deferred to R3.3-H.** **PASS-with-flag.**
- **G8 forward dependency (Art 31, `…114`) — two layers, recorded separately:** G8 is **not** verified here (it falls in Block 8's numeric range and begins R3.3-H), but its two Art. 31 layers have different reach and must both be closed before publication:
  - **Art. 31(1) — limited bespoke / custom-built exemption:** disapplies **only Art. 23(d), Art. 29, and Art. 30(1) and (3)**. It therefore reaches **G1 only as to its Art. 23(d) functional-equivalence limb**, plus **G4a/G4b** (Art 29 charges, Q9) and the **Art. 30(1)/(3) limbs represented by G5a/G5c** (Q10). It does **not** disapply G2*/G3/G6/G7/G9/G5b, nor the rest of G1.
  - **Art. 31(2) — whole-of-Chapter-VI non-production/test-evaluation exemption:** the obligations of the **entire Chapter VI** do not apply to qualifying non-production services provided for a limited period — so it must scope **all applicable Chapter VI operative duties verified in this block** (G1, G2a/G2b/G2c, G3, G6, G7, G9, G4a/G4b, G5a/G5b/G5c), not just the Q9/Q10 nodes.
  - **Art. 31(3) — pre-contract disclosure duty:** the provider must inform the prospective customer which Chapter VI obligations do not apply.
  - Net: G1/G4a/G4b/G5a/G5c must render with the 31(1) carve-out present, **and** every applicable Chapter VI duty must render with the 31(2) scope exemption present, once publication stages begin. **Flagged forward (mirrors F6/E6/D10).**
- **N3 (G6 ↔ H1a):** G6 (Art 28 contractual transparency on international access) is the N3 companion to H1a (Art 32, Ch VII, Block 8). H1a is **not** in this block; the N3 edge is a **cross-chapter forward reference**, not a blocking dependency — G6 is a self-standing transparency duty and is verified literally on its own terms. **Noted; H-series deferred to R3.3-H.**
- **G9 scope-limiter (Art 24):** verified this block; confines Arts 23/25/29/30 (and Ch VIII Art 34) to the source provider — bounds G1/G2*/G4*/G5* against over-reading. **PASS.**
- **Block 6 B2G logic untouched:** the emergency (15(1)(a) → 20(1) free) / non-emergency (15(1)(b) → 20(2)/(3) compensated) split verified in R3.3-F is not reopened or altered here; F6 only adds Art 16's scope-limit around it. **Unchanged.**

## 59. Guards honoured (R3.3-G)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**.
- No new `EP-CLM` / `EP-SRC` minted; **no renumbering** (the "G1–G8" label / numeric-range mismatch is recorded in §52, not resolved by renumbering). No claim verified outside Block 7 (G8/`…114` explicitly deferred; H-series untouched). Blocks 1–6 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed. Block 8 not begun.

## 60. Recommendation — R3.3-H

Proceed to **R3.3-H = Block 8** (*Unlawful international governmental access, Chapter VII*, `EP-CLM-000114` … `EP-CLM-000116`, rows **G8**, H1a–H1b) on a fresh branch off `main` after this unit merges. **Begin by verifying `EP-CLM-000114` (R-G8 = Art. 31) FIRST, with all three limbs, and close both exemption layers before any Chapter VII claim:** (i) **Art. 31(1)** — the limited bespoke / custom-built exemption reaching G1 (as to Art. 23(d)), G4a/G4b (Art. 29), and G5a/G5c (Art. 30(1)/(3)); (ii) **Art. 31(2)** — the whole-of-Chapter-VI non-production / test-evaluation exemption, which must scope every applicable Chapter VI operative duty verified in Block 7; and (iii) **Art. 31(3)** — the pre-contract disclosure duty. Only once both the 31(1) limited-bespoke dependencies and the 31(2) Chapter-VI-wide exemption are closed should R3.3-H proceed to H1a/H1b — exactly as this unit opened with F6, R3.3-F with E6, and R3.3-E with D10. Then Ch VII under **N6** (H1a Art 32(1) prevent third-country government access to non-personal data ↔ H1b Art 32(2) international-agreement recognition ↔ H1c Art 32(3)-(5) absent-agreement conditions), with the **N3** companion to G6 (Art 28, verified in this block) now closable. **Note the numeric-range seam continues:** rows H1a/H1b/H1c are `EP-CLM-000115`/`000116`/`000117`, so `…117` (H1c) will fall at Block 9's numeric boundary — treat the numeric range as authoritative and record the mismatch rather than renumbering.

---

# R3.3-H (Terminal Closeout) — Blocks 8–10 (Ch VI exemption close + Int'l access · Ch VII, Interop & smart contracts · Ch VIII, Enforcement & final · Ch IX–XI)

**Unit status:** **COMPLETE / PASS** — 19/19 `VERIFIED_LITERAL`. **Date:** 2026-09-02. **Basis:** `EP-SRC-000006` read with `EP-SRC-000007`. Blocks 1–7 untouched. **G8 verified FIRST** to close the Chapter VI Art. 31 exemption (both layers) over the R3.3-G switching regime. **This is the terminal R3.3 unit: it consolidates the remaining Blocks 8, 9 and 10 into one closeout and finishes Human Literal Verification at 87/87.**

## 61. Scope of this unit — Terminal Closeout (Blocks 8–10)

Verifies the **entire remaining numeric range `EP-CLM-000114` … `EP-CLM-000132`** (nineteen identities) in one consolidated closeout, preserving internal seam order. **First item = G8 (`EP-CLM-000114`, Art. 31)** — the Chapter VI exemption deferred from R3.3-G — then Chapters VII → VIII → IX–XI in numeric order: **G8, H1a, H1b, H1c, I3a, I4, J1, K1a, K1b, K1c, K1d, K3, K2a, K2b, K2c, K4, K5a, K5b, K5c**.

**Consolidation rationale:** the remaining three draft-sequence blocks (Block 8 `…114–…116`, Block 9 `…117–…119`, Block 10 `…120–…132`) are verified together as the terminal unit. The recurring "label vs numeric range" seam is now internal to this closeout and carries no trailing forward dependency — **`EP-CLM-000132` is the last minted identity** (next free is `…133`; nothing beyond is minted), so no boundary item is deferred past this unit. Internal seam markers preserved: **G8/`…114`** opens by closing Ch VI; the old Block 8/9 boundary (**H1c/`…117`**) and Block 9/10 boundary (**J1/`…120`**) are verified in numeric position, not as separate units.

**Excluded by design (not in range, not verified, correctly so):** **I1 (Art. 33)** and **I2 (Art. 35)** interoperability essential requirements carry **no `EP-CLM` identity** — source-constrained / standards-pending (R3.2 §4); they cannot enter R3.3 until Commission delegated acts / harmonised standards publish. **Arts. 41, 42, 45–49** (model terms, EDIB, delegation/comitology, amendments, evaluation) mint nothing and are not verified. **Art. 48** — the only corrigendum-touched article — is unminted, so the corrigendum remains no-effect on every verified claim.

## 62. Verbatim anchors used (quoted from EP-SRC-000006)

**Article 31 — Specific regime for certain data processing services (G8, Ch VI exemption; both layers):**
> 31(1) [G8 — limited bespoke]: "The obligations laid down in Article 23, point (d), Article 29 and Article 30(1) and (3) shall not apply to data processing services of which the majority of main features has been custom-built to accommodate the specific needs of an individual customer or where all components have been developed for the purposes of an individual customer, and where those data processing services are not offered at broad commercial scale via the service catalogue of the provider …"
> 31(2) [G8 — whole-of-Chapter-VI]: "The obligations laid down in this Chapter shall not apply to data processing services provided as a non-production version for testing and evaluation purposes and for a limited period of time."
> 31(3) [G8 — disclosure]: "Prior to the conclusion of a contract …, the provider … shall inform the prospective customer of the obligations of this Chapter that do not apply."

**Article 32 — International governmental access and transfer (H1a/H1b/H1c):**
> 32(1) [H1a]: "Providers of data processing services shall take all adequate technical, organisational and legal measures, including contracts, in order to prevent international and third-country governmental access and transfer of non-personal data held in the Union where such transfer or access would create a conflict with Union law or with the national law of the relevant Member State, without prejudice to paragraph 2 or 3."
> 32(2) [H1b]: "Any decision or judgment of a third-country court or tribunal and any decision of a third-country administrative authority requiring a provider … to transfer or give access to non-personal data … held in the Union shall be recognised or enforceable in any manner only if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union, or … a Member State."
> 32(3) [H1c]: "In the absence of an international agreement …, transfer to or access to such data by that third-country authority shall take place only where: (a) the third-country system requires the reasons and proportionality … to be set out and … specific in character …; (b) the reasoned objection of the addressee is subject to a review by a competent third-country court or tribunal; and (c) the competent third-country court or tribunal … is empowered … to take duly into account the relevant legal interests of the provider … protected by Union law …" · 32(4) [H1c]: minimum-data-permissible limb · 32(5) [H1c]: "shall inform the customer about the existence of a request … before complying …, except where the request serves law enforcement purposes …"

**Article 34 — Interoperability for in-parallel use (I3a/I4):**
> 34(1) [I3a]: "The requirements laid down in Article 23, Article 24, Article 25(2), points (a)(ii), (a)(iv), (e) and (f) and Article 30(2) to (5) shall also apply mutatis mutandis to providers of data processing services to facilitate interoperability for the purposes of in-parallel use of data processing services."
> 34(2) [I4]: "Where a data processing service is being used in parallel with another data processing service, the providers … may impose data egress charges, but only for the purpose of passing on egress costs incurred, without exceeding such costs."

**Article 36 — Essential requirements regarding smart contracts (J1):**
> 36(1) [J1]: "The vendor of an application using smart contracts or, in the absence thereof, the person whose … profession involves the deployment of smart contracts for others … to make data available shall ensure that those smart contracts comply with the following essential requirements of: (a) robustness and access control …; (b) safe termination and interruption …; (c) data archiving and continuity … (auditability); (d) access control …; and (e) consistency … with the terms of the data sharing agreement that the smart contract executes."
> 36(2)/(3) [J1]: "… shall perform a conformity assessment … and, on the fulfilment of those requirements, issue an EU declaration of conformity." + responsibility for compliance. (36(4) harmonised-standard conformity presumption.)

**Article 37 — Competent authorities and data coordinators (K1a/K1b/K1c/K1d):**
> 37(1)/(2) [K1a]: "Each Member State shall designate one or more competent authorities …"; "… it shall designate a data coordinator from among them to facilitate cooperation …" · 37(5) tasks/powers (a)-(j) incl. "(d) imposing effective, proportionate and dissuasive financial penalties …", "(i) ensuring that switching charges are withdrawn in accordance with Article 29", "(j) examining the requests for data made pursuant to Chapter V" · 37(6) data-coordinator single-point-of-contact · 37(7) "The Commission shall maintain a public register of those authorities."
> 37(3) [K1b]: "The supervisory authorities responsible for monitoring the application of Regulation (EU) 2016/679 shall be responsible for monitoring the application of this Regulation insofar as the protection of personal data is concerned … The European Data Protection Supervisor shall be responsible … insofar as it concerns the Commission, the European Central Bank or Union bodies …"
> 37(10) [K1d]: "Entities falling within the scope of this Regulation shall be subject to the competence of the Member State where the entity is established. Where the entity is established in more than one Member State, it shall be considered to be under the competence of the Member State in which it has its main establishment …"
> 37(11)/(12)/(13) [K1c]: "Any entity … that makes connected products available or offers services in the Union, and which is not established in the Union, shall designate a legal representative in one of the Member States." + mandate (12) + "Until such time as an entity designates a legal representative …, it shall be under the competence of all Member States … Any competent authority may exercise its competence, including by imposing effective, proportionate and dissuasive penalties …" (13)

**Articles 38 & 39 — Complaint + effective judicial remedy (K3):**
> 38(1) [K3]: "… natural and legal persons shall have the right to lodge a complaint, individually or, where relevant, collectively, with the relevant competent authority … if they consider that their rights under this Regulation have been infringed." (38(2)/(3) information + cooperation.)
> 39(1) [K3]: "… any affected natural and legal person shall have the right to an effective judicial remedy with regard to legally binding decisions taken by competent authorities." (39(2) failure-to-act remedy; 39(3) forum.)

**Article 40 — Penalties (K2a/K2b/K2c):**
> 40(1) [K2a]: "Member States shall lay down the rules on penalties … The penalties provided for shall be effective, proportionate and dissuasive." · 40(2) [K2a]: "Member States shall by 12 September 2025 notify the Commission …" · 40(3) [K2a]: non-exhaustive criteria (a)-(f).
> 40(4) [K2b]: "For infringements of the obligations laid down in Chapter II, III and V …, the supervisory authorities responsible for monitoring the application of Regulation (EU) 2016/679 may … impose administrative fines in accordance with Article 83 of Regulation (EU) 2016/679 and up to the amount referred to in Article 83(5) …"
> 40(5) [K2c]: "For infringements of the obligations laid down in Chapter V …, the European Data Protection Supervisor may impose … administrative fines in accordance with Article 66 of Regulation (EU) 2018/1725 up to the amount referred to in Article 66(3) …"

**Article 43 — Sui generis right (K4):**
> 43 [K4]: "The sui generis right provided for in Article 7 of Directive 96/9/EC shall not apply when data is obtained from or generated by a connected product or related service falling within the scope of this Regulation, in particular in relation to Articles 4 and 5 thereof."

**Article 44 — Other Union legal acts / savings (K5a/K5b/K5c):**
> 44(1) [K5a]: "The specific obligations for the making available of data … in Union legal acts that entered into force on or before 11 January 2024, and delegated or implementing acts pursuant thereto, shall remain unaffected."
> 44(2) [K5b]: "This Regulation is without prejudice to Union law specifying, in light of the needs of a sector, a common European data space, or an area of public interest, further requirements …"
> 44(3) [K5c]: "This Regulation, with the exception of Chapter V, is without prejudice to Union and national law providing for access to and authorising the use of data for scientific research purposes."

## 63. Terminal Closeout verification table (19 identities · EP-CLM-000114 … 000132)

| EP-CLM | Row | Locator | Literal check vs source | Over-breadth check | Role / edge & dependency | Verdict | `last_verified_at` |
|---|---|---|---|---|---|---|---|
| `EP-CLM-000114` | R-G8 | Art. 31(1)/(2)/(3) | both layers verbatim: 31(1) limited bespoke (only Art 23(d)/29/30(1)/(3)); 31(2) whole-of-Ch-VI for non-production test/eval; 31(3) pre-contract disclosure | Not broader — 31(1) enumerates the exact disapplied provisions; 31(2) is limited to non-production "for a limited period" | **Q9/Q10 exemption via 31(1) + Ch-VI-wide scope exemption via 31(2)**; **Verified FIRST.** Closes the R3.3-G G1/G4a/G4b/G5a/G5c forward dependency (§65) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000115` | R-H1a | Art. 32(1) | prevention duty verbatim ("all adequate technical, organisational and legal measures … to prevent international and third-country governmental access and transfer of non-personal data … conflict with Union law …") | Not broader — **non-personal data only**; "without prejudice to paragraph 2 or 3" | **N6 DEFAULT**; **N3 companion to G6** (Art 28, R3.3-G ✓) — N3 now CLOSED | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000116` | R-H1b | Art. 32(2) | recognition-only-via-agreement verbatim ("recognised or enforceable in any manner only if based on an international agreement, such as a mutual legal assistance treaty …") | Not broader — bounded to third-country decisions re non-personal data in the Union | **N6 qualifies H1a** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000117` | R-H1c | Art. 32(3)-(5) | absent-agreement conditions (a)/(b)/(c) verbatim + minimum-data 32(4) + customer-notification 32(5) (with law-enforcement exception) | Not broader — cumulative (a)-(c) conditions retained; notification carve-out kept | **N6 qualifies H1a** (old Block 8/9 numeric boundary — verified in position) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000118` | R-I3a | Art. 34(1) | in-parallel-use interoperability verbatim ("requirements laid down in Article 23, Article 24, Article 25(2), points (a)(ii), (a)(iv), (e) and (f) and Article 30(2) to (5) shall also apply mutatis mutandis …") | Not broader — exact cross-referenced sub-provisions; "mutatis mutandis" scope | **N4** — reuses G1/G9/G2b/G5b/G5c (all R3.3-G ✓) mutatis mutandis; N4 CLOSED with I4 | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000119` | R-I4 | Art. 34(2) | in-parallel egress-charge cap verbatim ("may impose data egress charges, but only for the purpose of passing on egress costs incurred, without exceeding such costs") | Not broader — cost-pass-through only | **N4 companion to I3a** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000120` | R-J1 | Art. 36(1)-(4) | five essential requirements (a)-(e) verbatim + conformity assessment + **EU declaration of conformity** 36(2)/(3) + harmonised-standard presumption 36(4) | Not broader — the five requirements are exhaustive; duty falls on the vendor/deployer | **N7 scope-gated** — only entrants deploying smart contracts to make data available; N7 CLOSED (old Block 9/10 numeric boundary — verified in position) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000121` | R-K1a | Art. 37(1)/(2)/(5)/(6)/(7) | competent-authority designation + data coordinator + tasks/powers (a)-(j) incl. penalties (d), switching-charge withdrawal (i), Ch V request examination (j) + public register 37(7) | Not broader | **Enforcement architecture** (hosts K1b/K1c/K1d/K3/K2*) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000122` | R-K1b | Art. 37(3) | GDPR-SA personal-data supervision + EDPS for Commission/ECB/Union bodies verbatim (Ch VI/VII GDPR mutatis mutandis) | Not broader — supervision confined to personal-data processing | **Interface to GDPR/EUDPR** (companion to K2b/K2c) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000123` | R-K1c | Art. 37(11)/(12)/(13) | non-EU entity **must designate a legal representative**; mandate; "until … designates … under the competence of all Member States … effective, proportionate and dissuasive penalties" | Not broader — the entrant enforcement hook, verbatim | **N5 enforcement hook** — the non-EU-entrant handle for every substantive duty; N5 CLOSED | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000124` | R-K1d | Art. 37(10) | jurisdiction / main-establishment rule verbatim ("competence of the Member State where the entity is established … main establishment … head office or registered office …") | Not broader | **Jurisdiction rule** on K1a | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000125` | R-K3 | Arts. 38(1)-(3), 39(1)-(3) | right to lodge complaint (individually/collectively) 38 + right to effective judicial remedy over binding decisions 39, incl. failure-to-act (39(2)) and forum (39(3)) | Not broader — bounded remedy (rights-under-this-Regulation) | **Bounded remedy** on K1a | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000126` | R-K2a | Art. 40(1)/(2)/(3) | national penalties "effective, proportionate and dissuasive"; **notify by 12 September 2025**; non-exhaustive criteria (a)-(f) | Not broader — criteria expressly non-exhaustive | **Q11 DEFAULT** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000127` | R-K2b | Art. 40(4) | GDPR Art. 83 fines for **Ch II/III/V** infringements, GDPR-SA competence, up to Art. 83(5) amount — verbatim | Not broader — chapter-scoped to II/III/V and to GDPR-SA competence | **Q11 qualifies K2a** (GDPR-SA fine route) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000128` | R-K2c | Art. 40(5) | EDPS fines for **Ch V** infringements per Reg (EU) 2018/1725 Art. 66, up to Art. 66(3) — verbatim | Not broader — scoped to Ch V and EDPS competence | **Q11 qualifies K2a** (EDPS fine route) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000129` | R-K4 | Art. 43 | sui generis DB-right exclusion verbatim ("shall not apply when data is obtained from or generated by a connected product or related service … in particular in relation to Articles 4 and 5") | Not broader — carve-out tied to connected-product/related-service data | **Q12 carve-out** of the external Dir. 96/9/EC Art. 7 right; Q12 CLOSED | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000130` | R-K5a | Art. 44(1) | pre-2024 sectoral acts unaffected verbatim ("Union legal acts that entered into force on or before 11 January 2024 … shall remain unaffected") | Not broader | **Q14 qualifies A1** (general-layer savings) | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000131` | R-K5b | Art. 44(2) | without-prejudice-to-further-sector/data-space-requirements verbatim (technical access / holder-right limits / beyond-access aspects) | Not broader | **Q14 qualifies A1** | **VERIFIED_LITERAL** | 2026-09-02 |
| `EP-CLM-000132` | R-K5c | Art. 44(3) | scientific-research carve-out verbatim ("with the exception of Chapter V, is without prejudice to Union and national law providing for access to and authorising the use of data for scientific research purposes") | Not broader — **Ch V expressly excepted** from the research carve-out | **Q14 qualifies A1**; **LAST minted identity** (`…132`) — no trailing forward dependency | **VERIFIED_LITERAL** | 2026-09-02 |

## 64. Tally — Terminal Closeout + R3.3 GRAND TOTAL

- **Reviewed this unit:** 19 (`EP-CLM-000114` … `EP-CLM-000132`).
- **`VERIFIED_LITERAL` this unit:** **19** — `last_verified_at = 2026-09-02` on all nineteen. 0 NEEDS_REWRITE / NEEDS_QUALIFIER / SOURCE_CONSTRAINED / BLOCKED.
- **State advance:** `workflow_state: draft → verified` (internal) on the nineteen; **`validity_state` stays `null`, `published` stays `false`.**
- **R3.3 GRAND TOTAL:** **87/87 `VERIFIED_LITERAL`** across Blocks 1–10 (`EP-CLM-000046..000132`). **Human Literal Verification COMPLETE.** 0 remaining `draft` verification identities (I1/I2 excluded — unminted, source-constrained).

## 65. Forward-dependency & edge closures (all edges now closed)

- **G8 / Art. 31 (both layers) — CLOSED:** 31(1) limited bespoke and 31(2) whole-of-Chapter-VI non-production exemptions verified; the R3.3-G forward dependency on G1/G4a/G4b/G5a/G5c is resolved (mirrors the F6/E6/D10 openings). No exemption limb outstanding.
- **N3 (G6 ↔ H1a) — CLOSED:** the Art. 28 transparency companion (G6, R3.3-G ✓) now sits with the Art. 32(1) prevention duty (H1a ✓).
- **N4 (I3a/I4 reuse G1/G2b/G5) — CLOSED:** the in-parallel-use regime reuses the R3.3-G switching duties mutatis mutandis; both I-rows verified.
- **N5 (legal-representative hook) — CLOSED:** K1c (Art. 37(11)/(13)) is the non-EU-entrant enforcement hook for every substantive Data Act duty verified in Blocks 1–10.
- **N6 (H1a ↔ H1b/H1c) — CLOSED:** the two-tier recognition/absent-agreement test is fully present.
- **N7 (J1 scope-gated) — CLOSED:** smart-contract essential requirements + EU declaration, gated to entrants deploying smart contracts.
- **Q11 (K2a ↔ K2b/K2c) — CLOSED:** national penalties default with both chapter-scoped fine routes (GDPR-SA for Ch II/III/V; EDPS for Ch V).
- **Q12 (K4) — CLOSED:** sui generis carve-out bounds the external Dir. 96/9/EC right.
- **Q14 (A1 ↔ K5a/b/c) — CLOSED:** general-layer savings (pre-2024 acts, sector/data-space, research-except-Ch-V).
- **Full constraint ledger:** Q1–Q16 and N1–N7 are now **all closed** across R3.3 (Q1 A-phasing ✓ R3.3-A; Q2/Q13/Q15/Q16 ✓ R3.3-B; Q3/Q4 ✓ R3.3-C/D; Q5/N1/N2 ✓ R3.3-D; Q6/Q15-Ch-IV ✓ R3.3-E/F; Q7/Q8 ✓ R3.3-F; Q9/Q10 ✓ R3.3-G; N3/N4/N5/N6/N7/Q11/Q12/Q14 ✓ this unit). **No orphan default remains.**

## 66. Corrigendum (EP-SRC-000007) effect on Blocks 8–10

**NONE.** The corrigendum touches **Article 48 only** — which mints no identity and is not verified. Blocks 8–10 cover Arts. 31, 32, 34, 36, 37, 38, 39, 40, 43, 44; none is touched. The whole of R3.3 rests on `EP-SRC-000006` unmodified.

## 67. Guards honoured (Terminal Closeout)

- No public `claims.json` created. No public HTML, `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt` touched.
- Freshness Gate **not opened**; Publish Gate **not opened**. `validity_state` null, `published` false throughout.
- No new `EP-CLM` / `EP-SRC` minted; no renumbering. I1/I2 (Arts 33/35) remain **unminted / source-constrained** and are **not** verified. Blocks 1–7 results unchanged.
- No CRA / EERS / Protocol work. No route score ≥ 90 claimed (RGS re-score is R3.8, behind the Publish Gate).

## 68. R3.3 COMPLETE — handoff to production staging

**R3.3 Human Literal Verification is COMPLETE / PASS at 87/87.** Every minted `EP-CLM` (`…046..132`) is `VERIFIED_LITERAL` against `EP-SRC-000006` (read with `…007`); every Q1–Q16 + N1–N7 edge is closed; all state stays internal (`validity_state` null, `published` false). **The next stage is production staging (R3.4 canonical graph → R3.5 page transformation), built as a `release-candidate` work-product with `published: false` — NOT a gate-opening step.** The public Publish Gate (R3.8: live `/regulation/eu-data-act/` swap + `claims.json` registration in `routes.json`/`sitemap.xml`/`llms.txt` + RGS re-score ≥ 90) remains **closed** and is deferred to a separate, explicitly-authorised production PR after human review of the release-candidate.

---

*EuraPlan.com — Sprint R3.3 workbench verification record (R3.3-A Block 1 + R3.3-B Block 2 + R3.3-C Block 3 + R3.3-D Block 4 + R3.3-E Block 5 + R3.3-F Block 6 + R3.3-G Block 7 + R3.3-H Terminal Closeout Blocks 8–10). **R3.3 COMPLETE — 87/87 VERIFIED_LITERAL.** Internal. Not a published website page. No public claims.json.*
