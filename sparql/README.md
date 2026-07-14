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
# sparql/ — competency questions as executable queries

The 5 competency questions and 2 cardinality checks from
`competency-questions/CQ-001-a-005-stendhal.md`, translated into real SPARQL following the W3C
HCLS *Compiling to SPARQL* methodology — one query per question, run against the real (not
synthetic) instance graph `test-data/stendhal-le-rouge-et-le-noir.ttl`.

`select/` holds the competency questions proper (open-ended lookups); `ask/` holds the boolean
cardinality checks. This split mirrors the two SPARQL query forms, not a difference in status or
importance.

| File | Question |
|---|---|
| `select/CQ1-autor-original.rq` | Who is the original author of work X? |
| `select/CQ2-lengua-expresion.rq` | What language is expression X in? |
| `select/CQ3-localizacion-ejemplar.rq` | Where is item X physically located? |
| `select/CQ4-derechos-edicion-digital.rq` | Who holds the rights to the digital edition of X? |
| `ask/CHECK-obra-tiene-un-unico-autor.rq` | Does the work have exactly one original author recorded? (cardinality check) |
| `ask/CHECK-manifestation-tiene-editor-cientifico.rq` | Does the manifestation have a scientific editor recorded? (cardinality check) |
| `ask/CQ5-digitalizado-vs-nato-digital.rq` | Is item X a digitization of a physical original, or born-digital? |

**Run:** `make cq` (invokes `scripts/run-competency-questions.sh`, which runs every query in both
folders against `test-data/stendhal-le-rouge-et-le-noir.ttl` and reports pass/fail per query).

**Pass criteria:** every `select/` query returns at least one binding; every `ask/` query returns
`true`. See `test-data/PROVENANCE-stendhal-verificacion.md` for how the instance graph itself was
verified against its primary sources before being trusted as a test fixture.
