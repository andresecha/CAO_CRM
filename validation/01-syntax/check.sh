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
STATUS=0

RIOT="$(command -v riot || true)"
[ -z "$RIOT" ] && [ -x "$ROOT/.tools/jena/bin/riot" ] && RIOT="$ROOT/.tools/jena/bin/riot"

PYTHON="python3"
[ -x "$ROOT/.venv/bin/python3" ] && PYTHON="$ROOT/.venv/bin/python3"

if command -v rapper >/dev/null 2>&1; then
  rapper -i rdfxml -o ntriples "$FILE" > /dev/null 2> "$OUT/rapper.log" || STATUS=1
  echo "rapper: $(grep -c 'Error\|Warning' "$OUT/rapper.log" || true) issue(s) — see $OUT/rapper.log"
else
  echo "SKIP rapper (not installed — see scripts/install-tools.sh)"
fi

if [ -n "$RIOT" ]; then
  "$RIOT" --validate "$FILE" > "$OUT/riot.log" 2>&1 || STATUS=1
  echo "riot: see $OUT/riot.log"
else
  echo "SKIP riot (not installed — see scripts/install-tools.sh)"
fi

"$PYTHON" - "$FILE" > "$OUT/rdflib.log" 2>&1 <<'PYEOF' || STATUS=1
import sys
from rdflib import Graph
g = Graph()
g.parse(sys.argv[1], format="xml")
print(f"OK: parsed {len(g)} triples")
PYEOF
echo "rdflib: see $OUT/rdflib.log"

exit $STATUS
