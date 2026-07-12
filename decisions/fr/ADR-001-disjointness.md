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
# ADR-001 — Ne pas ajouter de conditions `owl:disjointWith`

**État :** Décidé — 2026-07-03
**Décision prise par :** équipe CAO_CRM (Ariane)
**Type de décision :** restriction/délimitation d'un fragment réutilisé (ne crée rien de nouveau, ne modifie pas le modèle original)

## Contexte

`owl:disjointWith` est la manière, en OWL, d'exprimer que « ces deux classes ne peuvent jamais partager une même instance » — par exemple, déclarer que `E67_Birth` (naissance) et `E69_Death` (mort) sont disjointes empêcherait, par construction logique, qu'on enregistre par erreur un même événement comme relevant à la fois des deux catégories. Le raisonneur utiliserait cette déclaration pour détecter automatiquement ce type d'erreur de saisie de données.

Il a été vérifié que **le module actuel (`ontology/CAO_CRM-1.0.rdf`) ne comporte aucune déclaration `owl:disjointWith`**, et que **le fichier officiel de CIDOC-CRM 7.1.3 lui-même n'en déclare pas non plus** pour l'immense majorité de ses classes — il s'agit d'un choix de conception délibéré du consortium CIDOC-CRM (celui-ci préfère laisser la disjonction à l'appréciation de chaque implémentation concrète, plutôt que de l'imposer au niveau du modèle générique).

## Décision

**Aucune condition `owl:disjointWith` n'est ajoutée.** Le module reste fidèle à l'absence de disjonctions du fichier officiel.

## Raison

Conformément au même principe de composition pure appliqué dans tout le projet (voir, par exemple, problemes-et-solutions.md) : l'objectif de CAO_CRM est de délimiter *quelles pièces* de CIDOC-CRM/LRMoo/CRMdig sont utilisées ; imposer une restriction logique supplémentaire (une disjonction) que CIDOC-CRM lui-même évite délibérément reviendrait à introduire une décision de modélisation propre, et non une simple composition de fragments existants.

## Reconsidérer à l'avenir si...

Si, à l'avenir, AMIS (l'assistant de génération de métadonnées) venait à produire des erreurs de saisie réelles qu'une disjonction précise aurait permis de détecter, cette décision pourrait être reconsidérée — mais il s'agirait alors d'une décision fondée sur des éléments d'usage réel, documentée dans un nouvel ADR, et non d'une précaution spéculative prise par avance.
