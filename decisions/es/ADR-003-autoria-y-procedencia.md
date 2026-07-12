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
# ADR-003 — Autoría, procedencia y citación de herramientas en el encabezado

**Estado:** Decidido — 2026-07-03
**Decisión tomada por:** Andrés Echavarría, a partir de instrucción explícita del equipo AMIS
**Tipo de decisión:** corrección de metadatos de procedencia (no afecta al modelo conceptual ni al alcance de clases/propiedades)

## Contexto

El encabezado de `CAO_CRM-1.0.rdf` (`dc:creator`) decía, desde el inicio de este proyecto de validación: *"Model created by the Consortium HN Ariane and encoded by Mélanie Bouland"*. Esa frase era exacta para el archivo RDF **original** que entregó Mélanie Bouland — pero deja de serlo para el archivo que vive ahora en este repositorio, por una razón concreta señalada explícitamente por el equipo:

> "Efectivamente nos basamos sobre el modelo discutido y dibujado por Mélanie Bouland, pero la codificación es completamente nueva, además que se usaron scripts y técnicas que deben citarse [...] porque no es la ontología que nos entregó Mélanie."

Es decir: el **modelo conceptual** (qué clases y propiedades componer, cómo se relacionan — documentado en `CRM_V8.json` y en el paper del consorcio) sigue siendo el que Mélanie Bouland discutió y dibujó. Pero el **archivo RDF/OWL concreto** que hay en `ontology/CAO_CRM-1.0.rdf` es una implementación técnica distinta, reconstruida desde cero con un método diferente (extracción de módulo con ROBOT, razonamiento con HermiT, validación visual en Protégé — ver `decisions/informe-implementacion-RDF-modulo-acotado.md`) al que produjo el archivo original que ella entregó. Mantener la frase tal cual atribuía la codificación técnica de este archivo concreto a alguien que no la hizo.

## Decisión

Se distingue explícitamente, en el encabezado de la ontología, entre **quién concibió el modelo conceptual** y **quién construyó este archivo RDF concreto**:

| Propiedad | Valor | Rol |
|---|---|---|
| `dc:creator` | *"Conceptual model discussed and diagrammed by Mélanie Bouland, within the Consortium HN Ariane."* | Autoría del diseño conceptual — no de este archivo. |
| `dc:contributor` (1) | *"Andrés Echavarría -- RDF/OWL encoding, bounded module extraction and validation of this file (2026). This encoding is a new, independent implementation of the conceptual model above; it is not the RDF file originally delivered by Mélanie Bouland."* | Autoría de la codificación técnica de este archivo concreto, con la aclaración explícita de que no es el archivo original. |
| `dc:contributor` (2) | *"AMIS team (Consortium HN Ariane) -- current maintainers of this encoding."* | Refleja que quien retoma y mantiene este trabajo ahora mismo es el equipo AMIS, no solo "el consorcio" de forma genérica. |
| `dc:description` | Reescrita para integrar lo anterior en una frase legible, más las citas de herramientas (ver abajo). | — |
| `dcterms:references` (×3) | `http://robot.obolibrary.org/`, `http://www.hermit-reasoner.com/`, `https://protege.stanford.edu/` | Cita estructurada (no solo en prosa) de las herramientas usadas para construir y validar este archivo. |

**Dirección científica.** La codificación técnica atribuida a Andrés Echavarría en `dc:contributor` (1) se llevó a cabo bajo la dirección y el apoyo científico de **Fatiha Idmhand**, tal como ya refleja la marca de procedencia añadida a la cabecera de todos los archivos de este proyecto (véase el comentario introductorio de este mismo documento: *"Encoding carried out under the scientific direction and support of Fatiha Idmhand"*). Esta dirección científica es distinta, y se añade, a su rol de contribuyente nombrada junto con el resto del equipo AMIS en la cabecera de `ontology/CAO_CRM-1.0.rdf`.

**No se cita ningún asistente de inteligencia artificial como autor, contribuyente ni herramienta.** Aunque el proceso de reconstrucción se hizo con asistencia de un asistente de código (Claude, de Anthropic) operado por Andrés Echavarría, la autoría intelectual y la responsabilidad de las decisiones de modelado recaen en él como persona — igual que la autoría de un texto escrito con ayuda de un editor de texto no se atribuye al editor de texto. Esto es una decisión explícita del equipo, no un olvido.

## Herramientas citadas y por qué

- **ROBOT** (`http://robot.obolibrary.org/`) — la herramienta de línea de comandos usada para extraer el módulo acotado (`robot extract --method subset`) y para razonar/generar los informes de métricas y conformidad. Ver `decisions/informe-implementacion-RDF-modulo-acotado.md` para el detalle completo del proceso.
- **HermiT** (`http://www.hermit-reasoner.com/`) — el razonador OWL DL usado (a través de ROBOT) para comprobar la coherencia lógica del modelo en cada iteración.
- **Protégé** (`https://protege.stanford.edu/`) — el editor de ontologías usado para la **validación visual** del archivo final: confirmar que abre sin errores, que el título/encabezado se ve correctamente, y para la inspección manual de clases y propiedades durante la reconstrucción.

## No se modifica

- El `owl:versionIRI` (`http://www.CAO_CRM.org/ontology/2.0`) se mantiene sin cambios, para no romper la coherencia con el resto del repositorio (scripts, documentación, nombres de archivo) que ya lo referencian como "2.0".
- El alcance de clases y propiedades (las 29+61+5 ya acordadas) no se ve afectado por esta decisión — es puramente una corrección de metadatos de procedencia, no una decisión de modelado del dominio.

## Verificación

Tras el cambio, se volvió a ejecutar la batería completa: sintaxis (PASS), razonamiento HermiT (PASS, consistente), `validation/07-metadata/check.sh` (7/7 PASS, incluidas las comprobaciones de no-contaminación), y apertura confirmada en Protégé (título de ventana correcto: `ontology (http://www.CAO_CRM.org/ontology/2.0)`).
