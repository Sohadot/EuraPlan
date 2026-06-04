# SCALING_AND_AUTOMATION_POLICY.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, REFERENCE_CORPUS_GOVERNANCE.md, CONTENT_QUALITY_STANDARD.md

---

## 1. Automation Doctrine

Automation may assist EuraPlan expansion. It may never govern it.

The governed quality of EuraPlan's reference corpus is its primary competitive asset. Any automation that bypasses the governance layer — producing pages that skip source review, claim review, blueprint compliance, or route registry approval — does not accelerate EuraPlan. It destroys it.

The governing question for any automation proposal: does this maintain the governance standard, or does it route around it?

---

## 2. Permitted Automation Uses

| Use | Condition |
|---|---|
| Blueprint-driven page drafting | Produces a draft against the PAGE_BLUEPRINT_STANDARD.md template; requires human review before publication |
| Route registry validation | Checks that all HTML pages have a routes.json entry; checks that published pages are not orphaned |
| Sitemap generation | Generates sitemap.xml from routes.json entries with `sitemap: true` and `publication_status: published` |
| Internal link validation | Checks all internal links resolve and that no page is an orphan |
| Source citation format validation | Checks that citation format matches SOURCE_POLICY.md standards |
| Structured data validation | Validates JSON-LD blocks against schema.org before deployment |
| Duplicate intent detection | Flags pairs of pages with very similar titles or descriptions for human review |
| Performance audit | Runs Lighthouse or equivalent on new pages before publication |
| Accessibility audit | Runs axe-core or equivalent on new pages before publication |
| Translation drafting | Produces a machine translation draft; requires full human review per MULTILINGUAL_GOVERNANCE.md before publication |

---

## 3. Prohibited Automation Uses

| Prohibited | Reason |
|---|---|
| Auto-publishing pages to the live site without per-page human review | Bypasses governance layer — permanently prohibited |
| Generating pages from a list of keywords without a content brief | Produces thin, off-category content |
| Bulk creation of combinatorial URL pages | Prohibited by ROUTE_GOVERNANCE.md |
| Auto-generating source citations from AI-produced text | AI-generated citations are not Tier 1 sources |
| Applying claim risk or source confidence classifications without human verification | Classifications affect publication decisions and cannot be automated |
| Auto-approving routes in routes.json without route governance review | Routes.json is a governance document, not a config file |
| Auto-translating and auto-publishing multilingual pages | Violates MULTILINGUAL_GOVERNANCE.md |

---

## 4. Human Review Requirements

The following must always involve human review before any asset reaches `publication_status: published`:

- Content brief approval (decision to create the page)
- Source capture and Tier 1 verification for regulatory and compliance claims
- Claim risk classification review
- Page thesis and decision problem review
- Internal link sufficiency check
- Blueprint compliance review
- Disclaimer presence and adequacy review

No automation system may mark a page as published. That status change must be made by a human reviewer with this policy document in hand.

---

## 5. Blueprint-Driven Generation

When automation is used to draft page content, it must operate from the PAGE_BLUEPRINT_STANDARD.md blueprint for the relevant page type.

Blueprint-driven generation means:
- The system receives the page type, target regulation/country/sector/origin, and source list as input
- The system produces a structured draft with all required blueprint sections populated
- The draft is flagged as DRAFT throughout until human review is complete
- The draft is not committed to the main branch until all governance criteria are satisfied

---

## 6. Route Registry Enforcement

Automation may validate the route registry but may not modify it without human instruction.

**Automated checks:**
- Every HTML file in a route directory has a corresponding routes.json entry
- Every routes.json entry with `publication_status: published` has a corresponding HTML file
- No routes.json entry is missing required fields
- Sitemap entries match routes.json published routes exactly

**Human-only actions:**
- Adding a new route entry
- Changing `publication_status` to `published`
- Changing `indexable` or `sitemap` values
- Deprecating a route

---

## 7. Source Registry Enforcement

When the corpus grows beyond 20 published pages, a source registry file must be created: `SOURCE_REGISTRY.md`.

The source registry records all sources cited across the corpus, with:
- Source name and type
- URL
- Date last verified
- Pages that cite this source
- Current status (Active / Deprecated)

Automation may maintain and query the source registry. Human review is required when a source is flagged as deprecated or removed.

---

## 8. Duplicate Intent Detection

Before a new route is approved, check the existing corpus for pages with:
- Identical or near-identical `<title>` or meta description
- The same primary regulatory subject with the same audience framing
- Overlapping decision problems

If a near-duplicate is detected, the proposed page must be differentiated or the existing page updated before the new route is approved.

---

## 9. Page Status Lifecycle Enforcement

Automation may:
- Detect pages that have been in `status: draft` for > 30 days and flag for review
- Detect pages that have not been updated within their review cycle and flag for content review
- Detect broken internal links and flag for resolution

Automation may not:
- Remove pages
- Change page status
- Modify content

---

## 10. Commit Discipline

Every content commit must include a commit message that identifies:
- What was changed (page created, page updated, governance document revised)
- Why (new route addition, source update, enforcement date passed, sprint wave)
- What governance document authorised the change (sprint document, route approval, quality gate passed)

Example: `sprint 1 wave 1: publish /regulation/eu-ai-act/ — source review complete, all acceptance criteria met`

Bulk commits that contain dozens of page changes without individual justification are a governance failure.

---

## 11. Publication Gates Summary

A page may be pushed to `publication_status: published` only when all of the following pass:

1. ACCEPTANCE_CRITERIA.md — all criteria met
2. SOURCE_POLICY.md — all claims verified or referenced
3. CONTENT_QUALITY_STANDARD.md — all required elements present
4. SEO_GOVERNANCE.md — all technical SEO requirements met
5. ACCESSIBILITY_STANDARD.md — no critical failures
6. PERFORMANCE_BUDGET.md — no critical violations
7. PAGE_BLUEPRINT_STANDARD.md — blueprint followed for page type
8. STRUCTURED_DATA_POLICY.md — JSON-LD validated
9. Internal link check — at least two outbound, at least one inbound
10. Sitemap updated and validated

---

## 12. Rollback Rules

If a published page is found to contain a governance violation after publication:

1. Add `<meta name="robots" content="noindex">` immediately
2. Remove from sitemap.xml immediately
3. Fix the violation before re-adding to sitemap
4. If the violation is a false regulatory claim: remove or correct the claim and verify the correction with the source before re-publishing
5. Document the violation and resolution in the commit history

Do not leave a page live with a known governance violation while a fix is in progress, unless removing it would cause greater harm (e.g., widely linked regulatory reference with a minor labelling issue vs. a material false claim).

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
