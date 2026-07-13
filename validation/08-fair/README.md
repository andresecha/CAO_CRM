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
# 08 — FAIR principles assessment

**Checks:** the ontology and its publication meet Findable / Accessible / Interoperable / Reusable criteria (FAIR for ontologies, not just data).

**Tool:** [FOOPS!](https://github.com/oeg-upm/fair_ontologies) (covers FAIR + reuses OOPS! pitfalls), run **locally** via its own released jar — not the public web form.

**Update (2026-07-10) — fixed and verified working end to end.** The public web form
(`https://foops.linkeddata.es/FAIR_validator.html`, aliased at `https://w3id.org/foops/`) never
exposed a documented, stable JSON REST contract to script against — the old `/FOOPS_service` guess
this script relied on was unverified and did not work. Instead, `check.sh` now downloads the
official release jar (`fair_ontologies-0.4.0.jar`, cached in `.tools/`, gitignored), runs it as a
local Spring Boot server, and calls its own real, documented endpoint (`POST
/assessOntologyFile`, multipart file upload — confirmed against the project's own README on
GitHub). Confirmed working against `ontology/CAO_CRM-1.0.rdf` on 2026-07-10: **overall score
0.55/1.0** (Findable 1/4, Interoperable 3/3, Reusable 2/8; Accessible not evaluated in file-upload
mode, which requires a dereferenceable public URI instead of a local file).

**Update (2026-07-10, same day) — header metadata completed, score raised to 0.79/1.0.** Every gap
FOOPS! could report as a simple missing metadata triple was closed directly in the ontology's own
header: `vann:preferredNamespacePrefix`, `vann:preferredNamespaceUri` (as an `xsd:anyURI` literal —
using `rdf:resource` here instead breaks ROBOT/OWLAPI parsing with a misleading
`OWLOntologyAlreadyExistsException` on the *merged* graph; verified and fixed the same day),
`dcterms:created`, `dcterms:publisher`, `dcterms:source`, `mod:status` and
`dcterms:bibliographicCitation`. Re-running `check.sh` afterward gives **Findable 3/4, Interoperable
3/3, Reusable 5/8 — overall 0.79/1.0**. `VOC3`/`VOC4` fail for a reason specific to CAO_CRM's
pure-composition design, not a real documentation gap: FOOPS! looks for terms declared under the
ontology's own namespace to check their labels/definitions, and CAO_CRM declares none of its own —
every class and property keeps its original CIDOC-CRM/LRMoo/CRMdig URI. The tool correctly reports
zero own terms to check; it isn't detecting a documentation gap.

**Checklist (manual for the criteria FOOPS! can't check from a file alone — hosting/publication decisions this repo doesn't fully control):**

| Principle | Requirement | Status |
|---|---|---|
| F1 | Globally unique, persistent identifier (IRI) | ⚠ partial — `https://www.cao-crm.eu/ontology/` resolves, but FOOPS!'s `PURL1` check confirms it does not follow a recognized persistent-identifier scheme (w3id, purl, DOI...); registering a `w3id.org` redirect would require migrating every published URI to that namespace — a breaking change deliberately deferred to a future major version, not a metadata fix. |
| F2 | Rich metadata (creator, description) | ✅ present, see `validation/07-metadata` |
| A1 | Retrievable by its identifier (content negotiation) | ⚠ partial — the namespace and versionIRI now resolve to a real, working page (`.github/workflows/pages.yml` places a copy of the site at `/ontology/` and `/ontology/1.0/`), but GitHub Pages serves static files only, with no `Accept`-header-based 303 redirect to RDF/Turtle/JSON-LD as recommended by https://www.w3.org/TR/swbp-vocab-pub/ — the same static landing page is returned regardless of the requester, with links out to every serialization. This is the documented, accepted fallback for vocabularies without dedicated server infrastructure (see `decisions/es/informe-requisitos-publicacion-CAO_CRM.md`, section 1); true content negotiation would need w3id.org or equivalent server-side infra, not pursued here. |
| I1 | Uses a formal, shared representation (OWL/RDF) | ✅ FOOPS! `RDF1` confirms |
| I2 | Uses vocabularies that follow FAIR (CIDOC-CRM, SKOS) | ✅ FOOPS! `VOC1`/`VOC2` confirm |
| R1 | Clear usage license | ✅ CC BY-NC-SA 4.0 — FOOPS! `OM4_1`/`OM4_2` confirm |
| R1.2 | Detailed provenance | ✅ **resolved 2026-07-10** — `dcterms:created` and `dcterms:publisher` added; FOOPS! `OM5_1`/`OM5_2` now pass |
| R1.3 | Detailed metadata (DOI, publisher, logo, status, source) | ⚠ partial — publisher/logo/status/source added (`OM3` no longer flags them); the DOI sub-check still fails, since the ontology itself has no DOI yet — expected to resolve automatically once this RDF is deposited as a Nakala dataset with its own DOI. |

**Run:**
```bash
bash check.sh ../../ontology/CAO_CRM-1.0.rdf
```

**Pass criteria:** FOOPS! report generated in `out/foops-report.json` with a real HTTP 200 response (the script now fails loudly, printing the server log, if it isn't); every ⬜/⚠ row above resolved or explicitly accepted with rationale before claiming "publishable".
