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
"""Link team members' names to their personal/professional pages, in the
Widoco-generated <div class="head"> metadata block only (Creator/Contributor
<dd> lines) -- deliberately scoped to two exact, known substrings rather than
a blind name search-and-replace, since several of these names (Fatiha Idmhand,
Melanie Bouland) also appear elsewhere in the document (the copyright header,
the acknowledgments paragraph, narrative prose) where they must NOT be turned
into links."""
import sys

PEOPLE_LINKS = {
    "Fatiha Idmhand": "https://fatihaidmhand.ovh/",
    "Ioana Galleron": "https://www.sorbonne-nouvelle.fr/mme-galleron-ioana-468922.kjsp",
    "Sabine Loudcher": "https://eric.univ-lyon2.fr/sabine/",
    "Ala Eddine Laouir": "https://alaeddinelaouir.github.io/homepage/",
    "Ameni Guizani": "https://www.linkedin.com/in/guizani-ameni-5b431b220",
    "Mélanie Bouland": "https://www.linkedin.com/in/melanie-bouland",
}


def link(name):
    url = PEOPLE_LINKS[name]
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{name}</a>'


# Exact strings Widoco always emits for CAO_CRM's fixed dc:creator/dc:contributor
# literals (same in every language, since personal names are never translated).
CREATOR_DD = (
    '<dd><a href="https://cachetown.fr/" target="_blank" rel="noopener noreferrer">'
    "Andrés Echavarría Peláez</a></dd><dd> Mélanie Bouland</dd>"
)
CREATOR_DD_LINKED = (
    '<dd><a href="https://cachetown.fr/" target="_blank" rel="noopener noreferrer">'
    "Andrés Echavarría Peláez</a></dd><dd> "
    + link("Mélanie Bouland") + "</dd>"
)

CONTRIBUTOR_DD = (
    "<dd>Fatiha Idmhand</dd><dd> Ioana Galleron</dd><dd> Sabine Loudcher</dd>"
    "<dd> Ala Eddine Laouir</dd><dd> Ameni Guizani</dd>"
)
CONTRIBUTOR_DD_LINKED = (
    "<dd>" + link("Fatiha Idmhand") + "</dd>"
    "<dd> " + link("Ioana Galleron") + "</dd>"
    "<dd> " + link("Sabine Loudcher") + "</dd>"
    "<dd> " + link("Ala Eddine Laouir") + "</dd>"
    "<dd> " + link("Ameni Guizani") + "</dd>"
)


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: postprocess_people_links.py <index.html>")
    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        html = f.read()

    if CREATOR_DD_LINKED in html and CONTRIBUTOR_DD_LINKED in html:
        print(f"postprocess_people_links.py: already present in {path}, skipping")
        return

    if CREATOR_DD not in html:
        sys.exit(f"postprocess_people_links.py: creator <dd> block not found in {path}")
    if CONTRIBUTOR_DD not in html:
        sys.exit(f"postprocess_people_links.py: contributor <dd> block not found in {path}")

    html = html.replace(CREATOR_DD, CREATOR_DD_LINKED, 1)
    html = html.replace(CONTRIBUTOR_DD, CONTRIBUTOR_DD_LINKED, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_people_links.py: people links inserted into {path}")


if __name__ == "__main__":
    main()
