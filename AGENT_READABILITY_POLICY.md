# AGENT_READABILITY_POLICY.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, TECHNICAL_STANDARD.md, SEO_GOVERNANCE.md

---

## 1. Why Agent Readability Is a Category Claim

EuraPlan's future value includes being the reference intelligence layer for AI agents researching EU regulatory entry questions on behalf of non-EU companies, advisors, investors, and institutions. An AI agent querying "what EU regulations apply to a US SaaS company entering Germany?" must find EuraPlan's reference pages as authoritative, structured, complete, and directly extractable sources.

Agent readability is not a secondary concern. It is part of the category claim. A Category Intelligence Factory that is opaque to the agents that are increasingly mediating access to reference information is not occupying its category.

---

## 2. Stable URL Requirements

- All URLs follow the route registry in `routes.json` and do not change without a documented reason
- A route change requires a 301 redirect from the old URL before the change is deployed
- URL slugs are descriptive, permanent, and intention-expressing: `/regulation/eu-ai-act/` not `/reg/p123/`
- No page moves without updating `routes.json`, `sitemap.xml`, and all internal links simultaneously

---

## 3. Heading Hierarchy as Extractable Outline

- One `<h1>` per page containing the page thesis
- `<h2>` for major sections — each `<h2>` is a meaningful section of the intelligence output
- `<h3>` for subsections within major sections
- No skipped levels, no decorative headings
- The heading tree must be readable as a meaningful outline of the page's intelligence structure

---

## 4. Lead Summary Requirement

Every reference page must open with a concise lead summary (2–4 sentences) in the first paragraph of `<main>` that:

- States what the page covers
- States why it matters for non-EU company entry planning
- States who it is primarily for

This summary must be machine-extractable as the page's primary intelligence claim. It appears before any navigation elements within `<main>`.

---

## 5. HTML Tables for Cross-Reference Data

- All matrix and cross-reference data uses `<table>` with `<thead>`, `<tbody>`, `<caption>`, and `<th scope>` attributes
- A table read without CSS must still convey the cross-reference relationships as plain text
- Not a CSS grid that visually resembles a table but is structured as divs
- Table cells for regulatory obligations must contain text, not only icons or color signals

---

## 6. Visible Source Lists

- All source citations appear in the visible HTML source, not loaded asynchronously
- Source list format:
  `[Source name] — [Publication type] — [Date] — [URL]`
- Source lists appear in a dedicated `<section>` or `<aside>` element at the end of the page content
- Each source is individually linked where an official URL is available
- No source appears only in a tooltip, hover state, or JavaScript-activated panel

---

## 7. Internal Link Context

- All internal links use descriptive anchor text matching the destination page's thesis or section
- The surrounding sentence must make the relationship between source and destination intelligible to a reading agent
- No bare URL anchors, no "click here," no "read more" without the subject
- Example: `—Understand how GDPR applies through the <a href="/standard/eers/">European Entry Readiness Standard</a> Regulatory Mapping dimension—`

---

## 8. No Hidden Intelligence

- All regulatory claims, compliance obligations, funding eligibility criteria, and deadline data must appear in HTML source
- No intelligence is delivered only through JavaScript-rendered content
- No page uses canvas, SVG-only, or image-only representation for substantive planning data
- No regulatory clock data, matrix cell content, or EERS dimension descriptions hidden behind a JS interaction

---

## 9. No Ambiguous Route Combinations

- Every URL is unambiguous: `/regulation/eu-ai-act/` is the EU AI Act regulation reference page
- Context (origin, sector, country, objective) is not encoded in canonical page URLs unless it is a genuinely distinct page
- Diagnostic query states (`/diagnostic?origin=us`) are not stable, indexable, or agent-readable routes
- The route registry in `routes.json` is the definitive map of what each URL means

---

## 10. robots.txt Accuracy

- `robots.txt` must never accidentally disallow a published, indexable reference page
- After every `robots.txt` change, verify all published pages remain crawlable
- The `Disallow` directives in `robots.txt` must be reviewed whenever a new route category is added
- Crawl budget is protected by sitemap hygiene and by not publishing thin pages that dilute crawl value

---

## 11. Future API and Readiness Endpoint Principles (Phase 4)

When Phase 4 introduces API access, the following principles apply from the first release:

- Endpoints return structured JSON with field names matching the EuraPlan Entry Ontology
- Every response includes source attribution metadata
- The `route_id` from `routes.json` is referenceable from API responses to the corresponding HTML page
- No API response omits the planning intelligence disclaimer context
- API versioning is explicit: `/api/v1/readiness/`
- No diagnostic or readiness API response may be construed as legal advice

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
