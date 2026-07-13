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
# competency-questions/ — contenido real

Siguiendo la metodología del wiki HCLS del W3C ("Compiling to SPARQL"), cada pregunta de competencia se
traduce en una consulta SPARQL `ASK`/`SELECT` ejecutada contra el grafo de instancia real en
`../test-data/stendhal-le-rouge-et-le-noir.ttl`.

**Estado (desde el 10 de julio de 2026):** `CQ-001-a-005-stendhal.md` recoge 5 preguntas de
competencia formales (autor original, lengua de la expresión, localización del ejemplar, derechos
de la edición digital, digitalizado vs. nato-digital) más 2 verificaciones de cardinalidad (una
manifestación debe tener editor científico o comercial; una obra tiene un único autor original),
cada una mapeada a su archivo `.rq` correspondiente en `../sparql/ask/` o `../sparql/select/`.
`make cq` (o `bash ../scripts/run-competency-questions.sh`) las ejecuta todas contra datos reales,
no como plantilla.
