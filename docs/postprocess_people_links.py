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
    """Wrap a name in its personal link, or leave it bare if we don't have one.

    Not every contributor has given us a page to link to -- Ana Salgado, who
    reviewed the Portuguese, has not sent one yet -- and a missing link is not a
    reason to leave someone out of the credits. Fill PEOPLE_LINKS in when it
    arrives and the link appears on the next build, with nothing else to change.
    """
    url = PEOPLE_LINKS.get(name)
    if not url:
        return name
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

# Contributors that belong to one language edition only, because what they
# contributed *is* that edition. Ana Salgado reviewed the Portuguese text and is
# credited on the Portuguese page for it; she is not a contributor to the model
# itself, so she does not appear in the RDF's dc:contributor nor on the other
# four pages. The list here has to match config-<lang>.properties exactly, since
# that is what Widoco renders and what this script matches against.
CONTRIBUTORS_EXTRA = {
    "pt": [("Ana Salgado", "revisão linguística e terminológica da versão portuguesa")],
}


def contributor_dd(lang, linked):
    people = CONTRIBUTORS + CONTRIBUTORS_EXTRA.get(lang, [])
    render = link if linked else (lambda n: n)
    return "".join(
        (f"<dd>{render(name)} ({aff})</dd>" if i == 0 else f"<dd> {render(name)} ({aff})</dd>")
        for i, (name, aff) in enumerate(people)
    )


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: postprocess_people_links.py <index.html> <lang>")
    path, lang = sys.argv[1], sys.argv[2]
    contributor_plain = contributor_dd(lang, linked=False)
    contributor_linked = contributor_dd(lang, linked=True)
    with open(path, encoding="utf-8") as f:
        html = f.read()

    if CREATOR_DD_LINKED in html and contributor_linked in html:
        print(f"postprocess_people_links.py: already present in {path}, skipping")
        return

    if CREATOR_DD not in html:
        sys.exit(f"postprocess_people_links.py: creator <dd> block not found in {path}")
    if contributor_plain not in html:
        sys.exit(f"postprocess_people_links.py: contributor <dd> block not found in {path}")

    html = html.replace(CREATOR_DD, CREATOR_DD_LINKED, 1)
    html = html.replace(contributor_plain, contributor_linked, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_people_links.py: people links inserted into {path}")


if __name__ == "__main__":
    main()
