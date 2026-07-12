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
ONTOLOGY="${1:?usage: merge.sh <ontology.rdf> <output.ttl>}"
OUTPUT="${2:?usage: merge.sh <ontology.rdf> <output.ttl>}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$(dirname "$0")"

RIOT="$(command -v riot || true)"
[ -z "$RIOT" ] && [ -x "$ROOT/.tools/jena/bin/riot" ] && RIOT="$ROOT/.tools/jena/bin/riot"
if [ -z "$RIOT" ]; then
  echo "riot (Apache Jena) not found — run scripts/install-tools.sh first" >&2
  exit 1
fi

shopt -s nullglob
VENDOR_FILES=(vendor/*.rdf)
if [ ${#VENDOR_FILES[@]} -eq 0 ]; then
  echo "No vendored files in imports/vendor/ — run imports/fetch.sh first." >&2
  exit 1
fi

"$RIOT" --output=turtle "../$ONTOLOGY" "${VENDOR_FILES[@]}" > "../$OUTPUT"
echo "Merged $((${#VENDOR_FILES[@]} + 1)) files -> $OUTPUT"
