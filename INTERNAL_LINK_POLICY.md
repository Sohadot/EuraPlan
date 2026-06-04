# INTERNAL_LINK_POLICY.md
**Version:** 1.0
**Status:** Active — Governing Document
**Asset:** EuraPlan.com
**Last Updated:** June 2026

---

## 1. Purpose

Internal links define the intelligence architecture of EuraPlan.com. They show both users and search engines the structural relationships between planning concepts, regulatory objects, and intelligence outputs.

This document governs how internal links are created, maintained, and required.

---

## 2. Link Architecture Principles

**Every page must link outward to at minimum two related governed routes.**
No page may be a dead end.

**Every new route must be linked to from at least one existing published route.**
No page may be an orphan.

**Links must be contextual, not navigational decoration.**
A link should appear because the destination content is directly relevant to the sentence or section it appears in — not because a rule says "add three links."

**Anchor text must be descriptive.**
Do not use "click here," "learn more," or "read this." Use the destination page thesis or a specific concept name.

---

## 3. Required Links by Page Type

### Reference Ontology Page
- Must link to: `/sources/` (source note)
- Must link to: `/governance/` (governance note)
- Must link to: at least one related regulation or concept page
- Must link to: `/enter/` or `/diagnostic` as the action path

### Intelligence Output Page (Clock, Matrix, EERS, Protocol)
- Must link to: `/sources/`
- Must link to: `/standard/eers/` or `/protocol/` (where relevant)
- Must link to: at least one regulatory or country reference page
- Must link to: `/enter/` or `/diagnostic`

### Governance and Source Pages
- Must link to: each other
- Must link to: `/` (homepage)
- May link to: specific content pages where the governance context is directly illustrated

### Acquisition Page (`/acquire/`)
- Must link to: `/standard/eers/`
- Must link to: `/protocol/`
- Must link to: `/clock/`
- Must link to: `/governance/`

---

## 4. Prohibited Internal Linking Patterns

- Linking to draft or unpublished routes
- Linking to `/diagnostic?...` query-state URLs
- Circular links that serve no user navigation purpose
- Links using generic anchor text ("here," "this," "page")
- Excessive internal linking that makes a page feel like a link farm

---

## 5. Link Maintenance

When a route is deprecated:
- All internal links pointing to that route must be updated to the redirect target
- The ROUTE_GOVERNANCE.md lifecycle must be followed

When a new route is added:
- At least one existing page must be updated to link to it
- The new page must link outward to at least two existing routes

---

## 6. Link Audit Cycle

- Full internal link audit at every major content update
- Broken link check every 3 months
- Any 404 detected must be resolved within 7 days

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
