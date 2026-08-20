# SEO_GOVERNANCE.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, ROUTE_GOVERNANCE.md

---

## 1. SEO Identity

EuraPlan does not pursue volume SEO. It pursues category authority SEO.

The objective is not to rank for every possible EU-related query. The objective is to be the dominant, most trustworthy, most structured reference in the category: European Regulatory Entry Planning.

This distinction is operational: it prohibits thin pages created to capture longtail keyword variants, and it demands deep, source-governed reference pages that earn category authority through intelligence quality, not content volume.

---

## 2. Prohibited SEO Patterns

| Prohibited | Reason |
|---|---|
| Thin pages targeting longtail keyword variants | Fails content quality standard, dilutes category authority |
| Combinatorial route explosion | Architecturally prohibited by ROUTE_GOVERNANCE.md |
| Duplicate intent pages | Two pages answering the same question compete internally and split authority |
| AI-generated bulk page creation without per-page governance review | Violates SCALING_AND_AUTOMATION_POLICY.md |
| Pages without official source support for their central claims | Violates SOURCE_POLICY.md |
| Generic "doing business in Europe" articles | Off-category and architecturally prohibited |
| Pages created to serve a keyword that does not serve the non-EU company planning audience | Off-category |
| Keyword stuffing in titles or descriptions | Destroys institutional credibility |

---

## 3. Technical SEO Requirements

Every public page must include:

| Element | Requirement |
|---|---|
| `<title>` | Unique, descriptive, < 60 characters, includes primary concept and EuraPlan |
| `<meta name="description">` | Unique, 140–160 characters, describes the intelligence value of the page |
| `<link rel="canonical">` | Present, matches route path in routes.json, trailing slash |
| Open Graph tags | `og:title`, `og:description`, `og:type`, `og:url` present |
| `<html lang="">` | Correct BCP 47 language code (`en` for primary layer) |
| Heading hierarchy | Single `<h1>` containing page thesis, descending `<h2>` structure |
| Structured data | JSON-LD block per STRUCTURED_DATA_POLICY.md |
| No duplicate `<title>` | Every page's title is unique across the corpus |

---

## 4. Title Standards

| Page Type | Title Format |
|---|---|
| Homepage | `EuraPlan — European Regulatory Entry Planning Intelligence` |
| Regulation page | `[Regulation Name] — EU Entry Planning Reference \| EuraPlan` |
| Country page | `[Country] Entry Planning for Non-EU Companies \| EuraPlan` |
| Sector page | `[Sector] EU Entry Planning \| EuraPlan` |
| Origin page | `European Entry Planning for [Origin] Companies \| EuraPlan` |
| Funding page | `[Programme Name] — EU Funding Reference \| EuraPlan` |
| Standard page | `[Standard Name] \| EuraPlan` |
| Brief | `[Specific Profile] EU Entry Brief \| EuraPlan` |

**Meta description requirements:**
- Must describe the intelligence value of the page, not marketing positioning
- Must include the target decision or problem the page resolves
- Must not duplicate another page's description
- Must not include unsupported claims

---

## 5. Sitemap Discipline

- `sitemap.xml` contains only routes where `sitemap: true` and `publication_status: published` in `routes.json`
- Updated with every route status change
- Diagnostic query states are never in `sitemap.xml`
- Draft and planned routes are never in `sitemap.xml`
- Submitted to Google Search Console after every structural update
- `lastmod` dates are accurate and updated when content changes — same-release rule: a substantive change to an indexable governed route updates that URL's `<lastmod>` in the same release; unrelated URLs are not bumped; `sitemap: false` alternates (e.g. claim graphs) stay out of the sitemap (see `SCALING_AND_AUTOMATION_POLICY.md` §11)

---

## 6. Index/Noindex Rules

| Route Type | `<meta name="robots">` | `robots.txt` |
|---|---|---|
| Published reference page | `index, follow` | Allow |
| Governance and source page | `index, follow` | Allow |
| Diagnostic entry point | `index, follow` | Allow |
| Diagnostic query states | `noindex` (meta) | Disallow |
| Draft routes | `noindex` | Disallow |
| Published brief | `index, follow` | Allow |
| Published matrix | `index, follow` | Allow |
| Draft matrix | `noindex` | Disallow |

---

## 7. Route Admission from SEO Perspective

A route may be admitted into the governed corpus for SEO purposes when:

- It targets a query intent that serves the non-EU company planning audience
- It has sufficient intelligence depth to be non-thin under CONTENT_QUALITY_STANDARD.md
- It does not duplicate the intent of an existing published route
- It has a confirmed Tier 1 or Tier 2 source basis for its central claims
- It fits within a governed corpus layer per REFERENCE_CORPUS_GOVERNANCE.md

---

## 8. Internal Linking from SEO Perspective

Internal linking must serve the authority architecture, not only navigation.

- Regulation pages must link to each other where regulatory scope overlaps
- Country pages must link to the most relevant regulations for their compliance context
- All deep reference pages link back to `/protocol/` and `/standard/eers/` to consolidate authority
- Orphaned pages (zero inbound internal links) are prohibited — an orphan is both an SEO and a governance failure
- Anchor text must be descriptive and match the destination thesis — not "click here" or "learn more"

---

## 9. Matrix and Diagnostic Indexation Rules

**Matrix pages:**
- Canonical URL (`/matrix/country-sector-regulation/`) is indexable when published with complete content
- Matrix content must be in HTML source, not JavaScript-rendered
- HTML `<table>` is required for matrix data

**Diagnostic:**
- `/diagnostic` entry point is indexable when the tool is live
- `/diagnostic?origin=us&sector=saas&country=de` and all query-state variants are never indexed
- Diagnostic context is never surfaced as indexed URL parameters
- Query states are disallowed in `robots.txt` and carry `<meta name="robots" content="noindex">`

---

## 10. Multilingual SEO (Future)

When multilingual pages are added:
- `hreflang` attribute must be implemented for all language variants of a page
- Each language version carries its own canonical URL (not a parameter: `/fr/regulation/eu-ai-act/` not `/regulation/eu-ai-act/?lang=fr`)
- All language versions are submitted to Google Search Console
- No language version is published without passing the full SEO governance checklist for that language
- See MULTILINGUAL_GOVERNANCE.md for full requirements

---

## 11. AI Agent and Crawler Readability

EuraPlan pages must be readable by both human visitors and AI agents (Googlebot, AI web crawlers, semantic search systems). Requirements:

- All core intelligence content in HTML source — never JavaScript-gated
- Clear heading hierarchy conveying page structure as an extractable outline
- HTML tables for cross-reference data (not CSS grid)
- Visible, inline source citations
- `<meta name="description">` matches the actual page content (no bait-and-switch)
- No cloaking — the same content served to crawlers and to users
- `robots.txt` must not accidentally block any published page

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
