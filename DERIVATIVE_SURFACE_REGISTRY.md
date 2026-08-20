# DERIVATIVE_SURFACE_REGISTRY.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** EVIDENCE_GRAPH_MODEL.md, REFERENCE_SOVEREIGNTY_DOCTRINE.md, CLAIM_POLICY.md
**Opened by:** DEC-046 (Post-Merge homepage derivative drift)

---

## 1. Purpose

Any public surface that displays a date, phase, or other material fact taken from
the Evidence Graph is a **derivative surface**. Canonical truth lives in the claim
graph (e.g. `/regulation/eu-ai-act/claims.json` and the Verified Claim Register on
`/regulation/eu-ai-act/`). Derivative surfaces must not invent a parallel timeline.

This registry exists because Post-Merge Live Verification found the homepage
Regulatory Clock Preview still showing a pre-Omnibus AI Act lane after the
canonical graph and `/clock/` had been corrected — a consistency failure, not a
legal-research failure.

## 2. Rule

A surface that displays Evidence Graph dates MUST either:

1. **Derive** from the canonical claim graph (preferred — machine or explicit
   citation to claim IDs / `claims.json`), **or**
2. Be **registered here** as a derivative surface with a named consistency
   check against the canonical parent.

Unregistered manual copies of regulatory timelines are prohibited.

## 3. Registry

| Surface ID | Path | Kind | Canonical parent | Facts mirrored | Consistency check | Status |
|---|---|---|---|---|---|---|
| DS-HOME-CLOCK-PREVIEW | `/` (`index.html` Regulatory Clock Preview) | Manual HTML lane preview | `/regulation/eu-ai-act/claims.json` (AI Act lane); `/clock/` for full multi-regulation clock | AI Act phase markers 2024–2028; Data Act markers on same axis | Before any claim-date change ships: homepage AI Act markers match canonical effective dates (no `Art. 113.4` / Aug 2027 framing; Dec 2027 Annex III; Aug 2028 Annex I; Feb 2025 / Aug 2026 qualifications; Article 5 exception 2 Dec 2026 mentioned) | Active — corrected 2026-08-20 hotfix |
| DS-CLOCK-PAGE | `/clock/` | Full Regulatory Entry Clock | `/regulation/eu-ai-act/claims.json` (AI Act lane) | AI Act lane + established-date list | Publish-gate / release checks already require `/clock/` ↔ claims agreement | Active |

## 4. Change procedure

1. Change the canonical claim first (or reject the change).
2. Update every registered derivative that mirrors the affected facts in the
   **same** PR, or open a blocking follow-up before merge to `main`.
3. Record the surface in this registry before first publication if it is new.

## 5. Prohibited

| Prohibited | Reason |
|---|---|
| A second hand-maintained AI Act timeline not listed here | Reproduces homepage drift |
| Shipping a claim effective-date change without checking registered derivatives | Leaves a public surface lying |
| Treating a preview lane as authoritative over `claims.json` | Inverts the graph |

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
