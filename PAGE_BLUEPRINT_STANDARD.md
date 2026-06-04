# PAGE_BLUEPRINT_STANDARD.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, CONTENT_QUALITY_STANDARD.md, REFERENCE_CORPUS_GOVERNANCE.md

---

## 1. Purpose

Page blueprints define the mandatory structure for each class of EuraPlan page. They govern what content appears, in what order, what sources are required, what internal links are mandatory, and what patterns are prohibited.

No page of a given type may be published if it does not follow its blueprint. Blueprints are the production standard for the reference corpus.

---

## 2. Blueprint: Regulation Reference Page

**Route pattern:** `/regulation/[slug]/` — e.g., `/regulation/eu-ai-act/`

**Required fields (in order):**
1. Page thesis — what this regulation means for non-EU companies
2. Regulation ID — official number (e.g., Regulation (EU) 2024/1689)
3. Status and application date — when it entered into force and when it fully applies
4. Scope — which entity types, products, and market positions it governs
5. Application timeline — enforcement phases cited by article
6. Key obligations for non-EU companies — what they must do, cited by article
7. Interaction with other EU regulations — cross-regulation mapping
8. Entry planning implications — how this affects the EuraPlan Protocol
9. Source list — all citations with regulation number, article, EUR-Lex link
10. Planning intelligence disclaimer
11. Last updated date

**Required internal links:**
- `/clock/` — regulatory timeline context
- `/protocol/` — planning sequence
- `/standard/eers/` — readiness dimension context
- At least one related regulation page (once published)
- `/sources/`

**Source requirements:**
- Tier 1 mandatory for all obligation, deadline, and scope claims
- Every date cited references the specific article establishing it
- Source confidence: Verified for all central claims

**Acceptance criteria:**
- Minimum 800 words of substantive planning intelligence (not padding)
- No regulatory deadline without article citation
- No obligation claim without regulation text basis
- No implied legal advice
- No out-of-date enforcement dates
- No generic overview without entry-planning framing

**Prohibited patterns:**
- "What is GDPR?" introductory framing without planning intelligence
- Penalty amounts without citing the specific regulation article
- Future tense regulatory claims presented as confirmed
- Generic EU regulatory overview content not framed for non-EU company entry

---

## 3. Blueprint: Country Reference Page

**Route pattern:** `/country/[slug]/` — e.g., `/country/germany/`

**Required fields (in order):**
1. Page thesis — why this country matters for non-EU entry planning
2. Entry planning context — what makes this country distinct for regulatory and market entry
3. Regulatory implementation notes — how key EU frameworks are enforced nationally
4. Sector suitability signals — which sectors find this country a priority entry point
5. Entity setup considerations — key points on forming a legal presence (with official source)
6. Funding ecosystem — EU and national funding channels relevant here
7. Key national authorities — relevant regulatory, tax, and business registration bodies
8. Entry planning signals — structured signals for or against this country as first entry
9. Source list — all citations
10. Planning intelligence disclaimer
11. Last updated date

**Required internal links:**
- `/enter/`
- At least one relevant regulation page
- At least one relevant sector page (once published)
- `/standard/eers/`

**Source requirements:**
- Tier 1 for regulatory implementation claims
- Tier 2 for market context
- National official government source for entity setup information

**Prohibited patterns:**
- Tourism or cost-of-living content
- "[Country] is a great place for business" generic statements
- EU flag brochure framing
- Unverified tax rate claims
- Comparative rankings without official source

---

## 4. Blueprint: Sector Reference Page

**Route pattern:** `/sector/[slug]/` — e.g., `/sector/ai-saas/`

**Required fields (in order):**
1. Page thesis — what EU regulatory entry planning looks like for this sector
2. Sector scope — clear definition of what this sector means in EuraPlan terms
3. Applicable regulations — EU regulations with greatest impact on this sector, each sourced
4. Key compliance gates — sector-specific compliance checkpoints before EU market access
5. Country fit signals — which EU countries are particularly relevant for this sector
6. Funding opportunities — EU funding channels most relevant to this sector
7. EERS dimension notes — which readiness dimensions are most demanding in this sector
8. Source list
9. Planning intelligence disclaimer
10. Last updated date

**Required internal links:**
- `/clock/`
- At least one relevant regulation page
- At least one relevant country page (once published)
- `/standard/eers/`

**Source requirements:**
- Tier 1 for all regulatory applicability claims
- Tier 2 for market and sector fit signals

**Prohibited patterns:**
- Generic sector overview without EU regulatory entry framing
- Competitor comparisons or product/service recommendations
- Revenue potential claims without official source

---

## 5. Blueprint: Origin Reference Page

**Route pattern:** `/origin/[slug]/` — e.g., `/origin/us/`

**Required fields (in order):**
1. Page thesis — what European entry planning looks like for companies from this origin
2. Origin-EU regulatory relationship — equivalence, divergence, trade arrangements (sourced)
3. Priority regulatory exposure — which EU regulations most apply to companies from this origin
4. Country entry signals — which EU countries are most viable first entries from this origin
5. Funding eligibility context — whether companies from this origin qualify for EU funding instruments
6. Equivalence or recognition notes — any existing regulatory recognition arrangements, sourced
7. Entry planning priorities — what to address first based on origin context
8. Source list
9. Planning intelligence disclaimer
10. Last updated date

**Required internal links:**
- `/enter/`
- At least one relevant regulation page
- At least one relevant country page
- `/standard/eers/`
- `/protocol/`

**Source requirements:**
- Tier 1 for equivalence and regulatory relationship claims
- Tier 2 for market entry pattern signals

**Prohibited patterns:**
- Cultural or diplomatic commentary
- Claims about bilateral relationships without official documentation
- Legal advice on jurisdictional questions

---

## 6. Blueprint: Funding Reference Page

**Route pattern:** `/funding/[slug]/` — e.g., `/funding/horizon-europe/`

**Required fields (in order):**
1. Page thesis — what this funding programme means for non-EU companies entering Europe
2. Programme overview — scope, objectives, budget period (sourced from official documentation)
3. Eligibility for non-EU companies — specific conditions for non-EU participation
4. Relevant sectors — which sectors this programme primarily supports
5. Application process summary — key stages with link to official portal
6. Current call status — open or closed, with official EU Funding & Tenders Portal link
7. Integration with entry planning — how this maps to EERS Funding Awareness dimension
8. Source list — official programme documentation and portal links
9. Planning intelligence + funding disclaimer
10. Last updated date

**Required internal links:**
- `/enter/`
- `/standard/eers/` (Funding Awareness dimension)
- At least one relevant sector or country page

**Source requirements:**
- Tier 1 mandatory — official EU programme documentation only
- Call status must link directly to official EU Funding & Tenders Portal

**Prohibited patterns:**
- Funding amounts described as guaranteed
- Application process described without citing official sources
- Closed calls presented as open
- Specific grant amounts promised to specific company types

---

## 7. Blueprint: Matrix Page

**Route pattern:** `/matrix/[slug]/` — e.g., `/matrix/country-sector-regulation/`

**Activation requirement:** All underlying Layer 1 + Layer 2 + Layer 3 pages used in the matrix must be published first.

**Required fields (in order):**
1. Page thesis — what planning intelligence this matrix delivers
2. Matrix scope — which dimensions are cross-referenced and why
3. Reading guide — how to interpret the matrix for entry planning decisions
4. Matrix table — HTML `<table>` with `<caption>`, `<thead>`, `<th scope>`, `<tbody>`
5. Source summary — how each matrix intersection is sourced
6. Planning intelligence disclaimer
7. Last updated date

**Required internal links:**
- Links to every regulation, country, and sector page referenced in the matrix
- `/protocol/`
- `/sources/`

**Source requirements:**
- Tier 1 for every regulation-country-sector intersection claim

**Technical requirements:**
- Matrix data in HTML `<table>` — not CSS grid
- `<caption>` and `<th scope>` required for accessibility
- Table must be readable without CSS

**Prohibited patterns:**
- JavaScript-rendered matrix not present in HTML source
- Matrix cells with visual marks and no text content
- Matrix published before underlying reference pages are complete

---

## 8. Blueprint: Pre-Composed Brief

**Route pattern:** `/brief/[slug]/` — e.g., `/brief/us-saas-eu-ai-act-entry-2026/`

**Activation requirement:** Confirmed real demand (diagnostic data, search evidence, or institutional request). Not speculative.

**Required fields (in order):**
1. Brief scope — exact origin + sector + regulation/country combination
2. Target company profile — precise description of who this brief is for
3. Entry intelligence summary — what planning decisions this brief resolves
4. Regulatory entry clock for this profile — applicable timeline with citations
5. EERS scoring framing — how this profile typically performs against each dimension
6. 30/90/180-day planning anchors — key sequencing points for this specific profile
7. Advisory category map — what types of advisors are needed and when
8. Official source list — all citations at article level
9. Full planning intelligence disclaimer
10. Last updated date

**Required internal links:**
- All regulation pages relevant to the brief
- Relevant country page
- `/standard/eers/`
- `/protocol/`
- `/sources/`

**Source requirements:**
- Tier 1 for all regulatory claims, at article level

**Prohibited patterns:**
- Combinatorial brief created for SEO without confirmed demand
- Regulatory advice framing
- Guaranteed outcome language
- Implied specific legal strategy

---

## 9. Blueprint: Audience Layer Page

**Route pattern:** Governed by Wave 3+ in REFERENCE_CORPUS_GOVERNANCE.md

**Required fields:**
1. Audience identity — who specifically this page is for
2. How EuraPlan serves this audience — which intelligence outputs are most relevant to their role
3. Internal navigation — links to the most relevant reference pages for this audience
4. Appropriate disclaimer for audience type
5. Last updated date

**Prohibited patterns:**
- Compromising the primary non-EU company planning framing
- Adding content that contradicts primary layer pages
- Legal advice for lawyers, investment advice for investors

---

## 10. Blueprint: Standard Page (EERS and similar)

**Required fields:**
1. Standard name and version
2. What the standard defines and why it exists
3. The dimensions or components of the standard (fully described)
4. Who the standard applies to
5. How the standard is used in EuraPlan intelligence production
6. Relationship to other outputs (Protocol, Clock, etc.)
7. Disclaimer
8. Last updated date

**Prohibited patterns:**
- Claiming the standard is externally certified or independently regulated
- Using the standard to frame legal compliance conclusions

---

## 11. Blueprint: Source and Governance Pages

**Required fields:**
1. Purpose of the page
2. Summary of the relevant policy (source, claim, or governance architecture)
3. What the policy governs and why it matters to users
4. Links to related governance documents
5. Last updated date

**Prohibited patterns:**
- Claims about third-party partnerships or institutional endorsements
- Technical legal language implying compliance certification

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
