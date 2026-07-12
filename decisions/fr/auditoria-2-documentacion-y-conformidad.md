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
# Auditoría 2 — Verificación de la documentación y conformidad conceptual de `CAO_CRM-1.0.rdf`

**Fecha de la auditoría:** 6 de julio de 2026
**Agente:** segundo auditor de una cadena de tres, independiente de la auditoría 1 (RDF línea por línea, `auditoria-1-rdf.md`), cuyo trabajo no se repite aquí salvo para verificar que sus tres hallazgos 🟡 (H1, H3, H4) fueron efectivamente corregidos en el archivo actual.
**Método:** cada cita "textual" atribuida a un archivo oficial se verificó con `grep` directo sobre `imports/vendor/cidoc-crm-7.1.3.rdf`, `imports/vendor/lrmoo-1.1.1.rdf`, `imports/vendor/crmdig-5.0.rdf`; cada fragmento Turtle/RDF de ejemplo se contrastó contra el `CAO_CRM-1.0.rdf` real; el Issue 328 del CRM-SIG se verificó mediante fetch directo de `https://cidoc-crm.org/Issue/ID-328-rights-model`, no de memoria; los conteos cuantitativos del informe de comparación con Mélanie se recalcularon de forma independiente (`grep -c`, `rapper`, `md5sum`).

---

## 0. Verificación previa: ¿se cerraron los hallazgos H1/H3/H4 de la auditoría 1?

**Sí, las tres correcciones están aplicadas y son coherentes entre sí.** Verificado directamente sobre `ontology/CAO_CRM-1.0.rdf` e `imports/module-terms.txt`:

- **H3** — `imports/module-terms.txt` pasó de 127 a 171 líneas y ahora lista los 27 términos nuevos (`P127_has_broader_term`, las 3 subpropiedades `P14_a_pour_*`, `F32_Item_Production_Event`, `R2/R75/R76_*`, `D7_Digital_Machine_Event`, `D9_Data_Object`, etc.).
- **H4** — el `dcterms:description` (línea 716) ya dice explícitamente *"adds 27 new terms in total"* y detalla las cuatro familias de cambios, en vez de "16 terms".
- **H1** — `P54_has_current_permanent_location` y `P55_has_current_location` recibieron cada una un `rdfs:comment xml:lang="fr"` adicional (líneas 277 y 785) que explica la restricción de dominio a `E22_Human-Made_Object` y remite a `problemes-et-solutions.md`, sin borrar el comentario oficial heredado.

Estas tres correcciones no forman parte de los hallazgos de esta auditoría — se documentan aquí solo para que la cadena quede trazable.

---

## (a) Parte A — Verificación de la documentación

### A.1 — `problemes-et-solutions.md`

**Citas oficiales verificadas por `grep` directo** (muestreo exhaustivo sobre los 8 problemas + Problema 1b + la actualización del 6 de julio): todas las citas comprobadas coinciden palabra por palabra con los archivos vendorizados, incluyendo pasajes largos y poco obvios:
- `E55_Type` (jerarquías vía P127, ISO 25964-2 BTG) — coincide exacto (cidoc-crm-7.1.3.rdf).
- `P127_has_broader_term`, `P150_defines_typical_parts_of`, `E56_Language`, `E90_Symbolic_Object`, `E33_Linguistic_Object`, `P72_has_language`, `E3_Condition_State`, `E2_Temporal_Entity`/`E4_Period` (frase "two sister branches"), `P54`/`P55`/`F5_Item` (comentario LRMoo íntegro), `E72_Legal_Object`/`E30_Right`/`P104_is_subject_to`, `F1_Work`, `E7_Activity`, `D2_Digitization_Process`, `R3_is_realised_in`, `P16_used_specific_object`, `L11_had_output`, `R27_materialized`, `F32_Item_Production_Event`, `D9_Data_Object`, `D7_Digital_Machine_Event`, `L1_digitized` — **todas verificadas idénticas** al texto vendorizado, sin cortes engañosos ni paráfrasis presentada como cita literal.
- `E34_Inscription` (citada en la actualización del 6 de julio sobre "Système d'écriture") — verificada línea 678-680 de `cidoc-crm-7.1.3.rdf`: coincide exactamente, incluida la frase clave *"The alphabet used can be documented by P2 has type: E55 Type"*.

**Ejemplos Turtle contrastados contra `CAO_CRM-1.0.rdf` real:**
- El patrón `:expression_le_rouge_et_le_noir a lrmoo:F2_Expression, cidoc:E33_Linguistic_Object ; cidoc:P72_has_language ...` usa propiedades/clases que **sí** existen hoy en el archivo (`P72_has_language` línea 135-145, `E33_Linguistic_Object` línea 255-263) — coherente.
- Los ejemplos con `P14_a_pour_auteur_original`/`P14_a_pour_traducteur` usan propiedades que **sí** están declaradas (líneas 21-28, 1074-1081, 1292-1299).
- Los ejemplos con `R76_is_derivative_of`, `R75_incorporates`, `R2_is_derivative_of` — verificado que las tres están presentes en el archivo actual con domain/range `F2_Expression`/`F1_Work` correctos.

**Consistencia interna de la tabla de 8 problemas (encabezado) contra el cuerpo del documento:** ✅ consistente. La tabla resume "problema — dominio/portée exigido — naturaleza", sin marcar estados de resolución (a diferencia de `complete-model.md`), por lo que no hay contradicción posible entre "pendiente" en la tabla y "resuelto" en el cuerpo — ese riesgo simplemente no aplica a este documento porque su tabla no versiona estado.

**🟡 Hallazgo A.1.1 — inconsistencia de fecha/estado dentro del propio documento sobre "Système d'écriture":** el Problema 1 original (líneas 26-137) todavía presenta el patrón antiguo ("Système d'écriture" en `F5_Item`/`D1_Digital_Object`) como si fuera la solución vigente en su sección "État actuel"/"Proposition" (líneas 103-132) — y solo la sección añadida más abajo ("Mise à jour du 6 juillet 2026", línea 139) la corrige. Un lector que se detenga en el diagrama Mermaid de la línea 118-132 (antes de llegar a la actualización) se llevaría la versión ya superada. No es un error de contenido — la actualización existe y está bien fundamentada — pero el documento no reescribió ni marcó visualmente como obsoleto el diagrama Mermaid original, lo que puede inducir a error si se lee de forma no lineal (algo probable en un documento de 1284 líneas). Recomendación: añadir una nota "⚠ superado, ver más abajo" directamente sobre el diagrama Mermaid de la línea 118, no solo al final de la sección.

### A.2 — `complete-model.md`

**Verificación de la matriz 5×4 contra el cuerpo:** ✅ consistente. Cada celda marcada "✅ résolu"/"✅ légal" en la tabla de la sección 2 tiene su correspondiente justificación desarrollada en la sección 3 o ya en `problemes-et-solutions.md`; el tablero final (sección 5) refleja fielmente el estado de las 3 "Questions ouvertes" (2 resueltas, 1 con acción pendiente hacia el paper, no hacia el RDF) — no se encontró ninguna celda marcada resuelta en una tabla y pendiente en el texto, ni viceversa.

**Verificación puntual de exhaustividad (afirmación fuerte del documento, A.2 de `complete-model.md`):** *"Aucune propriété F2↔F2 supplémentaire trouvée [...] au-delà de ce qui est déjà dans le fichier vendorisé"*. Repetido el `grep` propio sobre `imports/vendor/lrmoo-1.1.1.rdf` para todas las propiedades `R*` con domain=range=`F2_Expression`: confirmado, únicamente `R75_incorporates`/`R76_is_derivative_of` (y sus inversas) cumplen esa condición. **Afirmación verificada correcta.**

**🟡 Hallazgo A.2.1 — línea 43 de `problemes-et-solutions.md`** vs. lo verificado aquí: no aplica (falso positivo descartado tras relectura). Sin más hallazgos en este documento.

### A.3 — `informe-P14-roles-autorat.md`

**Citas verificadas:**
- `P14_carried_out_by`, texto íntegro (líneas 1489-1502 de `cidoc-crm-7.1.3.rdf`): coincide exacto, incluida la frase *"The P14.1 in the role of property of the property specifies the nature of an Actor's participation"* — confirmado con `grep`, ni la coma ni el guion difieren.
- Encoding Rule 4 (preámbulo) — ya verificada palabra por palabra por el auditor 1; revalidada aquí de forma independiente, coincide.
- El ejemplo PC14/Michelangelo, el Issue 588, y las citas MARC/BIBFRAME/Linked Art/SARI son fuentes **externas** al repositorio (no vendorizadas) — no son re-verificables por `grep` local; el documento mismo declara honestamente el método de obtención (`curl` directo, fecha, tamaño de archivo) y no se encontró ninguna razón para dudar de su fidelidad, pero por definición esta auditoría no puede confirmar independientemente contenido no vendorizado sin volver a salir a internet, lo cual se hizo de forma selectiva (ver Parte B, punto 6, para el caso del Issue 328, que sí se revalidó).
- El código RDF propuesto para las 3 subpropiedades P14 (sección 5) coincide **exactamente**, campo por campo, con lo que hoy existe realmente en `CAO_CRM-1.0.rdf` (líneas 21-28, 1074-1081, 1292-1299) — la única diferencia es el label de `P14_a_pour_abregeur`, que en el informe se propone como "a pour abrégeur" pero en el RDF final quedó como "a pour abréviateur" (línea 1294). Diferencia menor, sin impacto semántico, pero es una divergencia real entre lo que el documento de decisión propone y lo que el RDF terminó implementando.

**🟡 Hallazgo A.3.1 — divergencia de etiqueta:** `informe-P14-roles-autorat.md` (líneas 244, 249) usa consistentemente el label "a pour abrégeur" en sus ejemplos propuestos; `CAO_CRM-1.0.rdf` línea 1294 declara en cambio `rdfs:label xml:lang="fr">a pour abréviateur`. Ambos términos son válidos en francés para el rol MARC "abr" (abridger), pero el documento de decisión y el RDF final no quedaron alineados textualmente — puede confundir a quien busque el término exacto citado en la ficha de decisión. Severidad menor.

### A.4 — `investigacion-complete-model-conclusiones.md` + `investigacion-complete-model-fuentes.md` (hoy `complete-model.md`)

> Nota: estos dos documentos, tal como existían en la fecha de esta auditoría, fueron
> posteriormente consolidados en `complete-model.md` (sección 6, "Sources et méthode de
> vérification"), que hoy contiene el mismo contenido de forma autocontenida. Las referencias de
> sección (A.2, A.3, B.1, sección E) citadas más abajo corresponden a la numeración de los
> documentos originales en la fecha de esta auditoría, no a `complete-model.md`.

**Verificación cruzada de las citas internas** (contra `imports/vendor/lrmoo-1.1.1.rdf` y `cidoc-crm-7.1.3.rdf`): `R74_uses_expression_of`, `R73_takes_representative_attribute_from`, `R79_has_representative_expression_attribute`, `R56_has_related_form`, `R36_uses_script_conversion`, `R68_is_inspired_by`, `R2_is_derivative_of`, `F36_Script_Conversion`, `E34_Inscription`, `F12_Nomen` — **todas verificadas exactas** contra el archivo vendorizado, incluyendo domain/range y `subPropertyOf` citados.

**Verificación de la afirmación negativa fuerte** (*"F52_Name_Use/R64 ausentes del fichero vendorisé, reconfirmado hoy con grep -c = 0 occurrence"*): reconfirmado independientemente, `grep -c "F52_Name_Use\|R64" imports/vendor/lrmoo-1.1.1.rdf` = 0. **Correcto.**

**Verificación del Issue 328** (fuente externa, sección B.1 de `complete-model.md`): ver Parte B, punto 6 — revalidado con WebFetch propio hoy, con una precisión menor sobre el número de reunión (ver más abajo).

**Sin hallazgos 🔴 en estos dos documentos.** Son, de los seis documentos auditados, los más disciplinados en señalar sus propios límites (sección E de `complete-model.md`, "Sources non consultées ou bloquées", es un ejercicio de honestidad metodológica poco común y que no requiere corrección).

### A.5 — `comparation/informe-evolucion-completa-Melanie-vs-2.5.md`

**Todos los conteos cuantitativos recalculados de forma independiente, coinciden:**
| Afirmación del informe | Verificación independiente | Resultado |
|---|---|---|
| MD5 de la copia con etiquetas añadidas = MD5 del archivo original entregado por Mélanie Bouland | `md5sum` ejecutado sobre ambos | ✅ idénticos (`f90c696826aa357d954a92387bcd81f5`) |
| 970 triples en el original | `rapper -i rdfxml -o ntriples` | ✅ "Parsing returned 970 triples" |
| 1058 triples en 2.5 | ya confirmado por auditor 1, revalidado | ✅ |
| 54 clases / 90 ObjectProperty / 16 DatatypeProperty (original) | `grep -c` sobre `owl:Class`/`owl:ObjectProperty`/`owl:DatatypeProperty rdf:about` | ✅ 54/90/16 exactos |
| 37 clases / 80 ObjectProperty / 5 DatatypeProperty (2.5) | `grep -c` sobre los tres tipos declarados vía `rdf:type` | ✅ 37/80/5 exactos |
| Namespace `ics.forth.gr` presente en el original, ausente en 2.5 | `grep -c "ics.forth.gr"` en el original = 33; `grep -c "cidoc-crm.org/extensions/crmdig"` en 2.5 = 35 | ✅ confirmado en ambas direcciones |
| `CAO_CRM.org/Movement_Name` sin reemplazo, punto abierto | `grep -c "Movement_Name"` en el original = 2 (label + about) | ✅ confirmado, sigue sin reemplazo en la ontología de hoy |

**No se encontró ningún tercer error** más allá de los dos que el propio autor ya corrigió (documentados explícitamente como correcciones en el Paso 4 y Paso 7 del informe: el caso `P104_is_subject_to` que sí existía correctamente en el original, y el caso `P90_has_value`/`E54_Dimension` que también existía correctamente). El informe es, de los seis, el que hace el trabajo de re-verificación cuantitativa más pesado, y resistió el recálculo íntegro sin fisuras.

**🟡 Hallazgo A.5.1 — matiz no destacado:** el informe presenta la reducción de clases (54→37) y propiedades (90+16→80+5) como prueba de que "menos no significa menos capacidad" (Paso 1), lo cual es cierto para el **módulo activo**, pero no menciona explícitamente que **algunas de las 5 propiedades `DatatypeProperty` que sí sobreviven en 2.5** (`P3_has_note`, `P82`, `P82a`, `P82b`, `P90_has_value`) son precisamente las que el propio informe (Paso 3) identifica como mal declaradas en el original (`P3_has_note` como `ObjectProperty`→`E62_String`). Sería más preciso decir que 2.5 no solo tiene menos propiedades de datos, sino que las que tiene están mejor tipadas — un matiz positivo que el informe deja implícito en vez de afirmarlo.

---

## (b) Parte B — Conformidad conceptual (foco principal)

### B.1 — `P127_has_broader_term` como mecanismo de "anclas" de categoría

**Cita oficial completa** (`imports/vendor/cidoc-crm-7.1.3.rdf`, ya citada en `problemes-et-solutions.md` y revalidada aquí):
> *E55_Type: "E55 Type provides an interface to domain specific ontologies and thesauri. These can be represented in the CIDOC CRM as subclasses of E55 Type, forming hierarchies of terms, i.e. instances of E55 Type linked via P127 has broader term (has narrower term): E55 Type. Such hierarchies may be extended with additional properties."*
> *P127_has_broader_term: "This property associates an instance of E55 Type with another instance of E55 Type that has a broader meaning. It allows instances of E55 Types to be organised into hierarchies. This is the sense of 'broader term generic (BTG)' as defined in ISO 25964-2:2013 [...] This property is transitive. This property is asymmetric."*

**Veredicto: uso parcialmente fiel, con una tensión real que el equipo debería conocer.**

En su forma más superficial, el patrón sí es una instancia legítima de BTG (genus-species): "Écriture latine" *es* efectivamente una especie del género "Système d'écriture" — no hay error categorial ahí, a diferencia, por ejemplo, del uso indebido de `P150_defines_typical_parts_of` que el mismo documento corrige en el Problème 2 (esa sí era una confusión de tipo, corregida correctamente).

La tensión real no está en la relación genus-species en sí, sino en **la función que cumplen las 7 anclas dentro del sistema**: la nota de balisaje de `E55_Type` describe `P127` como el mecanismo para construir jerarquías de tesauro *navegables por un usuario humano* — un tesauro real permite a alguien buscar "Écriture" y encontrar sus especies, o partir de "Écriture latine" y subir hacia conceptos más amplios con significado propio y asignable (ISO 25964 permite incluso, en la práctica de construcción de tesauros, "términos-nodo"/"guías de facette" no asignables directamente pero pensados para *organizar la visualización* del tesauro, uso que se acerca al patrón CAO_CRM). Aquí, sin embargo, la motivación explícita y documentada de la solución (Problème 1b, sección 2) es distinta: **"C'est exactement ce vide que P127_has_broader_term comble, en rendant explicite et interrogeable ce que la notation {...} de la documentation LRMoo officielle ne fait qu'indiquer en langage naturel."** Es decir: el ancla no se crea porque "Système d'écriture" sea un concepto que alguien quiera asignar o navegar por interés temático propio — se crea **como mecanismo de desambiguación automática por consulta SPARQL**, para poder distinguir programáticamente a qué facette pertenece cada valor de `E55_Type` cuando dos facettes distintas comparten la misma propiedad `P2_has_type`. Esa es una necesidad de **esquema** (saber a qué "campo" pertenece un valor), resuelta con un mecanismo pensado para **datos de tesauro** (relaciones semánticas entre conceptos reales). El propio documento lo reconoce indirectamente cuando dice que la anotación `{NomDeFacette}` de la documentación LRMoo "no es una construcción RDF" — y en lugar de resolver eso con un mecanismo de nivel de esquema (p. ej. `rdfs:range` distinto por subpropiedad, como de hecho ya hace el propio proyecto con los 7 `P14_a_pour_*`), lo resuelve inyectando la distinción como triples de instancia (ABox) que imitan una jerarquía de tesauro.

**Esto no es un error lógico** (el razonador no lo objeta, y la relación BTG es semánticamente correcta caso por caso) — pero sí es una **tensión de intención**: el mecanismo se usa para lo que la norma no lo diseñó explícitamente (aunque tampoco lo prohíbe), y el propio equipo ya reconoció una versión de esta tensión al escribir, en el mismo documento, que aplicar el patrón «Script» de `LRM-E9-A8` a `F5_Item`/`D1_Digital_Object` "reste une extension par analogie du patron officiel — cohérente dans son principe, mais pas une correspondance exacte au cas d'usage officiel". La misma honestidad debería extenderse explícitamente al uso de `P127` como mecanismo de desambiguación de facette, no solo al nivel donde se cuelga el atributo.

### B.2 — `E33_Linguistic_Object` co-tipando `F2_Expression`

**Veredicto: sancionado explícitamente por la propia norma — no es una inferencia razonable, es una instrucción textual directa.**

Verificado en `imports/vendor/lrmoo-1.1.1.rdf`, comentario oficial de `F2_Expression` (líneas 21-24), pasaje no citado hasta ahora por ninguno de los documentos de CAO_CRM revisados en esta cadena de auditorías:
> *"An instance of F2 Expression which includes spoken or written text **may be multiply instantiated as an instance of E33 Linguistic Object**. This allows for the association of the E56 Language of the text with the instance of F2 Expression by using the property P72 has language (is language of)."*

Esta frase es, literalmente, la instrucción oficial de LRMoo para hacer exactamente lo que `problemes-et-solutions.md` (Problème 2) decidió hacer por su cuenta a partir de una inferencia indirecta (comparando `E33_Linguistic_Object`/`E34_Inscription`/MARC21). El equipo llegó a la conclusión correcta y la implementó correctamente, pero **no citó la fuente más fuerte posible** — el comentario propio de `F2_Expression`, que zanja la cuestión sin necesidad de analogía ni de MARC21 ni de BIBFRAME. Es una omisión documental menor (la conclusión no cambia) pero significativa desde el punto de vista de la robustez argumental: la doble instanciación no es "una práctica común en OWL" aplicada por extensión, como sugiere `problemes-et-solutions.md` línea 461 (*"pratique courante en OWL"*) — es la instrucción explícita y nombrada del propio modelo LRMoo para este caso concreto.

**Recomendación:** añadir esta cita a `problemes-et-solutions.md` (Problème 2) y a `complete-model.md` (Partie B), reforzando lo que ya es una decisión correcta con la evidencia más directa disponible, en vez de apoyarse solo en la analogía vía `E34_Inscription`.

### B.3 — `E22_Human-Made_Object` co-tipando `F5_Item`

**Veredicto: igualmente sancionado de forma explícita y aún más fuerte que el caso anterior.**

Cita oficial completa, ya usada correctamente por `problemes-et-solutions.md` pero que merece destacarse por su fuerza normativa (`imports/vendor/lrmoo-1.1.1.rdf`, comentario de `F5_Item`):
> *"An instance of F5 Item that consists of a physical object or set of objects with clear physical boundaries **is also an instance of E22 Human-Made Object**."*

A diferencia del caso B.2 (donde la norma usa "may be multiply instantiated", un permiso condicional), aquí la norma usa **"is also an instance of"** — una afirmación categórica, no condicional, para el caso general (objeto físico con límites claros, que es exactamente el caso de un libro). Esto hace que el co-tipado de `F5_Item`/`E22_Human-Made_Object` sea, de los tres mecanismos de co-tipado examinados en esta auditoría, **el más sólidamente sancionado por la norma**, no una interpretación.

La única reserva real, ya señalada correctamente por el auditor 1 (H1) y no por este documento, es que esta doble pertenencia de clase no está reforzada por un axioma `rdfs:subClassOf` en el TBox de `CAO_CRM-1.0.rdf` — depende de que cada instancia real se co-tipe manualmente al cargar los datos. Esto no es una falla de fidelidad conceptual (la norma tampoco impone `F5_Item rdfs:subClassOf E22_Human-Made_Object` de forma universal — es "is also" para el caso normal, no un axioma incondicional, precisamente porque la norma reconoce casos donde `F5_Item` es más bien `E25_Human-Made_Feature`, ver la misma cita completa en el comentario de `F5_Item`), sino una cuestión de disciplina de captura de datos, ya correctamente clasificada por el auditor 1 como 🔴 de documentación/comentario, no de modelo conceptual.

### B.4 — `F32_Item_Production_Event` y `D9_Data_Object`/`D7_Digital_Machine_Event`

**Veredicto: el patrón "subclase específica en vez de clase madre" está genuinamente resuelto para los dos casos centrales (Problèmes 5 y 6), pero quedan dos matices reales de la nota de balisaje que ningún documento de CAO_CRM considera.**

1. **Matiz 1 — `D11_Digital_Measurement_Event` y el atajo `L20_has_created`.** La nota oficial de `D11_Digital_Measurement_Event` (`imports/vendor/crmdig-5.0.rdf`) dice textualmente: *"Note that the property L20 has created (was created by): D9 Data Object constitutes a shortcut of the full path from D11 Digital Measurement Event through O39 observed dimension (was observed in), E54 Dimension, L61 contains value set of (has value set representation), to D9 Data Object."* Esto confirma exactamente lo que el auditor 1 señaló en su Nota 3 (🟡): `D11_Digital_Measurement_Event`, `E11_Modification`, `E65_Creation` y `E31_Document` no están en el módulo, así que si el equipo alguna vez necesita documentar una medición digital completa (no solo el objeto de datos resultante) le faltará este eslabón. Ninguno de los documentos de decisión (`problemes-et-solutions.md`, `complete-model.md`) menciona esta clase ni este atajo — es un punto ciego real, aunque de bajo impacto práctico hoy (CAO_CRM no modela mediciones científicas, solo bibliografía).

2. **Matiz 2 — `D10_Software_Execution` y la ambigüedad de intersección con `D7_Digital_Machine_Event`.** La nota de `D11_Digital_Measurement_Event` también dice: *"Measurement devices may include running distinct software [...] If the respective software is configurable for the device, **the event is regarded as an instance of both classes, D10 Software Execution and D11 Digital Measurement Event.**"* Esto confirma que el patrón de doble pertenencia de clase no es exclusivo de `F5_Item`/`E22_Human-Made_Object` — es un patrón recurrente en toda la familia CRMdig, y el descubrimiento D2-A/`D7_Digital_Machine_Event` (que resuelve correctamente el caso de producción nativa vs digitalización) podría, en el futuro, necesitar la misma disciplina de co-tipado si el equipo distingue alguna vez entre "ejecución de software" y "evento de máquina digital" genérico. Ningún documento lo anticipa — no es un error hoy, pero es exactamente el tipo de matiz que la nota de balisaje completa revela y un domain/range aislado no.

**En conjunto:** para el uso actual de CAO_CRM (bibliografía, no ciencia experimental), estos dos matices no bloquean nada — pero confirman la observación ya hecha por el auditor 1 (Nota 3, H2): la extracción por ROBOT preserva la corrección lógica del módulo acotado, pero dos de las siete clases de la familia CRMdig incluidas (`D9_Data_Object`, `D7_Digital_Machine_Event`) tienen notas de balisaje oficiales que remiten a clases vecinas ausentes del módulo, con implicaciones de modelado reales si el alcance crece.

### B.5 — Las 3 subpropiedades `P14_a_pour_*`: ¿categorías suficientes?

**Veredicto: suficientes y mutuamente excluyentes para el caso citado por el paper (Christie/traductora/versión abreviada), pero el informe debería declarar explícitamente qué queda fuera de alcance — hoy lo hace solo de forma dispersa e implícita.**

Verificado: "auteur original" (MARC `aut`), "traducteur" (MARC `trl`) y "abrégeur" (MARC `abr`) son, en el vocabulario MARC Relator Terms, tres roles distintos y no solapados por definición — no hay ambigüedad conceptual entre ellos. Para el caso concreto que motiva el documento (*Mord im Orientexpress*, con autora + traductora, y el ejemplo LRMoo oficial de la "abridged English version" citado en el paper), los tres roles son efectivamente necesarios y suficientes.

**Lo que el informe sí menciona, pero de forma dispersa** (no como una sección dedicada de "fuera de alcance"): la sección 4 (tabla de comparación) menciona de pasada, en la fila "Flexibilité si de nouveaux rôles apparaissent", que "un nouveau rôle (ex. « préfacier », « éditeur scientifique »)" requeriría una nueva subpropiedad; y la sección "Implications pour la modélisation" (final) repite la misma idea con los mismos dos ejemplos. **Pero en ningún momento el documento presenta una lista explícita, aunque sea corta, de roles de autoría reales y comunes en un fondo patrimonial que NO están cubiertos** (editor, prologuista/prefacista, ilustrador, adaptador, compilador, anotador, revisor científico — todos ellos con código MARC Relator propio: `edt`, `wpr`/`pfr`, `ill`, `adp`, `com`, `ann`, `rev`) — se mencionan solo dos ejemplos, incidentalmente, dentro de una fila de tabla sobre "flexibilidad futura", no como una declaración de alcance. Para un informe que se preció de ser exhaustivo con las fuentes MARC Relator (citando textualmente `trl`, `abr`, `aut` con URIs verificadas), sorprende que no incluya una tabla equivalente, aunque fuera breve, de "roles frecuentes no cubiertos hoy" con sus códigos MARC — sería un ejercicio de un párrafo, dado que el propio documento ya demuestra dominio completo del vocabulario relator.

**Esto no invalida la recomendación (Opción B es la correcta)** — pero es una omisión real de honestidad de alcance, del mismo tipo que el propio documento sí practica en otras partes (p. ej. la reserva explícita sobre `LRM-E9-A8`/`F12_Nomen` en `problemes-et-solutions.md`). Recomendación: añadir una tabla corta "roles de autoría MARC Relator no cubiertos por esta decisión (a añadir si el equipo los necesita)" junto a la sección 5.

### B.6 — El camino indirecto para derechos morales de `F1_Work` y el Issue 328

**Verificación directa realizada hoy** (WebFetch sobre `https://cidoc-crm.org/Issue/ID-328-rights-model`, no de memoria): la página **existe, es accesible, y su contenido confirma exactamente lo que citan `complete-model.md` e `complete-model.md`** — la discusión sobre "Droit Moral/Moral Rights", el ejemplo de Leonardo da Vinci/Mona Lisa (verificado con la misma cita exacta, incluidos los mismos errores tipográficos del original: *"By decorating a Mona Lisa copy in a offending manner you can taken to court accussed for violating Leonardo's Moral Right"*), y la decisión de añadir ejemplos de copyright a la nota de `E30_Right` sin crear una propiedad directa que sortee la exclusión de `E28_Conceptual_Object`.

**Precisión menor detectada:** `complete-model.md` (línea 79) atribuye la discusión a la *"38th joined meeting"*; la página, verificada hoy, indica que la decisión de **cierre** del issue se tomó en la *"40th joined meeting (January 2018, Cologne)"*. No es necesariamente una contradicción — son issues de larga duración donde la discusión inicial y el cierre formal pueden ocurrir en reuniones distintas, y el texto citado por `complete-model.md` (*"In the 38th joined meeting [...] the crm-sig discussed [...] Comments and decisions are [...] To add copyright examples"*) es coherente con que la discusión sustantiva haya ocurrido en la 38ª y el cierre formal en la 40ª. Aun así, recomendable aclarar en el documento cuál reunión corresponde a qué paso, para que la cita no parezca imprecisa ante un lector que verifique la fuente por su cuenta (como se hizo aquí).

**Veredicto sobre la pérdida conceptual:** hay una pérdida conceptual real, y el propio `complete-model.md` la reconoce parcialmente pero no la nombra con toda su fuerza. Un derecho moral es, por definición jurídica (droit d'auteur continental), inherente a la **autoría de la obra** — vincula al autor con su creación intelectual, independientemente de cualquier materialización o traducción concreta. El camino propuesto (`F1_Work --R3_is_realised_in--> F2_Expression --P104_is_subject_to--> E30_Right`) cuelga el derecho de una **Expression concreta**, no de la Obra. Esto tiene una consecuencia práctica real que ningún documento de la cadena señala explícitamente: **si una Obra tiene varias Expressions (el texto original en francés, una traducción al alemán, una versión abreviada), el modelo obliga a elegir sobre cuál de ellas colgar el `E30_Right` de tipo "droit moral"** — o a repetirlo en cada Expression, lo cual no es incorrecto pero diluye la naturaleza unitaria del derecho (el derecho moral de Cailhava de l'Estandoux sobre su obra no depende de cuál Expression se esté consultando). El SIG confirma que esto es una limitación estructural conocida y aceptada del CRM (ningún mecanismo directo existe ni está previsto para `E28_Conceptual_Object`), no una elección arbitraria de CAO_CRM — pero el equipo debería saber que la solución **evita la inconsistencia lógica, no la pérdida de expresividad**: en el grafo resultante, "quién es dueño moral de la Obra" solo es recuperable indirectamente y de forma potencialmente redundante entre Expressions, nunca como una afirmación directa y única sobre `F1_Work`.

### B.7 — Los hallazgos 🟡 de simplificación de jerarquías (Notas 1-3 y H2 del auditor 1)

**Veredicto por elemento:**

- **`E33_Linguistic_Object` (Nota 1, sustituye `E73_Information_Object` por `E89_Propositional_Object`+`E90_Symbolic_Object`):** inocuo para la semántica pretendida. Verificado: `E73_Information_Object` no aparece en ninguna nota de balisaje citada por los documentos de CAO_CRM como origen de una propiedad o restricción que el módulo necesite invocar directamente (a diferencia de `E33_Linguistic_Object`, que sí es el ancla real de `P72_has_language`). La sustitución preserva la pertenencia a ambas superclases reales sin añadir ni quitar significado accesible desde el módulo.

- **`E22_Human-Made_Object` (Nota 2, sustituye `E19_Physical_Object`+`E24_Physical_Human-Made_Thing` por `E18_Physical_Thing`):** aquí sí hay una pérdida con relevancia conceptual, no solo de cierre de módulo: `E19_Physical_Object` es precisamente la clase que exigen oficialmente `P54`/`P55` (domain/range real, según lo confirma el propio auditor 1 en H1). Al no estar `E19_Physical_Object` declarada como superclase de `E22_Human-Made_Object` dentro del TBox de `CAO_CRM-1.0.rdf`, un razonador que solo tuviera el módulo (sin el vendor completo) no podría inferir automáticamente que un `E22_Human-Made_Object` satisface el dominio original de `P54`/`P55` — la única razón por la que hoy no hay problema es que el propio `CAO_CRM-1.0.rdf` ya sobreescribió el `rdfs:domain` de `P54`/`P55` a `E22_Human-Made_Object` directamente (decisión ya evaluada y validada por el auditor 1, H1). Es decir: la simplificación de jerarquía de la Nota 2 y la restricción de dominio de H1 son dos caras de la misma decisión, y juntas son coherentes — pero por separado, la Nota 2 sí representa una pérdida real de la cadena de herencia oficial, compensada solo porque el propio módulo tomó otra decisión (reescribir el dominio) que hace innecesaria esa cadena. Si algún día se revierte H1 (se decide restaurar `rdfs:domain E19_Physical_Object` por fidelidad literal), la Nota 2 volvería a ser un problema real, no solo cosmético.

- **`D9_Data_Object`/`D7_Digital_Machine_Event` (Nota 3, falta `E31_Document`/`E11_Modification`/`E65_Creation`):** ver B.4 arriba — no inocuo en términos absolutos (el atajo `L20_has_created` y el patrón de doble instanciación `D10_Software_Execution`/`D11_Digital_Measurement_Event` dependen de esas clases ausentes), pero sí inocuo **para el alcance actual** de CAO_CRM, que no modela mediciones digitales ni ejecución de software como actividad propia.

- **Pérdida de `subPropertyOf` (H2: `P55`→`P53`, `R2`→`R68`, `R76`→`P130`, `R75`→`P165`):** inocua para la semántica de cada propiedad tomada aisladamente (el `domain`/`range` de cada una es correcto y autosuficiente), pero sí tiene una consecuencia conceptual real y ya anticipada correctamente por `complete-model.md` (A.3): sin `R2 rdfs:subPropertyOf R68_is_inspired_by` declarado en el propio módulo, un razonador que opere solo sobre `CAO_CRM-1.0.rdf` (sin el vendor completo cargado) **no podrá inferir automáticamente** que una adaptación teatral (`R2_is_derivative_of`) también cuenta como "inspirada por" (`R68_is_inspired_by`) su obra fuente — la inferencia solo funciona si se razona sobre la fusión completa con los tres vendors (que es, de hecho, como el auditor 1 verificó que se ejecutan las validaciones). Es decir: la pérdida es inocua **en el pipeline de validación actual** (que siempre fusiona con los vendors completos antes de razonar) pero dejaría de serlo si alguna vez se consume `CAO_CRM-1.0.rdf` de forma aislada, sin sus tres importaciones — un supuesto de uso que ningún documento descarta explícitamente.

---

## (c) Veredicto final

**El modelo conceptual de `CAO_CRM-1.0.rdf`, en su conjunto, es fiel a CIDOC-CRM/LRMoo/CRMdig — con un margen de tensiones reales, conocidas y acotadas, que el equipo debería tener presentes, ninguna de las cuales bloquea la producción.**

Los tres mecanismos de co-tipado examinados (B.2, B.3) resultaron, tras verificación directa de las notas de balisaje completas (no solo domain/range), **más sólidamente sancionados por la norma de lo que la propia documentación de CAO_CRM se atrevía a afirmar** — en particular, el hallazgo B.2 (la frase "may be multiply instantiated as an instance of E33 Linguistic Object" en el comentario oficial de `F2_Expression`) es una instrucción textual directa que ningún documento de esta cadena había citado hasta ahora, y que refuerza — no debilita — la decisión ya tomada.

La tensión más real y menos resuelta es la de **B.1 (`P127_has_broader_term` como mecanismo de anclas)**: no es un error, pero es un uso del mecanismo de tesauro de CIDOC-CRM para resolver un problema de **esquema** (desambiguación de facette) con una herramienta pensada para **datos** (jerarquías de conceptos reales navegables). Es la misma familia de tensión, aplicada con más disciplina, que la que ya reconoce el propio equipo al hablar de "extensión por analogía" para el atributo Script. Recomendación concreta: documentar explícitamente, en `problemes-et-solutions.md` (Problème 1b), que las 7 anclas son un uso deliberadamente extendido de `P127` más allá de su caso de uso canónico de tesauro navegable, igual que ya se hace honestamente para el caso Script/`F12_Nomen`.

La segunda tensión real es **B.6 (derechos morales)**: el camino indirecto es la única vía legal y está bien corroborado por el Issue 328 (verificado hoy, accesible, contenido coincidente) — pero implica una pérdida de expresividad real (el derecho se ata a una Expression, no a la Obra como tal) que el equipo debería aceptar conscientemente, no solo como "la única opción sin inconsistencia lógica".

La tercera observación, más técnica que conceptual, es **B.7**: dos de las simplificaciones de jerarquía marcadas 🟡 por el auditor 1 (`E22_Human-Made_Object` y la pérdida de `subPropertyOf`) son inocuas **solo bajo el supuesto de que el módulo siempre se consume fusionado con los tres vendors completos** — supuesto que hoy se cumple en el pipeline de validación, pero que ningún documento fija como requisito explícito de uso del archivo.

**Ningún hallazgo de esta auditoría (Parte A o Parte B) alcanza severidad 🔴.** Todos son 🟡 — precisiones de documentación, omisiones de alcance no declaradas, o tensiones conceptuales reales pero conocidas y sin consecuencia práctica en el uso actual del modelo (bibliografía patrimonial, sin mediciones científicas ni ejecución de software como actividad modelada). El trabajo de hoy es conceptualmente sólido; las tensiones señaladas son del tipo que cualquier aplicación seria de CIDOC-CRM/LRMoo termina encontrando tarde o temprano al usar `E55_Type`/`P127` de forma extensiva, y su documentación explícita (no su eliminación, que no es posible sin rehacer el mecanismo) es la mejora recomendada.

### Resumen de hallazgos por severidad

| # | Sección | Severidad | Resumen |
|---|---|---|---|
| A.1.1 | `problemes-et-solutions.md` | 🟡 | El diagrama Mermaid original del Problème 1 (Système d'écriture) no se marcó como superado tras la actualización del 6/7, riesgo de lectura no lineal |
| A.3.1 | `informe-P14-roles-autorat.md` | 🟡 | Label propuesto "a pour abrégeur" vs. label final implementado "a pour abréviateur" — divergencia textual menor |
| A.5.1 | Informe Mélanie vs 2.5 | 🟡 | No destaca explícitamente que las DatatypeProperty supervivientes en 2.5 están mejor tipadas, no solo son menos |
| B.1 | Conformidad — P127 anclas | 🟡 | Repurposing de un mecanismo de tesauro (datos) para resolver un problema de esquema (desambiguación de facette); no documentado como tal, a diferencia del caso Script |
| B.4 | Conformidad — D9/D7/F32 | 🟡 | Dos matices reales de la nota de balisaje de CRMdig (atajo `L20_has_created`, doble instanciación `D10`/`D11`) no considerados, sin impacto en el alcance actual |
| B.5 | Conformidad — P14 roles | 🟡 | Ausencia de una sección explícita de "roles de autoría fuera de alcance" pese al dominio ya demostrado del vocabulario MARC Relator |
| B.6 | Conformidad — derechos morales | 🟡 | Pérdida real de expresividad (derecho atado a la Expression, no a la Obra) presentada sin todo el peso de la limitación; precisión menor sobre el número de reunión del Issue 328 |
| B.7 | Conformidad — simplificaciones de jerarquía | 🟡 | Dos simplificaciones (E22, pérdida de subPropertyOf) son inocuas solo si el módulo se consume siempre fusionado con los vendors — supuesto no declarado explícitamente |

**Total: 0 hallazgos 🔴, 8 hallazgos 🟡.** Ninguno bloquea el paso a producción; todos son mejoras de documentación/honestidad de alcance recomendadas antes de dar por cerrado el ciclo de trabajo de hoy.

No se modificó ningún archivo del repositorio durante esta auditoría salvo la creación de este informe.
