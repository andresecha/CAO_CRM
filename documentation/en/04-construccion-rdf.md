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
# How the model's RDF file was built, explained step by step

## Two words before starting

An **RDF** file (or **RDF/OWL**, nearly the same thing, with more logical rules layered on top) is a list of simple statements of the type "this is a kind of thing" or "this thing relates to that other thing in such a way" — thousands of such statements gathered together, in a format both a person and a program can read unambiguously. It is the formal version of the CAO_CRM model: not a drawing, but the file a program can actually load and use. This document tells, step by step, how we went from the diagram describing CAO_CRM to the final file: `ontology/CAO_CRM-1.0.rdf` (1165 triples, 41 classes, 84 object properties, 5 data properties).

## The starting point: a diagram, not a text

The Ariane consortium's paper presents CAO_CRM through a diagram, which also exists as a working file in Drawio format (a format for drawing and annotating diagrams), spread across 9 pages: the model's backbone (Work, Expression, Manifestation, Physical Item, Digital Object), a block for each of these elements, the digitization process, an overview page, and a full worked example built around a real novel (*Le Rouge et le Noir*, by Stendhal).

Every box or arrow in the diagram carries an attached text label: sometimes the exact technical name of a CIDOC-CRM, LRMoo, or CRMdig element (like `E35_Title`), sometimes just a descriptive label in French (like "Titre"). The first task was to separate, among hundreds of labels, those that were elements of the formal model from those that were merely explanatory text — and then, once that first extraction was done, to patiently re-check the diagram itself against the official files, box by box and arrow by arrow, to find what was missing or incorrectly used.

## Step 1 — Extracting the initial module with ROBOT

An analogy may help here: CIDOC-CRM, LRMoo, and CRMdig are, together, like three enormous reference books. CAO_CRM only needs a handful of pages from each — those defining the elements identified in the diagram. "Extracting a module" means photocopying only those pages, rather than photocopying all three books whole.

This extraction was not done by hand, but with a tool called **ROBOT**, in its `extract`/`subset` mode (extract an exact subset):

```bash
robot extract --input imports/vendor/cidoc-crm-7.1.3.rdf \
              --method subset --term-file imports/module-terms.txt \
              --output ontology/CAO_CRM.rdf
```

The `subset` mode is essential: unlike other modes, which automatically pull in the entire hierarchy above what is requested, `subset` extracts only the terms listed in `imports/module-terms.txt`, and nothing more — the exact, verifiable list that keeps the whole module to about a hundred terms rather than the thousands the three complete ontologies together contain.

## Step 2 — Eight problems found by comparing the diagram against the official files

Once the first module was extracted, it had to be checked that it truly matched what the consortium's diagram meant to express, and that every relation drawn was legal under the official rules (which class may carry which property). This verification, carried out systematically page by page, uncovered eight real problems — documented in full, each with its complete official citation, in `decisions/fr/problemes-et-solutions.md`:

1. **The description of an object** (`P3_has_note`) went through an artificial chain (`E55_Type` → `E62_String`) instead of a direct note — and `E62_String`, like `E60_Number` further on, does not even exist as a real class in CIDOC-CRM: they are "primitive values," always represented as plain text or a plain number, never as an entity with its own identity.
2. **The language of an Expression** was attached to the wrong level (`F3_Manifestation`) and through the wrong property — fixed by placing it on `F2_Expression`, co-typed `E33_Linguistic_Object`, via `P72_has_language`, exactly as LRMoo itself prescribes in its own official comment for this class.
3. **The location of a physical item** (`F5_Item`) had no legal mechanism — resolved by co-typing the item as `E22_Human-Made_Object` (a practice the official comment on `F5_Item` explicitly sanctions), enabling `P54`/`P55_has_current_location`.
4. **Rights** (`P104_is_subject_to`) were drawn on classes that cannot legally bear them (`F1_Work`, certain activities) — resolved by distinguishing moral right (attached to the Work's author via the already-legal `F27_Work_Creation` path) from patrimonial rights (transferable, attached to the Expression or the Manifestation).
5. **The production of an item** used a generic event — replaced with `F32_Item_Production_Event`, the LRMoo class specifically intended for this.
6. **The digital object carrying a dimension** (byte size, resolution) used `D1_Digital_Object` directly — fixed by co-typing `D9_Data_Object`, exactly the class CRMdig's official comment names for carrying `L61_contains_value_set_of`.
7. **Physical dimensions** lacked a unit of measurement — added via `P91_has_unit`/`E58_Measurement_Unit`.
8. **Date precision** had lost, during the first extraction, the XSD typing that Mélanie Bouland's original file had correctly applied — restored (`xsd:dateTime`, `xsd:integer`) without removing anything the module already had.

A ninth, subtler case required revisiting an earlier conclusion: one branch of the diagram distinguished digitizing an existing physical object (`D2_Digitization_Process`) from directly digital production, with no prior physical carrier. A first analysis had concluded this was a copy-paste error to be fixed by removing the branch; a closer reading of the paper's text showed instead that this was an intentional distinction by the team, only implemented with the wrong technical class — corrected by retyping it as `D7_Digital_Machine_Event`, the general CRMdig class of which `D2_Digitization_Process` is merely a specialization, requiring no physical input object.

## Step 3 — Completing the 4-category × 5-class matrix

The consortium's paper organizes each level of the model (Work, Expression, Manifestation, Item, Digital Object) along four cross-cutting categories: Characteristics, Process, Status, Relation. An exhaustive check of this matrix (documented in `decisions/fr/complete-model.md`) found and filled three real gaps: relations between expressions (`R75_incorporates`, `R76_is_derivative_of`), relations between works (`R2_is_derivative_of`), and the complete legal path linking a production event to the item it produces (`R28_produced`, added on July 7 after noticing the diagram already used it while the RDF module did not yet have it).

## Step 4 — Actor roles no official property distinguished

The consortium's paper distinguishes several roles around a single text, which no official CIDOC-CRM property natively differentiates: a single generic property, `P14_carried_out_by`, covers any role in any activity. The solution adopted rests on a rule CIDOC-CRM itself states in its own preamble (what the standard's authors call "Encoding Rule 4"): it explicitly authorizes creating named subproperties to specify a role, with a concrete example provided by the standard itself. At the Expression level, three authorship roles (original author, translator, person who produced an abridged version) are distinguished this way via `P14_has_original_author`, `P14_has_translator`, and `P14_has_abridger`, each aligned with the international MARC Relator Terms vocabulary. Full detail, including discarded alternatives, is in `decisions/fr/informe-P14-roles-autorat.md`.

The same principle extends to the Manifestation: the paper explicitly distinguishes there the commercial publisher's responsibility (the one who publishes and prints, such as Le Divan for the 1927 edition of *Le Rouge et le Noir*) from the scientific editor's responsibility (the one who establishes the critical text and writes the preface, such as Henri Martineau) — two roles carried respectively by `P14_has_publisher` and `P14_has_scientific_editor` on the same `F30_Manifestation_Creation` event. This latter property also applies, separately, to the Item and the Digital Object, whenever a distinct scientific activity (collating a copy, editorial choices on a digital edition) engages a specialist's responsibility independent of the material work of production. Full detail, with the paper's citation and the justification for each level, is in `decisions/fr/informe-activite-editoriale-scientifique.md`.

## Step 5 — Restoring a domain lost during the first extraction

One last check, carried out before publication, revealed that four very general properties (`P4_has_time-span`, `P7_took_place_at`, `P16_used_specific_object`, `P104_is_subject_to`, and their inverses) had lost their official domain or range during the very first extraction: the class they require (`E72_Legal_Object`, `E2_Temporal_Entity`, `E4_Period`, `E70_Thing`) had never been included in the module, since it was not needed as a visible box in the diagram. These four purely abstract classes were added to restore the original constraint, changing nothing else.

## Step 6 — Verifying, at every step, that the file actually works

Every addition described above was followed by the same checks: that the file remains well-formed (three independent readers), that the model remains logically consistent once merged with the three complete official sources (HermiT reasoner), that no axiom from the original sources was lost along the way, and that it opens without trouble in Protégé. The full detail of this verification chain is the subject of the next section of this documentation.

## One last independent check: three successive audits

Before considering the work finished, three independent and successive audits re-verified, each without trusting the previous one, every claim made throughout this process against the source files themselves rather than against summaries: an audit of the RDF term by term, an audit of the decision documentation and the conceptual conformance of every choice, and a final cross-check. The verdict of this chain: no undocumented critical defect remains. Full detail is in `decisions/fr/auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, and `auditoria-3-verificacion-final.md`.
