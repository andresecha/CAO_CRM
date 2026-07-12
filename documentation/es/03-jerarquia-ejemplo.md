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
# La jerarquía del modelo, explicada con un ejemplo real

## Cinco maneras de existir

Cuando decimos "tengo *Le Rouge et le Noir* de Stendhal en la mesa", mezclamos sin darnos cuenta varias cosas distintas: la novela como creación intelectual, el texto tal como Stendhal lo redactó, la edición concreta que compramos, el libro físico con sus páginas y su tapa, y quizá también el PDF que descargamos para leerlo en la tableta. CAO_CRM (Corpus Author Ontology CRM), el modelo del consorcio Ariane presentado en la primera sección de esta documentación, separa explícitamente esas capas porque confundirlas tiene consecuencias reales: los derechos de autor sobre la obra no son los mismos que los derechos editoriales de una edición concreta; el estado de conservación de un ejemplar en una biblioteca no dice nada sobre la calidad de un escaneo que circula en internet; y una "primera versión" de una novela puede referirse tanto a un cambio de ideas del autor como a un cambio tipográfico del impresor.

El paper del consorcio lo resume así: *"le modèle repose sur une progression allant de l'œuvre comme concept abstrait à ses différentes formes matérielles ou numériques"*: el modelo organiza cinco entidades (categorías de cosas) en una progresión que va de la obra como idea abstracta hasta sus formas materiales o digitales, cada una correspondiente a un "régimen de existencia" distinto del mismo texto. Esa progresión, heredada de LRMoo (la extensión bibliográfica vista en la sección anterior), es: **F1_Work → F2_Expression → F3_Manifestation → F5_Item → D1_Digital_Object**.

## F1_Work: la idea, antes de cualquier redacción

`F1_Work` es la obra en su dimensión puramente conceptual: *"corresponde au projet dans sa forme la plus abstraite, indépendamment de toute réalisation matérielle ou de toute mise en forme particulière"* (corresponde al proyecto en su forma más abstracta, sin ninguna realización material o puesta en forma concreta). En nuestro ejemplo, `F1_Work` es "la novela que Stendhal concibió sobre Julien Sorel", con su autor (Henri Beyle, conocido como Stendhal), sus fechas de vida y el movimiento literario al que se lo asocia. A este nivel todavía no hay ni una frase escrita: es el proyecto intelectual, no su ejecución.

## F2_Expression: cuando la idea se convierte en texto

`F2_Expression` designa las diferentes puestas en forma identificables de esa idea, independientemente de los documentos físicos que las identifican. Aquí aparece el texto en sí —las palabras, el orden de los capítulos— pero sin atarlo aún a una edición concreta. El paper ilustra la distinción, sutil pero crucial, con el caso de Flaubert: *"la première idée de Madame Bovary de Flaubert, dont témoignent des lettres de Du Camp en juillet et août 1851, sont une expression de l'œuvre, distincte des expressions ultérieures que permet de reconstituer le reste de la correspondance de l'auteur"*: ya existían borradores documentados por cartas antes de un manuscrito acabado, y cada etapa sustancialmente distinta del contenido cuenta como una expresión diferente. El paper advierte que esta capa suele pasar inadvertida en el trabajo bibliográfico habitual.

## F3_Manifestation: la edición, con su editor, su año y su lugar

`F3_Manifestation` es donde aparece, por fin, la noción de "edición" que cualquier lector reconocería. LRMoo la define como *"products rendering one or more Expressions... defined by both the overall content and the form of its presentation"* (productos que plasman una o varias expresiones, definidos tanto por su contenido global como por la forma de su presentación). El paper añade que hay manifestación desde el momento en que la obra ya no existe solo en la mente de su creador: no es un ejemplar concreto, sino la forma editorial genérica de la que pueden derivar varios objetos. Siguiendo un ejemplo real de los materiales del proyecto, la manifestación de *Le Rouge et le Noir* que tomamos aquí es la "Édition critique imprimée de Le Rouge et le Noir (1830)", publicada por Le Divan en París en 1927, con Henri Martineau como responsable científico de la revisión del texto y del prefacio. El modelo distingue aquí dos responsabilidades bien distintas, cada una portada por una propiedad separada sobre el mismo evento de creación de la manifestación: Le Divan como editor comercial (`P14_has_publisher`) y Henri Martineau como editor científico responsable del contenido (`P14_has_scientific_editor`). A este nivel se documentan el editor, la fecha, el lugar de producción, el formato o la lengua: datos de la edición, no de la obra ni del ejemplar físico.

## F5_Item: el libro concreto que se puede tocar

`F5_Item` designa un ejemplar material particular: el objeto físico consultado o manipulado. Aquí ya no hablamos de "la edición de Le Divan de 1927" en abstracto, sino de un volumen concreto: el ejemplar de 21 x 29,7 cm, en papel con tinta negra y roja, en buen estado de conservación, guardado hoy en una biblioteca de París. El paper insiste en que varios ítems pueden corresponder a una misma manifestación: los ejemplares dispersos en distintas bibliotecas de esa edición comparten la manifestación, pero cada uno tiene su propio estado de conservación, su propia procedencia y su propia historia material —uno puede tener anotaciones a mano, otro una tapa dañada—.

## D1_Digital_Object: el archivo que consultamos en la pantalla

Por último, `D1_Digital_Object` es, según CRMdig, *"identifiable immaterial items that can be represented as sets of bit sequences... A D1 Digital Object does not depend on a specific physical carrier"* (elementos inmateriales identificables representables como secuencias de bits, que no dependen de un soporte físico concreto). En nuestro ejemplo sería el archivo EPUB o PDF de *Le Rouge et le Noir* que hoy aloja una biblioteca digital, con su propio identificador, su peso en megabytes y sus propias condiciones de uso, distintas de los derechos que rigen la edición impresa de 1927. El paper señala que el modelo prevé, desde `F3_Manifestation`, dos vías complementarias: hacia el objeto material (`F5_Item`) y hacia el objeto digital (`D1_Digital_Object`), y que ambas no son excluyentes. Si el archivo proviene de escanear el libro físico, la relación se documenta con un `D2_Digitization_Process`, que registra quién hizo el escaneo, cuándo y con qué herramientas; pero un objeto digital también puede "nacer digital", sin pasar nunca por el papel —este segundo caso se documenta con `D7_Digital_Machine_Event`, la clase general de CRMdig de la que `D2_Digitization_Process` es solo una especialización, precisamente porque no exige ningún objeto físico de origen.

## Por qué ninguna capa sobra

Separar estas cinco capas no es un capricho teórico: permite responder preguntas que, de otro modo, quedarían mezcladas. ¿El "buen estado de conservación" describe el libro de papel o el archivo PDF? ¿Cuántas ediciones distintas existen de la novela, y en qué se diferencian de los borradores previos a un texto terminado? Cada pregunta se responde en un nivel distinto, y esa separación es lo que permite cruzar información sin confundir el estado físico de un ejemplar con las condiciones de licencia de su copia digital.

## ¿A quién pertenecen los derechos? Una respuesta en un nivel preciso, no en todos a la vez

La pregunta sobre los derechos de autor merece una respuesta construida, porque en realidad mezcla dos naturalezas de derecho distintas. El **derecho moral** (en el sentido del derecho de autor continental) es inalienable: protege la integridad de la obra misma, independientemente de tal o cual edición, y se responde de forma única desde `F1_Work`, siguiendo el camino `F1_Work → F27_Work_Creation → P14_has_original_author → Persona` —el camino que la propia LRMoo llama, en su comentario oficial, "la noción de creador de la obra". Los **derechos patrimoniales** (cesibles —derechos de edición, derechos de reproducción digital) se vinculan, en cambio, correctamente al nivel que los produjo concretamente: la Expresión, la Manifestación o el Objeto digital, según el caso, cada uno mediante `P104_is_subject_to`. Una misma novela puede así tener un único autor moral incuestionable, y a la vez distintos derechos de edición para cada Manifestación y condiciones de uso propias para cada copia digital —exactamente lo que la separación en cinco capas permite expresar sin contradicción.
