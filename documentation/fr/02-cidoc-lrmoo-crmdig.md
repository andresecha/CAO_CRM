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
# Ce que sont CIDOC-CRM, LRMoo et CRMdig, et pourquoi CAO_CRM les combine


Lorsque le consortium Ariane a voulu décrire avec précision un corpus littéraire numérisé — pensons à un roman du XVIIIe siècle conservé sous forme de manuscrit, publié en plusieurs éditions imprimées et aujourd'hui également disponible sous forme de PDF numérisé dans une bibliothèque numérique —, il s'est heurté à un problème : aucun vocabulaire existant, pris isolément, ne permettait de parler à la fois de l'idée abstraite de l'œuvre, de ses éditions concrètes et de l'archive numérique qui la représente aujourd'hui. C'est pourquoi CAO_CRM (Corpus Author Ontology CRM) n'a pas été construite à partir de rien, mais en combinant trois « ontologies » déjà existantes et reconnues internationalement. Une ontologie, dans ce contexte, est simplement un modèle formel : un ensemble de catégories (des « classes ») et de relations entre elles, conçu pour que les personnes comme les programmes informatiques puissent décrire une même réalité de manière cohérente et partagée. Les trois éléments que CAO_CRM réutilise sont CIDOC-CRM, LRMoo et CRMdig, chacun couvrant une partie distincte du problème.

## CIDOC-CRM : le vocabulaire général du patrimoine culturel

CIDOC-CRM est une ontologie de référence pour les musées, les archives et les bibliothèques, adoptée à l'échelle internationale depuis plus de deux décennies et maintenue par un comité international (le CRM-SIG). Son trait le plus caractéristique — et celui que le document du consortium souligne tout particulièrement — est qu'elle ne se centre pas tant sur les objets en eux-mêmes que sur les **événements et processus** qui les entourent : création, transformation, transmission, conservation. La classe la plus générale de toutes, `E1 CRM Entity`, se définit comme *"an abstract concept providing for three general properties: Identification by name or appellation... Classification by type... Attachment of free text"* : c'est-à-dire la catégorie « parapluie » dont dérivent toutes les autres classes du modèle (personnes, objets, lieux, périodes, activités…), chacune identifiable, classifiable et documentable au moyen de notes libres.

Cette orientation vers les processus est précisément ce qui la rend utile pour un corpus littéraire : elle permet de documenter qui a produit un objet, quand et où, plutôt que de se limiter à décrire ses caractéristiques. Mais, comme le souligne le document, *"s'il constitue un cadre particulièrement puissant pour décrire les objets patrimoniaux, il demeure relativement général"*. CIDOC-CRM ne distingue pas, par exemple, entre l'idée intellectuelle d'un roman et chacune de ses éditions imprimées : il faut, pour cela, une extension plus spécifique.

## LRMoo : l'extension bibliographique (œuvre, expression, manifestation, item)

LRMoo est une extension de CIDOC-CRM construite à partir du modèle conceptuel de l'IFLA (la Fédération internationale des associations de bibliothécaires), conçue spécifiquement pour le monde bibliographique. Elle introduit quatre classes centrales qui permettent de distinguer des niveaux que le langage courant a tendance à confondre sous le seul mot « livre ». `F1 Work` est *"distinct intellectual ideas conveyed in artistic and intellectual creations"* : l'idée de l'œuvre, indépendante de toute forme concrète qu'elle puisse prendre. `F2 Expression` sont *"the intellectual or artistic realisations of Works... Differences in form imply different Expressions"* : chaque rédaction ou version textuelle identifiable de cette idée (une traduction, une version révisée). `F3 Manifestation` sont *"products rendering one or more Expressions... defined by both the overall content and the form of its presentation"* : la forme éditoriale concrète — une édition imprimée déterminée, avec son éditeur, son année, son format — qui matérialise une ou plusieurs expressions. Et `F5 Item` désigne l'exemplaire physique particulier qu'un lecteur peut tenir entre ses mains.

Cette échelle œuvre → expression → manifestation → item est exactement ce qui manquait à CIDOC-CRM pour traiter les corpus littéraires : elle permet de dire, par exemple, qu'une même œuvre possède plusieurs éditions sans les confondre entre elles. Mais, comme le prévient le document, *"si cette extension permet de prendre en charge la dimension bibliographique et éditoriale des textes, elle ne suffit toutefois pas à rendre compte des transformations liées à leur numérisation et à leur exploitation dans les environnements numériques contemporains"*. LRMoo a été conçue pour les catalogues de bibliothèques, non pour les archives numériques, les fichiers numérisés ou les processus de numérisation.

## CRMdig : l'extension des objets et processus numériques

CRMdig complète le tableau en ajoutant le vocabulaire qui manquait pour décrire le numérique. Sa classe centrale, `D1 Digital Object`, se définit comme *"identifiable immaterial items that can be represented as sets of bit sequences, such as data sets, e-texts, images, audio or video items, software, etc... A D1 Digital Object does not depend on a specific physical carrier"* : un fichier numérique identifiable, indépendant du support physique sur lequel il est stocké. À ses côtés, `D2 Digitization Process` couvre le passage d'un objet physique à sa version numérique, typiquement au moyen d'une numérisation ou d'une photographie. CRMdig est, selon les termes du document, l'élément qui *"permet de retracer la provenance des données et de documenter les différentes étapes de leur constitution"*, notamment le logiciel utilisé, les formats et les transformations successives.

## Pourquoi il fallait combiner les trois

Aucune des trois pièces ne couvre, à elle seule, le cycle de vie complet d'un corpus littéraire numérisé. Le document le résume ainsi : *"le CIDOC CRM fournit le cadre général de représentation des objets culturels et de leurs trajectoires, LRMoo prend en charge la spécificité des œuvres et des objets bibliographiques, tandis que CRMdig permet d'intégrer leur dimension numérique ainsi que les processus techniques associés"*. CAO_CRM articule les trois précisément pour pouvoir suivre un même texte — Madame Bovary, par exemple — depuis l'idée abstraite du roman, en passant par ses différentes éditions imprimées, jusqu'au PDF numérisé qu'un chercheur consulte aujourd'hui dans une bibliothèque numérique, sans perdre aucun de ces niveaux en chemin.
