# CAO_CRM (Corpus Author Ontology CRM)
# Copyright (c) 2026 Andres Echavarria Pelaez
# Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)
# Encoding carried out under the scientific direction and support of Fatiha Idmhand
#
# This file is part of the CAO_CRM publication package, licensed under the
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
# License (CC BY-NC-SA 4.0). To view a copy of this license, visit
# https://creativecommons.org/licenses/by-nc-sa/4.0/
#
# Regenerates ontology/CAO_CRM-1.0.{ttl,nt,jsonld} from ontology/CAO_CRM-1.0.rdf.
#
# Exists because rdflib silently drops XML/Turtle *comments* on every parse+serialize
# round trip (comments are not part of the RDF data model) -- a plain `g.parse(...);
# g.serialize(...)` therefore strips the copyright header from the derived files every
# single time, which is exactly what happened earlier in this project's history. This
# script re-stamps the header on the two derived formats that support comments (Turtle,
# N-Triples both use '#'); JSON-LD has no comment syntax at all, so .jsonld is left
# without one, same as any other JSON file in this repo (requirements.txt-style plain
# data files are the other deliberate exception -- see scripts/check-watermark.sh).
#
# Run after any edit to ontology/CAO_CRM-1.0.rdf:
#   python3 scripts/reserialize-ontology.py

import pathlib
import rdflib

HEADER = """# CAO_CRM (Corpus Author Ontology CRM)
# Copyright (c) 2026 Andres Echavarria Pelaez
# Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)
# Encoding carried out under the scientific direction and support of Fatiha Idmhand
#
# This file is part of the CAO_CRM publication package, licensed under the
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
# License (CC BY-NC-SA 4.0). To view a copy of this license, visit
# https://creativecommons.org/licenses/by-nc-sa/4.0/
#
"""

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "ontology" / "CAO_CRM-1.0.rdf"

g = rdflib.Graph()
g.parse(SRC, format="xml")
print(f"triples: {len(g)}")

ttl = g.serialize(format="turtle")
(ROOT / "ontology" / "CAO_CRM-1.0.ttl").write_text(HEADER + ttl, encoding="utf-8")

nt = g.serialize(format="nt")
(ROOT / "ontology" / "CAO_CRM-1.0.nt").write_text(HEADER + nt, encoding="utf-8")

# JSON-LD has no comment syntax -- no header prepended, by design.
g.serialize(destination=str(ROOT / "ontology" / "CAO_CRM-1.0.jsonld"), format="json-ld")

print("done: CAO_CRM-1.0.ttl, CAO_CRM-1.0.nt (with header), CAO_CRM-1.0.jsonld (no comment syntax)")
