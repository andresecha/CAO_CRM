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

`CAO_CRM-1.0.rdf` only formally `owl:imports` SKOS. The CIDOC-CRM 7.1.3 / LRMoo 1.1.1 / CRMdig classes and properties it reuses are carried inline, with their original axioms preserved (`rdfs:label` in up to 7 languages, `rdfs:comment` scope notes, domains and ranges) — the module is a bounded, self-contained composition, not an `owl:imports`-based extension. The deep checks in the pipeline nevertheless need the base ontologies' **full axiomatization** — the complete class/property hierarchy above what the module retains, and every official restriction: consistency and conformance verification must run against the *complete* CIDOC-CRM/LRMoo/CRMdig model, not just the fragment the module carries — see `validation/02-reasoning` and `validation/06-conformance`. That is what the vendored copies below are for.

## What goes here (fetched by `fetch.sh`, not committed as binaries)

- `vendor/cidoc-crm-7.1.3.rdf` — official CIDOC-CRM RDFS/OWL release matching the version cited in `CAO_CRM-1.0.rdf`'s `owl:versionInfo` ("CIDOC-CRM : RDFs Implementation (February 2024) of CIDOC-CRM 7.1.3").
- `vendor/lrmoo-1.1.1.rdf` — LRMoo 1.1.1 (November 2025).
- `vendor/crmdig-5.0.rdf` — CRMdig 5.0 (October 2025).
- `vendor/skos.rdf` — SKOS core (already formally imported).

Pin exact versions — do not silently pull "latest", since CAO_CRM's `owl:versionInfo` annotations name specific releases and a newer upstream release could introduce breaking axiom changes invisible to this repo's tests.

## fetch.sh

Downloads the pinned files into `vendor/` and records a SHA-256 checksum in `vendor/CHECKSUMS.txt` so drift is detectable. The source URLs (CIDOC-CRM SIG at cidoc-crm.org, LRMoo and CRMdig served from cidoc-crm.org's own `/extensions/` paths, SKOS from w3.org) live in `fetch.sh` itself; `make validate`/`make reason`/`make conformance` all depend on it running successfully.

## merge.sh

Merges `CAO_CRM-1.0.rdf` with everything in `vendor/` into `merged.ttl`, the input every reasoning/conformance check in `validation/02-reasoning` and `validation/06-conformance` actually runs against.
