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
# 05 — Structural metrics & profile validation

**Checks:** OWL 2 DL profile compliance (or documents which OWL 2 sub-language CAO_CRM actually needs), plus structural metrics (class/property counts, max depth, annotation coverage).

**Tool:** ROBOT `report` (built-in rule set covering ~40 structural checks: missing labels, duplicate labels, deprecated-but-referenced entities, etc.) and ROBOT `validate-profile`.

**Run:**
```bash
bash check.sh ../../ontology/CAO_CRM-1.0.rdf
```

**Pass criteria:** `robot report` (with the curated profile below) produces 0 ERROR-level violations (WARN-level are advisory, list any accepted ones below). `robot validate-profile --profile DL` either passes or the failure reason is documented (e.g. if CAO_CRM intentionally uses OWL Full constructs inherited from CIDOC-CRM).

## Curated report profile (`report_profile.tsv`)

First run against the real ontology (2026-07-01) produced 455 ERROR-level violations under ROBOT's stock profile.

| Rule | Default level | Curated level | Why |
|---|---|---|---|
| `multiple_labels` | ERROR | **WARN** | Fires on every CIDOC-CRM class/property inlined into CAO_CRM with 7 language-tagged `rdfs:label`s each (`de/en/fr/pt/el/ru/zh`) — correct, deliberate multilingual documentation, not a defect. Demoted to advisory rather than silenced, so a genuine same-language duplicate would still show up in the report for manual review. |
| `missing_definition` | WARN | ~~ERROR~~ → **WARN (reverted 2026-07-03)** | Originally escalated when CAO_CRM had 8 native datatype properties (`Title`, `Name`, `Identifier`...) that genuinely lacked documentation. Those properties no longer exist (see `decisions/` — CAO_CRM was rebuilt as a pure bounded composition of CIDOC-CRM/LRMoo/CRMdig, zero native properties). Kept at ERROR it would now misfire on ~95 entities that **are** documented, because ROBOT's `missing_definition` rule checks specifically for the OBO Foundry annotation property `IAO:0000115` — an annotation CIDOC-CRM/LRMoo/CRMdig never use (they document via plain `rdfs:comment`, which almost every entity in the module has). Reverted to ROBOT's default WARN since the rule doesn't match this ontology family's documentation convention and the original justification no longer applies. |
| `duplicate_label` | ERROR | **WARN (2026-07-07)** | See "Accepted findings" below — 44/44 occurrences verified inherited verbatim from the official CIDOC-CRM/LRMoo releases, none introduced by CAO_CRM. Demoted following the exact same remedy the OBO Operations Committee itself requested from the ROBOT maintainers for this rule when it fires on imported/cross-ontology content (see citation below) — not a project-specific exception. |

Everything else (`missing_label`, `missing_ontology_title`, `missing_ontology_license`, `missing_ontology_description`, etc.) is untouched from ROBOT's stock defaults — diff `report_profile.tsv` against a fresh copy of ROBOT's default profile any time to confirm nothing else drifted.

## Accepted findings

- **`duplicate_label` (44 occurrences as of 2026-07-07, demoted to WARN):** several LRMoo/CIDOC-CRM property pairs share identical label text in one or more languages — e.g. `P106_is_composed_of` / `P46_is_composed_of` both mean "is composed of" in Chinese/Russian, `P45_consists_of` / `P86i_contains` share the Chinese label "包含", `R16_created`/`R17_created`/`R24_created` (LRMoo) all use plain "created" in English, and `R28i_was_produced_by` (LRMoo) shares "was produced by" with its own CIDOC-CRM superproperty `P108i_was_produced_by` (`R28i rdfs:subPropertyOf P108i` — LRMoo deliberately reuses its parent's exact English verb for specialized subproperties). Verified character-for-character against `imports/vendor/cidoc-crm-7.1.3.rdf` and `lrmoo-1.1.1.rdf` for a representative sample, and confirmed none of the 19 affected subjects is a CAO_CRM-declared term (`P14_has_*`) — 100% inherited, 0% introduced by this project's extraction.

  This is not a CAO_CRM-specific rationalization: the **OBO Operations Committee** raised this exact class of false positive with the ROBOT maintainers ([ontodev/robot#429](https://github.com/ontodev/robot/issues/429)), explicitly flagging that `duplicate_label` "produces false positives when checking imported or cross-ontology content" and requesting adjustments (excluding blank nodes, distinguishing "technical violations" from "principle violations"). [ROBOT's own documentation](http://robot.obolibrary.org/report.html) confirms the standard, sanctioned remedy for exactly this situation is a custom `--profile` demoting the rule's severity — which is what `report_profile.tsv` now does. Demoted to WARN rather than silenced entirely, so a genuine same-language duplicate introduced by a future edit would still surface in the report for manual review.
- **`missing_ontology_title` / `missing_ontology_license` (2026-07-03, now resolved):** CAO_CRM's own header was missing `dc:title` and `dc:license` specifically (it had `dc:description`/`dc:rights`, which are different DC properties from what this rule checks). Added `dc:title = "CAO_CRM (Corpus Author Ontology CRM)"@en` and `dc:license = <https://creativecommons.org/licenses/by-nc-sa/4.0/>` to the header.
