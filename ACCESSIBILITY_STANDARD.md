# ACCESSIBILITY_STANDARD.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, TECHNICAL_STANDARD.md

---

## 1. Accessibility Target

EuraPlan targets WCAG 2.1 Level AA compliance for all public pages.

This is not only a legal obligation in many markets — it is a direct consequence of the asset thesis. A sovereign intelligence resource for European regulatory entry planning must itself meet European and international accessibility standards. Inaccessible intelligence is not sovereign intelligence.

---

## 2. Semantic HTML

- All pages use semantic HTML5 elements: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`
- One `<main>` element per page
- `<nav>` carries an `aria-label` to distinguish site navigation from page navigation
- Heading hierarchy: one `<h1>`, descending `<h2>` → `<h3>` — no skipped levels, no decorative headings used as dividers
- Lists use `<ul>`, `<ol>`, `<dl>` appropriately
- `<div>` and `<span>` are used only where no semantic element is appropriate

---

## 3. Keyboard Navigation

- All interactive elements (links, buttons, form inputs) are reachable and operable by keyboard
- Tab order follows document flow
- No keyboard traps — users can leave any element via Tab/Shift+Tab
- A skip-to-main-content link must appear as the first focusable element on every page:

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
```

```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: var(--yellow);
  color: var(--blue-deep);
  padding: 8px 16px;
  z-index: 1000;
  font-weight: 700;
}
.skip-link:focus { top: 0; }
```

---

## 4. Focus States

- All focusable elements have a visible focus indicator
- `outline: none` is prohibited on interactive elements unless a custom focus indicator is provided with equal visibility
- Focus indicator contrast ratio: at least 3:1 against the adjacent colour (WCAG 2.1 AA 1.4.11)
- The yellow (`--yellow: #e0c040`) focus ring on deep blue (`--blue-deep: #0b1c2c`) must be verified at implementation to meet the 3:1 threshold

---

## 5. Colour Contrast

| Element | Minimum Ratio | WCAG Criterion |
|---|---|---|
| Body text | 4.5:1 | 1.4.3 (AA) |
| Large text (> 18pt or 14pt bold) | 3:1 | 1.4.3 (AA) |
| UI components (borders, icons) | 3:1 | 1.4.11 (AA) |
| Focus indicators | 3:1 | 1.4.11 (AA) |

**Colour pairs in the EuraPlan design system that require verification at deployment:**
- `--white (#f2f5f8)` on `--blue-deep (#0b1c2c)` — expect pass at approximately 16:1
- `--grey-light (#b8c4d0)` on `--blue-deep (#0b1c2c)` — must verify; must not be used for small body text if ratio < 4.5:1
- `--yellow (#e0c040)` on `--blue-deep (#0b1c2c)` — must verify for small text usage
- `--grey-mid (#6a7a8a)` on `--blue-deep (#0b1c2c)` — expected marginal; must verify and limit to large text if < 4.5:1

---

## 6. No Information by Colour Alone

- Yellow deadline signals must always be accompanied by text indicating urgency, not colour alone
- Source confidence badges (Verified, Referenced, Pending, Deprecated) must carry text labels, not only colour
- Claim risk classifications (Low, Medium, High, Blocked) must carry text labels
- Link underlines must not be removed for body text links (colour alone cannot distinguish links from non-link text)

---

## 7. Reduced Motion

The following must be present in `main.css` before any animation or transition is introduced:

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 8. Table Accessibility

All HTML tables used for matrices and cross-reference data must include:
- `<caption>` describing the table purpose
- `<th scope="col">` for column headers
- `<th scope="row">` for row headers where applicable
- For complex tables (multi-level headers): `id` and `headers` attribute pairs on cells
- A screen-reader-readable summary paragraph before the table describing what the matrix shows

---

## 9. Future Form Accessibility (Phase 3 Diagnostic)

When the `/diagnostic` form is built:
- All inputs carry explicit `<label>` elements (not placeholder text as the only label)
- Error messages programmatically associated via `aria-describedby`
- Required fields indicated in text, not colour alone
- Form completion must be achievable by keyboard only
- Timeout warnings must be announced before data is lost
- `aria-live` regions used for dynamic diagnostic output

---

## 10. Accessible Disclaimers and Source Lists

- Disclaimers are visible HTML text — not hidden in CSS-only small print
- Minimum disclaimer font size: 12px (0.75rem)
- Disclaimers are readable without JavaScript
- `display: none` or `visibility: hidden` must not be applied to disclaimers that are categorically required
- Source lists carry appropriate heading structure (`<h2>Sources</h2>` or `<h3>`) so they are navigable by screen-reader users

---

## 11. Language and Direction

- `<html lang="en">` on all English pages
- When multilingual pages are added: `<html lang="fr">`, `<html lang="de">`, `<html lang="ar" dir="rtl">` etc.
- RTL layout for Arabic requires systematic CSS changes per MULTILINGUAL_GOVERNANCE.md
- Language switch links, when introduced, must be accessible by keyboard and carry `hreflang` attributes

---

## 12. Accessibility Testing Cadence

- Automated: axe-core or Lighthouse accessibility audit on every significant HTML change
- Manual: keyboard-only navigation test before every new page type is published
- Screen reader: NVDA or VoiceOver smoke test before each new corpus layer goes live
- Colour contrast: verified with a contrast checker at implementation (not assumed from design)

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
