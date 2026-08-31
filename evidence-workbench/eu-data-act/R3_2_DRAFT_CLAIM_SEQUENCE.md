# R3.2 — EU Data Act Draft Claim Sequence
**Sprint:** R3 — EU Data Act (EP-REG-003) · **Phase:** R3.2 Draft Claim Sequencing
**Status:** DRAFT SEQUENCE FIXED — **all `draft`. No public claims.json. No live surface.**
**Opened by:** DEC-060
**Date:** 2026-08-31

---

## 1. Purpose

Records the **order** in which the 87 minted `EP-CLM` identities (`R3_2_IDENTITY_REGISTER.md`) will be carried into R3.3 (human literal verification) and R3.4 (canonical graph). The sequence follows the **regulation's own structure** (Chapters I → XI) so that scope/definitions and defaults are verified **before** the rights, duties and carve-outs that depend on them, and every default is sequenced **adjacent to** its qualifier so the pair never separates.

## 2. Sequence blocks (all `workflow_state: draft`)

| # | Block | Chapters | EP-CLM range | Rows | Verify-order rationale |
|---|---|---|---|---|---|
| 1 | Instrument & temporal scope | I / XI (Art 50) | `…046`–`…051` | A1–A5b | Dates + applicability gate everything downstream |
| 2 | Definitions & boundaries | I / II | `…052`–`…061` | B1–B7 | Scope-gating definitions + GDPR boundary + anti-waiver before the duties they scope |
| 3 | Connected-product access (Ch II) | II | `…062`–`…071` | C1–D2 | User access & third-party sharing rights with their trade-secret / gatekeeper / personal-data qualifiers |
| 4 | Data-holder availability (Ch III) | III | `…072`–`…079` | D3–D10 | FRAND/compensation duties gated by the Art 12(1) applicability gate (D9) and Art 8(4) user-request gate (D8) |
| 5 | Unfair terms (Ch IV) | IV | `…080`–`…088` | E1a–E6 | Unenforceability rule minted with its scope (E3), fairness tests (E2*), carve-outs (E1b/E5), severability (E4) |
| 6 | B2G exceptional need (Ch V) | V | `…089`–`…099` | F1–F6 | Duty minted with exceptional-need routes, micro/small carve-out, compensation split, PSB limits |
| 7 | Switching (Ch VI) | VI | `…100`–`…113` | G1–G8 | Switching duties with numeric contract terms, charge phase-out and service-tier limits |
| 8 | International access (Ch VII) | VII | `…114`–`…116` | H1a–H1c | Non-personal-data prevention duty with its two-tier recognition test |
| 9 | Interoperability & smart contracts (Ch VIII) | VIII | `…117`–`…119` | I3a, I4, J1 | Only the operative parallel-use + smart-contract items; Arts 33/35 excluded (source-constrained) |
| 10 | Enforcement & final (Ch IX–XI) | IX–XI | `…120`–`…132` | K1a–K5c | Authorities, legal-representative hook, penalties (incl. 40(5)), sui generis carve-out, savings |

## 3. Sequencing invariants
- **Default-before/with-qualifier:** no default block is verified without the block(s) carrying its `qualified_by` rows already present (Q1–Q16, N1–N7 from R3.1-F).
- **No mint before falsification:** every ID in the sequence corresponds to a row that passed R3.1 falsification; nothing new is introduced here.
- **Source-constrained items excluded:** Arts. 33/35 (R-I1/I2) are **not** in the sequence — they carry no identity and cannot enter R3.3/R3.4 until standards are published.
- **All `draft`:** no `validity_state`, no `published`, no `last_verified_at`, no provenance SHA is set in R3.2. Those are R3.3+ real-event outputs.

## 4. Next
- **R3.3 — Human Literal Verification:** verify each drafted `EP-CLM` block against `EP-SRC-000006` (+ `…007`) in sequence order; only a real verification event sets `last_verified_at` / advances state.
- **No public `claims.json`, no page transformation, no Publish Gate** before R3.4/R3.5/R3.8 respectively, each under its own gate.

---

*EuraPlan.com — Sprint R3.2 workbench draft claim sequence. Internal. Not a published website page.*
