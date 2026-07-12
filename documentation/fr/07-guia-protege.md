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
# Comment ouvrir et explorer le modèle CAO_CRM dans Protégé (guide pratique pas à pas)


## Qu'est-ce que Protégé

Protégé est le logiciel — gratuit, à code source ouvert, développé par l'université de Stanford — utilisé pour créer et examiner des **ontologies** : des schémas formels qui définissent quels « types de choses » existent dans un domaine (par exemple, « Œuvre », « Personne », « Objet numérique ») et comment ils se relient entre eux. Nul besoin de savoir programmer : il s'agit d'une interface visuelle conçue pour lire et modifier un modèle sans écrire de code.

L'équipe d'Ariane utilise la version 5.6.8, installée ici sous forme d'application Flatpak sous Linux, mais Protégé fonctionne de la même façon sous Windows et sous Mac : les menus décrits ci-dessous sont identiques. Ce guide ne porte que sur l'**exploration** du modèle déjà construit, et non sur son édition.

## Étape 1 : ouvrir le fichier du modèle

CAO_CRM est distribué sous la forme d'un fichier `.rdf` (RDF/XML, un format texte à la grammaire stricte, expliqué dans une autre section de cette documentation). Le fichier final du dépôt d'Ariane s'appelle `ontology/CAO_CRM-1.0.rdf`.

Pour l'ouvrir : dans la barre de menus, **File > Open...**, on navigue jusqu'au dossier contenant le fichier et on le sélectionne (on peut aussi le faire glisser dans la fenêtre du programme). Protégé mettra quelques secondes à le traiter — CAO_CRM intègre des classes et des propriétés issues de plusieurs standards internationaux (CIDOC-CRM, LRMoo, CRMdig, entre autres) — puis l'affichera une fois chargé.

## Étape 2 : « Active Ontology » — la fiche d'identité du modèle

Une fois le chargement terminé, Protégé affiche généralement en premier l'onglet **Active Ontology** (« ontologie active ») ; s'il n'apparaît pas, on le sélectionne dans la rangée d'onglets du haut. Il fonctionne comme une fiche d'identité du fichier : il indique son IRI (une adresse unique qui l'identifie sur le web, sans que celle-ci doive nécessairement pointer vers une page réelle), sa version, son auteur, la licence sous laquelle elle est publiée, ainsi que des commentaires généraux. C'est l'endroit indiqué pour se faire une première idée de « ce qu'est ce fichier » avant d'entrer dans le détail. C'est d'ailleurs la même information qu'une autre section de cette documentation examine comme preuve de qualité : si cette fiche est incomplète, ou mêlée à des données provenant d'une autre ontologie, c'est ici qu'on le détecte au premier coup d'œil.

## Étape 3 : « Entities » — là où résident les classes et les propriétés

L'onglet **Entities** (« entités ») est le cœur de l'exploration : c'est ici que l'on navigue à travers tout ce que CAO_CRM définit. Il comporte plusieurs sous-onglets :

- **Classes** (classes) : la liste des « types de choses » que reconnaît le modèle — par exemple, `F1_Work` (une œuvre à l'état abstrait) ou `F2_Expression` (une réalisation concrète, comme un texte dans une langue donnée) —, présentée sous la forme d'un arbre hiérarchique repliable, car certaines classes sont des sous-types d'autres.
- **Object properties** (propriétés d'objet) : des relations qui relient une instance d'une classe à une autre, comme celle qui unit une œuvre à la personne qui l'a créée.
- **Data properties** (propriétés de données) : des relations qui relient une instance d'une classe à une valeur simple — texte, date, nombre — et non à une autre entité ; par exemple, la propriété qui associe une œuvre au texte de son titre.
- **Annotation properties** (propriétés d'annotation) : elles documentent le modèle lui-même, sans décrire le domaine, comme `rdfs:label` (étiquette lisible d'un terme) ou `rdfs:comment` (sa description).

Il suffit de cliquer sur le nom d'une classe ou d'une propriété, dans le panneau de gauche, pour que le reste de l'écran affiche ses informations détaillées.

## Étape 4 : lire les informations d'une classe ou d'une propriété

Lorsqu'on sélectionne une classe ou une propriété, Protégé affiche plusieurs blocs qu'il convient de savoir reconnaître :

- **Le nom technique**, en haut, qui inclut généralement un code hérité des standards que CAO_CRM réutilise (par exemple, `F1_Work`, où « F1 » est l'identifiant utilisé par LRMoo, le standard bibliographique sur lequel s'appuie cette partie du modèle).
- **Étiquettes (`rdfs:label`) en différentes langues** : comme CAO_CRM hérite de standards internationaux élaborés par des communautés de plusieurs pays, il est normal de trouver une même classe ou propriété dotée d'étiquettes en anglais, en français, en allemand, en portugais, en russe ou en chinois, chacune marquée par son code de langue (`en`, `fr`, `de`...). Il ne s'agit ni d'une erreur ni d'une duplication, mais de la façon normale de lire le même terme dans différentes langues.
- **Le commentaire ou la définition** (`rdfs:comment`, parfois `skos:definition`) : le texte qui explique, en prose, ce que signifie la classe ou la propriété et comment elle doit être employée ; c'est généralement l'information la plus utile pour en comprendre le sens sans avoir à le deviner à partir du nom technique.
- **Les superclasses** (`SubClassOf`) : elles indiquent de quelle classe plus générale la classe sélectionnée est un cas particulier, c'est-à-dire de quoi elle hérite son sens et ses règles de base. Par exemple, `F32_Item_Production_Event` (l'événement de production d'un exemplaire physique) est déclarée sous-classe de `E12_Production`, une classe bien plus générale de CIDOC-CRM — c'est cette relation qui garantit que tout ce qui est légal pour une Production l'est aussi pour un événement de production d'exemplaire, sans qu'il soit besoin de le redéclarer terme par terme.

Pour les propriétés, le panneau équivalent affiche en outre le **domaine** (`domain`, quelle classe peut posséder cette propriété) et la **portée** (`range`, quelle valeur ou quelle classe elle peut recevoir), qui indiquent « qui se connecte à qui » dans cette relation.

## Le bouton du raisonneur (« Reasoner »)

Dans la barre de menus se trouve une option appelée **Reasoner**, avec des moteurs disponibles comme HermiT ou Pellet. En une phrase : le raisonneur vérifie automatiquement si les règles du modèle se contredisent entre elles et fait apparaître, au passage, des relations qui n'ont pas été écrites explicitement mais qui se déduisent logiquement des autres.

Il n'est pas nécessaire de l'activer pour explorer le modèle, mais si on le fait (**Reasoner > Start reasoner**, en comparant ensuite la vue « Asserted » — ce que le modèle dit littéralement — avec la vue « Inferred » — ce qui en est déduit —), c'est un moyen simple de vérifier que ce que l'on lit est, outre lisible, logiquement cohérent. Cette même vérification, appliquée de façon systématique, constitue l'une des preuves de qualité décrites dans la section consacrée à la validation du modèle.

## Une dernière recommandation

Il est conseillé de suivre cet ordre la première fois : d'abord la fiche générale (**Active Ontology**), ensuite l'arbre des classes, et seulement après les propriétés concrètes. Le champ de recherche de Protégé (icône en forme de loupe, ou `Ctrl+K`) permet de saisir « Work » ou « Titre » pour accéder directement au terme, sans devoir parcourir l'arbre entier à la main.
