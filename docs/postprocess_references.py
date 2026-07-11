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
"""Replace Widoco's placeholder References section with the real bibliography.

Widoco has no config option for supplying real References content (unlike
pathToIntro for the Introduction) -- it always emits a fixed per-language
placeholder sentence. This script substitutes that exact placeholder with the
verified bibliography content shared across all three languages (citations to
official sources conventionally stay in their original language, English here).
"""
import sys

PLACEHOLDERS = {
    "fr": '<span class="markdown">\nAjoutez vos références ici. Il est recommandé de les avoir sous forme de liste.</span>',
    "en": '<span class="markdown">\nAdd your references here. It is recommended to have them as a list.</span>',
    "es": '<span class="markdown">Añade aquí tus referencias, a ser posible en una lista.</span>',
}


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: postprocess_references.py <index.html> <bibliography.html>")
    html_path, bib_path = sys.argv[1], sys.argv[2]

    lang = None
    for candidate in PLACEHOLDERS:
        if f"index-{candidate}.html" in html_path or html_path.endswith("intro.html"):
            lang = candidate
            break
    if lang is None:
        for candidate, placeholder in PLACEHOLDERS.items():
            if placeholder.split("\n")[-1].split("</span>")[0] in open(html_path, encoding="utf-8").read():
                lang = candidate
                break
    if lang is None:
        sys.exit(f"postprocess_references.py: could not detect language for {html_path}")

    with open(html_path, encoding="utf-8") as f:
        html = f.read()
    with open(bib_path, encoding="utf-8") as f:
        bib = f.read()

    placeholder = PLACEHOLDERS[lang]
    if placeholder not in html:
        print(f"postprocess_references.py: WARNING placeholder not found in {html_path} (already patched?)")
        return

    html = html.replace(placeholder, bib)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_references.py: references inserted into {html_path}")


if __name__ == "__main__":
    main()
