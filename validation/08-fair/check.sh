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
# Runs the real FOOPS! tool locally (not the unverified public REST guess this
# script used to rely on -- see git history). The public web form
# (https://foops.linkeddata.es/FAIR_validator.html, aliased at
# https://w3id.org/foops/) never exposed a documented, stable JSON POST
# contract; the jar released at github.com/oeg-upm/fair_ontologies does, and
# was confirmed working on 2026-07-10 (its own Spring Boot server, endpoint
# POST /assessOntologyFile, multipart file upload) -- see README.md in this
# same directory for the full breakdown of the resulting score.
set -euo pipefail
FILE="$(cd "$(dirname "${1:?usage: check.sh <ontology.rdf>}")" && pwd)/$(basename "$1")"
cd "$(dirname "$0")"
mkdir -p out .tools

JAR=".tools/fair_ontologies-0.4.0.jar"
JAR_URL="https://github.com/oeg-upm/fair_ontologies/releases/download/v0.4.0/fair_ontologies-0.4.0.jar"
PORT=8083

if [ ! -f "$JAR" ]; then
  echo "Downloading FOOPS! v0.4.0 ($JAR_URL)..."
  curl -sL -o "$JAR" "$JAR_URL"
fi

LOG="$(mktemp)"
java -jar "$JAR" --server.port="$PORT" > "$LOG" 2>&1 &
SERVER_PID=$!
cleanup() { kill "$SERVER_PID" >/dev/null 2>&1 || true; rm -f "$LOG"; }
trap cleanup EXIT

echo "Waiting for local FOOPS! server (pid $SERVER_PID) on port $PORT..."
for _ in $(seq 1 30); do
  if curl -s -o /dev/null "http://localhost:$PORT/tests" 2>/dev/null; then
    break
  fi
  sleep 1
done

HTTP_CODE=$(curl -s -o out/foops-report.json -w "%{http_code}" \
  -X POST "http://localhost:$PORT/assessOntologyFile" \
  -H "accept: application/json;charset=UTF-8" \
  -F "file=@${FILE};type=application/rdf+xml")

if [ "$HTTP_CODE" != "200" ]; then
  echo "FAIL: FOOPS! request returned HTTP $HTTP_CODE. Server log:"
  cat "$LOG"
  exit 1
fi

python3 - <<'PYEOF'
import json
with open("out/foops-report.json", encoding="utf-8") as f:
    d = json.load(f)
print(f"FOOPS! overall_score: {d.get('overall_score')}")
by_cat = {}
for c in d.get("checks", []):
    cat = c["category_id"]
    by_cat.setdefault(cat, [0, 0])
    by_cat[cat][1] += 1
    if c["status"] == "ok":
        by_cat[cat][0] += 1
for cat, (ok, total) in by_cat.items():
    print(f"  {cat}: {ok}/{total} checks OK")
print("Full report -> out/foops-report.json")
PYEOF
echo "PASS: FOOPS! report generated (see out/foops-report.json; interpret score against the checklist in README.md -- a non-1.0 score is expected and should be read, not just re-run)."
