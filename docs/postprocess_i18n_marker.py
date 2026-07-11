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
"""Mark, in a generated Widoco index-{lang}.html, every class/property label or
definition that comes from the CAO_CRM working-translation overlay
(CAO_CRM-1.0-i18n.ttl) rather than from the official CIDOC-CRM/LRMoo/CRMdig
sources.

The overlay file itself already carries a header explaining its status (see
compile_overlay.py), but that header is invisible once Widoco has assembled
the cross-reference pages -- a reader looking at a single term's definition
has no way to tell, from the HTML alone, whether "Manifestation" is CIDOC-CRM's
own French label or a CAO_CRM working translation for a term the official
standard never translated. This script closes that gap with a small,
unobtrusive marker (a dagger, with a native HTML tooltip) placed exactly on
the label and/or the definition that the overlay actually supplied -- nothing
else is touched.

Determinism: rather than guessing from term family + language (which would
require hard-coding CIDOC-CRM/LRMoo/CRMdig's exact official-language matrix a
second time), this script reads the *actual* triples the overlay contributed
for the page's own language and marks exactly those IRIs -- so it stays
correct even if the overlay's coverage changes.

Usage: python3 postprocess_i18n_marker.py <index-{lang}.html> <lang> <overlay.ttl>
"""
import re
import sys

import rdflib
from rdflib.namespace import RDFS

TOOLTIP = {
    "fr": "Traduction de travail de l'équipe CAO_CRM, absente des sources officielles CIDOC-CRM/LRMoo/CRMdig.",
    "es": "Traducción de trabajo del equipo CAO_CRM, ausente de las fuentes oficiales CIDOC-CRM/LRMoo/CRMdig.",
    "en": "Working translation by the CAO_CRM team, not present in the official CIDOC-CRM/LRMoo/CRMdig sources.",
}

MARKER_TEMPLATE = '<sup class="i18n-overlay-marker" title="{tooltip}">&#8224;</sup>'

MARKER_CSS = """
<style>
  .i18n-overlay-marker { color: #888; cursor: help; font-size: 0.8em; margin-left: 0.15em; }
</style>
"""


def overlay_iris_for_lang(overlay_path: str, lang: str):
    g = rdflib.Graph()
    g.parse(overlay_path, format="turtle")
    labels, comments = set(), set()
    for s, o in g.subject_objects(RDFS.label):
        if o.language == lang:
            labels.add(str(s))
    for s, o in g.subject_objects(RDFS.comment):
        if o.language == lang:
            comments.add(str(s))
    return labels, comments


def mark_entity(html: str, iri: str, mark_label: bool, mark_comment: bool, tooltip: str) -> str:
    entity_marker = f'id="{iri}"'
    start = html.find(entity_marker)
    if start == -1:
        return html
    block_end = html.find('<div class="entity"', start + 10)
    if block_end == -1:
        block_end = len(html)
    block = html[start:block_end]

    marker = MARKER_TEMPLATE.format(tooltip=tooltip)

    if mark_label:
        # Insert right after the closing </sup> of the type badge (c/op/dp/ap),
        # which always immediately follows the label text in Widoco's own markup.
        m = re.search(r'</h3>', block)
        h3_match = re.search(r'(<h3>.*?</sup>)', block, re.DOTALL)
        if h3_match:
            block = block[:h3_match.end()] + marker + block[h3_match.end():]

    if mark_comment:
        m = re.search(r'(<div class="comment">\s*<span class="markdown">)', block)
        if m:
            block = block[:m.end()] + marker + " " + block[m.end():]

    return html[:start] + block + html[block_end:]


def main():
    if len(sys.argv) != 4:
        sys.exit("usage: postprocess_i18n_marker.py <index-{lang}.html> <lang> <overlay.ttl>")
    html_path, lang, overlay_path = sys.argv[1], sys.argv[2], sys.argv[3]
    if lang not in TOOLTIP:
        sys.exit(f"postprocess_i18n_marker.py: unknown language '{lang}'")

    labels, comments = overlay_iris_for_lang(overlay_path, lang)
    all_iris = labels | comments
    if not all_iris:
        print(f"postprocess_i18n_marker.py: no overlay content for lang={lang}, nothing to mark")
        return

    with open(html_path, encoding="utf-8") as f:
        html = f.read()

    if "i18n-overlay-marker" in html:
        print(f"postprocess_i18n_marker.py: markers already present in {html_path}, skipping")
        return

    tooltip = TOOLTIP[lang]
    for iri in sorted(all_iris):
        html = mark_entity(html, iri, iri in labels, iri in comments, tooltip)

    html = html.replace("</head>", MARKER_CSS + "</head>", 1)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_i18n_marker.py: marked {len(all_iris)} entities in {html_path}")


if __name__ == "__main__":
    main()
