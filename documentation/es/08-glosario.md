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
# Glosario de términos técnicos usados en este proyecto

Esta sección reúne, en orden alfabético, los términos técnicos que aparecen una y otra vez en la
documentación de CAO_CRM y en el repositorio de validación. No hace falta leerla de corrido: sirve
como referencia rápida para cuando, en otra página, un término aparezca sin explicación previa.

- **Clase (`owl:Class`).** Una categoría de cosas, no una cosa concreta. En CAO_CRM, `E21_Person` es
  la clase "todas las personas" y `F1_Work` es la clase "todas las obras". Una clase, por sí sola, no
  tiene ningún dato particular (ni nombre ni fecha); solo define un tipo. Ver también **instancia** y
  **subclase**.

- **Consistencia lógica.** Una ontología es *consistente* cuando no contiene ninguna contradicción
  interna que la vuelva imposible de cumplir. Un caso real de `validation/02-reasoning/` ilustra el
  problema: en una versión intermedia del modelo, el **razonador** detectó que, por equivalencias mal declaradas, una propiedad
  heredaba un valor de texto aunque su **rango** exigía una URI, algo imposible de satisfacer. Esa
  sola contradicción bastó para marcar toda la ontología como inconsistente, porque de una
  contradicción se puede "deducir" cualquier cosa.

- **Disyunción (`owl:disjointWith`).** Una declaración que dice "estas dos clases nunca pueden tener
  una instancia en común" (por ejemplo, `E67_Birth`/nacimiento y `E69_Death`/muerte disjuntas
  impedirían registrar un mismo evento como ambas cosas). El `ADR-001-disjointness.md` de este
  repositorio explica que CAO_CRM decidió no añadir ninguna disyunción, siguiendo la misma elección
  deliberada del propio CIDOC-CRM, que prefiere dejar esa restricción a criterio de cada proyecto.

- **Dominio (`rdfs:domain`) y rango (`rdfs:range`).** Cuando una **propiedad** conecta una cosa A con
  una cosa B, el dominio dice qué tipo de cosa puede ser A y el rango qué tipo de cosa puede ser B.
  Por ejemplo, `P3_has_note` ("tiene nota") tiene dominio `E1 CRM Entity` (cualquier entidad) y rango
  `rdfs:Literal` (cualquier literal simple), en la versión actual del modelo. Un matiz clave, explicado en `decisions/fr/problemes-et-solutions.md` (Problema 1): en OWL
  esto no es una validación que rechaza datos erróneos (eso es tarea de SHACL), sino una regla de la
  que el sistema *deduce* cosas automáticamente.

- **Espacio de nombres (namespace) / IRI.** Un prefijo compartido que evita que dos proyectos usen
  accidentalmente el mismo nombre para cosas distintas. Se implementa con un **IRI** (una versión de
  URI/URL que admite cualquier idioma), de modo que cada clase y propiedad tiene una dirección única,
  como `http://www.cidoc-crm.org/cidoc-crm/P3_has_note`. Cuando CAO_CRM reutiliza `P3_has_note`, no
  copia solo un nombre: reutiliza ese identificador exacto, lo que permite a cualquier programa saber
  sin ambigüedad de qué propiedad se trata.

- **Etiqueta multilingüe (`rdfs:label`).** El nombre "legible por humanos" de una clase o propiedad
  en un idioma concreto, marcado con una etiqueta de idioma (`@en`, `@fr`...); el identificador
  técnico (el IRI) no cambia con el idioma, solo cambia cómo se muestra. El `ADR-002-idiomas-LRMoo-
  CRMdig.md` documenta que un conjunto de términos de LRMoo/CRMdig solo tienen etiqueta oficial en inglés, y que
  el equipo decidió no inventar traducciones propias para no atribuir a esos consorcios un contenido
  que no publicaron.

- **Importar (`owl:imports`) vs. fusionar (merge).** `owl:imports` es una declaración formal que le
  dice a cualquier herramienta "carga también este otro archivo para razonar bien sobre este".
  `CAO_CRM-1.0.rdf` no declara ningún `owl:imports`; de CIDOC-CRM/LRMoo/CRMdig como de SKOS, copia una versión
  recortada dentro de su propio archivo, sin `owl:imports` formal (ver `imports/README.md`). Por eso
  existe un paso aparte de **fusión**: `imports/merge.sh` junta CAO_CRM con los archivos oficiales
  completos en `merged.ttl`, porque la copia recortada no trae toda la axiomática de esas ontologías.

- **Instancia / individuo.** Un ejemplo concreto de una clase, con datos propios. Si `E21_Person` es
  la clase "todas las personas", una instancia suya sería la persona real "Stendhal". En OWL,
  "instancia" e "individuo" son sinónimos.

- **Literal (`rdfs:Literal`) vs. tipo XSD.** Un literal es cualquier valor simple (texto, número,
  fecha) sin identidad propia. `rdfs:Literal` es la categoría más amplia posible de literales; los
  tipos **XSD** (del estándar XML Schema), como `xsd:string` o `xsd:decimal`, son subcategorías más
  estrictas. `decisions/fr/problemes-et-solutions.md` (Problema 1) documenta por qué CAO_CRM eligió `rdfs:Literal` para `P3_has_note`: es la
  misma convención que el archivo oficial de CIDOC-CRM usa en propiedades equivalentes como
  `P90_has_value`, aun representando conceptualmente "un número".

- **Nota de alcance (scope note).** El párrafo oficial que define una clase o propiedad, escrito por
  el consorcio correspondiente, explicando qué significa y qué no cubre. Por ejemplo, la *scope note*
  de `E59 Primitive Value` en CIDOC-CRM dice, cita textual, que *"the instances of E59 Primitive Value
  and its subclasses are not considered elements of the universe of discourse the CIDOC CRM aims to
  define and analyse"*: valores como números o textos no se tratan como "cosas" del mundo descrito,
  sino como la forma técnica de representar un dato simple. Es la fuente que se cita textualmente
  cuando surge una duda sobre cómo tratar una pieza reutilizada, como muestran los ADR de este
  repositorio.

- **Ontología.** Un esquema formal que define qué "tipos de cosas" existen en un dominio de
  conocimiento (obra, edición, ejemplar físico, archivo digital, persona, evento de creación...) y
  cómo se relacionan, de modo que tanto una persona como un programa puedan interpretarlo sin
  ambigüedad. CAO_CRM es la ontología de este repositorio: no inventa clases ni propiedades propias,
  sino que selecciona y ensambla piezas de CIDOC-CRM, LRMoo y CRMdig.

- **Propiedad de datos (`owl:DatatypeProperty`).** Un tipo de **propiedad** que conecta una
  **instancia** con un **literal** (texto, número, fecha), no con otra instancia. Por ejemplo, "esta
  obra `tiene como título` 'Le Rouge et le Noir'": el título es solo texto. `P3_has_note` es otro
  ejemplo: conecta cualquier entidad con una nota en texto libre.

- **Propiedad de objeto (`owl:ObjectProperty`).** Un tipo de **propiedad** que conecta una
  **instancia** con **otra instancia**, es decir, dos entidades con identidad propia. Por ejemplo,
  "esta obra `fue creada por` esta persona": ambas son entidades, a diferencia de un literal.

- **Razonador (reasoner).** Un programa que aplica las reglas lógicas de OWL sobre una ontología para
  comprobar que tiene sentido matemáticamente, deducir información implícita y detectar
  contradicciones. En este repositorio el razonador es HermiT, invocado vía ROBOT (ver
  `validation/02-reasoning/README.md`); su resultado principal es si la ontología es **consistente**
  y si tiene alguna clase insatisfacible (una clase que nunca podría tener ninguna instancia posible).

- **RDF/XML vs. Turtle (formatos de serialización).** Un mismo conjunto de datos en RDF se puede
  escribir en distintos formatos de texto, o *serializaciones*, sin que cambie su significado. RDF/XML
  es el formato basado en etiquetas XML —el que usa `CAO_CRM-1.0.rdf`— y suele ser más verboso.
  Turtle (extensión `.ttl`) es más compacto y legible, usado por ejemplo en `imports/module/`.
  Convertir de uno a otro no cambia ninguna clase ni relación, solo cómo se escribe el contenido.

- **SHACL.** Un lenguaje (Shapes Constraint Language) para definir reglas de validación que sí
  rechazan datos que no las cumplen, a diferencia del dominio y rango de OWL. Por ejemplo, una regla
  podría exigir que todo `E12_Production` tenga exactamente una fecha asociada. En este repositorio,
  `validation/03-shacl/` aplica esas reglas (con pySHACL) sobre `test-data/`, como capa complementaria
  a la comprobación de **consistencia lógica** del razonador.

- **SPARQL.** El lenguaje de consulta para interrogar datos en RDF, equivalente en su papel a SQL para
  bases de datos relacionales. Aquí se usa en dos formas, alineadas con las **preguntas de
  competencia** (los casos de uso que la ontología debe poder responder): consultas `ASK`
  (sí/no, en `sparql/ask/`) y `SELECT` (listas de resultados, en `sparql/select/`).

- **Subclase (`rdfs:subClassOf`).** Una relación entre dos clases que dice "todo lo que pertenece a
  esta clase pertenece también, automáticamente, a esta otra clase más general". Si `E21_Person`
  fuera subclase de `E39_Actor`, el razonador deduciría que cualquier persona es también un `E39_Actor`,
  sin declararlo aparte para cada individuo.

Otros conceptos mencionados en esta documentación —como el proyecto AMIS, la herramienta ROBOT o los
propios ADR (registros de decisión)— se explican en su contexto en las secciones correspondientes de
esta carpeta, y no se repiten aquí por no ser términos técnicos propios de OWL/RDF.
