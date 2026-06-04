# TECHNICAL_STANDARD.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md

---

## 1. Architecture Principle

EuraPlan.com is a static-first, HTML-first reference corpus.

The architecture must allow a non-EU company visiting `/regulation/eu-ai-act/` to read the full regulatory planning reference without executing any JavaScript. Every page is a document. The architecture serves the document.

This is a category signal, not a technical limitation. A sovereign intelligence asset for European regulatory entry planning must be structurally trustworthy: stable, crawlable, readable, performant, and not dependent on client-side runtime to deliver its intelligence.

---

## 2. HTML Standard

- Every public page is an `.html` file served as static content
- All core intelligence content must be in the HTML source, not JavaScript-rendered
- Pages use semantic HTML5 elements: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`, `<table>`, `<figure>`, `<blockquote>`
- Heading hierarchy: one `<h1>` per page, descending `<h2>` → `<h3>` → `<h4>`, no skipped levels
- HTML tables must be used for tabular data — not CSS grid layouts for cross-reference matrices
- All images carry descriptive `alt` attributes
- Internal links use root-relative paths: `/clock/` not `../clock/`
- External links to official sources carry `rel="noopener noreferrer"` and `target="_blank"`

---

## 3. CSS Standard

- Single shared stylesheet: `assets/css/main.css`
- All design tokens defined as CSS custom properties in `:root`
- No inline `style` attributes except dynamic layout values that cannot be expressed as a class
- No `!important` declarations
- Mobile-first media queries only
- No CSS framework imports (Bootstrap, Tailwind, etc.) without performance review and owner approval
- Visual system is defined in `VISUAL_SYSTEM_GOVERNANCE.md` — CSS must implement it

---

## 4. JavaScript Standard

**Phase 1 target:** Zero JavaScript. All pages function completely without JS.

**When JavaScript is permitted:**
- Only when a required interaction cannot be achieved with HTML/CSS alone
- Only as progressive enhancement — the page must be complete without it
- Only when performance budget in `PERFORMANCE_BUDGET.md` is not exceeded
- Only after owner approval
- Never in `<head>` as a synchronous blocking script

**Permanently prohibited:**
- JavaScript frameworks (React, Vue, Angular, Svelte) without owner approval
- JavaScript that hides, generates, or replaces core page content
- JavaScript-only navigation or routing
- Inline event handlers in HTML attributes

---

## 5. File Structure

```
/
├── index.html
├── assets/
│   ├── css/main.css
│   └── js/  (Phase 2+ only, when approved)
├── enter/index.html
├── clock/index.html
├── standard/eers/index.html
├── protocol/index.html
├── sources/index.html
├── governance/index.html
├── acquire/index.html
├── regulation/[slug]/index.html       # Sprint 1+
├── country/[slug]/index.html           # Sprint 1+
├── sector/[slug]/index.html            # Sprint 1+
├── origin/[slug]/index.html            # Wave 2+
├── funding/[slug]/index.html           # Sprint 1+
├── matrix/country-sector-regulation/index.html
├── brief/[slug]/index.html             # Phase 2, on demand
├── robots.txt
├── sitemap.xml
└── routes.json
```

No file may be created outside this structure without route governance approval.

---

## 6. Canonical URL Policy

- Every page carries `<link rel="canonical" href="https://euraplan.com[path]/">` in `<head>`
- Canonical always uses trailing-slash directory-index form
- Canonical is always the primary domain (`euraplan.com`), never a staging or branch URL
- Canonical must match the route path in `routes.json`

---

## 7. Trailing Slash Policy

- All page routes use trailing slashes: `/enter/`, `/clock/`, `/standard/eers/`
- Homepage canonical is `https://euraplan.com/`
- All internal links use root-relative trailing-slash paths
- Route IDs in `routes.json` record paths with trailing slashes

---

## 8. Route Registry Discipline

- `routes.json` is the single source of truth for all routes
- No HTML page may be created without a corresponding entry in `routes.json`
- No page moves to `publication_status: published` without all required `routes.json` fields completed
- `sitemap.xml` must reflect exactly the routes where `sitemap: true` and `publication_status: published`

---

## 9. Sitemap Discipline

- `sitemap.xml` is generated from `routes.json` entries with `sitemap: true` and `publication_status: published`
- Submitted to Google Search Console on every structural update
- Diagnostic query states (`/diagnostic?...`) are never included
- Draft and planned routes are never included
- `lastmod` dates in `sitemap.xml` are accurate and updated on content change
- Sitemap is validated after every push that changes route status

---

## 10. Build and Deploy Assumptions

- Phase 1: Static HTML served from repository root via GitHub Pages or Cloudflare Pages
- No server-side rendering required in Phase 1
- No build step required — HTML authored directly
- Phase 2/3 may introduce a static site generator (SSG) if volume justifies it — requires separate technical review
- Any SSG introduced must produce HTML-first output satisfying sections 2–6 of this standard

---

## 11. Failure Conditions

The following require resolution before publication:

- Core page content is inside JavaScript-rendered markup
- A page exists without a `routes.json` entry
- A page has no `<link rel="canonical">`
- `sitemap.xml` includes a draft or planned route
- A CSS framework is imported without performance review and approval
- A synchronous third-party script appears in `<head>`
- Heading hierarchy is broken (multiple `<h1>`, non-sequential levels)
- Internal links use relative paths instead of root-relative paths
- A matrix uses CSS grid layout instead of HTML `<table>` for its data

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
