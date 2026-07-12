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
# imports/ — vendored base ontologies

`CAO_CRM-1.0.rdf` only formally `owl:imports` SKOS. It does carry inline, flattened copies of the CIDOC-CRM 7.1.3 / LRMoo 1.1.1 / CRMdig classes and properties it reuses (`rdfs:label` in 7 languages, `rdfs:comment` scope notes — apparently pasted in from Protégé at export time rather than kept as a live import), so it's not a bare-URI stub as originally assumed here. What's still missing without vendoring the real files: the base ontologies' **full axiomatization** — property domain/range restrictions beyond what CAO_CRM happened to copy, disjointness axioms, the complete class/property hierarchy above what CAO_CRM directly touched. Consistency and unsatisfiability checks against the *complete* CIDOC-CRM/LRMoo/CRMdig model (not just the fragment CAO_CRM inlined) still need the real files loaded alongside — see `validation/02-reasoning` and `validation/06-conformance`.

## What goes here (fetched by `fetch.sh`, not committed as binaries unless the team decides otherwise)

- `vendor/cidoc-crm-7.1.3.rdf` — official CIDOC-CRM RDFS/OWL release matching the version cited in `CAO_CRM-1.0.rdf`'s `owl:versionInfo` ("CIDOC-CRM : RDFs Implementation (February 2024) of CIDOC-CRM 7.1.3").
- `vendor/lrmoo-1.1.1.rdf` — LRMoo 1.1.1 (November 2025).
- `vendor/crmdig-5.0.rdf` — CRMdig 5.0 (October 2025).
- `vendor/skos.rdf` — SKOS core (already formally imported).

Pin exact versions — do not silently pull "latest", since CAO_CRM's `owl:versionInfo` annotations name specific releases and a newer upstream release could introduce breaking axiom changes invisible to this repo's tests.

## fetch.sh

Downloads the pinned files into `vendor/` and records a SHA-256 checksum in `vendor/CHECKSUMS.txt` so drift is detectable. The exact source URLs (CIDOC-CRM SIG at cidoc-crm.org, LRMoo and CRMdig also served from cidoc-crm.org's own `/extensions/` paths, SKOS from w3.org) are already filled in and verified working — see `fetch.sh` itself; `make validate`/`make reason`/`make conformance` all depend on it running successfully.

## merge.sh

Merges `CAO_CRM-1.0.rdf` with everything in `vendor/` into `merged.ttl`, the input every reasoning/conformance check in `validation/02-reasoning` and `validation/06-conformance` actually runs against.
