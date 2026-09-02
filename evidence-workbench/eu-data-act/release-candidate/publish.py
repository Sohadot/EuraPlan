#!/usr/bin/env python3
"""EU Data Act Publish Gate — derive the live production tree from the reviewed candidates.

Reads the reviewed release-candidate (claims.json + index.html) and writes:
  ../../../regulation/eu-data-act/claims.json   (published/active public machine graph)
  ../../../regulation/eu-data-act/index.html    (indexable live page)

Publication-state transforms ONLY. Claim IDs, prose, source edges, provision locators,
qualified_by, related_claims, co_render_blocking_pairs, EERS mapping, claim_risk,
last_verified_at and source-registry substance are carried over unchanged.
No provenance SHAs (release_sha/merge_sha/live_on_main_since) are invented pre-merge.
"""
import json, re, copy, os

PUB_DATE = "2026-09-02"  # publication dateModified / sitemap lastmod (update at merge if the date moves)
HERE = os.path.dirname(os.path.abspath(__file__))
LIVE = os.path.normpath(os.path.join(HERE, "..", "..", "..", "regulation", "eu-data-act"))

# ---------- 1. public claims.json ----------
rc = json.load(open(os.path.join(HERE, "claims.json")))
rc_claims = rc["claims"]

pub_claims = []
for c in rc_claims:
    p = copy.deepcopy(c)
    assert p["workflow_state"] == "publishable" and p["validity_state"] is None
    p["workflow_state"] = "published"
    p["validity_state"] = "active"
    pub_claims.append(p)

pub_meta = {
    "batch": "EU Data Act - canonical claim graph (Data Act v1; published / active)",
    "status": ("published / active - canonical claim graph for the EU Data Act reference route (EP-REG-003). "
               "87/87 claims workflow_state=published; validity_state=active; verified against the pinned Official "
               "Journal source (EP-SRC-000006) read with its corrigendum. No claim text, ID, source edge, "
               "qualified_by, related_claims, co_render_blocking_pairs, EERS mapping, claim_risk or last_verified_at "
               "changed at publication."),
    "location_note": ("regulation/eu-data-act/claims.json - canonical machine-readable claim graph for the EU Data Act "
                      "reference route (EP-REG-003). Mirrors the visible Verified Claim Register on /regulation/eu-data-act/."),
    "published": True,
    "route_id": "EP-REG-003",
    "schema_version": rc["_meta"]["schema_version"],
    "claim_count": 87,
    "id_range": "EP-CLM-000046..EP-CLM-000132",
    "co_render_blocking_pairs": rc["_meta"]["co_render_blocking_pairs"],
    "excluded_source_constrained": rc["_meta"]["excluded_source_constrained"],
    "embedded_unminted_qualifiers": rc["_meta"]["embedded_unminted_qualifiers"],
    "governed_by": rc["_meta"]["governed_by"],
    "notes": [
        "Assembled from the EU Data Act human-literal verification (87/87 human-verified against the primary source) and "
        "the R3.1-F Q1-Q16/N1-N7 constraint audit. Claim prose is EuraPlan's plain-language proposition (not a verbatim "
        "quotation of the act); provision_locator is the exact Article/paragraph.",
        "Source edges use only supports/amends/clarifies. The corrigendum EP-SRC-000007 affects Article 48 only and "
        "amends/clarifies none of these 87 claims, so it carries no per-claim edge; it is retained in source_registry as "
        "the corrigendum read with the authentic act, with no effect on any claim.",
        "Claim->Claim relations: qualified_by only for a claim that narrows/excepts/conditions another; structural "
        "adjacency is related_claims; anti-waiver and applicability boundaries that accompany a right without narrowing "
        "its truth are co_render_blocking_pairs.",
        "claim_risk per CLAIM_POLICY v1.1: Low only for bibliographic instrument identity; all legal applicability/scope, "
        "compliance, right/restriction, exemption-with-effect and deadline claims are High (Tier-1 basis EP-SRC-000006).",
        "EERS dimensions per EERS_1.0 (multiple allowed): DIM-01 identification/scope/actor; DIM-02 timing; DIM-04 "
        "entity/representation/establishment; DIM-06 concrete product/service requirements; DIM-07 enforcement/penalty exposure.",
        "Index control: exact-path X-Robots-Tag: noindex on /regulation/eu-data-act/claims.json (CDN index-control doctrine). "
        "routes.json indexable:false is governance metadata only; this file is never listed in the sitemap.",
        "Publication provenance (the release commit SHA, the merge commit SHA, and the publication date) is finalized post-merge from the real git events; it is not set pre-merge.",
        "I1/I2 (Arts 33/35 interoperability essential requirements) carry no EP-CLM identity (source-constrained) and are excluded from the graph.",
    ],
    "generated": rc["_meta"]["generated"],
    "source_registry": rc["_meta"]["source_registry"],
}

pub = {"_meta": pub_meta, "claims": pub_claims}
os.makedirs(LIVE, exist_ok=True)
json.dump(pub, open(os.path.join(LIVE, "claims.json"), "w"), indent=2, ensure_ascii=False)

# release assertion: the pre-merge public graph must not assert live-state or invent provenance
_pub_blob = json.dumps(pub)
for _bad in ["live on main", "release_sha", "merge_sha", "live_on_main_since"]:
    assert _bad not in _pub_blob, f"public graph must not contain premature/provenance token: {_bad!r}"

# ---------- 2. live index.html ----------
html = open(os.path.join(HERE, "index.html")).read()
orig = html

# a) robots -> index,follow
html = html.replace('<meta name="robots" content="noindex, nofollow">',
                    '<meta name="robots" content="index, follow">', 1)
# b) remove the release-candidate banner block
html, n = re.subn(
    r'\n <div class="system-panel" role="note"[^\n]*>\n <p class="system-panel-body"[^\n]*Release candidate[^\n]*</p>\n </div>\n',
    "\n", html)
assert n == 1, f"banner block not removed cleanly (n={n})"
# c) hero workflow badge
html = html.replace("Workflow: publishable", "Workflow: published", 1)
# d) telemetry lifecycle
html = html.replace("<dt>Lifecycle</dt><dd>publishable</dd>", "<dt>Lifecycle</dt><dd>published</dd>", 1)
# e) register intro: publishable/null -> published/active
html = html.replace(
    "Every claim <code>workflow_state: publishable</code>, <code>validity_state: null</code>.",
    "Every claim <code>workflow_state: published</code>, <code>validity_state: active</code>.", 1)
# f) register cards: workflow: publishable -> published (87)
html = html.replace("workflow: publishable", "workflow: published")
# g) dateModified already PUB_DATE in the candidate; enforce it
assert f'"dateModified": "{PUB_DATE}"' in html, "dateModified must equal PUB_DATE"

open(os.path.join(LIVE, "index.html"), "w").write(html)
print("wrote", os.path.join(LIVE, "claims.json"))
print("wrote", os.path.join(LIVE, "index.html"))
print("html delta bytes:", len(orig) - len(html))
