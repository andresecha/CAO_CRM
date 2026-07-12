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
# Preguntas frecuentes y errores reales encontrados durante la construcción del modelo (y qué enseñan)

Construir un modelo ontológico (un archivo formal que describe clases, propiedades y reglas — aquí, CAO_CRM, el Corpus Author Ontology CRM del consorcio Ariane) reutilizando piezas de estándares existentes (CIDOC-CRM, LRMoo, CRMdig) no es "copiar y pegar" sin más: cada pieza trae convenciones y vacíos que pueden colarse por error. Esta sección recoge, en preguntas y respuestas, incidentes reales documentados durante la validación de CAO_CRM, con su causa, su solución y la lección que dejan — sin ánimo de señalar culpables, como ejemplo pedagógico para quien componga ontologías ajenas. Los tres casos descritos a continuación están **completamente resueltos** en la versión actual del modelo (`CAO_CRM-1.0.rdf`); se conservan aquí precisamente porque fueron los que convencieron al equipo de no volver a fiarse jamás de un resumen automático sin verificar el detalle — una disciplina que, mucho más adelante en el proyecto, dio lugar a una cadena de tres auditorías independientes y sucesivas antes de cualquier publicación (ver la última sección de este documento).

## ¿Por qué la documentación generada apareció titulada "SKOS Vocabulary" en vez de CAO_CRM?

Al generar el sitio de documentación con Widoco (un programa que lee la ontología y produce automáticamente una web navegable con sus clases y propiedades), la página mostraba como título "SKOS Vocabulary" — el nombre de otro estándar sin relación con CAO_CRM: SKOS (*Simple Knowledge Organization System*, un modelo para vocabularios controlados y tesauros).

Al inspeccionar `CAO_CRM-2.0.rdf` se confirmó que el nodo que describe la ontología en sí misma (su "ficha de identidad") tenía mezclados, además de sus propios datos, metadatos copiados literalmente de otras seis ontologías (SKOS, CIDOC-CRM, CRMdig, LRMoo, CRMsci, CRMinf): el título tenía el valor `"SKOS Vocabulary"@en`, la autoría estaba atribuida a los autores reales de SKOS, y había un bloque de casi 200 líneas que resultó ser, palabra por palabra, las notas de publicación propias de CIDOC-CRM.

**Cómo se descubrió:** no por revisión manual, sino porque Widoco reflejó un síntoma imposible de ignorar (un título equivocado), lo que llevó a inspeccionar el archivo fuente. La causa probable es un efecto colateral de cómo el editor Protégé "aplana" las importaciones al exportar: al volcar varios archivos importados en uno solo, sus metadatos propios pueden mezclarse en el mismo nodo.

**Cómo se soluciona:** eliminar del nodo de la ontología los valores ajenos y declarar los propios. El repositorio incluye consultas de "regresión" pensadas para volver a fallar si el problema reaparece.

**Lección general:** cualquier herramienta que lea el título para identificar "qué ontología es esta" —documentación, catálogos, indexadores de datos abiertos— confía ciegamente en ese valor. Conviene revisar siempre la cabecera de la ontología tras cualquier importación o "aplanado" de archivos.

## ¿Por qué el modelo, que antes pasaba la prueba de coherencia lógica, empezó a fallar como "inconsistente"?

Entre dos verificaciones, el archivo creció de forma sustancial (de 970 a más de 7.000 triples — cada triple es una afirmación básica "sujeto-predicado-objeto"), por una reexportación más completa desde Protégé. Con ese contenido nuevo, el razonador (*reasoner*, el programa que aplica las reglas lógicas del modelo para comprobar que no se contradice) reportó que la ontología era inconsistente: quedaba lógicamente vacía, porque una contradicción interna permite "deducir" cualquier cosa a partir de cualquier cosa.

**Cómo se descubrió:** con `robot explain`, una utilidad que identifica el conjunto mínimo de afirmaciones responsables. Encontró cuatro axiomas: `cao:Title` equivalente a la propiedad de título de Dublin Core; el nodo de la ontología con el valor contaminado `"SKOS Vocabulary"@en` en esa misma propiedad; `cao:Place` equivalente a `cao:Title`; y `cao:Place` con rango `xsd:anyURI` (solo admite identificadores URI). Por transitividad, el texto contaminado terminaba "heredado" por `cao:Place`, que exige URIs, no texto — contradicción irresoluble que colapsa el modelo entero.

**Cómo se soluciona:** es la combinación de dos problemas ya conocidos por separado: el metadato contaminado del caso anterior, y una advertencia de calidad (la trampa "P27 — Defining wrong equivalent properties", detectada por la herramienta OOPS!) que hasta entonces parecía solo una recomendación "importante", no urgente. Al crecer el archivo, esa recomendación se volvió una contradicción lógica dura. Corregirla exige revisar si `cao:Place` debe seguir siendo equivalente a `cao:Title`, además de limpiar el metadato contaminado.

**Lección general:** un aviso de calidad "menor" hoy puede convertirse mañana en un error lógico bloqueante, simplemente porque el modelo cambió de tamaño. Dos hallazgos independientes pueden combinarse en un tercero más grave que cualquiera por separado — por eso conviene tratar los avisos "importantes" con la misma seriedad que los "críticos".

## ¿Por qué faltaban axiomas de CIDOC-CRM sobre "tiene nota" (`P3_has_note`) al comparar el modelo combinado con el archivo oficial?

Al comparar el modelo combinado con el archivo oficial de CIDOC-CRM 7.1.3 mediante `robot diff` (que señala qué afirmaciones del original no aparecen, sin cambios, en el resultado), aparecieron 8 axiomas oficiales ausentes, ligados a `P3_has_note` ("tiene nota", una propiedad para adjuntar descripciones informales a cualquier entidad) y sus subpropiedades.

**Cómo se descubrió:** comparando cómo estaba declarada `P3_has_note` en CAO_CRM frente al archivo oficial. En CAO_CRM era `owl:ObjectProperty` (conecta con otra entidad con identidad propia). El release oficial de CIDOC-CRM la declara de forma genérica, como `rdf:Property`, sin decir si es de objeto o de dato: la documentación de referencia describe conceptualmente "Domain: E1 CRM Entity / Range: E62 String", pero el archivo RDF ejecutable nunca lo codificó — un vacío real del propio estándar, no un error de CAO_CRM. Al combinar ambas declaraciones para la misma URI se produce *punning* (usar el mismo nombre para dos naturalezas distintas), y las herramientas de fusión descartan silenciosamente los axiomas que solo tenían sentido bajo la lectura "de dato".

**Cómo se soluciona:** el equipo documentó la decisión en `decisions/fr/problemes-et-solutions.md` (Problema 1), el catálogo general de problemas y soluciones del proyecto. Se eligió declarar `P3_has_note` como `owl:DatatypeProperty` con rango `rdfs:Literal` (la categoría más amplia de valores simples), replicando el patrón que el propio archivo oficial usa en una propiedad hermana con el mismo vacío, `P90_has_value`: `<rdfs:range rdf:resource="http://www.w3.org/2000/01/rdf-schema#Literal" />`. Se descartó `xsd:string`: habría sido una restricción inventada sin respaldo oficial, contraria a la práctica del propio CIDOC-CRM, que evita comprometerse con tipos XSD incluso donde el tipo "parece obvio" (`P90_has_value` representa un número y aun así usa `rdfs:Literal`).

**Lección general:** cuando un estándar tiene un vacío en su implementación técnica, la forma más segura de rellenarlo no es inventar una solución "más precisa" propia, sino replicar cómo el mismo estándar resuelve casos equivalentes. En un proyecto definido como composición acotada de fragmentos ajenos, cualquier tipado que no esté ya en el original es, en la práctica, una redefinición conceptual del modelo base.

## ¿Cómo se relacionan estos casos entre sí?

No son incidentes aislados: "SKOS Vocabulary" fue una de las cuatro causas de la inconsistencia lógica del segundo caso, y `P3_has_note` fue detectado por dos pruebas distintas, lo que confirma que era un problema real y no un falso positivo. En un modelo compuesto de varias ontologías, los problemas rara vez quedan contenidos en el módulo donde se originan: se propagan a otras capas de verificación, y a veces solo se hacen visibles cuando el archivo crece o corre un tipo de prueba distinto al que los detectó primero.

## ¿Por qué no se corrigieron estos problemas "sobre la marcha", con la primera solución razonable disponible?

Porque una solución rápida, aunque funcione técnicamente, puede introducir una decisión de modelado que nadie autorizó ni documentó: elegir `xsd:string` para `P3_has_note` habría "arreglado" el problema, pero sin respaldo oficial. Cuando un hallazgo exige una decisión de diseño, el proceso es documentarlo en un ADR, con las alternativas evaluadas y las citas oficiales que respaldan la elección, en vez de resolverlo en silencio. Los hallazgos mecánicos, como limpiar metadatos contaminados, quedan pendientes de corrección directa, sin necesidad de un ADR.

## ¿Qué lección general deja todo esto para quien construya un modelo similar?

1. **Un resumen automático ("0 errores") nunca sustituye la inspección del informe completo.** "SKOS Vocabulary" no lo detectó una prueba diseñada para eso, sino un síntoma visual en una herramienta con otro objetivo.
2. **Los vacíos en la documentación oficial de un estándar reutilizado no se "adivinan" con una decisión propia**, sino replicando cómo ese mismo estándar resuelve casos equivalentes, dejando constancia escrita de la elección.
3. **Un modelo compuesto de varias ontologías necesita revisar sus "puntos de unión" con regularidad.** Lo que ayer era una recomendación menor puede ser, mañana, un error real, simplemente porque el contexto cambió.

## Lo que estas lecciones dieron, mucho más adelante en el proyecto

Estos tres incidentes dejaron una huella duradera en la metodología de trabajo: ninguna afirmación se acepta ya sin verificación directa contra el archivo fuente, nunca contra un resumen o un recuerdo. Esta disciplina alcanzó su forma más acabada justo antes de publicar la versión actual, en forma de una **cadena de tres auditorías independientes y sucesivas**: una primera auditoría que reverifica cada término del RDF uno por uno contra los archivos oficiales vendorizados; una segunda que reverifica la propia documentación de decisión y la conformidad conceptual de cada elección; y una tercera que reverifica de forma cruzada una muestra de las afirmaciones más fuertes de las dos anteriores, sin confiar tampoco en ellas. Ninguna de las tres auditorías encontró error alguno en las afirmaciones verificadas por la anterior —un resultado que, precisamente por los incidentes contados arriba, nunca se dio por sentado de antemano. El detalle completo está en `decisions/fr/auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md` y `auditoria-3-verificacion-final.md`.
