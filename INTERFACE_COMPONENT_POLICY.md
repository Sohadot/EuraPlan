# INTERFACE_COMPONENT_POLICY.md
**Version:** 1.1
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026 (Sprint 1B — Brand Asset Integration)
**Governed by:** GOVERNANCE_CHARTER.md, VISUAL_SYSTEM_GOVERNANCE.md, TECHNICAL_STANDARD.md

---

## 1. Purpose

This document defines the interface components that will be built in future phases. They are not implemented now — they are governed now. Defining them before implementation prevents ad hoc UI decisions that contradict the intelligence architecture.

Every component must embody the intelligence it represents. A Regulatory Clock component is not a design flourish — it is a structured representation of a regulatory timeline. Its visual form must follow from its intelligence function.

---

## 2. Component: Regulatory Clock

**Purpose:** Displays the timeline of applicable EU regulations by entity type, sector, and product. Shows enforcement phases, upcoming deadlines, and passed obligations.

**Data required:**
- List of applicable regulations (from EuraPlan Entry Ontology)
- Enforcement phases per regulation (from Tier 1 sourced regulation texts)
- Entity role (provider / deployer / manufacturer / etc.)
- Current date (to calculate time-to-deadline)

**Accessibility requirement:**
- All date and deadline data present in HTML source text, not only as visual timeline
- Yellow deadline markers accompanied by text labels
- Timeline navigable by keyboard
- Screen reader summary of the full timeline before visual presentation

**SEO safety requirement:**
- Core regulatory dates and phases rendered in HTML, not JavaScript-only
- Page must be indexable with the clock content present without JS execution

**Failure conditions:**
- Regulatory date rendered without article citation
- Clock shows dates for a company type that does not match the page context
- Deprecated regulation dates not marked as superseded

**When not to use:**
- On pages where a static text timeline in a table is sufficient
- When source capture for the displayed regulations is incomplete

**Brand mark (Sprint 1B+):** When a compact visual identity is shown on Clock surfaces (e.g., page hero or export header), use the clock + pillars mark (`assets/brand/logo-mark-gold.svg` on dark backgrounds). Brand Gold only — not European Yellow. The mark supplements text; it does not replace regulatory dates or citations.

---

## 3. Component: Context Gate

**Purpose:** Presents a condition that must be met before a company can proceed to the next planning step. Displays the condition, the evidence required, and the consequence of not meeting it.

**Data required:**
- Gate name and description
- Entry condition (what must be true)
- Evidence type (what document or action satisfies it)
- Consequence of not passing (regulatory or planning)
- Reference to EERS dimension it maps to

**Accessibility requirement:**
- Gate state (passed / not passed / unknown) conveyed in text, not colour alone
- Gate structure navigable by keyboard

**SEO safety requirement:**
- Gate content present in HTML source
- Not dependent on JavaScript for the intelligence content

**Failure conditions:**
- Gate condition stated without a basis in regulation text or official guidance
- Gate implies a legal conclusion (not permitted — must be framed as planning condition)

**When not to use:**
- When the condition is binary and can be expressed as a simple sentence
- When the page is a general reference page (not a company-specific planning tool)

---

## 4. Component: Readiness State Layer

**Purpose:** Displays a company's current score or estimated state across the eight EERS dimensions. Shows which dimensions are met, which are gaps, and which require action.

**Data required:**
- EERS dimension scores (derived from diagnostic input)
- Dimension labels and descriptions
- Gap descriptions for below-threshold dimensions

**Accessibility requirement:**
- All dimension states conveyed in text alongside any visual indicator
- Full dimension descriptions accessible without interaction
- No dimension state conveyed by colour alone

**SEO safety requirement:**
- Static representation of the EERS framework always present in HTML (the standard page at `/standard/eers/` serves this)
- Dynamic scoring output is session-specific and must not be indexed

**Failure conditions:**
- Readiness state presented as a binary pass/fail that implies compliance certification
- Scores displayed without the planning intelligence disclaimer
- Dimension scores derived from input without source-governed criteria

**When not to use:**
- On static reference pages where the standard (EERS) is the subject, not a specific company's score

---

## 5. Component: Compliance Gate

**Purpose:** Maps a specific product or service type to its applicable compliance checkpoints before EU market access. Shows which gates are regulatory requirements and which are strategic best practice.

**Data required:**
- Entity type and product classification
- Applicable regulation(s)
- Compliance checkpoint name and description
- Gate type: mandatory (regulatory) or recommended (strategic)
- Source citation for mandatory gates

**Accessibility requirement:**
- Mandatory vs. recommended distinction in text, not colour alone
- Gate descriptions in HTML source

**SEO safety requirement:**
- Mandatory compliance checkpoints in HTML source
- Not generated dynamically without static fallback

**Failure conditions:**
- A mandatory gate stated without Tier 1 source
- A recommended gate presented as mandatory
- Legal advice framing ("you must" without planning intelligence framing)

**When not to use:**
- On pages that are general regulatory overviews (use regulation reference page instead)

---

## 6. Component: Matrix Snippet

**Purpose:** Embeds a focused cross-reference extract from the full Country-Sector-Regulation Matrix within a regulation, country, or sector reference page. Shows only the rows/columns relevant to that page.

**Data required:**
- Subset of matrix data relevant to the current page context
- Source citations for each cell claim
- Link to the full matrix page

**Technical requirement:**
- Must be an HTML `<table>` with `<caption>`, `<thead>`, `<th scope>`, `<tbody>`
- Not a CSS grid
- Cell content in HTML text, not images or icon-only

**Accessibility requirement:**
- Table caption and header structure per ACCESSIBILITY_STANDARD.md
- Screen-reader-readable table summary paragraph before the table

**SEO safety requirement:**
- Matrix content present in HTML source

**Failure conditions:**
- Snippet content diverges from the source matrix page
- Cells contain visual marks without text content
- Published before the full matrix page exists

**When not to use:**
- When a simple sentence or list suffices — a table implies structured cross-reference data
- When the matrix is too large for a page context without confusion

---

## 7. Component: Pathway Strip

**Purpose:** Displays a sequential planning execution path — a 30/90/180-day entry plan structure, or a specific compliance sequence — as a visible, numbered strip.

**Data required:**
- Step titles and descriptions
- Time horizon assignment (30-day / 90-day / 180-day)
- Dependencies between steps
- EERS dimension each step addresses

**Accessibility requirement:**
- Steps in an ordered list (`<ol>`) or with explicit step numbers in text
- No step information conveyed only by position

**SEO safety requirement:**
- Step content in HTML source

**Failure conditions:**
- Steps presented without their logical dependencies
- Time horizons presented as fixed guarantees rather than planning anchors
- Implied legal advice in step descriptions

**When not to use:**
- On governance or source pages where sequential planning is not the subject

---

## 8. Component: Source Confidence Badge

**Purpose:** Displays the source confidence classification (Verified / Referenced / Pending / Deprecated) for a specific claim or section, per SOURCE_POLICY.md.

**Data required:**
- Classification level: Verified, Referenced, Pending, or Deprecated
- Source name and link (for Verified and Referenced)

**Visual:**
- Small badge with text label and colour differentiation
- Verified: green-adjacent on dark background with text
- Referenced: grey-light with text
- Pending: yellow with text (signals that publication should be blocked)
- Deprecated: red-adjacent with text
- Optional micro-mark: clock + pillars at badge scale only when a brand anchor is required; must not replace the text classification label

**Accessibility requirement:**
- Badge text must fully convey the state — no colour-only state
- Badge must not be the only indication that a section has source issues

**Failure conditions:**
- A Pending badge on a published page (publication must have been blocked)
- A Deprecated badge without a 30-day resolution plan

**When not to use:**
- On every sentence — badges are used at section or claim level, not inline on every statement

---

## 9. Component: Claim Risk Badge

**Purpose:** Displays the claim risk classification (Low / Medium / High / Blocked) for a section or output, per CLAIM_POLICY.md.

**Data required:**
- Risk level: Low, Medium, High, or Blocked
- Brief rationale (e.g., "High: regulatory deadline claim requiring Tier 1 citation")

**Accessibility requirement:**
- Text label for all risk levels

**Failure conditions:**
- A Blocked classification on a published claim (must not publish Blocked claims)
- A High claim published without Tier 1 source

**When not to use:**
- On Low-risk general framing sections where the label adds no user value

---

## 10. Component: Route Context Panel

**Purpose:** Displays related routes and navigation context at the end of a page, showing the user where they are in the reference corpus and what adjacent pages are most relevant to their planning question.

**Data required:**
- Related route IDs and titles from routes.json
- Relationship type (e.g., "related regulation," "applicable country," "planning step")

**Accessibility requirement:**
- Navigable by keyboard
- Descriptive link text for all related routes

**SEO safety requirement:**
- All related route links in HTML source
- Not loaded asynchronously

**Failure conditions:**
- Panel links to draft or unpublished routes
- Relationship labels are generic ("related page") with no substantive context

**When not to use:**
- On pages that already have comprehensive internal links in the body content
- On governance and source pages where navigation context is less relevant

---

## 11. Component: Governance Badge

**Purpose:** Identifies governed intelligence outputs, routes, or editorial layers that meet EuraPlan governance requirements before publication.

**Visual:**
- Text-first badge (e.g., "Governed," "Source-Governed," "Route-Governed")
- May include the clock + pillars mark at small scale (`logo-mark-gold.svg` on dark UI) when shown on governance or source surfaces
- Brand Gold for mark; European Yellow reserved for signal states only — not for the governance badge frame

**Accessibility requirement:**
- Governance state conveyed in text; mark is decorative (`aria-hidden="true"`) when adjacent to a text label

**When not to use:**
- As a substitute for source citations or claim risk classification
- On pages where governance is not the subject

---

## 12. Brief and Report Cover Identity

**Purpose:** Visual identity block for Phase 2+ briefs and planning reports (on-demand outputs).

**Visual:**
- Primary: clock + pillars mark + `EuraPlan` wordmark (text or `logo-wordmark-*.svg` on approved backgrounds)
- Strategic tagline on institutional covers: European Regulatory Entry & Expansion Planning Intelligence
- Interface tagline on in-product covers: European Entry Control Room
- Full composite logos (`logo-full-dark-bg.png`, `logo-full-light-bg.png`) only on approved export/print backgrounds

**Accessibility requirement:**
- Cover title and report type remain HTML text or accessible PDF text — mark does not replace the document title

**When not to use:**
- On static reference corpus pages in Phase 1 (use header mark only)

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
