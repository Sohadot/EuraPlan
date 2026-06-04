# CONTENT_QUALITY_STANDARD.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, CLAIM_POLICY.md, SOURCE_POLICY.md

---

## 1. Quality Standard Identity

EuraPlan is a Category Intelligence Factory. Its pages are reference documents, not articles.

The quality standard is not "well-written blog post." It is "authoritative regulatory planning reference that a non-EU company's legal, compliance, or strategy team can use to frame real decisions before entering Europe." That requires precision, source discipline, and editorial integrity at every level of the corpus.

---

## 2. Required Page Elements

Every public page must contain all of the following before publication:

| Element | Standard |
|---|---|
| Page Thesis | One sentence stating the intelligence this page delivers. No vague category descriptions. |
| Target Audience | Named specifically. "Non-EU SaaS companies facing EU AI Act and GDPR simultaneously" — not "companies interested in Europe." |
| Decision Problem | The specific planning question this page resolves. Must be a question a real company would ask. |
| Produced Intelligence Output | What the reader knows, understands, or has access to after reading. Must be concrete. |
| Last Updated Date | Present in page. No undated pages in the corpus. |
| Source Citations | All regulatory, compliance, funding, and statistical claims cite Tier 1 or Tier 2 sources inline. |
| Source Confidence Level | Assigned per SOURCE_POLICY.md: Verified, Referenced, or Pending. |
| Claim Risk Level | Assigned per CLAIM_POLICY.md: Low, Medium, High, or Blocked. |
| Disclaimer | Planning intelligence disclaimer on all pages with regulatory or compliance content. |
| Internal Links | Minimum two outward, minimum one inbound. |
| Canonical URL | Present in `<head>`. Matches routes.json entry. |

---

## 3. Prohibited Content Patterns

| Prohibited | Reason |
|---|---|
| Generic "doing business in Europe" content | Off-category |
| Legal advice framing ("you must comply by doing X") | Liability and governance violation |
| Penalty figures without citing the specific regulation article | Source policy violation |
| Funding amounts stated as guaranteed | Source policy violation |
| Fabricated statistics or percentages without an official source | Source policy violation |
| "Coming soon", "to be added", "check back later" | Thin content violation |
| Placeholder section headings with no content | Thin content violation |
| Partnership or endorsement claims not formally documented | Claim policy violation |
| Regulatory dates stated without the regulation number and article | Source policy violation |
| Implied universality ("every company must...") without qualifying conditions | Claim risk violation |
| Comparative product or service recommendations | Off-category, liability risk |
| Out-of-date regulatory content left uncorrected after an enforcement date passes | Source review failure |

---

## 4. Source Requirements by Claim Type

| Claim Type | Minimum Source | Confidence Level |
|---|---|---|
| A regulation applies to entity type X | Tier 1 — specific regulation and article | Verified |
| Regulatory deadline or enforcement date | Tier 1 — regulation article that establishes the date | Verified |
| Funding programme available for sector X | Tier 1 — official programme documentation | Verified |
| Country is viable entry target for sector X | Tier 2 — institutional reference | Referenced |
| Compliance step is typically required | Tier 1 — regulation text or official agency guidance | Verified |
| General market context (unquantified) | Low risk — no external source required for general framing | Low |
| Market size or penetration data | Tier 2 minimum — OECD, IMF, Eurostat, World Bank | Referenced |

---

## 5. Audience-Layer Writing Rules

EuraPlan's primary audience is non-EU AI, SaaS, tech, and compliance-sensitive companies. Secondary audiences include lawyers, investors, government officials, analysts, and students.

**Rules:**

- Lead with the planning problem, not the regulatory background
- Explain regulatory concepts at the level of a senior business decision-maker, not a specialist lawyer
- Define EU regulatory acronyms on first use: `GDPR (General Data Protection Regulation)`
- Explain institutional references briefly on first mention: "EUR-Lex, the EU's official law publication portal"
- Do not assume the reader knows EU institutional structure
- Do not simplify to the point of inaccuracy — precision is a quality criterion
- Do not pad with context the primary audience already has — every sentence must add planning value
- Do not write for a general European audience — write for a company approaching Europe from outside it

**Audience layer markers (internal governance use):**
- `[L1]` Primary planning audience (non-EU companies)
- `[L2]` Secondary professional audience (lawyers, advisors, analysts)
- `[L3]` General public and student audience

Sprint 1 reference corpus: L1/L2. L3 expansion governed by REFERENCE_CORPUS_GOVERNANCE.md Wave 3+.

---

## 6. Ordinary Reader Accessibility

Institutional quality must not mean inaccessibility to a general public reader who arrives via search.

- Every regulation page must open with a paragraph that a non-specialist can understand
- Technical terms must be followed by a plain-language explanation in parentheses or the following sentence
- Acronyms expanded on first use
- No assumption of prior knowledge of EU institutional structure

Accessibility to an ordinary reader is required alongside accuracy for a specialist reader. These are not competing requirements — they are both quality requirements.

---

## 7. Update and Review Cycle

- All pages carry a `Last Updated` date
- Regulation reference pages reviewed when: (a) a regulation they cite is amended; (b) an enforcement date passes; (c) official guidance changes
- Six-month rolling review for all pages with regulatory content
- Deprecated content updated or removed within 30 days of becoming outdated
- Review logged in git commit history with triggering event identified
- If a source is removed from its official location, the claim it supported must be re-verified or removed

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
