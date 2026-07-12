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
# Rapport de mise en œuvre : du modèle JSON au module RDF borné de CAO_CRM

**Date :** 2026-07-03
**État du fichier final :** vérifié syntaxiquement correct, logiquement cohérent, et confirmé qu'il s'ouvre sans erreur dans Protégé 5.6.8.
**Fichier final de cette étape :** `imports/module/cao_crm-module-clean.rdf`

---

## 0. Ce qui a été fait, en une phrase

On a pris le diagramme conceptuel du modèle CAO_CRM (enregistré sous la forme `CRM_V8.json`, un fichier exporté de draw.io/diagrams.net), on en a extrait les noms exacts des classes et des propriétés que l'équipe a confirmés comme constituant le périmètre réel du modèle, puis, à partir de cette liste, on a généré automatiquement — et non manuellement — un fichier RDF ne contenant *que* ces éléments, repris littéralement des fichiers officiels de CIDOC-CRM, LRMoo et CRMdig, sans importer le reste de ces trois ontologies (qui totalisent ensemble des milliers de classes et de propriétés).

---

## 1. Point de départ : le diagramme, et non le texte

L'article du consortium Ariane décrit le modèle CAO_CRM au moyen d'un diagramme (sa « Figure 2 »). Ce diagramme existe également comme fichier de travail : `CRM_V8.json`, comportant **9 pages** correspondant aux différentes parties du modèle :

| Page du diagramme | Ce qu'elle représente |
|---|---|
| `Hiérarchie` | L'ossature du modèle : comment s'articulent Œuvre → Expression → Manifestation → Item → Objet numérique |
| `F1` | Tout ce qui concerne l'Œuvre (`F1_Work`) |
| `F2` | Tout ce qui concerne l'Expression (`F2_Expression`) |
| `F3` | Tout ce qui concerne la Manifestation (`F3_Manifestation`) |
| `F5` | Tout ce qui concerne l'Item physique (`F5_Item`) |
| `D1` | Tout ce qui concerne l'Objet numérique (`D1_Digital_Object`) |
| `D2` | Le processus de numérisation (`D2_Digitization_Process`) |
| `model` | Vue d'ensemble (les mêmes éléments, réunis) |
| `exemple` | Un cas d'usage illustratif avec des données réelles (le roman *Le Rouge et le Noir*) |

Chaque « page » est, techniquement, une liste de cases et de flèches (`cells`), et chaque case/flèche porte un texte (`label`) — parfois le nom technique d'une classe ou d'une propriété de CIDOC-CRM/LRMoo/CRMdig (par exemple `E35_Title`), et parfois simplement une étiquette descriptive en français destinée à faciliter la lecture visuelle du diagramme (par exemple « Titre »).

---

## 2. Étape 1 — Extraire les noms techniques réels à partir du JSON

**Objectif :** distinguer, parmi les 814 étiquettes du diagramme, celles qui sont véritablement des noms de classes/propriétés de CIDOC-CRM/LRMoo/CRMdig, et celles qui ne sont que du texte explicatif en français (lequel ne devait pas être traité comme faisant partie du modèle formel).

**Comment cela a été fait :** un script Python a lu le JSON, parcouru les 7 pages de module (en excluant `model` et `exemple`, qui sont des vues répétant les mêmes éléments) et n'a retenu que les étiquettes correspondant au motif propre aux noms techniques réels de CIDOC-CRM/LRMoo/CRMdig : une lettre (`E`, `F`, `D`, `P`, `R` ou `L`) suivie d'un nombre et d'un tiret bas — par exemple `E35_Title`, `F1_Work`, `P1_is_identified_by`. Les étiquettes en français comme « Titre » ou « Type de droit » ne correspondent pas à ce motif et ont été automatiquement écartées.

Résultat de ce premier filtrage automatique : 30 classes et 36 propriétés (chaque propriété étant comptée une seule fois, sans que son inverse ne soit comptée à part).

**Vérification humaine :** l'équipe a examiné cette liste extraite et l'a corrigée et complétée, en y ajoutant :
- `F5_Item`, que le filtre automatique n'avait pas capté car, dans le diagramme, il était écrit « F5 Item » (avec une espace, et non un tiret bas).
- Les propriétés inverses explicites (par exemple, non seulement `R16_created` mais aussi `R16i_was_created_by`), car, dans CIDOC-CRM/LRMoo/CRMdig, chaque relation possède deux URI distincts (un pour chaque sens), et le diagramme ne les faisait pas toujours apparaître séparément.

**Liste finale confirmée par l'équipe (2026-07-03) :** 31 classes, 60 propriétés d'objet (30 paires directe/inverse) et 4 propriétés de données. Voir le détail complet dans l'échange de cette date-là ; la liste est également reprise sous forme de commentaires dans les fichiers de termes utilisés à l'étape 3.

---

## 3. Étape 2 — Vérifier que chaque nom existe réellement dans les fichiers officiels

Avant de générer quoi que ce soit, chacun des quelque 95 noms a été recherché littéralement (avec `grep`) dans les fichiers RDF/XML officiels déjà téléchargés dans ce dépôt (`imports/vendor/cidoc-crm-7.1.3.rdf`, `imports/vendor/lrmoo-1.1.1.rdf`, `imports/vendor/crmdig-5.0.rdf`), afin de confirmer que :

1. Le nom existe réellement (il ne s'agit pas d'une erreur de transcription du diagramme).
2. Il appartient bien à l'ontologie à laquelle on le rattachait (un même préfixe de lettre pouvant parfois prêter à confusion).

Cela a permis de repérer deux cas à corriger :

- **`E60_Number` et `E62_String` n'existent pas en tant qu'URI** dans aucun fichier officiel. Il ne s'agit pas d'une erreur : CIDOC-CRM précise, dans sa propre documentation, que ces « classes primitives » sont conçues pour être représentées directement comme une valeur de texte/nombre (`rdfs:Literal`), et non comme une entité dotée de son propre URI. Elles ont été exclues de la liste des classes à extraire (il reste 29 classes réelles pourvues d'un URI, sur les 31 initialement identifiées). Le détail complet de cette décision figure dans `problemes-et-solutions.md (Problème 1)`.
- **`P21_has_general_purpose`** (tel que transcrit initialement à partir du diagramme) n'existe pas ; le nom réel dans le fichier officiel est **`P21_had_general_purpose`** (au passé). Corrigé avant toute génération.

---

## 4. Étape 3 — Générer le RDF automatiquement avec ROBOT

**Outil utilisé :** [ROBOT](http://robot.obolibrary.org/), plus précisément sa commande `extract` avec la méthode `subset`.

**Pourquoi cet outil plutôt qu'un copier-coller manuel :** copier-coller manuellement les définitions depuis les fichiers officiels serait lent, propice aux erreurs de transcription, et surtout — comme cela s'est déjà produit dans ce même projet — c'est précisément le copier-coller manuel (ou une fusion mal réalisée dans Protégé) qui a été à l'origine des problèmes antérieurs (contamination de l'en-tête par « SKOS Vocabulary », perte d'axiomes, incohérence logique). Le recours à un outil automatique, alimenté par une liste de noms explicite et vérifiée, rend le processus :
- **Reproductible :** n'importe qui peut réexécuter la même commande et obtenir le même résultat.
- **Traçable :** le fichier d'entrée (la liste des termes) est conservé et peut être audité.
- **Fidèle à l'original :** ROBOT recopie les étiquettes, les commentaires et les définitions exactement tels qu'ils figurent dans le fichier source officiel, sans les réinterpréter.

**⚠ Correction apportée après la première version de cette section :** la première tentative a exécuté trois commandes séparées, une par ontologie source, chacune avec sa propre liste de termes (`terms-cidoc.txt`, `terms-lrmoo.txt`, `terms-crmdig.txt`). Cette méthode a été abandonnée : on a constaté qu'elle fait perdre les axiomes qui traversent plusieurs ontologies (par exemple, `F1_Work rdfs:subClassOf E89_Propositional_Object`, une relation LRMoo→CIDOC-CRM, disparaissait alors même qu'`E89_Propositional_Object` fait bien partie du périmètre), car, lors du traitement de LRMoo seul, `--method subset` ne reconnaît pas `E89_Propositional_Object` comme un terme « connu » dans ce fichier isolé. Le détail complet de cette découverte figure dans `informe-completitud-labels-domain-range.md`, section 0.

**La méthode finale et correcte, effectivement utilisée pour générer `ontology/CAO_CRM-1.0.rdf`, consiste à combiner les trois sources en un seul fichier avant l'extraction, avec une liste unique de termes :**

```bash
# 1. Combinar las tres fuentes oficiales en un solo grafo
riot --output=rdfxml imports/vendor/cidoc-crm-7.1.3.rdf \
                      imports/vendor/lrmoo-1.1.1.rdf \
                      imports/vendor/crmdig-5.0.rdf \
     > /tmp/combined-sources.rdf

# 2. Extraer el módulo en una sola pasada, con la lista completa de 95 términos
robot extract --input /tmp/combined-sources.rdf \
              --method subset \
              --term-file imports/module-terms.txt \
              --output imports/module/combined-module.ttl
```

**Le fichier `imports/module-terms.txt`** (inclus dans ce dépôt, également copié dans `imports/module-terms.txt`) correspond exactement à la liste des 95 termes — 31 classes (29 pourvues d'un URI réel, voir section 3) + 60 propriétés d'objet + 4 propriétés de données — que l'équipe a confirmée comme périmètre définitif de CAO_CRM. C'est le fichier d'entrée réel qui a produit le module final ; réexécuter les deux commandes ci-dessus avec ce même fichier reproduit exactement le même résultat.

La méthode `subset` (à la différence d'autres méthodes d'extraction de ROBOT, comme `mireot` ou `star`) extrait *exactement* les termes indiqués, sans entraîner automatiquement le reste de la hiérarchie de classes de l'ontologie source. C'est précisément ce dont CAO_CRM a besoin : un modèle composé et borné, et non une copie partielle déguisée des trois ontologies complètes. Combiner les sources avant l'extraction (plutôt que d'extraire chacune séparément) est ce qui permet de préserver cette propriété *sans* perdre les relations réelles qui traversent CIDOC-CRM, LRMoo et CRMdig au sein du périmètre choisi.

**Résultat de cette extraction, par source :**

| Source | Fichier généré | Lignes | Contenu |
|---|---|---|---|
| CIDOC-CRM 7.1.3 | `cidoc-crm-module.ttl` | 900 | 19 classes, 42 propriétés (38 d'objet + 4 de données) |
| LRMoo 1.1.1 | `lrmoo-module.ttl` | 179 | 7 classes, 15 propriétés d'objet |
| CRMdig 5.0 | `crmdig-module.ttl` | 93 | 3 classes, 8 propriétés d'objet |

Au total : **29 classes, 61 propriétés d'objet, 4 propriétés de données — 1172 lignes**, contre les milliers de classes et de propriétés que comptent les trois ontologies originales complètes.

---

## 5. Étape 4 — Un cas que l'extraction automatique n'a pas pu résoudre seule : `P3_has_note`

L'outil a fait son travail correctement, mais **a détecté et mis au jour** un problème déjà présent dans le fichier officiel de CIDOC-CRM : la propriété `P3_has_note` ne comporte, dans la version RDF/XML 7.1.3, aucun domaine ni aucune portée déclarés (alors que la documentation de lecture les décrit bien). En l'extrayant, ROBOT l'a laissée telle une simple annotation (étiquette + commentaire), sans type de propriété — ce qu'il y avait de plus sûr à faire, faute de savoir s'il s'agit d'une propriété reliant à une autre entité ou à une valeur de texte.

Ce vide a été comblé manuellement, mais **en reprenant littéralement la convention que le fichier officiel lui-même applique à sa propriété sœur `P90_has_value`** (celle-ci étant intégralement déclarée). La décision complète, avec les citations textuelles de la documentation officielle qui la justifient, est documentée dans `problemes-et-solutions.md (Problème 1)` — elle n'est pas reprise ici afin de ne pas dupliquer le contenu.

---

## 6. Étape 5 — Fusionner les trois modules et leur donner un en-tête propre

Les trois fichiers générés à l'étape 3 ont été combinés en un seul graphe avec `riot` (outil d'Apache Jena) :

```bash
riot --output=turtle cidoc-crm-module.ttl lrmoo-module.ttl crmdig-module.ttl > merged-module.ttl
```

**Problème rencontré lors de la fusion :** chacun des trois fichiers sources porte, hérité de son fichier d'origine, une déclaration `owl:Ontology` qui lui est propre (une pour CIDOC-CRM, une pour LRMoo, une pour CRMdig). En les réunissant, le fichier fusionné se retrouvait avec **trois identités d'« ontologie » distinctes et aucune identité propre à CAO_CRM** — exactement le type d'ambiguïté d'en-tête qui a causé le problème de « SKOS Vocabulary » déjà documenté dans ce projet (voir `validation/07-metadata/README.md`).

**Solution :** ces trois déclarations ont été supprimées (il s'agissait de triplets isolés, sans aucune autre annotation attachée, de sorte que leur suppression n'efface aucune information réelle) et une déclaration unique et propre a été ajoutée :

```turtle
<http://www.CAO_CRM.org/ontology/> rdf:type owl:Ontology .
```

Le fichier obtenu, `cao_crm-module-clean.rdf`, comporte **un seul en-tête, correspondant à CAO_CRM et à lui seul**.

---

## 7. Vérification : le fichier est-il prêt à être ouvert dans Protégé ?

Avant de valider définitivement le fichier, quatre vérifications indépendantes ont été effectuées, par ordre croissant d'exigence :

1. **Syntaxe RDF/XML** — vérifiée à l'aide de deux analyseurs distincts (`rapper` et `riot`), qui confirment tous deux que le fichier est bien formé : 751 triplets analysés sans aucune erreur.
2. **Cohérence logique** — vérifiée avec le raisonneur HermiT (via `robot reason`) : le modèle est cohérent, sans aucune classe ni propriété insatisfiable.
3. **Un en-tête d'ontologie unique** — confirmé après le nettoyage effectué à l'étape 6 (il y en avait trois auparavant ; il n'y en a désormais exactement qu'un, celui de CAO_CRM).
4. **Ouverture réelle dans Protégé 5.6.8** — Protégé a été lancé directement depuis le terminal en pointant vers ce fichier, et son propre journal d'activité a été lu en temps réel. Résultat textuel :

   ```
   Loading ontology from file:<repo>/imports/module/cao_crm-module-clean.rdf
   Finished loading file:<repo>/imports/module/cao_crm-module-clean.rdf
   Loading for ontology and imports closure successfully completed in 2180 ms
   ```

   Et la fenêtre de Protégé qui s'est ouverte affichait le titre correct : **`ontology (http://www.CAO_CRM.org/ontology/)`** — l'identifiant propre à CAO_CRM, et non celui de l'une quelconque des ontologies réutilisées, ni aucune contamination telle que celle de « SKOS Vocabulary » constatée précédemment.

   Seul avertissement (et non une erreur) : *« root element does not have an xml:base »* — une remarque informative de Protégé, non bloquante ; un `xml:base` explicite pourra être ajouté ultérieurement si on le souhaite, mais cela n'empêche ni d'ouvrir ni de travailler normalement avec le fichier.

**Conclusion : le fichier est correctement constitué, et il est confirmé qu'il s'ouvre sans erreur dans Protégé.**

---

## 8. Ce qui reste à faire après ce module

Ce module (`cao_crm-module-clean.rdf`) contient **uniquement les éléments réutilisés** de CIDOC-CRM/LRMoo/CRMdig, déjà bornés au périmètre confirmé par l'équipe. Il ne comprend pas encore :

- Les métadonnées propres à l'en-tête de CAO_CRM (auteur, description, licence, `owl:versionInfo`...) qui existaient bel et bien — correctement, sans contamination — dans les versions antérieures du fichier.
- Aucune restriction ni aucun axiome supplémentaire relevant de la composition propre à CAO_CRM (par exemple, la manière exacte dont `D1_Digital_Object` se rattache à `F2_Expression`, et si cela nécessite une restriction `owl:Restriction` qui ne serait pas déjà déclarée dans les sources).
- Les données d'exemple de la page `exemple` du diagramme (le cas du *Rouge et le Noir*), qui pourraient être converties en données de test réelles pour `test-data/`, afin que `03-shacl` cesse d'afficher « 0 Focus Nodes » (voir `validation/03-shacl/README.md`).

Ces étapes suivantes seront traitées séparément, chacune avec sa propre vérification avant d'être considérée comme achevée — en suivant la même rigueur que celle de ce rapport.
