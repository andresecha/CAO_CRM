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
# Notes d'application : les rôles d'acteur et les valeurs contrôlées du modèle

Cette section rassemble, pour chaque propriété de rôle propre à CAO_CRM et pour chaque catégorie de valeur contrôlée (`E55_Type`) utilisée dans le modèle, une **note d'application** au sens où CIDOC-CRM emploie lui-même ce terme : non pas seulement la définition formelle (déjà donnée dans le fichier RDF et dans les autres sections de cette documentation), mais un exemple concret qui montre comment la propriété ou la valeur s'utilise réellement, dans le prolongement direct du style que les fichiers officiels eux-mêmes pratiquent — une phrase d'illustration ajoutée à la suite de la note de portée, jamais une redéfinition.

## Les cinq rôles d'acteur

Les cinq sous-propriétés de `P14_carried_out_by` déclarées dans CAO_CRM (voir `05-decisiones-adr.md`) partagent toutes le même domaine (`E7_Activity`) et la même portée (`E39_Actor`) ; ce qui les distingue est uniquement le rôle qu'elles précisent. Chacune correspond à un code MARC Relator Terms officiel, et chacune s'illustre ici avec l'exemple de *Le Rouge et le Noir* déjà utilisé tout au long de cette documentation.

- **`P14_has_original_author`** (« a pour auteur original », MARC `aut`). S'applique sur l'événement de création de l'Œuvre, `F27_Work_Creation`. Par exemple : `F27_Work_Creation --P14_has_original_author--> Stendhal`, pour l'événement de conception du roman en tant que projet intellectuel — indépendamment de toute édition ou traduction ultérieure.

- **`P14_has_translator`** (« a pour traducteur », MARC `trl`). S'applique sur l'événement de création d'une Expression, `F28_Expression_Creation`, lorsque cette Expression résulte d'une traduction. Par exemple : `F28_Expression_Creation --P14_has_translator--> Elisabeth van Bebber`, pour l'événement qui produit la version allemande d'un roman d'Agatha Christie à partir du texte anglais original (exemple déjà développé dans `informe-P14-roles-autorat.md`).

- **`P14_has_abridger`** (« a pour abréviateur », MARC `abr`). S'applique également sur `F28_Expression_Creation`, lorsque l'Expression produite est une version raccourcie du texte, sans changement de langue. Par exemple : `F28_Expression_Creation --P14_has_abridger--> [nom de la personne]`, pour l'événement qui produit la version abrégée anglaise de *Murder on the Orient Express* mentionnée dans le paper source du projet.

- **`P14_has_scientific_editor`** (« a pour éditeur scientifique », MARC `edt`). S'applique sur l'événement de création de la Manifestation, `F30_Manifestation_Creation`, ou sur une activité scientifique autonome liée à un Item ou à un Objet numérique. Par exemple : `F30_Manifestation_Creation --P14_has_scientific_editor--> Henri Martineau`, pour l'événement qui établit l'édition critique de 1927 de *Le Rouge et le Noir* — révision du texte et rédaction de la préface, la responsabilité intellectuelle sur le contenu, distincte de la production matérielle du livre.

- **`P14_has_publisher`** (« a pour éditeur commercial », MARC `pbl`). S'applique sur `F30_Manifestation_Creation` et sur `F32_Item_Production_Event`. Par exemple : `F30_Manifestation_Creation --P14_has_publisher--> Le Divan`, pour la même édition de 1927, cette fois du point de vue de la maison d'édition responsable de la publication et de l'impression — une responsabilité commerciale et matérielle, distincte de celle de l'éditeur scientifique, et portée par une propriété différente sur le même événement.

Ces deux dernières propriétés peuvent coexister sur un seul et même événement `F30_Manifestation_Creation`, chacune reliée à un acteur différent : c'est exactement ce que montre l'exemple de *Le Rouge et le Noir*, où Le Divan et Henri Martineau interviennent tous deux, à des titres différents, dans l'existence de la même manifestation. Le détail complet de cette distinction est dans `decisions/fr/informe-activite-editoriale-scientifique.md`.

## Les valeurs contrôlées (`E55_Type`)

CIDOC-CRM prévoit, pour de très nombreuses propriétés, un mécanisme de typage générique : `P2_has_type` relie une entité à une valeur `E55_Type`, qui joue le rôle d'un terme de vocabulaire contrôlé (voir le glossaire, `08-glosario.md`, pour la définition formelle du mécanisme). CAO_CRM l'utilise à plusieurs endroits du modèle pour préciser des catégories que ni CIDOC-CRM, ni LRMoo, ni CRMdig ne prévoient de sous-classe dédiée pour représenter. Voici, avec un exemple concret pour chacune, les catégories de valeurs contrôlées effectivement utilisées dans le modèle.

- **Type de manifestation**, sur `F3_Manifestation`. Par exemple : « Édition », pour distinguer une édition critique imprimée d'une édition audiovisuelle ou d'une réimpression.

- **Mode de production**, sur l'événement de création de la Manifestation. Par exemple : « Impression », pour la manière dont la manifestation a été matériellement produite.

- **Mode d'agencement**, sur `F5_Item`. Par exemple : « Livre », pour la forme physique de l'exemplaire (par opposition à un feuillet, un carnet, une liasse).

- **Format**, sur `D1_Digital_Object`. Par exemple : « PDF », pour le format de fichier de l'objet numérique.

- **Type de processus**, sur `D2_Digitization_Process`/`D7_Digital_Machine_Event`. Par exemple : « Scan », pour la méthode technique employée lors de la numérisation.

- **Type de droit**, sur `E30_Right`, à chacun des niveaux (Expression, Manifestation, Objet numérique) où un droit patrimonial est documenté via `P104_is_subject_to`. Par exemple : « Domaine public », « Droit d'auteur » ou « Propriété intellectuelle », selon le régime juridique applicable à la ressource concernée. Suivant le même mécanisme, une note associée (`P3_has_note`) peut préciser le détail (« Droits éditeurs/imprimeurs », « Droits de reproduction numérique »).

- **Système d'écriture**, sur `F2_Expression` (co-typée `E33_Linguistic_Object`), suivant directement la propre instruction du commentaire officiel de LRMoo pour cette classe, et le patron que le CIDOC-CRM applique lui-même à `E34_Inscription` : *« The alphabet used can be documented by P2 has type: E55 Type. »* Par exemple : « Écriture latine », reliée par `P127_has_broader_term` à une ancre plus générale, « Type de système d'écriture », qui permet de distinguer programmatiquement cette facette d'autres valeurs `E55_Type` partageant la même propriété `P2_has_type` ailleurs dans le modèle (voir `complete-model.md` (section 4) pour le détail de ce choix).

- **Type d'activité**, sur la branche « activités éditoriales » (`F30_Manifestation_Creation`, ou l'activité scientifique autonome liée à un Item ou un Objet numérique — voir la section précédente). Par exemple : « Révision critique », pour typer précisément la nature du travail scientifique accompli, ou « Collation d'exemplaire » lorsqu'il s'agit d'examiner un exemplaire physique particulier plutôt que d'établir le texte de l'édition. C'est le mécanisme même que le commentaire officiel de `F28_Expression_Creation` recommande pour distinguer, par exemple, une traduction d'une révision : *« The P2 has type (is type of) property can be used to specify the type of the instance of F28 Expression Creation (i.e., activities such as translating, revising, or arranging music are types of creation process). »*

- **Type d'identifiant**, sur `E42_Identifier`, chaque fois qu'une ressource porte plusieurs identifiants de nature différente. Par exemple : « ISBN » ou « ARK », pour distinguer un identifiant commercial standard d'un identifiant pérenne attribué par un service d'archives (le modèle utilise déjà, dans son exemple travaillé, un identifiant de la forme `ark:/12148/cb119255047`).

- **Etat**, sur `E3_Condition_State`, suivant exactement l'exemple que le commentaire officiel de cette classe CIDOC-CRM donne lui-même : *« For example, the instance of E3 Condition State … can be characterized as an instance "wrecked" of E55 Type. »* Par exemple, pour un exemplaire physique : « Bon état », par opposition à un état endommagé ou fragile.

- **Type d'encodage**, sur `D1_Digital_Object`, pour documenter la méthode technique par laquelle le contenu numérique a été produit ou océrisé. Par exemple : « OCR et IIIF », correspondant à la reconnaissance optique de caractères combinée à un service de présentation d'images IIIF.

Dans chaque cas, la valeur elle-même reste un simple terme — jamais une nouvelle classe propre à CAO_CRM : c'est le mécanisme `E55_Type`/`P2_has_type` qui porte la précision, exactement comme CIDOC-CRM le prévoit pour ses propres classes.
