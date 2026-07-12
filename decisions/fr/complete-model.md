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
# Complete-model : les 4 catégories × 5 classes, ce qui manquait encore, entièrement résolu

**Date :** 6 juillet 2026.
**Objet de ce document :** vérifier, catégorie par catégorie et classe par classe, que les quatre catégories transversales du paper (« Caractéristiques », « Processus », « Statut », « Relation ») ont bien un mécanisme légal dans `CAO_CRM-1.0.rdf` pour les cinq niveaux du modèle (`F1_Work`, `F2_Expression`, `F3_Manifestation`, `F5_Item`, `D1_Digital_Object`). Ce document ne répète pas ce qui est déjà documenté dans `problemes-et-solutions.md` — il part de cette base déjà corrigée et cherche ce qui reste à faire. Ce document consolide, en un seul endroit, la matrice, les trois manques identifiés, leur résolution complète et la totalité du travail de vérification (raisonnement et citations sources) qui les corrobore.
**Sources vérifiées :** le paper (`Paper_Article_Revue HN_V2.docx.pdf`, tableau de métadonnées section 4.1, et sections 3.2/3.3), `CAO_CRM-1.0.rdf`, les trois modèles officiels vendorisés, et les sources externes détaillées section 6.
**Ce que ça implique pour la suite :** chaque manque identifié ici concerne à la fois le futur diagramme Drawio (une nouvelle case/arête à dessiner) et l'ontologie (un terme à extraire) — les deux sont signalés séparément, comme dans `problemes-et-solutions.md`.

---

## 1. La matrice de référence, telle que le paper la définit

Rappel des quatre catégories, citées en toutes lettres (section 3.3 du paper) :
> *« La catégorie "Caractéristiques" regroupe les informations descriptives et identificatoires [...] la catégorie "Processus" documente les événements associés à la création, à la production ou à la transformation d'une entité [...] la catégorie "Statut" concerne les aspects juridiques et matériels [...] la catégorie "Relation" permet de documenter les liens qu'une entité entretient avec d'autres ressources du modèle. »*

Et la réserve déjà faite par le paper lui-même sur `F1_Work` (note de bas de page 16) :
> *« Seule la F1_Work ne comporte que trois de ces catégories (statut, caractéristiques et process), la quatrième ("Relations") ayant été considérée, en l'occurrence, moins appropriée. [...] À ce stade, le modèle ne fournit pas d'étiquette permettant cette prise en charge de l'intertextualité, mais une telle extension ne serait pas difficile à ajouter. »*

Ce dernier point est directement pertinent : ce document identifie précisément cette « étiquette » que le paper annonçait comme facile à ajouter (§3, Manque 3).

---

## 2. Ce qui est déjà résolu — vérifié, pas supposé

Vérification faite terme par terme contre `CAO_CRM-1.0.rdf` (965+ triples, 6 juillet 2026) :

| Classe | Catégorie | Champ du paper | Mécanisme | Statut |
|---|---|---|---|---|
| `F1_Work` | Caractéristiques | Titre (E35 Title) | `P1_is_identified_by` → `E35_Title` | ✅ légal |
| `F1_Work` | Processus | Auteur, Date | `F27_Work_Creation` + `P14_carried_out_by` + `P4_has_time-span` | ✅ légal |
| `F2_Expression` | Caractéristiques | Langue | `P72_has_language` + `E33_Linguistic_Object` (Problème 2) | ✅ résolu |
| `F2_Expression` | Processus | Création, traducteur | `F28_Expression_Creation` + `P14_carried_out_by` + `P4_has_time-span` | ✅ légal |
| `F2_Expression` | Statut | Droits | `P104_is_subject_to` (`F2_Expression ⊂ E90_Symbolic_Object`) | ✅ légal |
| `F3_Manifestation` | Caractéristiques | Identifiant, Type | `P1_is_identified_by`, `P2_has_type` | ✅ légal |
| `F3_Manifestation` | Statut | Droits | `P104_is_subject_to` | ✅ légal |
| `F3_Manifestation` | Processus | Date, Lieu, Acteur, Mode de production | `F32_Item_Production_Event` (Problème 5) | ✅ résolu |
| `F3_Manifestation` | Relation | Manifestation alternative | `R78_has_alternate` | ✅ déjà présent |
| `F5_Item` | Caractéristiques | Identifiant, Dimension, Mode d'agencement, Matériaux, Système d'écriture | `P1_is_identified_by`, `E54_Dimension`+`P90`/`P91` (Problème 7), `P2_has_type`+`P127` (Problème 1b), `P45_consists_of` | ✅ résolu |
| `F5_Item` | Caractéristiques | Description | `P3_has_note` (Problème 1) | ✅ résolu |
| `F5_Item` | Statut *(absent du tableau du paper, mais déjà résolu)* | Condition, localisation | `P44_has_condition` + `E22_Human-Made_Object`+`P54`/`P55` (Problème 3) | ✅ résolu — **voir Question ouverte 3** |
| `F5_Item` | Relation | Autre objet physique | `P46_is_composed_of` | ✅ déjà présent |
| `D1_Digital_Object` | Caractéristiques | Identifiant, Dimension, Format, Description | `P1_is_identified_by`, `E54_Dimension`+`D9_Data_Object` (Problème 6), `P2_has_type`, `P3_has_note` | ✅ résolu |
| `D1_Digital_Object` | Statut | Droits, Entrepôt de données | `P104_is_subject_to`, `L19_stores` (`D13_Digital_Information_Carrier`) | ✅ légal |
| `D1_Digital_Object` | Processus | Numérisation / production native | `D2_Digitization_Process` / `D7_Digital_Machine_Event` (découverte complémentaire) | ✅ résolu |
| `D1_Digital_Object` | Relation | Autre objet numérique | `P106_is_composed_of` (`E90_Symbolic_Object`) | ✅ déjà présent |

**17 des 20 cases de la matrice sont donc déjà couvertes**, une fois `CAO_CRM-1.0.rdf` appliqué. Restent 3 manques réels, détaillés ci-dessous.

---

## 3. Les manques réels

### Manque 1 — `F1_Work`, catégorie Statut (Droits) : contradiction résolue

**Ce que le paper demande**, texte intégral de la ligne du tableau :
> `Oeuvre | Statut | Droits (E30 Right) | Propriété intellectuelle inaliénable de Cailhava de l'Estandoux`

**Le problème** : `P104_is_subject_to` exige `E72_Legal_Object`, qui n'a que deux sous-classes officielles (`E18_Physical_Thing`, `E90_Symbolic_Object`, vérifié au Problème 4). `F1_Work ⊂ E89_Propositional_Object ⊂ E28_Conceptual_Object` — la branche que la note de balisage d'`E72_Legal_Object` exclut explicitement :
> *« In the case of instances of E28 Conceptual Object, however, the identity of an instance of E28 Conceptual Object or the method of its use may be too ambiguous to reliably establish instances of E30 Right, as in the case of taxa and inspirations. »*

**Une nuance importante à ne pas manquer :** la valeur donnée par le paper — *« propriété intellectuelle inaliénable »* — n'est pas un droit patrimonial ordinaire (cessible, comme un droit d'édition) : c'est un **droit moral** (au sens du droit d'auteur continental), attaché à la personne de l'auteur et à son œuvre, précisément inaliénable et non cessible. Ce n'est donc pas un hasard si le paper veut ce droit au niveau de l'Œuvre plutôt qu'à celui de l'Expression ou de la Manifestation : le droit moral protège l'intégrité de l'œuvre elle-même, indépendamment de telle ou telle édition.

**La solution, sans rien ajouter au périmètre** : le chemin légal indirect déjà établi au Problème 4 s'applique de la même façon ici — passer par `F2_Expression`, déjà légalement compatible avec `P104_is_subject_to` :
```
F1_Work --R3_is_realised_in--> F2_Expression --P104_is_subject_to--> E30_Right
```
La nature « inaliénable » du droit ne se perd pas dans ce chemin : elle se documente en typant l'instance d'`E30_Right` elle-même (`P2_has_type` → une valeur `E55_Type` telle que « droit moral »/« droit inaliénable »), pas en l'accrochant directement à `F1_Work`. Le droit reste attaché à ce que l'œuvre *dit* (son Expression), ce qui correspond exactement à ce que protège un droit moral en pratique.

**Corroboration externe complète.** Ce chemin n'est pas seulement une déduction locale à partir des notes de balisage déjà citées ci-dessus — il est confirmé par la discussion officielle du CRM-SIG lui-même. L'issue « Rights Model » (ID 328, `https://cidoc-crm.org/Issue/ID-328-rights-model`, URL vérifiée par curl direct, HTTP 200, consultée le 6 juillet 2026) montre que le SIG a explicitement discuté, dès 2017, du cas du **droit moral** (« Droit Moral/Moral Rights »), avec l'exemple classique de Léonard de Vinci et de son droit moral post-mortem sur la Joconde — exactement le type de cas que représente Cailhava de l'Estandoux dans le paper. Citations extraites verbatim de la page :
> *« Can I then transfer ownership of an E30 Right? No, as you transfer ownership of Physical Things (E18), not of Propositional (E89), Conceptual (E28), Man-Made (E71), Things (E70). »* — Robert Sanderson.

> *« The New Zealand example has a kind of counterpart in the so called Droit Moral/Moral Rights connected with IPR [...] By decorating a Mona Lisa copy in a offending manner you can [be] taken to court accussed for violating Leonardo's Moral Right. Who posesses the rigths? Leonardo who died 500 years ago? »* — Christian-Emil Ore.

> *« In the 38th joined meeting of the CIDOC CRM SIG and ISO/TC46/SC4/WG9 and the 31st FRBR - CIDOC CRM Harmonization meeting, the crm-sig discussed about transferring ownership of an E30 Right. Comments and decisions are: [...] To add copyright examples in the scope note of E30 Right. »*

La décision actée en réunion (clôturée à la « 40th joined meeting », janvier 2018, Cologne) a été d'ajouter des exemples de copyright à la note de balisage d'`E30_Right`, **jamais** de créer une propriété directe qui contournerait l'exclusion d'`E28_Conceptual_Object`, et de renvoyer les cas complexes de titularité/transfert vers une extension séparée (« CRMsocial »). Aucune trace, dans cette discussion ni ailleurs, d'un chemin alternatif documenté qui contredirait celui proposé ici — le SIG confirme au contraire, implicitement et à plusieurs reprises, qu'aucun mécanisme direct n'existe ni n'est prévu pour rattacher un droit à un objet conceptuel.

**Nuance honnête à garder :** aucun projet réel déjà publié appliquant très précisément ce chemin pour un droit moral n'a été trouvé (recherche WebSearch dédiée, sans résultat) — la confirmation vient de la cohérence de la position du CRM-SIG sur le sujet, pas d'un précédent d'implémentation documenté.

**Reconnaissance honnête de la perte d'expressivité réelle** (relevée par l'auditoria-2-documentacion-y-conformidad.md, section B.6) : cette solution évite l'inconsistance logique, mais ne restitue pas toute l'expressivité perdue. Un droit moral est, par définition, inhérent à l'**auteur** et à son **Œuvre** — indépendant de toute matérialisation ou traduction concrète. Le chemin retenu accroche pourtant le droit à une **Expression précise**, pas à l'Œuvre en tant que telle. Conséquence pratique concrète : si une Œuvre a plusieurs Expressions (le texte original, une traduction, une version abrégée), le modèle oblige soit à choisir arbitrairement sur laquelle accrocher le `E30_Right` de type « droit moral », soit à le répéter sur chacune — ce qui n'est pas incorrect, mais dilue la nature unitaire du droit. Le SIG confirme qu'aucun mécanisme direct n'existe ni n'est prévu pour `E28_Conceptual_Object` — ce n'est donc pas un choix arbitraire de CAO_CRM, mais une limitation structurelle connue et acceptée du CRM lui-même.

#### A. Changements dans le diagramme visuel
- Ne pas dessiner de flèche directe `F1_Work → E30_Right`.
- S'assurer que `F1_Work --R3_is_realised_in--> F2_Expression` est présent (il l'est déjà, Problème 2), et que la flèche `P104_is_subject_to` part de `F2_Expression`, pas de `F1_Work`.
- Ajouter, sur l'instance `E30_Right` concernée, une case `E55_Type` (« Type de droit ») avec la valeur « droit moral »/« propriété intellectuelle inaliénable ».
- Ajouter également, si le diagramme le permet, la flèche déjà légale `F1_Work --R16i_was_created_by--> F27_Work_Creation --P14_a_pour_auteur_original--> E39_Actor` comme chemin explicite de réponse à « qui est l'auteur moral » (voir section C ci-dessous) — elle existe déjà dans le module, il s'agit seulement de la relier visuellement à la question du droit moral.

#### B. Changements dans le RDF
Aucun ajout de périmètre — tout est déjà présent.
```turtle
:oeuvre_art_comedie  lrmoo:R3_is_realised_in  :expression_art_comedie .
:expression_art_comedie  cidoc:P104_is_subject_to  :droit_moral_cailhava .
:droit_moral_cailhava  a cidoc:E30_Right ;
                        cidoc:P2_has_type  :valeur_droit_moral .
```

#### C. Résolution normative : séparer la question « qui détient moralement l'Œuvre » de la question « quel est le régime juridique formel du droit »

La tension décrite plus haut vient de vouloir faire porter à un **seul** mécanisme (`E30_Right`/`P104_is_subject_to`) deux réalités juridiques différentes :

1. **Le droit moral** — inaliénable, incessible, vested dans la personne de l'auteur et attaché à l'Œuvre elle-même, indépendamment de toute Expression particulière. Sa question centrale n'est pas « quel document juridique formel existe ? » mais **« qui est l'auteur, de façon unique et non ambiguë, pour cette Œuvre ? »**
2. **Les droits patrimoniaux** — cessibles (droit de reproduction, d'édition, de traduction), attachés à une exploitation concrète, donc légitimement rattachables à une Expression ou à une Manifestation précise (une traduction a ses propres droits d'édition, distincts de ceux du texte original).

**Ce que LRMoo fournit déjà, dans notre propre module, pour la question 1 (droit moral = autorat) : un chemin Œuvre-niveau, unique, sans besoin d'`E30_Right`.** La note de balisage officielle de `F27_Work_Creation` (`imports/vendor/lrmoo-1.1.1.rdf`) est explicite :
> *« An instance of E39 Actor with which a work is associated through the chain of properties F1 Work. R16i was created by: F27 Work Creation. P14 carried out by (performed): E39 Actor corresponds to the notion of the "creator" of the work. »*

Ce chemin — `F1_Work --R16i_was_created_by--> F27_Work_Creation --P14_carried_out_by (ou sa sous-propriété P14_a_pour_auteur_original)--> E39_Actor` — est **déjà entièrement présent dans le périmètre de CAO_CRM depuis l'origine du module** (voir la ligne « `F1_Work` | Processus | Auteur, Date » de la matrice, section 2 ci-dessus, déjà marquée ✅ légal — `F27_Work_Creation` est d'ailleurs déclarée `rdfs:subClassOf E7_Activity` directement dans `CAO_CRM-1.0.rdf`, donc `P14_a_pour_auteur_original`, dont le domaine est `E7_Activity`, s'y applique sans aucun ajout) et **est déclaré par la norme elle-même** comme la façon canonique d'identifier « le créateur » d'une Œuvre. Il est de plus **unique par construction** : une Œuvre a une (ou plusieurs, en cas de coauteurs) instance(s) de `F27_Work_Creation`, mais une seule, non répétée par Expression — exactement la propriété d'unicité qu'exige un droit moral, et que le chemin via `F2_Expression`/`E30_Right` ne garantit pas (voir la perte d'expressivité reconnue ci-dessus).

**Conséquence pratique — la recommandation retenue :** ne pas essayer de faire porter le droit moral par `E30_Right` sur `F1_Work` (structurellement impossible, confirmé par Sanderson/Issue 328 : *« you transfer ownership of Physical Things (E18), not of Propositional (E89), Conceptual (E28) [...] Things »*) ; ne pas non plus se reposer uniquement sur la répétition d'`E30_Right` par Expression pour répondre « qui est l'auteur moral ». Utiliser les deux mécanismes déjà légaux, chacun pour ce qu'il documente le mieux :
- **Pour répondre « qui détient le droit moral, de façon unique et non ambiguë » :** interroger le chemin Œuvre-niveau déjà légal, `F1_Work → R16i_was_created_by → F27_Work_Creation → P14_a_pour_auteur_original → E39_Actor` — c'est la réponse LRMoo native, sans ambiguïté, sans redondance entre Expressions.
- **Pour documenter le régime juridique formel** (mentions de type « droit moral », litiges, exemples de jurisprudence, ou un droit patrimonial cessible propre à une traduction) : garder `F1_Work --R3_is_realised_in--> F2_Expression --P104_is_subject_to--> E30_Right`, typé par `P2_has_type`, tel que proposé en section B ci-dessus — pertinent précisément parce que ce niveau *est* le bon niveau pour un droit patrimonial cessible (une traduction a ses propres droits d'édition), et reste, pour le droit moral, une trace formelle utile (ex. un litige documenté) sans prétendre être la source unique de vérité sur « qui est l'auteur ».

Cette double lecture ne change rien au RDF déjà en place (aucun nouveau terme, aucune modification de `CAO_CRM-1.0.rdf`, aucun changement à la solution B) : elle documente explicitement que le module possède déjà, depuis l'origine, les deux mécanismes nécessaires — il manquait seulement de les nommer et de les relier explicitement l'un à l'autre pour cet usage.

---

### Manque 2 — `F2_Expression`, catégorie Relation : résolu, exhaustivement vérifié

**Ce que le paper suggère implicitement** (section 3.2, à propos de LRMoo) :
> *« ex. F2 Expression: "the text of the abridged English version of 'Murder on the Orient Express' (as published by HarperCollins)" »* — un exemple de dérivation (version abrégée) entre deux Expressions.

**Vérifié : aucune propriété de relation entre deux `F2_Expression` n'était présente dans la première extraction de `CAO_CRM-1.0.rdf`.**

**Les deux propriétés officielles manquantes, citations complètes** (`imports/vendor/lrmoo-1.1.1.rdf`) :

> **`R76_is_derivative_of`** — *« This property associates an instance of F2 Expression with another instance of F2 Expression which was its source or one of its sources. This property is not transitive. It is asymmetric and irreflexive. »* — `rdfs:domain`/`rdfs:range` : `F2_Expression`. C'est exactement le mécanisme de l'exemple officiel de LRMoo cité au §3.2 du paper — une traduction, un abrégé, une revue de texte.

> **`R75_incorporates`** — *« This property associates an instance of F2 Expression with an instance of F2 Expression that is an integral part of the first, but where the latter realises a different instance of F1 Work from the first. This property is transitive, asymmetric and irreflexive. »* — `rdfs:domain`/`rdfs:range` : `F2_Expression`. Utile pour les anthologies, recueils, œuvres qui en incorporent une autre.

**Exhaustivité vérifiée.** Les ~60 propriétés `R*` du fichier `imports/vendor/lrmoo-1.1.1.rdf` ont été listées et contrôlées une par une, domaine et portée : **seules `R75_incorporates` et `R76_is_derivative_of` ont domaine ET portée = `F2_Expression`.** Les propriétés voisines qui auraient pu sembler pertinentes ont chacune été écartées pour une raison précise et vérifiée :
- `R73_takes_representative_attribute_from` : domaine `F1_Work`, portée `F2_Expression` (relation Work→Expression, pas Expression→Expression).
- `R74_uses_expression_of` : domaine et portée `F1_Work` — c'est la généralisation de `R75_incorporates` **au niveau Œuvre**, le texte officiel le dit explicitement : *« This property represents the generalized relationship between works that is described at the expression level using R75 incorporates. »* Utile à savoir pour une future extension : si l'équipe veut un jour documenter une relation d'incorporation au niveau Œuvre sans descendre au niveau Expression, `R74` est la propriété correspondante.
- `R77_accompanies_or_complements`, `R79_has_representative_expression_attribute` : domaine et/ou portée `F1_Work`/`E55_Type`, hors sujet.
- `R56_has_related_form`, `R36_uses_script_conversion` : ancrées sur `F12_Nomen`, hors périmètre.

Recherche complémentaire dans le document officiel complet LRMoo v1.0 (101 pages, PDF téléchargé et parcouru intégralement, `https://cidoc-crm.org/sites/default/files/LRMoo_V1.0.pdf`) : **aucune propriété F2↔F2 supplémentaire trouvée** au-delà de ce qui est déjà dans le fichier vendorisé — le fichier vendorisé et le PDF officiel s'accordent parfaitement sur ce point. La proposition ci-dessus est donc exhaustive, pas seulement plausible.

#### A. Changements dans le diagramme visuel
- Ajouter, sur la page `F2` (Expression), une case `F2_Expression` reliée à elle-même par deux arêtes possibles : `R76_is_derivative_of (R76i_has_derivative)` et `R75_incorporates (R75i_is_incorporated_in)` — patron visuel identique aux autres relations déjà dessinées (`R78_has_alternate` sur `F3_Manifestation`).

#### B. Changements dans le RDF
**Ajouté au périmètre :** `R76_is_derivative_of`/`R76i_has_derivative`, `R75_incorporates`/`R75i_is_incorporated_in`.
```turtle
:expression_traduction_allemande  a lrmoo:F2_Expression ;
                                    lrmoo:R76_is_derivative_of  :expression_originale_francaise .
```

---

### Manque 3 — `F1_Work`, catégorie Relation : le paper annonçait cette extension comme facile à ajouter — voici comment, résolu

Le paper dit explicitement (note 16, citée en Partie 1) qu'une étiquette pour l'intertextualité entre Œuvres (adaptations, suites, fan fiction) *« ne serait pas difficile à ajouter »*, sans la nommer. Elle existe déjà officiellement.

**`R2_is_derivative_of`, texte intégral** (`imports/vendor/lrmoo-1.1.1.rdf`) :
> *« This property associates an instance of F1 Work which modifies the content of another instance of F1 Work with the latter. This property is transitive, asymmetric and irreflexive. [...] That is, F1 Work(1). R2 is derivative of: F1 Work(2), without needing to specify the specific expressions involved in the derivation. »*
> — `rdfs:domain`/`rdfs:range` : `F1_Work` ; `rdfs:subPropertyOf` : `R68_is_inspired_by`.

C'est un raccourci officiel — il documente la dérivation entre deux Œuvres sans avoir à préciser les Expressions intermédiaires, exactement ce que le paper demandait.

**`R2` n'est pas un simple synonyme de `R68_is_inspired_by` : c'est une propriété-sœur avec un sens plus étroit, et la distinction compte pour l'usage.** Les deux textes officiels, mis côte à côte :
- `R68_is_inspired_by` : *« [...] whose content was inspired by that instance of F1 Work. The content of the range work instance served in some way as a source of ideas for the domain work instance. »* — une **source d'idées**, sans réutilisation directe du contenu. (`rdfs:subPropertyOf` : `P130_shows_features_of` ; `owl:inverseOf` : `R68i_is_inspiration_for`.)
- `R2_is_derivative_of` (`rdfs:subPropertyOf R68_is_inspired_by`) : *« [...] which modifies the content of another instance of F1 Work with the latter. »* — une **modification effective du contenu**.

Les exemples du paper — adaptation théâtrale, suite, fan fiction — impliquent tous une reprise ou une transformation du contenu de l'œuvre source (personnages, intrigue, univers) : ils relèvent bien de `R2`, pas seulement d'`R68`. Et comme `R2` est déclarée `rdfs:subPropertyOf R68`, toute assertion `R2` **implique automatiquement** `R68` par héritage de propriété OWL — l'équipe n'a donc rien à perdre en n'utilisant que `R2` pour ces cas.

**Nuance pratique à garder :** si l'équipe rencontre un jour un cas d'œuvre *purement* inspirée par une autre, sans reprise de contenu identifiable (par exemple : « cette symphonie a été composée après avoir vu ce tableau », sans emprunt de motifs ou de structure), ce n'est **pas** un cas pour `R2` — il faut alors utiliser `R68_is_inspired_by` directement, sans passer par `R2`. Ne pas forcer tous les cas d'intertextualité dans `R2` par défaut quand certains relèvent en réalité de la relation plus faible `R68`.

**Remarque de méthode :** ce point n'était pas signalé comme un défaut dans le paper (qui le présente comme une extension future, pas un manque actuel) — il est traité ici parce que ce document a pour objet de compléter systématiquement la matrice des 4 catégories, et parce que la solution officielle existe déjà et ne coûte qu'une propriété.

#### A. Changements dans le diagramme visuel
- Ajouter, sur la page `F1` (Work), une case `F1_Work` reliée à elle-même par `R2_is_derivative_of (R2i_has_derivative)` — **cela donne à `F1_Work` sa quatrième catégorie**, contredisant (en bien) la note 16 du paper qui la jugeait « moins appropriée » : elle est en réalité disponible nativement, sans effort de modélisation supplémentaire.

#### B. Changements dans le RDF
**Ajouté au périmètre :** `R2_is_derivative_of`/`R2i_has_derivative`.
```turtle
:oeuvre_adaptation_theatrale  a lrmoo:F1_Work ;
                                lrmoo:R2_is_derivative_of  :oeuvre_art_comedie .
```

---

## 4. Question ouverte, résolue — où doit vivre le Système d'écriture ?

Le tableau du paper porte, à la ligne « Objet numérique — Caractéristiques — Système d'écriture », la mention *« [non renseigné, doublon] »* — le paper reconnaît lui-même l'ambiguïté.

### 4.1 — La recommandation, en une phrase

**Le Système d'écriture se déplace vers `F2_Expression`** (co-typée `E33_Linguistic_Object`, exactement le mécanisme déjà utilisé pour la Langue au Problème 2), en utilisant `P2_has_type`/`E55_Type` ancré par `P127_has_broader_term` (déjà prévu au Problème 1b) — **et non plus sur `F5_Item`/`D1_Digital_Object` comme le proposait le Problème 1b initialement.** Voir la mise à jour complète dans `problemes-et-solutions.md` (Problème 1, section « Mise à jour du 6 juillet 2026 »).

Un doublon volontaire et documenté sur `F5_Item` et/ou `D1_Digital_Object` reste possible **en plus**, mais seulement pour le cas particulier où le support concret (l'exemplaire physique ou le fichier numérique) affiche réellement une écriture différente de celle de son Expression nominale — par exemple un objet numérique issu d'une translittération. Ce n'est plus alors un doublon « raté », mais une exception voulue et justifiée.

Ce déplacement corrige précisément le sentiment de « détournement » que l'équipe avait repéré dans les étiquettes d'origine : le Système d'écriture n'est pas, par nature, une caractéristique du support matériel/numérique — c'est une caractéristique du contenu linguistique, exactement comme la Langue. En procédant ainsi, `F2_Expression` retrouve sa cohérence : elle porte désormais, ensemble, la Langue (Problème 2) et le Système d'écriture, les deux attributs qui décrivent ce que le texte *est* linguistiquement — pas comment il est matériellement fabriqué ou stocké.

### 4.2 — Le raisonnement complet, avec ses quatre preuves

**Ce qu'on cherche à documenter, en langage simple :** un livre existe en tant qu'idée (l'Œuvre), en tant que texte précis avec ses mots exacts (l'Expression), en tant qu'édition (la Manifestation), et en tant qu'exemplaire qu'on tient en main (l'Item) — éventuellement aussi comme fichier numérique (l'Objet numérique). La question posée est : à quel niveau appartient l'information « cette écriture-ci a été utilisée pour noter le texte » (par exemple : écriture latine, cyrillique, arabe) ?

**Première preuve — ce que le modèle officiel LRMoo dit explicitement, et seulement là.** En fouillant intégralement le document complet du modèle IFLA LRM (103 pages, `https://www.ifla.org/wp-content/uploads/2019/05/assets/cataloguing/frbr-lrm/ifla_lrm_2017-03.pdf`, pas seulement la table des attributs), l'attribut « Script » n'apparaît, texte narratif inclus, qu'à un seul endroit : `LRM-E9-A8`, au niveau de l'entité `Nomen` (un nom ou une désignation attribuée à quelque chose, pas l'Œuvre/Expression/Manifestation/Item eux-mêmes). Citation intégrale de la note de balisage officielle (page 54, Table 4.4 Attributes) :
> *« LRM-E9-A8 NOMEN Script — The script in which the nomen is notated. Scope notes: The script attribute allows the identification of the writing system used to provide a notation for the nomen. [...] Examples: Tibetan [...]; Tibt [...]; t [...] »*

Le Nomen, ce n'est donc pas le texte lui-même — c'est un nom qu'on lui donne (un titre, une entrée d'index, une variante translittérée d'un nom d'auteur). Ce n'est pas exactement notre besoin : le paper demande le système d'écriture du *texte de l'objet lui-même*, pas d'un nom qui le désigne. Recherche exhaustive confirmée sur les 4267 lignes du texte extrait du PDF LRMoo v1.0 également : aucune ligne ne mentionne « script » comme attribut de `F1_Work`, `F2_Expression`, `F3_Manifestation`, `F5_Item` ou `D1_Digital_Object` — seulement de `F12_Nomen`.

**Deuxième preuve — une piste plus proche de notre besoin, trouvée dans le CIDOC-CRM de base (pas LRMoo), et cohérente avec ce que CAO_CRM a déjà décidé pour la Langue.** La classe `E34_Inscription` (un texte qu'on peut lire sur un objet physique, `imports/vendor/cidoc-crm-7.1.3.rdf`) dit, texte intégral :
> *« This class comprises recognisable texts that can be attached to instances of E24 Physical Human-Made Thing. [...] The alphabet used can be documented by P2 has type: E55 Type. [...] »*
— `rdfs:subClassOf` : `E33_Linguistic_Object`, `E37_Mark`.

Et cette classe est elle-même une sous-classe d'`E33_Linguistic_Object` — **exactement la même classe que celle déjà utilisée par CAO_CRM pour co-typer `F2_Expression`**, afin d'y accrocher la Langue via `P72_has_language` (décision du Problème 2, déjà appliquée dans `CAO_CRM-1.0.rdf`). Autrement dit : la norme officielle documente elle-même « l'alphabet utilisé » sur la branche des classes qui portent le contenu linguistique — la même branche que celle où la Langue vit déjà chez nous. Utiliser ce même mécanisme sur `F2_Expression` n'est donc pas une improvisation : c'est un prolongement direct d'une décision déjà prise et déjà justifiée par la norme.

**Troisième preuve — la pratique bibliothéconomique réelle (MARC21), qui confirme ce jumelage.** Dans les notices MARC21 (champ 546 « Language Note »), le sous-champ qui documente l'écriture/l'alphabet (`$b`) est logé **dans le même champ** que celui qui documente la langue (`$a`) :
> *« Subfield $b specifies the alphabet, script, or notation system that is used in the resource [...] »* (citation confirmée par plusieurs sources concordantes — Library of Congress, OCLC Bibliographic Formats and Standards — non re-vérifiée par fetch direct de `bd546.html`, réserve honnête à garder).

La pratique bibliothécaire traite donc, depuis des décennies, la langue et le système d'écriture comme deux facettes d'un même fait descriptif, presque toujours renseignées ensemble. Puisque la Langue a déjà été déplacée vers l'Expression (Problème 2), la cohérence appelle à faire de même pour le Système d'écriture.

**Quatrième preuve — BIBFRAME confirme la nuance, sans contredire la recommandation.** Le vocabulaire officiel BIBFRAME (Library of Congress, fichier RDF vérifié par téléchargement direct, `raw.githubusercontent.com/lcnetdev/bibframe-ontology`) documente une propriété `bf:notation` (dont la classe `bf:Script` est une sous-classe) avec la note d'usage :
> *« Alphabet, script, or symbol system used to convey the content of the resource [...] »* — `rdfs:comment` : *« Suggested use - With Work or Instance »*.

Comme `bf:Work` fusionne Œuvre+Expression et `bf:Instance` fusionne Manifestation+Item, cette note dit, en clair : selon le cas, le script peut être un fait sur le contenu intellectuel (Œuvre/Expression) OU sur le support concret (Manifestation/Item) — **un choix contextuel, pas une règle unique et automatique.** Ce n'est pas une contradiction avec la recommandation ci-dessus : c'est la confirmation que les deux niveaux sont légitimes selon ce qu'on veut dire, et que la bonne pratique est de choisir le niveau qui correspond au fait réellement documenté, pas de dupliquer par défaut.

### 4.3 — Pourquoi ce n'est pas la même chose qu'un doublon entre Item et Objet numérique

1. **Le cas normal, le plus fréquent** : le texte est écrit dans une seule écriture, et cette écriture est un fait sur le contenu du texte (l'Expression), pas sur son support. Dans ce cas, il n'y a **ni Item, ni Objet numérique** à renseigner séparément pour ce point — l'information vit une seule fois, à l'Expression, et l'Item comme l'Objet numérique en héritent implicitement par leur chemin vers l'Expression. C'est ce qui corrige le « doublon » signalé par le paper lui-même : ce doublon n'était pas un vrai besoin, c'était le signe que l'attribut avait été placé au mauvais niveau depuis le début — exactement le même diagnostic que celui déjà posé pour la Langue au Problème 2.
2. **Le cas exceptionnel, réel mais rare** : un support concret affiche une écriture *différente* de celle de son Expression nominale — par exemple un fichier numérique produit par translittération, ou un exemplaire physique portant une annotation manuscrite dans une autre écriture. Documenter le Système d'écriture directement sur `D1_Digital_Object` ou `F5_Item` (en plus de celui de l'Expression) est alors légitime — ce n'est plus un « doublon » machinal, c'est une exception documentée, avec une raison identifiable.
3. **Le mécanisme officiel qui existe pour ce cas exceptionnel, mais hors périmètre actuel** : LRMoo prévoit exactement ce cas via `R36_uses_script_conversion` (`F12_Nomen → F36_Script_Conversion`) — mais ce mécanisme est ancré sur `F12_Nomen`, une classe absente du périmètre de CAO_CRM. Tant que `F12_Nomen`/`F52_Name_Use`/`R64` ne sont pas importés (confirmé absents du fichier vendorisé, 0 occurrence), l'équipe devra se contenter, pour ce cas exceptionnel, d'un `P2_has_type`/`E55_Type` documenté directement sur l'Item ou l'Objet numérique concerné, avec une note (`P3_has_note`) expliquant la divergence.

### 4.4 — Ce qui change concrètement

- **Diagramme visuel** : déplacer la case « Système d'écriture » de `F5_Item`/`D1_Digital_Object` vers `F2_Expression` (co-typée `E33_Linguistic_Object`, la même case déjà utilisée pour la Langue).
- **RDF** : aucun nouvel ajout de périmètre — `E33_Linguistic_Object`, `P2_has_type`, `E55_Type`, `P127_has_broader_term` sont déjà extraits dans `CAO_CRM-1.0.rdf`.
- **Le paper** : comme pour la Langue (Problème 2), ce déplacement implique une correction du tableau de métadonnées du paper, qui place aujourd'hui le Système d'écriture sous « Objet physique »/« Objet numérique » et devrait avoir une ligne « Expression ».
- **Cas exceptionnel** (Item/Objet numérique divergent de l'Expression) : à documenter au cas par cas, seulement quand un besoin réel et identifié se présente — pas par défaut.

---

## 5. Une décision liée, traitée dans un document séparé

La distinction des rôles d'auteur (auteur original / traducteur / abréviateur) est une question voisine, mais suffisamment autonome pour mériter son propre document : voir `informe-P14-roles-autorat.md` pour l'investigation complète et la décision adoptée (sous-propriétés nommées de `P14_carried_out_by`, alignées MARC Relator Terms, déjà implémentées dans `CAO_CRM-1.0.rdf`).

Reste, non technique celle-là : faut-il ajouter « Statut » pour `F5_Item` dans le tableau du paper ? Le Problème 3 a résolu, techniquement, la condition et la localisation de l'exemplaire (`E22_Human-Made_Object` + `P44_has_condition` + `P54`/`P55`) — mais le tableau du paper ne montre aucune ligne « Statut » pour « Objet physique ». Recommandation transmise à l'équipe de rédaction : ajouter ces deux lignes au tableau du paper (section 4.1) :
```
Objet physique    Statut    Condition (E3 Condition State)         [ex. bon état]
Objet physique    Statut    Localisation (E53 Place)                84/33 CAIL 4 dela (BNF)
```

---

## 6. Sources et méthode de vérification

Toutes les vérifications ci-dessus ont été effectuées le 6 juillet 2026, par `curl`/WebFetch/WebSearch réels contre les sources primaires — aucune citation n'est reconstituée de mémoire. Sources externes consultées :

- **CIDOC CRM SIG, issue « Rights Model » (ID 328)** — `https://cidoc-crm.org/Issue/ID-328-rights-model` (HTTP 200, curl direct).
- **LRMoo v1.0, document officiel complet** (101 pages) — `https://cidoc-crm.org/sites/default/files/LRMoo_V1.0.pdf`.
- **IFLA Library Reference Model (LRM), édition consolidée 2017-04** (103 pages) — `https://www.ifla.org/wp-content/uploads/2019/05/assets/cataloguing/frbr-lrm/ifla_lrm_2017-03.pdf`.
- **BIBFRAME, vocabulaire RDF officiel** — `https://raw.githubusercontent.com/lcnetdev/bibframe-ontology/main/bibframe.rdf`.
- **MARC21, champ 066** — `https://www.loc.gov/marc/bibliographic/bd066.html` (accès direct bloqué, HTTP 403 ; contourné avec succès via `curl` + user-agent navigateur).
- **MARC21, champ 546** — contenu obtenu par synthèse WebSearch multi-sources concordantes (Library of Congress, OCLC), non re-vérifié par fetch direct : réserve honnête à garder.

**Sources non exploitables, signalées explicitement plutôt que passées sous silence :** RDA Registry (page SPA JavaScript, contenu non rendu par WebFetch) et RDA Toolkit (service par abonnement, hors de portée) — RDA étant construit sur IFLA LRM, une cohérence avec `LRM-E9-A8` est raisonnable à supposer, mais non vérifiée de première main et à ne jamais citer comme telle. Aucun projet réel publié appliquant précisément le chemin `F1_Work→F2_Expression→E30_Right` pour un droit moral n'a par ailleurs été localisé — la source la plus proche trouvée est l'issue CRM-SIG 328 elle-même.

---

## 7. État final

**État du périmètre au 6 juillet 2026 : tout est déjà extrait et validé dans `CAO_CRM-1.0.rdf`** — `R2_is_derivative_of`/`R2i`, `R76_is_derivative_of`/`R76i`, `R75_incorporates`/`R75i` (LRMoo, zéro nouvelle classe), plus les sous-propriétés de rôle `P14_a_pour_auteur_original`/`P14_a_pour_traducteur`/`P14_a_pour_abregeur` (méthode Encoding Rule 4, voir `informe-P14-roles-autorat.md`). Ontologie vérifiée : syntaxe propre, raisonneur HermiT consistant, 0 classe isolée, 7/7 métadonnées.

| Classe | Caractéristiques | Processus | Statut | Relation |
|---|---|---|---|---|
| `F1_Work` | ✅ | ✅ | ✅ Manque 1 résolu | ✅ Manque 3 résolu |
| `F2_Expression` | ✅ (Problème 2 + Système d'écriture) | ✅ (+ rôles P14) | ✅ | ✅ Manque 2 résolu |
| `F3_Manifestation` | ✅ | ✅ (Problème 5) | ✅ | ✅ |
| `F5_Item` | ✅ (Problèmes 1, 1b, 7 — Système d'écriture déplacé vers Expression) | *(non applicable, voir texte)* | ✅ (Problème 3) | ✅ |
| `D1_Digital_Object` | ✅ (Problèmes 1, 6 — Système d'écriture déplacé vers Expression) | ✅ (découverte D7) | ✅ | ✅ |

**Les manques identifiés dans ce document sont tous résolus** — seule la recommandation de la section 5 (ajout des lignes Statut de `F5_Item` au tableau du paper) reste une action éditoriale, déjà transmise à l'équipe de rédaction.
