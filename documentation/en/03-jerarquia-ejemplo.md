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
# The model's hierarchy, explained through a real example

## Five ways of existing

When we say "I have Stendhal's *Le Rouge et le Noir* on the table," we unknowingly mix together several distinct realities: the novel as intellectual creation, the text as Stendhal wrote it, the specific edition we bought, the physical book with its pages and cover, and perhaps also the PDF we downloaded to read on a tablet. CAO_CRM (Corpus Author Ontology CRM), the Ariane consortium's model presented in the first section of this documentation, explicitly separates these layers, because conflating them has real consequences: the copyright over the work is not the same as the publishing rights attached to a specific edition; the conservation state of a library copy says nothing about the quality of a scan circulating on the Internet; and a "first version" of a novel can refer either to a change in the author's ideas or to a mere typographical change made by the printer.

The consortium's paper sums it up this way: *"le modèle repose sur une progression allant de l'œuvre comme concept abstrait à ses différentes formes matérielles ou numériques"*: the model organizes five entities (categories of things) in a progression running from the work as abstract idea to its material or digital forms, each corresponding to a distinct "mode of existence" of the same text. This progression, inherited from LRMoo (the bibliographic extension covered in the previous section), is: **F1_Work → F2_Expression → F3_Manifestation → F5_Item → D1_Digital_Object**.

## F1_Work: the idea, before any writing

`F1_Work` is the work in its purely conceptual dimension: *"corresponde au projet dans sa forme la plus abstraite, indépendamment de toute réalisation matérielle ou de toute mise en forme particulière"* (it corresponds to the project in its most abstract form, independent of any material realization or particular formatting). In our example, `F1_Work` is "the novel Stendhal conceived around Julien Sorel," with its author (Henri Beyle, known as Stendhal), his life dates, and the literary movement it is associated with. At this level, not a single sentence has yet been written: it is the intellectual project, not its execution.

## F2_Expression: when the idea becomes text

`F2_Expression` designates the different identifiable renderings of that idea, independent of the physical documents that let us identify them. Here the text itself appears — the words, the order of the chapters — but without yet being tied to a specific edition. The paper illustrates this subtle but crucial distinction with Flaubert's case: *"la première idée de Madame Bovary de Flaubert, dont témoignent des lettres de Du Camp en juillet et août 1851, sont une expression de l'œuvre, distincte des expressions ultérieures que permet de reconstituer le reste de la correspondance de l'auteur"*: drafts attested by letters already existed before a finished manuscript, and every substantially different stage of the content counts as a distinct expression. The paper notes that this layer often goes unnoticed in ordinary bibliographic work.

## F3_Manifestation: the edition, with its publisher, year, and place

`F3_Manifestation` is where the notion of "edition" that any reader would recognize finally appears. LRMoo defines it as *"products rendering one or more Expressions... defined by both the overall content and the form of its presentation"*. The paper adds that a manifestation exists from the moment the work no longer lives solely in its creator's mind: it is not a specific copy, but the generic editorial form from which several objects can derive. Following a real example drawn from the project's materials, the manifestation of *Le Rouge et le Noir* used here is the "Édition critique imprimée de Le Rouge et le Noir (1830)," published by Le Divan in Paris in 1927, with Henri Martineau as the scholarly editor responsible for revising the text and writing the preface. The model distinguishes here two quite different responsibilities, each carried by a separate property on the same manifestation-creation event: Le Divan as commercial publisher (`P14_has_publisher`) and Henri Martineau as scientific editor responsible for the content (`P14_has_scientific_editor`). At this level, the publisher, date, place of production, format, or language are documented: data about the edition, not about the work or the physical copy.

## F5_Item: the concrete book one can touch

`F5_Item` designates a particular material copy: the physical object consulted or handled. Here we are no longer talking about "the 1927 Le Divan edition" in the abstract, but about a concrete volume: the 21 × 29.7 cm copy, printed on paper in black and red ink, in good conservation condition, kept today in a Paris library. The paper stresses that several items can correspond to a single manifestation: copies of that edition scattered across different libraries share the same manifestation, but each has its own conservation state, its own provenance, and its own material history — one may bear handwritten annotations, another a damaged cover.

## D1_Digital_Object: the file we consult on screen

Finally, `D1_Digital_Object` corresponds, per CRMdig, to *"identifiable immaterial items that can be represented as sets of bit sequences... A D1 Digital Object does not depend on a specific physical carrier"*. In our example, this would be the EPUB or PDF file of *Le Rouge et le Noir* now hosted by a digital library, with its own identifier, its weight in megabytes, and its own conditions of use, distinct from the rights governing the 1927 printed edition. The paper points out that the model provides, from `F3_Manifestation`, two complementary paths: one toward the material object (`F5_Item`), the other toward the digital object (`D1_Digital_Object`), and that these two paths are not mutually exclusive. If the file comes from scanning the physical book, the relation is documented through a `D2_Digitization_Process`, which records who performed the digitization, when, and with what tools; but a digital object can also be "born digital," without ever having existed on paper — this second case is documented with `D7_Digital_Machine_Event`, the general CRMdig class of which `D2_Digitization_Process` is only a specialization, precisely because it requires no source physical object.

## Why no layer is superfluous

Separating these five layers is not a theoretical whim: it lets us answer questions that would otherwise remain tangled. Does "good conservation state" describe the paper book or the PDF file? How many distinct editions of the novel exist, and how do they differ from drafts predating a finished text? Each question finds its answer at a different level, and it is precisely this separation that lets us cross-reference information without confusing a copy's physical condition with the licensing conditions of its digital copy.

## Who owns the rights? An answer at one precise level, not all at once

The question of copyright deserves a considered answer, because it actually mixes two distinct natures of right. **Moral right** (in the continental droit d'auteur sense) is inalienable: it protects the integrity of the work itself, independent of any given edition, and is answered uniquely from `F1_Work`, following the path `F1_Work → F27_Work_Creation → P14_has_original_author → Person` — the path LRMoo itself calls, in its own official comment, "the notion of the creator of the work." **Patrimonial rights** (transferable — publishing rights, digital reproduction rights) correctly attach, instead, to the level that concretely produced them: the Expression, the Manifestation, or the Digital Object, as the case may be, each via `P104_is_subject_to`. A single novel can thus have one unquestionable moral author, while having different publishing rights for each Manifestation and its own usage conditions for each digital copy — exactly what the five-layer separation lets us express without contradiction.
