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
# docs/ — generated human-readable documentation

**Tool:** [Widoco](https://github.com/dgarijo/Widoco) (jar-based, generates a full static HTML documentation site including sections, cross-references, and a changelog from `owl:versionIRI` history). Alternative: [pyLODE](https://github.com/RDFLib/pyLODE) (Python, lighter output) if Java/Widoco is undesirable.

**Run** (from the repo root — equivalently, `make docs`):
```bash
bash docs/build.sh ontology/CAO_CRM-1.0.rdf
```
(If invoking `build.sh` directly from inside `docs/` instead, drop the `docs/` prefix from both the script and the ontology path: `bash build.sh ontology/CAO_CRM-1.0.rdf` — `build.sh` resolves the ontology path relative to the repo root it computes from its own location, not from the caller's cwd.)

**Pass criteria:** `site/index-{en,fr,es}.html` all build without error and include non-empty, real (not just placeholder-template) content for classes, object properties, and datatype properties.

**Output:** `site/` — **not** gitignored (see `.gitignore`): it's committed as a ready-to-view artifact, so regenerate with the command above and commit the result whenever `ontology/CAO_CRM-1.0.rdf` changes. Four HTML entry points: `index.html` (a small hand-generated landing page linking the three languages — needed because this is what GitLab/GitHub Pages serves at the site root, and Widoco itself never produces a bare `index.html`) plus `index-{en,fr,es}.html`, one per language, each a fully self-contained file — `build.sh` deliberately does NOT use Widoco's combined `-lang en-fr-es` in one call (see "Multi-language build" below for why).

**PDF export:** `build.sh` also exports each of the three finished HTML files to PDF (`CAO_CRM-<version>-{en,fr,es}.pdf`, e.g. `CAO_CRM-1.0-fr.pdf`), linked from `index.html`. It shells out to whatever headless Chrome/Chromium binary is found on `PATH` (tries, in order: `google-chrome`, `google-chrome-stable`, `chromium`, `chromium-browser`) using its built-in `--print-to-pdf`, with `--no-pdf-header-footer` to suppress the browser's own date/title print header. This step is skipped (with a printed note, not a build failure) if no such binary is available — the HTML remains the primary, always-produced output. Since the PDF is exported from the exact same post-processed HTML Widoco/`postprocess_codes.py` produced, the two never drift out of sync with each other; regenerate both together with the single `build.sh` command above.

**Published via GitHub Pages:** see `.github/workflows/pages.yml` at the repo root — it copies `docs/site/` verbatim into `public/` on every push to the default branch; it does not rebuild via Widoco in CI (no JDK needed there), so the committed `docs/site/` must already be current. (The GitLab CI/CD equivalent, `.gitlab-ci.yml`, applies to the institutional GitLab copy — see README.md section 5.)

## Build design notes

- **Self-contained output (`-uniteSections`, `-includeAnnotationProperties`):** each language builds to a single, fully self-contained HTML file, viewable directly via `file://`. Without `-uniteSections`, Widoco splits content across separate `sections/*.html` files stitched together client-side via jQuery AJAX — which silently fails to load on local files (same-origin restrictions), leaving the documentation apparently empty when opened directly.

- **Abstract vs. Introduction:** the Abstract section is populated automatically from `dcterms:abstract` on the ontology header. The Introduction has no RDF-annotation equivalent Widoco reads, so it's supplied per language via Widoco's `pathToIntro` config option (`config-{lang}.properties` + `intro-{lang}.html`).

- **Widoco constraints handled by `build.sh`:** `-confFile` and `-getOntologyMetadata` are mutually exclusive (Widoco's own stated restriction) — using `pathToIntro` therefore means metadata (abstract, license, authors...) is not auto-extracted from the RDF at build time and must live in each config file. And `pathToIntro` only accepts an **absolute** path (it is not resolved relative to the working directory or to the config file's folder) — `build.sh` substitutes an absolute path into a throwaway temp copy of each `config-{lang}.properties` at build time, so the committed config files stay portable (relative paths, no machine-specific paths committed).

- **Division of responsibility:** `-confFile` supplies only content Widoco cannot source from the RDF (the Introduction, the per-language abstract/description/status) — never to override anything the RDF header already states. If a header value is wrong, fix it in `ontology/CAO_CRM-1.0.rdf` itself: every other consumer of the header (catalogs, FAIR harvesters) reads the same triples.

## Multi-language build: en/fr/es, three separate files, three custom introductions

`build.sh` runs Widoco **three times**, not once with a combined `-lang en-fr-es`:

1. `-lang en` with `-confFile`/`pathToIntro=intro-en.html` (config: `config-en.properties`).
2. `-lang fr` with `-confFile`/`pathToIntro=intro.html` (config: `config-fr.properties`) — the French intro keeps the bare filename `intro.html`.
3. `-lang es` with `-confFile`/`pathToIntro=intro-es.html` (config: `config-es.properties`).

Each language has its own hand-written, hand-translated Introduction and its own translated `abstract`/`description`/`status` fields, all reflecting the model's published 1.0 state (41 classes, 84 object properties, 5 data properties). The three outputs are fully independent: each language's Introduction text appears only in its own file.

**If the ontology header or any of these facts change**, all three `intro-*.html` and `config-*.properties` files need re-syncing by hand — there is no automated single source of truth for this prose, only the RDF's own header (which the `abstract`/`description` fields paraphrase, in each language) and `decisions/fr/*.md` (which the Design Rationale / Consistency sections summarize).

**Known limitation of the source models themselves (not a build issue):** CIDOC-CRM's official RDFS release only provides labels in seven languages (German, Greek, English, French, Portuguese, Russian, Chinese) — **no Spanish label exists for any CIDOC-CRM/LRMoo/CRMdig term**, and no definition (`rdfs:comment`) is translated in any language, not even for CIDOC-CRM's own native terms. Left unaddressed, `index-es.html` and `index-fr.html` would show large stretches of untranslated English. Per `decisions/fr/ADR-002-idiomas-LRMoo-CRMdig.md`, adding an official-looking translation directly to `ontology/CAO_CRM-1.0.rdf` would be content CAO_CRM originates on its own, not something taken from an official source.

**Handled for the generated documentation via `docs/i18n/`:** a separate translation overlay (`docs/i18n/CAO_CRM-1.0-i18n.ttl`) supplies working French/Spanish labels and definitions for exactly these gaps, merged into a *temporary* copy of the ontology only at `build.sh` time — `ontology/CAO_CRM-1.0.rdf` itself is never touched. Every label/definition sourced from the overlay is marked with a small dagger (†) and tooltip in the generated HTML (`postprocess_i18n_marker.py`), so a reader can always tell official CIDOC-CRM content from CAO_CRM's own working translation. See `docs/i18n/README.md` for the full layout, the regeneration command, and how to add another language.

**Code-prefixing (`postprocess_codes.py`) runs on all three files** — it keys off each term's IRI, not its label text, so it works identically regardless of language.

## Landing page (`site/index.html`)

Widoco itself never writes a plain `index.html` — only `index-{en,fr,es}.html` — while GitHub/GitLab Pages serves exactly `public/index.html` at the site root; without one, visiting the root would 404 even though the three real pages exist one path segment away. `build.sh` therefore generates a small static `site/index.html` at the end of every run — a one-page language picker linking to the three files, no Widoco involvement, regenerated in full (never hand-edited) on every build so it never drifts from the actual set of languages produced.
