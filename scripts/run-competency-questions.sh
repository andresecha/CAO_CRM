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
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

python3 - <<'PYEOF'
import glob, sys
from rdflib import Graph

data_files = glob.glob("test-data/*.ttl")
if not data_files:
    print("No test-data graphs yet — nothing to run.")
    sys.exit(0)

merged = Graph()
for f in data_files:
    merged.parse(f, format="turtle")

failed = 0
for qfile in sorted(glob.glob("sparql/ask/*.rq")):
    query = open(qfile).read()
    result = bool(merged.query(query).askAnswer)
    status = "PASS" if result else "FAIL"
    print(f"{status}  {qfile}")
    if not result:
        failed += 1

for qfile in sorted(glob.glob("sparql/select/*.rq")):
    query = open(qfile).read()
    rows = list(merged.query(query))
    print(f"INFO  {qfile}: {len(rows)} row(s) — compare manually against the CQ's Expected result field")

sys.exit(1 if failed else 0)
PYEOF
