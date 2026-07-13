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

if [ ! -x "$ROBOT" ]; then
  echo "ROBOT not installed — run scripts/install-tools.sh first" >&2
  exit 1
fi

"$ROBOT" reason --input "$MERGED" --reasoner HermiT \
  --output "$OUT/reasoned.ttl" \
  2>&1 | tee "$OUT/reason.log"

if grep -qi "inconsistent\|unsatisfiable" "$OUT/reason.log"; then
  echo "FAIL: inconsistency or unsatisfiable class detected — see $OUT/reason.log"
  exit 1
fi
echo "PASS: ontology consistent, no unsatisfiable classes reported."
