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
MERGED="${1:?usage: check.sh <merged.ttl>}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$(dirname "$0")/out"
mkdir -p "$OUT"
ROBOT="$ROOT/.tools/robot"
BASE="$ROOT/imports/vendor/cidoc-crm-7.1.3.rdf"

if [ ! -f "$BASE" ]; then
  echo "Vendored CIDOC-CRM file missing — run imports/fetch.sh first" >&2
  exit 1
fi

"$ROBOT" diff --left "$BASE" --right "$MERGED" --output "$OUT/diff.txt"
# Ignore the harmless OntologyID(...) VersionIRI line -- it's a merge artifact from combining
# multiple owl:Ontology headers into one file (documented in this folder's README), not a real
# axiom loss. Any OTHER "-" line means a genuine base-ontology axiom disappeared -- that's real.
if grep -E '^-' "$OUT/diff.txt" | grep -qv '^- OntologyID('; then
  echo "FAIL: base-ontology axioms were modified/removed — see $OUT/diff.txt"
  exit 1
fi
echo "PASS (automated part): no base-ontology axioms modified beyond the known-harmless OntologyID/VersionIRI merge artifact. Manual review of subclass relationships still recommended — see out/conformance-notes.md"
