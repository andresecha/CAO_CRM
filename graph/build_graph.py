#!/usr/bin/env python3
#
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
"""Construit un graphe HTML interactif du module CAO_CRM (classes, propriétés,
sous-classes, domaine/rang) avec pyvis -- un fichier unique, navigable dans
n'importe quel navigateur, sans serveur de base de données graphe requis."""
import sys
from pathlib import Path
from rdflib import Graph, RDF, RDFS, OWL
from pyvis.network import Network

ONTOLOGY = sys.argv[1] if len(sys.argv) > 1 else "../ontology/CAO_CRM-1.0.rdf"
OUTPUT = sys.argv[2] if len(sys.argv) > 2 else "CAO_CRM-1.0-graph.html"

g = Graph()
g.parse(ONTOLOGY, format="xml")


def local(uri):
    s = str(uri)
    return s.rstrip("/").rsplit("/", 1)[-1]


def label_en(entity):
    for lbl in g.objects(entity, RDFS.label):
        if lbl.language == "en":
            return str(lbl)
    return local(entity)


classes = sorted(set(g.subjects(RDF.type, OWL.Class)))
objprops = sorted(set(g.subjects(RDF.type, OWL.ObjectProperty)))
dataprops = sorted(set(g.subjects(RDF.type, OWL.DatatypeProperty)))

net = Network(
    height="900px",
    width="100%",
    directed=True,
    bgcolor="#1a1a2e",
    font_color="#f0f0f0",
    notebook=False,
)
net.barnes_hut(gravity=-4000, central_gravity=0.2, spring_length=180, spring_strength=0.02)

SOURCE_COLOR = {
    "cidoc-crm.org": "#4e9eff",       # CIDOC-CRM classes -> bleu
    "lrmoo": "#ff8c42",               # LRMoo -> orange
    "crmdig": "#9d4edd",              # CRMdig -> violet
}


def source_color(uri):
    s = str(uri)
    if "iflastandards" in s:
        return SOURCE_COLOR["lrmoo"]
    if "crmdig" in s:
        return SOURCE_COLOR["crmdig"]
    return SOURCE_COLOR["cidoc-crm.org"]


for c in classes:
    net.add_node(
        str(c),
        label=local(c),
        title=f"<b>{local(c)}</b><br>{label_en(c)}<br><i>{c}</i>",
        color=source_color(c),
        shape="ellipse",
        size=22,
    )

for p in objprops + dataprops:
    net.add_node(
        str(p),
        label=local(p),
        title=f"<b>{local(p)}</b><br>{label_en(p)}<br><i>{p}</i>",
        color="#555577",
        shape="box",
        size=12,
        font={"size": 11},
    )

# rdfs:subClassOf edges (class hierarchy)
for c in classes:
    for parent in g.objects(c, RDFS.subClassOf):
        if parent in classes:
            net.add_edge(str(c), str(parent), color="#888888", label="subClassOf", arrows="to", width=2)

# domain/range edges for object + data properties (property as intermediate node)
for p in objprops + dataprops:
    for dom in g.objects(p, RDFS.domain):
        if dom in classes:
            net.add_edge(str(dom), str(p), color="#3ddc97", label="domain", arrows="to")
    for rng in g.objects(p, RDFS.range):
        if rng in classes:
            net.add_edge(str(p), str(rng), color="#ff6b6b", label="range", arrows="to")

net.set_options("""
{
  "nodes": {"borderWidth": 1, "shadow": true},
  "edges": {"smooth": {"type": "continuous"}, "font": {"size": 9, "color": "#cccccc", "strokeWidth": 0}},
  "interaction": {"hover": true, "tooltipDelay": 100, "navigationButtons": true, "keyboard": true},
  "physics": {"stabilization": {"iterations": 150}}
}
""")

net.write_html(OUTPUT, notebook=False)
print(f"Grafo generado: {OUTPUT}")
print(f"  {len(classes)} clases, {len(objprops)} propiedades de objeto, {len(dataprops)} propiedades de datos")
