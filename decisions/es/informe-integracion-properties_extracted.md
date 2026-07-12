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
# Informe de integración: `properties_extracted.csv` en el módulo CAO_CRM

**Fecha:** 2026-07-03
**Archivo de entrada:** `properties_extracted.csv` (199 filas, exportación derivada del diagrama `CRM_V8.json`, el modelo conceptual discutido y acordado colectivamente por el equipo)
**Archivo modificado:** el archivo del módulo (único archivo intervenido, según la regla vigente de solo modificar el RDF de trabajo del proyecto, nunca los archivos derivados o vendorizados; hoy `CAO_CRM-1.0.rdf`)
**Estado:** aplicado y verificado — ver sección 5

**Nota importante sobre el alcance de este informe:** continúa y refina lo ya documentado en `informe-completitud-labels-domain-range.md` (categoría A: "dominio/rango falta porque apunta a una clase oficial fuera de las 29"). Este informe compara esa lista de vacíos contra los pares dominio-propiedad-rango *concretos* que el propio diagrama V8 utiliza, para separar los que se pueden completar sin riesgo semántico de los que reflejan un uso genuinamente genérico de una propiedad CIDOC-CRM/LRMoo/CRMdig.

---

## 0. Motivación: nodos sueltos en el grafo interactivo

El usuario observó, al navegar el grafo interactivo del módulo (`graph/`, hoy `CAO_CRM-1.0-graph.html`), clases sin ninguna arista de dominio/rango hacia otra clase del módulo. Auditoría confirmada antes de esta intervención: **9 clases sin ninguna conexión dominio-rango a otra clase de las 29** — `E12_Production`, `E30_Right`, `E35_Title`, `E42_Identifier`, `E53_Place`, `E54_Dimension`, `E56_Language`, `E89_Propositional_Object`, `F5_Item`.

Causa raíz: `robot extract --method subset` solo conserva un triple `rdfs:domain`/`rdfs:range` si la clase de destino está literalmente en las 29 elegidas; cuando el rango/dominio oficial de CIDOC-CRM es una clase más general fuera de alcance (`E1_CRM_Entity`, `E41_Appellation`, `E70_Thing`, `E72_Legal_Object`, `E24_Physical_Human-Made_Thing`, `E2_Temporal_Entity`, `E4_Period`, `F32_Item_Production_Event`), el triple simplemente se descarta, no se sustituye.

---

## 1. Método y criterio de seguridad aplicado

Antes de tocar el archivo, se acordó con el usuario el siguiente criterio (elegido específicamente para no violentar la semántica de CIDOC-CRM/LRMoo/CRMdig):

Una inserción de `rdfs:domain`/`rdfs:range` se considera **segura** solo si:
1. La propiedad **no tiene actualmente ningún valor** en ese lado (nada que romper por intersección).
2. El diagrama V8 / CSV usa esa propiedad con **una única clase candidata** en ese lado. RDFS interpreta múltiples `rdfs:domain` (o `rdfs:range`) sobre la misma propiedad como **intersección**, no unión — insertar una de varias clases candidatas para una propiedad genérica reutilizada forzaría al razonador a exigir que el sujeto pertenezca simultáneamente a clases que en la práctica son distintas y no relacionadas, lo cual produciría inconsistencias falsas con datos reales.

Si la propiedad ya tenía un valor existente, se comprobó además si ese valor era ya **idéntico** a lo pedido por el CSV (nada que hacer) o si el valor existente era ya un **ancestro** en la jerarquía `rdfs:subClassOf` de todas las clases pedidas por el CSV (tampoco hace falta tocar nada — el existente ya cubre lógicamente todos los casos, y estrecharlo further rompería otros usos legítimos de la misma propiedad).

## 2. Correcciones aplicadas al CSV antes de clasificar (documentadas, no ambiguas)

| Problema en el CSV | Corrección aplicada | Verificación |
|---|---|---|
| `P21_has_general_purpose` | → `P21_had_general_purpose` | nombre oficial confirmado ya presente en el RDF actual |
| `P67_referes_to` (fila 157) | → `P67_refers_to` | ídem |
| `R16i_was_ceated_by` (fila 165) | → `R16i_was_created_by` | ídem |
| `E7_Activity,P14_carried_out_by (P14i_performed,E21_Person` (fila 148) | descartada — celda corrupta, duplica el par ya presente en la fila 89 | — |
| `F5 Item` (con espacio, muchas filas) | → `F5_Item` | coincide con la única clase real declarada en el RDF |
| Etiquetas individuo en francés usadas como si fueran clase (`Numérisation`, `Datation de la création`, `Auteur`, `Production de l'objet`, `Autre objet physique`, `Pers. physique ou morale`, `Responsable scientifique`, `Création de l'expression`) | mapeadas a la clase real de la que son instancia (`D2_Digitization_Process`, `E52_Time-Span`, `E21_Person`, `E12_Production`, `E18_Physical_Thing`, `E39_Actor`, `E21_Person`, `F28_Expression_Creation` respectivamente) | son individuos del diagrama, no clases nuevas — ninguna requiere ampliar las 29 clases del alcance |
| Filas con valor literal entre comillas (fechas, nombres reales, ARK...) | excluidas del análisis de esquema — son datos de ejemplo (ABox), no pares de esquema | pendiente de decisión aparte si se quieren cargar como `test-data/` (no se ha hecho en este informe) |
| `E60_Number` / `E62_String` usadas como clase URI de rango (`P90_has_value`, `P3_has_note`, `P2_has_type`) | excluidas automáticamente (no están en las 29 clases) | consistente con problemes-et-solutions.md (Problema 1) e informe de completitud: estos valores CIDOC-CRM no deben tener URI propia |

De las 198 filas de datos, quedaron **134 pares de esquema válidos** tras esta limpieza.

## 3. Inserciones aplicadas (seguras, verificadas)

**12 lados de propiedad (6 pares directa/inversa) insertados** en el archivo del módulo (hoy `CAO_CRM-1.0.rdf`):

| Propiedad | Lado | Clase insertada | Justificación (fila CSV) |
|---|---|---|---|
| `L11_had_output` | domain | `D2_Digitization_Process` | filas 31, 122 |
| `L11i_was_output_of` | range | `D2_Digitization_Process` | filas 32, 123 |
| `L61_contains_value_set_of` | domain | `D1_Digital_Object` | fila 140 |
| `L61i_has_value_set_representation` | range | `D1_Digital_Object` | fila 141 |
| `P108_has_produced` | range | `F5_Item` | fila 48 |
| `P108i_was_produced_by` | domain | `F5_Item` | fila 49 |
| `P43_has_dimension` | domain | `F5_Item` | fila 19 |
| `P43i_is_dimension_of` | range | `F5_Item` | fila 20 |
| `P67_refers_to` | range | `E52_Time-Span` | filas 54, 157 |
| `P67i_is_referred_to_by` | domain | `E52_Time-Span` | fila 53 |
| `R27_materialized` | domain | `E12_Production` | filas 118, 154 |
| `R27i_was_materialized_by` | range | `E12_Production` | filas 119, 155 |

**Efecto sobre los nodos sueltos: de 9 clases aisladas a 5.** `E12_Production`, `E54_Dimension`, `E89_Propositional_Object` y `F5_Item` quedaron conectadas. Las 5 que **siguen sin conexión** (`E30_Right`, `E35_Title`, `E42_Identifier`, `E53_Place`, `E56_Language`) lo están únicamente porque las propiedades que las vinculan en el diagrama V8 son de uso genérico (ver sección 4) — no se puede resolver mecánicamente sin arriesgar la semántica.

## 4. Casos conflictivos — catalogados, NO aplicados, pendientes de discusión colectiva

### 4.1 Propiedades CIDOC-CRM genuinamente genéricas (unión no representable en RDFS simple)

Estas propiedades se usan en el diagrama V8 sobre **varias clases distintas** — es un uso legítimo y esperado de un vocabulario genérico, no un error. Forzar un único `rdfs:domain`/`rdfs:range` rompería los demás usos.

| Propiedad | Lado en conflicto | Clases candidatas (según V8/CSV) |
|---|---|---|
| `P104_is_subject_to` / `P104i_applies_to` | domain / range | `D1_Digital_Object`, `D2_Digitization_Process`, `E7_Activity`, `F1_Work`, `F2_Expression`, `F3_Manifestation`, `F5_Item` |
| `P2_has_type` / `P2i_is_type_of` | domain / range | `D1_Digital_Object`, `D2_Digitization_Process`, `E12_Production`, `E30_Right`, `E3_Condition_State`, `E42_Identifier`, `F3_Manifestation`, `F5_Item` |
| `P4_has_time-span` / `P4i_is_time-span_of` | domain / range | `D2_Digitization_Process`, `E12_Production`, `E67_Birth`, `E69_Death`, `E7_Activity`, `F27_Work_Creation`, `F30_Manifestation_Creation` |
| `P7_took_place_at` / `P7i_witnessed` | domain / range | `E12_Production`, `E3_Condition_State`, `E67_Birth`, `E69_Death`, `E7_Activity` |
| `P16_used_specific_object` / `P16i_was_used_for` | range / domain | `D1_Digital_Object`, `F3_Manifestation`, `F5_Item` |
| `P1_is_identified_by` / `P1i_identifies` | domain **y** range | domain: `F1_Work`, `F3_Manifestation`, `F5_Item` — range: `E35_Title`, `E42_Identifier` (nótese: `E35_Title` identifica específicamente `F1_Work`; `E42_Identifier` identifica `F3_Manifestation`/`F5_Item` — son dos patrones de uso distintos mezclados en la misma propiedad genérica) |

**Opciones para la discusión colectiva** (ninguna aplicada todavía):
- **(a) Dejarlo como está** — el modelo sigue siendo válido y consistente; el grafo mostrará estas clases sin arista directa, aunque la relación exista y funcione correctamente a nivel de instancia (ABox).
- **(b) Restricción OWL por clase** (`rdfs:subClassOf` con `owl:Restriction`/`owl:allValuesFrom`, ej. "toda instancia de `F5_Item` que use `P104_is_subject_to` debe apuntar a `E30_Right`") — más fiel a OWL, pero es una intervención de modelado más compleja y visible.
- **(c) SHACL** (capa `validation/03-shacl`, ya scaffolded en el proyecto) — declarar shapes por clase que expresen exactamente estos pares para validación de datos, sin tocar la semántica OWL del módulo ni la fidelidad a CIDOC-CRM. No resuelve la desconexión visual en el grafo actual (que lee directamente el RDF/OWL), pero sí documenta y valida formalmente el uso previsto.

### 4.2 Discrepancia real con el CIDOC-CRM oficial: `P150_defines_typical_parts_of`

El diagrama V8 usa esta propiedad como `E56_Language` → `E90_Symbolic_Object` (filas 96-97 del CSV). Verificado contra el archivo oficial vendored (`imports/vendor/cidoc-crm-7.1.3.rdf`):

```xml
<rdf:Property rdf:about="P150_defines_typical_parts_of">
  <rdfs:domain rdf:resource="E55_Type" />
  <rdfs:range rdf:resource="E55_Type" />
```

CIDOC-CRM 7.1.3 declara domain **y** range como `E55_Type` en ambos sentidos (una relación tipo-a-tipo). El domain propuesto por V8 (`E56_Language`) sí es válido — `E56_Language` es subclase de `E55_Type` en la jerarquía ya presente en el módulo, así que esa parte queda cubierta sin cambios. Pero el **range** (`E90_Symbolic_Object`) no es subclase de `E55_Type` — es una clase completamente distinta en la jerarquía. Esto **no es un vacío mecánico de extracción** (como sí lo fueron `P82`/`P90` en el informe anterior) sino una **reinterpretación deliberada** del equipo: usar esta propiedad para decir "este idioma define las partes típicas de este objeto simbólico concreto" en vez de su sentido oficial "este tipo de cosa define los tipos de partes típicas de otro tipo de cosa".

**No se aplicó ningún cambio.** Requiere una decisión explícita del equipo (candidato a un futuro ADR, mismo formato que los existentes): ¿se acepta esta reinterpretación como aportación propia de CAO_CRM (documentada, justificada, similar en espíritu a la decisión ya tomada para `P3_has_note` en problemes-et-solutions.md), o se ajusta el uso en el diagrama V8 al patrón oficial `E55_Type`→`E55_Type`?

## 5. Verificación tras aplicar las 12 inserciones seguras

| Chequeo | Resultado |
|---|---|
| Sintaxis (`rapper`) | PASS — 807 triples, 0 issues |
| Razonador (`robot reason`, HermiT) | PASS — consistente, sin log de errores/insatisfacibles |
| Metadatos (`validation/07-metadata/check.sh`) | PASS — 7/7 (4 presencia + 3 anti-contaminación SKOS) |
| Nodos aislados en el grafo dominio-rango | 9 → 5 (las 5 restantes, ver sección 4.1, requieren decisión colectiva, no un fix mecánico) |

Copia de respaldo del archivo previo a esta intervención guardada en el scratchpad de la sesión (fuera del repo, ya que este no usa git).

## 6bis. Segunda ronda (misma fecha): extracción directa del diagrama + validación contra los archivos oficiales completos

A raíz de una observación del usuario sobre el patrón de etiqueta `Propiedad\n(iPropiedad)` en las flechas del diagrama, se rehizo el análisis **sin pasar por `properties_extracted.csv`**, directamente sobre `CRM_V8.json`:

- Se extrajeron **265 aristas** con ese patrón de etiqueta en las 9 páginas del diagrama, resolviendo la clase real de cada extremo por proximidad de caja. **18 aristas se descartaron explícitamente** por apuntar a un punto de conexión huérfano (sin caja de clase asociada) — no se adivinó ninguna, para no introducir ruido. Quedaron **64 triples únicos (dominio, propiedad, rango)**.
- Cada uno se validó contra los **archivos oficiales completos** (`imports/vendor/cidoc-crm-7.1.3.rdf`, `lrmoo-1.1.1.rdf`, `crmdig-5.0.rdf` — no solo el subconjunto de 29 clases del módulo), comprobando que el dominio/rango usado en el diagrama sea, o sea subclase de, el dominio/rango que la propiedad tiene oficialmente declarado. Resultado: **56 LEGAL, 8 ILEGAL** (estos 8 son los mismos ocho problemas de modelado documentados, ya con su decisión y cita oficial de respaldo, en `problemes-et-solutions.md`; la nota interna de la primera ronda de discusión de estos hallazgos, dirigida a la coordinación del equipo para arbitraje colegiado, no forma parte de este repositorio).

**Confirmación importante sobre la fila 148 descartada en la sección 2:** se verificó independientemente contra el diagrama — la arista real (`E7_Activity`→`E21_Person` vía `P14_carried_out_by`) está correctamente etiquetada en 3 páginas del diagrama; el problema fue exclusivamente de la herramienta que generó el CSV al partir esa etiqueta de dos líneas, no un error del diagrama ni una pérdida de información real.

**Hallazgo nuevo: el diagrama mismo (no el CSV) contiene 2 nombres de propiedad mal escritos**, en el texto entre paréntesis de dos aristas de la página `exemple`/`F1`/`model`:
- `P67i_is_referred_to_by (P67_referes_to)` — el nombre correcto es `P67_refers_to`.
- `R16_created (R16i_was_ceated_by)` — el nombre correcto es `R16i_was_created_by`.

Al integrar esta segunda ronda se detectaron y revirtieron automáticamente **dos inserciones erróneas** que este mismo proceso había aplicado por error (tomó el texto entre paréntesis del diagrama sin validarlo, creando dos propiedades-fantasma `P67_referes_to` y `R16i_was_ceated_by` con `rdfs:domain`/`rdfs:range` propios). Corregido: ahora el script valida que el nombre entre paréntesis corresponda a una propiedad ya declarada en el archivo antes de usarlo; si no, lo descarta y lo reporta en vez de crear una propiedad nueva. Re-verificado tras la corrección: 807 triples (igual que al final de la primera ronda, sin cambios netos), sintaxis/razonador/metadatos PASS.

**Resultado de integrar los 56 LEGAL: 0 inserciones nuevas** — los 12 pares de la primera ronda (sección 3) ya cubrían todo lo que esta validación más completa (contra el esquema oficial íntegro, no solo nuestras 29 clases) confirma como correcto. Esto es una confirmación cruzada útil: las 12 inserciones de la sección 3 quedan doblemente verificadas.

## 6. Resumen para retomar la discusión colectiva

Quedan exactamente 2 asuntos abiertos de este informe, ninguno aplicado, ambos documentados arriba con todas las clases/filas candidatas:

1. **7 propiedades genéricas** (`P104_is_subject_to`, `P2_has_type`, `P4_has_time-span`, `P7_took_place_at`, `P16_used_specific_object`, `P1_is_identified_by` y sus inversas) usadas legítimamente sobre múltiples clases — decidir si se deja así, se modela con restricciones OWL por clase, o se pasa a SHACL.
2. **`P150_defines_typical_parts_of`** — decidir si la reinterpretación `E56_Language`→`E90_Symbolic_Object` del diagrama V8 se documenta como aportación propia (ADR-005) o se corrige el uso al patrón oficial `E55_Type`→`E55_Type`.

Además, quedó pendiente de decisión aparte (no incluida en este informe por estar fuera de su alcance): si las filas 52-199 del CSV (datos literales reales del caso "Le Rouge et le Noir") se cargan como datos de ejemplo en `test-data/` para alimentar las competency questions, todavía pendientes de expertise de dominio de Ariane.
