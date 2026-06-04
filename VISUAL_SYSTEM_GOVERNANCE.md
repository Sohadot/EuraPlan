# VISUAL_SYSTEM_GOVERNANCE.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md

---

## 1. Visual System Identity

The EuraPlan interface must feel like a European entry control room. Not a brochure about Europe. Not a consulting firm website. Not a news aggregator. Not a government portal.

Every visual decision must serve the intelligence. If a visual element does not advance the user's understanding of the planning intelligence it is displaying, it has no place on the page.

---

## 2. Colour System

All colours are defined as CSS custom properties in `:root` in `assets/css/main.css`. The visual system is not a collection of hex values — it is a semantic system where each colour has a defined role that cannot be violated.

| Token | Hex | Role | Restrictions |
|---|---|---|---|
| `--blue-deep` | `#0b1c2c` | Primary background. Institutional depth. | Never use as text colour. |
| `--blue-mid` | `#0f2236` | Card and panel backgrounds. | |
| `--blue-panel` | `#162d44` | Elevated panels and highlight cards. | |
| `--blue-border` | `#1e3a54` | Structural borders and dividers. | |
| `--white` | `#f2f5f8` | Primary text. Cold white. | |
| `--white-dim` | `#dce3ea` | Secondary text and quotes. | |
| `--grey-light` | `#b8c4d0` | Body text. Labels. | Verify contrast ratio — must meet 4.5:1 for body text. |
| `--grey-mid` | `#6a7a8a` | Metadata and de-emphasised labels. | Large text only if contrast < 4.5:1. |
| `--grey-dark` | `#344454` | Heavily de-emphasised elements. Footer text. | Decorative use only if contrast insufficient. |
| `--yellow` | `#e0c040` | European yellow — deadline and decision signals ONLY. | See Section 3. |
| `--font-ui` | system stack | Interface typography | See Section 5. |
| `--font-mono` | monospace stack | IDs, codes, regulation numbers | See Section 5. |

---

## 3. European Yellow — Strict Usage Rules

Yellow (`--yellow: #e0c040`) is a signal colour. It is not a brand colour and it is not a decorative colour.

**Permitted uses:**
- Regulatory deadline signals and date markers in the Clock
- Risk and warning indicators
- Active navigation indicator (underline only, not background)
- Focus ring outline
- Category label text (e.g., "Category: European Regulatory Entry Planning")

**Prohibited uses:**
- Background fills on large areas
- Decorative dividers or borders
- General heading text colouring
- Hover states on non-signal elements
- Any use where it appears as a brand or accent colour rather than an intelligence signal

The intent: when a user sees yellow on an EuraPlan page, they should understand immediately that it indicates a deadline, a decision point, or a planning signal. If yellow is overused, this meaning collapses.

---

## 4. Visual Grammar — Functional Elements

The interface uses functional visual grammar derived from the intelligence architecture. These elements are not decorative metaphors — they are functional representations of planning concepts.

| Element | What It Represents | Implementation |
|---|---|---|
| Clock | Regulatory deadline timeline | Timeline display; enforcement phases; yellow date markers |
| Gate | Compliance checkpoint | Entry/exit condition display; binary state (passed/not passed) |
| Matrix | Cross-reference of country × sector × regulation | HTML `<table>` with governed cell content |
| Pathway | Planning execution sequence | Numbered step list; 30/90/180-day structure |
| Signal | Risk indicator or opportunity marker | Yellow badge or indicator with text label |
| Readiness Layer | EERS dimension status display | Dimension-by-dimension status with text |

These elements are defined structurally in INTERFACE_COMPONENT_POLICY.md. The visual system must express them without making them decorative.

---

## 5. Typography

**Phase 1 — System fonts:**

```css
--font-ui: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
--font-mono: 'SF Mono', 'Fira Code', 'Cascadia Code', Consolas, monospace;
```

**Type scale (approximate):**
- `0.58–0.65rem` — labels, metadata, badges (uppercase, tracked)
- `0.78–0.88rem` — body text, table cells, step descriptions
- `0.95–1.05rem` — card titles, section descriptions
- `1.2–1.75rem` — section headings
- `1.9–3.2rem` (clamp) — hero and page headings

**Rules:**
- Monospace exclusively for: route IDs, regulation numbers, output IDs, code
- No display or script fonts in Phase 1
- No decorative ligatures or stylistic alternates in Phase 1
- Uppercase is used only for labels, eyebrows, and badges — not for body text

**Phase 2+ — If a custom web font is approved:**
- Must be an institutional sans-serif typeface (no playful, informal, or display-first typefaces)
- Performance requirements per PERFORMANCE_BUDGET.md apply

---

## 6. What the Interface Must Not Be

| Prohibited Visual Direction | Reason |
|---|---|
| EU flag aesthetic (12 stars repeated) | Implies official EU association not established |
| Generic consulting brochure layout (stock photography, hero image backgrounds) | Destroys category differentiation |
| Government portal aesthetic (institutional grey, bureaucratic layout) | Misrepresents the nature of the asset |
| Childish or gamification visual language | Inconsistent with the institutional intelligence identity |
| Heavy gradient backgrounds | Adds visual noise without intelligence value |
| Decorative animation as the primary visual interest | Distracts from planning intelligence |
| Social media card aesthetic | Wrong category signal |

---

## 7. Iconography Rules

- Phase 1: No icon fonts, no icon libraries (performance and accessibility risk)
- Icons, if introduced, must be inline SVG with accessible `aria-label` or `title` elements
- Icons must never be the sole carrier of meaning — text label always accompanies an icon
- No icon used purely decoratively without adding navigational or conceptual value
- No flag emoji or flag icons as national identifiers (use text country names)

---

## 8. Layout Principles

- Single-column content flow on mobile
- Maximum content width: `1060px` (`--max-content`)
- Grid layouts use `grid-template-columns: repeat(auto-fill, minmax(280px, 1fr))` or similar fluid patterns
- No fixed pixel layouts that break on non-standard viewports
- All interactive grid items have focus states and keyboard interaction
- Tables are horizontally scrollable on mobile within a container — not broken by viewport width

---

## 9. Visual Trust Requirements

The visual system must produce institutional trust at first glance. Specific requirements:

- The header wordmark must be visually dominant but restrained — not flashy
- Navigation must be clearly legible on all screen sizes
- Body text must be at a readable size without zooming on mobile (minimum effective 16px for body text)
- Source lists and disclaimers must be visually present, not hidden in near-invisible type
- No dark patterns — no visual manipulation of user attention toward unrelated commercial outcomes

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
