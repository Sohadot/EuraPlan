# AI_ACT_VERIFICATION_AUDIT_2026-08.md
**Status:** Public working evidence — Sprint 2A Evidence Record (frozen; a repository record, not a website page)
**Asset:** EuraPlan.com
**Audit type:** Forensic, read-only. No corpus change, no claim minted, no page edited.
**Audited surfaces:** `/regulation/eu-ai-act/index.html`, `/clock/index.html`
**Audited base:** `main` @ `bc4913b6eb0124d733d02d25089fd7a850947626` (content unchanged on this branch at audit time)
**Audit date:** 2026-08-18
**Governed by:** REFERENCE_SOVEREIGNTY_DOCTRINE.md, FRESHNESS_ENGINE.md, EVIDENCE_GRAPH_MODEL.md, CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md, SOURCE_POLICY.md, DISCLOSURE_BOUNDARY.md

---

## 0. What this record is — and is not

- This record documents the state of **legacy prose** on the two audited pages as of the audit date, judged against primary EU sources.
- It is **public working evidence** (Class 2 under `DISCLOSURE_BOUNDARY.md`): it lives in the public repository and is intended to be openly auditable. It is **not** a published website page and is not in the sitemap.
- The `A#` identifiers below are **temporary audit-row identifiers**. They are **not** `EP-CLM-*` claim identities, they are **not citable**, and they confer **no** identity on any statement.
- This record does **not** create Evidence Objects and does **not** retroactively assign claim identities to legacy prose. The Evidence Graph begins from current truth in Sprint 2B; legacy prose that was outdated is simply corrected forward, not reconstructed as superseded claims. This preserves history integrity (no manufactured past).
- No `verified_at` is set here; no public changelog is emitted; no live page date is advanced.

---

## 1. Material finding

Regulation (EU) **2026/1744** — "Digital Omnibus on AI", of 8 July 2026, published in the Official Journal **24 July 2026**, in force **27 July 2026** — amends Article 113 of the AI Act (Regulation (EU) 2024/1689) and also amends Regulation (EU) 2018/1139 (EASA) and Regulation (EU) 2023/1230 (Machinery). CELEX **32026R1744** confirmed verbatim on EUR-Lex.

Effect on the audited pages: the **high-risk application dates are outdated/superseded**, while both pages still display a "Verified — Art. 113" / "Source: Verified" badge over them. The asset's highest-risk claim was presented as verified while no longer correct — precisely the failure the Freshness Engine exists to prevent.

---

## 2. Verification ledger (full coverage)

Status vocabulary: confirmed / incomplete / outdated / superseded / unsupported / ambiguous.
Action vocabulary: retain / clarify / replace / remove / split.

### Group A — Identity & framing (low risk)
| # | Legacy statement | Primary source | Status | Action |
|---|---|---|---|---|
| A1 | Official name "Regulation (EU) 2024/1689 … of 13 June 2024" | EUR-Lex CELEX 32024R1689 | confirmed | retain |
| A2 | CELEX = 32024R1689 | EUR-Lex | confirmed | retain |
| A3 | "horizontal rules for AI systems and GPAI models" | 2024/1689 | confirmed | retain |

### Group B — Article 113 timeline (high risk — audit core)
| # | Legacy date/statement | Official position now | Status | Action |
|---|---|---|---|---|
| A4 | Entry into force = 1 Aug 2024 | Unchanged | confirmed | retain |
| A5 | Art 113(1) → 2 Feb 2025: prohibited practices (Ch. II) + AI literacy (Ch. I) | Unchanged | confirmed | retain |
| A6 | Art 113(2) → 2 Aug 2025: GPAI + governance | Unchanged | confirmed | retain |
| A7 | Art 113(3) → 2 Aug 2026: "general application **including high-risk Annex III**" | General application 2 Aug 2026 **remains**; high-risk Annex III (Art 6(2), Ch. III Sec 1–3) **deferred to 2 Dec 2027** by 2026/1744 | outdated (conflated) | **split**: (a) general application 2 Aug 2026 = retain; (b) high-risk Annex III = replace → 2 Dec 2027 |
| A8 | Art 113(4) → 2 Aug 2027: high-risk Annex I | **Deferred to 2 Aug 2028** (Art 6(1)/Annex I) by 2026/1744 | superseded | replace |

### Group C — Roles & classification (definitional)
| # | Legacy statement | Status | Action |
|---|---|---|---|
| A9 | Provider / Deployer / Importer / Distributor / Authorised-rep summaries (with explicit deference to official text) | confirmed (as planning summaries) | retain |
| A10 | GPAI provider — Art 113(2) brings GPAI obligations | confirmed | retain |
| A11 | Product manufacturer — Annex I on "later Art 113(4)" timeline | concept valid; implied 2027 date now 2028 | clarify (follows A8) |
| A12 | High-risk via Annex III / Annex I pathways | structure valid; timing changed (A7/A8) | clarify |
| A13 | Clock role panel: "Annex III obligations phase in from **August 2, 2026** (Art. 113.3)" | now 2 Dec 2027 | replace |

### Group D — New matter in the amending instrument (coverage gaps / additions)
| # | Item | Status | Action |
|---|---|---|---|
| A14 | New prohibited practices Art 5(1)(ba) (non-consensual intimate imagery) and (bb) (CSAM), plus Art 5(1a)/(1b), apply from **2 December 2026**, per Article 113 third paragraph point (a) as amended by 2026/1744 | **confirmed** (corrected from earlier ambiguous) | addition (minted 2B) |
| A15 | 2026/1744 also amends EASA (2018/1139) and Machinery (2023/1230) | confirmed (amendment exists) | out of scope for AI Act page; add to DIM-01 map |
| A16 | Articles 102–110 of the AI Act apply from **27 July 2026** (further amendment inside Article 113) | confirmed | addition (minted 2B) |

### Group E — Governance
| # | Item | Status | Action |
|---|---|---|---|
| A17 | Both pages badge the high-risk dates "Verified — Art. 113" | now false for high-risk dates | clarify/replace at implementation |

---

## 3. EERS impact
- **DIM-02 (Compliance Timeline):** direct — high-risk deadline structure moved (A7/A8/A14).
- **DIM-01 (Regulatory Mapping):** add Regulation (EU) 2026/1744 (and its EASA/Machinery amendments) to the instrument map.
- **DIM-06 / DIM-07 (Product / Risk):** indirect — high-risk timing shift.

## 4. Primary sources
- Regulation (EU) 2026/1744 — EUR-Lex ELI https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng — CELEX 32026R1744 (OJ 24 Jul 2026; in force 27 Jul 2026).
- Regulation (EU) 2024/1689 — EUR-Lex CELEX 32024R1689 (Article 113 base).

## 5. Verification-confidence notes (methodological honesty)
1. Amended high-risk dates (2 Dec 2027 Annex III; 2 Aug 2028 Annex I) and "general application 2 Aug 2026 retained": HIGH confidence — from EUR-Lex primary text + convergent independent legal analyses.
2. A14 (2 Dec 2026 for the new Article 5 prohibitions): confirmed against the amended Article 113 third paragraph.
3. Base dates (A4–A6): HIGH confidence unchanged (not touched by the amendment).
4. The literal amending-provision locators (Regulation (EU) 2026/1744 Article 1 points (39)(a) and (40)(a–c)) were confirmed by the human verifier against the EUR-Lex primary text before the Sprint 2B batch was minted and verified.

## 6. Disclosure note
This record is public working evidence and is intended to be openly readable — see `DISCLOSURE_BOUNDARY.md`. It carries no confidential or operational-strategy content. It is excluded from crawling only for hygiene (it is not the canonical published corpus); `robots.txt` is a crawl directive, not an access control.

---

*EuraPlan.com — Sprint 2A Evidence Record (public working evidence). Not a published reference page. A# identifiers are non-citable.*
