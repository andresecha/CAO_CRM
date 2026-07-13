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
"""Link team members' names -- but not their institutional affiliation, given in
parentheses right after each name -- to their personal/professional pages, in the
Widoco-generated <div class="head"> metadata block only (Creator/Contributor <dd>
lines). Deliberately scoped to two exact, known substrings rather than a blind
name search-and-replace, since several of these names (Fatiha Idmhand, Melanie
Bouland) also appear elsewhere in the document (the copyright header, the
acknowledgments paragraph, narrative prose) where they must NOT be turned into
links, and since Widoco's own authorsURI mechanism wraps the *entire* dc:creator
value -- name and affiliation both -- in a single <a>, which this script narrows
back down to just the name."""
import sys

PEOPLE_LINKS = {
    "Andrés Echavarría Peláez": "https://cachetown.fr/",
    "Mélanie Bouland": "https://www.linkedin.com/in/melanie-bouland",
    "Fatiha Idmhand": "https://fatihaidmhand.ovh/",
    "Ioana Galleron": "https://www.sorbonne-nouvelle.fr/mme-galleron-ioana-468922.kjsp",
    "Sabine Loudcher": "https://eric.univ-lyon2.fr/sabine/",
    "Ala Eddine Laouir": "https://alaeddinelaouir.github.io/homepage/",
    "Ameni Guizani": "https://www.linkedin.com/in/guizani-ameni-5b431b220",
    "Amelia Sanz": "https://www.ucm.es/leethi/amelia-sanz-cabrerizo",
    "Roxana Patras": "https://dhl.uaic.ro/taqwa/elementor-page-2114/members-2/",
    "Simone Rebora": "https://www.dlls.univr.it/?ent=persona&id=19903",
}


def link(name):
    url = PEOPLE_LINKS[name]
    return f'<a href="{url}" target="_blank" rel="noopener noreferrer">{name}</a>'


# Exact strings Widoco emits for CAO_CRM's fixed dc:creator/dc:contributor
# literals (same in every language, since personal names/affiliations are never
# translated). The creator <dd> already carries target/rel -- Widoco's own
# authorsURI mechanism adds them itself -- but wraps the affiliation in the
# link too, which the *_LINKED variant below narrows back to the name only.
CREATOR_DD = (
    '<dd><a href="https://cachetown.fr/" target="_blank" rel="noopener noreferrer">'
    "Andrés Echavarría Peláez (CNRS, AMIS, Consortium-HN ARIANE, France)</a></dd>"
)
CREATOR_DD_LINKED = (
    "<dd>" + link("Andrés Echavarría Peláez")
    + " (CNRS, AMIS, Consortium-HN ARIANE, France)</dd>"
)

CONTRIBUTORS = [
    ("Mélanie Bouland", "CNRS, Consortium-HN ARIANE, France"),
    ("Fatiha Idmhand", "Institut des textes et Manuscrits modernes, UMR8132, Université de Poitiers, France"),
    ("Ioana Galleron", "LATTICE, UMR8094, Université Sorbonne Nouvelle, France"),
    ("Sabine Loudcher", "ERIC, Université Lyon 2, France"),
    ("Ala Eddine Laouir", "CNRS, AMIS, Consortium-HN ARIANE, France"),
    ("Ameni Guizani", "CNRS, AMIS, Consortium-HN ARIANE, France"),
    ("Amelia Sanz", "Grupo de Investigación LEETHI, Universidad Complutense, Madrid, Espagne"),
    ("Roxana Patras", "Universitatea „Alexandru Ioan Cuza”, Iaşi, Roumanie"),
    ("Simone Rebora", "Verona University, Verone, Italie"),
]

CONTRIBUTOR_DD = "".join(
    f"<dd>{name} ({aff})</dd>" if i == 0 else f"<dd> {name} ({aff})</dd>"
    for i, (name, aff) in enumerate(CONTRIBUTORS)
)
CONTRIBUTOR_DD_LINKED = "".join(
    (f"<dd>{link(name)} ({aff})</dd>" if i == 0 else f"<dd> {link(name)} ({aff})</dd>")
    for i, (name, aff) in enumerate(CONTRIBUTORS)
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
