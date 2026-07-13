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
cd "$(dirname "$0")"
mkdir -p out
STATUS=0
shopt -s nullglob
for data in ../../test-data/*.ttl; do
  name="$(basename "$data" .ttl)"
  echo "== $name =="
  pyshacl -s shapes.ttl -d "$data" -f human > "out/$name.report.txt" 2>&1 || STATUS=1
  tail -n 5 "out/$name.report.txt"
done
if [ $STATUS -ne 0 ]; then
  echo "FAIL: see out/*.report.txt"
else
  echo "PASS: all test-data graphs conformant."
fi
exit $STATUS
