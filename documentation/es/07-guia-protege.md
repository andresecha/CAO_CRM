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
# Cómo abrir y explorar el modelo CAO_CRM en Protégé (guía práctica paso a paso)

## Qué es Protégé

Protégé es el programa —gratuito, de código abierto, desarrollado por la Universidad de Stanford— que se usa para crear y revisar **ontologías**: esquemas formales que definen qué "tipos de cosas" existen en un dominio (por ejemplo, "Obra", "Persona", "Objeto digital") y cómo se relacionan entre sí. No hace falta saber programar: es una interfaz visual pensada para leer y editar un modelo sin escribir código.

El equipo de Ariane usa la versión 5.6.8, instalada aquí como aplicación Flatpak en Linux, pero Protégé funciona igual en Windows y Mac: los menús descritos abajo son los mismos. Esta guía cubre solo la **exploración** del modelo ya construido, no la edición.

## Paso 1: abrir el archivo del modelo

CAO_CRM se distribuye como un archivo `.rdf` (RDF/XML, un formato de texto con gramática estricta, explicado en otra sección de esta documentación). El archivo final del repositorio de Ariane se llama `ontology/CAO_CRM-1.0.rdf`.

Para abrirlo: en la barra de menús, **File > Open...**, se navega hasta la carpeta del archivo y se selecciona (también se puede arrastrar a la ventana del programa). Protégé tardará unos segundos en procesarlo —CAO_CRM incorpora clases y propiedades de varios estándares internacionales (CIDOC-CRM, LRMoo, CRMdig, entre otros)— y luego lo mostrará cargado.

## Paso 2: "Active Ontology" — la ficha de identidad del modelo

Al terminar de cargar, Protégé suele mostrar primero la pestaña **Active Ontology** ("ontología activa"); si no aparece, se selecciona en la fila de pestañas superior. Funciona como una ficha de identidad del archivo: muestra su IRI (una dirección única que la identifica en la web, sin que tenga por qué apuntar a una página real), la versión, quién la creó, bajo qué licencia se publica y comentarios generales. Es el lugar indicado para hacerse una primera idea de "qué es este archivo" antes de entrar en el detalle. Es, dicho sea de paso, la misma información que otra sección de esta documentación revisa como prueba de calidad: si esta ficha está incompleta o mezclada con datos de otra ontología, es aquí donde se detecta a simple vista.

## Paso 3: "Entities" — donde viven las clases y propiedades

La pestaña **Entities** ("entidades") es el corazón de la exploración: aquí se navega por todo lo que CAO_CRM define. Dentro tiene varias sub-pestañas:

- **Classes** (clases): la lista de "tipos de cosas" que reconoce el modelo —por ejemplo, `F1_Work` (una obra en abstracto) o `F2_Expression` (una realización concreta, como un texto en un idioma determinado)—, mostrada como un árbol jerárquico plegable, porque unas clases son subtipos de otras.
- **Object properties** (propiedades de objeto): relaciones que conectan una instancia de una clase con otra, como la que une una obra con la persona que la creó.
- **Data properties** (propiedades de dato): relaciones que conectan una instancia de una clase con un valor simple —texto, fecha, número—, no con otra entidad; por ejemplo, la propiedad que asocia una obra con el texto de su título.
- **Annotation properties** (propiedades de anotación): documentan el propio modelo, sin describir el dominio, como `rdfs:label` (etiqueta legible de un término) o `rdfs:comment` (su descripción).

Basta con hacer clic en el nombre de una clase o propiedad, en el panel izquierdo, para que el resto de la pantalla muestre su información detallada.

## Paso 4: leer la información de una clase o propiedad

Al seleccionar una clase o propiedad, Protégé muestra varios bloques que conviene identificar:

- **El nombre técnico**, arriba, que suele incluir un código heredado de los estándares que CAO_CRM reutiliza (por ejemplo, `F1_Work`, donde "F1" es el identificador que usa LRMoo, el estándar bibliográfico en el que se apoya esa parte del modelo).
- **Etiquetas (`rdfs:label`) en distintos idiomas**: como CAO_CRM hereda de estándares internacionales trabajados por comunidades de varios países, es normal encontrar la misma clase o propiedad con etiquetas en inglés, francés, alemán, portugués, ruso o chino, cada una marcada con su código de idioma (`en`, `fr`, `de`...). No es un error ni una duplicación, sino la manera estándar de leer el mismo término en distintos idiomas.
- **El comentario o definición** (`rdfs:comment`, a veces `skos:definition`): el texto que explica en prosa qué significa la clase o propiedad y cómo debe usarse; suele ser el dato más útil para entender su sentido sin adivinarlo por el nombre técnico.
- **Las superclases** (`SubClassOf`): indican de qué clase más general es un caso particular la seleccionada, es decir, de qué hereda su significado y sus reglas básicas. Por ejemplo, `F32_Item_Production_Event` (el evento de producción de un ejemplar físico) se declara subclase de `E12_Production`, una clase mucho más general de CIDOC-CRM —esa relación es la que garantiza que todo lo que es legal para una Producción también lo es para un evento de producción de ejemplar, sin necesidad de redeclararlo término por término.

Para las propiedades, el panel equivalente muestra además el **dominio** (`domain`, qué clase puede tener esa propiedad) y el **rango** (`range`, qué valor o clase puede recibir), que indican "quién se conecta con quién" en esa relación.

## El botón del razonador ("Reasoner")

En la barra de menús hay una opción llamada **Reasoner**, con motores disponibles como HermiT o Pellet. En una frase: el razonador revisa automáticamente si las reglas del modelo se contradicen entre sí, y de paso muestra relaciones que no se escribieron explícitamente pero que se deducen lógicamente de las demás.

Para explorar no hace falta activarlo, pero si se hace (**Reasoner > Start reasoner**, comparando luego la vista "Asserted" —lo que el modelo dice literalmente— con la "Inferred" —lo deducido—), es una forma sencilla de comprobar que lo que se lee es, además de legible, lógicamente coherente. Esta misma comprobación, aplicada de forma sistemática, es una de las pruebas de calidad descritas en la sección dedicada a la validación del modelo.

## Una recomendación final

Conviene seguir este orden la primera vez: primero la ficha general (**Active Ontology**), después el árbol de clases, y solo después las propiedades concretas. El cuadro de búsqueda de Protégé (icono de lupa, o `Ctrl+K`) permite escribir "Work" o "Título" y saltar directamente al término, sin recorrer el árbol completo a mano.
