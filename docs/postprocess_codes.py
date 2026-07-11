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
"""Post-traitement du HTML genere par Widoco : prefixe chaque etiquette visible
(dans la liste "Overview", les references croisees domain/range/sous-classes,
et le titre de la fiche detaillee de chaque terme) avec son code d'origine
CIDOC-CRM/LRMoo/CRMdig (ex. "E7 -- Activity"), extrait de l'IRI elle-meme.

Ne modifie ni le RDF ni la configuration Widoco -- s'execute automatiquement a
chaque build, donc rien a resynchroniser manuellement si les labels changent.
Idempotent : si relance sur un fichier deja prefixe, ne double-prefixe rien.
"""
import re
import sys
from bs4 import BeautifulSoup, NavigableString

CODE_RE = re.compile(r"^([A-Za-z]+\d+[a-z]*)_")
SEP = " — "  # em dash, spelled out via escape to avoid encoding surprises


def code_from_iri(iri):
    local = iri.rsplit("#", 1)[-1].rsplit("/", 1)[-1]
    m = CODE_RE.match(local)
    return m.group(1) if m else None


def prefix_text_node(tag, code):
    """Prepend 'CODE -- ' to the first text content of tag, unless already present."""
    prefix = code + SEP
    for content in tag.contents:
        if isinstance(content, NavigableString) and content.strip():
            if content.strip().startswith(prefix.strip()):
                return False  # ya prefijado, idempotente
            content.replace_with(NavigableString(prefix + str(content)))
            return True
    return False


def main(path):
    with open(path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    changed = 0

    # 1. Enlaces "#IRI" en listas Overview, domain/range, sub/super-clases, etc.
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.startswith("#"):
            continue
        code = code_from_iri(href[1:])
        if not code:
            continue
        if prefix_text_node(a, code):
            changed += 1

    # 2. Titulo de la ficha detallada de cada termino (div.entity > h3/h2)
    for entity_div in soup.find_all("div", class_="entity"):
        code = code_from_iri(entity_div.get("id", ""))
        if not code:
            continue
        h = entity_div.find(["h3", "h2"])
        if h and prefix_text_node(h, code):
            changed += 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"postprocess_codes.py: {changed} etiquettes prefixees avec leur code dans {path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "site/index-en.html")
