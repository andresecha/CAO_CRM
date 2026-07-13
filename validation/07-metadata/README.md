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
- `owl:versionIRI` — present (`https://www.cao-crm.eu/ontology/1.0`, confirmed present; updated 2026-07-09 from the placeholder `http://www.CAO_CRM.org/ontology/1.0` once the real domain was acquired).
- `dc:creator` and/or `dc:description` — present.
- `dc:rights` / license — present (`CC BY-NC-SA 4.0`, confirmed present).
- `owl:versionInfo` — present for the ontology itself and its dependencies.

**Known, accepted limitations (not defects):**
- No explicit `dcterms:created` / `dcterms:modified` (dated timestamps) — only free-text version info (`owl:versionInfo`, `dcterms:description`). Would be a reasonable future addition, not required by any check currently in `check.sparql`.
- No `owl:imports` for CIDOC-CRM/LRMoo/CRMdig — a deliberate design choice, not an oversight: CAO_CRM is a bounded, ROBOT-extracted, "vendored" composition rather than an `owl:imports`-based extension (see section 3 of the main `README.md`).

**Run:**
```bash
bash check.sh ../../ontology/CAO_CRM-1.0.rdf
```

**Pass criteria:** every check in `check.sparql` returns its expected boolean (each query is preceded by a `# expect: true|false` directive — most require presence, the three "regression" queries below require *absence*).

## Current state (2026-07-08): PASS 7/7

All four required-presence checks pass, and all three regression checks (below) correctly return false.

**Resolved history:** early in development (2026-07-02), the ontology header at `http://www.CAO_CRM.org/ontology` was found to carry, verbatim, annotation properties copy-pasted from **at least six other ontologies' own headers** (SKOS, CIDOC-CRM, CRMdig, LRMoo, CRMsci, CRMinf) — an artifact of how imports were flattened during an early Protégé export. Concretely: `terms:title` read `"SKOS Vocabulary"@en`, `terms:creator`/`terms:contributor` were attributed to SKOS's actual authors, and a ~200-line `rdfs:comment` was literally CIDOC-CRM's own release notes. This was fixed during the module's reconstruction as a pure, bounded composition (see `decisions/fr/informe-implementacion-RDF-modulo-acotado.md`), and the three regression `ASK` queries at the bottom of `check.sparql` exist specifically to catch any recurrence of this exact bug — don't relax them.
