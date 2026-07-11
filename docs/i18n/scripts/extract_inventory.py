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
"""Extract a translation-planning inventory from CAO_CRM-1.0.rdf.

For every one of the 130 module terms, records: IRI, local name, source
family (CIDOC-CRM / LRMoo / CRMdig), which languages already have an official
rdfs:label, whether an official rdfs:comment exists in any language other
than English, and the official English label/comment themselves (the raw
material every translation batch starts from).

Usage: python3 extract_inventory.py <path-to-CAO_CRM-1.0.rdf> <output.json>
"""
import json
import sys

import rdflib
from rdflib.namespace import RDFS

RDF_TYPE = rdflib.RDF.type
OWL_CLASS = rdflib.URIRef("http://www.w3.org/2002/07/owl#Class")
OWL_OBJPROP = rdflib.URIRef("http://www.w3.org/2002/07/owl#ObjectProperty")
OWL_DATAPROP = rdflib.URIRef("http://www.w3.org/2002/07/owl#DatatypeProperty")


def family_of(iri: str) -> str:
    if "/extensions/crmdig/" in iri:
        return "CRMdig"
    if "/lrm/lrmoo/" in iri:
        return "LRMoo"
    return "CIDOC-CRM"


def local_name(iri: str) -> str:
    return iri.rstrip("/").rsplit("/", 1)[-1]


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: extract_inventory.py <CAO_CRM-1.0.rdf> <output.json>")
    rdf_path, out_path = sys.argv[1], sys.argv[2]

    g = rdflib.Graph()
    g.parse(rdf_path, format="xml")

    terms = []
    for rdf_type in (OWL_CLASS, OWL_OBJPROP, OWL_DATAPROP):
        for subj in g.subjects(RDF_TYPE, rdf_type):
            if not isinstance(subj, rdflib.URIRef):
                continue
            iri = str(subj)
            labels = {}
            comments = {}
            for o in g.objects(subj, RDFS.label):
                lang = o.language or "none"
                labels[lang] = str(o)
            for o in g.objects(subj, RDFS.comment):
                lang = o.language or "none"
                comments[lang] = str(o)

            terms.append({
                "iri": iri,
                "local_name": local_name(iri),
                "family": family_of(iri),
                "kind": {OWL_CLASS: "class", OWL_OBJPROP: "object_property", OWL_DATAPROP: "data_property"}[rdf_type],
                "official_languages_label": sorted(labels.keys()),
                "official_languages_comment": sorted(comments.keys()),
                "label_en": labels.get("en", ""),
                "comment_en": comments.get("en", ""),
                "label_fr_official": labels.get("fr", None),
                "needs_label_fr": "fr" not in labels,
                "needs_comment_fr": "fr" not in comments,
                "needs_label_es": "es" not in labels,
                "needs_comment_es": "es" not in comments,
            })

    terms.sort(key=lambda t: (t["family"], t["kind"], t["local_name"]))

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(terms, f, ensure_ascii=False, indent=2)

    total = len(terms)
    need_label_fr = sum(t["needs_label_fr"] for t in terms)
    need_comment_fr = sum(t["needs_comment_fr"] for t in terms)
    need_label_es = sum(t["needs_label_es"] for t in terms)
    need_comment_es = sum(t["needs_comment_es"] for t in terms)
    print(f"extract_inventory.py: {total} terms -> {out_path}")
    print(f"  fr: {need_label_fr} labels + {need_comment_fr} comments needed")
    print(f"  es: {need_label_es} labels + {need_comment_es} comments needed")
    print(f"  total fragments to translate: {need_label_fr + need_comment_fr + need_label_es + need_comment_es}")


if __name__ == "__main__":
    main()
