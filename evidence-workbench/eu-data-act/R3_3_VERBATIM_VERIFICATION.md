# R3.3 — EU Data Act Human Literal (Verbatim) Verification
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.3 Human Literal Verification
**Status:** **BLOCKS 1–2 COMPLETE / PASS** — 16/16 `VERIFIED_LITERAL` (Block 1 = 6, Block 2 = 10). Blocks 3–10 NOT started. **Internal workbench only — no public claims.json, no live surface, no publication-state advance.**
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

*EuraPlan.com — Sprint R3.3 workbench verification record (R3.3-A Block 1 + R3.3-B Block 2). Internal. Not a published website page. No public claims.json.*
