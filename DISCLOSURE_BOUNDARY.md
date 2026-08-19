# DISCLOSURE_BOUNDARY.md
**Version:** 1.0
**Status:** Active — Governing Document
**Asset:** EuraPlan.com
**Last Updated:** August 2026
**Governed by:** GOVERNANCE_CHARTER.md, SECURITY_POLICY.md, REFERENCE_SOVEREIGNTY_DOCTRINE.md

---

## 1. The governing principle

> **Public repository = public disclosure boundary.**
>
> Anything committed to `Sohadot/EuraPlan` is presumed **public and permanently
> disclosable**. Before any commit, assume a competitor, researcher, prospective
> buyer, journalist, or crawler will read it.

This is not only about technical secrets (keys, tokens, credentials). It is about
**any** file or information we would not want the public to have. The remedy is not
to hide such material inside the public repository — it is to keep it **out of the
repository entirely**.

### The pre-commit test

> Before committing a file, ask: *"Could this be published on the open internet
> tomorrow with no strategic or privacy harm?"* If the answer is **no**, it does not
> enter this repository at all.

This does not conflict with the transparency the asset is built on. Transparency
means that what we claim is public and auditable genuinely **is** — it does not mean
disclosing operational intellectual property or private information the public does
not need.

---

## 2. Three content classes

| Class | Belongs in the public repo? | Examples |
|---|---|---|
| **Public governance** | Yes — being public raises credibility | `SOURCE_POLICY`, `CLAIM_POLICY`, `EVIDENCE_GRAPH_MODEL`, `EERS` specification, provenance methodology, this document |
| **Public evidence / data** | Yes — deliberately auditable | verified claims, source registry, datasets, public changelog, verification audit records intended for open scrutiny |
| **Private operational intelligence** | **No — never** | buyer dossiers, commercial strategy, unpublished pricing, outreach lists, negotiations, acquisition valuations, notes on named companies, customer data / Entry Profiles, paid client reports, unreleased deal intelligence, sensitive drafts, internal weaknesses, credentials |

Classes 1 and 2 are the asset's **public intellectual record**. Class 3 lives in a
**separate private space** (a private repository or a store outside public GitHub),
and never in this repository — not in any file, not in any branch.

---

## 3. Hard rules

1. **A non-`main` branch is not private space.** Every branch of a public repository
   is readable. Do not use a feature branch as a place to stage confidential material.
2. **Deletion is not removal.** Removing a file in a later commit does not erase it
   from Git history. If confidential information has already been committed, it may
   require a history rewrite; if it is a technical secret, it also requires
   **rotation** (assume it is compromised).
3. **`robots.txt` is not an access control.** `Disallow` stops compliant crawlers
   only; the file remains directly fetchable. Never rely on it to keep anything
   private.
4. **"Unpublished on the site" ≠ "secret."** Working evidence that is not yet on the
   public pages is still public if it is in the repo. Name such folders honestly
   (see §4) — do not label public working material as "internal."

---

## 4. Naming honesty

The current `internal/` folder is a **misnomer**: its contents (a verification audit
record and the draft claims registry) are already publicly reachable and are, by
design, public working evidence — not secrets. The name wrongly implies privacy.

- Public working material that is not yet on the site SHOULD live under an honest,
  clearly-public name — e.g. `governance/audits/` for audit records and
  `evidence-workbench/` (or `review/`) for pre-publication claim registries.
- Truly private material does not get a folder here at all — it goes to the separate
  private space (§2).

Renaming `internal/` is a naming-honesty task, not a security fix, because nothing
currently under it is confidential.

---

## 5. This document is public by design

`DISCLOSURE_BOUNDARY.md` is Class 1 (public governance). Publishing the boundary
itself is a trust signal: it tells researchers and buyers exactly what the public
record does and does not contain, and commits the asset to keeping that promise.

---

*EuraPlan.com — European Regulatory Entry & Expansion Planning Intelligence*
*Asset owned by Sohadot | agent@sohadot.com*
