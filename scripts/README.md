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
# scripts/ — repository-wide utility scripts

Cross-cutting scripts invoked from the repo root (by the `Makefile`, by CI, or by hand) that don't
belong to a single validation category or a single documentation build. Category-specific scripts
(the eight validation checks, the i18n overlay compiler, the Widoco build) live next to what they
operate on instead — see `validation/<category>/check.sh`, `docs/i18n/scripts/`, `docs/build.sh`.

| Script | What it does | Invoked by |
|---|---|---|
| `install-tools.sh` | Downloads ROBOT and Apache Jena locally (no `sudo`, no system-wide install) into `.tools/`, used by every validation category that shells out to either tool. | `make validate` (first step), CI (`validate.yml`) |
| `run-competency-questions.sh` | Runs the 5 competency questions + 2 cardinality checks (`sparql/ask/`, `sparql/select/`) against `test-data/stendhal-le-rouge-et-le-noir.ttl` and reports pass/fail per query. | `make cq` |
| `check-watermark.sh` | Verifies every authored source file carries the copyright/attribution header shown at the top of this file; `--fix` inserts it where missing. Guards against files added or regenerated without the header — some tools silently drop comments when they rewrite a file. | `make validate` (`watermark` step), CI |
| `reserialize-ontology.py` | Regenerates `ontology/CAO_CRM-1.0.{ttl,nt,jsonld}` from `ontology/CAO_CRM-1.0.rdf`, reinserting the copyright header that `rdflib` silently drops on every parse+serialize round trip (comments aren't part of the RDF data model, so a plain `g.parse(...); g.serialize(...)` strips it). Run this after any manual edit to the canonical `.rdf`, before committing the derived serializations. | Run manually after editing `ontology/CAO_CRM-1.0.rdf` |
