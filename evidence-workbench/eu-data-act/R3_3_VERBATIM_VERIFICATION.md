# R3.3 — EU Data Act Human Literal (Verbatim) Verification
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.3 Human Literal Verification
**Status:** **BLOCK 1 COMPLETE / PASS** — 6/6 `VERIFIED_LITERAL`. Later blocks NOT started. **Internal workbench only — no public claims.json, no live surface, no publication-state advance.**
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

*EuraPlan.com — Sprint R3.3-A workbench verification record. Internal. Not a published website page. No public claims.json.*
