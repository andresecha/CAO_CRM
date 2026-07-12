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
# Application notes: the actor roles and the model's controlled values

This section gathers, for every role property specific to CAO_CRM and for every category of controlled value (`E55_Type`) used in the model, an **application note** in the same sense CIDOC-CRM itself uses this term: not just the formal definition (already given in the RDF file and in the other sections of this documentation), but a concrete example showing how the property or value is actually used, in the same vein as the style the official files themselves practice — an illustrative sentence appended after the scope note, never a redefinition.

## The five actor roles

The five subproperties of `P14_carried_out_by` declared in CAO_CRM (see `05-decisiones-adr.md`) all share the same domain (`E7_Activity`) and the same range (`E39_Actor`); what distinguishes them is only the role each specifies. Each corresponds to an official MARC Relator Terms code, and each is illustrated here with the *Le Rouge et le Noir* example already used throughout this documentation.

- **`P14_has_original_author`** ("has original author", MARC `aut`). Applies to the Work's creation event, `F27_Work_Creation`. For example: `F27_Work_Creation --P14_has_original_author--> Stendhal`, for the event of conceiving the novel as an intellectual project — independent of any later edition or translation.

- **`P14_has_translator`** ("has translator", MARC `trl`). Applies to an Expression's creation event, `F28_Expression_Creation`, when that Expression results from a translation. For example: `F28_Expression_Creation --P14_has_translator--> Elisabeth van Bebber`, for the event producing the German version of an Agatha Christie novel from the original English text (an example already developed in `informe-P14-roles-autorat.md`).

- **`P14_has_abridger`** ("has abridger", MARC `abr`). Also applies to `F28_Expression_Creation`, when the resulting Expression is a shortened version of the text, with no change of language. For example: `F28_Expression_Creation --P14_has_abridger--> [the person's name]`, for the event producing the abridged English version of *Murder on the Orient Express* mentioned in the project's source paper.

- **`P14_has_scientific_editor`** ("has scientific editor", MARC `edt`). Applies to the Manifestation's creation event, `F30_Manifestation_Creation`, or to a standalone scientific activity linked to an Item or a Digital Object. For example: `F30_Manifestation_Creation --P14_has_scientific_editor--> Henri Martineau`, for the event establishing the 1927 critical edition of *Le Rouge et le Noir* — revising the text and writing the preface, the intellectual responsibility for the content, distinct from the material production of the book.

- **`P14_has_publisher`** ("has publisher", MARC `pbl`). Applies to `F30_Manifestation_Creation` and to `F32_Item_Production_Event`. For example: `F30_Manifestation_Creation --P14_has_publisher--> Le Divan`, for that same 1927 edition, this time from the perspective of the publishing house responsible for publication and printing — a commercial and material responsibility, distinct from the scientific editor's, and carried by a different property on the same event.

These last two properties can coexist on one and the same `F30_Manifestation_Creation` event, each linked to a different actor: that is exactly what the *Le Rouge et le Noir* example shows, where both Le Divan and Henri Martineau are involved, each in a different capacity, in the existence of the same manifestation. Full detail on this distinction is in `decisions/fr/informe-activite-editoriale-scientifique.md`.

## The controlled values (`E55_Type`)

CIDOC-CRM provides, for a great many properties, a generic typing mechanism: `P2_has_type` links an entity to an `E55_Type` value, which plays the role of a controlled-vocabulary term (see the glossary, `08-glosario.md`, for the mechanism's formal definition). CAO_CRM uses it at several points in the model to specify categories for which neither CIDOC-CRM, LRMoo, nor CRMdig provides a dedicated subclass. Below, with a concrete example for each, are the categories of controlled values actually used in the model.

- **Manifestation type**, on `F3_Manifestation`. For example: "Edition," to distinguish a printed critical edition from an audiovisual edition or a reprint.

- **Production mode**, on the Manifestation's creation event. For example: "Printing," for the way the manifestation was materially produced.

- **Arrangement mode**, on `F5_Item`. For example: "Book," for the copy's physical form (as opposed to a leaflet, a notebook, a bundle of papers).

- **Format**, on `D1_Digital_Object`. For example: "PDF," for the digital object's file format.

- **Process type**, on `D2_Digitization_Process`/`D7_Digital_Machine_Event`. For example: "Scan," for the technical method used during digitization.

- **Rights type**, on `E30_Right`, at each level (Expression, Manifestation, Digital Object) where a patrimonial right is documented via `P104_is_subject_to`. For example: "Public domain," "Copyright," or "Intellectual property," depending on the legal regime applicable to the resource in question. Following the same mechanism, an associated note (`P3_has_note`) can spell out further detail ("Publisher/printer rights," "Digital reproduction rights").

- **Writing system**, on `F2_Expression` (co-typed `E33_Linguistic_Object`), directly following LRMoo's own official comment instruction for this class, and the same pattern CIDOC-CRM itself applies to `E34_Inscription`: *"The alphabet used can be documented by P2 has type: E55 Type."* For example: "Latin script," linked via `P127_has_broader_term` to a more general anchor, "Writing system type," which lets one programmatically distinguish this facet from other `E55_Type` values sharing the same `P2_has_type` property elsewhere in the model (see `decisions/fr/complete-model.md` (section 4) for the detail of this choice).

- **Activity type**, on the "editorial activities" branch (`F30_Manifestation_Creation`, or the standalone scientific activity linked to an Item or Digital Object — see the previous section). For example: "Critical revision," to precisely type the nature of the scientific work performed, or "Item collation," when the task is examining a particular physical copy rather than establishing the edition's text. This is the very mechanism the official comment on `F28_Expression_Creation` recommends for distinguishing, say, a translation from a revision: *"The P2 has type (is type of) property can be used to specify the type of the instance of F28 Expression Creation (i.e., activities such as translating, revising, or arranging music are types of creation process)."*

- **Identifier type**, on `E42_Identifier`, whenever a resource carries several identifiers of different natures. For example: "ISBN" or "ARK," to distinguish a standard commercial identifier from a persistent identifier assigned by an archival service (the model's own worked example already uses an identifier of the form `ark:/12148/cb119255047`).

- **State**, on `E3_Condition_State`, following exactly the example CIDOC-CRM's own official comment for this class gives: *"For example, the instance of E3 Condition State … can be characterized as an instance 'wrecked' of E55 Type."* For example, for a physical copy: "Good condition," as opposed to a damaged or fragile state.

- **Encoding type**, on `D1_Digital_Object`, to document the technical method by which the digital content was produced or OCR'd. For example: "OCR and IIIF," corresponding to optical character recognition combined with an IIIF image-presentation service.

In every case, the value itself remains a plain term — never a new class of CAO_CRM's own — it is the `E55_Type`/`P2_has_type` mechanism that carries the precision, exactly as CIDOC-CRM itself provides for its own classes.
