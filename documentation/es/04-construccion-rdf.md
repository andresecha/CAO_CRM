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
# Cómo se construyó el archivo RDF del modelo, explicado paso a paso

## Dos palabras antes de empezar

Un archivo **RDF** (o **RDF/OWL**, casi lo mismo, con más reglas lógicas encima) es una lista de afirmaciones simples del tipo "esto es un tipo de cosa" o "esta cosa se relaciona con esta otra de tal manera" —miles de esas afirmaciones reunidas, en un formato que tanto una persona como un programa pueden leer sin ambigüedad. Es la versión formal del modelo CAO_CRM: no un dibujo, sino el archivo que un programa puede realmente cargar y usar. Este documento cuenta, paso a paso, cómo se pasó del diagrama que describe CAO_CRM al archivo final: `ontology/CAO_CRM-1.0.rdf` (1165 triples, 41 clases, 84 propiedades de objeto, 5 propiedades de datos).

## El punto de partida: un diagrama, no un texto

El artículo del consorcio Ariane presenta CAO_CRM mediante un diagrama, que existe también como archivo de trabajo en formato Drawio (un formato para dibujar y anotar esquemas), repartido en 9 páginas: la columna vertebral del modelo (Obra, Expresión, Manifestación, Ítem físico, Objeto digital), un bloque para cada uno de esos elementos, el proceso de digitalización, una vista de conjunto y un ejemplo completo a partir de una novela concreta (*Le Rouge et le Noir*, de Stendhal).

Cada casilla o flecha del diagrama lleva un texto asociado: a veces el nombre técnico exacto de un elemento de CIDOC-CRM, LRMoo o CRMdig (como `E35_Title`), a veces solo una etiqueta descriptiva en francés (como "Titre"). El primer trabajo consistió en distinguir, entre cientos de etiquetas, las que eran elementos del modelo formal de las que eran solo texto explicativo —y luego, ya con esa primera extracción hecha, revisar pacientemente el propio diagrama contra los archivos oficiales, casilla por casilla y flecha por flecha, para encontrar lo que faltaba o lo que se usaba de forma incorrecta.

## Paso 1 — Extraer el módulo inicial con ROBOT

Una analogía puede ayudar aquí: CIDOC-CRM, LRMoo y CRMdig son, juntas, como tres enormes libros de referencia. CAO_CRM solo necesita un puñado de páginas de cada uno —las que definen los elementos identificados en el diagrama. "Extraer un módulo" significa fotocopiar solo esas páginas, en vez de fotocopiar los tres libros enteros.

Esta extracción no se hizo a mano, sino con una herramienta llamada **ROBOT**, en su modo `extract`/`subset` (extraer un subconjunto exacto):

```bash
robot extract --input imports/vendor/cidoc-crm-7.1.3.rdf \
              --method subset --term-file imports/module-terms.txt \
              --output ontology/CAO_CRM.rdf
```

El modo `subset` es esencial: a diferencia de otros modos, que arrastran automáticamente toda la jerarquía por encima de lo pedido, `subset` extrae únicamente los términos indicados en `imports/module-terms.txt`, y nada más —la lista exacta, verificable, que hace que todo el módulo quepa en un centenar de términos en vez de en los miles que suman las tres ontologías completas.

## Paso 2 — Ocho problemas encontrados al comparar el diagrama con los archivos oficiales

Una vez extraído el primer módulo, había que verificar que correspondiera realmente a lo que el diagrama del consorcio quería expresar, y que cada relación dibujada fuera legal según las reglas oficiales (qué clase puede llevar qué propiedad). Esta verificación, hecha sistemáticamente página por página, sacó a la luz ocho problemas reales —documentados en detalle, con cita oficial completa para cada uno, en `decisions/fr/problemes-et-solutions.md`:

1. **La descripción de un objeto** (`P3_has_note`) pasaba por una cadena artificial (`E55_Type` → `E62_String`) en vez de una nota directa —y `E62_String`, como `E60_Number` más adelante, ni siquiera existe como clase real en CIDOC-CRM: son "valores primitivos", siempre representados como texto o un número simple, nunca como una entidad con identidad propia.
2. **La lengua de una Expresión** estaba ligada al nivel equivocado (`F3_Manifestation`) y con la propiedad equivocada —corregido colocándola en `F2_Expression`, co-tipada `E33_Linguistic_Object`, vía `P72_has_language`, exactamente como LRMoo lo prescribe en su propio comentario oficial para esta clase.
3. **La localización de un ejemplar físico** (`F5_Item`) no tenía ningún mecanismo legal —resuelto co-tipando el ejemplar como `E22_Human-Made_Object` (una práctica que el comentario oficial de `F5_Item` sanciona explícitamente) para permitirle `P54`/`P55_has_current_location`.
4. **Los derechos** (`P104_is_subject_to`) estaban dibujados sobre clases que no pueden legalmente llevarlos (`F1_Work`, ciertas actividades) —resuelto distinguiendo derecho moral (ligado al autor de la Obra vía el camino ya legal `F27_Work_Creation`) de derechos patrimoniales (cesibles, ligados a la Expresión o a la Manifestación).
5. **La producción de un ejemplar** usaba un evento genérico —reemplazado por `F32_Item_Production_Event`, la clase de LRMoo prevista específicamente para eso.
6. **El objeto digital que lleva una dimensión** (peso en bytes, resolución) usaba `D1_Digital_Object` directamente —corregido co-tipando `D9_Data_Object`, exactamente la clase que el comentario oficial de CRMdig indica para llevar `L61_contains_value_set_of`.
7. **Las dimensiones físicas** carecían de unidad de medida —añadido vía `P91_has_unit`/`E58_Measurement_Unit`.
8. **La precisión de las fechas** había perdido, en la primera extracción, el tipado XSD que el archivo original de Mélanie Bouland sí tenía correctamente —restaurado (`xsd:dateTime`, `xsd:integer`) sin quitar nada de lo que el módulo ya tenía.

Un noveno caso, más sutil, exigió revisar una conclusión anterior: una rama del diagrama distinguía la digitalización de un objeto físico existente (`D2_Digitization_Process`) de la producción directamente digital, sin soporte físico previo. Un primer análisis había concluido que era un error de copiar y pegar a corregir eliminando la rama; un examen más profundo del texto del paper mostró que era, al contrario, una distinción querida por el equipo, solo implementada con la clase técnica equivocada —corregida retipándola como `D7_Digital_Machine_Event`, la clase general de CRMdig de la que `D2_Digitization_Process` es solo una especialización, sin exigir ningún objeto físico de entrada.

## Paso 3 — Completar la matriz de 4 categorías × 5 clases

El paper del consorcio organiza cada nivel del modelo (Obra, Expresión, Manifestación, Ítem, Objeto digital) según cuatro categorías transversales: Características, Proceso, Estatuto, Relación. Una verificación exhaustiva de esta matriz (documentada en `decisions/fr/complete-model.md`) permitió encontrar y completar tres carencias reales: las relaciones entre expresiones (`R75_incorporates`, `R76_is_derivative_of`), las relaciones entre obras (`R2_is_derivative_of`), y el camino legal completo que une un evento de producción con el ejemplar que produce (`R28_produced`, añadida el 7 de julio tras comprobar que el diagrama ya la usaba pero el módulo RDF todavía no la tenía).

## Paso 4 — Roles de actor que ninguna propiedad oficial distinguía

El paper distingue varios roles alrededor de un mismo texto, que ninguna propiedad oficial de CIDOC-CRM diferencia de forma nativa: una sola propiedad genérica, `P14_carried_out_by`, cubre cualquier rol en cualquier actividad. La solución adoptada se apoya en una regla que el propio CIDOC-CRM enuncia en su preámbulo (la "Encoding Rule 4"): autoriza explícitamente la creación de subpropiedades con nombre propio para precisar un rol, con un ejemplo concreto provisto por el propio estándar. A nivel de la Expresión, se distinguen así tres roles de autoría (autor original, traductor, persona que hizo una versión abreviada) mediante `P14_has_original_author`, `P14_has_translator` y `P14_has_abridger`, cada una alineada con el vocabulario internacional MARC Relator Terms. El detalle completo, con las opciones descartadas, está en `decisions/fr/informe-P14-roles-autorat.md`.

El mismo principio se extiende a la Manifestación: el paper distingue ahí explícitamente la responsabilidad del editor comercial (quien publica e imprime, como Le Divan para la edición de 1927 de *Le Rouge et le Noir*) de la del editor científico (quien establece el texto crítico y redacta el prefacio, como Henri Martineau) — dos roles portados respectivamente por `P14_has_publisher` y `P14_has_scientific_editor` sobre el mismo evento `F30_Manifestation_Creation`. Esta última propiedad se aplica también, por separado, al Ítem y al Objeto digital, cada vez que una actividad científica distinta (colación de un ejemplar, decisiones editoriales sobre una edición digital) compromete la responsabilidad de un especialista independientemente del trabajo material de producción. El detalle completo, con la cita del paper y la justificación de cada nivel, está en `decisions/fr/informe-activite-editoriale-scientifique.md`.

## Paso 5 — Restaurar un dominio perdido en la primera extracción

Una última verificación, hecha antes de la publicación, reveló que cuatro propiedades muy generales (`P4_has_time-span`, `P7_took_place_at`, `P16_used_specific_object`, `P104_is_subject_to`, y sus inversas) habían perdido su dominio o rango oficiales en la primera extracción: la clase que exigen (`E72_Legal_Object`, `E2_Temporal_Entity`, `E4_Period`, `E70_Thing`) nunca se había incluido en el módulo, por no ser necesaria como casilla visible del diagrama. Estas cuatro clases, puramente abstractas, se añadieron para restaurar la restricción original, sin cambiar nada más.

## Paso 6 — Verificar, en cada etapa, que el archivo funciona de verdad

Cada adición descrita arriba fue seguida de las mismas verificaciones: que el archivo siga bien formado (tres lectores independientes), que el modelo siga siendo lógicamente coherente al fusionarlo con las tres fuentes oficiales completas (razonador HermiT), que ningún axioma de las fuentes originales se haya perdido en el camino, y que se abra sin problemas en Protégé. El detalle completo de esta cadena de verificación es el tema de la siguiente sección de esta documentación.

## Una última verificación independiente: tres auditorías sucesivas

Antes de dar el trabajo por terminado, tres auditorías independientes y sucesivas revisaron, cada una sin confiar en la anterior, todas las afirmaciones de este proceso contra los propios archivos fuente y no contra resúmenes: una auditoría del RDF término por término, una auditoría de la documentación y la conformidad conceptual de cada decisión, y una verificación cruzada final. El veredicto de esta cadena: no queda ningún defecto crítico sin documentar. El detalle completo está en `decisions/fr/auditoria-1-rdf.md`, `auditoria-2-documentacion-y-conformidad.md` y `auditoria-3-verificacion-final.md`.
