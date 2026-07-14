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
  <a href="https://nakala.fr/10.34847/nkl.ae3bv5ji"><img src="https://img.shields.io/badge/CAO__CRM-Ontology%20v1.0-D5008F?style=plastic" alt="CAO_CRM — Ontology v1.0 (Nakala)" /></a>
  <a href="https://doi.org/10.34847/NKL.AE3BV5JI"><img src="https://img.shields.io/badge/DOI-10.34847%2FNKL.AE3BV5JI-007ec6?style=plastic" alt="DOI: 10.34847/NKL.AE3BV5JI" /></a>
</p>
<p align="center">
  <a href="http://www.cidoc-crm.org/cidoc-crm/"><img src="https://img.shields.io/badge/CIDOC--CRM-7.1.3-1a237e?style=plastic" alt="CIDOC-CRM 7.1.3" /></a>
  <a href="https://cidoc-crm.org/lrmoo/fm_releases"><img src="https://img.shields.io/badge/LRMoo-1.1.1-1b5e20?style=plastic" alt="LRMoo 1.1.1" /></a>
  <a href="http://www.cidoc-crm.org/extensions/crmdig/"><img src="https://img.shields.io/badge/CRMdig-5.0-ff69b4?style=plastic" alt="CRMdig 5.0" /></a>
</p>
<p align="center">
  <a href="https://www.cao-crm.eu/index-fr.html"><img src="https://img.shields.io/badge/Docs-FR-6a1b9a?style=plastic" alt="Documentation en français" /></a>
  <a href="https://www.cao-crm.eu/index-es.html"><img src="https://img.shields.io/badge/Docs-ES-ef6c00?style=plastic" alt="Documentación en español" /></a>
  <a href="https://www.cao-crm.eu/index-en.html"><img src="https://img.shields.io/badge/Docs-EN-00897b?style=plastic" alt="Documentation in English" /></a>
</p>
<p align="center">
  <a href="https://github.com/andresecha/CAO_CRM/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/andresecha/CAO_CRM/validate.yml?style=plastic&label=validation%20pipeline" alt="Validation pipeline status" /></a>
  <a href="https://github.com/andresecha/CAO_CRM/actions/workflows/pages.yml"><img src="https://img.shields.io/github/actions/workflow/status/andresecha/CAO_CRM/pages.yml?style=plastic&label=pages%20deploy" alt="GitHub Pages deployment status" /></a>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=plastic&logo=python&logoColor=white" alt="Python 3.12" />
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/"><img src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-9e9e9e?style=plastic" alt="License: CC BY-NC-SA 4.0" /></a>
</p>
<p align="center">
  <a href="https://cst-ariane.huma-num.fr/"><img src="https://img.shields.io/badge/Digital_Humanities-ARIANE-d32f2f?style=plastic" alt="Digital Humanities — Consortium ARIANE" /></a>
  <img src="https://img.shields.io/badge/FAIR%20(FOOPS!)-0.80%2F1.0-00796b?style=plastic" alt="FAIR score: 0.80/1.0" />
  <img src="https://img.shields.io/badge/Validation-8%2F8%20passing-388e3c?style=plastic" alt="8/8 validation categories passing" />
  <img src="https://img.shields.io/badge/Terms-130%20(bounded%20module)-3f51b5?style=plastic" alt="130 terms in the bounded module" />
</p>
<p align="center">
  <a href="https://www.cao-crm.eu/"><img src="https://img.shields.io/badge/Site-www.cao--crm.eu-000000?style=plastic&logo=googlechrome&logoColor=white" alt="Published documentation site" /></a>
  <a href="https://github.com/andresecha/CAO_CRM/issues"><img src="https://img.shields.io/github/issues/andresecha/CAO_CRM?style=plastic&color=fb8c00" alt="Open issues" /></a>
</p>

**CAO_CRM** (*Corpus Author Ontology CRM*) est le modèle ontologique développé au sein du Consortium HN Ariane pour structurer les métadonnées des corpus littéraires, dans le cadre du projet AMIS. Ce dépôt rassemble la version publiée (bornée et composée) de l'ontologie, sa documentation pédagogique complète en français, en espagnol et en anglais, ses décisions de conception justifiées, une visualisation interactive du modèle, et l'ensemble des tests de validation.

Ce document est le point d'entrée. La documentation pédagogique existe **en français, en espagnol et en anglais** (voir section 7) ; les citations littérales des sources officielles (CIDOC-CRM, LRMoo, CRMdig) restent, elles, toujours dans leur langue d'origine (l'anglais), pour ne jamais paraphraser ni déformer un texte de référence.

**Dernière mise à jour de ce document : 14 juillet 2026.**

---

## 1. Ce que contient ce dépôt

| Dossier / fichier | Contenu |
|---|---|
| `ontology/CAO_CRM-1.0.rdf` | **Le fichier de l'ontologie.** RDF/XML, 1165 triples, 41 classes, 84 propriétés d'objet, 5 propriétés de données — un sous-ensemble borné et composé de CIDOC-CRM 7.1.3, LRMoo 1.1.1 et CRMdig 5.0. Aucune classe ni propriété propre à CAO_CRM (voir section 3). En-tête multilingue (anglais/français/espagnol) — voir section 8. Sérialisations dérivées équivalentes dans le même dossier : `.ttl`, `.nt`, `.jsonld`, `.owx`. |
| `graph/CAO_CRM-1.0-graph.html` | **Visualisation interactive du modèle** — un graphe navigable au format HTML autonome (bibliothèque `pyvis`/vis-network), sans serveur de base de données en graphe requis. S'ouvre directement dans un navigateur. |
| `decisions/fr/`, `decisions/es/` | Les **ADR** (*Architecture/modeling Decision Records*) et l'ensemble des rapports techniques — chaque décision de conception non triviale, documentée avec les citations textuelles des sources officielles qui la justifient, les options envisagées et la décision finale, plus trois audits successifs qui revérifient chaque affirmation contre les fichiers sources. Voir section 6 pour le détail. |
| `documentation/fr/`, `documentation/es/`, `documentation/en/` | Dix sections rédigées pour un public **non expert** en ontologies — de « qu'est-ce que CAO_CRM » jusqu'au glossaire et aux notes d'application des propriétés `P14_has_*`/valeurs `E55_Type` — alignées sur l'état publié du modèle (1.0), dans les trois langues. |
| `validation/` | Les huit catégories de tests de validation (syntaxe, cohérence logique, SHACL, qualité, métriques, conformité, métadonnées, FAIR) — chacune avec son propre `README.md`. |
| `imports/` | Scripts pour récupérer les versions officielles exactes de CIDOC-CRM/LRMoo/CRMdig/SKOS (`fetch.sh`, avec sommes de contrôle dans `vendor/CHECKSUMS.txt`), les fusionner avec l'ontologie (`merge.sh`), et **`module-terms.txt`** — la liste exacte des 130 termes (IRI complètes) qui a servi à extraire ce module avec ROBOT. |
| `docs/site/index-{en,fr,es}.html` | Documentation HTML navigable générée par Widoco, dans les trois langues, à partir du RDF canonique — en fusionnant à la volée la couche de traduction de travail `docs/i18n/CAO_CRM-1.0-i18n.ttl` pour les termes LRMoo/CRMdig et les définitions sans traduction officielle (marqués comme tels dans le HTML, voir section 7), et avec une introduction propre à chaque langue (`docs/intro-en.html`, `docs/intro.html`, `docs/intro-es.html`). `docs/site/index.html` est la page d'accueil de choix de langue servie par GitHub Pages. |
| `docs/site/CAO_CRM-1.0-{en,fr,es}.pdf` | La même documentation, exportée en PDF (une par langue), générée automatiquement à partir du HTML final par `docs/build.sh` (Chrome/Chromium headless) — liens disponibles directement depuis `docs/site/index.html`. |
| `scripts/` | Scripts transversaux du dépôt : installation des outils (`install-tools.sh`), exécution des questions de compétence, vérification des en-têtes de licence, resérialisation de l'ontologie. |
| `competency-questions/`, `sparql/`, `test-data/` | Le banc d'essai sur données réelles : un graphe d'instance vérifié et non synthétique (`test-data/stendhal-le-rouge-et-le-noir.ttl` — l'édition Martineau/Gallica et la traduction Scott Moncrieff/Internet Archive), 5 questions de compétence formelles et 2 vérifications de cardinalité (`competency-questions/CQ-001-a-005-stendhal.md`), traduites en requêtes SPARQL (`sparql/ask/`, `sparql/select/`) suivant la méthodologie W3C HCLS *Compiling to SPARQL*. Exécutées par `make cq`. |
| `Makefile` | Point d'entrée unique : `make validate` exécute les huit catégories automatisées **plus `cq`** dans l'ordre (voir section 4 pour le détail de chacune). |
| `.github/workflows/validate.yml` | **Pipeline GitHub Actions, validation** : rejoue `make validate` (qui inclut `cq`/`shacl`/`fair`) à chaque push/pull request (voir section 5). |
| `.github/workflows/pages.yml` | **Pipeline GitHub Actions, publication** : publie `docs/site/` sur **GitHub Pages**, avec le domaine propre `www.cao-crm.eu`, à chaque push sur la branche par défaut (voir section 5). |
| `.gitlab-ci.yml` | Pipeline CI/CD de la copie institutionnelle de ce dépôt sur le GitLab Huma-Num (voir section 5) — sans effet ici, GitHub Actions ne l'exécute pas. |

### Arborescence complète

Les 177 fichiers suivis par Git, dossier par dossier (les fichiers ignorés — sorties de build regénérables — n'apparaissent pas ; voir `.gitignore`). Chaque dossier de premier niveau a son propre `README.md` avec le détail fichier par fichier ; le tableau ci-dessus reste la référence pour le *pourquoi*, cette arborescence pour le *où*.

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
make validate                       # exécute la chaîne de validation complète
```

Chaque commande peut aussi s'exécuter isolément (`make syntax`, `make reason`, `make metrics`, `make conformance`, `make metadata`, `make quality`, `make shacl`, `make cq`, `make fair`) — voir `validation/<catégorie>/README.md` pour la commande exacte et comment interpréter chaque résultat.

Pour visualiser le graphe interactif : ouvrir directement `graph/CAO_CRM-1.0-graph.html` dans un navigateur (aucune régénération nécessaire, déjà à jour).

---

## 3. Le principe de conception : composition pure, zéro contenu propre

CAO_CRM **ne crée aucune classe ni propriété qui lui soit propre**, à une seule exception méthodologique près, explicitement sanctionnée par CIDOC-CRM lui-même : les 5 sous-propriétés `P14_has_original_author`/`_translator`/`_abridger`/`_scientific_editor`/`_publisher`, déclarées selon la « Encoding Rule 4 » du CIDOC-CRM SIG (voir `decisions/fr/informe-P14-roles-autorat.md` et `informe-activite-editoriale-scientifique.md`). En dehors de ce cas, la contribution de CAO_CRM est purement une **sélection et composition bornée** de fragments de CIDOC-CRM, LRMoo et CRMdig.

Le module est construit par une méthode reproductible et vérifiable : la liste exacte de termes `imports/module-terms.txt` sert d'unique point d'entrée à l'extraction (ROBOT, `extract --method subset`, sur la fusion préalable des trois sources officielles complètes), et chaque axiome d'origine — domaines, rangs, étiquettes, notes d'application — est conservé intact. Le raisonnement complet derrière chaque choix de modélisation est consigné dans `decisions/` (voir section 6).

### Numérotation de version : pourquoi 1.0

CAO_CRM n'avait jamais été publié avant cette version : la numérotation publique commence donc, conformément à la pratique usuelle de versionnage des ontologies (que suivent d'ailleurs CIDOC-CRM, LRMoo et CRMdig eux-mêmes, avec leurs propres numéros 7.1.3/1.1.1/5.0), à **1.0**. Ce dépôt ne contient que cette version publiée ; l'archive de conception qui y a conduit est consignée dans `decisions/`.

---

## 4. État de la validation (version 1.0)

Le pipeline complet est rejoué par CI (`validate.yml`) à chaque push et chaque pull request.

| # | Catégorie | Commande | Résultat |
|---|---|---|---|
| 1 | Syntaxe | `make syntax` | ✅ **PASS** — 0 erreur (rapper + riot + rdflib) |
| 2 | Cohérence logique | `make reason` | ✅ **PASS** — raisonneur HermiT, ontologie cohérente, 0 classe insatisfiable, fusionnée avec les 3 sources officielles complètes + SKOS |
| 3 | SHACL | `make shacl` | ✅ **PASS** — 7 formes réelles, validées contre un graphe d'instance réel et non synthétique (`test-data/stendhal-le-rouge-et-le-noir.ttl`), y compris le cas négatif (une donnée obligatoire retirée déclenche bien une violation) |
| 4 | Conformité avec CIDOC-CRM/LRMoo/CRMdig | `make conformance` | ✅ **PASS** — aucun axiome des ontologies de base modifié (revue manuelle consignée dans `validation/06-conformance/out/`) |
| 5 | Métadonnées de l'en-tête | `make metadata` | ✅ **PASS 7/7** |
| 6 | Qualité (OOPS!) | `make quality` | ✅ **PASS** — 0 critique, 0 important, 2 mineurs (3 pitfalls exclus du filtre, chacun avec justification documentée) — voir détail ci-dessous |
| 7 | Métriques structurelles (ROBOT report) | `make metrics` | ✅ **PASS** — profil personnalisé documenté, voir détail ci-dessous |
| 8 | FAIR (FOOPS!) | `make fair` | ✅ **PASS — 0,80/1,0** — exécution locale reproductible (jar officiel v0.4.0, endpoint `assessOntologyFile`) — voir détail ci-dessous |

**`cq` (questions de compétence, hors des huit catégories numérotées mais exécutée avec la même rigueur) :** les 5 questions de compétence de `competency-questions/CQ-001-a-005-stendhal.md` et les 2 vérifications de cardinalité sont traduites en requêtes SPARQL réelles (`sparql/ask/`, `sparql/select/`) et s'exécutent contre le même graphe d'instance que `shacl` — `make cq` les rejoue toutes.

**`shacl`/`cq` :** le graphe d'instance est un cas réel, vérifié contre les sources primaires (BnF/Gallica pour l'édition Martineau, Internet Archive pour la traduction Scott Moncrieff), et chaque forme SHACL est confirmée par son cas négatif — retirer une donnée obligatoire déclenche bien la violation attendue ; un graphe trop simple pourrait passer n'importe quelle forme faute d'avoir quoi que ce soit à violer. Voir `test-data/PROVENANCE-stendhal-verificacion.md` et `test-data/PROVENANCE-stendhal-traduccion-internet-archive.md` pour la trace de vérification complète.

**`fair` :** score reproductible de **0,80/1,0**, obtenu par exécution locale du jar officiel FOOPS! (release v0.4.0, endpoint documenté `assessOntologyFile`). Les vérifications qui ne passent pas ont chacune une explication précise — dont deux (`VOC3`/`VOC4`) qui tiennent au principe même de composition pure : FOOPS! cherche des termes déclarés sous le namespace propre de l'ontologie, et CAO_CRM n'en déclare aucun, par conception. Voir `validation/08-fair/README.md` pour le détail complet du score par dimension FAIR.

**`metrics` :** le rapport ROBOT utilise un profil personnalisé (`report_profile.tsv`) qui rétrograde la règle `duplicate_label` au niveau advisory : les libellés dupliqués signalés (p. ex. `P106_is_composed_of` / `P46_is_composed_of` partageant le même libellé chinois, ou `R28i_was_produced_by` (LRMoo) partageant "was produced by" avec sa propre superpropriété CIDOC-CRM `P108i_was_produced_by`) **existent déjà tels quels dans les fichiers officiels** — aucun n'est introduit par CAO_CRM, vérifié caractère par caractère contre les fichiers vendorisés. C'est le remède standard documenté par ROBOT lui-même pour ce faux positif connu sur du contenu importé ([ontodev/robot#429](https://github.com/ontodev/robot/issues/429)) — voir `validation/05-metrics/README.md`, section « Accepted findings ».

**`quality` :** trois pitfalls OOPS! sont exclus du filtre `<Pitfalls>` envoyé au service (mécanisme officiellement documenté par OOPS! comme liste d'inclusion), chacun avec une justification individuelle : `P19` (domaines/portées multiples — chaque occurrence déjà analysée et justifiée dans `decisions/fr/problemes-et-solutions.md` et revérifiée par la chaîne d'audits), `P10` (absence de disjonction — **aucun des trois fichiers officiels ne déclare la moindre disjonction de classe** : c'est un choix de conception délibéré de cette famille d'ontologies, fondée sur le co-typage multiple, exactement le patron que CAO_CRM utilise partout, p. ex. `F5_Item + E22_Human-Made_Object`), et `P30` (faux positif sur `F2_Expression`/`F3_Manifestation`, deux classes officielles LRMoo bien distinctes). Voir `validation/04-quality/README.md`, section « Excluded pitfalls », pour la justification complète de chacun.

**Interprétation générale :** l'ontologie est syntaxiquement correcte, logiquement cohérente, conforme aux ontologies qu'elle compose, et sans aucun défaut réel non documenté. Tout ce qui reste signalé par les outils automatiques a été examiné individuellement et a une justification écrite et vérifiable.

---

## 5. Publication automatique (CI/CD et GitHub Pages)

**Ce dépôt GitHub est le dépôt principal du projet** ; une copie institutionnelle de référence est maintenue sur le GitLab du Consortium Huma-Num ARIANE (`gitlab.huma-num.fr/consortiumariane/cao_crm`), qui reçoit les mêmes contenus et exécute son propre pipeline (`.gitlab-ci.yml`). `.github/workflows/`, à la racine, définit deux workflows :

1. **`validate.yml`** — rejoue exactement `make validate`, qui inclut les huit catégories automatisées de la section 4 plus `cq` (contre le graphe d'instance réel `test-data/stendhal-le-rouge-et-le-noir.ttl`). Tourne sur chaque push et chaque pull request.
2. **`pages.yml`** — publie **GitHub Pages** : copie `docs/site/` (déjà généré et commité, voir section 1) dans `public/`, `public/ontology/` et `public/ontology/1.0/` (voir ci-dessous pourquoi ces deux derniers), ainsi que les sérialisations RDF/Turtle/N-Triples/JSON-LD dans `public/ontology/`, plus un fichier `public/CNAME` contenant `www.cao-crm.eu`. Ne tourne que sur la branche par défaut. Ne reconstruit **pas** la documentation via Widoco en CI (pas de JDK requis dans ce job) — la discipline : régénérer localement avec `make docs` et commiter `docs/site/` à jour avant de pousser. Côté GitHub, "Source" doit être réglé sur "GitHub Actions" (Settings → Pages).

**Domaine propre :** **www.cao-crm.eu** est configuré en CNAME, côté DNS du domaine, vers `andresecha.github.io` — c'est ce que le fichier `public/CNAME` généré par `pages.yml` indique à GitHub Pages de servir. C'est aussi le namespace propre de l'ontologie (`owl:Ontology` dans `ontology/CAO_CRM-1.0.rdf` : `https://www.cao-crm.eu/ontology/`, `owl:versionIRI` : `.../ontology/1.0`). GitHub Pages ne fait aucune négociation de contenu côté serveur (uniquement des fichiers statiques) : c'est pourquoi le job `pages.yml` place une copie complète du site à la fois à la racine, sous `/ontology/` (le namespace) et sous `/ontology/1.0/` (le `versionIRI`) — la même page d'accueil statique répond dans les trois cas, avec des liens vers chaque sérialisation, plutôt qu'une vraie redirection 303 selon l'en-tête `Accept` (voir `decisions/es/informe-requisitos-publicacion-CAO_CRM.md`, section 1, pour la discussion complète de ce compromis).

**Page d'accueil de la doc publiée :** l'URL racine de Pages sert `public/index.html` — une petite page de choix de langue (régénérée automatiquement par `docs/build.sh` à chaque `make docs`, jamais éditée à la main) qui renvoie vers `index-fr.html`, `index-en.html` et `index-es.html`.

---

## 6. Décisions de conception et audits (français, `decisions/fr/`)

Le cœur documentaire du projet. Chaque fichier peut être lu isolément ; ensemble, ils couvrent l'intégralité du raisonnement derrière chaque choix de modélisation.

| Fichier | Contenu |
|---|---|
| `problemes-et-solutions.md` | Document central — les 8 problèmes de modélisation identifiés (Description/`E62_String`, Système d'écriture, langue, localisation de `F5_Item`, droits, production d'exemplaire, objet numérique natif vs numérisé, dimension, précision XSD), chacun avec citation officielle complète, explication pédagogique, et la distinction explicite entre changement de diagramme et changement de RDF. |
| `complete-model.md` | Vérification exhaustive de la matrice 5 classes × 4 catégories (Caractéristiques/Processus/Statut/Relation) du paper — les manques réels identifiés et résolus (droits de `F1_Work`, relations Expression↔Expression et Work↔Work, placement du Système d'écriture), avec la recherche corroborative indépendante et les sources consolidées dans le même document. |
| `informe-P14-roles-autorat.md` | Justification complète (Encoding Rule 4, MARC Relator Terms, alternatives étudiées) de la décision d'ajouter les sous-propriétés de rôle d'auteur (auteur original, traducteur, abréviateur). |
| `informe-activite-editoriale-scientifique.md` | La branche « activités éditoriales » signalée par le paper comme différenciateur original de CAO_CRM (Manifestation, Item, Objet numérique) — distinction entre éditeur commercial (`P14_has_publisher`) et éditeur scientifique (`P14_has_scientific_editor`), avec citation intégrale du paper et justification de l'asymétrie entre niveaux. |
| `auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md` | Chaîne de 3 audits successifs et indépendants entre eux — RDF terme par terme, puis documentation et conformité conceptuelle, puis vérification croisée finale. Verdict final : 0 défaut critique restant. |
| `ADR-001-disjointness.md` | Pourquoi CAO_CRM ne déclare aucune condition `owl:disjointWith` — suit le même choix délibéré que CIDOC-CRM/LRMoo/CRMdig eux-mêmes. |
| `ADR-002-idiomas-LRMoo-CRMdig.md` | Pourquoi les termes de LRMoo/CRMdig qui n'existent qu'en anglais dans les sources officielles ne sont pas traduits dans le RDF canonique (la traduction de travail vit séparément, voir section 7 et `docs/i18n/`). |
| `ADR-003-autoria-y-procedencia.md` | Attribution de l'auteur du modèle conceptuel (Mélanie Bouland), de l'implémentation RDF/OWL (Andrés Echavarría) et des outils cités dans l'en-tête — voir aussi section 8. |
| `informe-completitud-labels-domain-range.md`, `informe-implementacion-RDF-modulo-acotado.md` | Rapports techniques d'implémentation et d'intégration du diagramme source — voir section 3. |

Le cas du typage de `P3_has_note` est traité dans `problemes-et-solutions.md` (Problème 1) plutôt que comme un ADR : ce cas précis n'a pas fait l'objet d'une décision collective actée par l'équipe, contrairement aux trois ADR ci-dessus — le label ADR implique une décision d'équipe, et il est réservé à ce cas.

`decisions/es/` contient la version espagnole des trois ADR et de certains rapports techniques ; les documents les plus récents (audits, `problemes-et-solutions.md`, `complete-model.md`) existent en version française.

---

## 7. Documentation pédagogique (français, espagnol et anglais)

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

## 8. Auteur, provenance et outils utilisés

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

## 9. Comment citer ce dépôt

Deux citations distinctes, selon ce qui est réutilisé — le modèle lui-même, ou les données de recherche qui documentent sa construction.

**Le modèle (ce dépôt — `ontology/CAO_CRM-1.0.rdf`, identique à `dcterms:bibliographicCitation` dans l'en-tête du fichier, voir section 8) :**

- **fr :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM (Corpus Author Ontology CRM)*, version 1.0. Consortium Huma-Num ARIANE. <https://www.cao-crm.eu/ontology/1.0>. Jeu de données Nakala : <https://doi.org/10.34847/NKL.AE3BV5JI>
- **es :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM (Corpus Author Ontology CRM)*, versión 1.0. Consorcio Huma-Num ARIANE. <https://www.cao-crm.eu/ontology/1.0>. Conjunto de datos Nakala: <https://doi.org/10.34847/NKL.AE3BV5JI>
- **en :** Echavarría Peláez, Andrés Felipe (2026). *CAO_CRM (Corpus Author Ontology CRM)*, version 1.0. Consortium Huma-Num ARIANE. <https://www.cao-crm.eu/ontology/1.0>. Nakala dataset: <https://doi.org/10.34847/NKL.AE3BV5JI>

**Les données de recherche** (diagramme conceptuel, module ontologique, couches de traduction de travail) sont déposées sur **Nakala**, chacune avec sa propre citation suggérée — utile pour citer, par exemple, uniquement la couche de traduction espagnole sans citer l'ensemble. **DOI publics attribués à ce jour :**

| Data | DOI |
|---|---|
| Diagramme conceptuel de CAO_CRM | <https://doi.org/10.34847/NKL.BBB115GR> |
| Module ontologique (identique à la citation du modèle ci-dessus) | <https://doi.org/10.34847/NKL.AE3BV5JI> |
| Traduction de travail (en/fr/es) | <https://doi.org/10.34847/NKL.90DBJ3CI> |
| Traduction de travail (en/fr) | <https://doi.org/10.34847/NKL.DDA58G95> |
