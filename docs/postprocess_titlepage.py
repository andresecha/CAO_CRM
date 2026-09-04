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
import base64
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
    # This subtitle was the one piece of front-matter prose left out of the
    # Romanian review of 2026-09-01 (which covered the acknowledgments, the
    # introduction, the abstract, the description and the 130 glossary terms), so
    # it reused the English sentence for as long as the page carried Widoco's
    # English chrome anyway. It goes out for review together with the interface
    # strings, as the `subtitle` entry of i18n/chrome-ro.yaml -- keep the two in
    # sync, along with the identical line in the ro entry of the landing page in
    # docs/build.sh.
    "ro": (
        "Un cadru semantic dezvoltat de grupul de lucru &bdquo;Metadate&rdquo; al "
        "Consor&#539;iului-HN ARIANE pentru a structura organizarea, descrierea &#537;i "
        "interoperabilitatea metadatelor care descriu corpusurile textuale"
    ),
    # Portuguese: this sentence was NOT part of the review Ana Salgado returned
    # (that covered the acknowledgments, the introduction, the abstract, the
    # description and the glossary). It is composed here out of her own reviewed
    # vocabulary -- "Cons&oacute;rcio", "corpora", "metadados", the «Metadados»
    # working-group name -- so it does not clash with the rest of the page, but it
    # has not itself been checked by a native speaker. Confirm it with her before
    # treating the Portuguese cover page as final.
    "pt": (
        "Um quadro sem&acirc;ntico desenvolvido pelo grupo de trabalho "
        "&laquo;Metadados&raquo; do Cons&oacute;rcio-HN ARIANE para estruturar a "
        "organiza&ccedil;&atilde;o, a descri&ccedil;&atilde;o e a interoperabilidade dos "
        "metadados que descrevem os corpora textuais"
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

    # The logo is embedded as a data: URI rather than linked by path, because no
    # path works in every place this markup has to render:
    #   - a relative "logos/ARIANE.svg" breaks the PDF. The pipeline in
    #     docs/build.sh runs WeasyPrint on a *copy* of this file that Chrome
    #     --dump-dom writes into a temp directory, so the relative path would
    #     resolve against the wrong base directory and silently load nothing.
    #   - an absolute "file:///.../docs/site/logos/ARIANE.svg" fixes the PDF but
    #     bakes the build machine's own filesystem path into a file that is then
    #     committed, published on the web, and deposited on Nakala as a citable
    #     artifact -- where it identifies the person who ran the build and
    #     resolves on no other machine.
    # A data: URI carries no path at all, so it renders identically in the
    # browser, in the temp copy WeasyPrint reads, and in any downstream copy.
    # (The one cost is ~13 KB per page; the external stylesheets are unaffected
    # -- they are media="screen", so the PDF never used them either way.)
    logo_path = os.path.join(os.path.dirname(os.path.abspath(path)), "logos", "ARIANE.svg")
    with open(logo_path, "rb") as f:
        logo_uri = "data:image/svg+xml;base64," + base64.b64encode(f.read()).decode("ascii")
    title_page = TITLE_PAGE_TEMPLATE.replace("__LOGO_PATH__", logo_uri)
    title_page = title_page.replace("__SUBTITLE__", SUBTITLES[lang])

    html = html.replace(marker, marker + "\n" + title_page, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"postprocess_titlepage.py: title page inserted into {path}")


if __name__ == "__main__":
    main()
