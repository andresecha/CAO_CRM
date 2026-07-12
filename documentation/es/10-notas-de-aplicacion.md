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
# Notas de aplicación: los roles de actor y los valores controlados del modelo

Esta sección reúne, para cada propiedad de rol propia de CAO_CRM y para cada categoría de valor controlado (`E55_Type`) usada en el modelo, una **nota de aplicación** en el mismo sentido en que el propio CIDOC-CRM emplea este término: no solo la definición formal (ya dada en el archivo RDF y en las demás secciones de esta documentación), sino un ejemplo concreto que muestra cómo se usa realmente la propiedad o el valor, en la misma línea del estilo que los propios archivos oficiales practican — una frase de ilustración añadida al final de la nota de alcance, nunca una redefinición.

## Los cinco roles de actor

Las cinco subpropiedades de `P14_carried_out_by` declaradas en CAO_CRM (ver `05-decisiones-adr.md`) comparten todas el mismo dominio (`E7_Activity`) y el mismo rango (`E39_Actor`); lo único que las distingue es el rol que precisan. Cada una corresponde a un código MARC Relator Terms oficial, y cada una se ilustra aquí con el ejemplo de *Le Rouge et le Noir* ya usado a lo largo de esta documentación.

- **`P14_has_original_author`** ("tiene por autor original", MARC `aut`). Se aplica sobre el evento de creación de la Obra, `F27_Work_Creation`. Por ejemplo: `F27_Work_Creation --P14_has_original_author--> Stendhal`, para el evento de concepción de la novela como proyecto intelectual — independiente de cualquier edición o traducción posterior.

- **`P14_has_translator`** ("tiene por traductor", MARC `trl`). Se aplica sobre el evento de creación de una Expresión, `F28_Expression_Creation`, cuando esa Expresión resulta de una traducción. Por ejemplo: `F28_Expression_Creation --P14_has_translator--> Elisabeth van Bebber`, para el evento que produce la versión alemana de una novela de Agatha Christie a partir del texto inglés original (ejemplo ya desarrollado en `informe-P14-roles-autorat.md`).

- **`P14_has_abridger`** ("tiene por abreviador", MARC `abr`). Se aplica también sobre `F28_Expression_Creation`, cuando la Expresión producida es una versión abreviada del texto, sin cambio de idioma. Por ejemplo: `F28_Expression_Creation --P14_has_abridger--> [nombre de la persona]`, para el evento que produce la versión abreviada en inglés de *Murder on the Orient Express* mencionada en el paper fuente del proyecto.

- **`P14_has_scientific_editor`** ("tiene por editor científico", MARC `edt`). Se aplica sobre el evento de creación de la Manifestación, `F30_Manifestation_Creation`, o sobre una actividad científica autónoma vinculada a un Ítem o a un Objeto digital. Por ejemplo: `F30_Manifestation_Creation --P14_has_scientific_editor--> Henri Martineau`, para el evento que establece la edición crítica de 1927 de *Le Rouge et le Noir* — revisión del texto y redacción del prefacio, la responsabilidad intelectual sobre el contenido, distinta de la producción material del libro.

- **`P14_has_publisher`** ("tiene por editor comercial", MARC `pbl`). Se aplica sobre `F30_Manifestation_Creation` y sobre `F32_Item_Production_Event`. Por ejemplo: `F30_Manifestation_Creation --P14_has_publisher--> Le Divan`, para la misma edición de 1927, esta vez desde el punto de vista de la editorial responsable de la publicación y de la impresión — una responsabilidad comercial y material, distinta de la del editor científico, y portada por una propiedad diferente sobre el mismo evento.

Estas dos últimas propiedades pueden coexistir sobre un mismo evento `F30_Manifestation_Creation`, cada una vinculada a un actor distinto: es exactamente lo que muestra el ejemplo de *Le Rouge et le Noir*, donde Le Divan y Henri Martineau intervienen ambos, a títulos distintos, en la existencia de la misma manifestación. El detalle completo de esta distinción está en `decisions/fr/informe-activite-editoriale-scientifique.md`.

## Los valores controlados (`E55_Type`)

CIDOC-CRM prevé, para numerosas propiedades, un mecanismo de tipado genérico: `P2_has_type` relaciona una entidad con un valor `E55_Type`, que cumple el papel de un término de vocabulario controlado (ver el glosario, `08-glosario.md`, para la definición formal del mecanismo). CAO_CRM lo usa en varios puntos del modelo para precisar categorías que ni CIDOC-CRM, ni LRMoo, ni CRMdig prevén representar con una subclase dedicada. A continuación, con un ejemplo concreto para cada una, las categorías de valores controlados efectivamente usadas en el modelo.

- **Tipo de manifestación**, sobre `F3_Manifestation`. Por ejemplo: "Edición", para distinguir una edición crítica impresa de una edición audiovisual o de una reimpresión.

- **Modo de producción**, sobre el evento de creación de la Manifestación. Por ejemplo: "Impresión", para la manera en que la manifestación fue materialmente producida.

- **Modo de disposición**, sobre `F5_Item`. Por ejemplo: "Libro", para la forma física del ejemplar (a diferencia de un folio, un cuaderno, un legajo).

- **Formato**, sobre `D1_Digital_Object`. Por ejemplo: "PDF", para el formato de archivo del objeto digital.

- **Tipo de proceso**, sobre `D2_Digitization_Process`/`D7_Digital_Machine_Event`. Por ejemplo: "Escaneo", para el método técnico empleado en la digitalización.

- **Tipo de derecho**, sobre `E30_Right`, en cada uno de los niveles (Expresión, Manifestación, Objeto digital) donde se documenta un derecho patrimonial vía `P104_is_subject_to`. Por ejemplo: "Dominio público", "Derecho de autor" o "Propiedad intelectual", según el régimen jurídico aplicable al recurso en cuestión. Siguiendo el mismo mecanismo, una nota asociada (`P3_has_note`) puede precisar el detalle ("Derechos de editores/impresores", "Derechos de reproducción digital").

- **Sistema de escritura**, sobre `F2_Expression` (co-tipada `E33_Linguistic_Object`), siguiendo directamente la propia instrucción del comentario oficial de LRMoo para esta clase, y el patrón que el propio CIDOC-CRM aplica a `E34_Inscription`: *"The alphabet used can be documented by P2 has type: E55 Type."* Por ejemplo: "Escritura latina", relacionada mediante `P127_has_broader_term` con un ancla más general, "Tipo de sistema de escritura", que permite distinguir programáticamente esta faceta de otros valores `E55_Type` que comparten la misma propiedad `P2_has_type` en otras partes del modelo (ver `decisions/fr/complete-model.md` (sección 4) para el detalle de esta elección).

- **Tipo de actividad**, sobre la rama de "actividades editoriales" (`F30_Manifestation_Creation`, o la actividad científica autónoma vinculada a un Ítem u Objeto digital — ver la sección anterior). Por ejemplo: "Revisión crítica", para tipar con precisión la naturaleza del trabajo científico realizado, o "Colación de ejemplar" cuando se trata de examinar un ejemplar físico particular en vez de establecer el texto de la edición. Es el mismo mecanismo que el comentario oficial de `F28_Expression_Creation` recomienda para distinguir, por ejemplo, una traducción de una revisión: *"The P2 has type (is type of) property can be used to specify the type of the instance of F28 Expression Creation (i.e., activities such as translating, revising, or arranging music are types of creation process)."*

- **Tipo de identificador**, sobre `E42_Identifier`, cada vez que un recurso lleva varios identificadores de naturaleza distinta. Por ejemplo: "ISBN" o "ARK", para distinguir un identificador comercial estándar de un identificador perenne asignado por un servicio de archivo (el modelo ya usa, en su ejemplo trabajado, un identificador con la forma `ark:/12148/cb119255047`).

- **Estado**, sobre `E3_Condition_State`, siguiendo exactamente el ejemplo que el propio comentario oficial de esta clase de CIDOC-CRM ofrece: *"For example, the instance of E3 Condition State … can be characterized as an instance 'wrecked' of E55 Type."* Por ejemplo, para un ejemplar físico: "Buen estado", en contraposición a un estado dañado o frágil.

- **Tipo de codificación**, sobre `D1_Digital_Object`, para documentar el método técnico mediante el cual se produjo u ocerizó el contenido digital. Por ejemplo: "OCR e IIIF", correspondiente al reconocimiento óptico de caracteres combinado con un servicio de presentación de imágenes IIIF.

En cada caso, el valor en sí sigue siendo un simple término —nunca una clase nueva propia de CAO_CRM—: es el mecanismo `E55_Type`/`P2_has_type` el que aporta la precisión, exactamente como lo prevé el propio CIDOC-CRM para sus clases.
