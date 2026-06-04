# PERFORMANCE_BUDGET.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, TECHNICAL_STANDARD.md

---

## 1. Performance Identity

EuraPlan is a static-first reference asset. It must load fast because its audience — non-EU companies making high-stakes planning decisions — must be able to access its intelligence on any device, on any connection, without waiting for a runtime framework to initialise.

Performance is not an optimisation step added after build. It is an architectural constraint that governs every technical decision from the start.

---

## 2. Core Web Vitals Targets

Measurements taken with Lighthouse in mobile simulation (simulated 4G). Reference: Google Search Console Core Web Vitals report.

| Metric | Target | Maximum Permitted |
|---|---|---|
| LCP (Largest Contentful Paint) | < 1.5s | 2.5s |
| INP (Interaction to Next Paint) | < 100ms | 200ms |
| CLS (Cumulative Layout Shift) | < 0.05 | 0.1 |
| TTFB (Time to First Byte) | < 200ms | 800ms |

Any page exceeding the Maximum Permitted threshold for LCP or CLS must be resolved before that page is submitted to sitemap.

---

## 3. Page Weight Budget

| Asset Type | Target | Maximum |
|---|---|---|
| HTML per page | < 60KB | 100KB |
| CSS (shared stylesheet) | < 25KB uncompressed | 40KB |
| JavaScript (Phase 1) | 0KB | 0KB |
| JavaScript (Phase 2+ interactive tools) | < 30KB gzipped, async | 60KB gzipped |
| Web fonts (Phase 1) | 0KB (system fonts) | 0KB |
| Web fonts (Phase 2+, if approved) | < 25KB per file, WOFF2 | 50KB total |
| Images per page | < 100KB total | 200KB total |
| Total transfer (HTML + CSS + fonts) | < 100KB | 150KB |

---

## 4. CSS Budget

- Single shared stylesheet: `assets/css/main.css`
- Target size: < 25KB uncompressed
- No unused CSS rules — audit required before each new corpus layer deployment
- No CSS framework import without performance review and owner approval
- Custom properties for all repeated values (no literal color/size repetition)
- No `@import` inside CSS files — link stylesheet in HTML only

If `main.css` approaches 40KB, a critical CSS inlining strategy must be reviewed before continuing to add styles.

---

## 5. JavaScript Budget

**Phase 1:** Zero JavaScript. Every page is fully functional without JS.

**Phase 2+ (interactive tools, when approved):**
- All JavaScript loaded as `async` or `defer` — never blocking
- No JavaScript in `<head>` without `async`/`defer`
- Maximum 30KB gzipped per JS module
- No JavaScript framework without owner approval and performance review
- Progressive enhancement: the page must be readable and navigable before any JS executes

---

## 6. Font Rules

**Phase 1 — System fonts only:**

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
```

No external font requests. This eliminates font-loading render blocking entirely.

**Phase 2+ — If a custom web font is approved:**
- Maximum 2 files per typeface (Regular + Bold only)
- Format: WOFF2 only
- `font-display: swap` required
- Self-hosted — no Google Fonts or external font CDN
- Subset to Latin and Extended-Latin only (unless multilingual layer requires additional subsets)
- Each file < 25KB

---

## 7. Image Rules

- All images compressed before commit: target < 80KB per image
- Format: WebP preferred, JPEG for photographs, PNG for transparency
- All `<img>` elements carry explicit `width` and `height` attributes (prevents layout shift)
- `loading="lazy"` on all below-fold images
- No image used to convey regulatory data, dates, or matrix content — use HTML text and tables
- No decorative image > 20KB that adds no intelligence value

---

## 8. Animation Constraints

- No CSS animation that causes layout reflow
- No `transition` on paint-triggering properties (`box-shadow`, `filter`) without justification
- `prefers-reduced-motion` implemented for any animation before it ships:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

- No JavaScript-driven animation in Phase 1
- No WebGL, Canvas animation, or 3D unless approved by INTERFACE_COMPONENT_POLICY.md

---

## 9. Third-Party Resource Constraints

- No synchronous third-party scripts in `<head>`
- No external font CDN
- No analytics scripts that block rendering
- Any approved third-party resource audited for size and render-blocking impact before deployment
- SRI hash required on any resource loaded from a CDN

---

## 10. Layout Stability Rules

- All images and media carry explicit `width` and `height` in HTML
- `font-display: swap` used if web fonts are approved
- No content injected above the fold after initial page load
- No reserved ad slots — advertising is prohibited by MONETIZATION_BOUNDARY.md and would introduce CLS risk

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
