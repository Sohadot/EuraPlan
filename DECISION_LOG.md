# DECISION_LOG.md
**Version:** 1.1
**Status:** Active — Governance Infrastructure
**Asset:** EuraPlan.com
**Owner:** Sohadot
**Created:** Sprint 4D — June 2026
**Last Updated:** June 2026 (Sprint 5B)

---

## 1. Purpose

This document is the official audit-ready decision register for EuraPlan.com. It records major strategic, technical, SEO, content, source, interface, route, monetization, and sequencing decisions made from Sprint 0A onward.

It exists so that future contributors, AI agents, maintainers, and strategic buyers can understand:
- What was decided
- Why it was decided
- What it affects
- What would be required to reverse it

DECISION_LOG.md does not replace the governing documents listed in Section 9. It records major decisions made under them.

---

## 2. Decision Record Format

Each entry uses the following structure:

| Field | Description |
|---|---|
| Decision ID | Unique identifier — DEC-NNN / REJ-NNN / DEF-NNN |
| Date | Sprint in which the decision was made or ratified |
| Status | Active / Superseded / Deferred / Rejected |
| Decision | What was decided |
| Rationale | Why |
| Affected routes/files | HTML pages, governance docs, sitemap, routes.json |
| Governance documents involved | Which governing documents authorize or govern this |
| Reversal conditions | What would be required to reverse or supersede |
| Notes | Additional context |

---

## 3. Active Decision Register

### DEC-001
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** EuraPlan is a Category Intelligence Factory, not a generic website.
- **Rationale:** Generic websites compete on volume. EuraPlan claims ownership of a category — European Regulatory Entry Planning — and builds defensible category infrastructure. This identity governs every build, content, monetization, and partnership decision.
- **Affected routes/files:** All public pages; GOVERNANCE_CHARTER.md; EURAPLAN_CATEGORY_INTELLIGENCE_FACTORY_PLAN.md
- **Governance documents involved:** GOVERNANCE_CHARTER.md Section 1
- **Reversal conditions:** Full strategic repositioning approved by owner; all affected pages and governance documents revised
- **Notes:** Foundational identity decision. All other decisions flow from it.

### DEC-002
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Strategic identity is "European Regulatory Entry & Expansion Planning Intelligence."
- **Rationale:** Precision identity signals category authority to target audience, buyers, and search engines. Avoids generic "doing business in Europe" positioning.
- **Affected routes/files:** All page titles, meta descriptions, footer, OG tags, structured data
- **Governance documents involved:** GOVERNANCE_CHARTER.md; SEO_GOVERNANCE.md
- **Reversal conditions:** Owner-approved repositioning with full site-wide title/meta/structured-data update
- **Notes:** Used verbatim in footer and site identity markers across all pages.

### DEC-003
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Core thesis: "Europe punishes absence. Europe rewards planning."
- **Rationale:** A governing sentence that every page and output must be traceable to. Not a marketing tagline — an architectural constraint. Pages that cannot be traced to this thesis do not belong in the corpus.
- **Affected routes/files:** GOVERNANCE_CHARTER.md; index.html; all reference pages
- **Governance documents involved:** GOVERNANCE_CHARTER.md Section 2
- **Reversal conditions:** Owner approval; full content audit to replace all thesis anchors
- **Notes:** Used verbatim in GOVERNANCE_CHARTER.md and on public pages.

### DEC-004
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Primary audience: non-EU AI, SaaS, tech, compliance-sensitive, and growth companies entering Europe.
- **Rationale:** Precision audience prevents content drift. Generic "companies" leads to generic content. Named audience enables specific decision-problem framing on every page.
- **Affected routes/files:** All public pages (telemetry strip audience cell); CONTENT_QUALITY_STANDARD.md; ACCEPTANCE_CRITERIA.md
- **Governance documents involved:** GOVERNANCE_CHARTER.md; CONTENT_QUALITY_STANDARD.md
- **Reversal conditions:** Owner approval; full audience-framing audit across corpus
- **Notes:** Audience stated explicitly on every reference page in the telemetry strip.

### DEC-005
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** English-first public asset; Arabic remains owner-operator working language only.
- **Rationale:** Target audience is international technology companies entering Europe. Institutional English is the correct register. Multilingual expansion requires separate gating.
- **Affected routes/files:** All public pages; MULTILINGUAL_GOVERNANCE.md
- **Governance documents involved:** GOVERNANCE_CHARTER.md Section 8; MULTILINGUAL_GOVERNANCE.md
- **Reversal conditions:** Multilingual activation requires MULTILINGUAL_GOVERNANCE.md gating process and a new decision recorded here
- **Notes:** Arabic communications between owner and agents are internal and not published.

### DEC-006
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Prohibit combinatorial URL explosion.
- **Rationale:** Combinatorial URLs such as /from/us-ai/to/germany/as/ai-provider/under/ai-act produce thin content, dilute category authority, and cannot be governed at scale. Rejected in favour of pre-composed canonical reference pages.
- **Affected routes/files:** routes.json; ROUTE_GOVERNANCE.md; robots.txt
- **Governance documents involved:** ROUTE_GOVERNANCE.md
- **Reversal conditions:** Not reversible without full governance review. Combinatorial URL permission requires owner approval and a new route governance decision recorded here.
- **Notes:** See REJ-001.

### DEC-007
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Use three governed route layers: (1) heavy reference ontology pages, (2) one canonical /diagnostic, (3) pre-composed /brief/... documents only when justified.
- **Rationale:** Prevents route sprawl while preserving the three legitimate content output types. Each layer has distinct governance requirements.
- **Affected routes/files:** routes.json; ROUTE_GOVERNANCE.md; sitemap.xml
- **Governance documents involved:** ROUTE_GOVERNANCE.md; ACCEPTANCE_CRITERIA.md
- **Reversal conditions:** New route layer requires owner approval and a new governance decision recorded here
- **Notes:** /diagnostic and /brief/ both have separate activation gating.

### DEC-008
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Keep /diagnostic deferred and non-indexed until explicitly approved.
- **Rationale:** The diagnostic tool requires the full EuraPlan Entry Planning Protocol implemented in an engine, all EERS dimensions governed, and all regulatory mappings Tier 1 sourced. Premature activation produces ungoverned outputs.
- **Affected routes/files:** routes.json (diagnostic entry — non-indexed); robots.txt; sitemap.xml
- **Governance documents involved:** ACCEPTANCE_CRITERIA.md Section 5; ROUTE_GOVERNANCE.md
- **Reversal conditions:** Separate activation decision required — see DEF-001
- **Notes:** Diagnostic query states must remain disallowed in robots.txt until activated.

### DEC-009
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Keep /matrix/ unpublished until regulation, country, sector, funding, and source dependencies are ready.
- **Rationale:** An incomplete matrix produces misleading cross-references. Dependencies must be complete before the cross-reference is meaningful.
- **Affected routes/files:** routes.json (matrix entry — unpublished); sitemap.xml
- **Governance documents involved:** ROUTE_GOVERNANCE.md; REFERENCE_CORPUS_GOVERNANCE.md
- **Reversal conditions:** Separate activation decision required — see DEF-003
- **Notes:** Matrix content may be drafted internally. Route exists in routes.json as unpublished.

### DEC-010
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Use route registry (routes.json) before publication. Every route must have a routes.json entry before HTML is published.
- **Rationale:** Route governance requires knowing what exists before it goes live. The registry prevents orphan pages, duplicate routes, and undocumented indexation.
- **Affected routes/files:** routes.json; all HTML pages
- **Governance documents involved:** ROUTE_GOVERNANCE.md; SCALING_AND_AUTOMATION_POLICY.md Section 6
- **Reversal conditions:** Not reversible — route registry is permanent infrastructure
- **Notes:** Changing publication_status to published is a human-only action.

### DEC-011
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Published routes must be in sitemap.xml and not blocked by robots.txt.
- **Rationale:** Indexation consistency. A page published without sitemap inclusion is effectively hidden. A page blocked by robots.txt while in sitemap creates a contradiction.
- **Affected routes/files:** sitemap.xml; robots.txt; routes.json
- **Governance documents involved:** SEO_GOVERNANCE.md; ROUTE_GOVERNANCE.md
- **Reversal conditions:** Only if a published page requires deindexation (governance violation, legal requirement) — requires documented rollback per SCALING_AND_AUTOMATION_POLICY.md Section 12
- **Notes:** Diagnostic query states and draft routes are explicitly excluded from sitemap.

### DEC-012
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Interface must embody the thesis, not decorate the asset.
- **Rationale:** A planning intelligence platform that looks like a generic information site undermines its authority. The interface is itself a signal of category seriousness.
- **Affected routes/files:** assets/css/main.css; all public HTML; INTERFACE_COMPONENT_POLICY.md
- **Governance documents involved:** INTERFACE_COMPONENT_POLICY.md; VISUAL_SYSTEM_GOVERNANCE.md
- **Reversal conditions:** Owner-approved redesign with governance review
- **Notes:** Foundational interface philosophy constraint from which DEC-013 through DEC-016 derive.

### DEC-013
- **Date:** Sprint 0B
- **Status:** Active
- **Decision:** Adopt European Entry Control Room as the interface direction.
- **Rationale:** Positions EuraPlan as an operational intelligence instrument — a control room for EU entry — rather than a marketing site or information portal. Supports the Category Intelligence Factory identity.
- **Affected routes/files:** All public HTML (class="control-room-shell"); assets/css/main.css
- **Governance documents involved:** INTERFACE_COMPONENT_POLICY.md; VISUAL_SYSTEM_GOVERNANCE.md
- **Reversal conditions:** Full design system change — owner approval required, new interface decision recorded here
- **Notes:** Used in site header label, page hero labels, and CSS class architecture.

### DEC-014
- **Date:** Sprint 0B
- **Status:** Active
- **Decision:** Adopt clock + pillars mark as official interface-facing identity (logo-mark-gold.svg).
- **Rationale:** The mark communicates precision timing (clock) and European institutional authority (pillars) — directly aligned with the category claim. Distinguishes from generic globe/map/flag identity common in European market entry sites.
- **Affected routes/files:** assets/brand/logo-mark-gold.svg; all public HTML (header and hero); OG images
- **Governance documents involved:** VISUAL_SYSTEM_GOVERNANCE.md
- **Reversal conditions:** Owner-approved brand decision; all HTML, OG, and structured data references updated
- **Notes:** Mark used at 32×32 in header and 64×64 in hero sections.

### DEC-015
- **Date:** Sprint 0B
- **Status:** Active
- **Decision:** Use Brand Gold for identity and European Yellow only for deadlines, gates, and decisions.
- **Rationale:** Colour carries semantic meaning in the EuraPlan system. Brand Gold signals authority and identity. European Yellow (--eu-yellow) signals action, urgency, and deadlines. Conflating them destroys the visual communication hierarchy.
- **Affected routes/files:** assets/css/main.css; VISUAL_SYSTEM_GOVERNANCE.md
- **Governance documents involved:** VISUAL_SYSTEM_GOVERNANCE.md
- **Reversal conditions:** Visual system redesign — owner approval required, new visual decision recorded here
- **Notes:** Defined as CSS custom properties --brand-gold and --eu-yellow.

### DEC-016
- **Date:** Sprint 0B
- **Status:** Active
- **Decision:** Keep interface HTML-first and CSS-first; no WebGL, canvas, or 3D unless explicitly justified by a governance decision.
- **Rationale:** HTML-first ensures accessibility, search-engine readability, and performance. WebGL/canvas/3D introduce dependency, accessibility failure, and performance risk without clear intelligence value in Phase 1.
- **Affected routes/files:** All public HTML; assets/css/main.css; INTERFACE_COMPONENT_POLICY.md
- **Governance documents involved:** INTERFACE_COMPONENT_POLICY.md; TECHNICAL_STANDARD.md; ACCESSIBILITY_STANDARD.md
- **Reversal conditions:** Specific governance decision approving a defined use case — cannot be reversed for general use
- **Notes:** Applies to Phase 1 and Phase 2. Phase 3 may revisit with a separate decision.

### DEC-017
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Source claims must be governed by the source tier system.
- **Rationale:** The credibility of EuraPlan's intelligence outputs depends on the credibility of its sources. An ungoverned source is an ungoverned claim. Tier 1 (official EU/government), Tier 2 (institutional), Tier 3 (secondary) — each has defined use cases.
- **Affected routes/files:** All reference pages; SOURCE_POLICY.md; source tables on all pages
- **Governance documents involved:** SOURCE_POLICY.md
- **Reversal conditions:** Not reversible — source governance is permanent infrastructure
- **Notes:** Source tier displayed via .source-confidence-badge on every reference page.

### DEC-018
- **Date:** Sprint 2
- **Status:** Active
- **Decision:** Tier 1 official sources are required for all regulation reference pages.
- **Rationale:** Regulatory claims made without official source support expose the asset to credibility failure. EUR-Lex, EC official communications, and official regulation texts are the only acceptable primary sources for regulatory obligation statements.
- **Affected routes/files:** regulation/eu-ai-act/, regulation/gdpr/, regulation/eu-data-act/, regulation/cyber-resilience-act/
- **Governance documents involved:** SOURCE_POLICY.md; ACCEPTANCE_CRITERIA.md Section 7
- **Reversal conditions:** Not reversible for regulation pages — Tier 1 requirement is permanent
- **Notes:** Applied and audited in Sprint 4B regulatory stack integration review.

### DEC-019
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** No unsupported partnership or endorsement claims.
- **Rationale:** Claiming an official relationship with an EU institution or government body without a formal agreement is a material misrepresentation. All institution references must include explicit disclaimers.
- **Affected routes/files:** All public pages (institution disclaimers); CLAIM_POLICY.md
- **Governance documents involved:** CLAIM_POLICY.md; GOVERNANCE_CHARTER.md Section 7
- **Reversal conditions:** Not reversible — a formal, documented partnership agreement would require a separate disclosure decision
- **Notes:** Standard disclaimer: "EuraPlan has no partnership with, and receives no endorsement from, any institution named on this page."

### DEC-020
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** No legal, tax, compliance, funding, incorporation, or investment advice framing.
- **Rationale:** EuraPlan produces planning intelligence, not professional services advice. Advice framing creates regulatory and liability exposure and misrepresents the product.
- **Affected routes/files:** All public pages (disclaimer blocks); CLAIM_POLICY.md
- **Governance documents involved:** CLAIM_POLICY.md; GOVERNANCE_CHARTER.md Section 7
- **Reversal conditions:** Not reversible — permanent policy
- **Notes:** Disclaimer wording varies by page type: legal/tax for regulation pages; investment/immigration added on country pages; funding/grant added on funding pages.

### DEC-021
- **Date:** Sprint 2
- **Status:** Active
- **Decision:** Planning-intelligence disclaimers are mandatory on all regulation and country reference pages.
- **Rationale:** Readers may mistake detailed regulatory planning information for legal advice. A visible disclaimer at the page level (not only in footer) is required to prevent misrepresentation.
- **Affected routes/files:** All regulation and country HTML pages (disclaimer element in hero section)
- **Governance documents involved:** CLAIM_POLICY.md; ACCEPTANCE_CRITERIA.md
- **Reversal conditions:** Not reversible — mandatory for all current and future regulation/country pages
- **Notes:** Disclaimer appears in hero section at 0.72rem, below badge row, on all 7 current reference pages. Extended to funding pages in Sprint 5A.

### DEC-022
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Internal review documents must be created after each completed layer before the next layer opens.
- **Rationale:** Review documents create an auditable record that a layer passed its governance gates. They prevent scope bleed and undocumented decisions between layers.
- **Affected routes/files:** Internal review .md files; REFERENCE_CORPUS_GOVERNANCE.md
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md; SCALING_AND_AUTOMATION_POLICY.md
- **Reversal conditions:** Not reversible — review documentation is permanent governance infrastructure
- **Notes:** Applied: regulation layer review before country pages; country layer review before sector; sector layer review before funding.

### DEC-023
- **Date:** Sprint 2
- **Status:** Active
- **Decision:** Build four regulation references first: EU AI Act, GDPR, EU Data Act, Cyber Resilience Act.
- **Rationale:** These are the four primary Wave 1 regulations affecting non-EU technology companies entering Europe. They form the regulatory foundation that country, sector, and funding pages depend on.
- **Affected routes/files:** regulation/eu-ai-act/, regulation/gdpr/, regulation/eu-data-act/, regulation/cyber-resilience-act/; routes.json; sitemap.xml
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md; FIRST_PUBLIC_RELEASE_PLAN.md
- **Reversal conditions:** Adding a fifth regulation requires a new sequencing decision recorded here
- **Notes:** All four delivered and governed in Sprint 2.

### DEC-024
- **Date:** Sprint 3
- **Status:** Active
- **Decision:** Perform regulatory stack integration review before country pages.
- **Rationale:** Country pages depend on regulation pages being complete and accurate. An integration review catches cross-page consistency issues before country content multiplies them.
- **Affected routes/files:** Sprint 3 integration review document; country pages
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md; SCALING_AND_AUTOMATION_POLICY.md
- **Reversal conditions:** Not reversible — sequencing gate is permanent
- **Notes:** Review completed Sprint 3 before country pages were opened.

### DEC-025
- **Date:** Sprint 3
- **Status:** Active
- **Decision:** Build first country trio: Germany, Netherlands, France.
- **Rationale:** These three markets represent the primary EU entry scenarios for non-EU technology companies: Germany (large enterprise/industrial), Netherlands (digital infrastructure/HQ), France (industrial policy/AI). They form the country execution layer above the regulation reference layer.
- **Affected routes/files:** country/germany/, country/netherlands/, country/france/; routes.json; sitemap.xml
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md
- **Reversal conditions:** Removing a country page requires owner approval and a route deprecation decision recorded here
- **Notes:** All three delivered and governed in Sprint 3.

### DEC-026
- **Date:** Sprint 3B
- **Status:** Active
- **Decision:** Perform country layer integration review before sector pages.
- **Rationale:** Sector pages depend on country pages being consistent and well-linked. Integration review before sector prevents compounding errors.
- **Affected routes/files:** Sprint 3B integration review document; sector pages
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md
- **Reversal conditions:** Not reversible — sequencing gate is permanent
- **Notes:** Review completed Sprint 3B before sector page was opened.

### DEC-027
- **Date:** Sprint 4A
- **Status:** Active
- **Decision:** Build AI/SaaS as the first sector node.
- **Rationale:** AI/SaaS is the highest-frequency audience segment among non-EU technology companies entering Europe. It sits at the intersection of EU AI Act, GDPR, and Data Act obligations, maximising cross-link value to existing regulation pages.
- **Affected routes/files:** sector/ai-saas/; routes.json; sitemap.xml
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md
- **Reversal conditions:** Second sector page requires a new sector sequencing decision — see DEF-006
- **Notes:** Delivered Sprint 4A.

### DEC-028
- **Date:** Sprint 4B
- **Status:** Active
- **Decision:** Perform sector layer integration review before opening funding or second sector.
- **Rationale:** Sector layer must be audited for cross-layer consistency before the funding layer opens. The review confirmed source tables, internal link structure, and EERS dimension mapping across all published pages.
- **Affected routes/files:** Sprint 4B integration review document
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md
- **Reversal conditions:** Not reversible — sequencing gate is permanent
- **Notes:** Review completed Sprint 4B. Identified source table caption defect, fixed in Sprint 4C.

### DEC-029
- **Date:** Sprint 4C
- **Status:** Active
- **Decision:** Perform source table accessibility hardening before funding. Add `<caption>` elements to all ep-table source list tables on regulation and country pages.
- **Rationale:** Sprint 4B integration review identified missing `<caption>` elements on 7 source tables — a WCAG semantic table labelling defect. Hardening required before opening the funding layer.
- **Affected routes/files:** regulation/eu-ai-act/, regulation/gdpr/, regulation/eu-data-act/, regulation/cyber-resilience-act/, country/germany/, country/netherlands/, country/france/
- **Governance documents involved:** ACCESSIBILITY_STANDARD.md; ACCEPTANCE_CRITERIA.md
- **Reversal conditions:** Not reversible — caption elements are a permanent accessibility requirement
- **Notes:** Fixed Sprint 4C across 5 commits on branch claude/sector-layer-integration-audit-Umx6V.

### DEC-030
- **Date:** Sprint 4D
- **Status:** Active
- **Decision:** Horizon Europe is the preferred next funding node (Sprint 5A) after decision log completion.
- **Rationale:** Horizon Europe is the largest EU research and innovation funding programme, directly relevant to non-EU technology companies entering Europe for R&D, pilots, and partnership access. Natural first node in the funding reference layer.
- **Affected routes/files:** funding/horizon-europe/ (delivered Sprint 5A); routes.json
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md; FIRST_PUBLIC_RELEASE_PLAN.md
- **Reversal conditions:** Owner decision to open a different funding programme first — requires decision recorded here
- **Notes:** Delivered Sprint 5A per DEC-039.

### DEC-031
- **Date:** Sprint 4D
- **Status:** Active
- **Decision:** Cloud/Data Infrastructure and Connected Products/IoT are candidate next sector pages after AI/SaaS.
- **Rationale:** Both sectors have direct regulatory linkage to the Data Act and CRA — already published. They represent the next-highest-frequency audience segments among non-EU technology companies.
- **Affected routes/files:** sector/cloud-data/ and sector/iot-connected-products/ (both pending, not approved)
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md
- **Reversal conditions:** Sector sequencing decision required before opening — see DEF-006
- **Notes:** Candidate status only. Sequencing decision required before any page is created.

### DEC-032
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Static-first architecture. No server-side rendering, dynamic routing, or database unless explicitly approved.
- **Rationale:** Static architecture provides maximum performance, security, deployment simplicity, and governance clarity in Phase 1. No moving parts that can fail, be compromised, or require infrastructure management.
- **Affected routes/files:** All HTML; assets/css/main.css; TECHNICAL_STANDARD.md; SECURITY_POLICY.md
- **Governance documents involved:** TECHNICAL_STANDARD.md; SECURITY_POLICY.md
- **Reversal conditions:** Phase 3 diagnostic engine may require dynamic infrastructure — requires a separate architecture decision recorded here
- **Notes:** Applies to Phase 1 and Phase 2 indefinitely.

### DEC-033
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** No third-party scripts, trackers, forms, cookies, API keys, unsafe embeds, or external dependencies unless explicitly approved by a governance decision.
- **Rationale:** Third-party scripts introduce performance, privacy, security, and governance risk. Each addition must be justified individually, not permitted by default.
- **Affected routes/files:** All public HTML; SECURITY_POLICY.md; ANALYTICS_AND_INDEXATION_POLICY.md
- **Governance documents involved:** SECURITY_POLICY.md; TECHNICAL_STANDARD.md
- **Reversal conditions:** Each third-party addition requires a separate governance decision recorded here
- **Notes:** Permanent policy. JSON-LD is allowed as a defined exception — see DEC-034.

### DEC-034
- **Date:** Sprint 0B
- **Status:** Active
- **Decision:** JSON-LD is allowed conservatively for structured data (Article, BreadcrumbList schema types).
- **Rationale:** JSON-LD structured data improves search engine understanding and is an inline script with no external dependency, no tracking, and no performance cost. Supports SEO and intelligence-output goals without governance risk.
- **Affected routes/files:** All public HTML (JSON-LD blocks in `<head>`); STRUCTURED_DATA_POLICY.md
- **Governance documents involved:** STRUCTURED_DATA_POLICY.md
- **Reversal conditions:** Additional schema types require separate governance approval per STRUCTURED_DATA_POLICY.md
- **Notes:** Currently uses Article and BreadcrumbList only. Other types require STRUCTURED_DATA_POLICY.md approval.

### DEC-035
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Core content must remain HTML-first and accessible (WCAG 2.1 AA minimum).
- **Rationale:** Accessibility is a legal obligation in the EU market, a signal of quality to enterprise procurement, and a prerequisite for the site's intelligence content to be readable by both humans and AI agents.
- **Affected routes/files:** All public HTML; assets/css/main.css; ACCESSIBILITY_STANDARD.md
- **Governance documents involved:** ACCESSIBILITY_STANDARD.md; TECHNICAL_STANDARD.md
- **Reversal conditions:** Not reversible — accessibility is a permanent requirement
- **Notes:** WCAG 2.1 AA is the current target. Sprint 4C addressed the source table caption defect.

### DEC-036
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Monetization must come from respectable intelligence outputs, not low-quality advertising.
- **Rationale:** Low-quality advertising contradicts the Category Intelligence Factory identity and degrades perceived authority. Revenue must be traceable to intelligence value delivery.
- **Affected routes/files:** MONETIZATION_BOUNDARY.md
- **Governance documents involved:** MONETIZATION_BOUNDARY.md; GOVERNANCE_CHARTER.md
- **Reversal conditions:** Any advertising or affiliate channel requires a separate monetization decision recorded here
- **Notes:** See REJ-005 for the rejected alternative.

### DEC-037
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Future revenue candidates include diagnostic reports, premium briefs, governed directories, audit intake, licensing, and institutional reports.
- **Rationale:** Each revenue type is consistent with the intelligence model. None can be activated before the prerequisite reference corpus and governance layer are in place.
- **Affected routes/files:** MONETIZATION_BOUNDARY.md; BUYER_LOGIC.md
- **Governance documents involved:** MONETIZATION_BOUNDARY.md
- **Reversal conditions:** Individual monetization unit activation requires a separate decision recorded here and ACCEPTANCE_CRITERIA.md Section 8 to pass
- **Notes:** All in deferred status until activation prerequisites are met.

### DEC-038
- **Date:** Sprint 0A
- **Status:** Active
- **Decision:** Acquisition logic frames EuraPlan as category infrastructure, not a normal website.
- **Rationale:** A buyer acquiring EuraPlan acquires a governed, defensible category position in European Regulatory Entry Planning — not a traffic asset or content library. This framing affects how the asset is documented, how governance is maintained, and how future decisions are recorded.
- **Affected routes/files:** BUYER_LOGIC.md; /acquire/ public page
- **Governance documents involved:** BUYER_LOGIC.md; GOVERNANCE_CHARTER.md
- **Reversal conditions:** Owner decision — repositioning the acquisition thesis requires owner approval and update to BUYER_LOGIC.md and /acquire/
- **Notes:** DECISION_LOG.md itself is part of the acquisition-ready governance infrastructure.

### DEC-039
- **Date:** Sprint 5A
- **Status:** Active
- **Decision:** Publish /funding/horizon-europe/ as the first funding reference node (EP-FUND-001), activating the funding reference layer (Layer 4) of the EuraPlan ontology.
- **Rationale:** DEC-030 designated Horizon Europe as the preferred first funding node, pending Sprint 4D decision log completion as the prerequisite gate. That gate was cleared. Horizon Europe is the largest EU R&D programme (2021–2027) with direct planning relevance for non-EU technology companies entering Europe for R&D partnerships, innovation pilots, and institutional sequencing. robots.txt required `Allow: /funding/` to permit indexation of the new route.
- **Affected routes/files:** funding/horizon-europe/index.html (new); routes.json (EP-FUND-001 added); sitemap.xml (new URL); robots.txt (`Allow: /funding/` added); sector/ai-saas/index.html (nav-link added); country pages and core pages (minimal nav-link updates)
- **Governance documents involved:** REFERENCE_CORPUS_GOVERNANCE.md; ROUTE_GOVERNANCE.md; SEO_GOVERNANCE.md; robots.txt; ACCESSIBILITY_STANDARD.md (caption on ep-table confirmed)
- **Reversal conditions:** Deindexation decision required (removes from sitemap; adds `Disallow: /funding/` to robots.txt); route deprecation per SCALING_AND_AUTOMATION_POLICY.md Section 12; decision recorded here as Superseded
- **Notes:** Page includes 8 funding readiness dimensions (FRD-01–08), 6 planning gates (F-GATE-01–06), EERS dimension mapping, EIC section, regulation × Horizon Europe coordination, matrix snippet, scope limits, and 5 Tier 1 official sources with ep-table caption. No funding advice, no eligibility claims, no JS. Layer 4 of EuraPlan ontology now open.

### DEC-040
- **Date:** Sprint 4E
- **Status:** Active
- **Decision:** Implement production security headers for EuraPlan.com via Cloudflare Pages `_headers` at repository root.
- **Rationale:** Closes the security policy-to-runtime execution gap identified in due diligence. EuraPlan is confirmed hosted on Cloudflare Pages as a static site; `_headers` is the correct deployment-layer mechanism for static response headers on that platform. Global rule applies to `/*` with baseline headers: `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, and `Permissions-Policy`.
- **Affected routes/files:** `_headers` (new); SECURITY_POLICY.md Section 8; DECISION_LOG.md
- **Governance documents involved:** SECURITY_POLICY.md; TECHNICAL_STANDARD.md; ACCEPTANCE_CRITERIA.md
- **Reversal conditions:** Owner-approved hosting migration away from Cloudflare Pages requires equivalent header enforcement on the new platform; decision recorded as Superseded with replacement mechanism documented
- **Notes:**
  - CSP is a **controlled baseline**, not maximum hardening: `script-src 'self' 'unsafe-inline'` and `style-src 'self' 'unsafe-inline'` are temporarily allowed because the static corpus uses inline JSON-LD script blocks and inline layout styles.
  - HSTS uses `max-age=31536000; includeSubDomains` — **no `preload`**.
  - Future hardening may move to hash-based CSP after structured-data externalization and inline-style cleanup.
  - **Verification gate:** Closed in DEC-041 (Sprint 4E-RC1). Runtime enforcement mechanism clarified there — `_headers` remains repository artifact; verified enforcement is Cloudflare Response Header Transform Rule while GitHub Pages/Fastly origin remains behind Cloudflare.

### DEC-041
- **Date:** Sprint 4E-RC1
- **Status:** Active
- **Decision:** Record production security-header verification and align governance with verified runtime enforcement mechanism.
- **Rationale:** Sprint 4E added `_headers` and documented Cloudflare Pages header enforcement. Production HTTP header capture confirmed all required security headers are active at runtime. However, the live response path still shows GitHub Pages/Fastly origin behavior behind Cloudflare — therefore the **verified** runtime enforcement mechanism is the Cloudflare **Response Header Transform Rule** named **EuraPlan Security Headers**, not repository `_headers` alone.
- **Affected routes/files:** DECISION_LOG.md; SECURITY_POLICY.md Section 8
- **Governance documents involved:** SECURITY_POLICY.md; DEC-040
- **Reversal conditions:** Cloudflare Pages becomes the active serving layer and `_headers` is confirmed via live header capture — record superseding note in DEC-041 Notes; Transform Rule may then be retired or kept as redundant edge policy per owner decision
- **Notes:**
  - **Production verification completed** via `curl.exe -I https://euraplan.com/` (or equivalent).
  - **Observed headers:** `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`.
  - **Verified runtime mechanism:** Cloudflare Response Header Transform Rule — **EuraPlan Security Headers**.
  - **`_headers` status:** Remains in repository as Cloudflare Pages-compatible deployment artifact. Must not be treated as verified runtime enforcement unless Cloudflare Pages is the active serving layer and headers are confirmed by live capture.
  - **Security policy-to-runtime gap:** **CLOSED** as of production header capture (Sprint 4E-RC1).
  - **Future:** Hosting migration to Cloudflare Pages may make `_headers` the primary runtime mechanism — requires new verification capture before governance records are updated.

### DEC-042
- **Date:** Sprint 4F
- **Status:** Active
- **Decision:** Close the structured data governance-to-implementation gap by adding conservative inline JSON-LD to all eight core category pages.
- **Rationale:** `STRUCTURED_DATA_POLICY.md` required schema by page type, but `/`, `/enter/`, `/clock/`, `/standard/eers/`, `/protocol/`, `/sources/`, `/governance/`, and `/acquire/` lacked JSON-LD while reference pages already had Article + BreadcrumbList. Due diligence identified this as a critical gap between policy and runtime page markup. Inline JSON-LD is the clearest agent-readability pattern and is permitted under the verified baseline CSP (`script-src 'self' 'unsafe-inline'`).
- **Affected routes/files:** `index.html`; `enter/index.html`; `clock/index.html`; `standard/eers/index.html`; `protocol/index.html`; `sources/index.html`; `governance/index.html`; `acquire/index.html`; `STRUCTURED_DATA_COVERAGE_AUDIT.md` (new, internal); `STRUCTURED_DATA_POLICY.md` Section 2 (implementation note)
- **Governance documents involved:** STRUCTURED_DATA_POLICY.md; AGENT_READABILITY_POLICY.md; SEO_GOVERNANCE.md
- **Reversal conditions:** Schema removal or type change requires decision recorded here as Superseded; full corpus re-audit against STRUCTURED_DATA_POLICY.md
- **Notes:**
  - **Schema types used:** `WebSite`, `Organization` (homepage); `WebPage` + `BreadcrumbList` (enter, clock, sources, governance, acquire); `Article` + `BreadcrumbList` (eers, protocol).
  - **Conservative scope:** No ratings, reviews, awards, service schema, fake endorsements, official affiliation schema, valuation schema, Product, Offer, Event, or price schema.
  - **EERS / Protocol:** Described as EuraPlan planning-intelligence artifacts — not official EU standards, government endorsement, or certification authority.
  - **Inline JSON-LD:** Retained under verified baseline CSP; externalization and hash-based CSP deferred until schema coverage stabilizes.
  - **Reference pages:** Regulation, country, sector, and funding pages already compliant — not modified in Sprint 4F.
  - **Audit:** `STRUCTURED_DATA_COVERAGE_AUDIT.md` records before/after coverage (internal, not in sitemap).

### DEC-043
- **Date:** Sprint 4G
- **Status:** Active
- **Decision:** Create the provenance and authenticity layer — five acquisition-readiness governance documents closing the third major due-diligence gap.
- **Rationale:** EuraPlan is a governed category intelligence asset, not merely a static website. Strategic value and buyer due diligence require documented proof of origin, custody, authenticity, transfer components, and rights posture. Sprints 4E/4E-RC1 closed security policy-to-runtime; Sprint 4F closed structured data policy-to-implementation; Sprint 4G closes provenance/authenticity without creating public pages or claiming legal certification.
- **Affected routes/files:** `PROVENANCE.md` (new); `AUTHENTICITY_CERTIFICATE.md` (new); `CHAIN_OF_CUSTODY.md` (new); `ASSET_TRANSFER_MANIFEST.md` (new); `RIGHTS_AND_USAGE_NOTICE.md` (new); `DECISION_LOG.md`; `GOVERNANCE_CHARTER.md` (minimal cross-reference); `BUYER_LOGIC.md` (minimal cross-reference); `ACCEPTANCE_CRITERIA.md` (minimal cross-reference)
- **Governance documents involved:** BUYER_LOGIC.md; GOVERNANCE_CHARTER.md; ACCEPTANCE_CRITERIA.md; SECURITY_POLICY.md (DEC-041 reference); STRUCTURED_DATA_COVERAGE_AUDIT.md (DEC-042 reference)
- **Reversal conditions:** Provenance layer deprecation requires owner decision recorded as Superseded; transfer completion may supersede with buyer-controlled custody records
- **Notes:**
  - **Files created:** PROVENANCE.md, AUTHENTICITY_CERTIFICATE.md, CHAIN_OF_CUSTODY.md, ASSET_TRANSFER_MANIFEST.md, RIGHTS_AND_USAGE_NOTICE.md — internal, not in sitemap, not linked from public navigation.
  - **No open-source LICENSE** added — rights reserved unless owner adds explicit license in future DEC entry.
  - **No claims:** formal notarization, trademark registration, government certification, institutional endorsement, valuation, sale price, traffic/revenue/ranking guarantees, or automatic third-party service transfer.
  - **Relationship:** Builds on DEC-041 (security runtime verification) and DEC-042 (structured data closure) as verification anchors in AUTHENTICITY_CERTIFICATE.md.
  - **Future hardening:** signed release tags, notarized certificate, timestamped archive, domain registry export, Cloudflare configuration export, buyer data room packaging.

### DEC-044
- **Date:** Sprint 5B
- **Status:** Active
- **Decision:** Complete funding layer integration review and accept Horizon Europe (`EP-FUND-001`) as integrated Layer 4 of the governed corpus.
- **Rationale:** Sprint 5A (DEC-039) published `/funding/horizon-europe/` without a formal integration review. Sprint 5B audits route registry, sitemap, robots, internal links, sources, claim boundaries, structured data, accessibility, security, and provenance alignment — mirroring Sprints 2E, 3D, and sector layer review pattern. No rebuild of Sprint 5A performed.
- **Affected routes/files:** `FUNDING_LAYER_INTEGRATION_REVIEW.md` (new, internal); `funding/horizon-europe/index.html` (FRD-04 claim-boundary fix); `enter/index.html` (funding situation card link); `routes.json` (funding link parity on 7 routes); `DECISION_LOG.md`
- **Governance documents involved:** ROUTE_GOVERNANCE.md; REFERENCE_CORPUS_GOVERNANCE.md; SOURCE_POLICY.md; CLAIM_POLICY.md; STRUCTURED_DATA_COVERAGE_AUDIT.md; DEC-039; DEC-043
- **Reversal conditions:** Funding layer deindexation requires DEC entry Superseded; route deprecation per SCALING_AND_AUTOMATION_POLICY.md Section 12
- **Notes:**
  - **Audit result:** APPROVED — 17 sitemap URLs; `Allow: /funding/` in robots.txt; EP-FUND-001 complete in routes.json.
  - **Defects fixed:** FRD-04 "optimal" country-ranking language; enter funding card missing Horizon Europe link; routes.json `required_internal_links` parity for enter, eers, protocol, sector, country trio.
  - **No new funding pages** created. No sitemap/robots changes.
  - **Next expansion:** controlled by future DEC entry — recommend Sprint 5C (agent readability) before second funding or sector page.

### DEC-045
- **Date:** 2026-08-20 (Reference Sovereignty Sprint — EU AI Act Publish Gate, Release Candidate)
- **Status:** Active
- **Decision:** Prepare and authorize the first governed Evidence Graph publication (Release Candidate) on the existing EU AI Act reference route. Fourteen human-verified Claim Objects (`EP-CLM-000001`..`EP-CLM-000014`) become publication candidates (`workflow_state: publishable`) with stable Citation Units (`#ep-clm-000001`..`#ep-clm-000014`) and a machine-readable canonical `regulation/eu-ai-act/claims.json`. The `/regulation/eu-ai-act/` and `/clock/` pages are corrected against the canonical claims. The final `published`/`active` transition and merge to `main` remain gated on Release Candidate review.
- **Rationale:** The legacy AI Act timeline predated Regulation (EU) 2026/1744 (Digital Omnibus on AI, in force 27 July 2026) and displayed high-risk dates as "Verified" while no longer correct. The Sovereignty layer (evidence graph, claim identity/lifecycle, freshness engine) makes each fact provable and citable; this decision authorizes the publication candidate for the first regulation as a Release Candidate without changing the 14 verified propositions.
- **Affected routes/files:** `regulation/eu-ai-act/claims.json` (new, canonical); `regulation/eu-ai-act/index.html` (timeline corrected; Verified Claim Register with 14 anchors; sources; dates); `clock/index.html` (AI Act lane/list corrected; dates; RC.2 visual scale); `llms.txt` (expose claims.json); `routes.json` (claims.json registered as alternate machine representation of EP-REG-001); `ROUTE_GOVERNANCE.md` (alternate machine representation registry rule); `assets/css/main.css` (five-year clock surface comment/scale); `governance/audits/EU_AI_ACT_PUBLISH_GATE_2026-08-20.md` (new); `DECISION_LOG.md`
- **Governance documents involved:** REFERENCE_SOVEREIGNTY_DOCTRINE.md; EVIDENCE_GRAPH_MODEL.md; CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md; FRESHNESS_ENGINE.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DISCLOSURE_BOUNDARY.md; ROUTE_GOVERNANCE.md
- **Reversal conditions:** RC rejection reverts the branch; a superseding DEC entry is required to change any of the 14 propositions or to move to published/active
- **Notes:**
  - **Append-only source discovery:** the 27 July 2026 EUR-Lex consolidated text (CELEX `02024R1689-20260727`) was added as a NEW source node `EP-SRC-000003` — a current-reading aid, NOT a replacement. `EP-SRC-000001`/`EP-SRC-000002` (the authentic Official Journal acts) are unchanged and remain the evidentiary basis. No historical source node was mutated.
  - **No manufactured history:** legacy prose held no `EP-CLM` identities; it is corrected forward, not reconstructed as superseded claims.
  - **Gate state:** publishable only. Not merged to `main`; `validity_state` remains `null`; no claim marked published/active; Article 111(4) deferred; EERS remains Candidate.
  - **Verification vs publication dates kept distinct:** human primary-source verification 2026-08-19; publication/freshness check 2026-08-20.
  - **RC.2 Final Release Preflight:** Clock marker positions recalibrated to the 2024–2028 visual scale (dates unchanged); `claims.json` registered as an alternate machine representation of EP-REG-001 in `routes.json`; `_meta.publish_gate` and DEC-045 Rationale aligned with release-state-then-merge semantics.
  - **Final Publication Release (2026-08-20):** RC.2 approved. Release-state transition authorized: 14/14 `publishable` → `published`, 14/14 `null` → `active`, `_meta.published: true`. No semantic Claim mutation. Release-state tree staged on the branch for atomic publication; public effectiveness begins when this exact release SHA is merged to `main`. Merge not yet authorized.

### DEC-046
- **Date:** 2026-08-20 (Post-Merge Live Verification — homepage derivative drift hotfix)
- **Status:** Active
- **Decision:** After merge of Final Publication Release (`1cc02e1` via merge commit `3322e6b`), Post-Merge Live Verification found the homepage Regulatory Clock Preview still displaying a pre-Omnibus AI Act timeline (incl. Aug 2027 / Art. 113.4) while `claims.json`, `/regulation/eu-ai-act/`, and `/clock/` were correct. Correct `index.html` only; do not reopen claim research. Adopt an architectural rule: any surface displaying Evidence Graph dates must derive from the canonical claim graph or be registered in `DERIVATIVE_SURFACE_REGISTRY.md` with a consistency check.
- **Rationale:** The defect is derivative drift between canonical truth and a hand-maintained preview — not a legal-proposition error. Closing the gate without a registry would allow the same class of failure on the next claim update.
- **Affected routes/files:** `index.html` (homepage clock preview); `DERIVATIVE_SURFACE_REGISTRY.md` (new); `EVIDENCE_GRAPH_MODEL.md` (v1.4 §10); `governance/audits/EU_AI_ACT_PUBLISH_GATE_2026-08-20.md` (Post-Merge section); `DECISION_LOG.md`
- **Governance documents involved:** EVIDENCE_GRAPH_MODEL.md; CLAIM_POLICY.md; REFERENCE_SOVEREIGNTY_DOCTRINE.md; DEC-045
- **Reversal conditions:** Superseding DEC entry required to retire the registry rule or to de-register a surface without removing the public timeline copy
- **Notes:**
  - **Not modified:** `claims.json`, any `EP-CLM-*`, source edges, `qualified_by`, `/regulation/eu-ai-act/`, `/clock/`
  - **Homepage AI Act lane** aligned to 2024–2028 scale and canonical phases; Aug 2027 removed; Article 5 exception (2 Dec 2026) mentioned in qualification text

### DEC-047
- **Date:** 2026-08-20 (Depth Equalization Program — Reference-Grade Route Standard v2 + Sprint R1)
- **Status:** Active
- **Decision:** (1) Housekeeping only: update `regulation/eu-ai-act/claims.json` `_meta` language from pre-merge “staged / effectiveness begins at merge” wording to **published / active — live on main since 2026-08-20**, retaining `release_sha` `1cc02e1…` and `merge_sha` `3322e6b…` as provenance. No claim proposition, workflow_state, validity_state, source, or `qualified_by` change. Does not reopen Publish Gate. (2) Adopt `REFERENCE_GRADE_ROUTE_STANDARD.md` v2.0 as mandatory for all indexable published routes: six layers (Identity & Scope; Primary Evidence; Unique Analytical Layer; Decision Utility; Machine & Citation; Maintenance Contract); hard-fail rejection criteria; moat test; Wave 1–3 Depth Equalization with **no new expansion** until Wave 1 Core Authority routes score ≥ 90/100. (3) Open Sprint R1 baseline audit in `governance/audits/REFERENCE_DEPTH_AUDIT_R1_2026-08-20.md`.
- **Rationale:** A sovereign reference asset cannot tolerate one gold regulation page beside peer-substitutable or summary-grade siblings. Depth must match ontology role, not word count. SEO follows information gain. Stale pre-merge `_meta` in the live claim graph is metadata debt, not a claim defect.
- **Affected routes/files:** `regulation/eu-ai-act/claims.json` (`_meta` only); `REFERENCE_GRADE_ROUTE_STANDARD.md` (new); `governance/audits/REFERENCE_DEPTH_AUDIT_R1_2026-08-20.md` (new); `GOVERNANCE_CHARTER.md`; `SCALING_AND_AUTOMATION_POLICY.md`; `ACCEPTANCE_CRITERIA.md`; `DECISION_LOG.md`
- **Governance documents involved:** REFERENCE_SOVEREIGNTY_DOCTRINE.md; EVIDENCE_GRAPH_MODEL.md; PAGE_BLUEPRINT_STANDARD.md; CONTENT_QUALITY_STANDARD.md; SEO_GOVERNANCE.md; DERIVATIVE_SURFACE_REGISTRY.md; DEC-045; DEC-046
- **Reversal conditions:** Superseding DEC required to lower the Wave 1 threshold, reopen expansion before Core Authority ≥ 90, or retire RGS v2
- **Notes:**
  - **Upgrade order (default):** GDPR → Data Act → CRA → EERS → Protocol → France → Germany → Netherlands → AI/SaaS → Horizon Europe
  - **Country Evidence IDs:** do not freeze `EP-CTR-CLM-*` until a country evidence model is designed
  - **Publish Gate:** remains CLOSED / PASS for EU AI Act v1

### DEC-048
- **Date:** 2026-08-20 (Sprint R2 — GDPR Evidence Graph-grade Upgrade opened)
- **Status:** Active
- **Decision:** Open Sprint R2 to upgrade `/regulation/gdpr/` (EP-REG-002) from structured summary toward Evidence Graph-grade reference under REFERENCE_GRADE_ROUTE_STANDARD.md v2. Sequence: source discovery → claim map/falsification → human verification → canonical `claims.json` → page transformation → Publish Gate → RGS re-score. No parallel Data Act/country/expansion work. No `EP-CLM-*` mint before literal falsification; next free ID is `EP-CLM-000015`. No HTML publish in R2.0. Correct RGS v2 post-R1 upgrade order line to include EERS and Protocol before France (consistency with Wave 1 / DEC-047; no score change).
- **Rationale:** R1 baseline shows AI Act at 97 and GDPR at 58. Depth equalization requires GDPR next, not expansion. Claim count must follow material truth for non-EU entry planning, not an AI Act template.
- **Affected routes/files:** `REFERENCE_GRADE_ROUTE_STANDARD.md` (upgrade-order consistency); `evidence-workbench/gdpr/*` (R2.0 discovery); `DECISION_LOG.md`
- **Governance documents involved:** REFERENCE_GRADE_ROUTE_STANDARD.md; EVIDENCE_GRAPH_MODEL.md; SOURCE_POLICY.md; CLAIM_POLICY.md; DISCLOSURE_BOUNDARY.md; DEC-047
- **Reversal conditions:** Superseding DEC to cancel R2 or to reopen expansion before Wave 1 ≥ 90
- **Notes:**
  - **R2.0 deliverables:** candidate source registry + claim candidates with exception flags; no `claims.json`; no GDPR page rewrite
  - **AI Act Gold Reference:** untouched except real freshness events

---

## 4. Superseded / Rejected Decisions

### REJ-001
- **Date:** Sprint 0A
- **Status:** Rejected
- **Decision rejected:** Combinatorial URLs such as /from/us-ai/to/germany/as/ai-provider/under/ai-act
- **Reason for rejection:** Produces ungovernable thin content at scale; cannot maintain source governance per page; dilutes canonical authority; creates index bloat
- **Replaced by:** DEC-006, DEC-007
- **Notes:** Permanently prohibited. See ROUTE_GOVERNANCE.md.

### REJ-002
- **Date:** Sprint 0B
- **Status:** Rejected
- **Decision rejected:** Generic consulting-site interface
- **Reason for rejection:** Contradicts Category Intelligence Factory identity; indistinguishable from thousands of European market-entry sites; destroys category claim
- **Replaced by:** DEC-013 (European Entry Control Room direction)
- **Notes:** Rejected at Sprint 0B design phase.

### REJ-003
- **Date:** Sprint 0B
- **Status:** Rejected
- **Decision rejected:** EU tourist/brochure aesthetic (maps, flags, stock European city images)
- **Reason for rejection:** Signals generic content rather than precision intelligence; audience expects institutional precision, not visual tourism
- **Replaced by:** DEC-013, DEC-014, DEC-015
- **Notes:** Rejected at Sprint 0B design phase.

### REJ-004
- **Date:** Sprint 0A
- **Status:** Rejected
- **Decision rejected:** Publishing matrix, diagnostic, or briefs before their dependencies are ready
- **Reason for rejection:** An incomplete matrix produces misleading cross-references. An ungoverned diagnostic produces ungoverned outputs. Premature publication degrades category authority.
- **Replaced by:** DEC-008 (diagnostic deferred), DEC-009 (matrix deferred), DEF-002 (/brief/ deferred)
- **Notes:** Permanent gate. Dependencies must be confirmed before each activation.

### REJ-005
- **Date:** Sprint 0A
- **Status:** Rejected
- **Decision rejected:** Low-quality ad monetization (display ads, undisclosed affiliate links) as a primary revenue path
- **Reason for rejection:** Contradicts intelligence model; signals commodity content; inconsistent with acquisition positioning as category infrastructure
- **Replaced by:** DEC-036, DEC-037
- **Notes:** Display advertising is not permanently prohibited for all time — it is prohibited as a primary path and in undisclosed form.

### REJ-006
- **Date:** Sprint 0A
- **Status:** Rejected
- **Decision rejected:** Unsupported official partnership or endorsement language with EU institutions or government bodies
- **Reason for rejection:** Material misrepresentation; legal and credibility risk; destroys trust of target audience
- **Replaced by:** DEC-019 (no unsupported partnership claims); standard institution disclaimer on all pages
- **Notes:** Permanent policy. Any formal partnership would require a separate disclosure decision.

---

## 5. Deferred Decisions

### DEF-001 — /diagnostic activation
- **Status:** Deferred
- **Decision deferred:** Activate /diagnostic as a live, indexed, interactive tool
- **Deferral reason:** Requires full EuraPlan Entry Planning Protocol implemented in an engine; all EERS dimensions governed; all regulatory exposure mappings Tier 1 sourced; diagnostic output governance layer built
- **Activation gate:** Separate activation decision recorded here; ACCEPTANCE_CRITERIA.md Section 5 must pass
- **Notes:** Route exists in routes.json as non-indexed. robots.txt disallows diagnostic query states.

### DEF-002 — /brief/ publication
- **Status:** Deferred
- **Decision deferred:** Publish pre-composed briefs under /brief/...
- **Deferral reason:** Briefs require confirmed real demand; unique intelligence not in reference layer; full Tier 1 sourcing; defined buyer profile; defined monetisation mechanism
- **Activation gate:** ACCEPTANCE_CRITERIA.md Section 4 must pass; separate decision recorded here for each brief
- **Notes:** Brief routes do not exist in routes.json or sitemap. Must not be created speculatively.

### DEF-003 — /matrix/ publication
- **Status:** Deferred
- **Decision deferred:** Publish /matrix/country-sector-regulation/ as a live, indexed page
- **Deferral reason:** Matrix requires regulation (4), country (3+), sector (2+), and funding (1+) dependencies to be complete before cross-reference is meaningful
- **Activation gate:** Dependency audit; separate activation decision recorded here; ACCEPTANCE_CRITERIA.md must pass
- **Notes:** Matrix content may be drafted internally. Route exists in routes.json as unpublished. Funding dependency (EP-FUND-001) now satisfied.

### DEF-004 — Multilingual expansion
- **Status:** Deferred
- **Decision deferred:** Publish any non-English public pages
- **Deferral reason:** English reference layer must be stronger before translation resources are committed. Translation quality gate and hreflang architecture require MULTILINGUAL_GOVERNANCE.md gating process.
- **Activation gate:** MULTILINGUAL_GOVERNANCE.md gating process; separate language activation decision recorded here
- **Notes:** Arabic owner-operator communications are internal and not subject to this deferral.

### DEF-005 — Additional country pages (Wave 2+)
- **Status:** Deferred
- **Decision deferred:** Add country pages beyond Germany, Netherlands, France
- **Deferral reason:** Country pages must be added by strategic waves, not alphabetically or all at once. Wave 2 country sequencing requires its own decision based on audience demand and regulatory stack readiness.
- **Activation gate:** Wave 2 country sequencing decision recorded here before any country page is created
- **Notes:** Candidates include Ireland, Sweden, Poland. No sequencing decision made.

### DEF-006 — Second sector page
- **Status:** Deferred
- **Decision deferred:** Publish second sector reference page
- **Deferral reason:** Second sector deferred until funding layer (Sprint 5A Horizon Europe) is delivered or a sector sequencing decision is separately recorded
- **Activation gate:** Sector sequencing decision recorded here; REFERENCE_CORPUS_GOVERNANCE.md Wave 2 prerequisites confirmed
- **Notes:** Candidate sectors: Cloud/Data Infrastructure, Connected Products/IoT — see DEC-031. Horizon Europe (EP-FUND-001) delivered Sprint 5A; second sector now eligible for sequencing decision.

### DEF-007 — Full interactive tooling
- **Status:** Deferred
- **Decision deferred:** Implement interactive diagnostic engine, protocol runner, or report generator
- **Deferral reason:** Public reference corpus must be stronger before interactive outputs are produced. Interactive tooling requires a Phase 3 architecture decision.
- **Activation gate:** Phase 3 architecture decision; separate tooling activation decision recorded here
- **Notes:** Phase 3 is not scoped in any current sprint document.

### DEF-008 — Monetised reports
- **Status:** Deferred
- **Decision deferred:** Publish or sell monetised intelligence reports
- **Deferral reason:** Diagnostic/report governance layer is not built. Revenue unit activation requires ACCEPTANCE_CRITERIA.md Section 8 to pass. Each report product requires a separate monetization decision.
- **Activation gate:** Diagnostic/report governance layer built; MONETIZATION_BOUNDARY.md updated; separate revenue unit decision recorded here
- **Notes:** Revenue candidates identified in DEC-037. None currently activated.

---

## 6. Future Decision Admission Rules

Any future major decision **must be recorded in DECISION_LOG.md before or during implementation** if it changes any of the following:

- Route architecture (new layers, new route types, new URL structures)
- Sitemap/indexation status (adding, removing, or changing indexed routes)
- Robots policy (disallowing or allowing previously controlled paths)
- Source policy (changing tier requirements, adding source types, deprecating sources)
- Claim policy (changing risk classifications, adding claim types, loosening restrictions)
- Interface thesis (changing the Control Room direction or any governed component)
- Visual identity (marks, colour tokens, typography system)
- Monetization model (adding revenue channels, activating deferred revenue units)
- Diagnostic/tooling behavior (activating, changing, or deprecating diagnostic functionality)
- Matrix publication (activating the matrix or changing its scope)
- Brief/report publication (activating or publishing any /brief/ route)
- Country expansion waves (adding any country beyond the Wave 1 trio)
- Sector expansion waves (adding any sector beyond AI/SaaS)
- Funding expansion (adding any funding programme)
- Multilingual expansion (activating any non-English language)
- Security posture (adding external scripts, APIs, or data flows)
- Analytics/indexation policy (adding tracking, changing indexation rules)
- Acquisition positioning (changing the buyer thesis or acquisition framing)

Minor decisions — fixing typos, updating last-updated dates, correcting broken links, adding accessibility attributes to existing tables — do not require a DECISION_LOG.md entry. Sprint records and commit history must still document them.

---

## 7. Change Control Rules

1. **Unique Decision ID** — Every major decision recorded here receives a unique DEC-NNN identifier. Rejected decisions receive REJ-NNN. Deferred decisions receive DEF-NNN.

2. **No silent reversals** — A decision recorded as Active cannot be removed. It must be marked Superseded, with a reference to the decision that replaced it and the rationale for the change.

3. **Reversals require rationale** — A superseding decision must document what changed, why, and which files and routes are affected.

4. **Superseded decisions remain visible** — They move to the Superseded/Rejected section with their full record intact. The audit trail must not be broken.

5. **Deferred decisions require explicit activation** — A deferred decision (DEF-NNN) cannot be implemented without a new Active decision (DEC-NNN) that references it and confirms the activation gate was cleared.

6. **Route decisions reference route governance** — Any decision affecting a public route must reference the relevant ROUTE_GOVERNANCE.md section and the routes.json entry.

7. **Monetization decisions reference monetization boundary** — Any decision activating a revenue channel must reference MONETIZATION_BOUNDARY.md and ACCEPTANCE_CRITERIA.md Section 8.

8. **Source decisions reference source and claim policies** — Any decision changing source requirements or claim permissions must reference SOURCE_POLICY.md and CLAIM_POLICY.md.

9. **Sequential numbering** — DEC IDs are assigned sequentially. Gaps are prohibited. If an entry must be removed, replace it with a \[REDACTED — see governance log\] placeholder stating the reason.

---

## 8. Relationship to Governance Documents

DECISION_LOG.md is the decision register. It does not replace the governing documents — it records the major decisions made under them.

| Governing Document | Role | Relationship to DECISION_LOG.md |
|---|---|---|
| GOVERNANCE_CHARTER.md | Asset identity and decision authority | Decisions authorized under this charter are recorded here |
| ROUTE_GOVERNANCE.md | URL architecture and route approval | Route architecture decisions (DEC-006, DEC-007, DEC-010) recorded here; route-level details in routes.json |
| SOURCE_POLICY.md | Source tier requirements | Source tier decisions (DEC-017, DEC-018) recorded here; per-source records in source tables and SOURCE_REGISTRY.md |
| CLAIM_POLICY.md | Claim risk classification | Claim policy decisions (DEC-019, DEC-020, DEC-021) recorded here; per-claim rules in CLAIM_POLICY.md |
| SEO_GOVERNANCE.md | Indexation discipline | Indexation decisions (DEC-011) recorded here; technical SEO rules in SEO_GOVERNANCE.md |
| INTERNAL_LINK_POLICY.md | Internal linking structure | Internal link policy changes recorded here; operational compliance in INTERNAL_LINK_POLICY.md |
| MONETIZATION_BOUNDARY.md | Revenue channels | Monetization decisions (DEC-036, DEC-037) and revenue unit activations recorded here; boundary rules in MONETIZATION_BOUNDARY.md |
| VISUAL_SYSTEM_GOVERNANCE.md | Colour tokens and visual design | Visual identity decisions (DEC-014, DEC-015) recorded here; design tokens and rules in VISUAL_SYSTEM_GOVERNANCE.md |
| INTERFACE_COMPONENT_POLICY.md | Interface component specifications | Interface direction decisions (DEC-012, DEC-013, DEC-016) recorded here; component specifications in INTERFACE_COMPONENT_POLICY.md |
| SCALING_AND_AUTOMATION_POLICY.md | Automation boundaries | Automation policy changes recorded here; operational rules in SCALING_AND_AUTOMATION_POLICY.md |
| ACCEPTANCE_CRITERIA.md | Publication gates | Decision log requirement added as Section 11 of ACCEPTANCE_CRITERIA.md |

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
*Governed by Sohadot | Established Sprint 4D — June 2026 | Updated Sprint 5B — June 2026*
