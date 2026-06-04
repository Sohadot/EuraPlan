# SECURITY_POLICY.md
**Version:** 1.0
**Status:** Active — Operating Governance
**Asset:** EuraPlan.com
**Last Updated:** June 2026
**Governed by:** GOVERNANCE_CHARTER.md

---

## 1. Asset Security Context

EuraPlan.com is a static reference asset. Its primary security surface is:
- Repository integrity (no secrets, no injection vectors)
- Third-party script trust (no uncontrolled external code execution)
- Future diagnostic and form data handling (no personal data collected without formal design)
- Reputational integrity (no false institutional claims, no supply-chain compromise)

EuraPlan does not currently collect user data, run server-side code, or handle payments. The security model is correspondingly minimal but must be formally governed before Phase 2 and Phase 3 introduce interactive capability.

---

## 2. Repository Rules

**Permanently prohibited in the repository:**
- API keys, access tokens, or credentials of any kind
- Private keys, certificates, or authentication secrets
- Personal data of any individual
- Database connection strings
- Environment variables embedded directly in source code
- `.env` files (must be in `.gitignore`)

`.gitignore` must exclude: `.env`, `*.pem`, `credentials.*`, `secrets.*`, `.DS_Store`, `node_modules/`.

---

## 3. Third-Party Script Policy

**Default position:** No third-party scripts without explicit owner approval.

**Approval requirements:**
- Business necessity documented
- Privacy impact assessed against ANALYTICS_AND_INDEXATION_POLICY.md
- Subresource Integrity (SRI) hash applied when loaded from a CDN
- Owner approval confirmed in writing

**Permanently prohibited without full privacy design:**
- Ad network scripts
- Unvetted affiliate tracking pixels
- Social media tracking scripts (Facebook Pixel, LinkedIn Insight Tag)
- Any script that transmits user behaviour data to a third party without explicit disclosure

---

## 4. Privacy Rules — Phase 1

EuraPlan Phase 1 collects no personal data.

- No cookies set by EuraPlan
- No form submissions
- No email capture
- No IP-level user tracking

Any analytics tool that sets cookies or fingerprints users requires a privacy review before deployment. Preferred: aggregated, server-side, or privacy-respecting tools (see ANALYTICS_AND_INDEXATION_POLICY.md).

---

## 5. Future Diagnostic Data Handling

The Phase 3 `/diagnostic` tool will accept structured user input. Before activation, all of the following must be completed:

- A formal privacy design document approved by the owner
- User input must not be logged or stored without explicit disclosure to the user
- No diagnostic input shared with third parties without consent
- Outputs are session-scoped, not stored against a user profile unless explicit account functionality is designed and GDPR-compliant
- GDPR Article 13/14 information obligations satisfied for EU-resident users

No diagnostic data handling may be implemented before this design is approved.

---

## 6. Future Form and Email Handling

Any email capture (newsletter, brief subscription) requires:
- Explicit opt-in mechanism
- A privacy notice identifying what data is collected and why
- A suppression/unsubscribe mechanism
- Data stored only for the stated purpose
- GDPR-compliant processor agreements if a third-party email service is used

---

## 7. Dependency Control

- No npm package or external library added without documented justification: purpose, version pinned, vulnerability status, licence
- Dependencies reviewed for known vulnerabilities at each major update cycle
- No dependency from an unmaintained repository (last commit > 24 months) without a documented exception
- Prefer zero-dependency or minimal-dependency implementations for Phase 1

---

## 8. Security Headers

When EuraPlan is served via Cloudflare Pages or an equivalent CDN/edge provider, configure:

| Header | Value |
|---|---|
| `Content-Security-Policy` | Strict — allow self and explicitly approved external sources only |
| `X-Content-Type-Options` | `nosniff` |
| `X-Frame-Options` | `SAMEORIGIN` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | Restrict camera, microphone, geolocation |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains` |

Content-Security-Policy must be reviewed whenever a new third-party resource is added.

---

## 9. Supply-Chain Caution

- Do not load fonts, icons, or libraries from third-party CDNs unless there is a documented reason and SRI hash protection
- Prefer self-hosted assets
- Phase 1 approved default: no external CDN dependencies — all assets served from repository
- Any third-party integration introduced in Phase 2+ requires a dependency review against this policy

---

## 10. Incident Response

If a security issue is identified (secret committed, data exposed, script injection detected):

1. Remove compromised content from repository immediately
2. Rotate any exposed credentials immediately
3. Assess what was exposed and to whom
4. Document the incident in owner private communications
5. If personal data was exposed, assess GDPR notification obligations (72-hour window under GDPR Article 33)
6. Review and update this policy if the incident reveals a governance gap

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
