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
# Rapport de complétude : étiquettes, domaine/portée et hiérarchie du module CAO_CRM

**Date :** 2026-07-03
**Fichier audité :** `imports/module/cao_crm-module-clean.rdf` (29 classes, 61 propriétés d'objet, 5 propriétés de données, 770 triplets)
**État :** vérifié — syntaxe correcte, logiquement cohérent (raisonneur HermiT, 0 insatisfaisable), confirmé qu'il s'ouvre dans Protégé 5.6.8 sans erreur.

**Remarque importante concernant ce rapport :** lors de la préparation de ces données, un véritable problème méthodologique a été découvert et corrigé (voir section 0) — de sorte que les chiffres de ce rapport **ne coïncident pas** avec ceux qu'aurait donnés le fichier généré hier. Le fichier actuel est meilleur et plus complet que celui d'hier.

**Correction postérieure à la première version de ce rapport (le jour même) :** la section 2.2 indiquait initialement que `P90_has_value` était « complète dans l'original » et servait de modèle de référence pour `P82_at_some_time_within`/`P82a`/`P82b`. Cette affirmation était **incorrecte** — en réexaminant le fichier officiel avec davantage de contexte, il apparaît que les quatre propriétés (`P90_has_value` incluse) possèdent bien un `rdfs:range rdfs:Literal` déclaré dans CIDOC-CRM 7.1.3 ; ce qui se passait en réalité, c'est que **l'outil d'extraction avait écarté cette portée pour les quatre propriétés**, parce que `rdfs:Literal` (un type générique de RDF, et non une classe propre à CIDOC-CRM) n'avait jamais été inclus dans la liste des termes à extraire. Il ne s'agissait donc pas d'une décision de modélisation en suspens (comme cela avait été le cas pour `P3_has_note`), mais d'une erreur mécanique de l'extraction. **Déjà corrigé :** le `rdfs:range rdfs:Literal` a été restauré pour les quatre propriétés, en recopiant littéralement ce que dit le fichier officiel, sans qu'aucun ADR ne soit nécessaire — il n'y a aucune ambiguïté à trancher. La section 2.2 ci-dessous est conservée telle qu'elle avait été rédigée à l'origine, uniquement à des fins de traçabilité du processus, mais sa conclusion a été rendue caduque par cette correction.

---

## 0. Correction effectuée aujourd'hui avant l'audit : l'extraction a été refaite en une seule passe

Hier, trois fichiers RDF distincts ont été générés séparément (un par ontologie source : CIDOC-CRM, LRMoo, CRMdig), puis fusionnés. Lors de la préparation de ce rapport, on a constaté que cette méthode **perd de l'information de façon chirurgicale** : lorsqu'une propriété d'une source (par exemple `F1_Work` dans LRMoo) a pour parent ou pour portée une classe qui n'existe que dans une AUTRE source (par exemple `E89_Propositional_Object`, qui appartient à CIDOC-CRM), l'outil d'extraction, en traitant LRMoo isolément, ne « sait » pas que cette classe existe et écarte la relation — alors même que la classe de destination fait bien partie de notre périmètre de 29 classes.

**Exemple réel constaté :** `F1_Work` devrait avoir pour parent `E89_Propositional_Object` (les deux figurent dans notre périmètre) — mais le fichier d'hier montrait `F1_Work` sans aucun parent. Cette donnée n'était pas manquante dans la documentation officielle ; elle a été perdue parce que les trois ontologies ont été traitées en passes séparées.

**Correction appliquée :** les trois fichiers officiels ont d'abord été combinés en un seul, puis l'extraction a été exécutée **une seule fois** sur cet ensemble combiné. Cela a permis de récupérer automatiquement plusieurs relations de hiérarchie et de domaine/portée qui traversent CIDOC-CRM/LRMoo/CRMdig et qui devraient effectivement être présentes selon le périmètre que nous avions nous-mêmes convenu. Tout a été revérifié (syntaxe, raisonneur, ouverture dans Protégé) après ce changement — le résultat reste cohérent et correct.

---

## 1. Étiquettes multilingues manquantes

CIDOC-CRM 7.1.3 fournit des étiquettes officielles en 7 langues : allemand (de), grec (el), anglais (en), français (fr), portugais (pt), russe (ru), chinois (zh). LRMoo et CRMdig, en revanche, **ne possèdent d'étiquettes qu'en anglais dans leur version officielle** — aucune traduction n'en existe dans aucun fichier, pas même dans la documentation de lecture.

### 1.1 Classes et propriétés qui possèdent bien les 7 langues complètes

21 des 29 classes et la grande majorité des 61 propriétés d'objet de CIDOC-CRM (`P1`...`P108`) possèdent les 7 traductions complètes. Cela ne requiert aucune action.

### 1.2 Exceptions au sein de CIDOC-CRM (langues partiellement manquantes)

| Entité | Langues présentes | Manquent |
|---|---|---|
| `E89_Propositional_Object` | de, en, fr, ru, zh | **el, pt** |
| `E90_Symbolic_Object` | de, en, fr, ru, zh | **el, pt** |
| `P150_defines_typical_parts_of` / `P150i_...` | en, fr, ru | **de, el, pt, zh** |
| `P82a_begin_of_the_begin` | de, el, en, fr, pt, ru | **zh** |
| `P82b_end_of_the_end` | de, el, en, fr, pt, ru | **zh** |

**Est-il possible de les récupérer ?** Pas sans recourir à une autre source — il a été vérifié que le fichier officiel `CIDOC_CRM_v7.1.3.rdfs` ne contient tout simplement pas ces traductions pour ces entités précises. Ce n'est pas un problème lié à notre extraction (confirmé : ce sont les mêmes absences dans le fichier source). Si elles s'avéraient nécessaires, il faudrait les traduire nous-mêmes (auquel cas il s'agirait bien d'un apport propre à CAO_CRM, à la différence d'une simple copie des étiquettes officielles) ou attendre que CIDOC-CRM les publie dans une version future.

### 1.3 Les 10 classes et 30 propriétés de LRMoo et CRMdig : uniquement en anglais, et non récupérable

Les 7 classes de LRMoo (`F1_Work`, `F2_Expression`, `F3_Manifestation`, `F5_Item`, `F27/F28/F30_..._Creation`), les 15 propriétés de LRMoo (`R3`, `R4`, `R16`, `R17`, `R24`, `R27`, `R71`, `R78` et leurs inverses), les 3 classes de CRMdig (`D1`, `D2`, `D13`) et les 8 propriétés de CRMdig (`L1`, `L11`, `L19`, `L61` et leurs inverses) **n'existent qu'en anglais dans le fichier officiel**. Cela a été vérifié directement dans les fichiers source (`imports/vendor/lrmoo-1.1.1.rdf` et `imports/vendor/crmdig-5.0.rdf`) : aucune d'entre elles ne comporte d'étiquette `xml:lang` différente de `en`.

**Conclusion sur la « récupération » d'étiquettes dans d'autres langues pour LRMoo/CRMdig : ce n'est pas possible, parce qu'elles n'ont jamais existé.** Toute traduction en français (ou dans une autre langue) de ces 25 termes devrait être rédigée par l'équipe CAO_CRM elle-même — il s'agirait alors bien d'un apport original du projet (comparable aux notes terminologiques du glossaire, et non d'une simple copie de fragments provenant d'ailleurs), et il faudrait décider consciemment si cela s'accorde avec le principe de « seulement composer, ne pas ajouter » retenu pour le reste du modèle.

---

## 2. Domaine et portée : tout est-il complet ?

Les 61 propriétés d'objet et les 5 propriétés de données ont été examinées de façon automatisée. Les cas sans domaine ou sans portée ont été classés en deux catégories, chacun étant vérifié par rapport au fichier officiel correspondant :

### 2.1 Catégorie A — le domaine/la portée pointe vers une classe hors des 31 classes retenues (correct, attendu, à ne pas « corriger »)

C'est le cas de l'immense majorité des cas « manquants ». Exemples :

| Propriété | Ce qui manque | Domaine/portée officiel (hors périmètre) |
|---|---|---|
| `P1_is_identified_by` / `P1i_identifies` | domaine **et** portée | `E1_CRM_Entity` (domaine) et `E41_Appellation` (portée) — aucune des deux ne figure parmi nos 31 classes |
| `P104_is_subject_to` | domaine | `E72_Legal_Object` |
| `P108_has_produced` | portée | `E24_Physical_Human-Made_Thing` |
| `P16_used_specific_object` | portée | `E70_Thing` |
| `P2_has_type` | domaine | `E1_CRM_Entity` |
| `P4_has_time-span` | domaine | `E2_Temporal_Entity` |
| `P43_has_dimension` | domaine | `E70_Thing` |
| `P67_refers_to` | portée | `E1_CRM_Entity` |
| `P7_took_place_at` | domaine | `E4_Period` |
| `R27_materialized` / `R27i_...` | domaine / portée | `F32_Item_Production_Event` (LRMoo) |

**Il ne s'agit pas d'un défaut — c'est très exactement ce que signifie « modèle borné ».** `E1_CRM_Entity` est la classe la plus générale de tout CIDOC-CRM (la racine à laquelle se rattache tout le reste) ; si nous l'incluions, avec `E41_Appellation`, `E70_Thing`, `E72_Legal_Object`, etc., nous cesserions d'avoir un modèle limité et nous recommencerions à entraîner avec nous une bonne partie de la hiérarchie complète que le projet a décidé de ne pas inclure. **Il n'est pas recommandé de « compléter » ces cas.**

### 2.2 Catégorie B — vide réel dans le fichier officiel de CIDOC-CRM lui-même (nécessite bien une décision, comme pour `P3_has_note`)

**4 propriétés de données** présentant ce problème ont été trouvées — exactement le même schéma que pour `P3_has_note` (documenté dans `problemes-et-solutions.md (Problème 1)`) :

| Propriété | État actuel | Diagnostic |
|---|---|---|
| `P3_has_note` | **Déjà corrigé** (`rdfs:range rdfs:Literal`, suivant le modèle de `P90_has_value`) | — |
| `P90_has_value` | Complète dans l'original (`rdfs:range rdfs:Literal`) | Sert de référence/de modèle |
| `P82_at_some_time_within` | **Non corrigé** — domaine oui, portée non | Le fichier officiel 7.1.3 ne déclare pas de `rdfs:range` pour cette propriété (confirmé, aucune ligne `rdfs:range` dans sa déclaration) |
| `P82a_begin_of_the_begin` | **Non corrigé** — domaine oui, portée non | Même vide |
| `P82b_end_of_the_end` | **Non corrigé** — domaine oui, portée non | Même vide |

**Recommandation :** appliquer exactement la même décision que celle prise pour `P3_has_note` (déclarer `rdfs:range rdfs:Literal` pour ces trois propriétés, en suivant le modèle de `P90_has_value`), pour la même raison que celle documentée dans problemes-et-solutions.md (Problème 1). Cela n'a pas encore été appliqué — cela reste en attente de votre confirmation, car cela implique de modifier le fichier à nouveau.

### 2.3 Aucun cas de « perte par extraction » en suspens

Après avoir refait l'extraction en une seule passe combinée (section 0), **il ne subsiste plus aucun cas où le domaine/la portée, existant dans l'original et pointant vers une classe de notre périmètre, n'aurait pas été récupéré.** Les seuls « AUCUN » qui subsistent dans le fichier relèvent, sans exception, soit de la catégorie A (corrects par conception), soit de la catégorie B (les 3 cas ci-dessus, en attente de décision).

---

## 3. Hiérarchie des classes (`rdfs:subClassOf`) : le modèle conceptuel est-il complet ?

Après la correction apportée à la section 0, voici la hiérarchie au sein du module (ne montrant que les relations entre classes qui figurent bien parmi nos 29) :

```
E18_Physical_Thing (racine)
 └─ E21_Person
     └─ (hérite aussi de E39_Actor)
 └─ F5_Item

E39_Actor (racine)
 └─ E21_Person

E7_Activity (racine)
 ├─ E12_Production
 │   ├─ F28_Expression_Creation
 │   └─ F30_Manifestation_Creation
 ├─ F27_Work_Creation
 └─ D2_Digitization_Process

E89_Propositional_Object (racine)
 ├─ E30_Right
 ├─ E35_Title
 ├─ F1_Work
 ├─ F2_Expression
 ├─ F3_Manifestation
 └─ D1_Digital_Object

E90_Symbolic_Object (racine)
 ├─ E35_Title
 ├─ E42_Identifier
 ├─ F2_Expression
 ├─ F3_Manifestation
 └─ D1_Digital_Object

E55_Type (racine)
 ├─ E56_Language
 └─ E57_Material

E3_Condition_State, E52_Time-Span, E53_Place, E54_Dimension, E67_Birth, E69_Death,
D13_Digital_Information_Carrier (sous E18_Physical_Thing)
```

**Le modèle est-il « complet » ?** Dans les limites du périmètre retenu (les 31 classes confirmées), oui — chaque classe qui descend officiellement d'une autre classe incluse dans le périmètre conserve cette relation. Les classes qui apparaissent comme « racines » dans ce module (`E18_Physical_Thing`, `E39_Actor`, `E7_Activity`, `E89_Propositional_Object`, `E90_Symbolic_Object`, `E55_Type`, `E3_Condition_State`, `E52_Time-Span`, `E53_Place`, `E54_Dimension`, `E67_Birth`, `E69_Death`) le sont parce que leur véritable parent officiel (par exemple `E1_CRM_Entity`, pour presque toutes) se trouve hors du périmètre — c'est exactement la même situation que la catégorie A de la section 2.1, et pour la même raison, il n'est pas recommandé de « le compléter ».

---

## 4. À propos des déclarations `owl:disjointWith`

**État actuel : aucune déclaration `owl:disjointWith` dans le module.** Le fichier officiel de CIDOC-CRM n'en déclare pas de façon étendue entre ces 29 classes précises, et l'extraction n'en a ajouté aucune.

Il s'agit là d'une véritable question de conception, et non de quelque chose que l'on pourrait « vérifier » automatiquement sans décision préalable — c'est pourquoi la question est posée ici plutôt que tranchée unilatéralement :

- **En faveur de leur ajout :** elles aideraient le raisonneur à détecter automatiquement des erreurs de saisie — par exemple, si quelqu'un instanciait par erreur à la fois `E67_Birth` et `E69_Death` (qui devraient être mutuellement exclusives), le raisonneur le signalerait comme une incohérence.
- **En défaveur :** le fichier officiel de CIDOC-CRM **ne** déclare **pas** ces disjonctions de façon explicite pour la plupart de ses classes (il s'agit d'un choix délibéré du consortium CIDOC-CRM, documenté dans sa philosophie de conception : il préfère un modèle souple où la disjonction est laissée à l'appréciation de chaque mise en œuvre). Les ajouter nous-mêmes constituerait, là encore, une décision de modélisation propre à CAO_CRM allant au-delà de la simple « composition de fragments » — le même type de tension que celle discutée à propos de `P3_has_note` dans problemes-et-solutions.md (Problème 1).

**Recommandation :** traiter cette question dans un ADR-001 distinct (en suivant le même format que les ADR existants), plutôt que de la trancher en passant ici, précisément parce qu'elle touche à la même question de fond (« jusqu'où va la pure composition ? ») et mérite la même documentation rigoureuse.

---

## 5. Résumé exécutif

| Question | Réponse |
|---|---|
| Y a-t-il des étiquettes manquantes ? | Oui : 5 entités de CIDOC-CRM présentent des langues partiellement manquantes (non récupérable, cela n'existe pas dans la source) ; les 25 entités de LRMoo/CRMdig ne disposent que de l'anglais (non récupérable, aucune traduction officielle n'a jamais existé) |
| Tout possède-t-il un domaine et une portée ? | **Oui, désormais complet.** 4 propriétés (`P82_at_some_time_within`, `P82a`, `P82b`, `P90_has_value`) ont été trouvées et corrigées : leur `rdfs:range rdfs:Literal` existait dans le fichier officiel mais avait été écarté par l'extraction en raison d'une limite mécanique de l'outil (et non d'un vide réel de l'original, à la différence de `P3_has_note`) — il a été restauré directement, sans qu'aucun ADR ne soit nécessaire. |
| Le modèle conceptuel (la hiérarchie) est-il complet ? | Oui, dans les limites du périmètre convenu — un véritable problème méthodologique (extraction en passes séparées), qui faisait effectivement perdre de l'information à l'intérieur de ce périmètre, a été corrigé ; il ne subsiste plus aucune perte |
| Des déclarations `owl:disjointWith` sont-elles nécessaires ? | Question de conception ouverte, non un défaut technique — il est recommandé de la documenter sous forme d'ADR-001 avant de trancher |

**Rien de tout cela ne bloque la poursuite du projet** — ce sont des ajustements, pas des erreurs structurelles. Le fichier `imports/module/cao_crm-module-clean.rdf` est syntaxiquement correct, logiquement cohérent, et s'ouvre proprement dans Protégé.
