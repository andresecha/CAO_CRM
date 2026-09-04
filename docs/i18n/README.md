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
It supplies French, Spanish and Romanian labels and definitions, produced by
the CAO_CRM team, for exactly the gaps described above. It is merged into a
*temporary* copy of the ontology only when generating the human-readable
documentation (`docs/build.sh`) -- `ontology/CAO_CRM-1.0.rdf` itself is never
touched, staying an exact, unmodified extraction from the official sources
(see the "pure composition" principle in `docs/intro.html`'s Design
Rationale). In the generated HTML, every label or definition that came from
this overlay carries a small dagger (†) with a tooltip saying so.

## Layout

- `translations/*.yaml` -- the actual fr/es translations, grouped by conceptual
  batch (e.g. the LRMoo Work→Item chain, CRMdig digital objects, the P14
  role subproperties) rather than alphabetically, so related terms were
  translated together with maximum shared context.
- `translations-ro/*.yaml` -- the same 130 terms in Romanian, in the same eight
  batches. **Reviewed and corrected on 2026-09-01 by [Roxana Patras](https://dhl.uaic.ro/taqwa/elementor-page-2114/members-2/)**
  (Universitatea „Alexandru Ioan Cuza”, Iaşi, Romania), a native speaker: 34 labels
  and 88 definitions corrected, and 6 entries of `glossary_crosswalk-ro.yaml` settled
  (they carry `source: native_review`). The corrected document she returned is
  archived in `review/review2-ro.md`. She is credited as a co-author of the Nakala
  deposit of this layer for it.

- `translations-pt/*.yaml` -- the same terms in Portuguese. **Reviewed and
  corrected on 2026-09-04 by Ana Salgado**, a native speaker of European
  Portuguese: 20 definitions corrected, plus the acknowledgments, the
  introduction and the abstract/description. No label changed, and
  `check_consistency.py` reports no drift, so no crosswalk entry needed
  overriding. The corrected document she returned is archived in
  `review/review-pt.md`. She is credited as a co-author of the Nakala deposit of
  this layer for it. Note this layer is smaller than the ro/it ones: CIDOC-CRM
  publishes an official Portuguese label for 76 of the 130 terms, so the overlay
  supplies only the remaining 54 labels, plus the 89 definitions (no source
  translates those in any language).
- `translations-it/` -- Italian draft, not yet reviewed, not wired into
  `docs/build.sh`, gitignored. See `docs/prompts/RETOMAR-it-publicacion.md`.
- `glossary_crosswalk.yaml`, `glossary_crosswalk-ro.yaml`,
  `glossary_crosswalk-pt.yaml` -- the ~35 recurring
  CIDOC-CRM concept-words (Actor, Activity, Physical Thing...) with their
  translation fixed once per language, so every batch reuses the same word
  instead of drifting. Entries the native review overrode are marked
  `source: native_review`.
- `term_inventory.json` -- generated snapshot of all 130 module terms and
  which official languages each one already has, used to plan/verify
  coverage.
- `CAO_CRM-1.0-i18n.ttl`, `CAO_CRM-1.0-i18n-ro.ttl` -- the compiled overlays
  actually consumed by `docs/build.sh` (`rdfs:label`/`rdfs:comment` triples in
  `@fr`/`@es` and `@ro` respectively, same IRIs as the module). Regenerate after
  editing any `translations*/*.yaml` with `scripts/compile_i18n_overlay.py`.
- `scripts/extract_inventory.py` -- rebuilds `term_inventory.json` from
  `ontology/CAO_CRM-1.0.rdf`.
- `scripts/compile_i18n_overlay.py` -- `translations*/*.yaml` → the matching
  `.ttl` overlay. Takes the language codes as trailing arguments (defaults to
  `fr es` when omitted).
- `scripts/check_consistency.py` -- flags a recurring English term translated
  two different ways across a `translations*/` directory (heuristic,
  cross-references `term_inventory.json` to avoid flagging unrelated uses of
  the same word; review its output, don't treat it as a hard gate).
- `scripts/build_review_doc.py` + `scripts/prepend_review_frontmatter.py` --
  produce a single `review/review-<lang>.md` for a native speaker to correct in
  place: English source, French reference, and the target language, for the
  acknowledgments, the introduction, the abstract/description, and all 130
  terms. There is no automated path back: a returned document is reintegrated
  into the four sources it came from by hand (see "Where a review lands" below).

## Regenerating after a translation edit

```bash
cd docs/i18n
python3 scripts/compile_i18n_overlay.py translations CAO_CRM-1.0-i18n.ttl
python3 scripts/check_consistency.py translations glossary_crosswalk.yaml term_inventory.json
# Romanian:
python3 scripts/compile_i18n_overlay.py translations-ro CAO_CRM-1.0-i18n-ro.ttl ro
python3 scripts/check_consistency.py translations-ro glossary_crosswalk-ro.yaml term_inventory.json
cd ../..
bash docs/build.sh ontology/CAO_CRM-1.0.rdf
```

## Where a review lands

A returned `review/review-<lang>.md` maps back onto exactly four places, one
per section of the document:

| Section | Destination |
|---|---|
| A. Acknowledgments | `PARAGRAPHS[<lang>]` in `docs/postprocess_acknowledgments.py` |
| B. Introduction / Status of this document | `docs/intro-<lang>.html` |
| C. Abstract & description | `abstract=` / `description=` in `docs/config-<lang>.properties` |
| D. Term-by-term glossary | `label`/`comment` in `translations-<lang>/*.yaml` |

Re-running `build_review_doc.py` + `prepend_review_frontmatter.py` after
reintegration should reproduce the corrected document exactly; that round trip
is the cheapest way to prove nothing was dropped. A label the review changed
usually also needs its `glossary_crosswalk-<lang>.yaml` entry updated, or
`check_consistency.py` will report drift on the next run.

## Adding a new language

Add a `translations-<lang>/` directory (or extend the existing batches) with a
`label`/`comment` entry for the new language code, add a
`glossary_crosswalk-<lang>.yaml`, compile its overlay, add its tooltip text to
`TOOLTIP` in `docs/postprocess_i18n_marker.py` and its cover-page subtitle to
`SUBTITLES` in `docs/postprocess_titlepage.py`, write its
`config-<lang>.properties` / `intro-<lang>.html` pair, and add the code to the
`LANGS` variable in `docs/build.sh`. If Widoco ships no bundle for that
language (check for `<lang>.properties` inside `docs/.tools/widoco.jar`), the
page will come out with an English frame -- see the Romanian section of
`docs/README.md` for what that implies, in particular for `ANCHORS` in
`docs/postprocess_acknowledgments.py`.
