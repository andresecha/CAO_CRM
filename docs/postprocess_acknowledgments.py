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
"""Insert a project-specific acknowledgments paragraph before Widoco's own
fixed tool-credits paragraph (which thanks the LODE/Widoco developers and is
not itself customizable via config.properties)."""
import sys

# Matched against Widoco's own fixed opening words for the tool-credits
# paragraph in each language, so the insertion point is unambiguous.
ANCHORS = {
    "fr": "Les auteurs voudraient remercier",
    "en": "The authors would like to thank",
    "es": "Los autores agradecen a",
    # Romanian is anchored on the Romanian string even though Widoco 1.4.25 ships
    # no ro bundle and emits this fixed tool-credits paragraph in English: by the
    # time this script runs, postprocess_ro_chrome.py has already translated it
    # (docs/build.sh runs that step earlier, see the ordering note there). Change
    # both together -- this anchor is the `ackText` entry of i18n/chrome-ro.yaml,
    # first fragment, and a mismatch makes this script exit with "anchor not
    # found" rather than fail silently.
    "ro": "Autorii doresc să îi mulțumească lui",
}

PARAGRAPHS = {
    "fr": (
        "Le groupe de travail « Métadonnées » du Consortium Huma-Num ARIANE tient à "
        "remercier chaleureusement Andrés Echavarría Peláez et Mélanie Bouland pour leur "
        "implication remarquable dans la conception, le suivi et le développement de cette "
        "ontologie.",
        "Il remercie également l'infrastructure IR* Huma-Num pour son soutien, et tout "
        "particulièrement Fatiha Idmhand, Ioana Galleron et Sabine Loudcher, pour leur "
        "engagement en tant que coordinatrices du Consortium ARIANE de 2023 à 2026, ainsi "
        "que pour leur rôle de responsables et de membres actives du groupe de travail.",
        "Il adresse en outre ses sincères remerciements à l'ensemble des personnes "
        "impliquées dans le projet AMIS (Advanced Metadata Intelligent System), Ala Eddine "
        "Laouir, Ameni Guizani, Roxana Patras, Amelia Sanz et Simone Rebora, dont le regard "
        "attentif, les remarques et les échanges ont contribué à enrichir ce travail, qui se "
        "situe à l'intersection de la modélisation des connaissances, des technologies du "
        "Web sémantique, des humanités numériques et des études littéraires comparées.",
        "Le groupe de travail tient également à remercier les membres du consortium "
        "Huma-Num MASAPlus, et tout particulièrement Florian Hivert et Olivier Marlet, pour "
        "leurs conseils avisés, leurs recommandations et leurs échanges tout au long de "
        "l'élaboration de cette ontologie.",
    ),
    "en": (
        "The Metadata Working Group of the Huma-Num ARIANE Consortium would like to "
        "express its sincere gratitude to Andrés Echavarría Peláez and Mélanie Bouland for "
        "their outstanding contribution to the design, coordination, and development of "
        "this ontology.",
        "The Working Group also gratefully acknowledges the support of the Huma-Num IR* "
        "research infrastructure, and extends its special thanks to Fatiha Idmhand, Ioana "
        "Galleron, and Sabine Loudcher for their commitment as coordinators of the ARIANE "
        "Consortium from 2023 to 2026, as well as for their roles as coordinators and "
        "active members of the Working Group.",
        "The Working Group further wishes to thank all members of the AMIS (Advanced "
        "Metadata Intelligent System) project, Ala Eddine Laouir, Ameni Guizani, Roxana "
        "Patras, Amelia Sanz, and Simone Rebora, whose careful reading, insightful "
        "comments, and stimulating discussions have significantly enriched this work, "
        "which lies at the intersection of knowledge modelling, Semantic Web technologies, "
        "Digital Humanities, and Comparative Literary Studies.",
        "The Working Group also wishes to thank the members of the Huma-Num MASAPlus "
        "Consortium, and especially Florian Hivert and Olivier Marlet, for their valuable "
        "advice, recommendations, and constructive discussions throughout the development "
        "of this ontology.",
    ),
    # Working (unofficial) Spanish translation of the fr/en text supplied by the working
    # group; faithful in content and structure, but not itself vetted by the group.
    "es": (
        "El grupo de trabajo «Metadatos» del Consorcio Huma-Num ARIANE desea expresar su "
        "más sincero agradecimiento a Andrés Echavarría Peláez y Mélanie Bouland por su "
        "notable contribución en el diseño, el seguimiento y el desarrollo de esta "
        "ontología.",
        "El grupo de trabajo agradece asimismo el apoyo de la infraestructura de "
        "investigación IR* Huma-Num, y expresa su especial gratitud a Fatiha Idmhand, "
        "Ioana Galleron y Sabine Loudcher por su compromiso como coordinadoras del "
        "Consorcio ARIANE de 2023 a 2026, así como por su papel de responsables y miembros "
        "activas del grupo de trabajo.",
        "Asimismo, extiende su sincero agradecimiento a todas las personas implicadas en "
        "el proyecto AMIS (Advanced Metadata Intelligent System): Ala Eddine Laouir, Ameni "
        "Guizani, Roxana Patras, Amelia Sanz y Simone Rebora, cuya atenta lectura, "
        "comentarios y discusiones contribuyeron a enriquecer este trabajo, situado en la "
        "intersección entre el modelado del conocimiento, las tecnologías de la Web "
        "semántica, las humanidades digitales y los estudios literarios comparados.",
        "El grupo de trabajo desea agradecer también a los miembros del consorcio "
        "Huma-Num MASAPlus, y en especial a Florian Hivert y Olivier Marlet, por sus "
        "valiosos consejos, recomendaciones e intercambios a lo largo de la elaboración de "
        "esta ontología.",
    ),
    # Romanian: reviewed by a native speaker (2026-09-01) and wired into
    # docs/build.sh's language loop -- see ANCHORS above for why its insertion
    # point is the English string.
    #
    # Italian and Portuguese remain working (unofficial) translations produced by
    # dedicated translation agents (2026-07-13), not yet vetted by the working group,
    # and are still unwired/gitignored pending a publication decision. They have no
    # ANCHORS entry: Widoco *does* ship it/pt bundles, so their tool-credits paragraph
    # would come out translated, and its exact wording has never been observed for this
    # project. Copy the fixed opening words from an actual generated index-{it,pt}.html
    # rather than guessing them, before wiring either language in.
    "ro": (
        "Grupul de lucru „Metadate” al Consorțiului Huma-Num ARIANE dorește să "
        "le mulțumească călduros D-lui Dr. Andrés Echavarría Peláez și D-nei "
        "Dr. Mélanie Bouland pentru implicarea lor remarcabilă în conceperea, "
        "coordonarea și dezvoltarea acestei ontologii.",
        "De asemenea, Grupul de lucru „Metadate” mulțumește infrastructurii de "
        "cercetare IR* Huma-Num pentru sprijinul acordat și, în mod special, "
        "Doamnelor Profesoare Fatiha Idmhand, Ioana Galleron și Sabine Loudcher "
        "pentru implicarea lor în calitate de coordonatoare ale Consorțiului "
        "ARIANE în perioada 2023-2026, precum și pentru rolul lor de "
        "responsabile și membre active.",
        "Grupul de lucru „Metadate” adresează, de asemenea, sincere mulțumiri "
        "tuturor persoanelor implicate în proiectul AMIS (Advanced Metadata "
        "Intelligent System), Dr. Ala Eddine Laouir, Dr. Ameni Guizani, Prof. "
        "Univ. Dr. Roxana Patras, Prof. Univ. Dr. Amelia Sanz și Conf. Univ. "
        "Dr. Simone Rebora, a căror atenție, observații și schimburi de idei au "
        "contribuit la îmbogățirea acestui demers, situat la intersecția dintre "
        "modelarea cunoașterii, tehnologiile Web-ului semantic, științele "
        "umaniste digitale și studiile de literatură comparată.",
        "Grupul de lucru dorește de asemenea să mulțumească membrilor "
        "consorțiului Huma-Num MASAPlus, în mod special D-lui Dr. Florian "
        "Hivert și Dr. Olivier Marlet, pentru sfaturile lor avizate, "
        "recomandările și schimburile de cunoaștere mobilizate pe parcursul "
        "elaborării acestei ontologii.",
    ),
    "it": (
        "Il gruppo di lavoro «Metadati» del Consorzio Huma-Num ARIANE desidera esprimere "
        "la propria più sincera gratitudine ad Andrés Echavarría Peláez e Mélanie Bouland "
        "per il loro straordinario contributo alla progettazione, al coordinamento e allo "
        "sviluppo di questa ontologia.",
        "Il gruppo di lavoro ringrazia inoltre l'infrastruttura di ricerca IR* Huma-Num "
        "per il suo sostegno, e rivolge un ringraziamento particolare a Fatiha Idmhand, "
        "Ioana Galleron e Sabine Loudcher per il loro impegno come coordinatrici del "
        "Consorzio ARIANE dal 2023 al 2026, nonché per il loro ruolo di responsabili e "
        "membri attive del gruppo di lavoro.",
        "Il gruppo di lavoro desidera inoltre ringraziare tutte le persone coinvolte nel "
        "progetto AMIS (Advanced Metadata Intelligent System), Ala Eddine Laouir, Ameni "
        "Guizani, Roxana Patras, Amelia Sanz e Simone Rebora, la cui lettura attenta, i "
        "cui commenti e i cui scambi hanno contribuito ad arricchire notevolmente questo "
        "lavoro, che si colloca all'intersezione tra la modellazione della conoscenza, le "
        "tecnologie del Web semantico, le discipline umanistiche digitali e gli studi "
        "letterari comparati.",
        "Il gruppo di lavoro desidera altresì ringraziare i membri del consorzio Huma-Num "
        "MASAPlus, e in particolare Florian Hivert e Olivier Marlet, per i loro preziosi "
        "consigli, le loro raccomandazioni e i loro scambi lungo tutto lo sviluppo di "
        "questa ontologia.",
    ),
    "pt": (
        "O grupo de trabalho «Metadados» do Consórcio Huma-Num ARIANE deseja agradecer "
        "calorosamente a Andrés Echavarría Peláez e a Mélanie Bouland pelo seu notável "
        "envolvimento na conceção, no acompanhamento e no desenvolvimento desta ontologia.",
        "Agradece também à infraestrutura de investigação IR* Huma-Num pelo seu apoio, e "
        "em particular a Fatiha Idmhand, Ioana Galleron e Sabine Loudcher, pelo seu "
        "empenho como coordenadoras do Consórcio ARIANE de 2023 a 2026, bem como pelo seu "
        "papel de responsáveis e membros ativas do grupo de trabalho.",
        "Dirige ainda os seus sinceros agradecimentos a todas as pessoas envolvidas no "
        "projeto AMIS (Advanced Metadata Intelligent System), Ala Eddine Laouir, Ameni "
        "Guizani, Roxana Patras, Amelia Sanz e Simone Rebora, cujo olhar atento, "
        "comentários e trocas de ideias contribuíram para enriquecer este trabalho, "
        "situado na interseção entre a modelação do conhecimento, as tecnologias da Web "
        "semântica, as humanidades digitais e os estudos literários comparados.",
        "O grupo de trabalho deseja também agradecer aos membros do consórcio Huma-Num "
        "MASAPlus, e em particular a Florian Hivert e Olivier Marlet, pelos seus "
        "conselhos avisados, recomendações e trocas de ideias ao longo da elaboração "
        "desta ontologia.",
    ),
}


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: postprocess_acknowledgments.py <index.html> <lang>")
    path, lang = sys.argv[1], sys.argv[2]
    if lang not in ANCHORS:
        sys.exit(f"postprocess_acknowledgments.py: unknown language '{lang}'")

    with open(path, encoding="utf-8") as f:
        html = f.read()

    if PARAGRAPHS[lang][0][:40] in html:
        print(f"postprocess_acknowledgments.py: already present in {path}, skipping")
        return

    anchor = ANCHORS[lang]
    if anchor not in html:
        sys.exit(f"postprocess_acknowledgments.py: anchor not found in {path}")

    insertion = "".join(f"<p>{p}</p>\n" for p in PARAGRAPHS[lang]) + "<p>\n"
    html = html.replace(f"<p>\n{anchor}", insertion + anchor, 1)
    html = html.replace(f"<p>{anchor}", insertion + anchor, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_acknowledgments.py: acknowledgments inserted into {path}")


if __name__ == "__main__":
    main()
