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

# Verificación — traducción inglesa e Internet Archive (enriquecimiento del test-data)

**Fecha:** 2026-07-10. **Investigación inicial:** agente con modelo Haiku, con instrucción
explícita de autoverificar cada dato contra dos fuentes independientes antes de aceptarlo (formato
tabular, columna de confianza). **Verificación cruzada adicional de la sesión principal:** consulta
directa a la API de metadatos de Internet Archive (`archive.org/metadata/redblack0000cktr`) y
búsqueda independiente de las fechas biográficas del traductor.

## Por qué se amplió el ejemplo

El primer ejemplo (Stendhal/Gallica/BnF) no ejercía `P14_has_translator` (ninguna traducción en los
datos de prueba) ni usaba ningún repositorio de digitalización distinto de Gallica. El usuario pidió
explícitamente diversificar las fuentes y añadir un caso de traducción real.

## Datos usados, con su verificación

| Dato | Valor usado | Verificación |
|---|---|---|
| Traductor | Charles Kenneth Scott Moncrieff | Wikipedia + Internet Archive (agente); fechas de vida (1889-09-25 / 1930-02-28) reconfirmadas independientemente por la sesión principal contra la página de alumni de la Universidad de Edimburgo, que coincide con Wikipedia |
| Título de la traducción | *The Red and the Black* | Wikipedia + metadatos de Internet Archive |
| Año de publicación usado | 1929 (edición Modern Library) | **Verificado directamente por la sesión principal** contra `https://archive.org/metadata/redblack0000cktr`: `date: "1929-01-01"`, `publisher: "Modern Library"`, `creator: "C.K. [Translation] Stendhal (M Henri Beyle); Scott-Moncrieff"` |
| Identificador de Internet Archive | `redblack0000cktr` | **HTTP 200 verificado directamente** por la sesión principal en `https://archive.org/details/redblack0000cktr`, y metadatos confirmados vía la API JSON oficial (no solo el HTML) |
| Editorial | Modern Library (Nueva York, activa desde 1917) | Metadatos de Internet Archive (agente); fecha de fundación no reverificada de forma independiente por la sesión principal — confianza media en ese dato puntual |

## Dato explícitamente NO usado, por confianza insuficiente

El agente también reportó una traducción española de Enrique de Mesa, pero sin poder verificar el
año exacto de publicación (marcado "no encontrado" tras búsqueda razonable) ni el traductor de las
digitalizaciones en español disponibles en Internet Archive (metadatos sin traductor identificado).
**Se decidió no incluir este dato en `test-data/stendhal-le-rouge-et-le-noir.ttl`**: incluir un nodo
"traductor" sin fecha ni certeza de autoría habría sido precisamente el tipo de dato débilmente
verificado que este ejercicio pretende evitar. Si en el futuro se verifica correctamente, puede
añadirse como una tercera expresión (`Expression_ES_*`).

## Otras traducciones/digitalizaciones reportadas por el agente, no incorporadas

El informe original también documentó, con distintos grados de confianza, las traducciones de Lowell
Bair (1959), Margaret R. B. Shaw ("Scarlet and Black", 1953), Catherine Slater (1991, Oxford World's
Classics) y Horace B. Samuel (1954, Liveright) — todas con identificadores de Internet Archive
propios. No se incorporaron al grafo de prueba para no sobrecargar el ejemplo; quedan documentadas
aquí por si se quiere ampliar el dataset de prueba más adelante.
