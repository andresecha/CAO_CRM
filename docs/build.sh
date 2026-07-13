#!/usr/bin/env bash
##
## CAO_CRM (Corpus Author Ontology CRM)
## Copyright (c) 2026 Andres Echavarria Pelaez
## Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)
## Encoding carried out under the scientific direction and support of Fatiha Idmhand
##
## This file is part of the CAO_CRM publication package, licensed under the
## Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
## License (CC BY-NC-SA 4.0). To view a copy of this license, visit
## https://creativecommons.org/licenses/by-nc-sa/4.0/
##
set -euo pipefail
FILE="${1:?usage: build.sh <ontology.rdf>}"
ONTOLOGY_BASENAME="$(basename "$FILE")"
ONTOLOGY_VERSION="$(basename "$FILE" .rdf | sed 's/^CAO_CRM-//')"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$(dirname "$0")"
mkdir -p .tools

if [ ! -f .tools/widoco.jar ]; then
  # NB: asset filename includes a JDK suffix (verified 2026-07-01 against the
  # v1.4.25 release) — check `curl -s https://api.github.com/repos/dgarijo/Widoco/releases/latest`
  # if this 404s on a future Widoco release.
  curl -L -o .tools/widoco.jar \
    https://github.com/dgarijo/Widoco/releases/latest/download/widoco-1.4.25-jar-with-dependencies_JDK-17.jar
fi

# Companion serializations (Turtle, N-Triples, JSON-LD) alongside the master
# RDF/XML file in ontology/, named identically to it -- so download links in
# the generated docs point to permanent, versioned files in the repo itself
# (ontology/CAO_CRM-<version>.ttl etc.) rather than Widoco's own generic,
# unversioned docs/site/ontology.* copies. RDF/XML itself is not regenerated
# here: the existing .rdf file already *is* that serialization.
#
# Delegates to scripts/reserialize-ontology.py rather than calling rdflib
# directly: a plain g.parse()/g.serialize() round trip silently drops the
# copyright header comment from .ttl/.nt (comments aren't part of the RDF
# data model) -- that script re-stamps it. Regenerating it inline here once
# already stripped the watermark from all three real copies of this repo
# without check-watermark.sh catching it (see that script's own history).
python3 "$ROOT/scripts/reserialize-ontology.py"

# CIDOC-CRM only ever translates rdfs:label (never rdfs:comment, in ANY
# language, not even for its own native terms -- verified empirically,
# 2026-07-09), and LRMoo/CRMdig never translate anything at all outside
# English. i18n/CAO_CRM-1.0-i18n.ttl supplies working French and Spanish
# labels/definitions for exactly those gaps -- produced by the CAO_CRM team,
# clearly marked as such in the generated docs (see postprocess_i18n_marker.py
# below), and NEVER merged into the published ontology/*.rdf itself. The merge
# below happens only in this throwaway temp file, fed to Widoco instead of the
# canonical RDF; regenerate i18n/CAO_CRM-1.0-i18n.ttl from i18n/translations/*.yaml
# with i18n/compile_i18n_overlay.py if the module's terms or translations change.
DOC_ONTFILE="$ROOT/$FILE"
if [ -f i18n/CAO_CRM-1.0-i18n.ttl ]; then
  MERGED_RDF="$(mktemp --suffix=.rdf)"
  trap 'rm -f "$MERGED_RDF"' EXIT
  python3 -c "
import rdflib
g = rdflib.Graph()
g.parse('$ROOT/$FILE', format='xml')
before = len(g)
g.parse('i18n/CAO_CRM-1.0-i18n.ttl', format='turtle')
g.serialize(destination='$MERGED_RDF', format='xml')
print(f'i18n overlay merged for doc build only: {before} -> {len(g)} triples ({len(g)-before} added, ontology/*.rdf itself untouched)')
"
  DOC_ONTFILE="$MERGED_RDF"
fi

# Three separate Widoco passes, one per language, deliberately NOT combined
# into one `-lang en-fr-es` call: each language now has its own hand-authored
# Introduction/Status-of-this-document content (intro-en.html, intro.html for
# fr, intro-es.html) and its own translated abstract/description/status
# (config-en.properties, config-fr.properties, config-es.properties),
# injected via -confFile + pathToIntro. -confFile and -getOntologyMetadata
# are mutually exclusive in Widoco itself, so none of the three passes can
# fall back to re-extracting abstract/description from the RDF's own
# language-tagged literals -- see docs/README.md for the regeneration
# procedure if the RDF header changes and these three config files need
# re-syncing with it.
TMP_CONF="$(mktemp)"
trap 'rm -f "$TMP_CONF"' EXIT

for lang in en fr es; do
  sed "s|^pathToIntro=.*|pathToIntro=$(pwd)/intro-${lang}.html|" "config-${lang}.properties" > "$TMP_CONF"
  if [ "$lang" = fr ]; then
    # French keeps its historical bare filename (intro.html, not intro-fr.html).
    sed -i "s|pathToIntro=$(pwd)/intro-fr.html|pathToIntro=$(pwd)/intro.html|" "$TMP_CONF"
  fi

  java -jar .tools/widoco.jar \
    -ontFile "$DOC_ONTFILE" \
    -outFolder site \
    -rewriteAll \
    -confFile "$TMP_CONF" \
    -uniteSections \
    -includeAnnotationProperties \
    -lang "$lang"
done

# Widoco has been observed to sometimes nest its output under site/doc/ instead of
# site/ directly (behavior seems to vary by version), even with -uniteSections.
# Flatten it so the documented paths (site/index-{en,fr,es}.html) always land there.
# Always overwrite (not just "if the target is missing") -- a stale file from a
# previous run must not silently shadow a fresh nested build.
if [ -d site/doc ]; then
  cp -rf site/doc/. site/
  rm -rf site/doc
fi

# Prefix every visible class/property label with its CIDOC-CRM/LRMoo/CRMdig
# code (e.g. "E7 — Activity"), extracted from each term's own IRI. Runs on
# every build automatically -- no RDF edit, nothing to keep in sync by hand.
# Language-agnostic (keys off the IRI, not the label text), so it applies the
# same way to all three generated files.
for f in site/index-en.html site/index-fr.html site/index-es.html; do
  [ -f "$f" ] && python3 postprocess_codes.py "$f"
done

# Widoco has no config option for real References content (unlike pathToIntro
# for the Introduction) -- it always emits a fixed placeholder sentence per
# language. Substitute it with the verified bibliography (bibliography.html,
# shared across all three languages -- citations to official sources stay in
# their original language, English, matching project convention).
if [ -f bibliography.html ]; then
  for f in site/index-en.html site/index-fr.html site/index-es.html; do
    [ -f "$f" ] && python3 postprocess_references.py "$f" bibliography.html
  done
fi

# Same idea for Acknowledgments: Widoco's own paragraph there (thanking the
# LODE/Widoco developers) is fixed, not configurable -- our own project
# acknowledgments are inserted just before it.
for lang in en fr es; do
  f="site/index-${lang}.html"
  [ -f "$f" ] && python3 postprocess_acknowledgments.py "$f" "$lang"
done

# Widoco 1.4.25 has a real display bug on the "issued" metadata field: the
# label is correctly translated per language ("Émis le:", "Fecha de
# publicación:", "Issued:") but the *value* always renders as the literal,
# untranslated fallback string "Date issued" regardless of the `issued=`
# value actually set in config-{lang}.properties. Patched here rather than
# left broken -- ISSUED_DATE must be kept in sync with `issued=` in the
# three config files by hand.
ISSUED_DATE="2026-07-08"
for f in site/index-en.html site/index-fr.html site/index-es.html; do
  [ -f "$f" ] && sed -i "s|<dd>Date issued</dd>|<dd>${ISSUED_DATE}</dd>|" "$f"
done

# Widoco's own "Authors:"/"Auteurs :"/"Autores:" metadata box renders the
# authorsURI= link (config-*.properties) as a bare <a href>, with no
# target/rel -- unlike every other occurrence of this same link, which we
# author ourselves directly in HTML. Patched here since this specific tag is
# generated by Widoco, not written by us.
for f in site/index-en.html site/index-fr.html site/index-es.html; do
  [ -f "$f" ] && sed -i 's|<a href="https://cachetown.fr/">|<a href="https://cachetown.fr/" target="_blank" rel="noopener noreferrer">|' "$f"
done

# Link team members' names, in the Creator/Contributor lines of Widoco's own
# metadata header, to their personal/professional pages. Runs after the
# authorsURI sed fix-up above, since it matches the already-patched
# (target/rel-bearing) Andrés Echavarría Peláez link.
for lang in en fr es; do
  f="site/index-${lang}.html"
  [ -f "$f" ] && python3 postprocess_people_links.py "$f"
done

# Print-only title page (model name + authors + ARIANE logo), inserted right
# after <body> so it is physically the first page once printed -- must run
# before the Chrome dump-dom step below, on the real site/index-*.html files
# (not a temp copy), since that step navigates to these files directly.
# Invisible in the browser (display:none outside @media print).
mkdir -p site/logos
cp -f logos/ARIANE.svg site/logos/ARIANE.svg
for lang in en fr es; do
  f="site/index-${lang}.html"
  [ -f "$f" ] && python3 postprocess_titlepage.py "$f" "$lang"
done

# Marks, with a small tooltipped dagger, exactly the labels/definitions that
# came from the i18n working-translation overlay above (not from Widoco's own
# language rendering) -- so a reader can always tell official content from
# CAO_CRM's own translations. No-op if the overlay file isn't present.
if [ -f i18n/CAO_CRM-1.0-i18n.ttl ]; then
  for lang in en fr es; do
    f="site/index-${lang}.html"
    [ -f "$f" ] && python3 postprocess_i18n_marker.py "$f" "$lang" i18n/CAO_CRM-1.0-i18n.ttl
  done
fi

# PDF export, one per language, from the same final HTML Widoco produced (post
# code-prefixing above) -- so the PDF and the HTML never drift out of sync with
# each other. Two-step pipeline, each tool doing the one thing it's actually
# good at:
#   1. Headless Chrome/Chromium --dump-dom: Widoco's own page converts every
#      <span class="markdown"> block from raw markdown text to real HTML
#      (<strong>, <em>, <ul><li>, <p>...) via client-side JavaScript
#      (resources/marked.min.js + jQuery, see index-*.html's own <script>
#      tag) -- this only happens when a real browser loads the page and runs
#      that script. --dump-dom navigates, waits for it to finish, and prints
#      the resulting DOM as static HTML.
#   2. WeasyPrint, run on that already-rendered HTML rather than Widoco's raw
#      output: WeasyPrint does NOT execute JavaScript, so feeding it the raw
#      file directly would print the literal, unconverted markdown source
#      (asterisks, literal "- " list markers, no real paragraph breaks) --
#      exactly the bug this two-step pipeline exists to avoid. WeasyPrint is
#      still the one doing the actual PDF compilation because of its proper
#      CSS @page support (real page numbers, margins, the print-only cover
#      page defined in intro.html's <style> block), which Chrome's own
#      print-to-pdf does not render nearly as well.
# Skips gracefully (does not fail the build) if either tool is missing -- the
# HTML documentation remains the primary, always-produced output.
CHROME_BIN=""
for candidate in google-chrome google-chrome-stable chromium chromium-browser; do
  if command -v "$candidate" >/dev/null 2>&1; then
    CHROME_BIN="$candidate"
    break
  fi
done
if [ -n "$CHROME_BIN" ] && python3 -c "import weasyprint" >/dev/null 2>&1; then
  DOM_TMP="$(mktemp -d)"
  trap 'rm -rf "$DOM_TMP"' EXIT
  for lang in en fr es; do
    html="site/index-${lang}.html"
    pdf="site/CAO_CRM-${ONTOLOGY_VERSION}-${lang}.pdf"
    rendered="$DOM_TMP/index-${lang}.rendered.html"
    if [ -f "$html" ]; then
      "$CHROME_BIN" --headless --disable-gpu --no-sandbox \
        --dump-dom "file://$(pwd)/$html" > "$rendered" 2>/dev/null
      python3 -m weasyprint "$rendered" "$pdf" >/dev/null 2>&1
      echo "PDF generated -> docs/$pdf"
    fi
  done
else
  echo "NOTE: PDF export needs both a Chrome/Chromium binary (tried: google-chrome, google-chrome-stable, chromium, chromium-browser) and WeasyPrint (pip install weasyprint) -- skipping, HTML documentation is unaffected."
fi

# Widoco has no notion of a shared, language-neutral landing page -- it only
# writes index-{en,fr,es}.html. Generate site/index.html ourselves so that
# visiting the bare site root (in particular the GitLab/GitHub Pages URL,
# which serves exactly public/index.html) lands somewhere useful instead of
# 404ing. Regenerated in full on every build, not hand-maintained.
cat > site/index.html <<HTMLEOF
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>CAO_CRM (Corpus Author Ontology CRM)</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; max-width: 40rem; margin: 4rem auto; padding: 0 1.5rem; color: #1a1a1a; text-align: center; }
  h1 { font-size: 1.4rem; }
  p.subtitle { font-style: italic; color: #444; font-size: 0.95rem; margin: 0.3em 0; }
  ul { list-style: none; padding: 0; }
  li { margin: 0.6rem 0; }
  a.lang { display: inline-block; padding: 0.5rem 1rem; border: 1px solid #ccc; border-radius: 6px; text-decoration: none; color: #1a1a1a; }
  a.lang:hover { background: #f0f0f0; }
  p.meta { color: #666; font-size: 0.9rem; }
  img.logo { width: 160px; height: auto; margin-top: 2rem; }
  @media (prefers-color-scheme: dark) {
    body { background: #1a1a1a; color: #eee; }
    p.subtitle { color: #aaa; }
    a.lang { border-color: #444; color: #eee; }
    a.lang:hover { background: #2a2a2a; }
    p.meta { color: #999; }
  }
</style>
</head>
<body>
<h1>CAO_CRM (Corpus Author Ontology CRM)</h1>
<p class="subtitle">Un cadre s&eacute;mantique d&eacute;velopp&eacute; par le groupe de travail &laquo;&nbsp;M&eacute;tadonn&eacute;es&nbsp;&raquo; du Consortium-HN ARIANE pour structurer l&rsquo;organisation, la description et l&rsquo;interop&eacute;rabilit&eacute; des m&eacute;tadonn&eacute;es d&eacute;crivant les corpus textuels.</p>
<p class="subtitle">A semantic framework developed by the &ldquo;Metadata&rdquo; working group of the Consortium-HN ARIANE to structure the organization, description, and interoperability of metadata describing textual corpora.</p>
<p class="subtitle">Un marco sem&aacute;ntico desarrollado por el grupo de trabajo &laquo;Metadatos&raquo; del Consorcio-HN ARIANE para estructurar la organizaci&oacute;n, la descripci&oacute;n y la interoperabilidad de los metadatos que describen los corpus textuales.</p>
<p>Choisir une langue / choose a language / elegir un idioma :</p>
<ul>
  <li><a class="lang" href="index-fr.html">🇫🇷 Français</a></li>
  <li><a class="lang" href="index-en.html">🇬🇧 English</a></li>
  <li><a class="lang" href="index-es.html">🇪🇸 Español</a></li>
</ul>
<p class="meta">Version PDF / PDF version / versión PDF :</p>
<ul>
  <li><a class="lang" href="CAO_CRM-${ONTOLOGY_VERSION}-fr.pdf">🇫🇷 PDF</a></li>
  <li><a class="lang" href="CAO_CRM-${ONTOLOGY_VERSION}-en.pdf">🇬🇧 PDF</a></li>
  <li><a class="lang" href="CAO_CRM-${ONTOLOGY_VERSION}-es.pdf">🇪🇸 PDF</a></li>
</ul>
<p class="meta">Version ${ONTOLOGY_VERSION} — Consortium HN Ariane / projet AMIS.</p>
<img class="logo" src="logos/ARIANE.svg" alt="Consortium Huma-Num ARIANE">
</body>
</html>
HTMLEOF

echo "Documentation built -> docs/site/index.html (landing) + index-{en,fr,es}.html"
