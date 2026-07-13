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
FILE="${1:?usage: check.sh <ontology.rdf>}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$(dirname "$0")/out"
mkdir -p "$OUT"
ROBOT="$ROOT/.tools/robot"

"$ROBOT" report --input "$FILE" --profile "$(dirname "$0")/report_profile.tsv" \
  --output "$OUT/report.tsv" --fail-on ERROR \
  || { echo "FAIL: see $OUT/report.tsv"; exit 1; }
"$ROBOT" validate-profile --input "$FILE" --profile DL --output "$OUT/profile.txt" \
  || echo "NOTE: not OWL 2 DL-compliant — see $OUT/profile.txt (document why in README if intentional)"
echo "PASS: no ERROR-level report violations."
