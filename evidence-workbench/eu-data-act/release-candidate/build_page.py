#!/usr/bin/env python3
"""Render the EU Data Act reference page release-candidate (R3.5) from claims.json.
Staged production surface for /regulation/eu-data-act/ - NOT live. robots: noindex,nofollow.
Mirrors the EuraPlan Control Room / clock-and-gates grammar used by /regulation/gdpr/.
The live /regulation/eu-data-act/index.html is written only at the R3.8 Publish Gate.
"""
import json, html, collections

d = json.load(open("claims.json"))
claims = d["claims"]; meta = d["_meta"]
by = {c["id"]: c for c in claims}
def num(cid): return cid[-6:]
def A(n):
    cid = f"EP-CLM-000{n:03d}" if n < 1000 else None
    cid = f"EP-CLM-{n:06d}"
    return f'<a href="#ep-clm-{cid[-6:]}"><code>{cid}</code></a>'
def esc(s): return html.escape(s, quote=True)

# co-render index: id -> set of partner ids
co_idx = collections.defaultdict(set)
for pair in meta["co_render_blocking_pairs"]:
    a,b = [x.strip() for x in pair.split("+")]
    co_idx[a].add(b); co_idx[b].add(a)

HEADER = '''<header class="site-header">
 <div class="site-header-inner">
 <a href="/" class="wordmark" aria-label="EuraPlan home">
 <img src="/assets/brand/logo-mark-gold.svg" alt="" class="brand-mark" width="32" height="32" decoding="async" aria-hidden="true">
 <span class="wordmark-text">
 <span class="wordmark-name">EuraPlan</span>
 <span class="wordmark-category">European Entry Control Room</span>
 </span>
 </a>
 <nav aria-label="Primary navigation">
 <a href="/enter/">Enter</a>
 <a href="/clock/">Clock</a>
 <a href="/standard/eers/">Standard</a>
 <a href="/protocol/">Protocol</a>
 <a href="/sources/">Sources</a>
 <a href="/governance/">Governance</a>
 <a href="/acquire/">Acquire</a>
 </nav>
 </div>
</header>'''

FOOTER = '''<footer class="site-footer">
 <div class="site-footer-inner">
 <div class="footer-brand">
 <strong>EuraPlan.com</strong><br>
 European Regulatory Entry &amp; Expansion Planning Intelligence
 </div>
 <div class="footer-links">
 <a href="/enter/">Enter</a>
 <a href="/clock/">Clock</a>
 <a href="/standard/eers/">Standard</a>
 <a href="/protocol/">Protocol</a>
 <a href="/sources/">Sources</a>
 <a href="/governance/">Governance</a>
 <a href="/acquire/">Acquire</a>
 </div>
 </div>
 <p class="footer-disclaimer">
 EuraPlan produces planning intelligence, not legal advice.
 Verify current text at EUR-Lex before acting. &copy; 2026 EuraPlan. Asset owned by Sohadot.
 </p>
</footer>'''

def panel(title, body):
    return f'<div class="system-panel"><p class="system-panel-body" style="margin:0 0 6px;"><strong>{title}</strong></p>{body}</div>'

def corender_panel(default_n, boundary_n, label):
    dc, bc = by[f"EP-CLM-{default_n:06d}"], by[f"EP-CLM-{boundary_n:06d}"]
    return panel(f"Co-render boundary &mdash; {label}",
        f'<p class="system-panel-body" style="margin:0 0 6px;">{A(default_n)} &mdash; {esc(dc["claim"])}</p>'
        f'<p class="system-panel-body" style="margin:0;">{A(boundary_n)} &mdash; {esc(bc["claim"])} <em>(must render together)</em></p>')

# ---- decision-oriented thematic sections ----
SECTIONS = []
def S(id_, eyebrow, title, body): SECTIONS.append((id_, eyebrow, title, body))

S("identity","01 - Identity &amp; applicability","Instrument identity &amp; the entry clock",
  f'<p class="section-body">The Data Act is {A(46)} (Reg (EU) 2023/2854), in force since {A(47)} and applicable in general from <strong>12 September 2025</strong> ({A(48)}). Three dates gate any entry plan: the {A(49)} access-by-design duty from <strong>12 Sep 2026</strong>, Chapter IV for new contracts from 12 Sep 2025 ({A(50)}) and for legacy indefinite/long contracts from <strong>12 Sep 2027</strong> ({A(51)}).</p>'
  + panel("Decision use", '<p class="system-panel-body" style="margin:0;">Place each obligation on the clock before committing engineering or contract effort: the design duty and the legacy-contract cut-over are the two dates most often missed.</p>'))

S("scope","02 - Who is in scope","Scope, definitions &amp; the size gate",
  f'<p class="section-body">Scope turns on four definitions: connected product {A(52)}, related service {A(53)}, user {A(54)} and data holder {A(55)}; cloud duties turn on the data-processing-service definition {A(56)}. A microenterprise/small-enterprise carve-out {A(57)} (extended to recently-medium firms {A(58)}) removes Chapter II duties, subject to its partner/linked/subcontractor conditions. Where personal data is in play, the GDPR/privacy stack prevails on conflict {A(59)} and a legal basis (GDPR Art 6/9 + ePrivacy Art 5(3)) is required where the user is not the data subject {A(60)}.</p>'
  + corender_panel(46,59,"instrument identity + data-protection prevalence"))

S("access","03 - Product data (Chapter II)","User access &amp; third-party sharing",
  f'<p class="section-body">The core Chapter II rights: access-by-design {A(62)} with pre-contract information {A(63)}/{A(64)}; a data-holder access duty where direct access is not possible {A(65)}, bounded by holder use-limits {A(66)}/{A(67)} and a graduated trade-secret carve-out {A(68)}; and the user right to have data shared with a third party {A(69)}, with the gatekeeper exclusion {A(70)}, third-party purpose limits {A(71)} and prohibitions {A(72)}. These rights cannot be contracted away &mdash; the Article 7(2) anti-waiver {A(61)} co-renders with each.</p>'
  + corender_panel(69,61,"third-party sharing right + Chapter II anti-waiver"))

S("availability","04 - Data-holder availability (Chapter III)","FRAND availability &amp; compensation",
  f'<p class="section-body">Where a holder is obliged to make data available, terms must be FRAND and transparent {A(73)} and non-discriminatory {A(74)}; compensation must be reasonable {A(75)} with an SME/non-profit cost cap {A(76)}. Technical protection measures are permitted but may not defeat the user\'s rights {A(77)}, and a holder may not push data to a recipient absent a user request {A(78)}. The whole chapter is gated by the Article 12(1) applicability rule {A(79)} and protected by the Article 12(2) anti-waiver {A(80)} &mdash; both co-render with the duties.</p>'
  + corender_panel(73,79,"availability duty + Chapter III applicability gate")
  + corender_panel(73,80,"availability duty + Chapter III anti-waiver"))

S("unfair","05 - Unfair contract terms (Chapter IV)","Unilaterally-imposed unfair terms",
  f'<p class="section-body">A unilaterally-imposed unfair term is not binding {A(81)}. The regime is defined by a mandatory-law carve-out {A(82)}, the general unfairness test {A(83)}, the always-unfair {A(84)} and presumed-unfair {A(85)} lists, the unilateral-imposition test and burden of proof {A(86)}, severability {A(87)} and the subject-matter/price exclusion {A(88)}. The Article 13(9) anti-waiver {A(89)} co-renders with the default.</p>'
  + corender_panel(81,89,"unfair-term unenforceability + Chapter IV anti-waiver"))

S("b2g","06 - B2G exceptional need (Chapter V)","Government access on exceptional need",
  f'<p class="section-body">On a demonstrated exceptional need, data holders (legal persons other than public bodies) must make data available {A(90)}. Two routes gate the duty: public emergency {A(91)} and the non-emergency, non-personal-data route {A(92)}, with a micro/small carve-out on the latter {A(93)}. Procedure ({A(94)}/{A(95)}), the compensation split (free in emergency {A(96)} vs fair compensation {A(97)}) and PSB limits ({A(98)}/{A(99)}) travel with it. Chapter V does not reach criminal/customs/tax activity {A(100)}.</p>'
  + corender_panel(90,100,"B2G duty + Article 16 scope-limit / criminal-customs-tax carve-out"))

S("switching","07 - Cloud switching (Chapter VI)","Switching &amp; the exit-obstacle regime",
  f'<p class="section-body">Providers must remove obstacles to switching {A(101)} (responsibilities limited to the source provider {A(102)}). The contract must be written {A(103)}, carry the mandatory terms &mdash; 30-day transition, &le;2-month notice, &ge;30-day retrieval {A(104)} &mdash; and the customer options / unfeasibility route {A(105)}, with information {A(106)} and good-faith cooperation {A(107)}. Switching charges fall away from <strong>12 Jan 2027</strong> {A(109)} (reduced &le;cost until then {A(110)}); functional equivalence {A(111)}, open interfaces {A(112)} and standards/export {A(113)} are the technical duties. A bespoke / non-production exemption {A(114)} co-renders with these.</p>'
  + corender_panel(101,114,"switching duty + Article 31 bespoke / non-production exemption"))

S("crossborder","08 - International access &amp; interoperability (Ch VII/VIII)","Third-country access, in-parallel use &amp; smart contracts",
  f'<p class="section-body">Providers must prevent conflicting third-country governmental access to non-personal data {A(115)}, recognisable only via international agreement {A(116)} or, absent one, under the Article 32(3)-(5) conditions {A(117)}; the Article 28 transparency duty {A(108)} co-renders as its companion. Interoperability for in-parallel use reuses the switching duties mutatis mutandis {A(118)} with a cost-only egress cap {A(119)}. Smart contracts executing data-sharing agreements must meet the five essential requirements and carry an EU declaration of conformity {A(120)}.</p>'
  + corender_panel(108,115,"transparency duty + international-access prevention (N3 companion)"))

S("enforcement","09 - Enforcement &amp; final provisions (Ch IX-XI)","Authorities, penalties &amp; savings",
  f'<p class="section-body">Member States designate competent authorities and a data coordinator {A(121)}; GDPR SAs/EDPS supervise personal-data aspects {A(122)}. A non-EU entrant must appoint a legal representative &mdash; the enforcement hook &mdash; or fall under the competence of all Member States {A(123)}; establishment/competence follows main establishment {A(124)}. Complaint and judicial-remedy rights apply {A(125)}. Penalties must be effective/proportionate/dissuasive (notified by <strong>12 Sep 2025</strong>) {A(126)}, with GDPR Art 83 fines for Ch II/III/V {A(127)} and EDPS fines for Ch V {A(128)}. The sui generis DB right is carved out {A(129)}; sectoral/data-space {A(131)}, pre-2024 {A(130)} and research {A(132)} savings bound the general layer.</p>'
  + panel("Entry-risk read", f'<p class="system-panel-body" style="margin:0;">For a non-EU company, {A(123)} (legal representative) and {A(127)}/{A(128)} (fine exposure) are the two enforcement inputs that most change an entry decision.</p>'))

def render_sections():
    out = []
    for i,(id_,eyebrow,title,body) in enumerate(SECTIONS):
        out.append(f'''<section class="page-section" id="{id_}" aria-labelledby="{id_}-heading">
 <div class="section-header">
 <span class="section-eyebrow">{eyebrow}</span>
 <h2 class="section-title" id="{id_}-heading">{title}</h2>
 </div>
 {body}
 </section>
 <hr class="section-divider">''')
    return "\n".join(out)

# ---- verified claim register (all 87 cards from claims.json) ----
def rel_line(c):
    bits = []
    if c["qualified_by"]:
        bits.append("Qualified by: " + " ".join(A(int(num(x))) for x in c["qualified_by"]))
    if c["related_claims"]:
        bits.append("Related: " + " ".join(A(int(num(x))) for x in c["related_claims"]))
    if co_idx[c["id"]]:
        bits.append("Co-render: " + " ".join(A(int(num(x))) for x in sorted(co_idx[c["id"]])))
    return (" &middot; ".join(bits)) if bits else ""

def card(c):
    src = c["sources"][0]
    rl = rel_line(c)
    rl_html = f'<p style="margin:0 0 8px; font-size:0.72rem; color:var(--grey-mid);"><strong>Graph:</strong> {rl}</p>' if rl else ""
    eff = f' &middot; effective: {c["effective_date"]}' if c["effective_date"] else ""
    return f'''<article class="clock-reg-item" id="ep-clm-{num(c["id"])}">
 <div>
 <div class="clock-reg-name">{esc(c["display_label"])}</div>
 <div class="clock-reg-id">{c["id"]} &middot; risk: {c["claim_risk"]} &middot; EERS: {", ".join(c["affected_eers_dimensions"])}{eff}</div>
 </div>
 <div class="clock-reg-dates">
 <p style="margin:0 0 8px;">{esc(c["claim"])}</p>
 <p style="margin:0 0 8px; font-size:0.72rem; color:var(--grey-mid);"><strong>Source:</strong> supports &mdash; Reg (EU) 2023/2854 &mdash; Official Journal &middot; {esc(src["provision_locator"])}</p>
 {rl_html}<p style="margin:0; font-size:0.72rem; color:var(--grey-mid);"><span class="source-confidence-badge source-confidence-badge--verified">Confidence: Verified</span> &middot; Verified against primary source: {c["last_verified_at"]} &middot; workflow: publishable</p>
 </div>
 </article>'''

register = "\n".join(card(c) for c in claims)

TITLE = "EU Data Act — Evidence Graph Reference — EuraPlan"
DESC = "Source-governed EU Data Act (Regulation (EU) 2023/2854) entry-planning reference for non-EU companies: connected-product data access, B2G exceptional need, cloud switching, international access, enforcement, EERS dimensions — not legal advice."

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{esc(TITLE)}</title>
 <meta name="description" content="{esc(DESC)}">
 <meta name="robots" content="noindex, nofollow">
 <link rel="canonical" href="https://euraplan.com/regulation/eu-data-act/">
 <link rel="stylesheet" href="/assets/css/main.css">
 <link rel="icon" href="/assets/brand/favicon.svg" type="image/svg+xml">
 <link rel="icon" href="/assets/brand/favicon.png" type="image/png" sizes="32x32">
 <meta property="og:title" content="{esc(TITLE)}">
 <meta property="og:description" content="Planning-intelligence reference for Regulation (EU) 2023/2854 (Data Act) — data access, B2G, cloud switching, and European entry implications for non-EU companies.">
 <meta property="og:type" content="article">
 <meta property="og:url" content="https://euraplan.com/regulation/eu-data-act/">
 <meta property="og:image" content="https://euraplan.com/assets/brand/og-default.jpg">
 <meta property="og:image:alt" content="EuraPlan clock and pillars mark — European Entry Control Room">
 <meta property="og:site_name" content="EuraPlan">
 <meta name="twitter:card" content="summary">
 <meta name="twitter:title" content="{esc(TITLE)}">
 <meta name="twitter:description" content="Planning-intelligence reference for Regulation (EU) 2023/2854 (Data Act) — for non-EU companies entering Europe.">
 <meta name="twitter:image" content="https://euraplan.com/assets/brand/og-default.jpg">
 <script type="application/ld+json">
 {{
   "@context": "https://schema.org",
   "@type": "Article",
   "headline": "EU Data Act — Evidence Graph Reference",
   "description": "Source-governed EU Data Act entry-planning reference for non-EU companies.",
   "author": {{ "@type": "Organization", "name": "EuraPlan", "url": "https://euraplan.com" }},
   "publisher": {{ "@type": "Organization", "name": "EuraPlan", "url": "https://euraplan.com" }},
   "dateModified": "2026-09-02",
   "url": "https://euraplan.com/regulation/eu-data-act/",
   "inLanguage": "en",
   "mainEntityOfPage": "https://euraplan.com/regulation/eu-data-act/"
 }}
 </script>
 <script type="application/ld+json">
 {{
   "@context": "https://schema.org",
   "@type": "BreadcrumbList",
   "itemListElement": [
     {{ "@type": "ListItem", "position": 1, "name": "EuraPlan", "item": "https://euraplan.com/" }},
     {{ "@type": "ListItem", "position": 2, "name": "Regulation Reference", "item": "https://euraplan.com/regulation/eu-data-act/" }}
   ]
 }}
 </script>
</head>
<body>

{HEADER}

<main class="control-room-shell">

 <div class="telemetry-strip" role="group" aria-label="Control room telemetry">
 <dl class="telemetry-grid">
 <div class="telemetry-cell"><dt>Route</dt><dd>EP-REG-003</dd></div>
 <div class="telemetry-cell"><dt>Reference</dt><dd>Reg (EU) 2023/2854 (Data Act)</dd></div>
 <div class="telemetry-cell"><dt>Claims</dt><dd>EP-CLM-000046..000132 (87)</dd></div>
 <div class="telemetry-cell"><dt>Sources</dt><dd>EP-SRC-000006 / EP-SRC-000007</dd></div>
 <div class="telemetry-cell"><dt>Lifecycle</dt><dd>publishable</dd></div>
 <div class="telemetry-cell"><dt>Verified</dt><dd>2026-09-02</dd></div>
 </dl>
 </div>

 <div class="system-panel" role="note" style="border-color:var(--gold);background:rgba(180,140,40,0.06);">
 <p class="system-panel-body" style="margin:0;"><strong>Release candidate &mdash; not published.</strong> Staged R3.5 page for <code>/regulation/eu-data-act/</code>; <code>robots: noindex, nofollow</code>; all claims <code>workflow_state: publishable</code>, <code>validity_state: null</code>, <code>published: false</code>. The live surface, sitemap/llms/routes registration and RGS re-score are reserved for the R3.8 Publish Gate.</p>
 </div>

 <section class="control-room-hero" aria-labelledby="reg-heading">
 <div class="control-room-hero-mark">
 <img src="/assets/brand/logo-mark-gold.svg" alt="" class="brand-mark brand-mark--hero" width="64" height="64" decoding="async" aria-hidden="true">
 </div>
 <span class="control-room-hero-label">EP-REG-003 — EU Data Act Evidence Graph reference</span>
 <h1 class="control-room-hero-title" id="reg-heading">EU Data Act — Evidence Graph Reference</h1>
 <p class="control-room-hero-thesis">
 Regulation (EU) 2023/2854 as a citable planning graph for non-EU entry: the applicability clock, connected-product data access and sharing, data-holder availability, unfair-term limits, B2G exceptional need, cloud switching, international access, interoperability, and enforcement &mdash; each truth proposition pinned to a permanent claim ID, verified verbatim against the Official Journal act.
 </p>
 <div class="badge-row">
 <span class="source-confidence-badge source-confidence-badge--tier1">Source: Tier 1 official</span>
 <span class="source-confidence-badge source-confidence-badge--verified">Verified — 2026-09-02</span>
 <span class="source-confidence-badge source-confidence-badge--verified">Workflow: publishable</span>
 </div>
 <p style="font-size: 0.72rem; color: var(--grey-mid); max-width: 640px; margin-top: 12px; line-height: 1.6;">
 EuraPlan produces planning intelligence. This reference is not legal advice. 87/87 propositions VERIFIED_LITERAL against Regulation (EU) 2023/2854 read with its corrigendum (Art. 48 only).
 </p>
 <div class="control-room-hero-actions">
 <a href="#claim-register" class="btn btn-primary">Verified Claim Register</a>
 <a href="#identity" class="btn btn-secondary">Identity &amp; Applicability</a>
 <a href="/regulation/gdpr/" class="btn btn-secondary">GDPR Reference</a>
 </div>
 </section>

 <hr class="section-divider">

{render_sections()}

 <section class="page-section" id="claim-register" aria-labelledby="claim-register-heading">
 <div class="section-header">
 <span class="section-eyebrow">10 - Verified Claim Register</span>
 <h2 class="section-title" id="claim-register-heading">EU Data Act — Verified Claim Register</h2>
 </div>
 <p class="section-body">All 87 propositions (<code>EP-CLM-000046..000132</code>), each pinned to its Article/paragraph in Regulation (EU) 2023/2854 (<code>EP-SRC-000006</code>) read with the corrigendum (<code>EP-SRC-000007</code>, Article 48 only). Every claim <code>workflow_state: publishable</code>, <code>validity_state: null</code>. Interoperability essential requirements (Arts 33/35) carry no claim identity (source-constrained).</p>
 <div class="clock-reg-list" style="margin-top: 20px;" role="list" aria-label="EU Data Act verified claim register">
{register}
 </div>
 </section>

</main>

{FOOTER}

</body>
</html>'''

open("index.html","w").write(page)

# ---- page checks ----
import re
assert page.count('class="clock-reg-item"') == 87, "must render 87 claim cards"
for c in claims:
    assert f'id="ep-clm-{num(c["id"])}"' in page, f"missing anchor {c['id']}"
assert '<meta name="robots" content="noindex, nofollow">' in page, "must be noindex"
assert "Release candidate &mdash; not published" in page, "staging banner"
assert "workflow: publishable" in page and "published: false" in page.lower()
# no live-path leakage: canonical points at target but this file is under release-candidate/
print("index.html written:", len(page), "bytes | 87 cards | noindex | staged")
