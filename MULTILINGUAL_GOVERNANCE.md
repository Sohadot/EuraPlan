# MULTILINGUAL_GOVERNANCE.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md, REFERENCE_CORPUS_GOVERNANCE.md

---

## 1. Language Doctrine

The primary language of EuraPlan.com is institutional English. This is not a default or a temporary state — it is a governing decision. The primary audience (non-EU AI, SaaS, tech, and compliance-sensitive companies) conducts international business planning in English.

Additional language layers may be added when they close a real intelligence gap for a specific audience segment. They are never added for SEO volume, translation practice, or to appear international.

Arabic is the owner-operator communication language. It is a candidate for a future content layer specifically for the GCC/MENA audience entering Europe, but that layer must be governed separately from owner-operator communications and must meet the same content quality standards as the English layer.

---

## 2. Language Priority Order

| Priority | Language | Rationale | Release Gate |
|---|---|---|---|
| 1 | English | Primary institutional layer | Complete (current) |
| 2 | French | EU institutional language; large French-speaking market; strong EuraPlan relevance for French-speaking African companies | Wave 3+ of corpus |
| 3 | German | Largest EU market; Germany is primary entry country for many non-EU companies | Wave 3+ |
| 4 | Arabic | GCC and MENA audience layer; owner-operator familiarity | Wave 4+ |
| 5 | Spanish | Latin American companies entering Europe | Wave 4+ |

No language layer is added before the English corpus reaches Wave 2 completion.

---

## 3. Language Layer Release Gates

Before a language layer may be published:

- The full English version of the page exists, is published, and has passed all quality gates
- A qualified human translator with regulatory and business planning expertise (not general translation) has reviewed the content
- All regulatory terminology has been translated with reference to the official translated EU regulation text in that language (EU regulations are published in all official EU languages on EUR-Lex)
- The EuraPlan regulatory terminology glossary for that language has been created and approved (see Section 7)
- `hreflang` implementation has been tested and validated
- The translated page passes the same CONTENT_QUALITY_STANDARD.md requirements as the English version

---

## 4. No Machine Translation Without Review

Machine translation tools (Google Translate, DeepL, AI translation APIs) may be used as a drafting aid only. They may never be published without:

- Full editorial review by a qualified human reviewer with EU regulatory domain knowledge
- Verification of all regulatory terminology against official EU sources in that language
- Confirmation that nuance and framing have not been flattened or distorted by the translation

A page that reads as machine-translated is a quality failure, regardless of technical accuracy.

---

## 5. URL Structure for Multilingual Pages

Multilingual pages use language-code path prefixes, not query parameters:

- English (primary): `/regulation/eu-ai-act/`
- French: `/fr/regulation/eu-ai-act/`
- German: `/de/regulation/eu-ai-act/`
- Arabic: `/ar/regulation/eu-ai-act/`

Query parameter approach (`/regulation/eu-ai-act/?lang=fr`) is prohibited. Each language version has its own canonical URL.

---

## 6. hreflang Implementation

When multilingual pages are added:

- All language versions of a page carry `<link rel="alternate" hreflang="[lang]" href="[url]">` for every language version, including `x-default` pointing to the English version
- `hreflang` tags are present in the `<head>` of every page in the language group
- `hreflang` values use BCP 47 language tags: `en`, `fr`, `de`, `ar`, `es`
- `hreflang` is validated before deployment using Google Search Console
- `x-default` is always the English version

---

## 7. Terminology and Glossary Consistency

Before any language layer is published:

- A terminology glossary for that language must be created, covering all EuraPlan-specific terms: regulatory clock, readiness standard, compliance gate, entry plan, funding readiness, etc.
- Each term must be translated consistently across all pages in that language layer
- Regulatory and legal terms must be translated with reference to the official EU translation: EU AI Act is "règlement sur l'intelligence artificielle" in French, "KI-Verordnung" in German — these are not invented; they are taken from official EUR-Lex publications
- Glossary is stored in the repository as `TERMINOLOGY_[LANGCODE].md`

---

## 8. RTL Considerations for Arabic

Arabic requires right-to-left (RTL) layout. Before the Arabic layer is published:

- The full CSS system must support `dir="rtl"` on the `<html>` element without layout breakage
- All flexbox and grid layouts must use logical CSS properties (`margin-inline-start` not `margin-left`) or RTL overrides
- Navigation must be reversed and verified in RTL mode
- Table layouts must be verified in RTL mode
- A dedicated RTL audit must be performed before publication

Arabic typography requirements:
- Arabic font must be specified and approved per PERFORMANCE_BUDGET.md font rules
- Arabic text must not be set in a Latin-default system font (system fonts for Arabic: use `system-ui` with the locale, or specify a named Arabic font)
- Line height and letter spacing must be reviewed for Arabic text

---

## 9. Language-Specific Source Requirements

Each language layer must cite sources that are:
- Official and authoritative for claims made in that language
- Where possible, the official EU translation of the regulation in that language (available on EUR-Lex for all official EU languages)
- Where national context is described (e.g., French regulatory enforcement practice), national official sources in that language are preferred

A French-language page on GDPR should cite the French CNIL (Commission Nationale de l'Informatique et des Libertés) for French regulatory implementation context, in addition to the EUR-Lex primary source.

---

## 10. Multilingual Quality Gate

A multilingual page must pass all of the following before publication:

- Full content quality standard per CONTENT_QUALITY_STANDARD.md, assessed in the target language
- Terminology glossary consistency verified
- `hreflang` implementation validated
- RTL audit completed (Arabic only)
- Human reviewer sign-off confirmed
- Regulatory terminology verified against official EUR-Lex translation
- Language-appropriate disclaimer present

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
