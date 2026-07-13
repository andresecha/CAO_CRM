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
"""Insert a print-only title page as the very first page of the PDF.

Must run *before* Chrome dumps the DOM (docs/build.sh), so the title page is
physically first in document order -- CSS alone cannot reorder it before
Widoco's own <div class="head"> block, which is itself turned into the
second page (see the print CSS in intro.html).
"""
import os
import sys

# One-sentence description of the model, shown as an italic subtitle right
# under the ontology name on the print-only cover page -- authored by the
# "Metadata" working group (see docs/postprocess_acknowledgments.py for the
# same group's full acknowledgments paragraph), translated for each language.
SUBTITLES = {
    "fr": (
        "Un cadre s&eacute;mantique d&eacute;velopp&eacute; par le groupe de travail "
        "&laquo;&nbsp;M&eacute;tadonn&eacute;es&nbsp;&raquo; du Consortium-HN ARIANE pour "
        "structurer l&rsquo;organisation, la description et l&rsquo;interop&eacute;rabilit&eacute; "
        "des m&eacute;tadonn&eacute;es d&eacute;crivant les corpus textuels"
    ),
    "en": (
        "A semantic framework developed by the &ldquo;Metadata&rdquo; working group of the "
        "Consortium-HN ARIANE to structure the organization, description, and "
        "interoperability of metadata describing textual corpora"
    ),
    "es": (
        "Un marco sem&aacute;ntico desarrollado por el grupo de trabajo "
        "&laquo;Metadatos&raquo; del Consorcio-HN ARIANE para estructurar la "
        "organizaci&oacute;n, la descripci&oacute;n y la interoperabilidad de los "
        "metadatos que describen los corpus textuales"
    ),
}

TITLE_PAGE_TEMPLATE = """<div class="cover-title-page">
  <h1 class="cover-title-page-name">CAO_CRM<br>(Corpus Author Ontology CRM)</h1>
  <p class="cover-title-page-subtitle">__SUBTITLE__</p>
  <p class="cover-title-page-authors"><a href="https://cachetown.fr/" target="_blank" rel="noopener noreferrer">Andr&eacute;s Echavarr&iacute;a Pel&aacute;ez</a></p>
  <img class="cover-title-page-logo" src="__LOGO_PATH__" alt="Consortium Huma-Num ARIANE">
</div>
<style>
  .cover-title-page { display: none; }
  @media print {
    .cover-title-page {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 25.7cm;
      page-break-after: always;
      text-align: center;
      position: relative;
    }
    .cover-title-page-name { font-size: 29.7px; color: #000; font-weight: bold; max-width: 32em; margin: 0 0 0.6em 0; line-height: 1.3; }
    .cover-title-page-subtitle { font-size: 20px; font-style: italic; color: #000; max-width: 28em; margin: 0 0 1.2em 0; line-height: 1.35; }
    .cover-title-page-authors { font-size: 16px; color: #000; margin: 0; }
    .cover-title-page-logo { position: absolute; bottom: 0.5cm; left: 50%; transform: translateX(-50%); width: 256px; height: auto; }
  }
</style>
"""


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: postprocess_titlepage.py <index.html> <lang>")
    path, lang = sys.argv[1], sys.argv[2]
    if lang not in SUBTITLES:
        sys.exit(f"postprocess_titlepage.py: unknown language '{lang}'")
    with open(path, encoding="utf-8") as f:
        html = f.read()

    marker = "<body>"
    if marker not in html:
        sys.exit(f"postprocess_titlepage.py: no <body> tag found in {path}")
    if 'class="cover-title-page"' in html:
        print(f"postprocess_titlepage.py: title page already present in {path}, skipping")
        return

    # Absolute file:// path, not a relative one: the PDF pipeline (docs/build.sh)
    # runs WeasyPrint on a *copy* of this file dumped into a different temp
    # directory by Chrome --dump-dom, so a relative "logos/ARIANE.svg" path
    # would resolve against the wrong base directory and silently fail to load.
    logo_abs = os.path.join(os.path.dirname(os.path.abspath(path)), "logos", "ARIANE.svg")
    title_page = TITLE_PAGE_TEMPLATE.replace("__LOGO_PATH__", "file://" + logo_abs)
    title_page = title_page.replace("__SUBTITLE__", SUBTITLES[lang])

    html = html.replace(marker, marker + "\n" + title_page, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_titlepage.py: title page inserted into {path}")


if __name__ == "__main__":
    main()
