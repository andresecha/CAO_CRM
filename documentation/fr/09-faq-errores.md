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
# Foire aux questions et erreurs réelles rencontrées lors de la construction du modèle (et ce qu'elles enseignent)


Construire un modèle ontologique (un fichier formel qui décrit des classes, des propriétés et des règles — ici, CAO_CRM, le Corpus Author Ontology CRM du consortium Ariane) en réutilisant des éléments de standards existants (CIDOC-CRM, LRMoo, CRMdig) ne consiste pas simplement à « copier-coller » : chaque élément apporte avec lui des conventions et des lacunes qui peuvent s'y glisser par erreur. Cette section rassemble, sous forme de questions et réponses, des incidents réels documentés lors de la validation de CAO_CRM, avec leur cause, leur solution et la leçon qu'ils en tirent — sans volonté de désigner des responsables, mais à titre d'exemple pédagogique pour quiconque compose des ontologies tierces. Les trois cas décrits ci-dessous sont **entièrement résolus** dans la version actuelle du modèle (`CAO_CRM-1.0.rdf`) ; ils sont conservés ici précisément parce que ce sont eux qui ont convaincu l'équipe de ne plus jamais se fier à un résumé automatique sans en vérifier le détail — une discipline qui a ensuite donné lieu, bien plus tard dans le projet, à une chaîne de trois audits indépendants et successifs avant toute publication (voir la dernière section de ce document).

## Pourquoi la documentation générée est-elle apparue sous le titre « SKOS Vocabulary » au lieu de CAO_CRM ?

Lors de la génération du site de documentation avec Widoco (un programme qui lit l'ontologie et produit automatiquement un site web navigable présentant ses classes et ses propriétés), la page affichait comme titre « SKOS Vocabulary » — le nom d'un autre standard, sans rapport avec CAO_CRM : SKOS (*Simple Knowledge Organization System*, un modèle pour les vocabulaires contrôlés et les thésaurus).

En examinant `CAO_CRM-2.0.rdf`, on a confirmé que le nœud décrivant l'ontologie elle-même (sa « fiche d'identité ») mêlait, outre ses propres données, des métadonnées copiées littéralement à partir de six autres ontologies (SKOS, CIDOC-CRM, CRMdig, LRMoo, CRMsci, CRMinf) : le titre portait la valeur `"SKOS Vocabulary"@en`, la paternité de l'ontologie était attribuée aux auteurs réels de SKOS, et l'on trouvait un bloc de près de 200 lignes qui s'est révélé être, mot pour mot, les notes de publication propres à CIDOC-CRM.

**Comment cela a-t-il été découvert :** non pas par une relecture manuelle, mais parce que Widoco a fait apparaître un symptôme impossible à ignorer (un titre erroné), ce qui a conduit à examiner le fichier source. La cause probable est un effet secondaire de la manière dont l'éditeur Protégé « aplatit » les importations lors de l'exportation : en regroupant plusieurs fichiers importés en un seul, leurs métadonnées propres peuvent se mélanger au sein d'un même nœud.

**Comment y remédier :** en supprimant du nœud de l'ontologie les valeurs étrangères et en y déclarant les valeurs propres. Le dépôt inclut des requêtes de « régression », conçues pour échouer de nouveau si le problème réapparaît.

**Leçon générale :** tout outil qui lit le titre pour identifier « de quelle ontologie s'agit-il » — documentation, catalogues, indexeurs de données ouvertes — fait aveuglément confiance à cette valeur. Il convient donc de toujours vérifier l'en-tête de l'ontologie après toute importation ou tout « aplatissement » de fichiers.

## Pourquoi le modèle, qui réussissait auparavant le test de cohérence logique, a-t-il commencé à échouer en tant qu'« incohérent » ?

Entre deux vérifications, le fichier a considérablement grossi (passant de 970 à plus de 7 000 triplets — chaque triplet étant une affirmation de base « sujet-prédicat-objet »), à la suite d'une réexportation plus complète depuis Protégé. Avec ce nouveau contenu, le raisonneur (*reasoner*, le programme qui applique les règles logiques du modèle pour vérifier qu'il ne se contredit pas) a signalé que l'ontologie était incohérente : elle devenait logiquement vide, car une contradiction interne permet de « déduire » n'importe quoi à partir de n'importe quoi.

**Comment cela a-t-il été découvert :** grâce à `robot explain`, un utilitaire qui identifie l'ensemble minimal d'affirmations responsables. Il a trouvé quatre axiomes : `cao:Title` équivalent à la propriété de titre de Dublin Core ; le nœud de l'ontologie portant la valeur contaminée `"SKOS Vocabulary"@en` sur cette même propriété ; `cao:Place` équivalent à `cao:Title` ; et `cao:Place` ayant pour portée `xsd:anyURI` (n'admettant que des identifiants URI). Par transitivité, le texte contaminé finissait par être « hérité » par `cao:Place`, qui exige des URI et non du texte — une contradiction irrésoluble qui fait s'effondrer tout le modèle.

**Comment y remédier :** il s'agit en réalité de la combinaison de deux problèmes déjà connus séparément : la métadonnée contaminée du cas précédent, et un avertissement de qualité (le piège « P27 — Defining wrong equivalent properties », détecté par l'outil OOPS!) qui, jusqu'alors, semblait n'être qu'une recommandation « importante », non urgente. Avec la croissance du fichier, cette recommandation s'est transformée en une contradiction logique dure. La corriger exige de revoir si `cao:Place` doit continuer à être équivalent à `cao:Title`, en plus de nettoyer la métadonnée contaminée.

**Leçon générale :** un avertissement de qualité « mineur » aujourd'hui peut devenir demain une erreur logique bloquante, simplement parce que le modèle a changé de taille. Deux constats indépendants peuvent se combiner en un troisième, plus grave que chacun d'eux pris séparément — c'est pourquoi il convient de traiter les avertissements « importants » avec le même sérieux que les avertissements « critiques ».

## Pourquoi manquait-il des axiomes de CIDOC-CRM relatifs à « a une note » (`P3_has_note`) lors de la comparaison du modèle combiné avec le fichier officiel ?

Lors de la comparaison du modèle combiné avec le fichier officiel de CIDOC-CRM 7.1.3 au moyen de `robot diff` (qui signale les affirmations de l'original absentes, sans modification, du résultat), 8 axiomes officiels manquants sont apparus, liés à `P3_has_note` (« a une note », une propriété permettant d'attacher des descriptions informelles à n'importe quelle entité) et à ses sous-propriétés.

**Comment cela a-t-il été découvert :** en comparant la manière dont `P3_has_note` était déclarée dans CAO_CRM par rapport au fichier officiel. Dans CAO_CRM, il s'agissait d'une `owl:ObjectProperty` (qui relie à une autre entité dotée d'une identité propre). La version officielle de CIDOC-CRM la déclare de manière générique, comme `rdf:Property`, sans préciser s'il s'agit d'une propriété d'objet ou d'une propriété de données : la documentation de référence décrit conceptuellement « Domain: E1 CRM Entity / Range: E62 String », mais le fichier RDF exécutable ne l'a jamais formalisé ainsi — une véritable lacune du standard lui-même, et non une erreur de CAO_CRM. En combinant les deux déclarations pour la même URI, il se produit un *punning* (utiliser le même nom pour deux natures distinctes), et les outils de fusion écartent silencieusement les axiomes qui n'avaient de sens que sous la lecture « de données ».

**Comment y remédier :** l'équipe a documenté sa décision dans `decisions/fr/problemes-et-solutions.md` (Problème 1), le catalogue général des problèmes et solutions du projet. Il a été choisi de déclarer `P3_has_note` comme `owl:DatatypeProperty` avec pour portée `rdfs:Literal` (la catégorie la plus large de valeurs simples), en reproduisant le schéma que le fichier officiel lui-même applique à une propriété sœur présentant la même lacune, `P90_has_value` : `<rdfs:range rdf:resource="http://www.w3.org/2000/01/rdf-schema#Literal" />`. L'option `xsd:string` a été écartée : elle aurait constitué une restriction inventée sans fondement officiel, contraire à la pratique de CIDOC-CRM lui-même, qui évite de s'engager sur des types XSD même lorsque le type « paraît évident » (`P90_has_value` représente un nombre et utilise pourtant `rdfs:Literal`).

**Leçon générale :** lorsqu'un standard présente une lacune dans sa mise en œuvre technique, le moyen le plus sûr de la combler n'est pas d'inventer une solution « plus précise » de son cru, mais de reproduire la manière dont ce même standard résout des cas équivalents. Dans un projet défini comme une composition bornée de fragments tiers, tout typage absent de l'original constitue, en pratique, une redéfinition conceptuelle du modèle de base.

## Comment ces cas sont-ils liés entre eux ?

Il ne s'agit pas d'incidents isolés : « SKOS Vocabulary » a été l'une des quatre causes de l'incohérence logique du deuxième cas, et `P3_has_note` a été détecté par deux tests distincts, ce qui confirme qu'il s'agissait d'un problème réel et non d'un faux positif. Dans un modèle composé de plusieurs ontologies, les problèmes restent rarement confinés au module où ils trouvent leur origine : ils se propagent à d'autres couches de vérification, et ne deviennent parfois visibles que lorsque le fichier grossit ou qu'un type de test différent de celui qui les a détectés en premier est exécuté.

## Pourquoi ces problèmes n'ont-ils pas été corrigés « à la volée », avec la première solution raisonnable disponible ?

Parce qu'une solution rapide, même si elle fonctionne techniquement, peut introduire une décision de modélisation que personne n'a autorisée ni documentée : choisir `xsd:string` pour `P3_has_note` aurait « réglé » le problème, mais sans fondement officiel. Lorsqu'un constat exige une décision de conception, la procédure consiste à la documenter dans un ADR, avec les alternatives évaluées et les citations officielles qui étayent le choix retenu, plutôt qu'à la résoudre en silence. Les constats de nature mécanique, comme le nettoyage de métadonnées contaminées, restent en attente d'une correction directe, sans qu'un ADR soit nécessaire.

## Quelle leçon générale cela laisse-t-il à quiconque construit un modèle similaire ?

1. **Un résumé automatique (« 0 erreur ») ne remplace jamais l'inspection du rapport complet.** « SKOS Vocabulary » n'a pas été détecté par un test conçu à cet effet, mais par un symptôme visuel repéré dans un outil poursuivant un tout autre objectif.
2. **Les lacunes de la documentation officielle d'un standard réutilisé ne se « devinent » pas au moyen d'une décision propre**, mais se comblent en reproduisant la manière dont ce même standard résout des cas équivalents, en laissant une trace écrite du choix effectué.
3. **Un modèle composé de plusieurs ontologies doit voir ses « points de jonction » révisés avec régularité.** Ce qui était hier une recommandation mineure peut devenir, demain, une erreur réelle, simplement parce que le contexte a changé.

## Ce que ces leçons ont donné, bien plus tard dans le projet

Ces trois incidents ont laissé une trace durable dans la méthode de travail : plus aucune affirmation n'est acceptée sans vérification directe contre le fichier source, jamais contre un résumé ou un souvenir. Cette discipline a atteint sa forme la plus aboutie juste avant la publication de la version actuelle, sous la forme d'une **chaîne de trois audits indépendants et successifs** : un premier audit qui revérifie chaque terme du RDF un par un contre les fichiers officiels vendorisés ; un second qui revérifie la documentation de décision elle-même et la conformité conceptuelle de chaque choix ; et un troisième qui revérifie de façon croisée un échantillon des affirmations les plus fortes des deux précédents, sans se faire confiance non plus. Aucun des trois audits n'a trouvé d'erreur dans les affirmations vérifiées par le précédent — un résultat qui, précisément à cause des incidents racontés ci-dessus, n'a jamais été considéré comme acquis d'avance. Le détail complet se trouve dans `decisions/fr/auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md` et `auditoria-3-verificacion-final.md`.
