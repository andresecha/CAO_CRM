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
# Auditoría 1 (RDF) — verificación línea por línea de `CAO_CRM-1.0.rdf`

**Fecha de la auditoría:** 6 de julio de 2026
**Agente:** primer auditor de una cadena de tres, independiente y sin confianza previa en ningún resumen
**Objeto auditado:** `ontology/CAO_CRM-1.0.rdf` (1407 líneas, 1058 triples RDF/XML), y su coherencia con `imports/vendor/cidoc-crm-7.1.3.rdf`, `imports/vendor/lrmoo-1.1.1.rdf`, `imports/vendor/crmdig-5.0.rdf`
**Método:** cada término se verificó con `grep` directo sobre los archivos vendorizados (no sobre resúmenes ni sobre las fichas de decisión), comparando URI, `rdfs:domain`, `rdfs:range`, `rdfs:subClassOf`/`rdfs:subPropertyOf` exactos. Se ejecutaron además los cuatro comandos de validación técnica pedidos, más un script propio en `rdflib` para clases aisladas.

---

## (a) Tabla de verificación término por término

### A.1 — 16+ términos extraídos por ROBOT (CIDOC-CRM / CRMdig)

| Término | Archivo fuente | URI verificada | domain/range/subClassOf en fuente oficial | domain/range/subClassOf en CAO_CRM-1.0.rdf | ¿Coincide? |
|---|---|---|---|---|---|
| `P127_has_broader_term` | cidoc-crm-7.1.3.rdf:3912 | `E55_Type → E55_Type`, inverso `P127i_has_narrower_term` | igual | igual (línea 387-402) | ✅ Sí |
| `P127i_has_narrower_term` | cidoc-crm-7.1.3.rdf:3927 | `E55_Type → E55_Type` | igual | igual (línea 912-923) | ✅ Sí |
| `E33_Linguistic_Object` | cidoc-crm-7.1.3.rdf:651 | `subClassOf E73_Information_Object` (nota: oficialmente también hereda de E89/E90 por transitividad documental, pero la declaración RDF directa es solo E73) | En CAO_CRM: `subClassOf E89_Propositional_Object` **y** `E90_Symbolic_Object` (línea 27-30) | 🟡 Ver nota 1 abajo | 🟡 Casi — ver nota |
| `P72_has_language` | cidoc-crm-7.1.3.rdf:2839 | `E33_Linguistic_Object → E56_Language`, inverso `P72i_is_language_of` | igual (línea 315-329) | igual | ✅ Sí |
| `P72i_is_language_of` | cidoc-crm-7.1.3.rdf:2853 | `E56_Language → E33_Linguistic_Object` | igual (línea 450-461) | igual | ✅ Sí |
| `E22_Human-Made_Object` | cidoc-crm-7.1.3.rdf:531 | `subClassOf E19_Physical_Object, E24_Physical_Human-Made_Thing` | En CAO_CRM: `subClassOf E18_Physical_Thing` únicamente (línea 1165-1173) | 🟡 Simplificado — ver nota 2 | 🟡 Casi — ver nota |
| `P54_has_current_permanent_location` | cidoc-crm-7.1.3.rdf:2523 | `domain E19_Physical_Object, range E53_Place` | **`domain E22_Human-Made_Object`** (línea 1015-1029) | 🔴 Dominio restringido manualmente — ver hallazgo H1 | 🔴 Divergencia deliberada, ver H1 |
| `P54i_is_current_permanent_location_of` | cidoc-crm-7.1.3.rdf:2537 | `domain E53_Place, range E19_Physical_Object` | `range E22_Human-Made_Object` (línea 677-688) | 🔴 mismo caso | 🔴 ver H1 |
| `P55_has_current_location` | cidoc-crm-7.1.3.rdf:2549 | `domain E19_Physical_Object, range E53_Place`, subPropertyOf `P53_has_former_or_current_location` | `domain E22_Human-Made_Object` (línea 415-430); **`subPropertyOf` de P53 no se reprodujo** | 🔴 + 🟡 ver H1 y H2 | 🔴/🟡 |
| `P55i_currently_holds` | cidoc-crm-7.1.3.rdf:2565 | `domain E53_Place, range E19_Physical_Object`, subPropertyOf `P53i_...` | `range E22_Human-Made_Object` (línea 1174-1184), sin subPropertyOf | 🔴 + 🟡 ver H1 y H2 | 🔴/🟡 |
| `E1_CRM_Entity` | cidoc-crm-7.1.3.rdf:231 | clase raíz, sin subClassOf | igual (línea 1134-1149) | — | ✅ Sí |
| `E41_Appellation` | cidoc-crm-7.1.3.rdf:734 | `subClassOf E90_Symbolic_Object` | igual (línea 1216-1232) | — | ✅ Sí |
| `P82_at_some_time_within` | cidoc-crm-7.1.3.rdf:3030 | `domain E52_Time-Span, range rdfs:Literal` (únicamente) | `range rdfs:Literal` **+** `range xsd:dateTime` (línea 189-202) | Cambio intencional (Problema 8) | ✅ Coincide con lo documentado — añade sin quitar |
| `P82a_begin_of_the_begin` | cidoc-crm-7.1.3.rdf:3042 | `subPropertyOf P82_at_some_time_within`, `range rdfs:Literal` | + `xsd:dateTime` + `owl:propertyDisjointWith P82b_end_of_the_end` (línea 655-668) | ✅ Coincide con Problema 8, incluida la restauración del axioma de Mélanie | ✅ Sí |
| `P82b_end_of_the_end` | cidoc-crm-7.1.3.rdf:3053 | `subPropertyOf P82_at_some_time_within`, `range rdfs:Literal` | + `xsd:dateTime` (línea 176-188) | ✅ Sí (el propertyDisjointWith es simétrico por semántica OWL2, basta una dirección) | ✅ Sí |
| `P90_has_value` | cidoc-crm-7.1.3.rdf:3117 | `domain E54_Dimension, range rdfs:Literal` | + `range xsd:integer` (línea 1049-1062) | ✅ Sí | ✅ Sí |
| `E58_Measurement_Unit` | cidoc-crm-7.1.3.rdf:844 | `subClassOf E55_Type` | igual (línea 1233-1246) | — | ✅ Sí |
| `P91_has_unit` | cidoc-crm-7.1.3.rdf:545 (bloque compuesto, ver ontología 2.5 línea 545-558) | `domain E54_Dimension, range E58_Measurement_Unit` | igual | — | ✅ Sí |
| `P91i_is_unit_of` | — | `domain E58_Measurement_Unit, range E54_Dimension` | igual (línea 967-978) | — | ✅ Sí |
| `F32_Item_Production_Event` | lrmoo-1.1.1.rdf:73 | `subClassOf E12_Production` | igual (línea 1113-1118) | — | ✅ Sí |
| `D9_Data_Object` | crmdig-5.0.rdf:43 | `subClassOf E31_Document, D1_Digital_Object` | **solo `subClassOf D1_Digital_Object`** (línea 1043-1048); falta `E31_Document` | 🟡 simplificación de ROBOT — ver nota 3 | 🟡 Casi |
| `D7_Digital_Machine_Event` | crmdig-5.0.rdf:32 | `subClassOf E11_Modification, E65_Creation` | **solo `subClassOf E7_Activity`** (línea 1389-1394) | 🟡 simplificación de ROBOT — ver nota 3 | 🟡 Casi |

### A.2 — 6 términos LRMoo nuevos (relaciones F1↔F1, F2↔F2)

| Término | lrmoo-1.1.1.rdf | domain/range oficial | CAO_CRM-1.0.rdf | ¿Coincide? |
|---|---|---|---|---|
| `R2_is_derivative_of` | línea 114 | `F1_Work → F1_Work`, `subPropertyOf R68_is_inspired_by` | igual (línea 1333-1340); **subPropertyOf R68 no se reprodujo** (🟡 pérdida menor de jerarquía, R68 fuera del módulo) | ✅ domain/range / 🟡 jerarquía |
| `R2i_has_derivative` | línea 122 | `F1_Work → F1_Work` | igual (línea 1348-1353) | ✅ Sí |
| `R76_is_derivative_of` | línea 559 | `F2_Expression → F2_Expression`, `subPropertyOf P130_shows_features_of` | igual domain/range (línea 935-942); subPropertyOf no reproducido (🟡, P130 fuera de módulo) | ✅ / 🟡 |
| `R76i_has_derivative` | línea 566 | `F2_Expression → F2_Expression` | igual (línea 1186-1191) | ✅ Sí |
| `R75_incorporates` | línea 531 | `F2_Expression → F2_Expression`, `subPropertyOf P165_incorporates` | igual domain/range (línea 669-676); subPropertyOf no reproducido (🟡) | ✅ / 🟡 |
| `R75i_is_incorporated_in` | línea 539 | `F2_Expression → F2_Expression` | igual (línea 1377-1382) | ✅ Sí |

### A.3 — 3 subpropiedades P14 declaradas manualmente

| Término | domain/range/subPropertyOf declarado | ¿Analogía exacta con `P14_carried_out_by`? |
|---|---|---|
| `P14_a_pour_auteur_original` | `owl:ObjectProperty`, `domain E7_Activity`, `range E39_Actor`, `subPropertyOf P14_carried_out_by` (línea 994-1001) | ✅ Sí — domain/range idénticos al padre verificado en cidoc-crm-7.1.3.rdf:1489 (`domain E7_Activity`, `range E39_Actor`) |
| `P14_a_pour_traducteur` | ídem (línea 478-485) | ✅ Sí |
| `P14_a_pour_abregeur` | ídem (línea 1305-1312) | ✅ Sí |

**Verificación de la Encoding Rule 4** (`imports/vendor/cidoc-crm-7.1.3.rdf`, líneas 33-40, texto confirmado por lectura directa):
```
RDF does not support properties of properties, therefore, users may create their own
subProperties for CRM properties that have a type property such as "P3 has note":
Instead of P3 has note (P3-1 has type : parts description) declare
<rdf:Property rdf:about="P3_parts_description">
   <rdfs:domain rdf:resource="E1_CRM_Entity"/>
   <rdfs:range rdf:resource="http://www.w3.org/2000/01/rdf-schema#Literal"/>
   <rdfs:subPropertyOf rdf:resource="P3_has_note"/>
</rdf:Property>
```
El patrón oficial usa: mismo `domain` que el padre, mismo `range` que el padre, `rdfs:subPropertyOf` hacia el padre. Las tres subpropiedades P14 reproducen exactamente esta estructura, con `domain`/`range` verificados idénticos a los de `P14_carried_out_by` (`E7_Activity`/`E39_Actor`, cidoc-crm-7.1.3.rdf:1489-1502). La única diferencia con el ejemplo textual de la regla es que el ejemplo es para una `DatatypeProperty` (rango literal) y aquí se trata de una `ObjectProperty` (rango `E39_Actor`) — diferencia obligada por la naturaleza de `P14_carried_out_by` mismo (que ya es `ObjectProperty` en el archivo oficial), no una desviación del método. **Veredicto: analogía exacta y correctamente adaptada.** Confirma además lo que cita `informe-P14-roles-autorat.md` sobre el Issue 588 del CIDOC-CRM SIG, que generaliza esta misma regla a cualquier propiedad ".1", no solo a `P3.1`.

---

## Notas sobre las divergencias marcadas 🟡 en la tabla A.1

**Nota 1 — `E33_Linguistic_Object`:** el archivo oficial declara únicamente `rdfs:subClassOf E73_Information_Object` en su triple RDF directo (línea 651-663 de `cidoc-crm-7.1.3.rdf`, confirmado con `grep`). `CAO_CRM-1.0.rdf` declara en cambio `subClassOf E89_Propositional_Object` y `E90_Symbolic_Object` — que son superclases *transitivas* correctas de `E73_Information_Object` en la jerarquía completa de CIDOC-CRM, pero `E73_Information_Object` mismo **no está declarado como clase en el módulo** (no aparece en `CAO_CRM-1.0.rdf`). Es decir: ROBOT (o quien construyó la extracción) sustituyó el padre inmediato ausente por sus abuelos presentes en el módulo, preservando el efecto de la jerarquía sin dejar una referencia colgante. Confirmado con el script de clases huérfanas (sección c): no hay ninguna referencia a clase no declarada. Esto es una simplificación de cierre de módulo, no un error — pero es una diferencia real frente a la declaración literal del archivo vendorizado, y debía señalarse.

**Nota 2 — `E22_Human-Made_Object`:** mismo patrón que la Nota 1. El oficial declara `subClassOf E19_Physical_Object, E24_Physical_Human-Made_Thing`; ninguna de las dos está presente como clase en el módulo, así que se sustituyó por `E18_Physical_Thing` (ancestro común verificado: `E19_Physical_Object ⊂ E18_Physical_Thing` y `E24_Physical_Human-Made_Thing ⊂ E18_Physical_Thing`, ambos confirmados en el archivo oficial). Efecto neto sobre el razonamiento: nulo (no se pierde ninguna inferencia que el módulo necesite), pero de nuevo es una reescritura, no una copia literal.

**Nota 3 — `D9_Data_Object` y `D7_Digital_Machine_Event`:** incompletos frente al oficial por la misma razón de cierre de módulo (`E31_Document`, `E11_Modification`, `E65_Creation` no están en el módulo). Sin impacto detectado en el razonador (0 clases insatisfacibles, ver sección b), pero **si en el futuro se necesita usar `L20_has_created` o el detalle de `D11_Digital_Measurement_Event` que sí menciona `E65_Creation` en su nota de balisaje, faltará ese eslabón.** Marcado 🟡 porque no bloquea nada hoy pero reduce la fidelidad de la jerarquía frente al original.

---

## Hallazgos etiquetados

### 🔴 H1 — Restricción de dominio de `P54`/`P55` a `E22_Human-Made_Object`: verificado como intencional, pero con una laguna lógica real

Confirmado en el archivo oficial (`cidoc-crm-7.1.3.rdf:2523-2580`): `P54_has_current_permanent_location` y `P55_has_current_location` tienen oficialmente `rdfs:domain E19_Physical_Object` / `rdfs:range E19_Physical_Object` (según dirección), **no** `E22_Human-Made_Object`. `E19_Physical_Object` **no existe en ningún lugar de `CAO_CRM-1.0.rdf`** (grep negativo confirmado). La sustitución del dominio por `E22_Human-Made_Object` (la subclase concreta relevante para `F5_Item`) es coherente con lo que describe `problemes-et-solutions.md` (Problema 3): la única necesidad real detectada en todo el modelo es localizar el `F5_Item` físico, y el propio comentario oficial de `F5_Item` confirma la doble pertenencia de clase (`F5_Item` / `E22_Human-Made_Object`) como el patrón normal para libros.

**Verificado exhaustivamente que este es el único uso real de `P54`/`P55` en el módulo** (grep de `P54_has_current_permanent_location\b` y `E19_Physical_Object` en todo el archivo: 0 ocurrencias adicionales) — no hay ninguna otra clase que reclame esta propiedad, por lo que restringir el dominio a una sola clase no genera un conflicto de intersección con otro uso concurrente. Confirmado también que `F5_Item` **no está declarado formalmente `rdfs:subClassOf E22_Human-Made_Object`** en el TBox (línea 1383-1388: solo `subClassOf E18_Physical_Thing`) — la doble pertenencia de clase depende, tal como documenta `problemes-et-solutions.md`, de que cada instancia real de `F5_Item` se co-tipe manualmente como `E22_Human-Made_Object` al cargar los datos. Esto **no es un error lógico** (no genera inconsistencia, confirmado por el razonador HermiT: 0 insatisfacibles) pero es una dependencia de disciplina de captura de datos, no una garantía estructural del esquema. Si en el futuro alguien asigna `P54`/`P55` directamente a una instancia tipada solo como `F5_Item` (sin el co-tipado `E22_Human-Made_Object`), el razonador **inferirá silenciosamente** que esa instancia también es `E22_Human-Made_Object` (regla RDFS de dominio) en lugar de señalar un error — comportamiento válido en OWL/RDFS de mundo abierto, pero puede ocultar errores de captura de datos en la práctica.

**Veredicto sobre H1: la restricción es segura desde el punto de vista lógico (no hay otro uso concurrente, no genera inconsistencia), pero es una divergencia real y no documentada como tal dentro del propio archivo RDF** (el `rdfs:comment` heredado de `P54`/`P55` sigue mencionando literalmente "E19 Physical Object" en su texto, mientras que el `rdfs:domain` real ya dice `E22_Human-Made_Object` — un desfase entre comentario y axioma real que puede confundir a un futuro editor). Clasificado 🔴 no porque bloquee la producción, sino porque es el tipo de discrepancia comentario/axioma que debe corregirse antes de considerar el archivo "limpio": se recomienda añadir una nota propia (`rdfs:comment` adicional en francés/español, como ya se hace en las subpropiedades P14) explicando la restricción deliberada, en vez de dejar el comentario oficial sin editar contradiciendo al axioma.

### 🟡 H2 — Pérdida de `rdfs:subPropertyOf` en varias propiedades extraídas

`P55_has_current_location`/`P55i_currently_holds` pierden su `subPropertyOf P53_has_former_or_current_location`/`P53i_...` (el padre `P53` no está en el módulo). `R2_is_derivative_of` pierde `subPropertyOf R68_is_inspired_by`. `R76_is_derivative_of` pierde `subPropertyOf P130_shows_features_of`. `R75_incorporates` pierde `subPropertyOf P165_incorporates`. En todos los casos la clase padre de la subpropiedad no forma parte del módulo, así que ROBOT (o la extracción manual) omitió el eslabón en vez de dejar una referencia colgante — comportamiento consistente y no genera triples rotos (confirmado: 0 referencias huérfanas, sección c). Efecto práctico: se pierde la posibilidad de inferir automáticamente los triples más generales (p. ej. que un `R2_is_derivative_of` implica también un `R68_is_inspired_by`) si algún día se decide importar esos términos. No bloquea nada hoy. Clasificado 🟡.

### 🟡 H3 — `imports/module-terms.txt` no se actualizó con los nuevos términos de 2.5

El propio `dcterms:abstract` de `CAO_CRM-1.0.rdf` (línea 794) afirma: *"el conjunto exacto de clases y propiedades necesarias (documentado en imports/module-terms.txt) fue extraído... con la herramienta ROBOT"*. Verificado con `grep`: **ninguno** de los 16 términos ROBOT-extraídos ni de los 6 términos LRMoo nuevos aparece en `imports/module-terms.txt` (127 líneas, todavía reflejando solo el alcance del borrador inicial). Esto rompe la trazabilidad/reproducibilidad que el propio archivo afirma tener: si alguien intentara reproducir `CAO_CRM-1.0.rdf` ejecutando `robot extract --method subset --term-file imports/module-terms.txt` hoy, obtendría de nuevo el alcance del borrador inicial, no el actual. No es un error del RDF en sí, pero es una inconsistencia de gobernanza/documentación que debe corregirse antes de considerar el trabajo de hoy completamente cerrado. Clasificado 🟡 (no bloqueante para el RDF, pero sí para la reproducibilidad declarada).

### 🟡 H4 — El changelog interno (`dcterms:description`) no menciona todos los cambios reales

`CAO_CRM-1.0.rdf` línea 797: *"CAO_CRM-2.5: adds 16 terms and restores XSD precision per decisions/fr/problemes-et-solutions.md (2026-07-06)."* Esta descripción no menciona: (i) las 6 propiedades LRMoo de relación (`R2`/`R2i`/`R75`/`R75i`/`R76`/`R76i`), (ii) las 3 subpropiedades `P14_a_pour_*`, (iii) la restricción de dominio de `P54`/`P55`. El recuento real de términos nuevos (verificado por diff programático entre el borrador inicial del módulo y `CAO_CRM-1.0.rdf`) es **27**, no 16. Menor, pero recomendable de corregir para que el metadato interno de versión sea una bitácora fiel.

### 🟡 H5 — Ninguna subpropiedad `P14_a_pour_*` tiene una propiedad inversa declarada

A diferencia del resto del patrón del archivo (que declara sistemáticamente pares directa/inversa, p. ej. `P14_carried_out_by`/`P14i_performed`), las tres subpropiedades de rol no tienen un equivalente `P14i_a_ete_...`. No es un error — el propio `informe-P14-roles-autorat.md` no lo exige — pero rompe la simetría estilística del resto del archivo. Sin impacto lógico.

### Sin hallazgos 🔴 adicionales
No se encontraron triples contradictorios, tipos incompatibles (`owl:ObjectProperty` con rango literal o viceversa), URIs mal formadas, ni declaraciones duplicadas (verificado: cada `rdf:about` aparece exactamente una vez en el archivo, 0 duplicados). El eje `owl:propertyDisjointWith` entre `P82a`/`P82b` es sintácticamente correcto y semánticamente simétrico por definición de OWL2 (no requiere declarar ambas direcciones).

---

## (b) Resultado de los comandos de validación ejecutados

### 1. Sintaxis (`validation/01-syntax/check.sh`)
```
$ bash validation/01-syntax/check.sh ontology/CAO_CRM-1.0.rdf
rapper: 0 issue(s) — see validation/01-syntax/out/rapper.log
riot: see validation/01-syntax/out/riot.log
rdflib: see validation/01-syntax/out/rdflib.log
```
Contenido real de los logs:
```
rapper.log:
rapper: Parsing URI file:///.../ontology/CAO_CRM-1.0.rdf with parser rdfxml
rapper: Serializing with serializer ntriples
rapper: Parsing returned 1058 triples

riot.log: (vacío — sin errores)

rdflib.log:
OK: parsed 1058 triples
```
**Resultado: PASS, sin advertencias, en los tres analizadores.**

### 2. Fusión + razonamiento (`imports/merge.sh` + `validation/02-reasoning/check.sh`)
```
$ bash imports/merge.sh ontology/CAO_CRM-1.0.rdf imports/merged-2.5-audit.ttl
22:00:37 INFO  riot :: File: ../ontology/CAO_CRM-1.0.rdf
22:00:37 INFO  riot :: File: vendor/cidoc-crm-7.1.3.rdf
22:00:38 INFO  riot :: File: vendor/crmdig-5.0.rdf
22:00:38 INFO  riot :: File: vendor/lrmoo-1.1.1.rdf
22:00:38 INFO  riot :: File: vendor/skos.rdf
Merged 5 files -> imports/merged-2.5-audit.ttl

$ bash validation/02-reasoning/check.sh imports/merged-2.5-audit.ttl
PASS: ontology consistent, no unsatisfiable classes reported.
```
Nota de auditoría: el archivo fusionado generado de forma independiente por este auditor resultó **byte-idéntico** (`diff` sin diferencias) al `imports/merged-2.5.ttl` ya presente en el repositorio de trabajos previos de hoy — confirma que la fusión es reproducible y no hay manipulación posterior. `reason.log` queda vacío porque ROBOT no emite salida por stdout cuando no hay errores (comportamiento normal, confirmado ejecutando el comando de razonamiento manualmente por separado: exit code 0, archivo `reasoned.ttl` de 7389 líneas generado, 0 ocurrencias de `owl:Nothing` o "unsatisfiable"/"inconsistent" en el resultado). **Resultado: PASS — 0 clases insatisfacibles, ontología consistente**, verificado sobre la fusión completa (módulo CAO_CRM + CIDOC-CRM 7.1.3 + LRMoo 1.1.1 + CRMdig 5.0 + SKOS íntegros, no solo el módulo acotado).

(El archivo `imports/merged-2.5-audit.ttl` generado para esta auditoría fue borrado al finalizar, por ser idéntico al ya existente `imports/merged-2.5.ttl` — no se dejó ningún archivo nuevo aparte de esta auditoría, conforme a la instrucción de no modificar el repositorio más allá del informe.)

### 3. Metadatos (`validation/07-metadata/check.sh`)
```
$ bash validation/07-metadata/check.sh ontology/CAO_CRM-1.0.rdf
PASS (expect True, got True) ASK { ?o a owl:Ontology ; owl:versionIRI ?v . }
PASS (expect True, got True) ASK { ?o a owl:Ontology ; dc:creator ?c . }
PASS (expect True, got True) ASK { ?o a owl:Ontology ; dc:rights ?r . }
PASS (expect True, got True) ASK { ?o a owl:Ontology ; owl:versionInfo ?vi . }
PASS (expect False, got False) ASK { ?o a owl:Ontology ; terms:title "SKOS Vocabulary"@en . }
PASS (expect False, got False) ASK { ?o a owl:Ontology ; terms:creator "Alistair Miles" . }
PASS (expect False, got False) ASK { ?o a owl:Ontology ; terms:contributor "Dave Beckett" . }
```
**Resultado: PASS 7/7.**

### 4. Script propio (`rdflib`) — clases aisladas
Criterio aplicado: una clase se considera "aislada" si nunca aparece como `rdfs:domain`, `rdfs:range`, ni como sujeto/objeto de `rdfs:subClassOf` de ninguna propiedad/clase del archivo.
```
Total owl:Class declarations: 37
Classes with NO domain/range/subClassOf involvement: 0
Classes never appearing as domain, range, subClassOf(subj/obj), or type of any individual: 0
```
**Resultado: 0 clases aisladas.** Verificado también, con un segundo script, que no existen referencias "colgantes" (clases usadas como `domain`/`range`/`subClassOf` pero nunca declaradas `owl:Class` en el propio archivo): **0 referencias huérfanas** — confirma que las simplificaciones de jerarquía descritas en las Notas 1-3 no dejaron ningún enlace roto.

### Estadísticas adicionales verificadas
- Triples totales: 1058 (los tres analizadores de sintaxis coinciden).
- `owl:Class`: 37. `owl:ObjectProperty`: 80. `owl:DatatypeProperty`: 5.
- Términos nuevos frente al borrador inicial del módulo (diff programático): **27** (no 16 — ver H4). Ningún término fue eliminado (todos los términos del borrador inicial siguen presentes en `CAO_CRM-1.0.rdf`).
- 0 declaraciones `rdf:about` duplicadas en todo el archivo.

---

## (c) Resumen de problemas encontrados

| # | Severidad | Resumen |
|---|---|---|
| H1 | 🔴 | Dominio de `P54`/`P55` restringido a `E22_Human-Made_Object` (correcto y sin conflicto lógico, único uso real verificado), pero el `rdfs:comment` heredado del oficial sigue hablando de `E19 Physical Object`, y la garantía de aplicabilidad depende de una disciplina de co-tipado en el ABox, no de un axioma `subClassOf` en el TBox — desfase comentario/axioma a corregir |
| H2 | 🟡 | Pérdida de `rdfs:subPropertyOf` hacia superpropiedades ausentes del módulo (`P53`, `R68`, `P130`, `P165`) en 4 propiedades — sin impacto práctico hoy |
| H3 | 🟡 | `imports/module-terms.txt` no se actualizó — rompe la reproducibilidad declarada en el propio `dcterms:abstract` del archivo |
| H4 | 🟡 | El `dcterms:description` interno dice "16 terms" cuando el recuento real de términos nuevos es 27; omite mencionar las relaciones LRMoo y las subpropiedades P14 |
| H5 | 🟡 | Las 3 subpropiedades `P14_a_pour_*` no tienen inversa declarada (rompe la simetría estilística del resto del archivo, sin impacto lógico) |
| Notas 1-3 | 🟡 | Simplificaciones de jerarquía (`E33_Linguistic_Object`, `E22_Human-Made_Object`, `D9_Data_Object`, `D7_Digital_Machine_Event`) sustituyen padres inmediatos ausentes del módulo por ancestros presentes — verificado sin huérfanos ni inconsistencia, pero divergen de la declaración literal del archivo oficial |

**Ningún hallazgo bloquea el funcionamiento técnico del archivo**: sintaxis limpia (tres analizadores), razonador HermiT consistente sobre la fusión completa con los cuatro vendors, 7/7 metadatos, 0 clases aisladas, 0 referencias huérfanas, 0 triples duplicados. El único hallazgo 🔴 (H1) no es un error lógico sino una discrepancia de documentación/comentario frente al axioma real, y una dependencia (razonable y ya documentada en `problemes-et-solutions.md`) de disciplina de captura de datos en el ABox.

---

## (d) Veredicto final

**Sí, la implementación RDF de `CAO_CRM-1.0.rdf` de hoy es técnicamente correcta y segura para pasar a producción**, con una condición menor recomendada antes del cierre definitivo (no antes de este paso de la cadena de auditorías):

1. Los 16 términos ROBOT-extraídos y los 6 términos LRMoo nuevos coinciden con sus fuentes oficiales en URI, `domain`/`range` y, salvo simplificaciones de cierre de módulo ya explicadas y sin impacto (Notas 1-3, H2), en jerarquía.
2. Las 3 subpropiedades `P14_a_pour_*` son una analogía exacta y correctamente adaptada del patrón oficial de la Encoding Rule 4 del CIDOC-CRM SIG, verificada palabra por palabra contra el preámbulo del archivo vendorizado.
3. La restricción de dominio de `P54`/`P55` a `E22_Human-Made_Object` es segura: es, verificado exhaustivamente, el único uso real de esas propiedades en el módulo, no genera ninguna inconsistencia (confirmado por HermiT), y es coherente con el diagnóstico ya documentado en `problemes-et-solutions.md` (Problema 3). El hallazgo 🔴 H1 señala una imprecisión de comentario/documentación y una dependencia de disciplina de datos, no un defecto lógico del esquema.
4. Los cuatro comandos de validación técnica (sintaxis, razonamiento sobre la fusión completa con los tres vendors + SKOS, metadatos, clases aisladas) pasan sin excepción, ejecutados de forma independiente por este auditor y no solo heredados de una ejecución previa.

**Recomendación antes de considerar el ciclo de hoy completamente cerrado** (no bloqueante para producción, pero sí para la próxima vez que alguien intente reproducir el módulo): actualizar `imports/module-terms.txt` (H3) y el `dcterms:description` interno (H4), y opcionalmente añadir un comentario propio junto a `P54`/`P55` explicando la restricción deliberada de dominio (H1), en vez de dejar el comentario oficial heredado sin editar.

No se modificó `CAO_CRM-1.0.rdf` ni ningún otro archivo del repositorio durante esta auditoría; el único archivo nuevo creado es este informe.
