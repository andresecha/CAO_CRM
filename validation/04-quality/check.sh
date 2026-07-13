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
mkdir -p out

python3 - "$FILE" <<'PYEOF'
import sys, urllib.request

path = sys.argv[1]
with open(path, encoding="utf-8") as f:
    content = f.read()

# CDATA per OOPS! web service spec (https://oops.linkeddata.es/webservice.html) -
# content is not XML-escaped, just wrapped, so guard against a stray "]]>" in the ontology.
safe_content = content.replace("]]>", "]]]]><![CDATA[>")

# Pitfalls actually implemented by the OOPS! service, minus P10/P19/P30 -- see
# validation/04-quality/README.md, "Excluded pitfalls" section, for the full
# justification (2026-07-07) of why these three do not apply to this ontology
# family and are not silently-accepted defects.
PITFALLS = "2,3,4,5,6,7,8,11,12,13,20,21,22,24,25,26,27,28,29"

payload = f"""<?xml version="1.0" encoding="utf-8"?>
<OOPSRequest>
<OntologyUrl></OntologyUrl>
<OntologyContent><![CDATA[{safe_content}]]></OntologyContent>
<Pitfalls>{PITFALLS}</Pitfalls>
<OutputFormat>XML</OutputFormat>
</OOPSRequest>"""

req = urllib.request.Request(
    "https://oops.linkeddata.es/rest",
    data=payload.encode("utf-8"),
    headers={"Content-Type": "application/xml"},
)
with urllib.request.urlopen(req, timeout=120) as resp:
    report = resp.read().decode("utf-8")

with open("out/oops-report.xml", "w", encoding="utf-8") as f:
    f.write(report)

critical = report.count("<oops:Importance>Critical</oops:Importance>")
important = report.count("<oops:Importance>Important</oops:Importance>")
minor = report.count("<oops:Importance>Minor</oops:Importance>")
print(f"OOPS! report: {critical} critical, {important} important, {minor} minor pitfall type(s) -> out/oops-report.xml")
sys.exit(1 if critical > 0 else 0)
PYEOF
