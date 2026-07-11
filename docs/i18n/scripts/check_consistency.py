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
"""Flag terminology drift across translations/*.yaml: for every crosswalk
concept whose English key actually appears (whole-word, case-insensitive) in
a term's official English label/comment, verify that the crosswalk's
expected fr/es translation appears somewhere in that term's translated
label+comment. Cross-referencing against the real English source (via
term_inventory.json) avoids the false positives of a plain substring search
across the translated text alone.

This is a heuristic aid for human review, not a build gate.

Usage: python3 check_consistency.py <translations-dir> <glossary_crosswalk.yaml> <term_inventory.json>
"""
import glob
import os
import re
import sys

import yaml


def whole_word(term: str, text: str) -> bool:
    return re.search(r"\b" + re.escape(term) + r"\b", text, re.IGNORECASE) is not None


def main():
    if len(sys.argv) != 4:
        sys.exit("usage: check_consistency.py <translations-dir> <glossary_crosswalk.yaml> <term_inventory.json>")
    tdir, crosswalk_path, inventory_path = sys.argv[1], sys.argv[2], sys.argv[3]

    with open(crosswalk_path, encoding="utf-8") as f:
        crosswalk = yaml.safe_load(f)
    concepts = crosswalk.get("concepts", {})

    import json
    with open(inventory_path, encoding="utf-8") as f:
        inventory = {t["iri"]: t for t in json.load(f)}

    findings = []

    for yml_path in sorted(glob.glob(os.path.join(tdir, "*.yaml"))):
        with open(yml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        base = os.path.basename(yml_path)
        for entry in data.get("terms", []):
            iri = entry["iri"]
            inv = inventory.get(iri)
            if not inv:
                continue
            en_source = f"{inv.get('label_en', '')} {inv.get('comment_en', '')}"

            for lang in ("fr", "es"):
                translated = f"{entry.get('label', {}).get(lang, '')} {entry.get('comment', {}).get(lang, '')}"
                if not translated.strip():
                    continue
                for concept, translations in concepts.items():
                    if not whole_word(concept, en_source):
                        continue
                    expected = translations.get(lang, {}).get("text")
                    if not expected:
                        continue
                    if expected.lower() not in translated.lower():
                        findings.append(
                            f"[{lang}] {base}:{entry.get('local_name', iri)} -- EN source mentions "
                            f"'{concept}' but translation doesn't contain expected '{expected}'"
                        )

    if not findings:
        print("check_consistency.py: no terminology drift detected against the crosswalk.")
    else:
        for line in findings:
            print(line)
        print(f"\ncheck_consistency.py: {len(findings)} finding(s) to review (heuristic, may include false positives e.g. when a concept is legitimately paraphrased or omitted).")


if __name__ == "__main__":
    main()
