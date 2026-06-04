# STRUCTURED_DATA_POLICY.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, SEO_GOVERNANCE.md

---

## 1. Purpose

Structured data makes EuraPlan pages readable as typed, structured knowledge by search engines and AI agents — not just raw text. This policy governs which structured data types are used, how they are implemented, and what is prohibited.

---

## 2. Implementation Method

- All structured data implemented as JSON-LD in the `<head>` of each page
- No Microdata or RDFa (JSON-LD only)
- JSON-LD blocks validated against schema.org before deployment
- One primary JSON-LD block per page; additional blocks for BreadcrumbList and secondary types
- JSON-LD content must accurately reflect the visible page content — no bait-and-switch

---

## 3. Approved Schema Types by Page Type

| Page Type | Primary Schema | Secondary Schema |
|---|---|---|
| Homepage | `WebSite` | `Organization` |
| Regulation reference page | `Article` | `BreadcrumbList` |
| Country reference page | `Article` | `BreadcrumbList` |
| Sector reference page | `Article` | `BreadcrumbList` |
| Origin reference page | `Article` | `BreadcrumbList` |
| Funding reference page | `Article` | `BreadcrumbList` |
| Matrix page | `Dataset` | `BreadcrumbList` |
| Brief | `Article` | `BreadcrumbList` |
| Standard page | `Article` | `BreadcrumbList` |
| Protocol page | `Article` | `BreadcrumbList` |
| Source / Governance pages | `WebPage` | `BreadcrumbList` |
| Acquisition page | `WebPage` | — |

---

## 4. Required Open Graph and Meta Tags

Every page must include in `<head>`:

```html
<meta property="og:title" content="[page title]">
<meta property="og:description" content="[page description]">
<meta property="og:type" content="website"> <!-- or "article" for reference pages -->
<meta property="og:url" content="https://euraplan.com/[path]/">
<meta property="og:site_name" content="EuraPlan">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="[page title]">
<meta name="twitter:description" content="[page description]">
```

---

## 5. Organization Schema (Homepage Only)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "EuraPlan",
  "url": "https://euraplan.com",
  "description": "European Regulatory Entry and Expansion Planning Intelligence",
  "contactPoint": {
    "@type": "ContactPoint",
    "email": "agent@sohadot.com",
    "contactType": "Business Enquiries"
  }
}
```

**Prohibited in Organization schema:**
- `sameAs` links to EU institutions (implies association not established)
- `award` or `certification` fields
- `memberOf` fields for institutional bodies
- `foundingDate` unless accurate

---

## 6. Article Schema (Reference Pages)

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[page title]",
  "description": "[page description]",
  "author": {
    "@type": "Organization",
    "name": "EuraPlan",
    "url": "https://euraplan.com"
  },
  "publisher": {
    "@type": "Organization",
    "name": "EuraPlan",
    "url": "https://euraplan.com"
  },
  "dateModified": "YYYY-MM-DD",
  "url": "https://euraplan.com/[path]/",
  "inLanguage": "en"
}
```

`dateModified` must match the Last Updated date visible on the page. These two values must never diverge.

---

## 7. BreadcrumbList Schema (All Inner Pages)

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "EuraPlan",
      "item": "https://euraplan.com/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "[Section label]",
      "item": "https://euraplan.com/[section]/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "[Page label]",
      "item": "https://euraplan.com/[path]/"
    }
  ]
}
```

---

## 8. Prohibited Schema Uses

| Prohibited | Reason |
|---|---|
| `AggregateRating` on any page | No legitimate review or rating system exists |
| `Review` or `UserReview` | EuraPlan does not aggregate user reviews |
| `Certification` or external validation schema | No external certification has been obtained |
| `GovernmentOrganization` type | EuraPlan is a private intelligence asset |
| `sameAs` linking to EU institutions | Implies formal association not established |
| `FAQPage` schema without genuine visible Q&A | Structured data must match visible content |
| `JobPosting` | Off-category |
| `SpeakableSpecification` | Requires audio interface design not yet approved |

---

## 9. Dataset Schema (Matrix Pages)

When a matrix page contains structured cross-reference data, Dataset schema may be used:

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "[Matrix title]",
  "description": "[What the matrix maps]",
  "url": "https://euraplan.com/matrix/[slug]/",
  "publisher": {
    "@type": "Organization",
    "name": "EuraPlan",
    "url": "https://euraplan.com"
  },
  "inLanguage": "en",
  "dateModified": "YYYY-MM-DD"
}
```

---

## 10. Internal Ontology Metadata

EuraPlan pages may use `data-*` HTML attributes for internal ontology and tooling purposes:

- `data-ep-route-id="EP-R-003"` on `<main>` — matches routes.json route_id
- `data-ep-corpus-layer="1"` on `<main>` — corpus layer per REFERENCE_CORPUS_GOVERNANCE.md
- `data-ep-regulation="EU-2024-1689"` — applicable regulation identifier
- `data-ep-audience="L1"` — primary audience layer
- `data-ep-last-updated="YYYY-MM-DD"` — machine-readable update date

These attributes are not indexed by search engines. They support future diagnostic, automation, and API tooling.

---

## 11. Structured Data Validation

- All JSON-LD blocks validated with Google's Rich Results Test before deployment
- No validation errors permitted before publishing
- `dateModified` in JSON-LD must match the visible Last Updated date on the page
- BreadcrumbList paths must match actual route paths in routes.json

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
