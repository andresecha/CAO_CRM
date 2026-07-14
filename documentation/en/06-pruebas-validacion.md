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
# How we check that the model is well built

## Why a battery of tests is needed, and why it is not enough for it to "open without error"

An ontological model such as CAO_CRM (Corpus Author Ontology CRM, the Ariane consortium's model) is, at bottom, a text file with a very strict grammar, describing classes ("Work," "Person," "Place"...), properties that relate them ("has author," "has title"...), and rules governing how they can combine. Such a file can fail in very different ways: through a typo that prevents it from being read, by being readable yet logically contradictory, by silently contradicting the standards it claims to extend, or by being flawless yet unable to answer the real questions that motivated its construction.

That is why the validation repository applies a **chain of eight automated checks**, each designed to catch a type of problem the others cannot see, runnable in a single command (`make validate`) or individually. One warning applies to all of them: it is never enough to trust the terminal's summary line, nor the fact that a tool "finishes without error" — the detailed report must be opened whenever one exists. This discipline is not theoretical: very early in the project, a summary once read "0 problems" while the actual report contained several serious problems, due to a bug in the counting script itself (see the "Frequently Asked Questions" section of this documentation for this and other cases, kept as lessons).

## Current state (July 10, 2026, `CAO_CRM-1.0.rdf`, 1165 triples, 41 classes, 84 object properties, 5 data properties)

| # | Test | Command | Result |
|---|---|---|---|
| 1 | Syntax | `make syntax` | ✅ PASS |
| 2 | Logical consistency | `make reason` | ✅ PASS |
| 3 | SHACL constraints | `make shacl` | ✅ PASS (real data, see below) |
| 4 | Conformance with source standards | `make conformance` | ✅ PASS |
| 5 | Header metadata | `make metadata` | ✅ PASS (7/7) |
| 6 | Design quality (OOPS!) | `make quality` | ✅ PASS |
| 7 | Structural metrics (ROBOT report) | `make metrics` | ✅ PASS |
| 8 | FAIR principles (FOOPS!) | `make fair` | ✅ PASS — 0.80/1.0 (real local run) |

All eight tests pass, with no exception. This is the result of verification work carried out in several successive waves, each more demanding than the last — the full detail of this journey, with citations and evidence, is in `decisions/fr/problemes-et-solutions.md` and in the chain of three independent audits (`auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md`).

## 1. Syntax: can the file be read?

The most elementary check: that `CAO_CRM-1.0.rdf` is a well-formed RDF/XML document, free of grammatical errors, verified by three independent readers (`rapper`, `riot`, `rdflib`) so as not to depend on any single one's blind spot. If this check failed, no other program could even open the file.

## 2. Logical consistency (reasoning)

A "reasoner" (here, HermiT) applies the model's logical rules to verify they lead to no contradiction, in particular to no "unsatisfiable class": a category defined such that it could, logically, never have a single real member. The test runs on the model merged with the three complete official sources (CIDOC-CRM, LRMoo, CRMdig) plus SKOS, not just on the isolated module — because a module can appear consistent on its own while hiding a contradiction that only surfaces once recombined with what it claims to extend.

## 3. SHACL constraints on real data

While logical consistency examines the model in the abstract, SHACL checks something more concrete: whether a specific dataset — a work, an author, a date — respects the shape rules imposed on it. It is a complementary layer to reasoning, oriented toward real data rather than abstract structure. The graph used (`test-data/stendhal-le-rouge-et-le-noir.ttl`) is not a synthetic example invented for the occasion: it applies the model's five levels to Stendhal's *Le Rouge et le Noir*, with two real cases verified against their sources (Henri Martineau's critical edition, digitized by the BnF/Gallica, and C. K. Scott Moncrieff's English translation, digitized by Internet Archive) — see `test-data/PROVENANCE-stendhal-verificacion.md` for the detail of each verification.

## 4. Conformance with the standards CAO_CRM extends

CAO_CRM invents no classes from nothing: it reuses elements from CIDOC-CRM, LRMoo, and CRMdig. This test compares the combined model against the official files of these standards to detect whether any original axiom was lost or silently contradicted during integration. The automated part today reports no lost axiom, beyond one harmless merge artifact (documented in `validation/06-conformance/out/conformance-notes.md`); a manual review of subclass relations is still recommended as a complement, out of caution.

## 5. Version and provenance metadata

This test verifies that the file's "identity card" — who created it, which version it is, under what license it is published — is complete, and that it contains no metadata pasted in by mistake from another ontology (a real incident that happened very early in this project — see "Frequently Asked Questions"). All 7 checks pass: presence of `owl:versionIRI`, `dc:creator`, `dc:rights`, `owl:versionInfo`, and absence of any contamination from SKOS.

## 6. Design quality (OOPS!)

OOPS! is an external service specializing in the "pitfalls" typical of ontology design, such as declaring that a property admits two domains at once, or the absence of disjointness between classes. Three pitfall categories (`P10`, `P19`, `P30`) are deliberately excluded from the analysis requested of the service, each for a reason verified and documented in `validation/04-quality/README.md` — among others, that CIDOC-CRM, LRMoo, and CRMdig themselves declare no class disjointness anywhere in their official releases, a deliberate design choice of this family of standards, not an oversight on CAO_CRM's part. What remains within the analyzed scope passes with no critical or important pitfall.

## 7. Structural metrics (ROBOT report)

This test scans the model for common oversights: properties lacking an explicit definition, labels duplicated between two terms, and so on. The `duplicate_label` rule was recalibrated from ERROR to WARN in the verification profile, after confirming that the 44 flagged occurrences exist, as such, in the official CIDOC-CRM and LRMoo files (sister properties that deliberately share the same verb in a given language) — this is not an oversight by CAO_CRM, and the remedy applied (a custom profile) is what ROBOT's own documentation recommends for this exact situation, already raised, separately, with the OBO Operations Committee.

## 8. FAIR principles

FAIR is a set of principles (that a resource be easy to find, access, combine with others, and reuse) used in open science. This test now runs for real, locally: the official FOOPS! release jar (version 0.4.0) is downloaded and run as a small server, then queried through its own documented REST endpoint (`assessOntologyFile`) — no need for the public online service, whose REST contract was never reliably documented. Score obtained: **0.80 out of 1.0** (Interoperable 3/3, Findable 3/4, Reusable 6/8; the Accessible dimension is not evaluated in local-file mode, since it requires a dereferenceable public URI). Reusable rose from 5/8 to 6/8 on July 14, once the ontology's Nakala DOI was added (`dcterms:identifier`). Full breakdown, dimension by dimension, is in `validation/08-fair/README.md`.

## Competency questions and auto-generated documentation

Two complementary steps, outside the `make validate` chain but just as real:
- **Competency questions** (`competency-questions/CQ-001-a-005-stendhal.md`) are now 5 concrete questions — who the original author is, in what language, where the copy is held, what rights apply, digitized vs. born-digital — plus 2 cardinality checks, each translated into a real SPARQL query (`sparql/ask/`, `sparql/select/`) run against the same Stendhal graph as SHACL. `make cq` runs them all.
- **Auto-generated HTML documentation** (via Widoco, see `docs/site/index-{en,fr,es}.html`) regenerates without error and today faithfully reflects CAO_CRM's own header, in all three languages — including the metadata added to close the FAIR gap.

## The overall picture

All eight test categories are today entirely green, with no exception and no warning swept under the rug, and the competency questions are real rather than a methodological skeleton. Every decision that led to this state — why a given rule was recalibrated, why another was deliberately excluded, how the test graph was built and verified — is documented with supporting evidence, rather than blindly trusting a "pass" or "fail" label.
