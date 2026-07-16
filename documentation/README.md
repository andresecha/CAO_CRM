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
# documentation/ — pedagogical documentation (non-expert audience)

Ten sections written for readers who are **not** ontology experts — from "what is CAO_CRM" to a
glossary and application notes for the `P14_has_*` role properties and the `E55_Type` controlled
values used in the model. Each document exists in **French, Spanish and English**, with exactly
the same content: `fr/<file>`, `es/<file>`, `en/<file>`.

This is prose the CAO_CRM team itself wrote to explain the model — unlike `decisions/`, which
documents *why* a modeling choice was made, this documents *what the model is* for someone reading
it for the first time. It is compiled, together with the ontology's own metadata, into the
navigable HTML/PDF documentation under `docs/site/` (see `docs/README.md`).

| File | Content |
|---|---|
| `01-que-es-cao-crm.md` | What CAO_CRM is and what it's for |
| `02-cidoc-lrmoo-crmdig.md` | What CIDOC-CRM, LRMoo and CRMdig are, and why combine them |
| `03-jerarquia-ejemplo.md` | The F1→F2→F3→F5→D1 hierarchy, illustrated with a concrete example |
| `04-construccion-rdf.md` | How the RDF file was built, step by step |
| `05-decisiones-adr.md` | The modeling decisions explained in plain language (ADR-001 to 003 and related cases) |
| `06-pruebas-validacion.md` | What each validation test category checks |
| `07-guia-protege.md` | Practical guide to opening and exploring the model in Protégé |
| `08-glosario.md` | Glossary of technical terms |
| `09-faq-errores.md` | Frequently asked questions and real incidents encountered during construction |
| `10-notas-de-aplicacion.md` | Application notes (in the CIDOC-CRM sense) for the 5 `P14_has_*` role properties and the `E55_Type` controlled values used in the model, each with a concrete example |

File names are identical across the three language folders — kept in Spanish — so the same
relative path always resolves to the matching section regardless of language.

Terminology translations into Italian, Romanian and Portuguese are prepared as part of the
separate Nakala research-data collection; they cover the ontology's own terminology, not this
pedagogical documentation.
