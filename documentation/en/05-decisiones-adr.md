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
# Decisions made while building the model, and why

## A model that sets out to invent nothing

CAO_CRM (Corpus Author Ontology CRM) creates no classes or properties of its own. Its work consists of **selecting and assembling** pieces that already exist in three official cultural-heritage models — CIDOC-CRM (the general standard for entities and events), LRMoo (the bibliographic standard for works, expressions, manifestations, and items), and CRMdig (the extension for digital objects) — without reinterpreting them or adding new content to them. This principle, which the team calls "composition of existing fragments," matters just as much to understanding the model as any of its classes.

The trouble is that no official standard covers every detail with equal precision everywhere. When the team ran into such gaps or ambiguities, it had to decide how to act without betraying this principle, and kept a record of these decisions in documents called **ADRs** (*Architecture Decision Records*: a short text laying out a problem, the options considered, and the one chosen). All of them share the same method: before deciding, the team looked for **verified textual citations** from CIDOC-CRM's official documentation — not internal opinions — to support each argument.

## The `P3_has_note` case: what kind of value a "note" accepts

CIDOC-CRM has a property, `P3_has_note` ("has note"), used to attach an informal description to any entity — for instance, noting that a physical item "has note: deteriorated condition on the spine." The problem is that the official file actually used to process the model (`CIDOC_CRM_v7.1.3.rdfs`) declares the property but **does not explicitly state** what kind of value it accepts on the other side — any text, or something more technically precise (an "XSD type")? This gap exists in the official file itself; it is not something CAO_CRM created, and it had in fact already caused a logical contradiction that an automated checking program (a "reasoner") detected on its own.

Two paths were possible. The first was to follow the convention CIDOC-CRM itself applies to an already well-declared sister property, `P90_has_value` ("has value"): although it conceptually represents a number, the official file types it with the broadest possible category of simple value (`rdfs:Literal`, "any text or simple datum, with no further precision"), and the file's own encoding-rules comment recommends this same scheme for properties like `P3_has_note`. The second was to type the property more strictly, requiring for instance that it be text (`xsd:string`), which would have allowed finer automatic validation — useful for AMIS, the AI-driven metadata-generation assistant.

The team chose the first option, for the following reason: scoping down which elements of the standards are used is consistent with CAO_CRM's goal, "but further restricting the internal meaning of one of these elements (...) would no longer be 'scoping the perimeter,' it would be conceptually modifying a CIDOC-CRM application note — exactly what the project set out not to do." Filling a gap by following the original authors' own logic completes the model; filling it with a criterion invented by the team would start redefining it, however well-intentioned.

## ADR-001: why certain categories are not declared mutually exclusive

There is a mechanism, `owl:disjointWith` ("disjoint with"), that lets one state "these two categories can never apply to the same thing at once" — for instance, forbidding a single event from being recorded as both a birth and a death, so that a data-entry error would be automatically detectable. The team checked that CAO_CRM's module contained no such declaration, and that CIDOC-CRM itself barely uses it for any of its categories: a deliberate choice by the consortium, which prefers to leave this kind of restriction to each project using the model rather than imposing it from the general standard.

The decision was to add none, following the same logic as the previous case: imposing a restriction CIDOC-CRM deliberately avoids would be a modeling decision of the team's own, not a composition of existing elements. The document leaves a door open: if AMIS in the future produces real data-entry errors that such a restriction would have prevented, the decision can be revisited, but based on actual usage evidence and documented again, not as a precaution taken in advance.

## ADR-002: why some terms are kept only in English

The third case is linguistic. CIDOC-CRM offers, for nearly all of its terms, human-readable labels (`rdfs:label`, the "human" name of a class or property) in up to seven languages. But upon examining the official LRMoo and CRMdig files, the team found that the terms CAO_CRM borrows from these two sources **only exist with an English label**: no other language is available for them in the official source.

The question was whether to add a translation, say into French (Ariane's working language). The decision was not to, for the reason tying all three cases together: a translation would be content CAO_CRM produced on its own initiative, not something borrowed from an official source. The document states it plainly: this "contradicts the principle of pure composition (...): CAO_CRM must not generate its own content about the elements it reuses, only select and compose them as they exist." Here too, it is specified how to proceed should this ever be judged indispensable: explicitly mark the translation as an annotation added by CAO_CRM (not as though it were an official LRMoo or CRMdig label), and document it in a new decision record.

## A fourth, later case, following exactly the same principle

After these first three decisions, a more substantial need arose: the consortium's paper distinguishes three authorship roles (original author, translator, person who produced an abridged version), which CIDOC-CRM does not natively differentiate — a single generic property, `P14_carried_out_by`, covers any role in any activity. Here too the temptation could have been to invent a solution of its own. But CIDOC-CRM itself provides, in its own preamble (a rule the standard's authors call "Encoding Rule 4"), the exact procedure for this kind of need: create named subproperties, with a concrete example the standard itself provides for an analogous case (`P3_parts_description`, a subproperty of `P3_has_note`). Three subproperties were thus declared following this pattern to the letter — `P14_has_original_author`, `P14_has_translator`, `P14_has_abridger` — aligned with the international MARC Relator Terms vocabulary. Full detail, with the rule's complete citation and the discarded alternatives, is in `decisions/fr/informe-P14-roles-autorat.md`.

## A fifth case, this one structural

The paper also presents, as one of CAO_CRM's original differentiators from plain LRMoo, a branch of "editorial activities" added to the Manifestation, letting one signal a scientific editor's intervention in establishing a version of the text — a gap, the paper itself says, in the standard LRMoo model. This case differs from the four preceding ones: it is not just about specifying a role on an already-covered relation, but about distinguishing two real responsibilities that had until then been conflated at the Manifestation level — the commercial publisher's, who publishes and prints, and the scientific editor's, who establishes the text's content. Following the same pattern as the first four cases (Encoding Rule 4), two further subproperties were declared: `P14_has_scientific_editor` and `P14_has_publisher`, each aligned with its own MARC Relator Terms code (`edt`, `pbl`). Full detail, with the paper's citation and the justification for each level (Manifestation, Item, Digital Object), is in `decisions/fr/informe-activite-editoriale-scientifique.md`.

## The common thread

The five cases — a missing data type, an undeclared logical restriction, a missing translation, a role distinction that did not exist, an undistinguished editorial responsibility — are all resolved by the same underlying question: does this decision complete the model by following the logic its own authors already used in equivalent cases, or does it introduce a new criterion the team would be adding on its own? When the answer is the former, the decision is adopted, with the official textual citation as support. When it would be the latter, the decision is set aside, however technically convenient it might be, unless it is at some point explicitly shown, with real evidence, why it is worth breaking this general rule. This same thread later guided the resolution of the eight modeling problems found while exhaustively comparing the diagram against the official files — see `decisions/fr/problemes-et-solutions.md` for that more recent and more extensive chapter of the same story.
