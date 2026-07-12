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
# ADR-002 — No traducir los términos de LRMoo/CRMdig que solo existen en inglés

**Estado:** Decidido — 2026-07-03
**Decisión tomada por:** equipo CAO_CRM (Ariane)
**Tipo de decisión:** restricción/acotación de un fragmento reutilizado (no crea nada nuevo, no modifica el modelo original)

## Contexto

Se verificó, revisando directamente los archivos oficiales (`imports/vendor/lrmoo-1.1.1.rdf`, `imports/vendor/crmdig-5.0.rdf`), que las 7 clases y 15 propiedades de LRMoo, y las 3 clases y 8 propiedades de CRMdig usadas por CAO_CRM **solo tienen `rdfs:label` en inglés** — ningún otro idioma existe en esas fuentes para esos 25 términos (a diferencia de CIDOC-CRM, que sí ofrece hasta 7 idiomas para la mayoría de sus términos). Detalle completo en `decisions/informe-completitud-labels-domain-range.md`, sección 1.

## Decisión

**No se añade ninguna traducción.** Los 25 términos de LRMoo/CRMdig quedan solo en inglés en el módulo de CAO_CRM.

## Razón

Añadir una traducción al francés (u otro idioma) de estos términos sería, por definición, contenido que CAO_CRM originaría — no algo copiado de una fuente oficial. Eso contradice el principio de pura composición que rige todo el proyecto (ver problemes-et-solutions.md): CAO_CRM no debe generar contenido propio sobre las piezas que reutiliza, solo seleccionarlas y componerlas tal cual existen.

## Reconsiderar en el futuro si...

Si el equipo decide en algún momento que la documentación en francés es imprescindible para el uso práctico de AMIS o para la publicación del modelo, esa traducción debería:
1. Marcarse explícitamente como una anotación de CAO_CRM (por ejemplo, con una propiedad de anotación propia como `cao:has_working_translation`, no como si fuera un `rdfs:label@fr` oficial de LRMoo/CRMdig), para no crear la falsa impresión de que esa traducción viene avalada por los consorcios LRMoo/CRMdig.
2. Documentarse como un ADR nuevo, con la lista completa de términos traducidos y quién los revisó.
