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
# Preguntas de competencia (Competency Questions) — caso Stendhal

Cinco preguntas de competencia reales, formuladas antes de escribir las consultas SPARQL
correspondientes (siguiendo la metodología ORSD: primero la pregunta en lenguaje natural, después
su traducción formal).
Cada una se ejecuta contra `../test-data/stendhal-le-rouge-et-le-noir.ttl` mediante
`../scripts/run-competency-questions.sh`, siguiendo el patrón de "compilación a SPARQL" del wiki
HCLS del W3C (*FDA Therapeutic Area Ontologies -- Validation*,
`https://www.w3.org/wiki/HCLS/ClinicalObservationsInteroperability/FDATherapeuticAreaOntologies/Validation`):
las consultas `SELECT` responden preguntas de valor concreto; las consultas `ASK` verifican
restricciones de tipo cardinalidad/existencia bajo hipótesis de mundo cerrado (CWA), complementando
el razonamiento OWL de mundo abierto que ya hace `make reason`.

El grafo de prueba cubre dos casos reales encadenados a la misma obra: (1) la edición crítica
francesa de Henri Martineau (Le Divan, 1927), digitalizada por la BnF en Gallica; y (2) la
traducción inglesa de C. K. Scott Moncrieff (Modern Library, 1929), digitalizada por Internet
Archive — añadida para ejercer `P14_has_translator` (ausente del primer caso) y para no depender de
un solo repositorio de digitalización. Ver `../test-data/PROVENANCE-stendhal-traduccion-internet-archive.md`
para el detalle de verificación de este segundo caso.

## CQ1 — ¿Quién es el autor original de la obra X?

**Formal:** dada una instancia de `F1_Work`, obtener la persona vinculada como
`P14_has_original_author` a través de su `F27_Work_Creation`.
**Consulta:** `sparql/select/CQ1-autor-original.rq`
**Resultado esperado:** 2 filas, mismo `?author` (`ex:Stendhal`) — una por cada etiqueta
multilingüe declarada (fr/es); no es una duplicación del dato, es `rdfs:label` multivaluado.

## CQ2 — ¿En qué lengua está escrita esta expresión concreta?

**Formal:** dada una instancia de `F2_Expression` co-tipada `E33_Linguistic_Object`, obtener su
`P72_has_language`.
**Consulta:** `sparql/select/CQ2-lengua-expresion.rq`
**Resultado esperado:** 6 filas — `ex:French` (3 etiquetas fr/es/en) y `ex:English` (3 etiquetas
fr/es/en), una por cada expresión del corpus (la francesa original y la traducción inglesa).

## CQ3 — ¿Dónde se conserva físicamente el ejemplar Y?

**Formal:** dada una instancia de `F5_Item` co-tipada `E22_Human-Made_Object`, obtener su
`P54_has_current_permanent_location` (o `P55_has_current_location`).
**Consulta:** `sparql/select/CQ3-localizacion-ejemplar.rq`
**Resultado esperado:** 2 filas, mismo `?location` (`ex:BnF`) — una por etiqueta multilingüe (fr/es).

## CQ4 — ¿Qué derechos aplican a esta edición digital, y quién los posee?

**Formal:** dada una instancia de `D1_Digital_Object`, obtener el/los `E30_Right` a los que está
sujeta vía `P104_is_subject_to`.
**Consulta:** `sparql/select/CQ4-derechos-edicion-digital.rq`
**Resultado esperado:** 3 filas — `ex:Right_PublicDomain_Gallica` (dominio digital de Gallica) y
`ex:Right_PublicDomain` (dominio público general, también aplicado al objeto digital de Internet
Archive), con sus respectivas etiquetas multilingües.

## CQ5 — ¿Este objeto digital proviene de digitalizar un objeto físico, o nació digital?

**Formal:** para una instancia de `D1_Digital_Object`, verificar (bajo CWA) si existe un
`D2_Digitization_Process` que lo tenga como `L11_had_output` y que a su vez haya digitalizado
(`L1_digitized`) un objeto físico — distinción explícitamente señalada como relevante en el
Problema estructural "complementario" documentado en `../decisions/fr/problemes-et-solutions.md`
(digitalización vía `D2_Digitization_Process` frente a producción nativamente digital vía
`D7_Digital_Machine_Event` sin `L1_digitized`).
**Consulta:** `sparql/ask/CQ5-digitalizado-vs-nato-digital.rq`
**Resultado esperado:** `true` (el objeto digital de Gallica SÍ proviene de digitalizar
`ex:Item_BnF_Tome1`).

## Verificaciones adicionales de cardinalidad (CWA), no formuladas como CQ pero sí como ASK

- `sparql/ask/CHECK-manifestation-tiene-editor-cientifico.rq` — toda `F30_Manifestation_Creation`
  del corpus debe declarar al menos un responsable editorial (`P14_has_scientific_editor` o
  `P14_has_publisher`) — corregido el 2026-07-10 tras un primer fallo legítimo: la formulación
  original exigía editor científico para todas las manifestaciones, y la edición Modern Library de
  1929 (sin editor científico distinguido, solo editorial) reveló que esa regla universal era
  incorrecta.
- `sparql/ask/CHECK-obra-tiene-un-unico-autor.rq` — la obra de este ejemplo tiene exactamente un
  `P14_has_original_author` (no cero, no varios) — verifica que el dato no esté duplicado ni vacío.
