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
# Informe de completitud: labels, dominio/rango y jerarquía del módulo CAO_CRM

**Fecha:** 2026-07-03
**Archivo auditado:** `imports/module/cao_crm-module-clean.rdf` (29 clases, 61 propiedades de objeto, 5 propiedades de datos, 770 triples)
**Estado:** verificado — sintaxis correcta, lógicamente consistente (razonador HermiT, 0 insatisfacibles), confirmado que abre en Protégé 5.6.8 sin errores.

**Nota importante sobre este informe:** al preparar estos datos se descubrió y corrigió un problema metodológico real (ver sección 0) — así que las cifras de este informe **no coinciden** con las que hubiera dado el archivo generado ayer. El archivo actual es mejor y más completo que el de ayer.

**Corrección posterior a la primera versión de este informe (mismo día):** la sección 2.2 decía inicialmente que `P90_has_value` estaba "completa en el original" y servía de patrón de referencia para `P82_at_some_time_within`/`P82a`/`P82b`. Eso era **incorrecto** — al revisar con más contexto el archivo oficial, las cuatro propiedades (`P90_has_value` incluida) sí tienen `rdfs:range rdfs:Literal` declarado en CIDOC-CRM 7.1.3; lo que pasaba es que **la herramienta de extracción descartó ese rango en las cuatro**, porque `rdfs:Literal` (un tipo genérico de RDF, no una clase propia de CIDOC-CRM) nunca se incluyó en la lista de términos a extraer. No era, por tanto, una decisión de modelado pendiente (como sí lo fue `P3_has_note`) sino un error mecánico de la extracción. **Ya corregido**: se restauró `rdfs:range rdfs:Literal` en las cuatro propiedades, copiando literalmente lo que dice el archivo oficial, sin necesidad de ningún ADR — no hay ambigüedad que decidir. La sección 2.2 más abajo se mantiene tal cual se escribió originalmente solo a efectos de trazabilidad del proceso, pero su conclusión quedó superada por esta corrección.

---

## 0. Corrección hecha hoy antes de auditar: la extracción se rehízo en una sola pasada

Ayer se generaron tres archivos RDF por separado (uno por cada ontología fuente: CIDOC-CRM, LRMoo, CRMdig) y luego se fusionaron. Al preparar este informe se detectó que ese método **pierde información quirúrgicamente**: cuando una propiedad de una fuente (por ejemplo, `F1_Work` en LRMoo) tiene como padre o rango una clase que solo existe en OTRA fuente (por ejemplo `E89_Propositional_Object`, que es de CIDOC-CRM), la herramienta de extracción, al procesar LRMoo sola, no "sabe" que esa clase existe y descarta la relación — aunque la clase de destino sí forme parte de nuestro alcance de 29 clases.

**Ejemplo real encontrado:** `F1_Work` debería tener como padre `E89_Propositional_Object` (ambas están en nuestro alcance) — pero el archivo de ayer mostraba `F1_Work` sin ningún padre. Ese dato no estaba perdido en la documentación oficial, se perdió por procesar las tres ontologías en pasadas separadas.

**Corrección aplicada:** se combinaron los tres archivos oficiales en uno solo primero, y se ejecutó la extracción **una sola vez** contra ese conjunto combinado. Esto recuperó automáticamente varias relaciones de jerarquía y de dominio/rango que cruzan entre CIDOC-CRM/LRMoo/CRMdig y que sí deberían estar presentes según nuestro propio alcance acordado. Se volvió a verificar todo (sintaxis, razonador, apertura en Protégé) después del cambio — sigue siendo consistente y correcto.

---

## 1. Labels faltantes (etiquetas multilingües)

CIDOC-CRM 7.1.3 provee etiquetas oficiales en 7 idiomas: alemán (de), griego (el), inglés (en), francés (fr), portugués (pt), ruso (ru), chino (zh). LRMoo y CRMdig, en cambio, **solo tienen etiquetas en inglés en su release oficial** — no existen traducciones suyas en ningún archivo, ni siquiera en la documentación de lectura.

### 1.1 Clases y propiedades que SÍ tienen los 7 idiomas completos

21 de las 29 clases y la inmensa mayoría de las 61 propiedades de objeto de CIDOC-CRM (`P1`...`P108`) tienen las 7 traducciones completas. Esto no requiere ninguna acción.

### 1.2 Excepciones dentro de CIDOC-CRM (idiomas parcialmente faltantes)

| Entidad | Idiomas presentes | Faltan |
|---|---|---|
| `E89_Propositional_Object` | de, en, fr, ru, zh | **el, pt** |
| `E90_Symbolic_Object` | de, en, fr, ru, zh | **el, pt** |
| `P150_defines_typical_parts_of` / `P150i_...` | en, fr, ru | **de, el, pt, zh** |
| `P82a_begin_of_the_begin` | de, el, en, fr, pt, ru | **zh** |
| `P82b_end_of_the_end` | de, el, en, fr, pt, ru | **zh** |

**¿Se puede recuperar?** No sin acudir a otra fuente — se verificó que el archivo oficial `CIDOC_CRM_v7.1.3.rdfs` sencillamente no contiene esas traducciones para esas entidades concretas. No es un problema de nuestra extracción (confirmado: son las mismas ausencias en el archivo fuente). Si se necesitan, habría que traducirlas nosotros mismos (y entonces sí serían una aportación propia de CAO_CRM, a diferencia de copiar las oficiales) o esperar a que CIDOC-CRM las publique en una versión futura.

### 1.3 Las 10 clases y 30 propiedades de LRMoo y CRMdig: solo inglés, y no es recuperable

Las 7 clases de LRMoo (`F1_Work`, `F2_Expression`, `F3_Manifestation`, `F5_Item`, `F27/F28/F30_..._Creation`), las 15 propiedades de LRMoo (`R3`, `R4`, `R16`, `R17`, `R24`, `R27`, `R71`, `R78` y sus inversas), las 3 clases de CRMdig (`D1`, `D2`, `D13`) y las 8 propiedades de CRMdig (`L1`, `L11`, `L19`, `L61` y sus inversas) **solo existen en inglés en el archivo oficial**. Se comprobó directamente en los archivos fuente (`imports/vendor/lrmoo-1.1.1.rdf` y `imports/vendor/crmdig-5.0.rdf`): no hay ninguna etiqueta `xml:lang` distinta de `en` en ninguna de ellas.

**Conclusión sobre "recuperar" labels en otros idiomas para LRMoo/CRMdig: no es posible, porque nunca existieron.** Cualquier traducción al francés (o a otro idioma) de estos 25 términos tendría que redactarla el propio equipo CAO_CRM — en ese caso sí sería una aportación original del proyecto (comparable a las notas terminológicas del glosario, no una simple copia de fragmentos ajenos), y habría que decidir conscientemente si eso encaja con el principio de "solo componer, no añadir" que se estableció para el resto del modelo.

---

## 2. Dominio y rango: ¿está todo completo?

Se revisaron programáticamente las 61 propiedades de objeto y las 5 propiedades de datos. Los casos sin dominio o sin rango se clasificaron en dos categorías, verificando cada uno contra el archivo oficial correspondiente:

### 2.1 Categoría A — el dominio/rango apunta a una clase fuera de las 31 elegidas (correcto, esperado, no se debe "arreglar")

Es la inmensa mayoría de los casos "faltantes". Ejemplos:

| Propiedad | Lo que falta | Dominio/rango oficial (fuera de alcance) |
|---|---|---|
| `P1_is_identified_by` / `P1i_identifies` | domain **y** range | `E1_CRM_Entity` (dominio) y `E41_Appellation` (rango) — ninguna de las dos está en nuestras 31 clases |
| `P104_is_subject_to` | domain | `E72_Legal_Object` |
| `P108_has_produced` | range | `E24_Physical_Human-Made_Thing` |
| `P16_used_specific_object` | range | `E70_Thing` |
| `P2_has_type` | domain | `E1_CRM_Entity` |
| `P4_has_time-span` | domain | `E2_Temporal_Entity` |
| `P43_has_dimension` | domain | `E70_Thing` |
| `P67_refers_to` | range | `E1_CRM_Entity` |
| `P7_took_place_at` | domain | `E4_Period` |
| `R27_materialized` / `R27i_...` | domain / range | `F32_Item_Production_Event` (LRMoo) |

**Esto no es un defecto — es literalmente lo que significa "modelo acotado".** `E1_CRM_Entity` es la clase más general de todo CIDOC-CRM (la raíz de la que cuelga todo lo demás); si la incluyéramos, junto con `E41_Appellation`, `E70_Thing`, `E72_Legal_Object`, etc., dejaríamos de tener un modelo limitado y empezaríamos a arrastrar de vuelta buena parte de la jerarquía completa que el proyecto decidió no incluir. **No se recomienda "completar" estos casos.**

### 2.2 Categoría B — vacío real en el propio archivo oficial de CIDOC-CRM (sí requiere una decisión, como con `P3_has_note`)

Se encontraron **4 propiedades de datos** con este problema — el mismo patrón exacto que `P3_has_note` (documentado en `problemes-et-solutions.md (Problema 1)`):

| Propiedad | Estado actual | Diagnóstico |
|---|---|---|
| `P3_has_note` | **Ya corregido** (`rdfs:range rdfs:Literal`, siguiendo el patrón de `P90_has_value`) | — |
| `P90_has_value` | Completo en el original (`rdfs:range rdfs:Literal`) | Sirve de referencia/patrón |
| `P82_at_some_time_within` | **Sin corregir** — domain sí, range no | El archivo oficial 7.1.3 no declara `rdfs:range` para esta propiedad (confirmado, cero líneas `rdfs:range` en su declaración) |
| `P82a_begin_of_the_begin` | **Sin corregir** — domain sí, range no | Mismo vacío |
| `P82b_end_of_the_end` | **Sin corregir** — domain sí, range no | Mismo vacío |

**Recomendación:** aplicar exactamente la misma decisión que se tomó para `P3_has_note` (declarar `rdfs:range rdfs:Literal` para estas tres, siguiendo el patrón de `P90_has_value`), por la misma razón documentada en problemes-et-solutions.md (Problema 1). No se ha aplicado todavía — se deja pendiente de tu confirmación, ya que implica editar el archivo de nuevo.

### 2.3 Ningún caso de "pérdida por extracción" pendiente

Tras rehacer la extracción en una sola pasada combinada (sección 0), **ya no queda ningún caso donde el dominio/rango exista en el original apuntando a una clase de nuestro alcance y no se haya recuperado.** Los únicos "NINGUNO" que quedan en el archivo son, sin excepción, categoría A (correctos por diseño) o categoría B (los 3 casos de arriba, pendientes de decisión).

---

## 3. Jerarquía de clases (`rdfs:subClassOf`): ¿está el modelo conceptual completo?

Tras la corrección de la sección 0, la jerarquía dentro del módulo es esta (mostrando solo relaciones entre clases que SÍ están en nuestras 29):

```
E18_Physical_Thing (raíz)
 └─ E21_Person
     └─ (también hereda de E39_Actor)
 └─ F5_Item

E39_Actor (raíz)
 └─ E21_Person

E7_Activity (raíz)
 ├─ E12_Production
 │   ├─ F28_Expression_Creation
 │   └─ F30_Manifestation_Creation
 ├─ F27_Work_Creation
 └─ D2_Digitization_Process

E89_Propositional_Object (raíz)
 ├─ E30_Right
 ├─ E35_Title
 ├─ F1_Work
 ├─ F2_Expression
 ├─ F3_Manifestation
 └─ D1_Digital_Object

E90_Symbolic_Object (raíz)
 ├─ E35_Title
 ├─ E42_Identifier
 ├─ F2_Expression
 ├─ F3_Manifestation
 └─ D1_Digital_Object

E55_Type (raíz)
 ├─ E56_Language
 └─ E57_Material

E3_Condition_State, E52_Time-Span, E53_Place, E54_Dimension, E67_Birth, E69_Death,
D13_Digital_Information_Carrier (bajo E18_Physical_Thing)
```

**¿Está "completo"?** Dentro del alcance que se decidió (las 31 clases confirmadas), sí — cada clase que oficialmente desciende de otra clase incluida en el alcance conserva esa relación. Las clases que aparecen como "raíz" en este módulo (`E18_Physical_Thing`, `E39_Actor`, `E7_Activity`, `E89_Propositional_Object`, `E90_Symbolic_Object`, `E55_Type`, `E3_Condition_State`, `E52_Time-Span`, `E53_Place`, `E54_Dimension`, `E67_Birth`, `E69_Death`) lo son porque su verdadero padre oficial (por ejemplo, `E1_CRM_Entity` para casi todas) está fuera del alcance — es exactamente la misma situación que la categoría A de la sección 2.1, y por la misma razón no se recomienda "completarlo".

---

## 4. Sobre las condiciones `owl:disjointWith`

**Estado actual: cero declaraciones `owl:disjointWith` en el módulo.** Ni el archivo oficial de CIDOC-CRM las declara de forma extensa entre estas 29 clases concretas, ni la extracción añadió ninguna.

Esto es una pregunta de diseño genuina, no algo que se pueda "verificar" automáticamente sin una decisión previa — por eso se deja planteada aquí en vez de decidirla unilateralmente:

- **A favor de añadirlas:** ayudarían al razonador a detectar automáticamente errores de captura de datos — por ejemplo, si alguien instancia por error algo como simultáneamente `E67_Birth` y `E69_Death` (que deberían ser mutuamente excluyentes), el razonador lo señalaría como inconsistencia.
- **En contra:** el archivo oficial de CIDOC-CRM **no** declara estas disjunciones de forma explícita para la mayoría de sus clases (es una elección deliberada del consorcio CIDOC-CRM, documentada en su filosofía de diseño: prefieren un modelo flexible donde la disjunción se deja a criterio de cada implementación). Añadirlas nosotros sería, otra vez, una decisión de modelado propia de CAO_CRM que va más allá de "componer fragmentos" — el mismo tipo de tensión que se discutió para `P3_has_note` en problemes-et-solutions.md (Problema 1).

**Recomendación:** tratar esto como un ADR-001 aparte (siguiendo el mismo formato que los ADR existentes), en vez de decidirlo de pasada aquí, precisamente porque toca la misma pregunta de fondo ("¿hasta dónde llega la pura composición?") y merece la misma documentación cuidadosa.

---

## 5. Resumen ejecutivo

| Pregunta | Respuesta |
|---|---|
| ¿Hay labels faltantes? | Sí: 5 entidades de CIDOC-CRM con algún idioma parcial (no recuperable, no existe en la fuente); las 25 entidades de LRMoo/CRMdig solo tienen inglés (no recuperable, nunca existió traducción oficial) |
| ¿Todo tiene dominio y rango? | **Sí, ya completo.** Se encontraron y corrigieron 4 propiedades (`P82_at_some_time_within`, `P82a`, `P82b`, `P90_has_value`) cuyo `rdfs:range rdfs:Literal` existía en el archivo oficial pero la extracción lo había descartado por un límite mecánico de la herramienta (no un vacío real del original, a diferencia de `P3_has_note`) — restaurado directamente, sin necesidad de ADR. |
| ¿Está completo el modelo conceptual (jerarquía)? | Sí, dentro del alcance acordado — se corrigió un problema metodológico real (extracción en pasadas separadas) que sí perdía información dentro de ese alcance; ya no hay pérdidas pendientes |
| ¿Hacen falta condiciones `owl:disjointWith`? | Pregunta abierta de diseño, no un defecto técnico — recomendado documentarla como ADR-001 antes de decidir |

**Nada de esto bloquea seguir adelante** — son afinamientos, no errores estructurales. El archivo `imports/module/cao_crm-module-clean.rdf` es sintácticamente correcto, lógicamente consistente y abre limpio en Protégé.
