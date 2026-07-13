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
"""Prepend Acknowledgments / Introduction / Description review sections
(EN source, FR reference, target language to correct) to a term-level
review-<lang>.md already produced by build_review_doc.py.

Usage: python3 prepend_review_frontmatter.py <lang> <review.md>
"""
import re
import sys
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

LANG_NAMES = {"ro": "Romanian", "it": "Italian", "pt": "Portuguese"}

# Acknowledgments paragraphs -- copied from docs/postprocess_acknowledgments.py's
# PARAGRAPHS dict (kept as plain strings here to avoid importing that module).
sys.path.insert(0, os.path.join(ROOT, "docs"))
from postprocess_acknowledgments import PARAGRAPHS  # noqa: E402


def read_intro_paragraph(lang_file):
    path = os.path.join(ROOT, "docs", lang_file)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.search(r'<h2 id="status">.*?</h2>\s*<span class="markdown">\s*\n\s*\n(.*?)\n\n', text, re.S)
    return m.group(1).strip() if m else "*(not found)*"


def read_config_field(config_file, field):
    path = os.path.join(ROOT, "docs", config_file)
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith(field + "="):
                return line[len(field) + 1:].strip()
    return "*(not found)*"


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: prepend_review_frontmatter.py <lang> <review.md>")
    lang, review_path = sys.argv[1], sys.argv[2]
    if lang not in LANG_NAMES:
        sys.exit(f"unknown lang '{lang}'")

    intro_en = read_intro_paragraph("intro-en.html")
    intro_fr = read_intro_paragraph("intro.html")
    intro_tgt = read_intro_paragraph(f"intro-{lang}.html")

    abstract_en = read_config_field("config-en.properties", "abstract")
    abstract_fr = read_config_field("config-fr.properties", "abstract")
    abstract_tgt = read_config_field(f"config-{lang}.properties", "abstract")

    desc_en = read_config_field("config-en.properties", "description")
    desc_fr = read_config_field("config-fr.properties", "description")
    desc_tgt = read_config_field(f"config-{lang}.properties", "description")

    ack_en = PARAGRAPHS["en"]
    ack_fr = PARAGRAPHS["fr"]
    ack_tgt = PARAGRAPHS[lang]

    lines = []
    lines.append("## A. Acknowledgments (docs/postprocess_acknowledgments.py)\n")
    lines.append("**English (source)**")
    for p in ack_en:
        lines.append(f"> {p}")
    lines.append("\n**Français (reference, working translation)**")
    for p in ack_fr:
        lines.append(f"> {p}")
    lines.append(f"\n**{LANG_NAMES[lang]} — PLEASE REVIEW / CORRECT BELOW**")
    for p in ack_tgt:
        lines.append(f"> {p}")

    lines.append("\n---\n")
    lines.append("## B. Introduction (docs/intro-*.html, \"Status of this document\")\n")
    lines.append("**English (source)**")
    lines.append(f"> {intro_en}")
    lines.append("\n**Français (reference)**")
    lines.append(f"> {intro_fr}")
    lines.append(f"\n**{LANG_NAMES[lang]} — PLEASE REVIEW / CORRECT BELOW**")
    lines.append(f"> {intro_tgt}")

    lines.append("\n---\n")
    lines.append("## C. Ontology abstract & description (docs/config-*.properties)\n")
    lines.append("**English (source) — abstract**")
    lines.append(f"> {abstract_en}")
    lines.append("\n**Français (reference) — abstract**")
    lines.append(f"> {abstract_fr}")
    lines.append(f"\n**{LANG_NAMES[lang]} — PLEASE REVIEW / CORRECT BELOW — abstract**")
    lines.append(f"> {abstract_tgt}")
    lines.append("\n**English (source) — description**")
    lines.append(f"> {desc_en}")
    lines.append("\n**Français (reference) — description**")
    lines.append(f"> {desc_fr}")
    lines.append(f"\n**{LANG_NAMES[lang]} — PLEASE REVIEW / CORRECT BELOW — description**")
    lines.append(f"> {desc_tgt}")

    lines.append("\n---\n")
    lines.append("## D. Term-by-term glossary (CIDOC-CRM / LRMoo / CRMdig classes and properties)\n")

    with open(review_path, encoding="utf-8") as f:
        existing = f.read()

    # existing starts with "# CAO_CRM -- ... translation review\n\n<intro paragraph>\n\n---\n\n"
    header_end = existing.find("\n---\n")
    header = existing[:header_end + len("\n---\n")]
    rest = existing[header_end + len("\n---\n"):]

    new_content = header + "\n" + "\n".join(lines) + "\n" + rest
    with open(review_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"prepend_review_frontmatter.py: sections A-D prepended to {review_path}")


if __name__ == "__main__":
    main()
