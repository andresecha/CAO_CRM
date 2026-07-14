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
# Comment vérifie-t-on que le modèle est bien construit

## Pourquoi une batterie de tests est nécessaire, et pourquoi il ne suffit pas qu'il « s'ouvre sans erreur »

Un modèle ontologique tel que CAO_CRM (Corpus Author Ontology CRM, le modèle du consortium Ariane) est, au fond, un fichier texte doté d'une grammaire très stricte, qui décrit des classes (« Œuvre », « Personne », « Lieu »...), des propriétés qui les relient (« a pour auteur », « a pour titre »...) et des règles régissant la manière dont elles peuvent se combiner. Ce fichier peut être défaillant de façons très différentes : par une erreur typographique qui en empêche la lecture, en étant lisible mais logiquement contradictoire, en contredisant silencieusement les normes qu'il prétend étendre, ou encore en étant irréprochable tout en se révélant incapable de répondre aux questions réelles qui ont motivé sa construction.

C'est pourquoi le dépôt de validation applique une **chaîne de huit vérifications automatisées**, chacune conçue pour détecter un type de problème que les autres ne voient pas, exécutables en une seule commande (`make validate`) ou individuellement. Un avertissement qui vaut pour toutes : il ne suffit jamais de se fier à la ligne résumée du terminal, ni au fait qu'un outil « se termine sans erreur » — il faut ouvrir le rapport détaillé quand il existe. Cette discipline n'est pas théorique : au tout début du projet, un résumé indiquait « 0 problème » alors que le rapport réel contenait plusieurs problèmes graves, à cause d'une erreur dans le script de comptage lui-même (voir la section « Foire aux questions » de cette documentation pour ce cas et d'autres, conservés comme leçons).

## État actuel (10 juillet 2026, `CAO_CRM-1.0.rdf`, 1165 triplets, 41 classes, 84 propriétés d'objet, 5 propriétés de données)

| # | Test | Commande | Résultat |
|---|---|---|---|
| 1 | Syntaxe | `make syntax` | ✅ PASS |
| 2 | Cohérence logique | `make reason` | ✅ PASS |
| 3 | Contraintes SHACL | `make shacl` | ✅ PASS (données réelles, voir plus bas) |
| 4 | Conformité aux normes sources | `make conformance` | ✅ PASS |
| 5 | Métadonnées de l'en-tête | `make metadata` | ✅ PASS (7/7) |
| 6 | Qualité de conception (OOPS!) | `make quality` | ✅ PASS |
| 7 | Métriques structurelles (ROBOT report) | `make metrics` | ✅ PASS |
| 8 | Principes FAIR (FOOPS!) | `make fair` | ✅ PASS — 0,80/1,0 (exécution locale réelle) |

Les huit tests passent tous, sans exception. C'est le résultat d'un travail de vérification mené en plusieurs vagues successives, chacune plus exigeante que la précédente — le détail complet de ce parcours, avec citations et preuves, se trouve dans `decisions/fr/problemes-et-solutions.md` et dans la chaîne de trois audits indépendants (`auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md`).

## 1. Syntaxe : le fichier est-il lisible ?

Il s'agit de la vérification la plus élémentaire : que `CAO_CRM-1.0.rdf` soit un document RDF/XML bien formé, exempt d'erreurs de grammaire, vérifié par trois lecteurs indépendants (`rapper`, `riot`, `rdflib`) afin de ne pas dépendre du point aveugle d'un seul d'entre eux. Si cette vérification échouait, aucun autre programme ne pourrait même ouvrir le fichier.

## 2. Cohérence logique (raisonnement)

Un « raisonneur » (*reasoner*, ici HermiT) applique les règles logiques du modèle afin de vérifier qu'elles ne conduisent à aucune contradiction, en particulier à une « classe insatisfiable » : une catégorie définie de telle sorte qu'elle ne pourrait, logiquement, jamais avoir le moindre membre réel. Le test s'exécute sur le modèle fusionné avec les trois sources officielles complètes (CIDOC-CRM, LRMoo, CRMdig) plus SKOS, pas seulement sur le module isolé — car un module peut sembler cohérent en apparence tout en cachant une contradiction qui n'apparaît qu'une fois recombiné avec ce qu'il prétend étendre.

## 3. Contraintes SHACL sur des données réelles

Alors que la cohérence logique examine le modèle dans l'abstrait, SHACL vérifie quelque chose de plus concret : si un ensemble de données précis — une œuvre, un auteur, une date — respecte les règles de forme qui lui sont imposées. C'est une couche complémentaire au raisonnement, orientée données réelles plutôt que structure abstraite. Le graphe utilisé (`test-data/stendhal-le-rouge-et-le-noir.ttl`) n'est pas un exemple synthétique inventé pour l'occasion : il applique les cinq niveaux du modèle à *Le Rouge et le Noir* de Stendhal, avec deux cas réels et vérifiés contre leurs sources (l'édition critique de Henri Martineau, numérisée par la BnF/Gallica, et la traduction anglaise de C. K. Scott Moncrieff, numérisée par Internet Archive) — voir `test-data/PROVENANCE-stendhal-verificacion.md` pour le détail de chaque vérification.

## 4. Conformité aux normes que CAO_CRM étend

CAO_CRM n'invente pas de classes à partir de rien : il réutilise des éléments issus de CIDOC-CRM, de LRMoo et de CRMdig. Ce test compare le modèle combiné aux fichiers officiels de ces normes afin de détecter si un axiome d'origine a été perdu ou silencieusement contredit lors de leur intégration. La partie automatisée ne signale aujourd'hui aucun axiome perdu, au-delà d'un artefact de fusion sans conséquence (documenté dans `validation/06-conformance/out/conformance-notes.md`) ; une revue manuelle des relations de sous-classe reste recommandée en complément, par prudence.

## 5. Métadonnées de version et de provenance

Ce test vérifie que la « fiche d'identité » du fichier — qui l'a créé, de quelle version il s'agit, sous quelle licence il est publié — est complète, et qu'elle ne contient pas de métadonnées d'une autre ontologie collées par erreur (un incident réel qui s'est produit tôt dans ce projet — voir la « Foire aux questions »). Les 7 vérifications passent : présence de `owl:versionIRI`, `dc:creator`, `dc:rights`, `owl:versionInfo`, et absence de toute contamination provenant de SKOS.

## 6. Qualité de conception (OOPS!)

OOPS! est un service externe spécialisé dans les « pièges » (*pitfalls*) typiques de la conception d'ontologies, comme le fait de déclarer qu'une propriété admet deux domaines à la fois, ou l'absence de disjonction entre classes. Trois catégories de pitfalls (`P10`, `P19`, `P30`) sont délibérément exclues de l'analyse demandée au service, chacune pour une raison vérifiée et documentée dans `validation/04-quality/README.md` — notamment que CIDOC-CRM, LRMoo et CRMdig eux-mêmes ne déclarent aucune disjonction de classe nulle part dans leurs versions officielles, un choix de conception délibéré de cette famille de normes, pas un oubli de CAO_CRM. Ce qui reste dans le périmètre analysé passe sans aucun pitfall critique ni important.

## 7. Métriques structurelles (ROBOT report)

Ce test parcourt le modèle à la recherche de négligences courantes : propriétés dépourvues de définition explicite, étiquettes dupliquées entre deux termes, etc. La règle `duplicate_label` a été recalibrée d'ERROR à WARN dans le profil de vérification, après avoir vérifié que les 44 occurrences signalées existent, telles quelles, dans les fichiers officiels de CIDOC-CRM et LRMoo (des propriétés sœurs qui partagent délibérément le même verbe dans une langue donnée) — ce n'est pas une négligence de CAO_CRM, et le remède appliqué (un profil personnalisé) est celui que la documentation de ROBOT elle-même recommande pour ce cas de figure, déjà signalé par ailleurs à l'OBO Operations Committee.

## 8. Principes FAIR

FAIR est un ensemble de principes (qu'une ressource soit facile à trouver, à consulter, à combiner avec d'autres et à réutiliser) employé en science ouverte. Ce test s'exécute désormais réellement, en local : le jar officiel de FOOPS! (version 0.4.0) est téléchargé et lancé comme un petit serveur, puis interrogé via son propre point d'accès REST documenté (`assessOntologyFile`) — plus besoin du service public en ligne, dont le contrat REST n'a jamais été documenté de façon fiable. Score obtenu : **0,80 sur 1,0** (Interopérable 3/3, Trouvable 3/4, Réutilisable 6/8 ; la dimension Accessible n'est pas évaluée en mode fichier local, elle exige une URI publique déréférençable). Réutilisable est passé de 5/8 à 6/8 le 14 juillet, avec l'ajout du DOI Nakala de l'ontologie (`dcterms:identifier`). Le détail complet, dimension par dimension, est dans `validation/08-fair/README.md`.

## Questions de compétence et documentation générée automatiquement

Deux étapes complémentaires, hors de la chaîne `make validate` mais tout aussi réelles :
- Les **questions de compétence** (`competency-questions/CQ-001-a-005-stendhal.md`) sont désormais 5 questions concrètes — qui est l'auteur original, quelle langue, où se trouve l'exemplaire, quels droits, numérisé ou nativement numérique — plus 2 vérifications de cardinalité, chacune traduite en une requête SPARQL réelle (`sparql/ask/`, `sparql/select/`) et exécutée contre le même graphe Stendhal que SHACL. `make cq` les rejoue toutes.
- La **documentation HTML générée automatiquement** (par Widoco, voir `docs/site/index-{en,fr,es}.html`) se régénère sans erreur et reflète aujourd'hui fidèlement l'en-tête propre de CAO_CRM, dans les trois langues — y compris les métadonnées ajoutées pour fermer l'écart FAIR.

## Le résultat d'ensemble

Les huit catégories de test sont aujourd'hui entièrement vertes, sans aucune exception ni aucun avertissement passé sous silence, et les questions de compétence sont réelles plutôt qu'un squelette méthodologique. Chaque décision qui a permis d'atteindre cet état — pourquoi telle règle a été recalibrée, pourquoi telle autre a été délibérément exclue, comment le graphe de test a été construit et vérifié — est documentée avec sa preuve à l'appui, plutôt que de se fier aveuglément à une étiquette « réussi » ou « échoué ».
