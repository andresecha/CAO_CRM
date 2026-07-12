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
# Qué es CAO_CRM y para qué sirve

## El problema: un texto literario no es una sola cosa

Cuando un investigador en literatura se propone describir una obra —una novela, un poemario, una correspondencia de autor—, descubre pronto que "describirla" puede significar cosas muy distintas. Se puede hablar de la obra como idea o proyecto intelectual (lo que Flaubert imaginaba antes de escribir una sola línea de *Madame Bovary*), como texto con distintas versiones (el manuscrito, las variantes, la edición corregida), como objeto material conservado en una biblioteca, o como archivo digital, resultado de una digitalización o nacido directamente en formato electrónico. No son cuatro maneras de decir lo mismo: cada una responde a una lógica distinta, involucra actores distintos (autor, editor, bibliotecario, archivista, equipo técnico) y exige un vocabulario propio.

El artículo del consorcio Ariane que documenta CAO_CRM lo resume así: *"comment, dès lors, représenter, au sein d'un cadre sémantique cohérent, une entité qui relève simultanément de la création intellectuelle, de la matérialité documentaire, de l'herméneutique littéraire et de l'environnement numérique?"* —es decir, cómo representar, dentro de un marco coherente de significado, algo que es a la vez creación intelectual, objeto material, materia de interpretación literaria y recurso digital, sin reducirlo a una sola de esas dimensiones. Ese es el problema que CAO_CRM (Corpus Author Ontology CRM) intenta resolver: ofrecer un modelo unificado —lo que en este campo se llama una **ontología**, un esquema formal que define qué "tipos de cosas" existen en un dominio (obra, edición, ejemplar físico, archivo digital, persona, evento de creación...) y cómo se relacionan entre sí— capaz de acompañar a un corpus literario a lo largo de todo su ciclo de vida.

Sin ese marco común, cada comunidad profesional describe el mismo objeto con sus propias categorías: bibliotecarios, archivistas, filólogos y genetistas del texto priorizan aspectos distintos. El resultado, señala el artículo, es una descripción fragmentada en la que los metadatos —los datos que describen a un recurso, como su autor, fecha o formato— terminan siendo incompletos y difíciles de cruzar automáticamente.

## AMIS: un asistente de inteligencia artificial que necesitaba un "cerebro" conceptual

CAO_CRM no nació como un ejercicio teórico aislado, sino como respuesta a una necesidad concreta del proyecto europeo **AMIS** (Advanced Metadata Intelligent System), desarrollado dentro de Ariane con financiación europea (OSCARS, Open Science Clusters' Action for Research & Society). AMIS es una aplicación web que ayuda a crear y enriquecer metadatos de recursos textuales digitales (PDF, imágenes, XML/TEI) de forma semiasistida: en vez de dejar que el investigador rellene manualmente cada campo —tarea que el artículo califica de "chronophage" (que consume mucho tiempo) e idiosincrásica—, un "robot" apoyado en IA (modelos de visión, que leen una página digitalizada, y grandes modelos de lenguaje, o LLM) analiza el documento y propone los datos, que el investigador valida, corrige o rechaza.

Durante el desarrollo de AMIS surgió un obstáculo central: los modelos de lenguaje detectan razonablemente bien datos como el autor, el título o la fecha, pero no disponen por sí mismos de ningún marco conceptual que les permita distinguir a qué "nivel" pertenece cada dato. ¿Ese título describe la obra en abstracto, esta edición concreta, o el archivo PDF que se está consultando ahora? Como señala el propio artículo, *"il lui manquait une base de connaissances qui lui permette d'organiser ces données"* —es decir, al sistema le faltaba una base de conocimiento para organizar esos datos. CAO_CRM es precisamente esa base: la estructura conceptual que indica qué entidades existen (obra, edición, ejemplar físico, objeto digital, y los procesos que los relacionan) y qué información corresponde a cada una. Gracias a ella, AMIS organiza de forma coherente lo extraído y usa la misma estructura para guiar el enriquecimiento por RAG (Retrieval-Augmented Generation: un LLM que consulta fuentes externas para completar información).

## Por qué construir un modelo propio en vez de usar uno ya existente

Antes de crear una nueva ontología, el consorcio Ariane hizo lo contrario: buscó sistemáticamente recursos ya existentes que pudieran, con ajustes razonables, cubrir las necesidades de AMIS, mediante un inventario de una cuarentena de ontologías del dominio del arte y la cultura. El resultado fue revelador: solo nueve concernían específicamente al campo de los textos y la ficción, y cada una cubría solo una parte del problema —unas privilegiaban los metadatos bibliográficos, otras las entidades históricas mencionadas en los textos, otras más las dimensiones lingüísticas o de género literario. Ninguna, concluye el artículo, permitía representar de forma continua todo el proceso literario, desde las huellas genéticas de la creación hasta las formas de difusión y sus reutilizaciones digitales.

Ariane era consciente del riesgo de añadir una ontología más a un paisaje ya disperso; por eso el consorcio no partió de cero: decidió apoyarse en estándares internacionales ya bien establecidos en el patrimonio cultural (de los que trata otra sección de esta documentación) en vez de inventar un vocabulario nuevo. Pero, tras evaluarlos, concluyó que ninguno de ellos, ni siquiera combinados, resolvía por completo las necesidades de AMIS: unos eran demasiado generales y no distinguían con precisión la obra, sus ediciones y sus objetos digitales; otros describían bien los aspectos técnicos de la digitalización pero dejaban en la sombra el trabajo científico —el de un editor crítico, por ejemplo— que consiste en decidir qué variantes conservar. De ahí la decisión de construir CAO_CRM: no como una alternativa que ignora lo existente, sino como una articulación original de esos estándares, completada donde era necesario, para acompañar un corpus literario, con coherencia, desde la idea hasta el archivo digital.

## En síntesis

CAO_CRM es un intento de darle a las humanidades digitales algo que aún no tenían de forma unificada: un lenguaje común y formal para describir corpus literarios en todas sus dimensiones —intelectual, material, editorial y digital— sin perder la precisión que exige la investigación filológica, ni la posibilidad de que un sistema como AMIS trate esa descripción de forma coherente. No es un fin en sí mismo, sino una infraestructura conceptual que sostiene tanto el trabajo experto de los investigadores como la asistencia que la inteligencia artificial puede ofrecerles.
