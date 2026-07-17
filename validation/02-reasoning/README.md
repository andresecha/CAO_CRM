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
# 02 — Logical consistency & coherence

**Checks:** the merged graph (`imports/merged.ttl` = CAO_CRM + vendored CIDOC-CRM/LRMoo/CRMdig/SKOS) is logically consistent and has zero unsatisfiable classes, under a standard OWL DL reasoner.

**Tool:** [ROBOT](http://robot.obolibrary.org/) `reason` command, which wraps HermiT (default), ELK, or JFact. HermiT is the safest default for full OWL 2 DL; ELK is faster but only supports OWL 2 EL (won't be sufficient here given CIDOC-CRM's use of general class axioms).

**Run:**
```bash
bash check.sh ../../imports/merged.ttl
```

Internally: `.tools/robot reason --input merged.ttl --reasoner HermiT --output out/reasoned.ttl` plus `.tools/robot reason --input merged.ttl --reasoner HermiT -vv` for the human-readable unsatisfiable-class report.

**Pass criteria:**
- Reasoner reports the ontology as **consistent**.
- **Zero unsatisfiable classes** (`owl:Nothing` equivalents). If CIDOC-CRM/LRMoo/CRMdig axioms interact with a CAO_CRM addition to produce an unsatisfiable class, that is a modeling bug in CAO_CRM, not something to suppress.

**On failure:** `.tools/robot explain` (or Protégé's explanation feature) to get the minimal axiom set causing the inconsistency — do not just delete the failing class/axiom without understanding why.

## Current state: PASS — consistent, 0 unsatisfiable classes

`bash check.sh ../../imports/merged.ttl` reports the ontology as consistent, with zero unsatisfiable classes, merged against the three complete official sources (CIDOC-CRM 7.1.3, LRMoo 1.1.1, CRMdig 5.0) plus SKOS.
