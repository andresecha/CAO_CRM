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
# How to open and explore the CAO_CRM model in Protégé (a practical step-by-step guide)

## What Protégé is

Protégé is the software — free, open-source, developed by Stanford University — used to create and inspect **ontologies**: formal schemas defining which "kinds of things" exist in a domain (for example, "Work," "Person," "Digital Object") and how they relate to each other. No programming knowledge is required: it is a visual interface designed to read and edit a model without writing code.

The Ariane team uses version 5.6.8, installed here as a Flatpak application on Linux, but Protégé works the same way on Windows and Mac: the menus described below are identical. This guide covers only **exploring** the already-built model, not editing it.

## Step 1: opening the model file

CAO_CRM is distributed as an `.rdf` file (RDF/XML, a strict-grammar text format explained in another section of this documentation). The final file in Ariane's repository is called `ontology/CAO_CRM-1.0.rdf`.

To open it: in the menu bar, **File > Open...**, navigate to the folder containing the file and select it (it can also be dragged into the program's window). Protégé will take a few seconds to process it — CAO_CRM incorporates classes and properties from several international standards (CIDOC-CRM, LRMoo, CRMdig, among others) — then display it once loaded.

## Step 2: "Active Ontology" — the model's identity card

Once loading finishes, Protégé usually shows the **Active Ontology** tab first; if it does not appear, select it from the row of tabs at the top. It works as the file's identity card: it shows its IRI (a unique address identifying it on the web, without necessarily pointing to a real page), its version, its author, the license it is published under, and general comments. This is the right place to get a first sense of "what this file is" before going into detail. It is, incidentally, the same information another section of this documentation examines as evidence of quality: if this card is incomplete, or mixed with data from another ontology, this is where it is spotted at a glance.

## Step 3: "Entities" — where classes and properties live

The **Entities** tab is the heart of exploration: this is where one navigates through everything CAO_CRM defines. It has several sub-tabs:

- **Classes**: the list of "kinds of things" the model recognizes — for example, `F1_Work` (a work in the abstract) or `F2_Expression` (a concrete realization, such as a text in a given language) — shown as a collapsible hierarchical tree, since some classes are subtypes of others.
- **Object properties**: relations connecting an instance of one class to another, such as the one linking a work to the person who created it.
- **Data properties**: relations connecting an instance of a class to a simple value — text, date, number — not to another entity; for example, the property associating a work with the text of its title.
- **Annotation properties**: these document the model itself, without describing the domain, such as `rdfs:label` (a term's readable label) or `rdfs:comment` (its description).

Clicking a class or property name in the left-hand panel is enough for the rest of the screen to show its detailed information.

## Step 4: reading a class's or property's information

When a class or property is selected, Protégé displays several blocks worth recognizing:

- **The technical name**, at the top, usually including a code inherited from the standards CAO_CRM reuses (for example, `F1_Work`, where "F1" is the identifier LRMoo, the bibliographic standard this part of the model relies on, uses).
- **Labels (`rdfs:label`) in different languages**: since CAO_CRM inherits from international standards developed by communities from several countries, it is normal to find the same class or property with labels in English, French, German, Portuguese, Russian, or Chinese, each marked with its language code (`en`, `fr`, `de`...). This is neither an error nor a duplication, but the standard way of reading the same term in different languages.
- **The comment or definition** (`rdfs:comment`, sometimes `skos:definition`): the prose text explaining what the class or property means and how it should be used; usually the most useful piece of information for understanding its meaning without guessing from the technical name.
- **Superclasses** (`SubClassOf`): these indicate of which more general class the selected one is a particular case, that is, from which it inherits its meaning and basic rules. For example, `F32_Item_Production_Event` (the event of producing a physical item) is declared a subclass of `E12_Production`, a much more general CIDOC-CRM class — this relation is what guarantees that whatever is legal for a Production is also legal for an item-production event, with no need to redeclare it term by term.

For properties, the equivalent panel also shows the **domain** (which class may have this property) and the **range** (what value or class it may receive), indicating "who connects to whom" in that relation.

## The reasoner button

In the menu bar there is an option called **Reasoner**, with available engines such as HermiT or Pellet. In one sentence: the reasoner automatically checks whether the model's rules contradict one another, and along the way reveals relations that were not written explicitly but that logically follow from the others.

It is not necessary to enable it to explore the model, but doing so (**Reasoner > Start reasoner**, then comparing the "Asserted" view — what the model literally states — with the "Inferred" view — what follows from it) is a simple way to confirm that what one reads is, besides readable, logically consistent. This same check, applied systematically, is one of the quality checks described in the section devoted to model validation.

## One final recommendation

It is advisable to follow this order the first time: first the general card (**Active Ontology**), then the class tree, and only afterward the concrete properties. Protégé's search box (magnifying-glass icon, or `Ctrl+K`) lets one type "Work" or "Title" to jump straight to the term, without walking the whole tree by hand.
