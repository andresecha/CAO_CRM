<!--
CAO_CRM (Corpus Author Ontology CRM)
Copyright (c) 2026 Andres Echavarria Pelaez
Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)
Encoding carried out under the scientific direction and support of Fatiha Idmhand

This file is part of the CAO_CRM publication package, licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License (CC BY-NC-SA 4.0). To view a copy of this license, visit
https://creativecommons.org/licenses/by-nc-sa/4.0/
-->
# decisions/ — modeling decision record and audits

Every non-trivial modeling decision behind CAO_CRM, documented with the literal citation from the
official source (CIDOC-CRM/LRMoo/CRMdig) that justifies it, the options considered, the final
decision, and — for the three ADRs — three successive independent audits that re-verify every
claim against the source files. This is the project's primary evidence trail: not a changelog of
*what* changed, but a record of *why*, checkable against the standards themselves.

`fr/` is the primary, most complete set (all files, written first); `es/` carries the three ADRs
plus a subset of the technical reports, translated or written independently. Not every file exists
in both languages — see the table below for exactly which. The root `README.md` (section 7)
carries a longer description of each file's content; this table is a navigation aid, not a
duplicate of that section.

| File | `fr/` | `es/` | Content |
|---|---|---|---|
| `ADR-001-disjointness.md` | ✅ | ✅ | Why CAO_CRM declares no `owl:disjointWith` — follows the same deliberate choice as CIDOC-CRM/LRMoo/CRMdig themselves |
| `ADR-002-idiomas-LRMoo-CRMdig.md` | ✅ | ✅ | Why LRMoo/CRMdig terms that only exist in English officially aren't translated in the canonical RDF — the working translation lives separately (see `docs/i18n/`) |
| `ADR-003-autoria-y-procedencia.md` | ✅ | ✅ | Attribution of the conceptual model author, the RDF/OWL implementation author, and the tools cited in the ontology header |
| `problemes-et-solutions.md` | ✅ | — | Central document — the 8 modeling problems identified during construction, each with full official citation, plain-language explanation, and the explicit distinction between a diagram-level and an RDF-level change |
| `complete-model.md` | ✅ | — | Exhaustive verification of the paper's 5-class × 4-category matrix; real gaps identified and resolved, with corroborating research |
| `informe-P14-roles-autorat.md` | ✅ | — | Justification (CIDOC-CRM SIG Encoding Rule 4, MARC Relator Terms, alternatives studied) for adding the authorship-role sub-properties |
| `informe-activite-editoriale-scientifique.md` | ✅ | — | The "editorial activity" branch flagged by the paper as CAO_CRM's original differentiator — commercial vs. scientific editor distinction |
| `auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md` | ✅ | — | Chain of 3 independent, successive audits — RDF term-by-term, then documentation/conceptual conformance, then final cross-check |
| `informe-completitud-labels-domain-range.md` | ✅ | ✅ | Why some domains/ranges point outside the 29 classes chosen for this bounded module, and what that does and doesn't mean |
| `informe-implementacion-RDF-modulo-acotado.md` | ✅ | ✅ | How the bounded module was actually built and integrated, term by term |
| `informe-integracion-properties_extracted.md` | — | ✅ | Spanish-only report: reconciling `properties_extracted.csv` (the conceptual diagram's exported domain/range pairs) against the RDF module, term by term |
| `informe-requisitos-publicacion-CAO_CRM.md` | — | ✅ | Spanish-only report on the publication requirements (namespace, versionIRI, Pages routing) later implemented identically for the GitHub repository |

The `P3_has_note` typing case, initially documented as a fourth ADR, now lives inside
`problemes-et-solutions.md` (Problem 1): it was never validated collectively by the team the way
the three ADRs above were, so it stays in the general problem catalogue rather than under the ADR
label, which implies an enacted team decision.
