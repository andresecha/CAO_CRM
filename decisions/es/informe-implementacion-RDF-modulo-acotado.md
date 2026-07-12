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
# Informe de implementación: del modelo JSON al módulo RDF acotado de CAO_CRM

**Fecha:** 2026-07-03
**Estado del archivo resultante:** verificado sintácticamente correcto, lógicamente consistente, y confirmado que abre sin errores en Protégé 5.6.8.
**Archivo final de esta etapa:** `imports/module/cao_crm-module-clean.rdf`

---

## 0. Qué se hizo, en una frase

Se tomó el diagrama conceptual del modelo CAO_CRM (guardado como `CRM_V8.json`, un archivo exportado de draw.io/diagrams.net), se extrajeron de ahí los nombres exactos de las clases y propiedades que el equipo confirmó como el alcance real del modelo, y con esa lista se generó automáticamente — no a mano — un archivo RDF que contiene *solo* esas piezas, tomadas literalmente de los archivos oficiales de CIDOC-CRM, LRMoo y CRMdig, sin arrastrar el resto de esas tres ontologías (que juntas suman miles de clases y propiedades).

---

## 1. Punto de partida: el diagrama, no el texto

El artículo del consorcio Ariane describe el modelo CAO_CRM mediante un diagrama (su "Figura 2"). Ese diagrama existe también como archivo de trabajo: `CRM_V8.json`, con **9 páginas** correspondientes a las partes del modelo:

| Página del diagrama | Qué representa |
|---|---|
| `Hiérarchie` | La columna vertebral del modelo: cómo se relacionan Obra → Expresión → Manifestación → Ítem → Objeto digital |
| `F1` | Todo lo relacionado con la Obra (`F1_Work`) |
| `F2` | Todo lo relacionado con la Expresión (`F2_Expression`) |
| `F3` | Todo lo relacionado con la Manifestación (`F3_Manifestation`) |
| `F5` | Todo lo relacionado con el Ítem físico (`F5_Item`) |
| `D1` | Todo lo relacionado con el Objeto digital (`D1_Digital_Object`) |
| `D2` | El proceso de digitalización (`D2_Digitization_Process`) |
| `model` | Vista de conjunto (las mismas piezas, todas juntas) |
| `exemple` | Un caso de uso ilustrativo con datos reales (la novela *Le Rouge et le Noir*) |

Cada "página" es, técnicamente, una lista de cajas y flechas (`cells`), y cada caja/flecha tiene un texto (`label`) — a veces el nombre técnico de una clase o propiedad de CIDOC-CRM/LRMoo/CRMdig (por ejemplo `E35_Title`), y a veces solo una etiqueta descriptiva en francés para que el diagrama se entienda mejor visualmente (por ejemplo "Titre").

---

## 2. Paso 1 — Extraer los nombres técnicos reales del JSON

**Objetivo:** separar, dentro de las 814 etiquetas del diagrama, cuáles son de verdad nombres de clases/propiedades de CIDOC-CRM/LRMoo/CRMdig, y cuáles son solo texto explicativo en francés (que no debía tratarse como parte del modelo formal).

**Cómo se hizo:** un script en Python leyó el JSON, recorrió las 7 páginas de módulo (excluyendo `model` y `exemple`, que son vistas repetidas de las mismas piezas) y filtró solo las etiquetas que seguían el patrón de nombre técnico real de CIDOC-CRM/LRMoo/CRMdig: una letra (`E`, `F`, `D`, `P`, `R` o `L`) seguida de un número y un guion bajo — por ejemplo `E35_Title`, `F1_Work`, `P1_is_identified_by`. Las etiquetas en francés como "Titre" o "Type de droit" no encajan en ese patrón y quedaron automáticamente fuera.

Resultado de este primer filtrado automático: 30 clases y 36 propiedades (contando cada propiedad una sola vez, sin su inversa por separado).

**Verificación humana:** el equipo revisó esa lista extraída y la corrigió/completó, añadiendo:
- `F5_Item`, que el filtro automático no capturó porque en el diagrama estaba escrito "F5 Item" (con espacio, no guion bajo).
- Las propiedades inversas explícitas (por ejemplo, no solo `R16_created` sino también `R16i_was_created_by`), porque en CIDOC-CRM/LRMoo/CRMdig cada relación tiene dos URIs distintas (una para cada sentido), y el diagrama no siempre mostraba las dos por separado.

**Lista final confirmada por el equipo (2026-07-03):** 31 clases, 60 propiedades de objeto (30 pares directa/inversa) y 4 propiedades de datos. Ver el detalle completo en la conversación de esa fecha; la lista está también incorporada como comentarios en los archivos de términos usados en el paso 3.

---

## 3. Paso 2 — Verificar que cada nombre existe de verdad en los archivos oficiales

Antes de generar nada, cada uno de los ~95 nombres se buscó literalmente (con `grep`) dentro de los archivos RDF/XML oficiales ya descargados en este repositorio (`imports/vendor/cidoc-crm-7.1.3.rdf`, `imports/vendor/lrmoo-1.1.1.rdf`, `imports/vendor/crmdig-5.0.rdf`), para confirmar que:

1. El nombre existe realmente (no es un error de transcripción del diagrama).
2. Pertenece a la ontología que se pensaba (a veces un mismo prefijo de letra puede prestarse a confusión).

Esto encontró dos casos a corregir:

- **`E60_Number` y `E62_String` no existen como URI** en ningún archivo oficial. No es un error — CIDOC-CRM explica en su propia documentación que estas "clases primitivas" están pensadas para representarse directamente como un valor de texto/número (`rdfs:Literal`), no como una entidad con URI propia. Se excluyeron de la lista de clases a extraer (quedan 29 clases reales con URI, de las 31 originalmente identificadas). El detalle completo de esta decisión está en `problemes-et-solutions.md (Problema 1)`.
- **`P21_has_general_purpose`** (como se había transcrito inicialmente del diagrama) no existe; el nombre real en el archivo oficial es **`P21_had_general_purpose`** (tiempo pasado). Corregido antes de generar nada.

---

## 4. Paso 3 — Generar el RDF automáticamente con ROBOT

**Herramienta usada:** [ROBOT](http://robot.obolibrary.org/), concretamente su comando `extract` con el método `subset`.

**Por qué esta herramienta y no copiar/pegar a mano:** copiar y pegar manualmente las definiciones desde los archivos oficiales sería lento, propenso a errores de transcripción, y sobre todo — como ya pasó antes con este mismo proyecto — el copy/paste manual (o una fusión mal hecha en Protégé) fue precisamente la causa de los problemas anteriores (contaminación del encabezado con "SKOS Vocabulary", pérdida de axiomas, inconsistencia lógica). Usar una herramienta automática, alimentada por una lista de nombres explícita y revisada, hace que el proceso sea:
- **Reproducible:** cualquiera puede volver a ejecutar el mismo comando y obtener el mismo resultado.
- **Trazable:** el archivo de entrada (la lista de términos) queda guardado y se puede auditar.
- **Fiel al original:** ROBOT copia las etiquetas, comentarios y definiciones exactamente como están en el archivo fuente oficial, sin reinterpretarlas.

**⚠ Corrección posterior a la primera versión de esta sección:** el primer intento ejecutó tres comandos separados, uno por ontología fuente, cada uno con su propia lista de términos (`terms-cidoc.txt`, `terms-lrmoo.txt`, `terms-crmdig.txt`). Ese método se abandonó — se detectó que pierde axiomas que cruzan entre ontologías (por ejemplo, `F1_Work rdfs:subClassOf E89_Propositional_Object`, una relación LRMoo→CIDOC-CRM, desaparecía aunque `E89_Propositional_Object` sí está en el alcance), porque al procesar LRMoo solo, `--method subset` no reconoce `E89_Propositional_Object` como un término "conocido" en ese archivo aislado. El detalle completo de este hallazgo está en `informe-completitud-labels-domain-range.md`, sección 0.

**El método final y correcto, realmente usado para generar `ontology/CAO_CRM-1.0.rdf`, combina las tres fuentes en un solo archivo antes de extraer, con una única lista de términos:**

```bash
# 1. Combinar las tres fuentes oficiales en un solo grafo
riot --output=rdfxml imports/vendor/cidoc-crm-7.1.3.rdf \
                      imports/vendor/lrmoo-1.1.1.rdf \
                      imports/vendor/crmdig-5.0.rdf \
     > /tmp/combined-sources.rdf

# 2. Extraer el módulo en una sola pasada, con la lista completa de 95 términos
robot extract --input /tmp/combined-sources.rdf \
              --method subset \
              --term-file imports/module-terms.txt \
              --output imports/module/combined-module.ttl
```

**El archivo `imports/module-terms.txt`** (incluido en este repositorio, también copiado a `imports/module-terms.txt`) es exactamente la lista de 95 términos —31 clases (29 con URI real, ver sección 3) + 60 propiedades de objeto + 4 propiedades de datos— que el equipo confirmó como alcance definitivo de CAO_CRM. Es el archivo real de entrada que produjo el módulo final; volver a ejecutar los dos comandos de arriba con ese mismo archivo reproduce exactamente el mismo resultado.

El método `subset` (a diferencia de otros métodos de extracción de ROBOT, como `mireot` o `star`) extrae *exactamente* los términos indicados, sin arrastrar automáticamente el resto de la jerarquía de clases de la ontología fuente. Esto es justo lo que CAO_CRM necesita: un modelo compuesto y acotado, no una copia parcial disfrazada de las tres ontologías completas. Combinar las fuentes antes de extraer (en vez de extraer cada una por separado) es lo que permite que esto siga siendo cierto *sin* perder las relaciones reales que cruzan entre CIDOC-CRM, LRMoo y CRMdig dentro del alcance elegido.

**Resultado de esta extracción, por fuente:**

| Fuente | Archivo generado | Líneas | Contenido |
|---|---|---|---|
| CIDOC-CRM 7.1.3 | `cidoc-crm-module.ttl` | 900 | 19 clases, 42 propiedades (38 de objeto + 4 de datos) |
| LRMoo 1.1.1 | `lrmoo-module.ttl` | 179 | 7 clases, 15 propiedades de objeto |
| CRMdig 5.0 | `crmdig-module.ttl` | 93 | 3 clases, 8 propiedades de objeto |

En total: **29 clases, 61 propiedades de objeto, 4 propiedades de datos — 1172 líneas**, frente a los miles de clases/propiedades que tienen las tres ontologías originales completas.

---

## 5. Paso 4 — Un caso que la extracción automática no pudo resolver sola: `P3_has_note`

La herramienta hizo su trabajo correctamente, pero **detectó y expuso** un problema que ya existía en el archivo oficial de CIDOC-CRM: la propiedad `P3_has_note` no tiene declarado ningún dominio ni rango en la versión RDF/XML 7.1.3 (aunque la documentación de lectura sí los describe). Al extraerla, ROBOT la dejó solo como una anotación (etiqueta + comentario), sin tipo de propiedad — lo más seguro que podía hacer al no saber si es una propiedad que conecta con otra entidad o con un valor de texto.

Este vacío se completó a mano, pero **replicando literalmente la convención que el propio archivo oficial usa para su propiedad hermana `P90_has_value`** (que sí está completamente declarada). La decisión completa, con las citas textuales de la documentación oficial que la justifican, está documentada en `problemes-et-solutions.md (Problema 1)` — no se repite aquí para no duplicar contenido.

---

## 6. Paso 5 — Fusionar los tres módulos y ponerles un encabezado propio

Los tres archivos generados en el paso 3 se combinaron en un solo grafo con `riot` (herramienta de Apache Jena):

```bash
riot --output=turtle cidoc-crm-module.ttl lrmoo-module.ttl crmdig-module.ttl > merged-module.ttl
```

**Problema encontrado al fusionar:** cada uno de los tres archivos fuente trae, heredado de su propio archivo original, una declaración `owl:Ontology` para sí mismo (una para CIDOC-CRM, una para LRMoo, una para CRMdig). Al juntarlos, el archivo fusionado quedaba con **tres identidades de "ontología" distintas y ninguna propia de CAO_CRM** — exactamente el tipo de ambigüedad de encabezado que causó el problema de "SKOS Vocabulary" documentado anteriormente en este proyecto (ver `validation/07-metadata/README.md`).

**Solución:** se eliminaron esas tres declaraciones (eran triples sueltos, sin ninguna otra anotación pegada, así que quitarlas no borra ninguna información real) y se añadió una única declaración limpia:

```turtle
<http://www.CAO_CRM.org/ontology/> rdf:type owl:Ontology .
```

El archivo resultante, `cao_crm-module-clean.rdf`, tiene **un solo encabezado, correspondiente a CAO_CRM y a nadie más**.

---

## 7. Verificación: ¿está listo para abrirse en Protégé?

Antes de dar el archivo por bueno, se hicieron cuatro comprobaciones independientes, en orden creciente de exigencia:

1. **Sintaxis RDF/XML** — comprobado con dos analizadores distintos (`rapper` y `riot`), ambos confirman que el archivo está bien formado: 751 triples parseados sin ningún error.
2. **Coherencia lógica** — comprobado con el razonador HermiT (a través de `robot reason`): el modelo es consistente, sin ninguna clase ni propiedad insatisfacible.
3. **Un único encabezado de ontología** — confirmado tras la limpieza del paso 6 (antes había tres, ahora hay exactamente uno, el de CAO_CRM).
4. **Apertura real en Protégé 5.6.8** — se lanzó Protégé directamente desde la terminal apuntando a este archivo, y se leyó su propio registro de actividad en tiempo real. Resultado textual:

   ```
   Loading ontology from file:<repo>/imports/module/cao_crm-module-clean.rdf
   Finished loading file:<repo>/imports/module/cao_crm-module-clean.rdf
   Loading for ontology and imports closure successfully completed in 2180 ms
   ```

   Y la ventana de Protégé que se abrió mostraba el título correcto: **`ontology (http://www.CAO_CRM.org/ontology/)`** — el identificador propio de CAO_CRM, no el de ninguna de las ontologías reutilizadas ni ninguna contaminación como la de "SKOS Vocabulary" que se encontró anteriormente.

   Único aviso (no un error): *"root element does not have an xml:base"* — una nota informativa de Protégé, no bloqueante; se puede añadir un `xml:base` explícito más adelante si se desea, pero no impide abrir ni trabajar con el archivo con normalidad.

**Conclusión: el archivo está correctamente constituido y confirmado que abre sin errores en Protégé.**

---

## 8. Qué queda pendiente después de este módulo

Este módulo (`cao_crm-module-clean.rdf`) contiene **únicamente las piezas reutilizadas** de CIDOC-CRM/LRMoo/CRMdig, ya acotadas al alcance que el equipo confirmó. Todavía no incluye:

- Los metadatos propios del encabezado de CAO_CRM (autoría, descripción, licencia, `owl:versionInfo`...) que sí existían — correctamente, sin contaminación — en versiones anteriores del archivo.
- Ninguna restricción o axioma adicional que sea composición propia de CAO_CRM (por ejemplo, cómo se conecta exactamente `D1_Digital_Object` con `F2_Expression`, si eso requiere alguna restricción `owl:Restriction` que no viniera ya declarada en las fuentes).
- Los datos de ejemplo de la página `exemple` del diagrama (el caso de *Le Rouge et le Noir*), que podrían convertirse en datos de prueba reales para `test-data/` y así dejar de tener el `03-shacl` con "0 Focus Nodes" (ver `validation/03-shacl/README.md`).

Estos pasos siguientes se abordarán por separado, cada uno con su propia verificación antes de darlo por cerrado — siguiendo la misma disciplina de este informe.
