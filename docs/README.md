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

**Published via GitHub Pages:** see `.github/workflows/pages.yml` at the repo root — it copies `docs/site/` verbatim into `public/` on every push to the default branch; it does not rebuild via Widoco in CI (no JDK needed there), so the committed `docs/site/` must already be current. (The GitLab CI/CD equivalent, `.gitlab-ci.yml`, is kept for the institutional GitLab mirror but no longer publishes the custom domain — see README.md section 5.)

## Two real bugs found and fixed (2026-07-02)

1. **Documentation appeared essentially empty when opened directly.** The first version of `build.sh` didn't pass `-uniteSections`, so Widoco split content across `doc/index-en.html` plus separate `doc/sections/*.html` files, stitched together **client-side via jQuery AJAX** (`$("#overview").load("sections/overview-en.html")`, etc.). Opening the file directly in a browser via `file://` silently fails to load those sections (same-origin/CORS restrictions on local files), so only the header/title/download-links were visible — the actual class/property documentation (thousands of lines) never rendered. Fixed by adding `-uniteSections` (single self-contained HTML file, all content inlined, viewable directly) and `-includeAnnotationProperties` to `build.sh`. Output path also changed as a result: it's now `site/index-en.html` directly, not `site/doc/index-en.html`.

2. **Generated documentation was titled "SKOS Vocabulary" instead of CAO_CRM.** This was Widoco *faithfully* reflecting a real bug in an early draft's ontology header (SKOS's own `terms:title`/`terms:creator`/`terms:contributor` merged onto it verbatim, not a Widoco/build script problem — see "Resolved history" in `validation/07-metadata/README.md`). Not worked around in `build.sh` (e.g. by overriding the title via a Widoco `-confFile`) — the underlying ontology header metadata was fixed directly instead, since every other tool reading `terms:title` (catalogs, FAIR harvesters) would have hit the same wrong-title problem, not just Widoco.

**Update (2026-07-04) — Introduction section, `config.properties` + `intro.html`:** the Abstract section is populated from `dcterms:abstract` on the ontology header (added later, see ADR-003) — no build-time action needed for it. The **Introduction** section has no RDF-annotation equivalent Widoco reads automatically, so it's supplied via Widoco's `pathToIntro` config option instead. (Superseded 2026-07-07 — see "Multi-language build" below: there is now one intro/config pair **per language**, not a single French-only one.)

**Real, verified Widoco quirk:** `-confFile` and `-getOntologyMetadata` are mutually exclusive (Widoco's own stated restriction) — using `pathToIntro` therefore means metadata (abstract, license, authors...) is no longer auto-extracted from the RDF at build time. Also verified empirically: `pathToIntro` is **not** resolved relative to the working directory or to the config file's own folder — only an absolute path works. `build.sh` handles this by substituting an absolute path into a throwaway temp copy of each `config-{lang}.properties` at build time (`$(pwd)/intro-{lang}.html`), so the committed config files themselves stay portable (relative paths, no machine-specific paths committed).

The 2026-07-02 note above (don't use `-confFile` to paper over a wrong `terms:title`) still holds in spirit — this use of `-confFile` supplies content Widoco has no other way to source, it doesn't override anything the RDF already states correctly.

## Multi-language build (updated 2026-07-07): en/fr/es, three separate files, three separate custom introductions

`build.sh` runs Widoco **three times**, not once with `-lang en-fr-es` and not via the earlier two-pass split:

1. `-lang en` with `-confFile`/`pathToIntro=intro-en.html` (config: `config-en.properties`).
2. `-lang fr` with `-confFile`/`pathToIntro=intro.html` (config: `config-fr.properties`) — `intro.html` keeps its historical bare filename rather than being renamed `intro-fr.html`.
3. `-lang es` with `-confFile`/`pathToIntro=intro-es.html` (config: `config-es.properties`).

Until 2026-07-07, only French had real custom Introduction content — English and Spanish fell back to Widoco's own generic placeholder text via `-getOntologyMetadata`, and the shared `config.properties` used for the French pass still carried its abstract/description/status in English, an unnoticed mismatch. All three languages now have their own hand-written, hand-translated Introduction (`intro-en.html`, `intro.html`, `intro-es.html`) and their own translated `abstract`/`description`/`status` fields (`config-en.properties`, `config-fr.properties`, `config-es.properties`), all reflecting the model's final 1.0 state (41 classes, 84 object properties, 5 data properties, three completed audits) rather than the draft state with open `<!-- TODO -->` markers that `intro.html` used to carry.

**If the ontology header or any of these facts change again**, all three `intro-*.html` and `config-*.properties` files need re-syncing by hand — there is no automated single source of truth for this prose, only the RDF's own header (which the `abstract`/`description` fields paraphrase, in each language) and `decisions/fr/*.md` (which the Design Rationale / Consistency sections summarize).

Tested empirically that this produces three genuinely separate files (`index-en.html`, `index-fr.html`, `index-es.html`) with no cross-contamination: each language's own Introduction text appears only in its own file.

**Known, real limitation of the source models themselves (not a build bug) — verified 2026-07-05:** CIDOC-CRM's official RDFS release only ever provided labels in seven languages: German, Greek, English, French, Portuguese, Russian, Chinese. **There has never been a Spanish label for any CIDOC-CRM/LRMoo/CRMdig term**, and no definition (`rdfs:comment`) is ever translated in any language, not even for CIDOC-CRM's own native terms. Left unaddressed, `index-es.html` and `index-fr.html` would show large stretches of untranslated English. Already documented for the canonical RDF module itself in `decisions/fr/ADR-002-idiomas-LRMoo-CRMdig.md`: adding an official-looking translation directly to `ontology/CAO_CRM-1.0.rdf` would be content CAO_CRM originates on its own, not something taken from an official source.

**Closed for the generated documentation only, since 2026-07-09, via `docs/i18n/`:** a separate translation overlay (`docs/i18n/CAO_CRM-1.0-i18n.ttl`) supplies working French/Spanish labels and definitions for exactly these gaps, merged into a *temporary* copy of the ontology only at `build.sh` time — `ontology/CAO_CRM-1.0.rdf` itself is never touched. Every label/definition sourced from the overlay is marked with a small dagger (†) and tooltip in the generated HTML (`postprocess_i18n_marker.py`), so a reader can always tell official CIDOC-CRM content from CAO_CRM's own working translation. See `docs/i18n/README.md` for the full layout, the regeneration command, and how to add another language.

**Code-prefixing (`postprocess_codes.py`) runs on all three files** — it keys off each term's IRI, not its label text, so it works identically regardless of language.

## Landing page (`site/index.html`), added 2026-07-07

Widoco itself never writes a plain `index.html` — only `index-{en,fr,es}.html`. That's a problem the moment this becomes a GitLab/GitHub Pages site: the root URL serves exactly `public/index.html` (see `.gitlab-ci.yml`), so without one, visiting the site's root 404s even though the three real pages exist one path segment away. `build.sh` now generates a small static `site/index.html` at the very end of every run — a one-page language picker linking to the three files, no Widoco involvement, regenerated in full (not hand-edited) on every build so it never drifts from the actual set of languages produced.
