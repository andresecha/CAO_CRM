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
# Glossaire des termes techniques utilisés dans ce projet


Cette section rassemble, par ordre alphabétique, les termes techniques qui reviennent sans cesse dans
la documentation de CAO_CRM et dans le dépôt de validation. Il n'est pas nécessaire de la lire d'un
bout à l'autre : elle sert de référence rapide, pour le cas où un terme apparaîtrait, sur une autre
page, sans explication préalable.

- **Classe (`owl:Class`).** Une catégorie de choses, non une chose concrète. Dans CAO_CRM, `E21_Person`
  est la classe « toutes les personnes » et `F1_Work` est la classe « toutes les œuvres ». Une classe,
  à elle seule, ne comporte aucune donnée particulière (ni nom ni date) ; elle ne fait que définir un
  type. Voir aussi **instance** et **sous-classe**.

- **Cohérence logique.** Une ontologie est *cohérente* lorsqu'elle ne contient aucune contradiction
  interne qui la rendrait impossible à satisfaire. Un cas réel tiré de `validation/02-reasoning/`
  illustre le problème : le **raisonneur** a détecté que, en raison d'équivalences mal déclarées, la
  une propriété héritait d'une valeur textuelle alors que sa **portée** exigeait une URI, ce
  qui est impossible à satisfaire. Cette seule contradiction a suffi à faire considérer toute
  l'ontologie comme incohérente, car d'une contradiction on peut « déduire » n'importe quoi.

- **Disjonction (`owl:disjointWith`).** Une déclaration qui affirme que « ces deux classes ne peuvent
  jamais avoir d'instance en commun » (par exemple, si `E67_Birth`/naissance et `E69_Death`/mort
  étaient déclarées disjointes, cela empêcherait d'enregistrer un même événement comme relevant des
  deux à la fois). Le fichier `ADR-001-disjointness.md` de ce dépôt explique que CAO_CRM a décidé de
  n'ajouter aucune disjonction, suivant le même choix délibéré que CIDOC-CRM lui-même, qui préfère
  laisser cette restriction à l'appréciation de chaque projet.

- **Domaine (`rdfs:domain`) et portée (`rdfs:range`).** Lorsqu'une **propriété** relie une chose A à
  une chose B, le domaine indique de quel type de chose A peut être et la portée, de quel type de chose
  B peut être. Par exemple, `P3_has_note` (« a pour note ») a pour domaine `E1 CRM Entity` (toute
  entité) et, dans la version actuelle du modèle, pour portée `rdfs:Literal` (tout littéral simple). Une nuance essentielle, expliquée dans
  `decisions/fr/problemes-et-solutions.md` (Problème 1) : en OWL, il ne s'agit pas d'une validation qui rejette les
  données erronées (c'est le rôle de SHACL), mais d'une règle à partir de laquelle le système *déduit*
  automatiquement certaines informations.

- **Espace de noms (namespace) / IRI.** Un préfixe partagé qui évite que deux projets n'utilisent
  accidentellement le même nom pour désigner des choses différentes. Il se met en œuvre au moyen d'un
  **IRI** (une variante de l'URI/URL qui admet n'importe quelle langue), de sorte que chaque classe et
  chaque propriété possède une adresse unique, telle que
  `http://www.cidoc-crm.org/cidoc-crm/P3_has_note`. Lorsque CAO_CRM réutilise `P3_has_note`, il ne se
  contente pas de reprendre un nom : il réutilise cet identifiant exact, ce qui permet à n'importe quel
  programme de savoir sans ambiguïté de quelle propriété il s'agit.

- **Étiquette multilingue (`rdfs:label`).** Le nom « lisible par un être humain » d'une classe ou d'une
  propriété dans une langue donnée, marqué par une balise de langue (`@en`, `@fr`...) ; l'identifiant
  technique (l'IRI) ne change pas selon la langue, seule sa présentation change. Le fichier
  `ADR-002-idiomas-LRMoo-CRMdig.md` indique qu'un ensemble de termes de LRMoo/CRMdig ne possèdent d'étiquette
  officielle qu'en anglais, et que l'équipe a décidé de ne pas inventer de traductions propres, afin de
  ne pas attribuer à ces consortiums un contenu qu'ils n'ont pas publié.

- **Importer (`owl:imports`) vs. fusionner (merge).** `owl:imports` est une déclaration formelle qui
  indique à tout outil « charge aussi cet autre fichier pour bien raisonner sur celui-ci ». Le fichier
  `CAO_CRM-1.0.rdf` ne déclare aucun `owl:imports` : de CIDOC-CRM/LRMoo/CRMdig comme de SKOS, il recopie une
  version tronquée directement dans son propre fichier, sans `owl:imports` formel (voir
  `imports/README.md`). C'est pourquoi il existe une étape distincte de **fusion** : `imports/merge.sh`
  réunit CAO_CRM et les fichiers officiels complets dans `merged.ttl`, car la copie tronquée n'apporte
  pas toute l'axiomatique de ces ontologies.

- **Instance / individu.** Un exemple concret d'une classe, doté de données qui lui sont propres. Si
  `E21_Person` est la classe « toutes les personnes », une instance de cette classe serait la personne
  réelle « Stendhal ». En OWL, « instance » et « individu » sont synonymes.

- **Littéral (`rdfs:Literal`) vs. type XSD.** Un littéral est toute valeur simple (texte, nombre, date)
  dépourvue d'identité propre. `rdfs:Literal` est la catégorie la plus large possible de littéraux ;
  les types **XSD** (issus de la norme XML Schema), comme `xsd:string` ou `xsd:decimal`, en sont des
  sous-catégories plus strictes. `decisions/fr/problemes-et-solutions.md` (Problème 1) explique pourquoi CAO_CRM a choisi `rdfs:Literal` pour
  `P3_has_note` : c'est la même convention qu'emploie le fichier officiel de CIDOC-CRM pour des
  propriétés équivalentes comme `P90_has_value`, alors même que celle-ci représente conceptuellement
  « un nombre ».

- **Note de portée (scope note).** Le paragraphe officiel qui définit une classe ou une propriété,
  rédigé par le consortium concerné, expliquant ce qu'elle signifie et ce qu'elle ne couvre pas. Par
  exemple, la *scope note* de `E59 Primitive Value` dans CIDOC-CRM affirme, citation textuelle :
  *"the instances of E59 Primitive Value and its subclasses are not considered elements of the
  universe of discourse the CIDOC CRM aims to define and analyse"* (les instances de E59 Primitive
  Value et de ses sous-classes ne sont pas considérées comme des éléments de l'univers du discours que
  le CIDOC CRM vise à définir et à analyser) : des valeurs telles que des nombres ou des textes ne sont
  pas traitées comme des « choses » du monde décrit, mais comme la manière technique de représenter une
  donnée simple. C'est la source que l'on cite textuellement lorsqu'un doute surgit sur la façon de
  traiter un élément réutilisé, comme le montrent les ADR de ce dépôt.

- **Ontologie.** Un schéma formel qui définit quels « types de choses » existent dans un domaine de
  connaissance (œuvre, édition, exemplaire physique, fichier numérique, personne, événement de
  création...) et comment ils se relient entre eux, de manière à ce qu'une personne comme un programme
  puissent l'interpréter sans ambiguïté. CAO_CRM est l'ontologie de ce dépôt : elle n'invente ni
  classes ni propriétés qui lui seraient propres, mais sélectionne et assemble des éléments de
  CIDOC-CRM, de LRMoo et de CRMdig.

- **Propriété de données (`owl:DatatypeProperty`).** Un type de **propriété** qui relie une
  **instance** à un **littéral** (texte, nombre, date), et non à une autre instance. Par exemple,
  « cette œuvre `a pour titre` "Le Rouge et le Noir" » : le titre n'est que du texte. `P3_has_note` en
  est un autre exemple : elle relie n'importe quelle entité à une note en texte libre.

- **Propriété d'objet (`owl:ObjectProperty`).** Un type de **propriété** qui relie une **instance** à
  **une autre instance**, c'est-à-dire deux entités dotées chacune de leur propre identité. Par
  exemple, « cette œuvre `a été créée par` cette personne » : les deux sont des entités, à la
  différence d'un littéral.

- **Raisonneur (reasoner).** Un programme qui applique les règles logiques d'OWL à une ontologie afin
  de vérifier qu'elle a un sens mathématiquement, de déduire des informations implicites et de détecter
  des contradictions. Dans ce dépôt, le raisonneur employé est HermiT, invoqué via ROBOT (voir
  `validation/02-reasoning/README.md`) ; son résultat principal indique si l'ontologie est **cohérente**
  et si elle comporte une classe insatisfaisable (une classe qui ne pourrait jamais avoir la moindre
  instance possible).

- **RDF/XML vs. Turtle (formats de sérialisation).** Un même ensemble de données en RDF peut s'écrire
  dans différents formats de texte, ou *sérialisations*, sans que son sens en soit modifié. RDF/XML est
  le format fondé sur des balises XML — celui qu'utilise `CAO_CRM-1.0.rdf` — et tend à être plus
  verbeux. Turtle (extension `.ttl`) est plus compact et plus lisible ; il est employé, par exemple,
  dans `imports/module/`. Convertir l'un vers l'autre ne modifie aucune classe ni aucune relation, seule
  change la manière dont le contenu est écrit.

- **SHACL.** Un langage (Shapes Constraint Language) permettant de définir des règles de validation qui,
  elles, rejettent effectivement les données qui ne les respectent pas, à la différence du domaine et
  de la portée en OWL. Par exemple, une règle pourrait exiger que toute instance de `E12_Production`
  possède exactement une date associée. Dans ce dépôt, `validation/03-shacl/` applique ces règles (au
  moyen de pySHACL) sur `test-data/`, en tant que couche complémentaire à la vérification de
  **cohérence logique** effectuée par le raisonneur.

- **SPARQL.** Le langage de requête permettant d'interroger des données en RDF, jouant un rôle
  équivalent à celui de SQL pour les bases de données relationnelles. Il est utilisé ici sous deux
  formes, alignées sur les **questions de compétence** (les cas d'usage auxquels l'ontologie doit
  pouvoir répondre) : les requêtes `ASK` (oui/non, dans `sparql/ask/`) et `SELECT` (listes de
  résultats, dans `sparql/select/`).

- **Sous-classe (`rdfs:subClassOf`).** Une relation entre deux classes qui signifie que « tout ce qui
  appartient à cette classe appartient aussi, automatiquement, à cette autre classe plus générale ». Si
  `E21_Person` était déclarée sous-classe de `E39_Actor`, le raisonneur en déduirait que toute personne
  est également un `E39_Actor`, sans qu'il soit nécessaire de le déclarer séparément pour chaque
  individu.

D'autres notions mentionnées dans cette documentation — comme le projet AMIS, l'outil ROBOT ou les
ADR (comptes rendus de décision) eux-mêmes — sont expliquées dans leur contexte, dans les sections
correspondantes de ce dossier ; elles ne sont pas reprises ici, car il ne s'agit pas de termes
techniques propres à OWL/RDF.
