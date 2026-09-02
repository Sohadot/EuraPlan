#!/usr/bin/env python3
"""Assemble the EU Data Act canonical claim-graph release-candidate (R3.4 machine package).
Staged artifact for /regulation/eu-data-act/claims.json - NOT live. published=false.

Correction pass (production-adjacent):
 - Source edges: only supports/amends/clarifies (EVIDENCE_GRAPH_MODEL v1.4). The corrigendum
   EP-SRC-000007 affects Article 48 only and amends/clarifies none of these 87 claims, so it
   carries NO per-claim edge; it is kept in _meta.source_registry + notes as read with the act.
 - Claim prose re-checked for lost scope (esp. 052/055/056/057/058/060/061/069/111).
 - Claim->Claim relations normalized to the R3.1-F Q1-Q16/N1-N7 audit: qualified_by only for a
   claim that narrows/excepts/conditions another; structural adjacency -> related_claims; an
   anti-waiver / applicability boundary that must accompany a right -> co_render_blocking_pairs.
 - EERS re-mapped per EERS_1.0 semantics (multiple dimensions allowed).
 - claim_risk from CLAIM_POLICY v1.1 (Low = bibliographic identity / entry-into-force orientation;
   everything with legal applicability/effect/deadline/compliance = High).
"""
import re, json, collections

reg = {}
for line in open("../R3_2_IDENTITY_REGISTER.md"):
    m = re.match(r'\| `(EP-CLM-\d+)` \| (R-[\w]+) \| ([IVXL]+) \| ([^|]+?) \| ([^|]+?) \| ([^|]+?) \| EP-SRC-000006 \(\+000007\) \| (.+?) \|', line)
    if m:
        cid,row,ch,loc,prop,edge,state = [g.strip() for g in m.groups()]
        lv = "2026-08-31" if "2026-08-31" in state else "2026-09-02"
        reg[cid] = dict(row=row, ch=ch, loc=loc, prop=prop, edge=edge, lv=lv)
assert len(reg) == 87, len(reg)

def C(n): return f"EP-CLM-{n:06d}"

# claim prose (verified-literal proposition), qualified_by (qb), related_claims (rel),
# eers dimensions, and optional source-locator override (loc).
E = {
 46:dict(claim="The EU Data Act is Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 (CELEX 32023R2854), a regulation directly applicable in all Member States.", qb=[59,130,131,132], eers=["DIM-01"]),
 47:dict(claim="The EU Data Act entered into force on 11 January 2024, the twentieth day following its publication in the Official Journal on 22 December 2023.", qb=None, eers=["DIM-02"], eff="2024-01-11"),
 48:dict(claim="The EU Data Act applies in general from 12 September 2025 (Article 50).", qb=[49,50,51], eers=["DIM-02","DIM-01"], eff="2025-09-12"),
 49:dict(claim="The Article 3(1) access-by-design obligation applies to connected products and related services placed on the market after 12 September 2026.", qb=None, eers=["DIM-02","DIM-06"], eff="2026-09-12"),
 50:dict(claim="Chapter IV (unfair contractual terms) applies to contracts concluded after 12 September 2025.", qb=None, eers=["DIM-02"], eff="2025-09-12"),
 51:dict(claim="Chapter IV applies from 12 September 2027 to contracts concluded on or before 12 September 2025 that are of indefinite duration or expire at least 10 years from 11 January 2024.", qb=None, eers=["DIM-02"], eff="2027-09-12"),
 52:dict(claim="A 'connected product' is an item that obtains, generates or collects data concerning its use or environment and is able to communicate product data via an electronic communications service, physical connection or on-device access, and whose primary function is not the storing, processing or transmission of data on behalf of any party other than the user (Article 2(5)).", qb=None, eers=["DIM-01"]),
 53:dict(claim="A 'related service' is a digital service, other than an electronic communications service, including software, connected with the product at or after purchase, rent or lease such that its absence would prevent the product from performing one or more of its functions, or subsequently connected to add, update or adapt functions (Article 2(6)).", qb=None, eers=["DIM-01"]),
 54:dict(claim="A 'user' is a natural or legal person that owns a connected product, to whom temporary rights to use it have been contractually transferred, or that receives related services (Article 2(12)).", qb=None, eers=["DIM-01"]),
 55:dict(claim="A 'data holder' is a natural or legal person that has the right or obligation, in accordance with this Regulation, applicable Union law or national law adopted in accordance with Union law, to use and make available data, including, where contractually agreed, product data or related-service data it has retrieved or generated during the provision of a related service (Article 2(13)).", qb=None, eers=["DIM-01"]),
 56:dict(claim="A 'data processing service' is a digital service provided to a customer that enables ubiquitous and on-demand network access to a shared pool of configurable, scalable and elastic computing resources of a centralised, distributed or highly distributed nature that can be rapidly provisioned and released with minimal management effort or service-provider interaction (Article 2(8)).", qb=None, eers=["DIM-01"]),
 57:dict(claim="The Chapter II obligations do not apply to data generated through the use of connected products manufactured or designed, or related services provided, by a microenterprise or small enterprise, provided that enterprise has no partner or linked enterprise (within Article 3 of the Annex to Recommendation 2003/361/EC) that is not itself a micro or small enterprise, and is not subcontracted to manufacture or design the product or provide the service (Article 7(1)).", qb=None, eers=["DIM-01","DIM-04"]),
 58:dict(claim="The same Article 7(1) exemption applies to an enterprise that has qualified as a medium-sized enterprise for less than one year, and to connected products for one year after they are placed on the market by such an enterprise, carrying the same Article 7(1) conditions rather than as an unconditional exemption (Article 7(1), second subparagraph).", qb=None, eers=["DIM-01","DIM-04"]),
 59:dict(claim="Where the Data Act conflicts with Union law on the protection of personal data or privacy, or with national implementing law, the data-protection or privacy law prevails (Article 1(5)).", qb=None, eers=["DIM-01"]),
 60:dict(claim="Where the user is not the data subject, personal data generated by the use of a connected product or related service may be made available (to the user or to a third party) only where there is a valid legal basis for processing under Article 6 GDPR and, where relevant, the conditions of Article 9 GDPR and of Article 5(3) of Directive 2002/58/EC (ePrivacy) are fulfilled (Articles 4(12)/5(7)).", qb=None, eers=["DIM-01","DIM-06"]),
 61:dict(claim="Any contractual term that, to the detriment of the user, excludes the application of, derogates from or varies the effect of the user's rights under Chapter II is not binding on the user (Article 7(2)).", qb=None, eers=["DIM-01"]),
 62:dict(claim="Connected products and related services must be designed and provided so that product data and related-service data, including the relevant metadata, are by default easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format and, where relevant and technically feasible, directly accessible to the user (Article 3(1)).", qb=[49,57,58], rel=[63,64], eers=["DIM-06","DIM-01"]),
 63:dict(claim="Before concluding a connected-product contract, the seller, renter or lessor must provide the specified pre-contractual information about the data the product generates and how the user can access it (Article 3(2)).", qb=None, eers=["DIM-06"]),
 64:dict(claim="Before concluding a related-service contract, the prospective service provider must provide the specified pre-contractual information about the data generated and access to it (Article 3(3)).", qb=None, eers=["DIM-06"]),
 65:dict(claim="Where data cannot be directly accessed by the user, the data holder must make readily available product and related-service data, and the relevant metadata, available to the user without undue delay, easily, securely, free of charge, in a comprehensive, structured, commonly used and machine-readable format and, where relevant and technically feasible, continuously and in real time (Article 4(1)).", qb=[68,60,57,58], rel=[66,67], eers=["DIM-06","DIM-01"]),
 66:dict(claim="A data holder may use readily available non-personal product data only on the basis of a contract with the user, and may not use such data to derive insights about the user's economic situation, assets or production methods that could undermine the user's commercial position (Article 4(13)).", qb=None, eers=["DIM-06"]),
 67:dict(claim="A data holder may not make non-personal product data available to third parties for commercial or non-commercial purposes other than to fulfil its contract with the user (Article 4(14)).", qb=None, eers=["DIM-06"]),
 68:dict(claim="Trade secrets need be disclosed only where the data holder and user have agreed the measures necessary to preserve confidentiality; where such measures are not agreed or implemented, or the user fails to observe them, the data holder may withhold or suspend sharing of the identified data under the graduated conditions of Article 4(6)/(7)/(8).", qb=None, eers=["DIM-06","DIM-01"]),
 69:dict(claim="At the user's request, the data holder must make product and related-service data available to a third party without undue delay, of the same quality as available to the data holder and, where relevant and technically feasible, continuously and in real time; trade secrets are preserved and disclosed to the third party only as strictly necessary for the agreed purpose, and where the necessary confidentiality measures are not agreed or are breached the data holder may withhold or suspend, or in exceptional cases refuse, sharing of the identified data (Article 5(1), read with the trade-secret boundary in Article 5(9)-(11)).", qb=[70,72,60,57,58], rel=[71,78], eers=["DIM-06","DIM-01"], loc="Article 5(1); third-party trade-secret boundary Article 5(9)-(11)"),
 70:dict(claim="An undertaking designated as a gatekeeper under Article 3 of Regulation (EU) 2022/1925 (DMA) is not an eligible third party and may not solicit or commercially incentivise a user to make data available to it (Article 5(3)).", qb=None, eers=["DIM-01","DIM-06"]),
 71:dict(claim="A third party may process the data made available only for the purposes and under the conditions agreed with the user and subject to Union data-protection law, and must erase the data when no longer necessary (Article 6(1)).", qb=None, eers=["DIM-06"]),
 72:dict(claim="A third party receiving data must not, among other things, use it to develop a competing connected product, coerce or deceive the user, profile the user unless necessary, make the data available to a gatekeeper, or use it outside the agreed purposes (Article 6(2), points (a)-(h)).", qb=None, eers=["DIM-06"]),
 73:dict(claim="Where, in business-to-business relations, a data holder is obliged to make data available to a data recipient under Chapter III, it must do so under fair, reasonable and non-discriminatory terms and in a transparent manner (Article 8(1)).", qb=[79], rel=[74,78], eers=["DIM-06","DIM-01"]),
 74:dict(claim="A data holder must not discriminate between comparable categories of data recipients when making data available, and must, on request, demonstrate the absence of discrimination (Article 8(3)).", qb=[79], eers=["DIM-06","DIM-01"]),
 75:dict(claim="Any compensation agreed between a data holder and a data recipient for making data available under Chapter III must be non-discriminatory and reasonable, and may include a margin (Article 9(1)).", qb=[76,79], eers=["DIM-06","DIM-01"]),
 76:dict(claim="Where the data recipient is an SME or a not-for-profit research organisation, compensation must not exceed the costs directly related to making the data available and attributable to the request (Article 9(4)).", qb=None, eers=["DIM-06","DIM-01"]),
 77:dict(claim="A data holder may apply appropriate technical protection measures to prevent unauthorised access and ensure compliance, provided they do not hinder the user's or recipient's exercise of Article 4/5 rights, with the remedies of Article 11(2)/(3)/(5) available against misuse (Article 11(1)/(2)/(3)/(5)).", qb=[79], rel=[65,69], eers=["DIM-06"]),
 78:dict(claim="A data holder must not make product or related-service data available to a data recipient absent a user request under Chapter II (Article 8(4)).", qb=None, eers=["DIM-06","DIM-01"]),
 79:dict(claim="The Chapter III obligations on data holders apply where they are obliged by Article 5, or by other Union law or national implementing law, to make data available to a data recipient (Article 12(1)).", qb=None, eers=["DIM-01"]),
 80:dict(claim="A contractual term in a data-sharing agreement that, to the detriment of one party or the user, excludes, derogates from or varies the application of Chapter III is not binding on that party (Article 12(2)).", qb=None, eers=["DIM-01"]),
 81:dict(claim="A contractual term concerning access to and use of data, or liability and remedies for breach or termination of data-related obligations, that has been unilaterally imposed by one enterprise on another is not binding on the latter if it is unfair (Article 13(1)).", qb=[82,83,84,85,86,87,88], eers=["DIM-01","DIM-06"]),
 82:dict(claim="A contractual term that reflects mandatory provisions of Union law, or provisions that would apply if the term did not regulate the matter, is not to be considered unfair (Article 13(2)).", qb=None, eers=["DIM-01"]),
 83:dict(claim="A contractual term is unfair if its use grossly deviates from good commercial practice in data access and use, contrary to good faith and fair dealing (Article 13(3)).", qb=None, eers=["DIM-01","DIM-06"]),
 84:dict(claim="A contractual term is always unfair where its object or effect is one of those listed in Article 13(4) (for example, excluding liability for intentional acts or gross negligence) (Article 13(4)).", qb=None, eers=["DIM-01","DIM-06"]),
 85:dict(claim="A contractual term is presumed unfair where its object or effect is one of those listed in Article 13(5), subject to the point-(g) proviso on indefinite-duration contracts (Article 13(5)).", qb=None, eers=["DIM-01","DIM-06"]),
 86:dict(claim="A term is unilaterally imposed where supplied by one party and the other could not influence its content despite attempting to negotiate; the supplier bears the burden of proving it was not unilaterally imposed and may not argue that its own term is unfair (Article 13(6)).", qb=None, eers=["DIM-01"]),
 87:dict(claim="Where an unfair contractual term is severable from the remaining terms of the contract, those remaining terms remain binding (Article 13(7)).", qb=None, eers=["DIM-01"]),
 88:dict(claim="The Article 13 unfairness regime does not apply to terms defining the main subject matter of the contract or to the adequacy of the price as against the data supplied in exchange (Article 13(8)).", qb=None, eers=["DIM-01"]),
 89:dict(claim="Parties to a contract covered by Article 13(1) may not exclude the application of Article 13, derogate from it or vary its effects (Article 13(9)).", qb=None, eers=["DIM-01"]),
 90:dict(claim="Where a public sector body, the Commission, the ECB or a Union body demonstrates an exceptional need under Article 15 to use data to carry out statutory duties in the public interest, data holders that are legal persons (other than public sector bodies) must make that data available on a duly reasoned request (Article 14).", qb=[91,92,93,100], rel=[94,95,96,97,98,99], eers=["DIM-06","DIM-01"]),
 91:dict(claim="An exceptional need exists where the data requested is necessary to respond to a public emergency and the body cannot obtain it by alternative means in a timely and effective manner under equivalent conditions (Article 15(1)(a)).", qb=None, eers=["DIM-06","DIM-01"]),
 92:dict(claim="Outside a public emergency, and only for non-personal data, an exceptional need exists where a body acting under Union or national law has identified specific data whose lack prevents a specific public-interest task and has exhausted all other means to obtain it (Article 15(1)(b)).", qb=None, eers=["DIM-06","DIM-01"]),
 93:dict(claim="The Article 15(1)(b) non-emergency route does not apply to microenterprises and small enterprises (Article 15(2)).", qb=None, eers=["DIM-01","DIM-04"]),
 94:dict(claim="A B2G request for data must specify the data and demonstrate the exceptional need, state the purpose, legal basis and erasure expectations, and meet the form and proportionality requirements of Article 17(1)/(2), subject to the reuse, delegation, complaint and model-template rules of Article 17(3)-(6).", qb=None, eers=["DIM-06"]),
 95:dict(claim="A data holder must make requested data available without undue delay, and may decline or seek modification of a request within 5 working days (public emergency) or 30 working days (other exceptional need) on the grounds set out in Article 18(2), subject to Article 18(1)-(5).", qb=None, eers=["DIM-06","DIM-02"]),
 96:dict(claim="Data holders other than micro and small enterprises must make data necessary to respond to a public emergency (Article 15(1)(a)) available free of charge (Article 20(1)).", qb=None, eers=["DIM-06"]),
 97:dict(claim="For data made available under the Article 15(1)(b) route, the data holder is entitled to fair compensation covering technical and organisational costs plus a reasonable margin, and this entitlement also applies where a micro or small enterprise claims compensation (Article 20(2)/(3)).", qb=None, eers=["DIM-06"]),
 98:dict(claim="A public sector body, the Commission, the ECB or a Union body receiving data must not use it incompatibly with the stated purpose, must implement confidentiality and security measures, must erase it when no longer necessary, must not use it to develop a competing product or share it for that purpose, and must observe trade-secret and security obligations (Article 19(1)-(4)).", qb=None, eers=["DIM-06"]),
 99:dict(claim="A recipient body may share data received under Chapter V only with individuals or organisations for scientific research or analytics, or with national statistical institutes and Eurostat, subject to not-for-profit conditions, the Article 17(3)/19 obligations, a six-month retention limit and data-holder notification (Article 21(1)-(5)).", qb=None, eers=["DIM-06","DIM-01"]),
 100:dict(claim="Chapter V does not affect other reporting, access or compliance obligations and does not apply to activities for the prevention, investigation, detection or prosecution of criminal or administrative offences, the execution of criminal penalties, or customs or taxation administration (Article 16).", qb=None, eers=["DIM-01"]),
 101:dict(claim="Providers of data processing services must take the measures in Articles 25, 26, 27, 29 and 30 to enable customers to switch to another provider of the same service type or to on-premises ICT infrastructure, and must not impose and must remove obstacles to switching (Article 23).", qb=[102,114], rel=[103,104,105,106,107,108,109,111], eers=["DIM-06","DIM-01"]),
 102:dict(claim="The switching responsibilities in Articles 23, 25, 29, 30 and 34 apply only to the services, contracts or commercial practices provided by the source provider of data processing services (Article 24).", qb=None, eers=["DIM-01"]),
 103:dict(claim="The customer's rights and the provider's switching obligations must be set out in a written contract made available before signing in a form the customer can store and reproduce (Article 25(1)).", qb=None, eers=["DIM-06"]),
 104:dict(claim="The switching contract must include the mandatory terms of Article 25(2), including a maximum 30-calendar-day transitional period, a maximum notice period not exceeding two months, and a data-retrieval period of at least 30 calendar days (Article 25(2), points (a)-(i)).", qb=None, eers=["DIM-06","DIM-02"]),
 105:dict(claim="The contract must let the customer elect to switch to another provider, switch to on-premises infrastructure or erase its data; where the maximum transitional period is technically unfeasible the provider must notify within 14 working days and set an alternative period not exceeding seven months, and the customer may extend the transitional period once (Article 25(3)/(4)/(5)).", qb=None, eers=["DIM-06","DIM-02"]),
 106:dict(claim="The provider must give the customer information on switching and porting procedures, methods, formats and known limitations, and a reference to an up-to-date online register of data structures, formats, standards and open interoperability specifications (Article 26).", qb=None, eers=["DIM-06"]),
 107:dict(claim="All parties involved, including destination providers, must cooperate in good faith to make the switching process effective, enable timely data transfer and maintain service continuity (Article 27).", qb=None, eers=["DIM-06"]),
 108:dict(claim="Providers must publish and keep up to date, on their websites, the jurisdiction of the ICT infrastructure used and a general description of measures preventing international governmental access to or transfer of non-personal data held in the Union that would conflict with Union or Member-State law, and must list those websites in their contracts (Article 28(1)/(2)).", qb=None, rel=[115], eers=["DIM-06","DIM-01"]),
 109:dict(claim="From 12 January 2027, providers of data processing services may not impose any switching charges on customers for the switching process (Article 29(1)).", qb=[110,114], eers=["DIM-02","DIM-06"], eff="2027-01-12"),
 110:dict(claim="From 11 January 2024 until 12 January 2027, providers may impose reduced switching charges not exceeding the costs directly linked to the switching process (Article 29(2)/(3)).", qb=None, eers=["DIM-02","DIM-06"]),
 111:dict(claim="Providers of data processing services that concern scalable and elastic computing resources limited to infrastructural elements (such as servers, networks and the virtual resources necessary to operate the infrastructure) and that do not provide access to the operating services, software and applications stored, processed or deployed on those elements must take all reasonable measures in their power to help the customer achieve functional equivalence after switching to a service of the same service type (Article 30(1)).", qb=[114], rel=[112,113], eers=["DIM-06","DIM-01"]),
 112:dict(claim="Providers other than those in Article 30(1) must make open interfaces available to all customers and concerned destination providers free of charge to facilitate switching (Article 30(2)).", qb=None, eers=["DIM-06"]),
 113:dict(claim="Providers other than those in Article 30(1) must ensure compatibility with common specifications or harmonised standards at least 12 months after their reference is published, export exportable data in a machine-readable format where none are published, and are not required to develop new technologies, disclose IP or trade secrets, or compromise security (Article 30(3)/(5)/(6)).", qb=None, eers=["DIM-06","DIM-02"]),
 114:dict(claim="The Article 23(d), 29 and 30(1)/(3) obligations do not apply to bespoke or custom-built services not offered at broad commercial scale (Article 31(1)); the whole of Chapter VI does not apply to non-production services provided for testing and evaluation for a limited period (Article 31(2)); and the provider must disclose which Chapter VI obligations do not apply (Article 31(3)).", qb=None, eers=["DIM-01","DIM-06"]),
 115:dict(claim="Providers of data processing services must take all adequate technical, organisational and legal measures to prevent international and third-country governmental access to, or transfer of, non-personal data held in the Union where such access or transfer would conflict with Union or Member-State law (Article 32(1)).", qb=[116,117], rel=[108], eers=["DIM-06","DIM-01"]),
 116:dict(claim="A third-country court or administrative decision requiring transfer of or access to non-personal data held in the Union is recognisable or enforceable only if based on an international agreement, such as a mutual legal assistance treaty, in force between the requesting third country and the Union or a Member State (Article 32(2)).", qb=None, eers=["DIM-06","DIM-01"]),
 117:dict(claim="Absent such an international agreement, transfer or access may take place only where the Article 32(3) conditions on reasoned, proportionate and reviewable third-country decisions are met, with the provider disclosing only the minimum data permissible (Article 32(4)) and informing the customer before complying save for law-enforcement purposes (Article 32(5)).", qb=None, eers=["DIM-06","DIM-01"]),
 118:dict(claim="The requirements in Articles 23, 24, 25(2) points (a)(ii), (a)(iv), (e) and (f) and 30(2)-(5) apply mutatis mutandis to facilitate interoperability for the in-parallel use of data processing services (Article 34(1)).", qb=None, rel=[119,101,104,111,112,113], eers=["DIM-06"]),
 119:dict(claim="Where a data processing service is used in parallel with another, providers may impose data egress charges only to pass on the egress costs incurred, without exceeding them (Article 34(2)).", qb=None, eers=["DIM-06"]),
 120:dict(claim="A vendor or deployer of smart contracts for executing data-sharing agreements must ensure they meet the essential requirements of robustness and access control, safe termination and interruption, data archiving and continuity, access control and consistency, perform a conformity assessment and issue an EU declaration of conformity (Article 36(1)-(4)).", qb=None, eers=["DIM-06"]),
 121:dict(claim="Each Member State must designate one or more competent authorities to enforce this Regulation, designate a data coordinator where there is more than one, and define their tasks and powers (including penalties, switching-charge withdrawal and examining Chapter V requests); the Commission maintains a public register of those authorities (Article 37(1)/(2)/(5)/(6)/(7)).", qb=None, rel=[122,123,124,125], eers=["DIM-01","DIM-07"]),
 122:dict(claim="The GDPR supervisory authorities monitor application of this Regulation as regards the protection of personal data, and the European Data Protection Supervisor does so as regards the Commission, the ECB and Union bodies (Article 37(3)).", qb=None, eers=["DIM-01","DIM-07"]),
 123:dict(claim="An entity within scope that makes connected products available or offers services in the Union but is not established in the Union must designate a legal representative in a Member State; until it does, it is under the competence of all Member States for enforcement (Article 37(11)/(12)/(13)).", qb=None, eers=["DIM-04","DIM-07"]),
 124:dict(claim="An entity within scope is under the competence of the Member State where it is established, or, where established in more than one, of the Member State of its main establishment (the head or registered office exercising principal financial and operational control) (Article 37(10)).", qb=None, rel=[123], eers=["DIM-04","DIM-01"]),
 125:dict(claim="Natural and legal persons have the right to lodge a complaint with the competent authority if they consider their rights under this Regulation infringed, and any affected person has the right to an effective judicial remedy against binding decisions of competent authorities (Articles 38(1)-(3), 39(1)-(3)).", qb=None, eers=["DIM-07","DIM-01"]),
 126:dict(claim="Member States must lay down effective, proportionate and dissuasive penalties for infringements, notify them to the Commission by 12 September 2025, and take account of the Article 40(3) criteria (Article 40(1)/(2)/(3)).", qb=[127,128], eers=["DIM-07","DIM-02"], eff="2025-09-12"),
 127:dict(claim="For infringements of Chapters II, III and V, the GDPR supervisory authorities may, within their competence, impose administrative fines under Article 83 GDPR up to the Article 83(5) amounts (Article 40(4)).", qb=None, eers=["DIM-07"]),
 128:dict(claim="For infringements of Chapter V, the European Data Protection Supervisor may, within its competence, impose administrative fines under Article 66 of Regulation (EU) 2018/1725 up to the Article 66(3) amounts (Article 40(5)).", qb=None, eers=["DIM-07"]),
 129:dict(claim="The sui generis database right in Article 7 of Directive 96/9/EC does not apply to data obtained from or generated by a connected product or related service within the scope of this Regulation, in particular in relation to Articles 4 and 5 (Article 43).", qb=None, eers=["DIM-01"]),
 130:dict(claim="Specific data-availability obligations in Union legal acts that entered into force on or before 11 January 2024, and their delegated or implementing acts, remain unaffected by this Regulation (Article 44(1)).", qb=None, eers=["DIM-01"]),
 131:dict(claim="This Regulation is without prejudice to Union law laying down, for a sector, a common European data space or an area of public interest, further requirements on data access and use (Article 44(2)).", qb=None, eers=["DIM-01"]),
 132:dict(claim="This Regulation, with the exception of Chapter V, is without prejudice to Union and national law providing for access to and use of data for scientific research purposes (Article 44(3)).", qb=None, eers=["DIM-01"]),
}
assert len(E) == 87, len(E)

# claim_risk per CLAIM_POLICY v1.1, calibrated to the live GDPR graph:
# Low = bibliographic instrument identity + entry-into-force orientation; everything else = High.
LOW = {46, 47}
def risk_of(n): return "Low" if n in LOW else "High"

def label(cid):
    r = reg[cid]
    return f"Data Act / {r['row'][2:]} / Ch {r['ch']} / {r['loc']}"

claims = []
for n in range(46, 133):
    cid = C(n); r = reg[cid]; e = E[n]
    locator = e.get("loc", r["loc"])
    claims.append({
        "id": cid,
        "display_label": label(cid),
        "claim": e["claim"],
        "jurisdiction": "EU",
        "actor": None,
        "effective_date": e.get("eff"),
        "sources": [
            {"source_id":"EP-SRC-000006","provision_locator":locator,"relationship":"supports"},
        ],
        "qualified_by": [C(x) for x in e["qb"]] if e.get("qb") else None,
        "related_claims": [C(x) for x in e["rel"]] if e.get("rel") else None,
        "workflow_state": "publishable",
        "validity_state": None,
        "confidence": "Verified",
        "claim_risk": risk_of(n),
        "affected_eers_dimensions": e["eers"],
        "last_verified_at": r["lv"],
        "supersedes": None, "superseded_by": None,
        "corrects": None, "corrected_by": None, "change_type": None,
    })

# co_render_blocking_pairs: anti-waiver / applicability boundaries that must render with their right.
co_render = [
    "EP-CLM-000046 + EP-CLM-000059",  # A1 + GDPR-prevalence (Q13)
    "EP-CLM-000062 + EP-CLM-000061",  # C1 + Ch II anti-waiver B7 (Q15)
    "EP-CLM-000065 + EP-CLM-000061",  # C3 + B7
    "EP-CLM-000069 + EP-CLM-000061",  # C6 + B7
    "EP-CLM-000073 + EP-CLM-000079",  # D3 + Ch III applicability gate D9 (N1)
    "EP-CLM-000073 + EP-CLM-000080",  # D3 + Ch III anti-waiver D10
    "EP-CLM-000075 + EP-CLM-000080",  # D5a + D10
    "EP-CLM-000081 + EP-CLM-000089",  # E1a + Ch IV anti-waiver E6
    "EP-CLM-000090 + EP-CLM-000100",  # F1 + Ch V scope-limit F6 (Art 16)
    "EP-CLM-000101 + EP-CLM-000114",  # G1 + Ch VI Art 31 exemption G8
    "EP-CLM-000109 + EP-CLM-000114",  # G4a + G8
    "EP-CLM-000111 + EP-CLM-000114",  # G5a + G8
    "EP-CLM-000108 + EP-CLM-000115",  # G6 + H1a (N3 companion)
]

meta = {
    "batch": "EU Data Act - canonical claim graph (Data Act v1; machine package candidate; NOT published; NOT live)",
    "status": "R3.4 canonical-graph machine package candidate assembled from the R3.3 human-literal verification (87/87 VERIFIED_LITERAL). workflow_state=publishable; validity_state=null; published=false. Publication (publishable->published, null->active, published=true), provenance SHAs, and routes/sitemap/llms registration are reserved for the R3.8 Publish Gate.",
    "location_note": "evidence-workbench/eu-data-act/release-candidate/claims.json - machine package candidate for the public path /regulation/eu-data-act/claims.json. NOT the live file; the live file is written only in the R3.8 Publish Gate sequence.",
    "published": False,
    "route_id": "EP-REG-003",
    "schema_version": "EVIDENCE_GRAPH_MODEL.md v1.4",
    "claim_count": 87,
    "id_range": "EP-CLM-000046..EP-CLM-000132",
    "co_render_blocking_pairs": co_render,
    "excluded_source_constrained": ["R-I1 (Art. 33)","R-I2 (Art. 35)"],
    "embedded_unminted_qualifiers": [
        "EP-CLM-000069 embeds the Article 5(9)-(11) third-party trade-secret boundary (no separate EP-CLM identity).",
    ],
    "governed_by": [
        "EVIDENCE_GRAPH_MODEL.md","CLAIM_IDENTITY_AND_LIFECYCLE_SPECIFICATION.md",
        "SOURCE_POLICY.md","CLAIM_POLICY.md","ROUTE_GOVERNANCE.md","DISCLOSURE_BOUNDARY.md",
        "REFERENCE_GRADE_ROUTE_STANDARD.md","EERS_1.0_CANDIDATE_SPECIFICATION.md",
        "DEC-057","DEC-059","DEC-060",
    ],
    "notes": [
        "Assembled from R3_3_VERBATIM_VERIFICATION.md (Blocks 1-10, 87/87 VERIFIED_LITERAL) and the R3.1-F Q1-Q16/N1-N7 constraint audit. Claim prose is the verified-literal proposition; provision_locator is the exact Article/paragraph.",
        "Source edges use only supports/amends/clarifies (EVIDENCE_GRAPH_MODEL v1.4). The corrigendum EP-SRC-000007 affects Article 48 only and amends/clarifies none of these 87 claims, so it carries NO per-claim edge; it is retained here in source_registry as the corrigendum read with the authentic act, with no effect on any claim.",
        "Claim->Claim relations follow the R3.1-F audit: qualified_by only for a claim that narrows/excepts/conditions another (Q/N carve-outs, exemptions, applicability gates); structural adjacency (implementation duties, enforcement architecture, procedure) is related_claims; anti-waiver and applicability boundaries that accompany a right without narrowing its truth are co_render_blocking_pairs.",
        "claim_risk per CLAIM_POLICY v1.1, calibrated to the live GDPR graph: Low only for bibliographic instrument identity (A1) and entry-into-force orientation (A2); all legal applicability/scope, compliance, right/restriction, exemption-with-effect and deadline claims are High (Tier-1 basis EP-SRC-000006).",
        "EERS dimensions per EERS_1.0 semantics (multiple allowed): DIM-01 identification/scope/actor; DIM-02 timing; DIM-04 entity/representation/establishment; DIM-06 concrete product/service requirements; DIM-07 enforcement/penalty exposure. DIM-03/05/08 not asserted without direct support.",
        "All 87 claims workflow_state=publishable; validity_state=null; published=false. Publication is reserved for the R3.8 Publish Gate.",
        "Not live: no file under regulation/eu-data-act/**; no routes.json / llms.txt / sitemap / robots mutation here. Provenance SHAs are set only at the Publish Gate.",
        "I1/I2 (Arts 33/35 interoperability essential requirements) carry no EP-CLM identity (source-constrained / standards-pending) and are excluded from the graph.",
    ],
    "generated": "2026-09-02",
    "target_public_path": "/regulation/eu-data-act/claims.json",
    "target_route": "/regulation/eu-data-act/",
    "source_registry": {
        "EP-SRC-000006": {
            "instrument_id":"EU-2023-2854","official_title":"Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data and amending Regulation (EU) 2017/2394 and Directive (EU) 2020/1828 (Data Act)",
            "celex":"32023R2854","eli":"http://data.europa.eu/eli/reg/2023/2854/oj","oj_reference":"OJ L, 2023/2854, 22.12.2023",
            "source_version_date":"2023-12-22","retrieved_at":"2026-08-31","source_tier":1,"role":"authentic Official Journal act - evidentiary basis (supports every claim)",
        },
        "EP-SRC-000007": {
            "instrument_id":"EU-2023-2854-CORRIGENDUM-20241209","official_title":"Corrigendum to Regulation (EU) 2023/2854 (Data Act)",
            "eli":"http://data.europa.eu/eli/reg/2023/2854/corrigendum/2024-12-09/oj","oj_reference":"OJ L, 2024/90790, 9.12.2024",
            "source_version_date":"2024-12-09","retrieved_at":"2026-08-31","source_tier":1,"role":"corrigendum read with EP-SRC-000006; affects Article 48 only; no effect on any of these 87 claims, hence no per-claim edge",
        },
    },
}

out = {"_meta": meta, "claims": claims}
json.dump(out, open("claims.json","w"), indent=2, ensure_ascii=False)

# ---- hardened generator checks ----
ids = {c["id"] for c in claims}
assert len(ids) == 87 and min(ids) == C(46) and max(ids) == C(132), "id set"
ALLOWED_REL = {"supports","amends","clarifies"}
for c in claims:
    for s in c["sources"]:
        assert s["relationship"] in ALLOWED_REL, f"{c['id']} bad source rel {s['relationship']}"
    for q in (c["qualified_by"] or []): assert q in ids, f"{c['id']} qb dangling {q}"
    for q in (c["related_claims"] or []): assert q in ids, f"{c['id']} rel dangling {q}"
    assert c["workflow_state"]=="publishable" and c["validity_state"] is None and out["_meta"]["published"] is False
    if c["claim_risk"] == "High":
        assert any(s["source_id"]=="EP-SRC-000006" for s in c["sources"]), f"{c['id']} High without Tier-1"
    # qualified_by and related_claims must be disjoint
    qb=set(c["qualified_by"] or []); rl=set(c["related_claims"] or [])
    assert not (qb & rl), f"{c['id']} qb/rel overlap"
def QB(n): return set(next(c for c in claims if c["id"]==C(n))["qualified_by"] or [])
# canonical Q/N safety-relation representation
assert C(59) in QB(46), "Q13 A1->B6"
assert {C(49),C(50),C(51)} <= QB(48), "Q1 A3 phasing"
assert {C(57),C(58)} <= QB(62), "Q2 on C1"
assert {C(68),C(60),C(57),C(58)} <= QB(65), "Q3/Q16/Q2 on C3"
assert {C(70),C(72),C(60),C(57),C(58)} <= QB(69), "Q4/Q16/Q2 on C6"
assert C(79) in QB(73) and C(79) in QB(74), "N1 D9 gate"
assert {C(82),C(83),C(84),C(85),C(86),C(87),C(88)} <= QB(81), "Q6 on E1a"
assert C(100) in QB(90), "Q7 F6 on F1"
assert {C(91),C(92),C(93)} <= QB(90), "Q7 routes on F1"
assert C(114) in QB(101) and C(114) in QB(109) and C(114) in QB(111), "Q9/Q10 G8"
assert {C(116),C(117)} <= QB(115), "N6 on H1a"
assert {C(127),C(128)} <= QB(126), "Q11 on K2a"
crset = set(co_render)
for p in ["EP-CLM-000046 + EP-CLM-000059","EP-CLM-000062 + EP-CLM-000061","EP-CLM-000065 + EP-CLM-000061","EP-CLM-000069 + EP-CLM-000061","EP-CLM-000081 + EP-CLM-000089","EP-CLM-000090 + EP-CLM-000100","EP-CLM-000101 + EP-CLM-000114","EP-CLM-000073 + EP-CLM-000080"]:
    assert p in crset, f"missing co-render {p}"
# G8 two-layer semantics preserved in prose
assert "Article 31(1)" in E[114]["claim"] and "Article 31(2)" in E[114]["claim"] and "Article 31(3)" in E[114]["claim"], "G8 two-layer"
print("claims.json written:", len(claims), "claims - ALL CHECKS PASS")
print("risk split:", dict(collections.Counter(c['claim_risk'] for c in claims)))
print("eers usage:", dict(collections.Counter(d for c in claims for d in c['affected_eers_dimensions'])))
print("qualified_by non-null:", sum(1 for c in claims if c['qualified_by']), "| related_claims non-null:", sum(1 for c in claims if c['related_claims']), "| co_render pairs:", len(co_render))
