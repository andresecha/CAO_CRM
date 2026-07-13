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
FILE="$(cd "$(dirname "${1:?usage: check.sh <ontology.rdf>}")" && pwd)/$(basename "$1")"
cd "$(dirname "$0")"

python3 - "$FILE" <<'PYEOF'
import sys, re
from rdflib import Graph
g = Graph()
g.parse(sys.argv[1], format="xml")

text = open("check.sparql").read()
prefixes = "\n".join(l for l in text.splitlines() if l.strip().startswith("PREFIX"))
blocks = [b.strip() for b in text.split("\n\n")
          if any(l.strip().startswith("ASK") for l in b.splitlines())]
failed = 0
for b in blocks:
    m = re.search(r"#\s*expect:\s*(true|false)", b)
    expected = (m.group(1) == "true") if m else True
    query = prefixes + "\n" + "\n".join(l for l in b.splitlines() if not l.strip().startswith("#"))
    result = bool(g.query(query).askAnswer)
    ok = (result == expected)
    label = query.splitlines()[-1].strip() if query.strip().endswith("}") else query.strip()
    print(("PASS " if ok else "FAIL ") + f"(expect {expected}, got {result}) " + label)
    if not ok:
        failed += 1
sys.exit(1 if failed else 0)
PYEOF
