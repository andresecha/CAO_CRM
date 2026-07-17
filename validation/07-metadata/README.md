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
# 07 — Versioning & provenance metadata

**Checks:** required annotation properties are present on the ontology header (`owl:Ontology` node), per common publishing checklists (W3C best practice, DCAT, VANN).

**Required (checked by `check.sh`):**
- `owl:versionIRI` — present (`https://www.cao-crm.eu/ontology/1.0`).
- `dc:creator` and/or `dc:description` — present.
- `dc:rights` / license — present (`CC BY-NC-SA 4.0`).
- `owl:versionInfo` — present for the ontology itself and its dependencies.

The header additionally carries the full publication metadata set (`dcterms:created`, `dcterms:issued`, `dcterms:publisher`, `dcterms:source`, `dcterms:identifier` with the ontology's Nakala DOI, `dcterms:bibliographicCitation`, `vann:preferredNamespacePrefix`/`vann:preferredNamespaceUri`, `mod:status`) — assessed by the FAIR category, see `validation/08-fair/README.md`.

**Known, accepted design choice (not a defect):**
- No `owl:imports` for CIDOC-CRM/LRMoo/CRMdig: CAO_CRM is a bounded, ROBOT-extracted, "vendored" composition rather than an `owl:imports`-based extension (see section 3 of the main `README.md`).

**Run:**
```bash
bash check.sh ../../ontology/CAO_CRM-1.0.rdf
```

**Pass criteria:** every check in `check.sparql` returns its expected boolean (each query is preceded by a `# expect: true|false` directive — most require presence, the three "regression" queries below require *absence*).

## Current state: PASS 7/7

All four required-presence checks pass, and all three header-purity checks correctly return false: the three `ASK` queries at the bottom of `check.sparql` verify that the ontology header carries only CAO_CRM's own metadata — never header metadata from any of the composed sources (a risk inherent to any workflow that flattens imports into a single file). Don't relax them.
