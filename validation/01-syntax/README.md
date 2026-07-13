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
# 01 — Syntax validation

**Checks:** the RDF/XML file is well-formed and parses cleanly under the RDF 1.1 spec.

**Tools:** `rapper` (raptor2-utils) as primary strict check, `riot` (Jena) as cross-check, Python `rdflib` as a third independent parser (belt-and-braces — different parsers catch different issues).

**Run:**
```bash
bash check.sh ../../ontology/CAO_CRM-1.0.rdf
```

**Pass criteria:** all three parsers report 0 errors and 0 warnings. Any warning must be resolved or explicitly justified below in a "Known exceptions" section (none yet).

**Output:** `out/rapper.log`, `out/riot.log`, `out/rdflib.log` (created on run, gitignored).
