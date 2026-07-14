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
# CAO_CRM — paquet de publication

<p align="center">
  <img src="https://img.shields.io/badge/CAO__CRM-Ontology%20v1.0-6f42c1?style=for-the-badge" alt="CAO_CRM — Ontology v1.0" />
  <img src="https://img.shields.io/badge/Domain-CIDOC--CRM%20%C2%B7%20LRMoo%20%C2%B7%20CRMdig-ff6f00?style=flat-square" alt="Domain: CIDOC-CRM, LRMoo, CRMdig" />
  <img src="https://img.shields.io/badge/Docs-FR%20%7C%20ES%20%7C%20EN-0d47a1?style=flat-square" alt="Documentation in French, Spanish and English" />
</p>
<p align="center">
  <a href="https://github.com/andresecha/CAO_CRM/actions/workflows/validate.yml"><img src="https://github.com/andresecha/CAO_CRM/actions/workflows/validate.yml/badge.svg" alt="Validation pipeline status" /></a>
  <a href="https://github.com/andresecha/CAO_CRM/actions/workflows/pages.yml"><img src="https://github.com/andresecha/CAO_CRM/actions/workflows/pages.yml/badge.svg" alt="GitHub Pages deployment status" /></a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.12" />
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-9e9e9e?style=flat-square" alt="License: CC BY-NC-SA 4.0" /></a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Digital_Humanities-yes-2e7d32?style=flat-square" alt="Digital Humanities" />
  <img src="https://img.shields.io/badge/FAIR%20(FOOPS!)-0.79%2F1.0-00796b?style=flat-square" alt="FAIR score: 0.79/1.0" />
  <img src="https://img.shields.io/badge/Validation-8%2F8%20passing-388e3c?style=flat-square" alt="8/8 validation categories passing" />
  <img src="https://img.shields.io/badge/Terms-130%20(bounded%20module)-3f51b5?style=flat-square" alt="130 terms in the bounded module" />
</p>
<p align="center">
  <a href="https://www.cao-crm.eu/"><img src="https://img.shields.io/badge/Site-www.cao--crm.eu-000000?style=flat-square&logo=googlechrome&logoColor=white" alt="Published documentation site" /></a>
  <a href="https://github.com/andresecha/CAO_CRM/issues"><img src="https://img.shields.io/github/issues/andresecha/CAO_CRM?style=flat-square&color=fb8c00" alt="Open issues" /></a>
</p>

**CAO_CRM** (*Corpus Author Ontology CRM*) est le modèle ontologique développé au sein du Consortium HN Ariane pour structurer les métadonnées des corpus littéraires, dans le cadre du projet AMIS. Ce dossier rassemble la version finale (bornée et composée) de l'ontologie, sa documentation pédagogique complète en français, en espagnol et en anglais, ses décisions de conception justifiées, une visualisation interactive du modèle, et l'ensemble des tests de validation préalables à la publication.

Ce document est le point d'entrée. La documentation pédagogique existe **en français, en espagnol et en anglais** (voir section 8) ; les citations littérales des sources officielles (CIDOC-CRM, LRMoo, CRMdig) restent, elles, toujours dans leur langue d'origine (l'anglais), pour ne jamais paraphraser ni déformer un texte de référence.

**Dernière mise à jour de ce document : 14 juillet 2026.**

---

## 1. Ce que contient ce dossier

| Dossier / fichier | Contenu |
|---|---|
| `ontology/CAO_CRM-1.0.rdf` | **Le fichier de l'ontologie — première version publiée.** RDF/XML, 1165 triples, 41 classes, 84 propriétés d'objet, 5 propriétés de données — un sous-ensemble borné et composé de CIDOC-CRM 7.1.3, LRMoo 1.1.1 et CRMdig 5.0. Aucune classe ni propriété propre à CAO_CRM (voir section 3). En-tête multilingue (anglais/français/espagnol) — voir section 9. |
| `graph/CAO_CRM-1.0-graph.html` | **Visualisation interactive du modèle** — un graphe navigable au format HTML autonome (bibliothèque `pyvis`/vis-network), sans serveur de base de données en graphe requis. S'ouvre directement dans un navigateur. |
| `decisions/fr/`, `decisions/es/` | Les **ADR** (*Architecture/modeling Decision Records*) et l'ensemble des rapports techniques — chaque décision de conception non triviale, documentée avec les citations textuelles des sources officielles qui la justifient, les options envisagées, la décision finale, et (depuis le 6 juillet) trois audits indépendants et successifs qui revérifient chaque affirmation contre les fichiers sources. Voir section 7 pour le détail. |
| `documentation/fr/`, `documentation/es/`, `documentation/en/` | Dix sections rédigées pour un public **non expert** en ontologies — de « qu'est-ce que CAO_CRM » jusqu'au glossaire et aux notes d'application des propriétés `P14_has_*`/valeurs `E55_Type`. Réécrites et alignées le 7-8 juillet sur l'état final du modèle (1.0), dans les trois langues. |
| `validation/` | Les huit catégories de tests de validation (syntaxe, cohérence logique, SHACL, qualité, métriques, conformité, métadonnées, FAIR) — chacune avec son propre `README.md`. |
| `imports/` | Scripts pour récupérer les versions officielles exactes de CIDOC-CRM/LRMoo/CRMdig/SKOS, les fusionner avec l'ontologie, et **`module-terms.txt`** — la liste exacte des 130 termes (IRI complètes) qui a servi à extraire ce module avec ROBOT. |
| `docs/site/index-{en,fr,es}.html` | Documentation HTML navigable générée par Widoco, dans les 3 langues — régénérée le 10 juillet avec le RDF final (métadonnées FOOPS/FAIR incluses), fusionnant à la volée la couche de traduction de travail `docs/i18n/CAO_CRM-1.0-i18n.ttl` pour les termes LRMoo/CRMdig et les définitions non traduites officiellement (marqués comme tels, voir section 8), **et avec une introduction complète et à jour propre à chaque langue** (`docs/intro-en.html`, `docs/intro.html`, `docs/intro-es.html` ; auparavant seul le français avait un texte d'introduction réel, et il était encore au brouillon). `docs/site/index.html` est une page d'accueil (ajoutée le 7 juillet) qui renvoie vers les trois langues — nécessaire pour GitHub Pages, voir ci-dessous. |
| `docs/site/CAO_CRM-1.0-{en,fr,es}.pdf` | La même documentation, exportée en PDF (une par langue), générée automatiquement à partir du HTML final par `docs/build.sh` (Chrome/Chromium headless) — liens disponibles directement depuis `docs/site/index.html`. |
| `scripts/` | Installation des outils nécessaires (`install-tools.sh`) et exécution des questions de compétence. |
| `competency-questions/`, `sparql/`, `test-data/` | **Contenu réel** (depuis le 10 juillet) : un graphe d'instance vérifié et non synthétique (`test-data/stendhal-le-rouge-et-le-noir.ttl` — l'édition Martineau/Gallica et la traduction Scott Moncrieff/Internet Archive), 5 questions de compétence formelles et 2 vérifications de cardinalité (`competency-questions/CQ-001-a-005-stendhal.md`), traduites en requêtes SPARQL réelles (`sparql/ask/`, `sparql/select/`) suivant la méthodologie W3C HCLS *Compiling to SPARQL*. Exécutées par `make cq`. |
| `Makefile` | Point d'entrée unique : `make validate` exécute les huit catégories automatisées **plus `cq`** dans l'ordre (voir section 4 pour le détail de chacune). |
| `.github/workflows/validate.yml` | **Pipeline GitHub Actions, validation** : rejoue `make validate` (qui inclut déjà `cq`/`shacl`/`fair`) à chaque push/pull request (voir section 5). |
| `.github/workflows/pages.yml` | **Pipeline GitHub Actions, publication** : publie `docs/site/` tel quel sur **GitHub Pages**, avec le domaine propre `www.cao-crm.eu`, à chaque push sur la branche par défaut (voir section 5). |
| `.gitlab-ci.yml` | Pipeline GitLab CI/CD historique, conservé pour la copie institutionnelle de ce dépôt sur GitLab (voir section 5) — inactif ici, GitHub Actions ne l'exécute pas. |
| `.github/workflows/validate.yml` | Équivalent GitHub Actions du job `validate` ci-dessus — ne s'exécute que si ce dépôt est un jour poussé/miroité vers GitHub ; sans effet sur GitLab. |

### Arborescence complète

Les 174 fichiers suivis par Git, dossier par dossier (les fichiers ignorés — sorties de build regénérables, brouillons de traduction non encore revus — n'apparaissent pas ; voir `.gitignore`). Chaque dossier de premier niveau a son propre `README.md` avec le détail fichier par fichier ; le tableau ci-dessus reste la référence pour le *pourquoi*, cette arborescence pour le *où*.

```
./
├── CNAME
├── competency-questions/
│   ├── CQ-001-a-005-stendhal.md
│   └── README.md
├── decisions/
│   ├── README.md
│   ├── es/
│   │   ├── ADR-001-disjointness.md
│   │   ├── ADR-002-idiomas-LRMoo-CRMdig.md
│   │   ├── ADR-003-autoria-y-procedencia.md
│   │   ├── informe-completitud-labels-domain-range.md
│   │   ├── informe-implementacion-RDF-modulo-acotado.md
│   │   ├── informe-integracion-properties_extracted.md
│   │   └── informe-requisitos-publicacion-CAO_CRM.md
│   └── fr/
│       ├── ADR-001-disjointness.md
│       ├── ADR-002-idiomas-LRMoo-CRMdig.md
│       ├── ADR-003-autoria-y-procedencia.md
│       ├── auditoria-1-rdf.md
│       ├── auditoria-2-documentacion-y-conformidad.md
│       ├── auditoria-3-verificacion-final.md
│       ├── complete-model.md
│       ├── informe-activite-editoriale-scientifique.md
│       ├── informe-completitud-labels-domain-range.md
│       ├── informe-implementacion-RDF-modulo-acotado.md
│       ├── informe-P14-roles-autorat.md
│       └── problemes-et-solutions.md
├── docs/
│   ├── bibliography.html
│   ├── build.sh
│   ├── config-{en,es,fr}.properties
│   ├── i18n/
│   │   ├── CAO_CRM-1.0-i18n.ttl
│   │   ├── glossary_crosswalk.yaml
│   │   ├── README.md
│   │   ├── scripts/
│   │   │   ├── build_review_doc.py
│   │   │   ├── check_consistency.py
│   │   │   ├── compile_i18n_overlay.py
│   │   │   ├── extract_inventory.py
│   │   │   └── prepend_review_frontmatter.py
│   │   ├── term_inventory.json
│   │   └── translations/               (8 lots thématiques .yaml)
│   ├── intro{-en,-es,}.html
│   ├── logos/ARIANE{-dark,}.svg
│   ├── postprocess_*.py                (5 scripts de post-traitement Widoco)
│   ├── README.md
│   └── site/                           (documentation HTML/PDF générée, publiée sur GitHub Pages)
├── documentation/
│   ├── README.md
│   ├── en/  (10 fiches .md)
│   ├── es/  (10 fiches .md)
│   └── fr/  (10 fiches .md)
├── .github/workflows/
│   ├── pages.yml
│   └── validate.yml
├── .gitignore
├── .gitlab-ci.yml
├── graph/
│   ├── build_graph.py
│   ├── CAO_CRM-1.0-graph.html
│   ├── lib/                            (bibliothèques JS vendorisées : vis-network, tom-select)
│   └── README.md
├── imports/
│   ├── fetch.sh
│   ├── merge.sh
│   ├── module-terms.txt
│   └── README.md
├── Makefile
├── ontology/
│   └── CAO_CRM-1.0.{rdf,ttl,nt,jsonld,owx}
├── README.md
├── requirements.txt
├── scripts/
│   ├── check-watermark.sh
│   ├── install-tools.sh
│   ├── reserialize-ontology.py
│   ├── run-competency-questions.sh
│   └── README.md
├── sparql/
│   ├── ask/     (3 requêtes .rq)
│   ├── select/  (4 requêtes .rq)
│   └── README.md
├── test-data/
│   ├── PROVENANCE-stendhal-*.md
│   ├── README.md
│   └── stendhal-le-rouge-et-le-noir.ttl
└── validation/
    └── 01-syntax/ … 08-fair/           (check.sh + README.md par catégorie, plus shapes.ttl et check.sparql où pertinent)
```

---

## 2. Démarrage rapide

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash scripts/install-tools.sh      # télécharge ROBOT et Apache Jena localement, sans sudo
make validate                       # exécute la chaîne de validation fiable
```

Chaque commande peut aussi s'exécuter isolément (`make syntax`, `make reason`, `make metrics`, `make conformance`, `make metadata`, `make quality`, `make shacl`, `make cq`, `make fair`) — voir `validation/<catégorie>/README.md` pour la commande exacte et comment interpréter chaque résultat.

Pour visualiser le graphe interactif : ouvrir directement `graph/CAO_CRM-1.0-graph.html` dans un navigateur (aucune régénération nécessaire, déjà à jour).

---

## 3. Le principe de conception : composition pure, zéro contenu propre

CAO_CRM **ne crée aucune classe ni propriété qui lui soit propre**, à une seule exception méthodologique près, explicitement sanctionnée par CIDOC-CRM lui-même : les 5 sous-propriétés `P14_has_original_author`/`_translator`/`_abridger`/`_scientific_editor`/`_publisher`, déclarées selon la « Encoding Rule 4 » du CIDOC-CRM SIG (voir `decisions/fr/informe-P14-roles-autorat.md` et `informe-activite-editoriale-scientifique.md`). En dehors de ce cas, la contribution de CAO_CRM est purement une **sélection et composition bornée** de fragments de CIDOC-CRM, LRMoo et CRMdig.

Ce principe a été établi après plusieurs itérations où le modèle avait, par erreur, accumulé des propriétés natives et des métadonnées d'en-tête contaminées par d'autres ontologies (voir `decisions/fr/informe-implementacion-RDF-modulo-acotado.md`). La version présente dans ce dossier a été reconstruite en suivant une méthode reproductible et vérifiable, à partir de la liste exacte de termes `imports/module-terms.txt`, avec trois vagues d'ajouts documentées dans `decisions/fr/problemes-et-solutions.md`, `complete-model.md`, et le `dcterms:description` de l'ontologie elle-même.

### Numérotation de version : pourquoi 1.0

CAO_CRM n'avait jamais été publié avant cette version : la numérotation publique commence donc, conformément à la pratique usuelle de versionnage des ontologies (que suivent d'ailleurs CIDOC-CRM, LRMoo et CRMdig eux-mêmes, avec leurs propres numéros 7.1.3/1.1.1/5.0), à **1.0** — quel qu'ait été le nombre d'itérations de travail internes qui l'ont précédée. Ce dépôt ne contient que cette version publiée ; le détail des étapes de travail internes qui y ont conduit est consigné, à titre d'archive de conception, dans `decisions/`.

---

## 4. État de la validation (dernière exécution complète : 10 juillet 2026)

| # | Catégorie | Commande | Résultat |
|---|---|---|---|
| 1 | Syntaxe | `make syntax` | ✅ **PASS** — 0 erreur (rapper + riot + rdflib) |
| 2 | Cohérence logique | `make reason` | ✅ **PASS** — raisonneur HermiT, ontologie cohérente, 0 classe insatisfiable, fusionnée avec les 3 sources officielles complètes + SKOS |
| 3 | SHACL | `make shacl` | ✅ **PASS** — 7 formes réelles, validées contre un graphe d'instance réel et non synthétique (`test-data/stendhal-le-rouge-et-le-noir.ttl`), y compris le cas négatif (une donnée obligatoire retirée déclenche bien une violation) — voir détail ci-dessous |
| 4 | Conformité avec CIDOC-CRM/LRMoo/CRMdig | `make conformance` | ✅ **PASS** (partie automatisée) — aucun axiome des ontologies de base modifié, au-delà d'un artefact de fusion sans importance |
| 5 | Métadonnées de l'en-tête | `make metadata` | ✅ **PASS 7/7** |
| 6 | Qualité (OOPS!) | `make quality` | ✅ **PASS** — 0 critique, 0 important, 2 mineurs (avec 3 pitfalls exclus du filtre, documentés) — voir détail ci-dessous |
| 7 | Métriques structurelles (ROBOT report) | `make metrics` | ✅ **PASS** — profil personnalisé, voir détail ci-dessous |
| 8 | FAIR (FOOPS!) | `make fair` | ✅ **PASS — 0,79/1,0** — exécution locale réelle et reproductible (jar officiel v0.4.0, endpoint `assessOntologyFile`), pas un simple test manuel — voir détail ci-dessous |

**`cq` (questions de compétence, hors des huit catégories numérotées mais exécutée avec la même rigueur) :** les 5 questions de compétence de `competency-questions/CQ-001-a-005-stendhal.md` et les 2 vérifications de cardinalité sont traduites en requêtes SPARQL réelles (`sparql/ask/`, `sparql/select/`) et s'exécutent contre le même graphe d'instance que `shacl` — `make cq` les rejoue toutes.

**`shacl`/`cq` (fermé le 10 juillet) :** la première version du graphe de test était un squelette minimal, sans contenu réel — insuffisant pour vérifier qu'une forme SHACL discrimine vraiment (un graphe trop simple peut passer n'importe quelle forme faute d'avoir quoi que ce soit à violer). Le graphe a été remplacé par un cas réel et vérifié contre les sources primaires (BnF/Gallica pour l'édition Martineau, Internet Archive pour la traduction Scott Moncrieff), et chaque forme a été confirmée par son cas négatif (retirer une donnée obligatoire déclenche bien la violation attendue). Voir `test-data/PROVENANCE-stendhal-verificacion.md` et `test-data/PROVENANCE-stendhal-traduccion-internet-archive.md` pour la trace de vérification complète.

**`fair` (fermé le 10 juillet) :** le script pointait vers un contrat REST du service public jamais vérifié, qui ne fonctionnait pas. Remplacé par une exécution locale réelle (jar officiel de la release v0.4.0, endpoint `assessOntologyFile` documenté) : score reproductible de 0,79/1,0. Voir `validation/08-fair/README.md` pour le détail complet du score par dimension FAIR.

**`metrics` (résolu le 7 juillet) :** le rapport ROBOT signalait 44 occurrences de la règle `duplicate_label` — vérifié directement, caractère par caractère contre les fichiers officiels : ces libellés dupliqués (p. ex. `P106_is_composed_of` / `P46_is_composed_of` partageant le même libellé chinois, ou `R28i_was_produced_by` (LRMoo) partageant "was produced by" avec sa propre superpropriété CIDOC-CRM `P108i_was_produced_by`) **existent déjà tels quels dans les fichiers officiels** — aucun n'est introduit par CAO_CRM. Ce n'est pas une rationalisation propre à ce projet : le **OBO Operations Committee** a soulevé exactement ce type de faux positif auprès des mainteneurs de ROBOT ([ontodev/robot#429](https://github.com/ontodev/robot/issues/429)), signalant que `duplicate_label` "produces false positives when checking imported or cross-ontology content". Le remède standard et documenté par ROBOT lui-même est un profil personnalisé démotant la sévérité de la règle — voir `validation/05-metrics/README.md`, section « Accepted findings », pour le détail complet et les sources.

**`quality` (résolu le 7 juillet) :** OOPS! signalait 1 pitfall « Critical » (`P19`, domaines/portées multiples — chaque occurrence déjà individuellement justifiée dans `decisions/fr/problemes-et-solutions.md` et revérifiée par la chaîne d'audits) et 2 « Important » (`P10`, absence de disjonction ; `P30`, `F2_Expression`/`F3_Manifestation` signalées comme « peut-être équivalentes », faux positif). Vérifié aujourd'hui : **aucun des trois fichiers officiels (CIDOC-CRM/LRMoo/CRMdig) ne déclare la moindre disjonction de classe** — c'est un choix de conception délibéré de cette famille d'ontologies (elle repose sur le co-typage multiple, exactement le patron que CAO_CRM utilise partout : `F5_Item + E22_Human-Made_Object`, etc.), pas un oubli. Inventer une disjonction sans précédent officiel introduirait du contenu propre à CAO_CRM, contraire au principe de la section 3. Ces trois pitfalls sont désormais exclus du filtre `<Pitfalls>` envoyé au service OOPS! (mécanisme officiellement documenté par OOPS! lui-même comme liste d'inclusion, pas un contournement) — voir `validation/04-quality/README.md`, section « Excluded pitfalls », pour la justification complète de chacun.

**Interprétation générale :** l'ontologie est syntaxiquement correcte, logiquement cohérente, conforme aux ontologies qu'elle compose, et sans aucun défaut réel non documenté. Tout ce qui reste signalé par les outils automatiques a été examiné individuellement et a une justification écrite et vérifiable.

---

## 5. Publication automatique (CI/CD et GitHub Pages)

**Ce dépôt GitHub est le dépôt principal du projet**, à la suite d'une migration : le dépôt
GitLab institutionnel du Consortium Huma-Num ARIANE (`gitlab.huma-num.fr/consortiumariane/cao_crm`)
reste la copie de référence institutionnelle, mais l'infrastructure GitLab Pages de Huma-Num ne
permet pas, pour l'instant, de configurer le domaine propre `www.cao-crm.eu` en CNAME. C'est ce
dépôt-ci, avec GitHub Pages, qui publie donc la documentation et l'ontologie sur ce domaine.
`.github/workflows/`, à la racine, définit deux workflows :

1. **`validate.yml`** — rejoue exactement `make validate`, qui inclut déjà les huit catégories automatisées de la section 4 plus `cq` (contre le graphe d'instance réel `test-data/stendhal-le-rouge-et-le-noir.ttl`, pas une plantille vide). Tourne sur chaque push et chaque pull request.
2. **`pages.yml`** — publie **GitHub Pages** : copie `docs/site/` (déjà généré et commité, voir section 1) tel quel dans `public/`, `public/ontology/` et `public/ontology/1.0/` (voir ci-dessous pourquoi ces deux derniers), ainsi que les sérialisations RDF/Turtle/N-Triples/JSON-LD dans `public/ontology/`, plus un fichier `public/CNAME` contenant `www.cao-crm.eu`. Ne tourne que sur la branche par défaut. Ne reconstruit **pas** la documentation via Widoco en CI (pas besoin de JDK dans ce job) — la discipline reste la même qu'aujourd'hui : régénérer localement avec `make docs` et commiter `docs/site/` à jour avant de pousser. **Configuration ponctuelle requise dans l'interface GitHub** (Settings → Pages) : régler "Source" sur "GitHub Actions" pour que ce workflow puisse publier quoi que ce soit.

**Domaine propre :** **www.cao-crm.eu** doit être configuré en CNAME, côté DNS du domaine (chez le
registrar/fournisseur DNS, hors de ce dépôt), vers `andresecha.github.io` — c'est ce que le fichier
`public/CNAME` généré par `pages.yml` indique à GitHub Pages de servir. C'est aussi, depuis le 9
juillet 2026, le namespace propre de l'ontologie (`owl:Ontology` dans `ontology/CAO_CRM-1.0.rdf` :
`https://www.cao-crm.eu/ontology/`, `owl:versionIRI` : `.../ontology/1.0`) — remplaçant l'ancien
namespace `http://www.CAO_CRM.org/ontology/`, qui n'était qu'un nom de domaine jamais réellement
enregistré (voir `validation/08-fair/README.md`). GitHub Pages, comme GitLab Pages, ne fait aucune
négociation de contenu côté serveur (pas de `.htaccess`, uniquement des fichiers statiques) : c'est
pourquoi le job `pages.yml` place une copie complète du site à la fois à la racine, sous
`/ontology/` (le namespace) et sous `/ontology/1.0/` (le `versionIRI`) — la même page d'accueil
statique répond dans les trois cas, avec des liens vers chaque sérialisation, plutôt qu'une vraie
redirection 303 selon l'en-tête `Accept` (voir `decisions/es/informe-requisitos-publicacion-CAO_CRM.md`,
section 1, pour la discussion complète de ce compromis, initialement rédigée pour GitLab Pages mais
qui s'applique identiquement ici).

**Page d'accueil de la doc publiée :** l'URL racine de Pages sert `public/index.html` — une petite page de choix de langue (régénérée automatiquement par `docs/build.sh` à chaque `make docs`, jamais éditée à la main) qui renvoie vers `index-fr.html`, `index-en.html` et `index-es.html`.

**Le pipeline GitLab CI/CD historique** (`.gitlab-ci.yml`, conservé dans ce dépôt) continue de
s'exécuter sur la copie institutionnelle GitLab, mais son job `pages` n'y publie plus rien d'utile
pour le domaine propre — GitHub Actions et GitHub Pages, ici, ont pris ce rôle.

---

## 6. Ce qu'il reste à faire avant une publication définitive

1. **Le diagramme de travail (Drawio) qui a servi de base conceptuelle au modèle** reste partiellement corrigé — un travail interne de maintenance sur cet artefact de conception, sans rapport avec la validité du fichier RDF publié ici, qui a déjà intégré et vérifié indépendamment tout ce qui devait l'être. Le travail restant est mécanique (appliquer des règles déjà établies), pas une nouvelle investigation.

~~Questions de compétence réelles~~ — **résolu le 10 juillet 2026** : `test-data/stendhal-le-rouge-et-le-noir.ttl` (graphe réel et vérifié, pas synthétique), 5 questions de compétence + 2 vérifications de cardinalité, traduites en requêtes SPARQL réelles suivant la méthodologie W3C HCLS — voir section 4.

~~Confirmer le contrat REST exact du service FOOPS!~~ — **résolu le 10 juillet 2026** : exécution locale réelle du jar officiel (v0.4.0), endpoint `assessOntologyFile` confirmé et scripté dans `validation/08-fair/check.sh` — score reproductible 0,79/1,0, voir section 4.

~~Rôles d'autorité non couverts par les sous-propriétés `P14_*`~~ — **résolu le 8 juillet 2026** : ajout de `P14_has_scientific_editor` et `P14_has_publisher`, fermant en même temps un manque structurel plus large explicitement signalé par le paper lui-même comme différenciateur original du modèle (voir `decisions/fr/informe-activite-editoriale-scientifique.md`).

Le seul point encore ouvert (le diagramme Drawio) ne remet pas en cause la validité de l'ontologie RDF elle-même — c'est un artefact de conception complémentaire.

### Corrections apportées le 10 juillet 2026

Une relecture d'ensemble a confirmé que le code et la documentation reflètent bien l'état réel du
dépôt ; les écarts suivants, trouvés pendant cette relecture, ont été corrigés :

- **`.gitlab-ci.yml` / `.github/workflows/validate.yml`** rejouaient `cq`/`shacl`/`fair` comme des
  étapes séparées, en plus de `make validate` — redondant depuis que le Makefile les inclut déjà ;
  simplifié à un seul appel à `make validate`, et les commentaires obsolètes (« service FOOPS!
  injoignable », « no-op tant qu'il n'y a pas de test-data réel ») ont été retirés.
- **`test-data/README.md` et `competency-questions/README.md`** annonçaient encore « pendiente » /
  « aucun contenu réel » alors que le graphe d'instance Stendhal et les questions de compétence
  existent depuis le 10 juillet — réécrits pour décrire le contenu réel.
- **Les fichiers de provenance de `test-data/`** (`PROVENANCE-stendhal-*.md`) pointaient vers
  `Validation/research/...`, un chemin du répertoire de travail privé, absent de ce dépôt publié —
  copiés dans `test-data/` lui-même et les références corrigées en conséquence.
- **La numérotation des ADR** commençait à `ADR-002` (le premier, sur le typage de `P3_has_note`,
  ayant été replacé dans le catalogue général de problèmes — voir section 7) : renumérotés
  `ADR-001`/`ADR-002`/`ADR-003`, fichiers et toutes les références croisées mis à jour.
- **La section 7 ci-dessous** décrivait les ADR actuels comme un « historique de décisions
  antérieures... conservées pour la traçabilité », alors que ce sont les décisions actives du
  modèle publié — reformulée.
- **Les triples/score obsolètes** (1153 au lieu de 1165 ; FAIR « partiel » au lieu de 0,79/1,0 réel)
  ont été mis à jour dans tout ce document.

---

## 7. Historique des décisions et audits (français, `decisions/fr/`)

Le cœur documentaire du projet. Chaque fichier peut être lu isolément ; ensemble, ils couvrent l'intégralité du raisonnement derrière chaque choix de modélisation.

| Fichier | Contenu |
|---|---|
| `problemes-et-solutions.md` | Document central — les 8 problèmes de modélisation identifiés (Description/`E62_String`, Système d'écriture, langue, localisation de `F5_Item`, droits, production d'exemplaire, objet numérique natif vs numérisé, dimension, précision XSD), chacun avec citation officielle complète, explication pédagogique, et la distinction explicite entre changement de diagramme et changement de RDF. |
| `complete-model.md` | Vérification exhaustive de la matrice 5 classes × 4 catégories (Caractéristiques/Processus/Statut/Relation) du paper — les manques réels identifiés et résolus (droits de `F1_Work`, relations Expression↔Expression et Work↔Work, placement du Système d'écriture), avec la recherche corroborative indépendante et les sources consolidées dans le même document. |
| `informe-P14-roles-autorat.md` | Justification complète (Encoding Rule 4, MARC Relator Terms, alternatives étudiées) de la décision d'ajouter les sous-propriétés de rôle d'auteur (auteur original, traducteur, abréviateur). |
| `informe-activite-editoriale-scientifique.md` | La branche « activités éditoriales » signalée par le paper comme différenciateur original de CAO_CRM (Manifestation, Item, Objet numérique) — distinction entre éditeur commercial (`P14_has_publisher`) et éditeur scientifique (`P14_has_scientific_editor`), avec citation intégrale du paper et justification de l'asymétrie entre niveaux. |
| `auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md` | Chaîne de 3 audits indépendants et successifs (6-7 juillet) — RDF terme par terme, puis documentation et conformité conceptuelle, puis vérification croisée finale. Verdict final : 0 défaut critique restant. |
| `ADR-001-disjointness.md` | Pourquoi CAO_CRM ne déclare aucune condition `owl:disjointWith` — suit le même choix délibéré que CIDOC-CRM/LRMoo/CRMdig eux-mêmes. |
| `ADR-002-idiomas-LRMoo-CRMdig.md` | Pourquoi les termes de LRMoo/CRMdig qui n'existent qu'en anglais dans les sources officielles ne sont pas traduits dans le RDF canonique (la traduction de travail vit séparément, voir section 8 et le dataset i18n). |
| `ADR-003-autoria-y-procedencia.md` | Attribution de l'auteur du modèle conceptuel (Mélanie Bouland), de l'implémentation RDF/OWL (Andrés Echavarría) et des outils cités dans l'en-tête — voir aussi section 9. |
| `informe-completitud-labels-domain-range.md`, `informe-implementacion-RDF-modulo-acotado.md` | Rapports techniques d'implémentation et d'intégration du diagramme source — voir section 3. |

Le cas du typage de `P3_has_note` (initialement documenté comme un quatrième ADR séparé) est
aujourd'hui traité dans `problemes-et-solutions.md` (Problème 1) : ce cas précis n'a jamais été
validé collectivement par l'équipe, contrairement aux trois ADR ci-dessus, et vit donc dans le
catalogue général de problèmes plutôt que sous le label ADR, qui implique une décision d'équipe
actée.

`decisions/es/` contient la version espagnole des trois ADR et de certains rapports techniques ;
les documents les plus récents (audits, `problemes-et-solutions.md`, `complete-model.md`) n'ont
pour l'instant que leur version française.

Un rapport de comparaison complète, triple par triple, entre le fichier original de Mélanie Bouland et l'état actuel du modèle a également été produit à des fins de contrôle qualité interne ; il documente l'évolution complète du modèle mais ne fait pas partie de ce dépôt de publication.

---

## 8. Documentation pédagogique (français, espagnol et anglais)

Chaque document existe dans les trois langues, avec exactement le même contenu — `documentation/fr/<fichier>`, `documentation/es/<fichier>` et `documentation/en/<fichier>` :

| Fichier | Contenu |
|---|---|
| `01-que-es-cao-crm.md` | Qu'est-ce que CAO_CRM et à quoi ça sert |
| `02-cidoc-lrmoo-crmdig.md` | Que sont CIDOC-CRM, LRMoo et CRMdig, et pourquoi les combiner |
| `03-jerarquia-ejemplo.md` | La hiérarchie F1→F2→F3→F5→D1, illustrée par un exemple concret |
| `04-construccion-rdf.md` | Comment le fichier RDF a été construit, étape par étape |
| `05-decisiones-adr.md` | Les décisions de modélisation expliquées en langage simple (ADR-001 à 003 et cas connexes) |
| `06-pruebas-validacion.md` | Ce que vérifie chaque catégorie de test de validation |
| `07-guia-protege.md` | Guide pratique pour ouvrir et explorer le modèle dans Protégé |
| `08-glosario.md` | Glossaire des termes techniques |
| `09-faq-errores.md` | Questions fréquentes et incidents réels rencontrés pendant la construction |
| `10-notas-de-aplicacion.md` | Notes d'application (au sens CIDOC-CRM) des 5 propriétés de rôle `P14_has_*` et des valeurs contrôlées `E55_Type` utilisées dans le modèle, chacune avec un exemple concret. |

Pour explorer le modèle soi-même : ouvrir `ontology/CAO_CRM-1.0.rdf` dans Protégé, ou naviguer `graph/CAO_CRM-1.0-graph.html` dans un navigateur.

---

## 9. Auteur, provenance et outils utilisés

Le **modèle conceptuel** (quelles classes et propriétés composer, comment elles se relient) a été discuté et schématisé par **Mélanie Bouland**, au sein du Consortium HN Ariane. Le **codage RDF/OWL de ce fichier précis** est une implémentation nouvelle et indépendante, réalisée par **Andrés Echavarría** (2026). L'équipe **AMIS** (Consortium HN Ariane) assure aujourd'hui la maintenance de ce codage.

Cette distinction, ainsi que les outils cités ci-dessous, figurent aussi directement dans l'en-tête de `ontology/CAO_CRM-1.0.rdf` (propriétés `dc:creator`, `dc:contributor`, `dc:description`, `dcterms:references`), en anglais, en français et en espagnol. Détail complet dans `decisions/fr/ADR-003-autoria-y-procedencia.md`.

**Outils et techniques employés pour la construction et la validation :**
- [ROBOT](http://robot.obolibrary.org/) — extraction du module borné (`robot extract --method subset`), raisonnement, rapports de métriques et de conformité.
- [HermiT](http://www.hermit-reasoner.com/) — raisonneur OWL DL pour la vérification de la cohérence logique.
- [Protégé](https://protege.stanford.edu/) — validation visuelle du fichier final.
- [Apache Jena](https://jena.apache.org/) (`riot`) — fusion et validation syntaxique des graphes RDF.
- [OOPS!](https://oops.linkeddata.es/) — détection de pièges de modélisation.
- [Widoco](https://github.com/dgarijo/Widoco) — génération de la documentation HTML navigable (`docs/site/`).
- [pyvis](https://pyvis.readthedocs.io/) / [rdflib](https://rdflib.readthedocs.io/) — génération du graphe interactif (`graph/`).
- Chrome/Chromium (mode headless) — export de la documentation HTML en PDF (`docs/site/*.pdf`).

---

## 10. Comment citer ce dépôt

Deux citations distinctes, selon ce qui est réutilisé — le modèle lui-même, ou les données de recherche qui documentent sa construction.

**Le modèle (ce dépôt — `ontology/CAO_CRM-1.0.rdf`, identique à `dcterms:bibliographicCitation` dans l'en-tête du fichier, voir section 9) :**

- **fr :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM (Corpus Author Ontology CRM)*, version 1.0. Consortium Huma-Num ARIANE. <https://www.cao-crm.eu/ontology/1.0>
- **es :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM (Corpus Author Ontology CRM)*, versión 1.0. Consorcio Huma-Num ARIANE. <https://www.cao-crm.eu/ontology/1.0>
- **en :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM (Corpus Author Ontology CRM)*, version 1.0. Consortium Huma-Num ARIANE. <https://www.cao-crm.eu/ontology/1.0>

**Les données de recherche** (diagramme conceptuel, décisions de modélisation, documentation pédagogique, couche de traduction de travail — voir la collection Nakala séparée, `data-publication/`, hors de ce dépôt de code) :

- **fr :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM — données de recherche* [Collection]. Nakala. [DOI en attente — collection non encore publiée]
- **es :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM — datos de investigación* [Colección]. Nakala. [DOI pendiente — colección aún no publicada]
- **en :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM — research data* [Collection]. Nakala. [DOI pending — collection not yet published]

Chacun des huit "data" qui composent cette collection (voir `data-publication/COLLECTION-METADATA-nakala.md`) a en plus sa propre citation suggérée, avec sa propre autorité, dans son `METADATA-nakala.md` respectif — utile pour citer, par exemple, uniquement la couche de traduction espagnole sans citer l'ensemble de la collection.
