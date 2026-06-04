# ANALYTICS_AND_INDEXATION_POLICY.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, SECURITY_POLICY.md

---

## 1. Measurement Doctrine

EuraPlan measures what matters for the category claim: indexation health, query intent alignment, content quality signals, and audience composition. It does not measure engagement metrics that create perverse incentives to water down intelligence quality (time-on-page optimisation, bounce rate minimisation).

Measurement must not corrupt the asset. An analytics implementation that requires privacy trade-offs incompatible with SECURITY_POLICY.md is not permitted.

---

## 2. Primary Measurement Tool: Google Search Console

Google Search Console (GSC) is the primary intelligence tool for EuraPlan indexation and search performance monitoring. It requires no cookie or tracking script on the site — only a DNS or HTML verification token.

**What GSC monitors for EuraPlan:**
- Which pages are indexed
- Which queries drive impressions and clicks
- Core Web Vitals performance by page
- Mobile usability issues
- Coverage errors (4xx, 5xx, redirect chains)
- Sitemap submission status and coverage
- `hreflang` errors (when multilingual is added)

GSC must be connected at the time of first public deployment. Sitemap must be submitted immediately.

---

## 3. Secondary Analytics Tool

A privacy-respecting analytics tool may be added when the site has meaningful public traffic. Approved tool categories:

- Server-side analytics (no client-side script, no cookies): Preferred
- Privacy-first client-side analytics (Plausible Analytics, Fathom Analytics): Permitted after owner approval
- Google Analytics 4: Permitted only with a fully compliant cookie consent implementation and a documented privacy review

**Not permitted:**
- Any analytics tool that fingerprints users
- Any analytics tool that shares individual user behaviour with advertising networks
- Any analytics tool installed before a privacy review is completed

---

## 4. Indexation Monitoring

**What to monitor, in priority order:**

1. Are all published pages (`publication_status: published`, `sitemap: true` in routes.json) indexed by Google?
2. Are any draft or planned routes appearing in Google's index? (If so, investigate and resolve.)
3. Are any diagnostic query states (`/diagnostic?...`) indexed? (Must never be.)
4. Are coverage errors spiking after a deployment?
5. Are Core Web Vitals degrading on any page type?

**Monitoring cadence:**
- GSC check: weekly minimum once the corpus has > 10 published pages
- Coverage errors: reviewed after every deployment that adds or modifies routes
- Core Web Vitals: reviewed monthly and before each new corpus layer is published

---

## 5. Query Intent Monitoring

GSC provides query data (what search terms drive impressions and clicks). This data must be used to:

- Verify that published pages attract the intended audience queries
- Identify genuine intelligence gaps (queries for which EuraPlan has no page) that may justify a new governed route
- Identify query intent mismatches (pages attracting irrelevant queries, suggesting the page thesis needs refinement)

**What query data must NOT be used for:**
- Creating thin pages targeting every longtail keyword variant
- Adjusting content to serve query patterns that are off-category
- Optimising for impressions or clicks at the expense of intelligence quality

---

## 6. Content Quality Signals

From GSC and analytics, monitor:

- Average position by page (are reference pages ranking for their target queries?)
- Click-through rate by page (is the meta description accurately representing the content?)
- Pages with zero clicks after 60 days of indexation (potential quality or intent issue)

A page with zero clicks after 60 days must be reviewed: is the query intent accurate, is the meta description clear, is the page genuinely non-thin?

---

## 7. Diagnostic Data — Zero Collection Until Privacy Design Is Complete

When the Phase 3 `/diagnostic` tool is live:

- No user input data from the diagnostic may be logged, retained, or transmitted to any analytics tool without an approved privacy design document
- Diagnostic usage patterns (e.g., number of completions, most common entity types entered) may be tracked only in aggregate, never at individual session level, and only after the privacy design is approved
- This zero-collection default applies until explicitly overridden by an approved privacy design

---

## 8. Sitemap Monitoring

- Sitemap must be resubmitted to GSC after every change to route status or content
- GSC sitemap report must show no errors for any submitted URL within 30 days of submission
- Any URL submitted in the sitemap that returns a 4xx or 5xx error is a critical failure requiring immediate resolution

---

## 9. Privacy and Compliance

- Any analytics tool that sets cookies requires a cookie consent mechanism compliant with the EU ePrivacy Directive and GDPR for EU-resident visitors
- The preferred approach (server-side or cookieless analytics) avoids this requirement entirely
- EuraPlan does not display cookie consent banners in Phase 1 because no cookies are set
- If a cookie-setting analytics tool is introduced, a consent implementation must precede its activation

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
