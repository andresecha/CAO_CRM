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
# 06 — Conformance with CIDOC-CRM / LRMoo / CRMdig

**Checks:** CAO_CRM's extension (subclasses, new properties, restrictions) doesn't contradict or duplicate the base ontologies it builds on. This is not covered by generic reasoning — a merged graph can be *consistent* while still misusing base-ontology conventions (e.g. redefining an E-class's intended scope, using the wrong property direction).

**Method (no dedicated tool — this is manual review supported by scripted diffing):**
1. `robot diff --left imports/vendor/cidoc-crm-7.1.3.rdf --right imports/merged.ttl` — confirms CAO_CRM didn't accidentally redeclare/override any CIDOC-CRM axiom.
2. Manual check against CIDOC-CRM SIG numbering convention: new CAO_CRM classes/properties must NOT reuse an `E<n>`/`P<n>` identifier pattern reserved for CIDOC-CRM itself — CAO_CRM should mint its own namespace-local names (it does: `https://www.cao-crm.eu/ontology/...`).
3. For every CAO_CRM class that `rdfs:subClassOf` a CIDOC-CRM/LRMoo/CRMdig class, confirm the specialization is semantically narrower, not contradictory (spot-check against the official scope notes in the CIDOC-CRM/LRMoo/CRMdig definition documents).

**Run:**
```bash
bash check.sh ../../imports/merged.ttl
```

**Pass criteria:** `robot diff` shows only additions (no modified/removed base axioms); manual review notes recorded in `out/conformance-notes.md` for every new subclass relationship.

## Current state (2026-07-08): PASS (automated part)

`bash check.sh ../../imports/merged.ttl` reports no base-ontology axioms modified beyond the known-harmless `OntologyID`/`versionIRI` merge artifact (an unavoidable byproduct of merging several `owl:Ontology` headers into one file for the reasoner, not a real conflict). Manual review of every `rdfs:subClassOf` relationship against the official scope notes is recorded in `out/conformance-notes.md`.

**Resolved history:** the first run (2026-07-01) found `P3_has_note` declared as `owl:ObjectProperty` in an early draft, conflicting via punning with CIDOC-CRM's own untyped, datatype-oriented declaration (see `decisions/fr/problemes-et-solutions.md` (Problème 1) for the full resolution). Fixing this datatype mismatch also removed the resulting `robot diff`, which had previously shown 7 official CIDOC-CRM axioms dropped from the merged graph as a side effect.
