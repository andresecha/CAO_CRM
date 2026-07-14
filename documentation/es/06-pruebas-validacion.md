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
# Cómo se comprueba que el modelo está bien construido

## Por qué hace falta una batería de pruebas, y por qué no basta con que "abra sin error"

Un modelo ontológico como CAO_CRM (Corpus Author Ontology CRM, el modelo del consorcio Ariane) es, en el fondo, un archivo de texto con una gramática muy estricta, que describe clases ("Obra", "Persona", "Lugar"...), propiedades que las relacionan ("tiene por autor", "tiene por título"...) y reglas sobre cómo pueden combinarse. Ese archivo puede fallar de maneras muy distintas: por un error tipográfico que impide leerlo, siendo legible pero lógicamente contradictorio, contradiciendo en silencio las normas que dice extender, o siendo intachable y aun así incapaz de responder las preguntas reales que motivaron su construcción.

Por eso el repositorio de validación aplica una **cadena de ocho verificaciones automatizadas**, cada una pensada para detectar un tipo de problema que las demás no ven, ejecutables en un solo comando (`make validate`) o de forma individual. Una advertencia válida para todas: nunca basta con fiarse de la línea resumida de la terminal, ni de que una herramienta "termine sin error" —hay que abrir el informe detallado cuando existe. Esta disciplina no es teórica: al comienzo mismo del proyecto, un resumen indicó "0 problemas" mientras el informe real contenía varios problemas graves, por un error en el propio script de conteo (ver la sección "Preguntas frecuentes" de esta documentación para este caso y otros, conservados como lecciones).

## Estado actual (10 de julio de 2026, `CAO_CRM-1.0.rdf`, 1165 triples, 41 clases, 84 propiedades de objeto, 5 propiedades de datos)

| # | Prueba | Comando | Resultado |
|---|---|---|---|
| 1 | Sintaxis | `make syntax` | ✅ PASS |
| 2 | Coherencia lógica | `make reason` | ✅ PASS |
| 3 | Restricciones SHACL | `make shacl` | ✅ PASS (datos reales, ver más abajo) |
| 4 | Conformidad con las normas fuente | `make conformance` | ✅ PASS |
| 5 | Metadatos del encabezado | `make metadata` | ✅ PASS (7/7) |
| 6 | Calidad de diseño (OOPS!) | `make quality` | ✅ PASS |
| 7 | Métricas estructurales (ROBOT report) | `make metrics` | ✅ PASS |
| 8 | Principios FAIR (FOOPS!) | `make fair` | ✅ PASS — 0,80/1,0 (ejecución local real) |

Las ocho pruebas pasan, sin excepción. Es el resultado de un trabajo de verificación hecho en varias oleadas sucesivas, cada una más exigente que la anterior —el detalle completo de este recorrido, con citas y pruebas, está en `decisions/fr/problemes-et-solutions.md` y en la cadena de tres auditorías independientes (`auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md`, `auditoria-3-verificacion-final.md`).

## 1. Sintaxis: ¿se puede leer el archivo?

Es la verificación más elemental: que `CAO_CRM-1.0.rdf` sea un documento RDF/XML bien formado, sin errores de gramática, verificado por tres lectores independientes (`rapper`, `riot`, `rdflib`) para no depender del punto ciego de uno solo. Si esta verificación fallara, ningún otro programa podría siquiera abrir el archivo.

## 2. Coherencia lógica (razonamiento)

Un "razonador" (*reasoner*, aquí HermiT) aplica las reglas lógicas del modelo para verificar que no llevan a ninguna contradicción, en particular a una "clase insatisfacible": una categoría definida de tal manera que, lógicamente, nunca podría tener ni un solo miembro real. La prueba se ejecuta sobre el modelo fusionado con las tres fuentes oficiales completas (CIDOC-CRM, LRMoo, CRMdig) más SKOS, no solo sobre el módulo aislado —porque un módulo puede parecer coherente en apariencia y aun así esconder una contradicción que solo aparece al recombinarlo con lo que dice extender.

## 3. Restricciones SHACL sobre datos reales

Mientras que la coherencia lógica examina el modelo en abstracto, SHACL verifica algo más concreto: si un conjunto de datos preciso —una obra, un autor, una fecha— respeta las reglas de forma que se le imponen. Es una capa complementaria al razonamiento, orientada a datos reales en vez de a la estructura abstracta. El grafo usado (`test-data/stendhal-le-rouge-et-le-noir.ttl`) no es un ejemplo sintético inventado para la ocasión: aplica los cinco niveles del modelo a *Le Rouge et le Noir* de Stendhal, con dos casos reales verificados contra sus fuentes (la edición crítica de Henri Martineau, digitalizada por la BnF/Gallica, y la traducción inglesa de C. K. Scott Moncrieff, digitalizada por Internet Archive) —ver `test-data/PROVENANCE-stendhal-verificacion.md` para el detalle de cada verificación.

## 4. Conformidad con las normas que CAO_CRM extiende

CAO_CRM no inventa clases de la nada: reutiliza elementos de CIDOC-CRM, de LRMoo y de CRMdig. Esta prueba compara el modelo combinado con los archivos oficiales de esas normas para detectar si se perdió o se contradijo en silencio algún axioma de origen al integrarlos. La parte automatizada no señala hoy ningún axioma perdido, más allá de un artefacto de fusión sin consecuencias (documentado en `validation/06-conformance/out/conformance-notes.md`); se recomienda además, por prudencia, una revisión manual complementaria de las relaciones de subclase.

## 5. Metadatos de versión y procedencia

Esta prueba verifica que la "ficha de identidad" del archivo —quién lo creó, de qué versión se trata, bajo qué licencia se publica— esté completa, y que no contenga metadatos de otra ontología pegados por error (un incidente real que ocurrió muy temprano en este proyecto —ver "Preguntas frecuentes"). Las 7 verificaciones pasan: presencia de `owl:versionIRI`, `dc:creator`, `dc:rights`, `owl:versionInfo`, y ausencia de cualquier contaminación proveniente de SKOS.

## 6. Calidad de diseño (OOPS!)

OOPS! es un servicio externo especializado en las "trampas" (*pitfalls*) típicas del diseño de ontologías, como declarar que una propiedad admite dos dominios a la vez, o la ausencia de disyunción entre clases. Tres categorías de pitfalls (`P10`, `P19`, `P30`) quedan deliberadamente excluidas del análisis solicitado al servicio, cada una por una razón verificada y documentada en `validation/04-quality/README.md` —entre otras, que CIDOC-CRM, LRMoo y CRMdig mismos no declaran ninguna disyunción de clase en ningún lugar de sus versiones oficiales, una elección de diseño deliberada de esta familia de normas, no un descuido de CAO_CRM. Lo que queda dentro del alcance analizado pasa sin ningún pitfall crítico ni importante.

## 7. Métricas estructurales (ROBOT report)

Esta prueba recorre el modelo en busca de descuidos frecuentes: propiedades sin definición explícita, etiquetas duplicadas entre dos términos, etc. La regla `duplicate_label` se recalibró de ERROR a WARN en el perfil de verificación, tras comprobar que las 44 ocurrencias señaladas existen, tal cual, en los archivos oficiales de CIDOC-CRM y LRMoo (propiedades hermanas que comparten deliberadamente el mismo verbo en un idioma dado) —no es un descuido de CAO_CRM, y el remedio aplicado (un perfil personalizado) es el que la propia documentación de ROBOT recomienda para este caso, ya señalado además ante el OBO Operations Committee.

## 8. Principios FAIR

FAIR es un conjunto de principios (que un recurso sea fácil de encontrar, de consultar, de combinar con otros y de reutilizar) empleado en ciencia abierta. Esta prueba ahora se ejecuta de verdad, en local: se descarga y lanza el jar oficial de FOOPS! (versión 0.4.0) como un pequeño servidor, y se consulta su propio endpoint REST documentado (`assessOntologyFile`) —ya no hace falta el servicio público en línea, cuyo contrato REST nunca se documentó de forma fiable. Puntuación obtenida: **0,80 sobre 1,0** (Interoperable 3/3, Encontrable 3/4, Reutilizable 6/8; la dimensión Accesible no se evalúa en modo archivo local, exige una URI pública dereferenciable). Reutilizable subió de 5/8 a 6/8 el 14 de julio, al añadirse el DOI de Nakala de la ontología (`dcterms:identifier`). El detalle completo, por dimensión, está en `validation/08-fair/README.md`.

## Preguntas de competencia y documentación generada automáticamente

Dos pasos complementarios, fuera de la cadena `make validate` pero igualmente reales:
- Las **preguntas de competencia** (`competency-questions/CQ-001-a-005-stendhal.md`) son hoy 5 preguntas concretas —quién es el autor original, en qué lengua, dónde está el ejemplar, qué derechos, digitalizado o nato-digital— más 2 verificaciones de cardinalidad, cada una traducida a una consulta SPARQL real (`sparql/ask/`, `sparql/select/`) y ejecutada contra el mismo grafo Stendhal que SHACL. `make cq` las ejecuta todas.
- La **documentación HTML generada automáticamente** (con Widoco, ver `docs/site/index-{en,fr,es}.html`) se regenera sin error y refleja hoy fielmente el encabezado propio de CAO_CRM, en los tres idiomas —incluidos los metadatos añadidos para cerrar la brecha FAIR.

## El resultado de conjunto

Las ocho categorías de prueba están hoy completamente en verde, sin ninguna excepción ni ninguna advertencia silenciada, y las preguntas de competencia son reales en vez de un esqueleto metodológico. Cada decisión que permitió llegar a este estado —por qué se recalibró tal regla, por qué se excluyó deliberadamente tal otra, cómo se construyó y verificó el grafo de prueba— está documentada con su prueba de respaldo, en vez de fiarse ciegamente de una etiqueta "aprobado" o "fallido".
