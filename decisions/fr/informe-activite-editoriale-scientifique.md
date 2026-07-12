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
# La branche « activité éditoriale » (Manifestation, Item, Digital Object) : auteur, éditeur commercial, éditeur scientifique

**Date :** 8 juillet 2026
**Objet de ce document :** documenter un manque structurel resté non résolu jusqu'ici — le paper source du projet
présente explicitement, comme l'un des différenciateurs originaux de CAO_CRM face à LRMoo/CRMdig nu, une branche
signalant l'intervention d'un **éditeur scientifique** au niveau Manifestation (et, « dans un esprit similaire »,
au niveau Digital Object). Cette branche n'avait jamais été implémentée dans le RDF, n'était citée dans aucun des
documents de décision précédents, et n'avait donc été détectée par aucune des trois auditorías successives. Ce
document explique pourquoi, ce qui a été ajouté, et pourquoi la solution retenue distingue trois rôles — auteur,
éditeur commercial, éditeur scientifique — plutôt qu'un seul.
**Sources vérifiées :** `Paper_Article_Revue HN_V2.docx.pdf` (extraction `pdftotext`, citations intégrales
ci-dessous), `imports/vendor/lrmoo-1.1.1.rdf` et `imports/vendor/crmdig-5.0.rdf` (grep direct des scope notes
officiels), `CAO_CRM-final.drawio` (inspection directe de la structure XML du diagramme), et les fiches
RDF officielles des codes MARC Relator Terms `edt`/`pbl` (`https://www.loc.gov/marc/relators/relaterm.html`,
récupérées par téléchargement direct le 8 juillet 2026).
**Ce que ça implique pour la suite :** ce document complète `informe-P14-roles-autorat.md` (qui reste centré sur
la distinction des rôles d'auctorialité sur `F28_Expression_Creation`) sans le contredire — voir son propre
addendum du 8 juillet, qui renvoie ici.

---

## 1. Ce que dit le paper, texte intégral

Sur la Manifestation :
> *« Une autre différence consiste dans l'ajout d'une branche "activités éditoriales" (E7_Activity) aux
> manifestations, qui donne la possibilité de signaler l'intervention d'un éditeur scientifique dans
> l'établissement d'une version de l'oeuvre manifestée sur un support particulier ; dans certains cas, la
> manifestation n'est donc pas seulement le résultat (si on peut dire) d'une expression, qui a pour acteur le
> seul auteur, mais aussi d'un processus d'élaboration scientifique, qui retient et rejette des variantes, fixe
> les lections, organise le matériel disponible, engageant, de ce fait, la responsabilité d'un spécialiste. Cet
> aspect nous semble constituer un manque significatif du modèle LRMoo, ou du moins un point sur lequel cette
> ontologie ne permet pas une expression claire des responsabilités. »*

Sur l'objet numérique :
> *« Dans un esprit similaire, l'ajout d'une entité "E7_Activity", avec ses satellites (informations en lien avec
> le process et avec le statut), en lien avec D1_Digital_Object et D2_Digitization process, distingue notre
> modèle de ce qui est proposé via CRMDig, qui est très détaillé en ce qui concerne la représentation des
> techniques et outils impliqués dans les opérations de digitalisation, mais qui occulte le travail scientifique
> qui les motive, les détermine et les accompagne. »*

Le paper décrit donc lui-même ce manque comme une contribution centrale du modèle, pas un détail secondaire.
Aucun des documents de décision antérieurs (`problemes-et-solutions.md`, `complete-model.md`,
`informe-P14-roles-autorat.md`, les trois auditorías) ne cite ce passage — vérifié par recherche directe dans les
trois fichiers, aucune occurrence de « activités éditoriales » ni de `F30_Manifestation_Creation` associée à un
rôle d'acteur.

## 2. Ce que le diagramme prévoyait déjà, sans jamais l'avoir connecté au RDF

Inspection directe de `CAO_CRM-final.drawio` : les pages **F5** (Item), **D1** (Digital Object) et
**exemple** contiennent déjà un motif complet — une case `E7_Activity` (« Activités scientifiques ») reliée à
quatre satellites : `E21_Person` (« Responsable scientifique »), `E55_Type` (« Type d'activité »),
`E52_Time-Span` (« Date »), `E53_Place` (« Lieu de création »), plus l'objet principal (F5_Item / D1_Digital_Object)
— mais **aucune des flèches ne porte de nom de propriété**. La page **F3** (Manifestation) a une version partielle :
`F30_Manifestation_Creation` (déjà correctement relié à `F3_Manifestation` via `R24_created`) est aussi relié à un
acteur générique (`E39_Actor`, étiqueté « Pers. physique ou morale »), lui aussi sans propriété nommée.

Découverte supplémentaire en explorant la page `exemple` : cet acteur générique représente en réalité **l'éditeur
commercial** — identifié par la chaîne littérale `"Editeur et imprimeur Le Divan"^^xsd:string` — et non l'éditeur
scientifique. Il apparaît connecté deux fois : une fois à `F30_Manifestation_Creation`, une fois à un événement
`E12_Production` (« Production de l'objet », correspondant à `F32_Item_Production_Event`) — cohérent avec le
double rôle d'éditeur *et* imprimeur. La page `model` (vue d'ensemble) contenait deux tentatives redondantes de
consolidation, l'une explicitement marquée « Responsable scientifique **à supprimer** » et une note « **renommer**
activité scientifique » — signe que l'auteur du diagramme (Mélanie Bouland) avait déjà commencé, sans la
terminer, la même clarification que ce document propose.

**Conclusion : rien ne manquait dans les classes.** `F30_Manifestation_Creation`, `F32_Item_Production_Event`,
`D2_Digitization_Process`, `D7_Digital_Machine_Event`, `E55_Type`, `E52_Time-Span`, `E53_Place` étaient déjà toutes
dans le module. Ce qui manquait : une propriété reliant un acteur (`E39_Actor`) à ces événements, avec un rôle
distinct de la responsabilité d'auteur déjà couverte sur `F27_Work_Creation`/`F28_Expression_Creation`.

## 3. Trois rôles, pas deux

Le diagramme distingue en réalité, une fois reconstitué, trois responsabilités bien différentes autour d'une
Manifestation :

| Rôle | Qui, dans l'exemple du projet | Code MARC (vérifié en direct, 8 juillet 2026) | Niveau |
|---|---|---|---|
| Auteur original | Stendhal | `aut` | `F27_Work_Creation` (déjà couvert, `P14_has_original_author`) |
| Éditeur commercial | Le Divan | `pbl` — *« A person or organization responsible for publishing, releasing, or issuing a resource. »* | `F30_Manifestation_Creation` et `F32_Item_Production_Event` |
| Éditeur scientifique | Henri Martineau | `edt` — *« A person, family, or organization contributing to a resource by revising or elucidating the content, e.g., adding an introduction, notes, or other critical matter. An editor may also prepare a resource for production, publication, or distribution. »* | `F30_Manifestation_Creation` + une `E7_Activity` autonome sur Item/Digital Object |

La définition officielle du code `edt` couvre à la fois la révision du texte et la rédaction d'une préface —
exactement les deux tâches attribuées à Martineau dans la documentation pédagogique du projet (« révision du texte
et la préface ») — ce qui confirme qu'**une seule propriété suffit**, sans distinguer un rôle de « préfacier »
séparé.

Deux nouvelles sous-propriétés de `P14_carried_out_by` ont été déclarées, suivant exactement la même méthode que
les trois déjà existantes (Encoding Rule 4, voir `informe-P14-roles-autorat.md`) :

```xml
<rdf:Description rdf:about="http://www.cidoc-crm.org/cidoc-crm/P14_has_scientific_editor">
  <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
  <rdfs:label xml:lang="en">has scientific editor</rdfs:label>
  <rdfs:label xml:lang="fr">a pour éditeur scientifique</rdfs:label>
  <rdfs:domain rdf:resource="http://www.cidoc-crm.org/cidoc-crm/E7_Activity"/>
  <rdfs:range rdf:resource="http://www.cidoc-crm.org/cidoc-crm/E39_Actor"/>
  <rdfs:subPropertyOf rdf:resource="http://www.cidoc-crm.org/cidoc-crm/P14_carried_out_by"/>
</rdf:Description>

<rdf:Description rdf:about="http://www.cidoc-crm.org/cidoc-crm/P14_has_publisher">
  <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#ObjectProperty"/>
  <rdfs:label xml:lang="en">has publisher</rdfs:label>
  <rdfs:label xml:lang="fr">a pour éditeur commercial</rdfs:label>
  <rdfs:domain rdf:resource="http://www.cidoc-crm.org/cidoc-crm/E7_Activity"/>
  <rdfs:range rdf:resource="http://www.cidoc-crm.org/cidoc-crm/E39_Actor"/>
  <rdfs:subPropertyOf rdf:resource="http://www.cidoc-crm.org/cidoc-crm/P14_carried_out_by"/>
</rdf:Description>
```

## 4. Pourquoi Manifestation réutilise l'événement existant, et pourquoi Item/Digital Object en créent un séparé

Ce n'est pas une incohérence — c'est le reflet direct des scope notes officiels, vérifiés verbatim dans les
fichiers vendorisés :

- **`F30_Manifestation_Creation`** (`imports/vendor/lrmoo-1.1.1.rdf`) : *« This class comprises the activities of
  selecting, arranging and presenting one or more instances of F2 Expression on a carrier or other persistent
  presentation means with the purpose of communicating it to some public. »* — cette définition couvre déjà,
  telle quelle, le travail éditorial que le paper réclame (sélectionner, organiser). Il suffit donc d'ajouter la
  propriété d'acteur sur l'événement déjà présent et déjà bien relié (`R24_created`/`R24i_was_created_through`
  à `F3_Manifestation`) — pas besoin d'un second événement parallèle.
- **`F32_Item_Production_Event`** : *« activities that result in one or more instances of F5 Item coming into
  existence. The production of a series of physical objects (printed books, scores, CDs...) »* — purement
  mécanique (impression, copie). **`D2_Digitization_Process`**/**`D7_Digital_Machine_Event`** (`crmdig-5.0.rdf`) :
  même registre, uniquement technique. Aucune de ces trois classes ne couvre, dans sa propre définition
  officielle, un jugement intellectuel sur le contenu. Y accrocher directement `P14_has_scientific_editor`
  reviendrait à typer l'événement de façon contraire à sa propre définition — précisément le type d'erreur que la
  relecture manuelle de `validation/06-conformance/` existe pour repérer. L'activité scientifique y reste donc une
  `E7_Activity` autonome (non co-typée), reliée à l'objet principal via `P16_used_specific_object` — déjà
  précédenté dans ce projet pour ce même patron « activité → objet qu'elle concerne » (voir
  `problemes-et-solutions.md`).

Cette asymétrie est voulue : elle ne doit pas être « corrigée » plus tard vers une fausse symétrie qui coreproduirait
`P14_has_scientific_editor` directement sur `F32`/`D2`/`D7`.

## 5. Exemple concret (Manifestation, Item et Digital Object)

```turtle
:manifestation_1927  a  lrmoo:F3_Manifestation .

:creation_manifestation_1927  a  lrmoo:F30_Manifestation_Creation ;
    lrmoo:R24_created            :manifestation_1927 ;
    cidoc:P14_has_publisher       :le_divan ;
    cidoc:P14_has_scientific_editor  :henri_martineau ;
    cidoc:P4_has_time-span        :periode_1927 ;
    cidoc:P2_has_type              :type_revision_critique .

:le_divan  a  cidoc:E39_Actor ;
    rdfs:label  "Éditeur et imprimeur Le Divan"@fr .

:henri_martineau  a  cidoc:E21_Person ;
    rdfs:label  "Henri Martineau"@fr .

# Item : responsabilité mécanique (l'impression), séparée de la responsabilité scientifique
:production_exemplaire  a  lrmoo:F32_Item_Production_Event ;
    lrmoo:R28_produced      :exemplaire_bnf ;
    cidoc:P14_has_publisher  :le_divan .

:activite_scientifique_exemplaire  a  cidoc:E7_Activity ;
    cidoc:P16_used_specific_object   :exemplaire_bnf ;
    cidoc:P14_has_scientific_editor  :henri_martineau ;
    cidoc:P2_has_type                 :type_collation_exemplaire .

# Objet numérique : même patron que pour l'Item
:activite_scientifique_numerique  a  cidoc:E7_Activity ;
    cidoc:P16_used_specific_object   :objet_numerique_epub ;
    cidoc:P14_has_scientific_editor  :henri_martineau .
```

## 6. Ce qui reste à faire dans le diagramme (mécanique, pas une nouvelle investigation)

Le détail complet, page par page, est dans le suivi de travail interne du diagramme (hors de ce
dépôt de publication) : étiqueter les flèches déjà dessinées avec les noms ci-dessus, ajouter les
deux satellites manquants sur la page F3, consolider les deux branches redondantes de la page
`model`.

---

## Sources citées

- `Paper_Article_Revue HN_V2.docx.pdf`, extraction complète via `pdftotext`, passages cités intégralement en
  section 1.
- `imports/vendor/lrmoo-1.1.1.rdf` — scope notes de `F30_Manifestation_Creation`, `F32_Item_Production_Event`
  cités verbatim en section 4.
- `imports/vendor/crmdig-5.0.rdf` — scope note de `D2_Digitization_Process` (via `D11_Digital_Measurement_Event`
  ⊂ `D7_Digital_Machine_Event`), cité en section 4.
- `CAO_CRM-final.drawio` — inspection directe de la structure XML (pages `model`, `F3`, `F5`, `D1`,
  `exemple`), section 2.
- Library of Congress, MARC Relator Terms, `https://www.loc.gov/marc/relators/relaterm.html`, récupéré par
  téléchargement direct le 8 juillet 2026 — codes `edt` et `pbl` cités intégralement en section 3.
