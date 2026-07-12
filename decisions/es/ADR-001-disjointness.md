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
# ADR-001 — No añadir condiciones `owl:disjointWith`

**Estado:** Decidido — 2026-07-03
**Decisión tomada por:** equipo CAO_CRM (Ariane)
**Tipo de decisión:** restricción/acotación de un fragmento reutilizado (no crea nada nuevo, no modifica el modelo original)

## Contexto

`owl:disjointWith` es la forma en OWL de decir "estas dos clases nunca pueden compartir una misma instancia" — por ejemplo, declarar que `E67_Birth` (nacimiento) y `E69_Death` (muerte) son disjuntas evitaría, por construcción lógica, que alguien registrara por error un mismo evento como ambas cosas a la vez. El razonador usaría esa declaración para detectar automáticamente ese tipo de error de captura de datos.

Se verificó que **el módulo actual (`ontology/CAO_CRM-1.0.rdf`) no tiene ninguna declaración `owl:disjointWith`**, y que **el propio archivo oficial de CIDOC-CRM 7.1.3 tampoco las declara** para la inmensa mayoría de sus clases — es una elección de diseño deliberada del consorcio CIDOC-CRM (prefieren dejar la disjunción a criterio de cada implementación concreta, no imponerla a nivel del modelo genérico).

## Decisión

**No se añade ninguna condición `owl:disjointWith`.** El módulo se mantiene fiel a la ausencia de disjunciones del archivo oficial.

## Razón

Coherente con el mismo principio de composición pura aplicado en todo el proyecto (ver, p. ej., problemes-et-solutions.md): acotar *qué piezas* de CIDOC-CRM/LRMoo/CRMdig se usan es el objetivo de CAO_CRM; imponer una restricción lógica adicional (disjunción) que el propio CIDOC-CRM evita deliberadamente sería introducir una decisión de modelado propia, no una simple composición de fragmentos existentes.

## Reconsiderar en el futuro si...

Si en el futuro AMIS (el asistente de generación de metadatos) empieza a producir errores de captura reales que una disjunción concreta habría detectado, esta decisión puede revisarse — pero entonces sería una decisión informada por evidencia de uso real, documentada en un ADR nuevo, no una precaución especulativa tomada de antemano.
