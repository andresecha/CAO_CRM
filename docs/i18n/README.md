<!--
CAO_CRM (Corpus Author Ontology CRM)
Copyright (c) 2026 Andres Echavarria Pelaez
Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)
Encoding carried out under the scientific direction and support of Fatiha Idmhand

This file is part of the CAO_CRM publication package, licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License (CC BY-NC-SA 4.0). To view a copy of this license, visit
https://creativecommons.org/licenses/by-nc-sa/4.0/
-->
# Documentation translation overlay (i18n)

CIDOC-CRM only ever translates `rdfs:label` -- never `rdfs:comment`, in any
language, not even for its own native terms (verified empirically against
`ontology/CAO_CRM-1.0.rdf`: e.g. `E39_Actor` has `label@fr` but `comment`
only in `@en`). LRMoo and CRMdig translate nothing at all outside English.
This means the generated documentation would otherwise show English-only
definitions everywhere, and English-only labels for every LRMoo/CRMdig term,
regardless of which language a reader selected.

**This directory is not part of the official CIDOC-CRM/LRMoo/CRMdig sources.**
It supplies working French and Spanish labels and definitions, produced by
the CAO_CRM team, for exactly the gaps described above. It is merged into a
*temporary* copy of the ontology only when generating the human-readable
documentation (`docs/build.sh`) -- `ontology/CAO_CRM-1.0.rdf` itself is never
touched, staying an exact, unmodified extraction from the official sources
(see the "pure composition" principle in `docs/intro.html`'s Design
Rationale). In the generated HTML, every label or definition that came from
this overlay carries a small dagger (†) with a tooltip saying so.

## Layout

- `translations/*.yaml` -- the actual translations, grouped by conceptual
  batch (e.g. the LRMoo Work→Item chain, CRMdig digital objects, the P14
  role subproperties) rather than alphabetically, so related terms were
  translated together with maximum shared context.
- `glossary_crosswalk.yaml` -- the ~35 recurring CIDOC-CRM concept-words
  (Actor, Activity, Physical Thing...) with their fr/es translation fixed
  once, so every batch reuses the same word instead of drifting.
- `term_inventory.json` -- generated snapshot of all 130 module terms and
  which official languages each one already has, used to plan/verify
  coverage.
- `CAO_CRM-1.0-i18n.ttl` -- the compiled overlay actually consumed by
  `docs/build.sh` (`rdfs:label`/`rdfs:comment` triples in `@fr`/`@es` only,
  same IRIs as the module). Regenerate after editing any `translations/*.yaml`
  with `scripts/compile_i18n_overlay.py`.
- `scripts/extract_inventory.py` -- rebuilds `term_inventory.json` from
  `ontology/CAO_CRM-1.0.rdf`.
- `scripts/compile_i18n_overlay.py` -- `translations/*.yaml` → `CAO_CRM-1.0-i18n.ttl`.
- `scripts/check_consistency.py` -- flags a recurring English term translated
  two different ways across `translations/*.yaml` (heuristic, cross-references
  `term_inventory.json` to avoid flagging unrelated uses of the same word;
  review its output, don't treat it as a hard gate).

## Regenerating after a translation edit

```bash
cd docs/i18n
python3 scripts/compile_i18n_overlay.py translations CAO_CRM-1.0-i18n.ttl
python3 scripts/check_consistency.py translations glossary_crosswalk.yaml term_inventory.json
cd ../..
bash docs/build.sh ontology/CAO_CRM-1.0.rdf
```

## Adding a new language

Add a new `translations/*.yaml` batch (or extend the existing ones) with a
`label`/`comment` entry for the new language code, add it to
`glossary_crosswalk.yaml`, add its tooltip text to `TOOLTIP` in
`docs/postprocess_i18n_marker.py`, and add the language to the `for lang in
en fr es` loops in `docs/build.sh` and its `config-<lang>.properties` /
`intro-<lang>.html` pair.
