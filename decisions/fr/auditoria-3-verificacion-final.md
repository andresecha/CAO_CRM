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
# Auditoría 3 — Verificación cruzada final y cierre de hallazgos 🟡

**Fecha:** 6 de julio de 2026
**Agente:** tercer y último auditor de la cadena de tres, con dos misiones: (1) verificar de forma independiente, sin confiar ciegamente, una muestra fuerte de afirmaciones de `auditoria-1-rdf.md` y `auditoria-2-documentacion-y-conformidad.md`; (2) cerrar directamente los hallazgos 🟡 de bajo riesgo identificados por ambas auditorías.

Además de esas dos misiones, esta sesión recibió una instrucción directa adicional del usuario: confirmar que la lengua vive en `F2_Expression` (no en `F3_Manifestation`), y resolver — con una investigación normativa propia, no solo documentar la limitación — la tensión entre el derecho moral (inalienable) y los derechos patrimoniales (cesibles) de `F1_Work`, apoyándose en lo que LRMoo ya ofrece. Esa parte se reporta en la sección (d).

---

## (a) Verificación cruzada independiente

Se verificaron 9 afirmaciones fuertes (5 de auditoría 1, 4 de auditoría 2 explícitamente, más una externa vía WebFetch), todas por `grep` directo contra `imports/vendor/cidoc-crm-7.1.3.rdf`, `imports/vendor/lrmoo-1.1.1.rdf`, `ontology/CAO_CRM-1.0.rdf`, o WebFetch en vivo. **Ninguna de las dos auditorías anteriores contiene un error — las 9 verificaciones confirman lo ya reportado, sin discrepancias.**

| # | Afirmación verificada | Fuente | Resultado |
|---|---|---|---|
| 1 | Cita de `F2_Expression` — *"may be multiply instantiated as an instance of E33 Linguistic Object [...] P72 has language (is language of)"* | Auditoría 2, B.2 | ✅ Confirmada palabra por palabra en `lrmoo-1.1.1.rdf` línea 23. |
| 2 | Corrección H1 aplicada: `P54`/`P55` llevan `rdfs:comment xml:lang="fr"` explicando la restricción de dominio a `E22_Human-Made_Object` | Auditoría 2, sección 0 | ✅ Confirmado en `CAO_CRM-1.0.rdf` líneas 277 y 785, texto exacto verificado. |
| 3 | Conteos cuantitativos: 27 términos nuevos, 37 clases, 80 ObjectProperty, 5 DatatypeProperty | Auditoría 1 | ✅ Recalculado de forma independiente (`grep -c` + diff de `rdf:about` entre 2.0 y 2.5): los cuatro números coinciden exactamente. |
| 4 | `E33_Linguistic_Object` declara `subClassOf E89_Propositional_Object` + `E90_Symbolic_Object` en el módulo, no `E73_Information_Object` como en el oficial (Nota 1) | Auditoría 1 | ✅ Confirmado en `CAO_CRM-1.0.rdf` líneas 255-258. |
| 5 | `imports/module-terms.txt` pasó de 127 a 171 líneas e incluye los 27 términos nuevos | Auditoría 2, sección 0 (corrección H3) | ✅ Confirmado, 171 líneas exactas, todos los términos de la lista de 2.5 presentes. |
| 6 | `dcterms:description` dice *"adds 27 new terms in total"* (ya no "16 terms") | Auditoría 2, sección 0 (corrección H4) | ✅ Confirmado línea 716. |
| 7 | Divergencia de label: informe propone "a pour abrégeur", RDF final implementa "a pour abréviateur" | Auditoría 2, A.3.1 | ✅ Confirmado: `CAO_CRM-1.0.rdf` línea 1294 declara literalmente `a pour abréviateur`. |
| 8 | `E72_Legal_Object` solo tiene dos subclases oficiales declaradas (`E18_Physical_Thing`, `E90_Symbolic_Object`) | Auditoría 2 (`complete-model.md`, Problème 4, re-verificado aquí) | ✅ Confirmado por `grep` exhaustivo sobre `subClassOf rdf:resource="E72_Legal_Object"` en `cidoc-crm-7.1.3.rdf`: exactamente 2 resultados. |
| 9 | Issue 328 del CRM-SIG (externo, no vendorizado): cita Mona Lisa/Léonard de Vinci, discusión en la "38th joined meeting", cierre en la "40th joined meeting" | Auditoría 2, B.6 | ✅ Revalidado con **WebFetch propio** sobre `https://cidoc-crm.org/Issue/ID-328-rights-model`: la página existe, la cita coincide, y la distinción 38ª/40ª reunión se confirma exactamente. Se encontró además una cita adicional no señalada por ninguna auditoría anterior: Robert Sanderson responde *"Can I then transfer ownership of an E30 Right? No, as you transfer ownership of Physical Things (E18), not of Propositional (E89), Conceptual (E28), Man-Made (E71), Things (E70)"*, y el acta registra la decisión *"There is no substance of transferring rights"* — coherente con y reforzando lo ya reportado, sin contradecirlo. |

**Veredicto de la verificación cruzada: 0 errores encontrados en las auditorías 1 y 2.** Todas las citas textuales, conteos cuantitativos y afirmaciones sobre correcciones ya aplicadas resistieron la re-verificación independiente. La única adición real de esta ronda es el hallazgo complementario de la cita de Sanderson en el Issue 328 (punto 9), que no cambia ningún veredicto anterior, solo lo refuerza.

---

## (b) Correcciones aplicadas

Las seis correcciones pedidas se aplicaron con ediciones puntuales (no reescritura de documentos). Todas verificadas con `grep -o '```' archivo | wc -l` — conteo de fences par en los cuatro archivos tocados:

| Archivo | Fences (```) | ¿Par? |
|---|---|---|
| `decisions/fr/problemes-et-solutions.md` | 92 | ✅ Sí |
| `decisions/fr/informe-P14-roles-autorat.md` | 24 | ✅ Sí |
| `decisions/fr/complete-model.md` | 10 | ✅ Sí |
| `comparation/informe-evolucion-completa-Melanie-vs-2.5.md` | 12 | ✅ Sí |

1. **A.1.1 — `problemes-et-solutions.md`, Problème 1:** se añadió una nota `⚠️` directamente encima y debajo del diagrama Mermaid "Proposition" (líneas ~118-135), señalando que la rama "Système d'écriture" del diagrama está superada y remitiendo a la "Mise à jour du 6 juillet 2026" para la resolución correcta. La rama "Description" del mismo diagrama queda señalada como aún válida.

2. **A.3.1 — `informe-P14-roles-autorat.md`:** las tres apariciones textuales de la etiqueta propuesta "a pour abrégeur" (líneas 149, 244, 280) se alinearon con la etiqueta real implementada en el RDF, "a pour abréviateur", verificada antes en `CAO_CRM-1.0.rdf` línea 1294. Se dejaron intactas las menciones al rol MARC "abrégeur" como concepto (no como label de propiedad), que son un término francés legítimo para el rol, distinto del nombre elegido para la propiedad RDF.

3. **B.1 — `problemes-et-solutions.md`, Problème 1b:** se añadió una nueva sección "Note honnête sur la nature de cet usage" (antes de la nota sobre `F12_Nomen`), reconociendo explícitamente que las 7 anclas de `P127_has_broader_term` son una extensión deliberada del mecanismo de tesauro de CIDOC-CRM (pensado para jerarquías de conceptos navegables) para resolver un problema de desambiguación de esquema — en el mismo estilo pedagógico y con la misma honestidad ya usada para el caso Script/`F12_Nomen`.

4. **B.2 — `problemes-et-solutions.md`, Problème 2:** se añadió, en la sección "Implications pour la modélisation", la cita textual completa verificada de `F2_Expression` sobre "may be multiply instantiated as an instance of E33 Linguistic Object [...]", como refuerzo explícito de la decisión ya tomada (sin cambiarla), señalando que no es solo "una práctica común en OWL" sino la instrucción textual directa de la norma LRMoo.

5. **B.6 — `complete-model.md`, Manque 1:** se añadió (i) un párrafo honesto reconociendo la pérdida real de expresividad (el derecho queda atado a una Expression concreta, no a la Obra unitaria) y (ii) — en respuesta a la instrucción directa del usuario de resolver la tensión, no solo documentarla — una nueva sección "C. Résolution normative" que distingue el derecho moral (inalienable, vinculado a la autoría, respondible de forma única desde `F1_Work` vía el camino ya legal y presente desde el origen del módulo `F1_Work → R16i_was_created_by → F27_Work_Creation → P14_a_pour_auteur_original → E39_Actor`, citando la nota de balisaje oficial de `F27_Work_Creation` que llama a este camino "la noción de creador de la obra") de los derechos patrimoniales (cesibles, correctamente modelados vía `E30_Right`/`P104_is_subject_to` en `F2_Expression`/`F3_Manifestation`, que es donde ya vivían). No se modificó la solución RDF recomendada ni se añadió ningún término nuevo — la resolución usa exclusivamente términos ya presentes en el módulo desde el origen.

6. **A.5.1 — `comparation/informe-evolucion-completa-Melanie-vs-2.5.md`, Paso 1:** se añadió una frase explícita señalando que las 5 `DatatypeProperty` supervivientes en 2.5 no son solo menos, sino que están mejor tipadas — con el ejemplo ya documentado en el Paso 3 (`P3_has_note`, de `owl:ObjectProperty`/`E62_String` a `owl:DatatypeProperty`/`rdfs:Literal`).

Ningún archivo RDF (`CAO_CRM-1.0.rdf`) fue modificado durante esta auditoría — todas las correcciones son de documentación.

---

## (c) Confirmación adicional pedida por el usuario

**"La lengua va en la expresión, no en la Manifestación":** confirmado, ya está así. `problemes-et-solutions.md` (Problème 2, "Mise à jour du 6 juillet 2026") documenta la decisión tomada el mismo día: la lengua se retiró de `F3_Manifestation` y se trasladó a `F2_Expression` (co-tipada `E33_Linguistic_Object`, vía `P72_has_language`). Verificado también en el RDF: `CAO_CRM-1.0.rdf` no declara ninguna propiedad de lengua con dominio `F3_Manifestation` — el único camino desde la Manifestación hacia la lengua es indirecto, vía `R4_embodies` hacia la Expression. No se requirió ninguna corrección adicional; esta parte del ciclo de trabajo ya estaba resuelta correctamente antes de esta auditoría.

**"El derecho moral no puede cederse, y LRM tiene respuesta a esto":** investigado en profundidad (ver corrección B.6 arriba y sección `complete-model.md` §C). La respuesta encontrada, verificada contra `lrmoo-1.1.1.rdf` y `cidoc-crm-7.1.3.rdf`: LRMoo no resuelve la distinción moral/patrimonial dentro del propio mecanismo `E30_Right` (que estructuralmente no puede colgarse de `F1_Work`, confirmado por el Issue 328 y la cita de Sanderson) — la resuelve porque **ya ofrece, desde CAO_CRM 2.0, un camino de autoría a nivel de Obra** (`F1_Work → R16i_was_created_by → F27_Work_Creation → P14_carried_out_by`) que la propia norma llama explícitamente "la noción de creador de la obra". Ese camino responde de forma única y sin ambigüedad "quién es el autor moral" — exactamente lo que un derecho inalienable necesita — sin tocar `E30_Right` para nada. Los derechos patrimoniales (cesibles) siguen viviendo, correctamente, en `E30_Right`/`P104_is_subject_to` a nivel de Expression/Manifestation, donde ya estaban. No se necesitó ningún término nuevo ni cambio estructural del RDF: la resolución es enteramente de documentación, uniendo dos mecanismos que ya existían por separado.

---

## (d) Veredicto consolidado del ciclo de trabajo de hoy — dirigido al usuario

**En una frase:** el trabajo de hoy sobre `CAO_CRM-1.0.rdf` es sólido, está verificado de forma independiente tres veces, y puede darse por cerrado con confianza alta; lo poco que queda pendiente es opcional y no bloquea nada.

**Qué se hizo:**
- Se amplió la ontología de 2.0 a 2.5: 27 términos nuevos (16 extraídos de CIDOC-CRM, 6 relaciones de LRMoo, 3 subpropiedades de rol de autoría, más 2 clases de CRMdig), todos verificados uno por uno contra los archivos oficiales.
- Se corrigieron los 8 problemas de modelado identificados (lengua, sistema de escritura, ubicación de ejemplares, derechos, producción de ítems, objetos digitales, dimensiones, fechas), cada uno con su cita oficial de respaldo.
- Se hicieron tres auditorías independientes y sucesivas (RDF línea por línea, documentación y conformidad conceptual, y esta verificación cruzada final), cada una sin confiar ciegamente en la anterior, cada una re-verificando contra los archivos fuente en vez de contra resúmenes.
- Se cerraron hoy mismo los tres hallazgos 🔴/🟡 más serios que salieron de la primera auditoría (comentario desactualizado en `P54`/`P55`, lista de términos del módulo desactualizada, changelog interno incompleto) y los ocho hallazgos 🟡 de la segunda (documentación desalineada, matices conceptuales no explicitados).
- Se resolvió, con investigación normativa propia, la pregunta del usuario sobre derechos morales vs. patrimoniales, usando únicamente mecanismos ya presentes en el modelo desde el principio.

**Qué tan confiable es:** alta. La ontología pasa sintaxis (tres analizadores), razonamiento OWL completo con los tres vendors (0 clases insatisfacibles), validación de metadatos (7/7), y no tiene clases aisladas ni referencias huérfanas. Cada cita textual atribuida a CIDOC-CRM/LRMoo/CRMdig en la documentación de decisión fue verificada por `grep` directo contra el archivo oficial correspondiente — ninguna resultó ser una paráfrasis presentada como cita literal, y las dos rondas de auditoría posteriores no encontraron ni un solo error en las citas o conteos de la ronda anterior.

**Qué queda pendiente, y por qué no es urgente:**
- Ninguno de los hallazgos restantes bloquea el uso del modelo hoy. Los que quedan son de "alcance no declarado explícitamente": por ejemplo, dos simplificaciones de jerarquía (`E22_Human-Made_Object`, pérdida de `subPropertyOf` en algunas relaciones) son inocuas siempre que el archivo se use fusionado con los tres vendors completos — que es como se usa hoy en el pipeline de validación, pero ningún documento lo fija como requisito explícito de uso futuro. Si alguna vez alguien quisiera consumir `CAO_CRM-1.0.rdf` de forma aislada (sin sus tres importaciones), convendría revisar ese punto primero.
- La ausencia de un catálogo corto de "roles de autoría MARC no cubiertos hoy" (editor, prologuista, ilustrador, etc.) en `informe-P14-roles-autorat.md` — mencionado de pasada pero no como lista explícita. Fácil de añadir cuando el equipo lo necesite, no antes.
- Ningún hallazgo 🔴 real permanece abierto en ninguna de las tres auditorías.

No se modificó `ontology/CAO_CRM-1.0.rdf` durante esta auditoría. Los únicos archivos modificados fueron los cuatro documentos de decisión listados en la sección (b), y el único archivo nuevo creado es este informe.
