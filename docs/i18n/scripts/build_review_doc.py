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
"""Build a human-friendly Markdown review document for a working-translation
language (ro/it/pt): one block per CIDOC-CRM/LRMoo/CRMdig term, showing the
official English source (with a link to the live published English page, to
resolve any doubt), the French reference translation (official where it
exists, working translation otherwise), and the language under review, ready
to be corrected in place.

Usage: python3 build_review_doc.py <lang> <output.md>
"""
import glob
import json
import os
import sys

import rdflib
import yaml
from rdflib.namespace import RDFS

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
I18N = os.path.join(ROOT, "docs", "i18n")

LANG_NAMES = {"ro": "Romanian", "it": "Italian", "pt": "Portuguese"}


def load_translations(tdir):
    """iri -> {label: {lang: text}, comment: {lang: text}}"""
    out = {}
    for path in sorted(glob.glob(os.path.join(tdir, "*.yaml"))):
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        for entry in data.get("terms", []):
            out[entry["iri"]] = entry
    return out


def load_official_fr(rdf_path):
    """iri -> {label: text|None, comment: text|None}, official rdfs:label@fr / rdfs:comment@fr only."""
    g = rdflib.Graph()
    g.parse(rdf_path, format="xml")
    out = {}
    for s, p, o in g.triples((None, RDFS.label, None)):
        if getattr(o, "language", None) == "fr":
            out.setdefault(str(s), {})["label"] = str(o)
    for s, p, o in g.triples((None, RDFS.comment, None)):
        if getattr(o, "language", None) == "fr":
            out.setdefault(str(s), {})["comment"] = str(o)
    return out


def en_link(iri):
    return f"https://www.cao-crm.eu/index-en.html#{iri}"


def block(n, inv, official_fr, fr_working, target):
    iri = inv["iri"]
    local = inv["local_name"]
    family = inv["family"]
    kind = inv.get("kind", "")

    lbl_en = inv.get("label_en") or "*(none)*"
    cmt_en = inv.get("comment_en") or "*(no English definition exists for this term)*"

    off = official_fr.get(iri, {})
    fr_work = fr_working.get(iri, {})
    lbl_fr = off.get("label") or fr_work.get("label", {}).get("fr") or "*(no French label/reference available)*"
    cmt_fr = off.get("comment") or fr_work.get("comment", {}).get("fr") or "*(no French definition/reference available)*"
    fr_note = []
    if "label" in off:
        fr_note.append("label: official")
    elif fr_work.get("label", {}).get("fr"):
        fr_note.append("label: working translation")
    if "comment" in off:
        fr_note.append("comment: official")
    elif fr_work.get("comment", {}).get("fr"):
        fr_note.append("comment: working translation")
    fr_note_str = f" _({', '.join(fr_note)})_" if fr_note else ""

    tgt = target.get(iri, {})
    lbl_tgt = tgt.get("label", {}).get(list(tgt.get("label", {}).keys())[0]) if tgt.get("label") else None
    cmt_tgt = tgt.get("comment", {}).get(list(tgt.get("comment", {}).keys())[0]) if tgt.get("comment") else None
    # simpler: fetch by explicit lang key later; placeholder replaced by caller
    return {
        "n": n, "iri": iri, "local": local, "family": family, "kind": kind,
        "lbl_en": lbl_en, "cmt_en": cmt_en, "lbl_fr": lbl_fr, "cmt_fr": cmt_fr,
        "fr_note": fr_note_str,
    }


def main():
    if len(sys.argv) != 3:
        sys.exit("usage: build_review_doc.py <lang> <output.md>")
    lang, out_path = sys.argv[1], sys.argv[2]
    if lang not in LANG_NAMES:
        sys.exit(f"unknown lang '{lang}', expected one of {list(LANG_NAMES)}")

    with open(os.path.join(I18N, "term_inventory.json"), encoding="utf-8") as f:
        inventory = json.load(f)

    official_fr = load_official_fr(os.path.join(ROOT, "ontology", "CAO_CRM-1.0.rdf"))
    fr_working = load_translations(os.path.join(I18N, "translations"))
    target = load_translations(os.path.join(I18N, f"translations-{lang}"))

    lines = []
    lines.append(f"# CAO_CRM — {LANG_NAMES[lang]} translation review\n")
    lines.append(
        "For each term below: the **official English source** (with a link to the live "
        "published English documentation, in case anything looks wrong or unclear), the "
        f"**French reference** (official where CIDOC-CRM/LRMoo/CRMdig provide one, a working "
        f"translation otherwise), and the **{LANG_NAMES[lang]} working translation** to review "
        "and correct in place. Edit directly in this file; anything you change will be "
        "carried back into the project's translation files.\n"
    )
    lines.append("---\n")

    for i, inv in enumerate(inventory, 1):
        iri = inv["iri"]
        tgt = target.get(iri, {})
        has_label = bool(tgt.get("label", {}).get(lang))
        has_comment = bool(tgt.get("comment", {}).get(lang))
        if not has_label and not has_comment:
            continue  # nothing to review for this term in this language

        b = block(i, inv, official_fr, fr_working, target)
        lines.append(f"## {i}. `{inv['local_name']}` — {inv['family']} ({inv.get('kind', '')})\n")
        lines.append(f"[Consult the official English entry →]({en_link(iri)})\n")

        lines.append("**English (official source)**")
        lines.append(f"- Label: {b['lbl_en']}")
        lines.append(f"- Comment: {b['cmt_en']}\n")

        lines.append(f"**Français (reference){b['fr_note']}**")
        lines.append(f"- Label: {b['lbl_fr']}")
        lines.append(f"- Comment: {b['cmt_fr']}\n")

        lines.append(f"**{LANG_NAMES[lang]} — PLEASE REVIEW / CORRECT BELOW**")
        if has_label:
            lines.append(f"- Label: {tgt['label'][lang]}")
        else:
            lines.append("- Label: *(no official label existed in this language — not part of this review)*")
        if has_comment:
            lines.append(f"- Comment: {tgt['comment'][lang]}")
        else:
            lines.append("- Comment: *(not applicable — no English source definition for this term)*")
        lines.append("\n---\n")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    reviewed = sum(1 for inv in inventory if target.get(inv["iri"], {}).get("label", {}).get(lang) or target.get(inv["iri"], {}).get("comment", {}).get(lang))
    print(f"build_review_doc.py: {reviewed} terms written -> {out_path}")


if __name__ == "__main__":
    main()
