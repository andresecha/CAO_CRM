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
# ADR-002 — Ne pas traduire les termes de LRMoo/CRMdig qui n'existent qu'en anglais

**État :** Décidé — 2026-07-03
**Décision prise par :** équipe CAO_CRM (Ariane)
**Type de décision :** restriction/délimitation d'un fragment réutilisé (ne crée rien de nouveau, ne modifie pas le modèle original)

## Contexte

Il a été vérifié, en examinant directement les fichiers officiels (`imports/vendor/lrmoo-1.1.1.rdf`, `imports/vendor/crmdig-5.0.rdf`), que les 7 classes et 15 propriétés de LRMoo, ainsi que les 3 classes et 8 propriétés de CRMdig utilisées par CAO_CRM, **ne possèdent de `rdfs:label` qu'en anglais** — aucune autre langue n'existe dans ces sources pour ces 25 termes (contrairement à CIDOC-CRM, qui propose bien jusqu'à 7 langues pour la plupart de ses termes). Détail complet dans `decisions/informe-completitud-labels-domain-range.md`, section 1.

## Décision

**Aucune traduction n'est ajoutée.** Les 25 termes de LRMoo/CRMdig restent uniquement en anglais dans le module de CAO_CRM.

## Raison

Ajouter une traduction en français (ou dans une autre langue) de ces termes constituerait, par définition, un contenu que CAO_CRM créerait lui-même — et non quelque chose de copié depuis une source officielle. Cela contredit le principe de pure composition qui régit tout le projet (voir problemes-et-solutions.md) : CAO_CRM ne doit pas générer de contenu propre sur les éléments qu'il réutilise, mais seulement les sélectionner et les composer tels qu'ils existent.

## À reconsidérer à l'avenir si...

Si l'équipe décide, à un moment donné, que la documentation en français est indispensable à l'usage pratique d'AMIS ou à la publication du modèle, cette traduction devrait :
1. Être marquée explicitement comme une annotation de CAO_CRM (par exemple, au moyen d'une propriété d'annotation propre telle que `cao:has_working_translation`, et non comme s'il s'agissait d'un `rdfs:label@fr` officiel de LRMoo/CRMdig), afin de ne pas donner la fausse impression que cette traduction est avalisée par les consortium LRMoo/CRMdig.
2. Être documentée dans un nouvel ADR, comprenant la liste complète des termes traduits et l'identité de leurs relecteurs.
