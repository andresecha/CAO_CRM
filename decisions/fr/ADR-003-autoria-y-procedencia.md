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
# ADR-003 — Auteur, provenance et citation des outils dans l'en-tête

**État :** Décidé — le 3 juillet 2026
**Décision prise par :** Andrés Echavarría, sur instruction explicite de l'équipe AMIS
**Type de décision :** correction de métadonnées de provenance (sans incidence sur le modèle conceptuel ni sur le périmètre des classes et propriétés)

## Contexte

L'en-tête de `CAO_CRM-1.0.rdf` (`dc:creator`) indiquait, depuis le début de ce projet de validation : *« Model created by the Consortium HN Ariane and encoded by Mélanie Bouland »*. Cette formule était exacte pour le fichier RDF **d'origine** livré par Mélanie Bouland — mais elle ne l'est plus pour le fichier qui figure désormais dans ce dépôt, pour une raison précise, signalée explicitement par l'équipe :

> « Nous nous appuyons effectivement sur le modèle discuté et schématisé par Mélanie Bouland, mais le codage est entièrement nouveau ; en outre, des scripts et des techniques ont été utilisés et doivent être cités [...] car il ne s'agit pas de l'ontologie que Mélanie nous a livrée. »

Autrement dit : le **modèle conceptuel** (quelles classes et propriétés composer, comment elles se relient entre elles — documenté dans `CRM_V8.json` ainsi que dans l'article du consortium) demeure celui que Mélanie Bouland a discuté et schématisé. En revanche, le **fichier RDF/OWL concret** que l'on trouve dans `ontology/CAO_CRM-1.0.rdf` constitue une implémentation technique distincte, reconstruite intégralement selon une méthode différente (extraction de module avec ROBOT, raisonnement avec HermiT, validation visuelle dans Protégé — voir `decisions/informe-implementacion-RDF-modulo-acotado.md`) de celle qui avait produit le fichier original qu'elle avait livré. Maintenir la formule telle quelle revenait à attribuer le codage technique de ce fichier précis à quelqu'un qui ne l'avait pas réalisé.

## Décision

L'en-tête de l'ontologie distingue désormais explicitement **qui a conçu le modèle conceptuel** et **qui a construit ce fichier RDF concret** :

| Propriété | Valeur | Rôle |
|---|---|---|
| `dc:creator` | *« Conceptual model discussed and diagrammed by Mélanie Bouland, within the Consortium HN Ariane. »* | Paternité de la conception conceptuelle — non de ce fichier. |
| `dc:contributor` (1) | *« Andrés Echavarría -- RDF/OWL encoding, bounded module extraction and validation of this file (2026). This encoding is a new, independent implementation of the conceptual model above; it is not the RDF file originally delivered by Mélanie Bouland. »* | Paternité du codage technique de ce fichier précis, avec la précision explicite qu'il ne s'agit pas du fichier original. |
| `dc:contributor` (2) | *« AMIS team (Consortium HN Ariane) -- current maintainers of this encoding. »* | Traduit le fait que ce sont désormais l'équipe AMIS, et non plus « le consortium » de façon générique, qui reprend et assure la maintenance de ce travail. |
| `dc:description` | Réécrite pour intégrer ce qui précède dans une formulation lisible, avec les citations des outils (voir ci-dessous). | — |
| `dcterms:references` (×3) | `http://robot.obolibrary.org/`, `http://www.hermit-reasoner.com/`, `https://protege.stanford.edu/` | Citation structurée (pas seulement en prose) des outils employés pour construire et valider ce fichier. |

**Direction scientifique.** Le codage technique attribué à Andrés Echavarría dans `dc:contributor` (1) a été réalisé sous la direction et avec le soutien scientifique de **Fatiha Idmhand**, comme le reflète déjà la mention de provenance ajoutée à l'en-tête de tous les fichiers de ce projet (voir le commentaire introductif de ce même document : *« Encoding carried out under the scientific direction and support of Fatiha Idmhand »*). Cette direction scientifique est distincte de, et s'ajoute à, son rôle de contributrice nommée aux côtés du reste de l'équipe AMIS dans l'en-tête de `ontology/CAO_CRM-1.0.rdf`.

**Aucun assistant d'intelligence artificielle n'est cité comme auteur, contributeur ou outil.** Bien que le processus de reconstruction se soit déroulé avec l'assistance d'un assistant de programmation (Claude, d'Anthropic) piloté par Andrés Echavarría, la paternité intellectuelle et la responsabilité des choix de modélisation lui reviennent en propre — de même que la paternité d'un texte rédigé à l'aide d'un traitement de texte n'est pas attribuée au traitement de texte. Il s'agit d'une décision explicite de l'équipe, non d'un oubli.

## Outils cités, et pourquoi

- **ROBOT** (`http://robot.obolibrary.org/`) — l'outil en ligne de commande employé pour extraire le module borné (`robot extract --method subset`) ainsi que pour raisonner sur l'ontologie et produire les rapports de métriques et de conformité. Voir `decisions/informe-implementacion-RDF-modulo-acotado.md` pour le détail complet du processus.
- **HermiT** (`http://www.hermit-reasoner.com/`) — le raisonneur OWL DL utilisé (par l'intermédiaire de ROBOT) pour vérifier la cohérence logique du modèle à chaque itération.
- **Protégé** (`https://protege.stanford.edu/`) — l'éditeur d'ontologies utilisé pour la **validation visuelle** du fichier final : confirmer qu'il s'ouvre sans erreur, que le titre et l'en-tête s'affichent correctement, et pour l'inspection manuelle des classes et des propriétés pendant la reconstruction.

## Ce qui n'a pas été modifié

- Le `owl:versionIRI` (`http://www.CAO_CRM.org/ontology/2.0`) reste inchangé, afin de ne pas rompre la cohérence avec le reste du dépôt (scripts, documentation, noms de fichiers) qui le désigne déjà comme « 2.0 ».
- Le périmètre des classes et propriétés (les 29 + 61 + 5 déjà arrêtées) n'est pas affecté par cette décision — il s'agit purement d'une correction des métadonnées de provenance, non d'un choix de modélisation du domaine.

## Vérification

Après cette modification, l'ensemble des tests a été rejoué : syntaxe (réussi), raisonnement HermiT (réussi, cohérent), `validation/07-metadata/check.sh` (7/7 réussis, y compris les vérifications d'absence de contamination), et ouverture confirmée dans Protégé (titre de la fenêtre correct : `ontology (http://www.CAO_CRM.org/ontology/2.0)`).
