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
# 03 — SHACL constraint validation

**Checks:** instance data (ABox graphs in `test-data/`) conforms to shape constraints derived from CAO_CRM's intended usage rules (cardinalities, required properties, datatype/range constraints) — this is the "closed-world" enforcement layer that complements OWL's open-world reasoning (see the W3C HCLS wiki, *FDA Therapeutic Area Ontologies -- Validation*, `https://www.w3.org/wiki/HCLS/ClinicalObservationsInteroperability/FDATherapeuticAreaOntologies/Validation`, for the closed-world-assumption rationale followed here and in `../../competency-questions/`).

**Tool:** [pySHACL](https://github.com/RDFLib/pySHACL) (`pip install pyshacl`, already in `requirements.txt`).

**Files:**
- `shapes.ttl` — SHACL shapes, one `sh:NodeShape` per CAO_CRM class that has usage constraints (e.g. every `E12_Production` must have exactly one `crm:P4_has_time-span`).
- `check.sh` — runs pySHACL against every file in `../../test-data/`.

**Run:**
```bash
bash check.sh
```

**Pass criteria:** `pyshacl` reports `Conformant: True` (0 violations) for every test-data graph. A shape with 0 matching data anywhere in `test-data/` is a smell — it means either the shape is dead or `test-data/` is missing coverage; note it explicitly rather than leaving it silent.
