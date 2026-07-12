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
# Frequently asked questions and real errors found while building the model (and what they teach)

Building an ontological model (a formal file describing classes, properties, and rules — here, CAO_CRM, the Ariane consortium's Corpus Author Ontology CRM) by reusing pieces from existing standards (CIDOC-CRM, LRMoo, CRMdig) is not simply "copy-paste": every piece brings along conventions and gaps that can slip in by mistake. This section gathers, as questions and answers, real incidents that occurred very early in CAO_CRM's construction, with their cause, their solution, and the lesson they leave — not to assign blame, but as a pedagogical example for anyone composing third-party ontologies. The three cases described below are **fully resolved** in the model's current version (`CAO_CRM-1.0.rdf`); they are kept here precisely because they are what convinced the team never again to trust an automated summary without checking the detail — a discipline that, much later in the project, led to a chain of three independent, successive audits before any publication (see the last section of this document).

## Why did the generated documentation appear titled "SKOS Vocabulary" instead of CAO_CRM?

While generating the documentation site with Widoco (a program that reads the ontology and automatically produces a browsable website presenting its classes and properties), the page showed "SKOS Vocabulary" as its title — the name of a completely unrelated standard: SKOS (*Simple Knowledge Organization System*, a model for controlled vocabularies and thesauri).

Inspecting the file, it was confirmed that the node describing the ontology itself (its "identity card") had mixed in, besides its own data, metadata copied verbatim from six other ontologies (SKOS, CIDOC-CRM, CRMdig, LRMoo, CRMsci, CRMinf): the title held the value `"SKOS Vocabulary"@en`, authorship was attributed to SKOS's real authors, and there was a block of nearly 200 lines that turned out to be, word for word, CIDOC-CRM's own release notes.

**How it was discovered:** not through manual review, but because Widoco surfaced a symptom impossible to ignore (a wrong title), which led to inspecting the source file. The likely cause is a side effect of how the Protégé editor "flattens" imports on export: when merging several imported files into one, their own metadata can end up mixed within a single node.

**How it was fixed:** by removing the foreign values from the ontology node and declaring the correct ones. The repository includes "regression" queries designed to fail again should the problem reappear.

**General lesson:** any tool reading the title to identify "which ontology is this" — documentation, catalogues, open-data indexers — blindly trusts that value. It is worth always checking the ontology header after any import or file "flattening."

## Why did the model, which used to pass the logical-consistency test, start failing as "inconsistent"?

Between two checks, the file grew substantially (from 970 to over 7,000 triples — each triple being a basic "subject-predicate-object" statement), due to a more complete re-export from Protégé. With this new content, the reasoner (the program applying the model's logical rules to check it does not contradict itself) reported the ontology as inconsistent: it became logically empty, since an internal contradiction lets one "derive" anything from anything.

**How it was discovered:** via `robot explain`, a utility that identifies the minimal set of responsible statements. It found four axioms: a native title property declared equivalent to Dublin Core's title property; the ontology node carrying the contaminated value `"SKOS Vocabulary"@en` on that very property; a native place property declared equivalent to that same title property; and that place property having range `xsd:anyURI` (accepting only URI identifiers). By transitivity, the contaminated text ended up "inherited" by the place property, which requires URIs, not text — an unsolvable contradiction that collapses the whole model.

**How it was fixed:** this turned out to be the combination of two problems already known separately: the contaminated metadata from the previous case, and a quality warning (the "P27 — Defining wrong equivalent properties" pitfall, detected by the OOPS! tool) that until then seemed only an "important," non-urgent recommendation. As the file grew, that recommendation turned into a hard logical contradiction. Fixing it required reviewing whether those two native properties should keep being declared equivalent, on top of cleaning the contaminated metadata.

**General lesson:** a "minor" quality warning today can become a blocking logical error tomorrow, simply because the model changed size. Two independent findings can combine into a third, more serious one than either alone — which is why "important" warnings deserve the same seriousness as "critical" ones.

## Why were CIDOC-CRM axioms about "has note" (`P3_has_note`) missing when comparing the combined model with the official file?

When comparing the combined model against the official CIDOC-CRM 7.1.3 file via `robot diff` (which flags original statements absent, unchanged, from the result), 8 missing official axioms appeared, tied to `P3_has_note` ("has note," a property for attaching informal descriptions to any entity) and its subproperties.

**How it was discovered:** by comparing how `P3_has_note` was declared in CAO_CRM against the official file. In CAO_CRM it was an `owl:ObjectProperty` (connecting to another entity with its own identity). The official CIDOC-CRM release declares it generically, as `rdf:Property`, without stating whether it is an object or data property: the reference documentation conceptually describes "Domain: E1 CRM Entity / Range: E62 String," but the executable RDF file never formalized this — a genuine gap in the standard itself, not an error by CAO_CRM. Combining both declarations for the same URI produces *punning* (using the same name for two distinct natures), and merge tools silently discard the axioms that only made sense under the "data" reading.

**How it was fixed:** the team documented its decision in `decisions/fr/problemes-et-solutions.md` (Problème 1), the project's general problem-and-solution catalog. It was decided to declare `P3_has_note` as `owl:DatatypeProperty` with range `rdfs:Literal` (the broadest category of simple values), replicating the pattern the official file itself applies to a sister property with the same gap, `P90_has_value`: `<rdfs:range rdf:resource="http://www.w3.org/2000/01/rdf-schema#Literal" />`. The `xsd:string` option was discarded: it would have been an invented restriction with no official backing, contrary to CIDOC-CRM's own practice, which avoids committing to XSD types even where the type "seems obvious" (`P90_has_value` conceptually represents a number and still uses `rdfs:Literal`).

**General lesson:** when a standard has a gap in its technical implementation, the safest way to fill it is not to invent a "more precise" solution of one's own, but to replicate how that same standard resolves equivalent cases. In a project defined as a bounded composition of third-party fragments, any typing absent from the original is, in practice, a conceptual redefinition of the base model.

## How are these cases related to one another?

They are not isolated incidents: "SKOS Vocabulary" was one of the four causes behind the second case's logical inconsistency, and `P3_has_note` was flagged by two distinct tests, confirming it was a real problem and not a false positive. In a model composed of several ontologies, problems rarely stay confined to the module where they originate: they propagate to other verification layers, and sometimes only become visible once the file grows or a different type of test from the one that first caught them is run.

## Why weren't these problems fixed "on the fly," with the first reasonable solution available?

Because a quick fix, even if it works technically, can introduce a modeling decision nobody authorized or documented: choosing `xsd:string` for `P3_has_note` would have "solved" the problem, but with no official backing. When a finding calls for a design decision, the procedure is to document it in an ADR, with the alternatives evaluated and the official citations backing the chosen option, rather than resolving it silently. Purely mechanical findings, like cleaning up contaminated metadata, are left for direct correction, with no ADR needed.

## What general lesson does this leave for anyone building a similar model?

1. **An automated summary ("0 errors") never replaces inspecting the full report.** "SKOS Vocabulary" was not caught by a test designed for that purpose, but by a visual symptom noticed in a tool pursuing an entirely different goal.
2. **Gaps in a reused standard's official documentation are not "guessed" through a decision of one's own**, but filled by replicating how that same standard resolves equivalent cases, leaving a written trace of the choice made.
3. **A model composed of several ontologies needs its "junction points" reviewed regularly.** What was a minor recommendation yesterday can become a real error tomorrow, simply because the context changed.

## What these lessons led to, much later in the project

These three incidents left a lasting mark on the working method: no claim is accepted anymore without direct verification against the source file, never against a summary or a memory. This discipline reached its most mature form just before publishing the current version, in the form of a **chain of three independent, successive audits**: a first audit re-verifying every RDF term one by one against the vendored official files; a second re-verifying the decision documentation itself and the conceptual conformance of every choice; and a third cross-checking a sample of the strongest claims from the first two, without trusting them either. None of the three audits found an error in the claims verified by the previous one — a result that, precisely because of the incidents recounted above, was never taken for granted in advance. Full detail is in `decisions/fr/auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, and `auditoria-3-verificacion-final.md`.
