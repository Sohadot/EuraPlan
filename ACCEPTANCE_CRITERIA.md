# ACCEPTANCE_CRITERIA.md
**Version:** 1.1
**Status:** Active — Governing Document
**Asset:** EuraPlan.com
**Last Updated:** June 2026

---

## 1. Purpose

This document defines the pass/fail criteria for every future addition to EuraPlan.com. Nothing is published without passing the relevant criteria set.

---

## 2. Page Acceptance Criteria

Every public page must satisfy all of the following:

| Criterion | Requirement |
|---|---|
| Route ID | Assigned and registered in routes.json |
| Page Thesis | One clear sentence defining the intelligence or doctrine this page exists to deliver |
| Ontology Class or Doctrine Purpose | Defined — which EuraPlan ontology entity or planning doctrine does this page serve? |
| Target Audience | Explicitly identified — which non-EU company profile is this for? |
| Decision Problem | One clear problem the target audience faces that this page addresses |
| Produced Intelligence Output | What does the user know, understand, or have access to after reading this page? |
| Official Sources | Where regulatory, compliance, or funding claims are made: Tier 1 source cited inline |
| Last Updated Date | Present in the page — not optional |
| Canonical URL | Confirmed and registered |
| Internal Links | Minimum two outward links to related governed routes; minimum one inbound link from existing route |
| Source Confidence Classification | Assigned per SOURCE_POLICY.md |
| Claim Risk Classification | Assigned per CLAIM_POLICY.md |
| Disclaimer | Planning intelligence disclaimer present where regulatory or compliance content exists |
| No Legal Advice | No language framing that implies legal advice or guaranteed compliance outcomes |
| No Unsupported Partnership Claims | No claim of official relationship with EU institutions or third parties without formal agreement |
| No Thin Content | No section exists purely as a placeholder or to fill space |
| No Placeholder Sections | No "coming soon," "to be added," or "check back later" copy |

**Any page that fails one or more criteria must not be published.**

---

## 3. Route Acceptance Criteria

Every route must satisfy all of the following before being added to routes.json with `publication_status: published`:

- route_id assigned
- path confirmed as non-combinatorial
- title defined
- purpose documented
- ontology_role or doctrine_role defined
- indexable status confirmed
- sitemap status confirmed
- required_internal_links identified
- source_requirement assessed
- content_status confirmed as ready

---

## 4. Brief Acceptance Criteria

A `/brief/...` route may only be created when:

- Confirmed real demand exists (not speculative)
- The brief adds intelligence not available in the reference layer
- Full Tier 1 sourcing is available for all regulatory claims
- The brief has a defined buyer profile
- The brief has a defined monetisation mechanism
- All standard page acceptance criteria are met

---

## 5. Diagnostic Output Acceptance Criteria

A diagnostic output (Phase 3+) may only be activated when:

- The EuraPlan Entry Planning Protocol is fully implemented in the engine
- All EERS dimensions are scored using defined, governed criteria
- All regulatory exposure mappings are Tier 1 sourced
- Output includes the planning intelligence disclaimer
- Output does not claim to constitute legal advice
- Diagnostic query states do not appear in sitemap.xml
- Diagnostic query states are disallowed in robots.txt

---

## 6. Claim Acceptance Criteria

A public claim may be published when:

- It is classified under CLAIM_POLICY.md and is not Blocked
- If High risk: Tier 1 source is cited inline
- If Medium risk: Tier 2 or Tier 3 source is cited
- If Low risk: no unsupported factual assertions are present
- Appropriate disclaimer is included where required

---

## 7. Source Acceptance Criteria

A source may be used when:

- It meets the tier requirements in SOURCE_POLICY.md for the claim type it supports
- It is named, dated, and linked to the official publication
- It is not classified as Deprecated
- It has not been superseded by a newer official version

---

## 8. Monetisation Unit Acceptance Criteria

A monetisation channel or product may be activated when:

- It is listed in the Permitted Channels of MONETIZATION_BOUNDARY.md
- It does not require thin content, unsupported claims, or unvetted referrals
- Owner approval is confirmed
- The intelligence output it is attached to is published and governed

---

## 9. Interface Component Acceptance Criteria

An interface component may be added when:

- It embodies the planning intelligence doctrine — it does not merely decorate the site
- It does not hide core content from search engines (no canvas-only or JS-gate-only content)
- It does not require external UI frameworks not already in the build system
- It is static-first or progressively enhanced
- It does not implement WebGL, 3D, or animation-first interaction in Phase 1

---

## 10. Operating Policy Compliance

Every page published from Sprint 2 onwards must be verified against all relevant Companion Operating Documents listed in GOVERNANCE_CHARTER.md Section 5. Failure of any applicable policy blocks publication.

| Policy | Applies To |
|---|---|
| TECHNICAL_STANDARD.md | All pages |
| SEO_GOVERNANCE.md | All indexable pages |
| CONTENT_QUALITY_STANDARD.md | All content pages |
| ACCESSIBILITY_STANDARD.md | All pages |
| PERFORMANCE_BUDGET.md | All pages |
| STRUCTURED_DATA_POLICY.md | All pages |
| PAGE_BLUEPRINT_STANDARD.md | All reference, brief, and matrix pages |
| VISUAL_SYSTEM_GOVERNANCE.md | All pages |
| AGENT_READABILITY_POLICY.md | All pages |
| SCALING_AND_AUTOMATION_POLICY.md | Any page produced with automation assistance |

The publication gate checklist in SCALING_AND_AUTOMATION_POLICY.md must be completed for every page before publication_status is changed to `published` in routes.json.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
