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
# Comment le fichier RDF du modèle a été construit, expliqué pas à pas

## Deux mots avant de commencer

Un fichier **RDF** (ou **RDF/OWL**, presque la même chose, avec davantage de règles logiques par-dessus) est une liste d'affirmations simples du type « ceci est un type de chose » ou « cette chose est en relation avec cette autre chose de telle façon » — des milliers de ces affirmations réunies, dans un format qu'une personne comme un programme peuvent lire sans ambiguïté. C'est la version formelle du modèle CAO_CRM : non pas un dessin, mais le fichier qu'un programme peut réellement charger et utiliser. Ce document raconte, pas à pas, comment on est passé du diagramme qui décrit CAO_CRM au fichier final : `ontology/CAO_CRM-1.0.rdf` (1165 triplets, 41 classes, 84 propriétés d'objet, 5 propriétés de données).

## Le point de départ : un diagramme, pas un texte

L'article du consortium Ariane présente CAO_CRM au moyen d'un diagramme, qui existe également comme fichier de travail au format Drawio (un format pour dessiner et annoter des schémas), réparti sur 9 pages : la colonne vertébrale du modèle (Œuvre, Expression, Manifestation, Item physique, Objet numérique), un bloc pour chacun de ces éléments, le processus de numérisation, une vue d'ensemble et un exemple complet à partir d'un roman concret (*Le Rouge et le Noir*, de Stendhal).

Chaque case ou flèche du diagramme porte un texte attaché : parfois le nom technique exact d'un élément de CIDOC-CRM, LRMoo ou CRMdig (comme `E35_Title`), parfois seulement une étiquette descriptive en français (comme « Titre »). Le premier travail a consisté à distinguer, parmi des centaines d'étiquettes, celles qui étaient des éléments du modèle formel de celles qui n'étaient que du texte explicatif — puis, une fois cette première extraction faite, à revérifier patiemment le diagramme lui-même contre les fichiers officiels, case par case et flèche par flèche, pour trouver ce qui manquait ou ce qui était employé de façon incorrecte.

## Étape 1 — Extraire le module initial avec ROBOT

Une analogie peut aider ici : CIDOC-CRM, LRMoo et CRMdig sont, ensemble, comme trois énormes ouvrages de référence. CAO_CRM n'a besoin que d'une poignée de pages de chacun d'eux — celles qui définissent les éléments repérés dans le diagramme. « Extraire un module » signifie photocopier uniquement ces pages, plutôt que de photocopier les trois ouvrages entiers.

Cette extraction n'a pas été réalisée à la main, mais au moyen d'un outil appelé **ROBOT**, dans son mode `extract`/`subset` (extraire un sous-ensemble exact) :

```bash
robot extract --input imports/vendor/cidoc-crm-7.1.3.rdf \
              --method subset --term-file imports/module-terms.txt \
              --output ontology/CAO_CRM.rdf
```

Le mode `subset` est essentiel : contrairement à d'autres modes, qui entraînent automatiquement toute la hiérarchie au-dessus de ce qui est demandé, `subset` extrait uniquement les termes indiqués dans `imports/module-terms.txt`, et rien de plus — la liste exacte, vérifiable, qui fait tenir tout le module dans une centaine de termes plutôt que dans les milliers que comptent les trois ontologies complètes.

## Étape 2 — Huit problèmes trouvés en comparant le diagramme aux fichiers officiels

Une fois le premier module extrait, il fallait vérifier qu'il correspondait réellement à ce que le diagramme du consortium voulait exprimer, et que chaque relation dessinée était légale au regard des règles officielles (quelle classe peut porter quelle propriété). Cette vérification, menée systématiquement page par page, a mis au jour huit problèmes réels — documentés en détail, avec citation officielle complète pour chacun, dans `decisions/fr/problemes-et-solutions.md` :

1. **La description d'un objet** (`P3_has_note`) passait par une chaîne artificielle (`E55_Type` → `E62_String`) au lieu d'une note directe — et `E62_String`, comme `E60_Number` plus loin, n'existe d'ailleurs pas comme classe réelle dans CIDOC-CRM : ce sont des « valeurs primitives », toujours représentées comme du texte ou un nombre simple, jamais comme une entité dotée de sa propre identité.
2. **La langue d'une Expression** était rattachée au mauvais niveau (`F3_Manifestation`) et par la mauvaise propriété — corrigé en la plaçant sur `F2_Expression`, co-typée `E33_Linguistic_Object`, via `P72_has_language`, exactement comme LRMoo le prescrit dans son propre commentaire officiel pour cette classe.
3. **La localisation d'un exemplaire physique** (`F5_Item`) n'avait aucun mécanisme légal — résolu en co-typant l'exemplaire comme `E22_Human-Made_Object` (une pratique que le commentaire officiel de `F5_Item` sanctionne explicitement) pour lui permettre `P54`/`P55_has_current_location`.
4. **Les droits** (`P104_is_subject_to`) étaient dessinés sur des classes qui ne peuvent légalement pas en être sujettes (`F1_Work`, certaines activités) — résolu en distinguant droit moral (rattaché à l'auteur de l'Œuvre via le chemin déjà légal `F27_Work_Creation`) et droits patrimoniaux (cessibles, rattachés à l'Expression ou à la Manifestation).
5. **La production d'un exemplaire** utilisait un événement générique — remplacé par `F32_Item_Production_Event`, la classe LRMoo spécifiquement prévue pour cela.
6. **L'objet numérique portant une dimension** (poids en octets, résolution) utilisait `D1_Digital_Object` directement — corrigé en co-typant `D9_Data_Object`, exactement la classe que le commentaire officiel de CRMdig indique pour porter `L61_contains_value_set_of`.
7. **Les dimensions physiques** manquaient d'unité de mesure — ajouté via `P91_has_unit`/`E58_Measurement_Unit`.
8. **La précision des dates** avait perdu, lors de la première extraction, le typage XSD que le fichier original de Mélanie Bouland avait pourtant correctement — restauré (`xsd:dateTime`, `xsd:integer`) sans rien retirer de ce que le module avait déjà.

Un neuvième cas, plus subtil, a nécessité de revoir une conclusion antérieure : une branche du diagramme distinguait la numérisation d'un objet physique existant (`D2_Digitization_Process`) de la production directement numérique, sans support physique préalable. Une première analyse avait conclu à une erreur de copier-coller à corriger en supprimant la branche ; un examen plus approfondi du texte du paper a montré qu'il s'agissait au contraire d'une distinction voulue par l'équipe, seulement implémentée avec la mauvaise classe technique — corrigée en la retypant `D7_Digital_Machine_Event`, la classe CRMdig générale dont `D2_Digitization_Process` n'est qu'une spécialisation, sans exiger d'objet physique en entrée.

## Étape 3 — Compléter la matrice des 4 catégories × 5 classes

Le paper du consortium organise chaque niveau du modèle (Œuvre, Expression, Manifestation, Item, Objet numérique) selon quatre catégories transversales : Caractéristiques, Processus, Statut, Relation. Une vérification exhaustive de cette matrice (documentée dans `decisions/fr/complete-model.md`) a permis de trouver et combler trois manques réels : les relations entre expressions (`R75_incorporates`, `R76_is_derivative_of`), les relations entre œuvres (`R2_is_derivative_of`), et le chemin légal complet reliant un événement de production à l'exemplaire qu'il produit (`R28_produced`, ajoutée le 7 juillet après avoir constaté que le diagramme l'utilisait déjà mais que le module RDF ne l'avait pas encore).

## Étape 4 — Des rôles d'acteur qu'aucune propriété officielle ne distinguait

Le paper distingue plusieurs rôles autour d'un même texte, qu'aucune propriété officielle de CIDOC-CRM ne différencie nativement : une seule propriété générique, `P14_carried_out_by`, couvre n'importe quel rôle dans n'importe quelle activité. La solution retenue s'appuie sur une règle que CIDOC-CRM énonce lui-même dans son propre préambule (l'« Encoding Rule 4 ») : elle autorise explicitement la création de sous-propriétés nommées pour préciser un rôle, avec un exemple concret fourni par le standard. Au niveau de l'Expression, trois rôles d'auteur (auteur original, traducteur, personne ayant réalisé une version abrégée) sont ainsi distingués par `P14_has_original_author`, `P14_has_translator` et `P14_has_abridger`, chacune alignée sur le vocabulaire MARC Relator Terms international. Le détail complet, options écartées comprises, se trouve dans `decisions/fr/informe-P14-roles-autorat.md`.

Le même principe s'étend à la Manifestation : le paper y distingue explicitement la responsabilité de l'éditeur commercial (celui qui publie et imprime, comme Le Divan pour l'édition de 1927 de *Le Rouge et le Noir*) de celle de l'éditeur scientifique (celui qui établit le texte critique et rédige la préface, comme Henri Martineau) — deux rôles portés respectivement par `P14_has_publisher` et `P14_has_scientific_editor` sur le même événement `F30_Manifestation_Creation`. Cette dernière propriété s'applique aussi, séparément, à l'Item et à l'Objet numérique, chaque fois qu'une activité scientifique distincte (collation d'un exemplaire, choix éditoriaux sur une édition numérique) engage la responsabilité d'un spécialiste indépendamment du travail matériel de production. Le détail complet, avec la citation du paper et la justification de chaque niveau, se trouve dans `decisions/fr/informe-activite-editoriale-scientifique.md`.

## Étape 5 — Restaurer un domaine perdu lors de la première extraction

Une dernière vérification, menée avant la publication, a révélé que quatre propriétés très générales (`P4_has_time-span`, `P7_took_place_at`, `P16_used_specific_object`, `P104_is_subject_to`, et leurs inverses) avaient perdu leur domaine ou leur portée officiels lors de la toute première extraction : la classe qu'elles exigent (`E72_Legal_Object`, `E2_Temporal_Entity`, `E4_Period`, `E70_Thing`) n'avait jamais été incluse dans le module, faute d'être nécessaire comme case visible du diagramme. Ces quatre classes, purement abstraites, ont été ajoutées pour restaurer la contrainte d'origine, sans rien changer d'autre.

## Étape 6 — Vérifier, à chaque étape, que le fichier fonctionne réellement

Chaque ajout décrit ci-dessus a été suivi des mêmes vérifications : que le fichier reste bien formé (trois lecteurs indépendants), que le modèle reste logiquement cohérent une fois fusionné avec les trois sources officielles complètes (raisonneur HermiT), qu'aucun axiome des sources d'origine n'ait été perdu en chemin, et qu'il s'ouvre sans problème dans Protégé. Le détail complet de cette chaîne de vérification fait l'objet de la section suivante de cette documentation.

## Une dernière vérification indépendante : trois audits successifs

Avant de considérer le travail terminé, trois audits indépendants et successifs ont revérifié, chacun sans faire confiance au précédent, l'ensemble des affirmations de ce processus contre les fichiers sources eux-mêmes plutôt que contre des résumés : un audit du RDF terme par terme, un audit de la documentation et de la conformité conceptuelle de chaque décision, et une vérification croisée finale. Le verdict de cette chaîne : aucun défaut critique non documenté ne subsiste. Le détail complet se trouve dans `decisions/fr/auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md` et `auditoria-3-verificacion-final.md`.
