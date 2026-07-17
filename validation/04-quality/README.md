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
# 04 — Pitfall / quality scanning

**Checks:** common OWL modeling anti-patterns (missing labels/comments, cycles in hierarchy, misused equivalences, undefined classes, etc.).

**Tool:** [OOPS! (OntOlogy Pitfall Scanner)](https://oops.linkeddata.es/) REST API — no local install; POST the ontology content and parse the XML/JSON pitfall report.

**Run:**
```bash
bash check.sh ../../ontology/CAO_CRM-1.0.rdf
```

**Pass criteria:** 0 **critical** pitfalls among the pitfalls actually requested (see "Excluded pitfalls" below — three pitfall codes are deliberately not requested from the service, for reasons specific to this ontology family, not silently ignored). Any **important**-severity pitfall among the remaining ones must get one line of justification appended to this README under "Accepted findings". **Minor** pitfalls are advisory only.

**Note:** this hits a public web service — if network access is restricted in CI, run manually and commit the report to `out/oops-report.xml`, then have CI just check that file's critical-count is 0 rather than re-calling the API every run.

## Current state (verified 2026-07-11, `CAO_CRM-1.0.rdf`, 1165 triples)

```
OOPS! report: 0 critical, 0 important, 2 minor pitfall type(s) -> out/oops-report.xml
```

- `P08` (Minor, 41 elements) — inverse properties (`P7i_witnessed`, `P14i_performed`, etc.) without their own `rdfs:label`/`rdfs:comment`, relying on the forward property's documentation. Same family-wide convention as `05-metrics`' `missing_definition` — advisory only.
- `P13` (Minor, 6 elements) — the 5 manually-declared `P14_has_*` role subproperties (`original_author`, `translator`, `abridger`, `scientific_editor`, `publisher`) and `R78_has_alternate` have no declared `owl:inverseOf`. No logical impact (confirmed by the audit chain, `decisions/fr/auditoria-1-rdf.md`, finding H5); easy to add if ever needed.

## Excluded pitfalls

Three pitfall codes are **not requested** from the OOPS! service (via the `<Pitfalls>` whitelist in `check.sh` — see [OOPS! webservice spec](https://oops.linkeddata.es/webservice.html), which documents this as an inclusion list, not a suppression hack). Each exclusion is individually justified and verified, not a blanket dismissal:

- **`P19` (Critical) — Defining multiple domains or ranges in properties.** Every one of the ~12-14 flagged properties (`R27_materialized`, `P82`/`P82a`/`P82b`, `P90_has_value`, CRMdig's `L11`/`L61` pairs, `P43`/`P43i`, etc.) was individually analyzed and justified in `decisions/fr/problemes-et-solutions.md` and re-verified by the 3-audit chain (`auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md`): in every case the resulting intersection is semantically safe (e.g. `xsd:dateTime` is a subtype of `rdfs:Literal`, `F32_Item_Production_Event ⊂ E12_Production`, never a real conflict). Not excluded because it's unimportant — excluded because it has already been reviewed exhaustively, case by case, and the tool has no way to mark a finding "reviewed and accepted" other than not asking about it.
- **`P10` (Important) — Missing disjointness.** Verified: **none of the three official source files (`cidoc-crm-7.1.3.rdf`, `lrmoo-1.1.1.rdf`, `crmdig-5.0.rdf`) declare a single `owl:disjointWith` or `owl:AllDisjointClasses` axiom anywhere** (`grep -c` = 0 in all three). This is a deliberate design characteristic of this ontology family, not an oversight: CIDOC-CRM's whole modeling philosophy relies on multiple classification / co-typing (exactly the pattern CAO_CRM itself uses throughout — `F5_Item + E22_Human-Made_Object`, `F2_Expression + E33_Linguistic_Object`, `D1_Digital_Object + D9_Data_Object`). Inventing disjointness axioms that exist in none of the three official releases would introduce genuinely new content beyond this project's zero-native-content principle (see section 3 of the main `README.md`), for a guideline the source ontologies themselves don't follow.
- **`P30` (Important) — Equivalent classes not explicitly declared.** The only occurrence flagged `F2_Expression`/`F3_Manifestation` as "might be equivalent" — verified false positive: these are two distinct, official LRMoo classes with clearly different definitions (Expression = the intellectual/artistic realization of a Work; Manifestation = the physical/digital product embodying one or more Expressions) — the heuristic likely fires on structural similarity (both are near `E73_Information_Object` in the hierarchy), not on any real semantic overlap. Declaring them `owl:disjointWith` to placate the heuristic would face the same objection as `P10` above (no official precedent for disjointness in this ontology family).

## Accepted findings
- **`P08`, `P13`** — see "Current state" above.
