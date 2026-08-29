# AGENT_READABILITY_AND_MACHINE_TRUST_AUDIT.md
**Version:** 1.0
**Status:** Active — Internal Governance / Audit
**Asset:** EuraPlan.com
**Owner:** Sohadot
**Created:** Sprint 5C — August 2026
**Last Updated:** August 2026 (Sprint 5C)
**Governed by:** GOVERNANCE_CHARTER.md, AGENT_READABILITY_POLICY.md, SOURCE_POLICY.md, CLAIM_POLICY.md, ROUTE_GOVERNANCE.md, STRUCTURED_DATA_POLICY.md, SECURITY_POLICY.md
**Decision reference:** DEC-058 (DECISION_LOG.md)

> This is an **internal governance / audit document**. It is **not** a public page.
> It is **not** listed in `sitemap.xml`, it is **not** linked from public navigation,
> and it makes no public claims. It records the state of EuraPlan's machine
> readability and AI-agent trust posture at the close of Sprint 5C.

---

## 1. Title and status

**EuraPlan.com — Agent Readability & Machine Trust Audit (Sprint 5C).**

**Status:** Active. This audit was performed as a **trust-hardening review**, not a
corpus-expansion sprint. No new public pages, routes, regulation/country/sector/funding
references, `/matrix/`, `/brief/`, diagnostic functionality, or combinatorial URLs were
created. No trackers, forms, cookies, external scripts, canvas, WebGL, or 3D were added.

Sprint 5C follows the completion of:

- Security runtime verification (DEC-040, DEC-041; `SECURITY_POLICY.md` §8)
- Structured data completion (DEC-042; `STRUCTURED_DATA_COVERAGE_AUDIT.md`)
- Provenance / authenticity layer (DEC-043; `PROVENANCE.md`, `AUTHENTICITY_CERTIFICATE.md`, `CHAIN_OF_CUSTODY.md`, `ASSET_TRANSFER_MANIFEST.md`)
- Funding layer integration review (DEC-044; `FUNDING_LAYER_INTEGRATION_REVIEW.md`)
- GDPR Evidence Graph publication and R2.8 closure (DEC-045, DEC-054, DEC-055, DEC-056, DEC-057)

---

## 2. Purpose

To make it easier for **AI agents, search systems, reviewers, and future buyers** to
understand, without ambiguity:

- how EuraPlan should be read;
- what it claims and — as importantly — what it does **not** claim;
- how its route system works (ontology roles);
- how source confidence works (tiers and confidence classification);
- how claim risk works (Low / Medium / High / Blocked, plus "requires mapping" states);
- why the site must be treated as **planning intelligence**, not legal, tax, compliance,
  funding, grant-writing, incorporation, or investment advice, and not an official EU source.

The audit verifies that these signals are present, machine-extractable, mutually
consistent, and cautious, and records the minimal fixes applied where clarity was missing.

---

## 3. Scope

**In scope (reviewed):**

Governance / policy layer — `AGENT_READABILITY_POLICY.md`, `STRUCTURED_DATA_POLICY.md`,
`CLAIM_POLICY.md`, `SOURCE_POLICY.md`, `ROUTE_GOVERNANCE.md`, `DECISION_LOG.md`,
`SECURITY_POLICY.md`, `PROVENANCE.md`, `AUTHENTICITY_CERTIFICATE.md`,
`CHAIN_OF_CUSTODY.md`, `ASSET_TRANSFER_MANIFEST.md`.

Machine-control layer — `routes.json`, `sitemap.xml`, `robots.txt`, `llms.txt`.

Public surface — `index.html`, `enter/index.html`, `clock/index.html`,
`standard/eers/index.html`, `protocol/index.html`, `sources/index.html`,
`governance/index.html`, `acquire/index.html`, `funding/horizon-europe/index.html`,
`sector/ai-saas/index.html`, and the four regulation references
(`regulation/eu-ai-act/`, `regulation/gdpr/`, `regulation/eu-data-act/`,
`regulation/cyber-resilience-act/`) and three country references
(`country/germany/`, `country/netherlands/`, `country/france/`).

**Out of scope (explicitly not changed):** Cloudflare edge configuration, security headers,
source-tier structure, claim-risk taxonomy, corpus content, interface system, and any new
route type. This sprint touches documentation and one concise public governance section only.

---

## 4. Current agent-readable trust signals

EuraPlan already exposes a coherent machine-trust layer. Confirmed present:

| Signal | Location | State |
|---|---|---|
| Agent-readability doctrine | `AGENT_READABILITY_POLICY.md` | Active — stable URLs, `<h1>` outline, lead summary, HTML tables, visible source lists, no hidden intelligence |
| Machine-readable site brief | `llms.txt` | Present — states "planning intelligence, not legal advice"; explicit "Notes for automated agents"; declares EuraPlan is "not a government body or an official EU source" |
| Route registry | `routes.json` | Present — every route carries `route_id`, `ontology_role`/`doctrine_role`, `indexable`, `sitemap`, `source_requirement`, `publication_status` |
| Canonical claim graphs | `regulation/eu-ai-act/claims.json`, `regulation/gdpr/claims.json` | Published, `indexable:false`, `sitemap:false`, declared in `llms.txt` with "implies no external endorsement" |
| Source confidence badges | `sources/index.html` + reference pages | Text-readable (e.g. "Tier 1 — Primary Authoritative", "Verified", "Pending"), not colour-only |
| Claim-risk badges | governance + reference pages | Text-readable (e.g. "Claim risk: Low — architecture description") |
| Readiness state labels | reference pages | "Relevant — requires mapping" / "Unassessed" — cautious, no fabricated EERS scores |
| Advice-boundary blocks | every reference page | "What EuraPlan does NOT provide" tension lists (legal advice, certification, guaranteed compliance outcomes, etc.) |
| Mandatory disclaimers | `CLAIM_POLICY.md` §4 + page footers | Planning-intelligence, regulatory-change, and funding disclaimers |
| Structured data | all pages | JSON-LD `WebPage`/`Article` + `BreadcrumbList` per `STRUCTURED_DATA_POLICY.md` |

**Fix applied this sprint:** a concise **"How AI Agents Should Read EuraPlan"** section was
added to `governance/index.html` to consolidate these signals into one agent-facing statement
on an existing public governance surface (no new page created).

---

## 5. Route ontology audit

`routes.json` (v1.0, `last_updated: 2026-08-23`, governed by `ROUTE_GOVERNANCE.md`) registers
19 routes with clear, consistently described roles. Ontology is expressed through two fields:
`ontology_role` (functional role in the intelligence architecture) and `doctrine_role`
(governance/meta pages). Route types observed:

| Route class | Ontology signal | Examples | Status |
|---|---|---|---|
| Core reference / thesis | descriptive `ontology_role` | `/` (category thesis), `/enter/`, `/clock/`, `/standard/eers/`, `/protocol/` | published |
| Regulation references | `ontology_role: "regulation_reference"` | `/regulation/eu-ai-act/`, `/regulation/gdpr/`, `/regulation/eu-data-act/`, `/regulation/cyber-resilience-act/` | published |
| Country references | `ontology_role: "country_reference"` | `/country/germany/`, `/country/netherlands/`, `/country/france/` | published |
| Sector references | `ontology_role: "sector_reference"` | `/sector/ai-saas/` | published |
| Funding references | `ontology_role: "funding_reference"` | `/funding/horizon-europe/` | published |
| Governance / doctrine | `doctrine_role` set, `ontology_role: null` | `/sources/`, `/governance/` | published |
| Acquisition / readiness | `doctrine_role` set | `/acquire/` | published |
| Deferred diagnostic / matrix | `ontology_role` set, `publication_status: draft`/`planned` | `/matrix/country-sector-regulation/` (`indexable:false`, `sitemap:false`), `/diagnostic` (`sitemap:false`) | not published |

**Finding:** Route ontology is clear and consistent for all key route types, including the
deferred diagnostic/matrix routes, which correctly carry non-published status and are excluded
from `sitemap.xml`. **No defect.** No new route type was required, so none was created.

---

## 6. Source confidence audit

Governed by `SOURCE_POLICY.md` and surfaced publicly at `/sources/`.

**Governed model (authoritative):** a **three-tier** source system —
Tier 1 Primary Authoritative (official EU legislation/EUR-Lex, Commission/Parliament/Council,
EU agency guidance, **and official national government sources folded into Tier 1**),
Tier 2 Institutional Reference (EEN, EIB, EIF, OECD, IMF, World Bank), Tier 3 Professional
Reference (named/dated law-firm, Big Four, industry-association material) — plus an explicit
**Rejected** class (anonymous content, AI-generated summaries, Wikipedia, undated marketing,
social media). Confidence classification: **Verified / Referenced / Pending / Deprecated**,
with "Pending" barred from publication and "Deprecated" fixed within 30 days.

**Readability check:** on `/sources/` every tier and confidence level is rendered as a
text-labelled badge and a full `<table>` with `<thead>`/`<th scope>` — readable without CSS
and not colour-dependent. `SRC-CTRL-01` panel ("Why Tier 1 Matters") states the posture in
plain language for both humans and agents.

**Note for reviewers:** the Sprint 5C brief referenced a four-tier framing
(Tier 1 official / Tier 2 national official / Tier 3 institutional / Tier 4 secondary).
The **governed and implemented reality is three tiers** (national official is inside Tier 1).
This audit documents the real system; the source taxonomy was **not** restructured, as doing so
would be a governance change beyond this trust-hardening sprint and no defect requires it.

**Finding:** Source confidence is readable and clearly explained. **No defect; no change.**

---

## 7. Claim risk audit

Governed by `CLAIM_POLICY.md` §6. The taxonomy is:

| Risk level | Meaning | Requirement |
|---|---|---|
| **Low** | General category/orientation; bibliographic instrument identity | No external source required |
| **Medium** | Sector / country / strategy framing (interpretation) | Tier 2 or Tier 3 source |
| **High** | Regulatory deadline, compliance requirement, funding eligibility, legal-effect/amendment/repeal | Tier 1 source required |
| **Blocked** | Legal conclusion or implied legal advice | Not permitted — rephrase or remove |

In addition, reference pages express a **planning-implication caution state** through readiness
labels: **"Relevant — requires mapping"** and **"Unassessed"**, meaning no automatic conclusion
or company-specific score is asserted.

**Readability check:** claim-risk badges are text-labelled ("Claim risk: Low — architecture
description", "High risk without Tier 1"). "Requires mapping" / "Unassessed" appear as literal
text states on reference pages and the homepage ("dimensions unassessed until protocol run").
Language is precise and **not alarmist**.

**Finding:** Claim-risk language distinguishes low-risk factual reference, medium-risk
interpretation, high-risk planning implication, and unassessed/requires-mapping states, and is
readable. **No defect; no change.**

---

## 8. Advice-boundary audit

EuraPlan must consistently frame itself as **planning intelligence**, never as legal, tax,
compliance, funding, grant-writing, incorporation, investment advice, eligibility
determination, or official representation.

**Evidence gathered (repository-wide scan of public HTML):**

- Every regulation and sector reference page carries an explicit **"What EuraPlan does NOT
  provide"** block naming legal advice, legal representation, certification/conformity
  assessment, notified-body services, "guaranteed compliance outcomes", final applicability
  determination, and "not a substitute for qualified … counsel".
- `funding/horizon-europe/` route purpose states "Planning intelligence, not funding advice."
- `CLAIM_POLICY.md` §3 prohibits "You are compliant if…", "EuraPlan guarantees entry success",
  "Official partner of …", etc.; §4 mandates the planning-intelligence, regulatory-change, and
  funding disclaimers.
- `llms.txt`, `PROVENANCE.md`, and `AUTHENTICITY_CERTIFICATE.md` all restate: not an EU
  institution, no endorsement, planning intelligence only.
- The token "guarantee" appears in public HTML only inside **verbatim official legal text**
  (GDPR Art. 28 quotes) or inside **negative disclaimers** ("guaranteed compliance outcomes"
  as a prohibited output). No page asserts a guarantee, endorsement, certification, or
  eligibility determination on EuraPlan's own behalf.

**Finding:** Advice-boundary framing is consistent and safe. **No risky wording found; no
change required.** Legitimate disclaimers were preserved.

---

## 9. Structured data audit summary

Governed by `STRUCTURED_DATA_POLICY.md`; prior completion recorded in DEC-042 and
`STRUCTURED_DATA_COVERAGE_AUDIT.md`.

- Core governance/source pages use `WebPage` + `BreadcrumbList`; reference pages use
  `Article` + `BreadcrumbList` — matching the approved schema-by-page-type table.
- `dateModified` is present and must match the visible "Last Updated" date (policy §6/§11).
- Prohibited schema (`AggregateRating`, `Review`, `Certification`, `GovernmentOrganization`,
  `sameAs` to EU institutions, unfounded `FAQPage`) — none observed.

**Change this sprint:** on `governance/index.html`, because a public section was added, the
JSON-LD `dateModified` and the visible "Last Updated" were advanced **together** (2026-06-04 →
2026-08-29) to keep them aligned per policy §6. **No new schema type was added.**

**Finding:** Structured data remains valid and policy-aligned.

---

## 10. Security runtime proof summary

Governed by `SECURITY_POLICY.md` §8; decisions DEC-040 (repository `_headers` artifact) and
DEC-041 (production runtime verification).

- Runtime enforcement is a **Cloudflare Response Header Transform Rule — "EuraPlan Security
  Headers"**, verified Sprint 4E-RC1 by live `curl -I` capture. Headers: CSP (self-only
  baseline, `'unsafe-inline'` retained for inline JSON-LD/layout styles), `X-Content-Type-Options:
  nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: strict-origin-when-cross-origin`,
  `Permissions-Policy` (camera/mic/geo/etc. disabled), HSTS `max-age=31536000; includeSubDomains`.
- Repository `_headers` is documented as **Cloudflare Pages-compatible config, not proven sole
  runtime mechanism** while GitHub Pages/Fastly remains behind Cloudflare — correctly caveated.
- A `secret-scan` GitHub Action (Gitleaks, full history, SHA-pinned) plus the PR public-disclosure
  attestation form the two-gate secret boundary (`SECURITY_POLICY.md` §11).

**Finding:** Security runtime proof is correctly recorded. **Per sprint scope, no Cloudflare
settings and no headers were changed.** No defect found.

---

## 11. Provenance / authenticity proof summary

Governed by the Sprint 4G acquisition-readiness layer:

- `PROVENANCE.md` — origin, category identity, thesis, route corpus map, decision-log
  relationship, security/structured-data closure notes, current limitations, provenance statement.
- `AUTHENTICITY_CERTIFICATE.md` — repository authenticity posture, covered materials,
  representative (non-invented) commit anchors, explicit non-claims (no notarization, no EU
  endorsement, no valuation, no traffic/revenue/ranking guarantees).
- `CHAIN_OF_CUSTODY.md`, `ASSET_TRANSFER_MANIFEST.md`, `RIGHTS_AND_USAGE_NOTICE.md` — custody,
  transfer checklist, and rights posture.

**Observation (staleness, not a defect):** the provenance layer is dated June 2026 (Sprint 4G)
and its route-corpus and decision snapshots predate DEC-044 (funding), DEC-045/054–057 (GDPR
Evidence Graph / R2.8), and this Sprint 5C. The records remain **accurate as historical
snapshots** and correctly point reviewers to `DECISION_LOG.md` as the live audit trail.

**Decision this sprint:** provenance files were **not** rewritten. They contain specific commit
hashes and dated closures that must not be fabricated or silently advanced; the machine-trust
status and the funding/GDPR progression are instead recorded here and in DEC-058, which is the
governed, additive way to update the audit trail. Refreshing `PROVENANCE.md`'s corpus snapshot
is listed as a recommendation (§15).

---

## 12. Sitemap / robots / route registry alignment

Cross-checked `routes.json` ↔ `sitemap.xml` ↔ `robots.txt`:

- **Sitemap (17 URLs)** = exactly the `routes.json` entries with `sitemap: true` and
  `publication_status: published` (8 core + 4 regulation + 3 country + 1 sector + 1 funding).
- **robots.txt** allows those public route roots and `/assets/`; disallows `/diagnostic?`,
  `/draft/`, `/brief/`, `/evidence-workbench/`, `/matrix/` — consistent with their
  non-published registry status.
- **claims.json** graphs are `indexable:false` / `sitemap:false` and are correctly absent from
  `sitemap.xml`, while being discoverable via `llms.txt` for agents.
- `robots.txt` `Sitemap:` directive points to `https://euraplan.com/sitemap.xml`.

**Finding:** Registry, sitemap, and robots are aligned. **No defect. No sitemap, robots, or
routes.json change was required, so none was made.**

---

## 13. Public-page machine readability gaps

Assessed against `AGENT_READABILITY_POLICY.md`:

- Single `<h1>` thesis, `<h2>`/`<h3>` outline, lead summary, HTML tables with `<th scope>`,
  visible end-of-page source lists, descriptive internal-link anchors, no JS-hidden
  intelligence — all satisfied on the reviewed pages.
- Regulatory claims, readiness states, and cross-reference tables are present in HTML source
  (confirmed by `llms.txt` "Notes for automated agents" and direct inspection).

**One consolidation gap identified:** the trust signals above were distributed across pages and
documents, with **no single, concise, agent-directed statement** telling an automated reader
how to interpret EuraPlan as a whole (planning-intelligence status, ontology roles, source
tiers, claim-risk caution, "requires mapping" meaning, prefer-official-sources instruction).

---

## 14. Fixes applied

Minimal, in scope:

1. **`AGENT_READABILITY_AND_MACHINE_TRUST_AUDIT.md`** (this file) — created as the internal
   Sprint 5C audit record. Not in sitemap; not linked from public navigation.
2. **`governance/index.html`** — added a concise **"How AI Agents Should Read EuraPlan"**
   section on the existing governance surface (no new public page). It states: EuraPlan is a
   planning-intelligence reference system; not an official EU institution; provides no legal,
   tax, compliance, funding, grant-writing, incorporation, or investment advice; route pages are
   governed by ontology role; sources are classified by confidence tier; claim-risk labels
   indicate interpretation caution; "requires mapping" means no automatic conclusion; agents
   should prefer official sources for primary legal/programme facts and use EuraPlan as a
   structured planning layer. The page's JSON-LD `dateModified` and visible "Last Updated" were
   advanced together to stay aligned. No redesign, no interface change, no hype, no agent-
   endorsement claim.
3. **`DECISION_LOG.md`** — added **DEC-058** recording Sprint 5C, and advanced the header
   "Last Updated" line.

No other file was modified. No corpus, sitemap, robots, routes.json, security, or provenance
file was changed.

---

## 15. Remaining limitations

- **Provenance snapshot staleness** — `PROVENANCE.md` / `AUTHENTICITY_CERTIFICATE.md` corpus and
  decision snapshots predate DEC-044/045/054–058. Recommend a dedicated, carefully sourced
  provenance refresh (with real commit anchors) in a future acquisition-readiness pass.
- **Source-tier framing mismatch** — external briefs may describe a four-tier model; the
  governed reality is three tiers (national official inside Tier 1). Any future move to a
  four-tier model must go through `SOURCE_POLICY.md` and a DEC, not an ad-hoc edit.
- **No machine-trust endpoint** — agent guidance is currently HTML + `llms.txt` only; a
  structured agent-trust manifest (e.g. a `/.well-known/` descriptor or `trust.json`) is a
  Phase 4 candidate, not implemented here.
- **Security scope** — runtime headers proven at the Cloudflare edge only; `_headers` remains
  unverified as sole mechanism. Unchanged by design this sprint.
- **CSP strictness** — `'unsafe-inline'` retained for inline JSON-LD/layout; hash-based CSP
  hardening remains deferred (per DEC-042 / `SECURITY_POLICY.md` §8).

---

## 16. Final sign-off

Sprint 5C is a **trust-hardening documentation sprint**. Verified before sign-off:

- [x] No new public pages, corpus routes, `/matrix/`, `/brief/`, diagnostic, or combinatorial URLs created
- [x] No sitemap, robots, or route-registry change (none required; none made)
- [x] No external scripts, trackers, forms, cookies, canvas, WebGL, or 3D added
- [x] No legal / funding / grant-writing advice framing, endorsement, eligibility, or valuation claims added
- [x] Source-confidence language readable (text badges + tables, not colour-only)
- [x] Claim-risk language readable and non-alarmist; "requires mapping" remains cautious
- [x] Structured data remains valid; `dateModified` kept aligned with visible "Last Updated"
- [x] Security runtime proof remains documented and unchanged
- [x] Provenance documents remain internally consistent (staleness recorded, not falsified)
- [x] Internal links on the edited page still resolve

**Sign-off:** Sprint 5C — Agent Readability & Machine Trust Hardening: **COMPLETE / PASS.**

---

## 17. Recommendation for next sprint

Trust hardening is complete and requires no follow-up. The two candidate expansion sprints are:

- **Sprint 6A — Second Sector Reference: Cloud / Data Infrastructure**
  (a second `sector_reference` sibling to `/sector/ai-saas/`), or
- **Sprint 6B — Second Funding Reference: EIC / Digital Europe / ERDF**
  (a second `funding_reference` sibling to `/funding/horizon-europe/`).

**Governance gate — read before either is opened.** The active decision log currently
**prohibits corpus expansion**. DEC-047 (Wave 1 Depth Equalization), reaffirmed by DEC-057,
holds that **no new country, sector, funding, brief, matrix, or regulation route** may be added
beyond the Wave 1 set **until every Wave 1 Core Authority route scores ≥ 90 (RGS v2)**. As of
DEC-057 the scores are: EU AI Act 97, GDPR 97.5 (both ≥ 90); **EU Data Act 58, CRA 60, EERS 62,
Protocol 60 — all below threshold**. The active mandate is *repetition of quality*
(Data Act → CRA → EERS → Protocol upgrades), **not** expansion.

Therefore Sprint 6A / 6B cannot begin under current governance. The correct sequence is either
(a) complete the Wave 1 equalization upgrades (Sprint R3 onward) until all four remaining routes
reach ≥ 90, after which 6A/6B open normally under a new DEC; or (b) adopt a superseding DEC that
consciously lifts or amends the DEC-047/DEC-057 no-expansion gate. Whichever expansion sprint is
eventually chosen must follow the sovereign single-page reference pattern (Tier 1 sourcing, no
combinatorial URLs, JSON-LD `Article` + `BreadcrumbList`, advice-boundary block, "requires
mapping" readiness states) and be admitted through `routes.json` + `sitemap.xml` under its own
DEC. A provenance-snapshot refresh (§15) may be folded into that sprint.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
*Governed by Sohadot | Internal — not in sitemap | Sprint 5C — August 2026*
