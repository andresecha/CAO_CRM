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
# Informe: qué falta para publicar CAO_CRM como ontología usable, citable y descubrible en línea

**Fecha:** 5 de julio de 2026
**Motivación:** hoy no existe ninguna forma de que alguien fuera de este repositorio Git use, cite o encuentre CAO_CRM en línea. Tener el `.rdf` bien construido (validado, consistente, documentado) es condición necesaria pero no suficiente — publicar una ontología es, en sí mismo, un conjunto de pasos técnicos distintos, con su propia literatura de buenas prácticas. Este informe investiga esos pasos específicamente, con fuentes verificadas, y los aplica al caso concreto de CAO_CRM.
**Relación con el resto del proyecto:** este informe trata específicamente la **infraestructura de publicación** (dominio, resolución de URIs, alojamiento) — un asunto ortogonal a las decisiones de modelado del **contenido** de la ontología, documentadas en el resto de `decisions/`; ambos frentes pueden avanzar en paralelo.

---

## 0. Punto de partida, verificado hoy directamente (no asumido)

| Comprobación | Resultado |
|---|---|
| ¿Resuelve `http://www.CAO_CRM.org/ontology/` (el namespace declarado en el RDF)? | **No.** `curl` no puede ni resolver el nombre de dominio (`Could not resolve host`) — no es que el servidor esté caído, es que ese dominio, tal como está escrito en el RDF, no existe registrado y apuntando a nada. |
| ¿Existe `CITATION.cff`, `codemeta.json`, `.htaccess` en el repositorio? | **No**, ninguno de los tres. |
| ¿Hay algún pipeline de despliegue/publicación (GitHub Pages, GitLab Pages)? | **No.** Solo existe `.github/workflows/validate.yml`, que **valida** en cada push — no publica ni despliega nada. |
| ¿Está CAO_CRM registrado en algún catálogo de ontologías? | No, en ninguno. |
| ¿Tiene DOI? | No. |

**Conclusión de partida: se necesita infraestructura nueva, no solo "activar algo que ya existe pero está apagado".**

---

## 1. El problema central: la URI de cada clase/propiedad tiene que resolver de verdad

Esto es la base de todo lo demás — sin esto, ningún catálogo va a aceptar la ontología, y cualquier programa que intente "seguir" (`dereference`) una de sus URIs (por ejemplo `http://www.CAO_CRM.org/ontology/E7_Activity`) no obtendrá nada.

**El patrón estándar** (documentado en el *Note* del W3C [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/) y en [Best Practice Recipes for Publishing RDF Vocabularies](https://www.w3.org/TR/swbp-vocab-pub/)) es **"303 URIs" con negociación de contenido**: la URI de un término no es un archivo descargable en sí misma — el servidor responde con una redirección `303 See Other` hacia una página HTML legible si quien pregunta es un navegador (`Accept: text/html`), o hacia el RDF/Turtle/JSON-LD si quien pregunta es un programa. Es justo la diferencia entre "esta URI identifica un concepto" y "esta URI es un documento".

**Cómo resolverlo sin tener un dominio propio verificado:**

- **[w3id.org](https://w3id.org/)** — servicio de identificadores permanentes gestionado por el *Permanent Identifier Community Group* del W3C. Confirmé en vivo que está activo y funcionando: es exactamente el servicio que usa **FOOPS!** (`https://w3id.org/foops/` redirige de verdad a `https://foops.linkeddata.es/FAIR_validator.html`) — el mismo servicio que este proyecto ya intentó usar para la evaluación FAIR de CAO_CRM. Para solicitarlo: hacer *fork* de [github.com/perma-id/w3id.org](https://github.com/perma-id/w3id.org), añadir una carpeta con un `.htaccess` (reglas de redirección/negociación) y un `README.md`, y enviar un Pull Request.
- **[purl.org](https://purl.org/)** — alternativa más antigua, hoy gestionada por Internet Archive (desde 2016, cuando OCLC se lo cedió). Confirmé que sigue operativo. Menos usado hoy en el mundo de ontologías que w3id, pero también válido.
- **GitHub/GitLab Pages con dominio propio** — sirve los archivos estáticos (HTML, `.rdf`, `.ttl`, `.jsonld`), pero **no permite negociación de contenido real** (no soporta `.htaccess`, solo sirve archivos por extensión). Por eso el patrón habitual en la comunidad es **combinar los dos**: w3id.org resuelve la redirección 303 según el `Accept` del cliente, y detrás de esa redirección vive el sitio estático en GitHub/GitLab Pages con el contenido real.

**Aplicado a CAO_CRM concretamente:** dado que el repositorio vive en el GitLab de Huma-Num, vale la pena primero preguntar si Huma-Num ofrece alojamiento web con dominio propio para proyectos del consorcio (varios proyectos CNRS/Ariane sí lo tienen) — si no, la ruta w3id + Pages es la más barata y estándar, y ya tiene un precedente directo dentro del propio ecosistema de este proyecto (FOOPS! la usa).

---

## 2. Registrar CAO_CRM en catálogos de ontologías — para que se pueda *encontrar*

Un catálogo es lo que hace que alguien que no conoce este proyecto pueda toparse con CAO_CRM buscando "ontología corpus literario" o "extensión de CIDOC-CRM".

- **[LOV — Linked Open Vocabularies](https://lov.linkeddata.es/)**: existe un formulario de sugerencia activo (verificado en vivo). **No acepta automáticamente cualquier envío** — exige justamente lo que trata este informe: URIs estables y resolubles, disponibilidad web real, formatos estándar, metadatos de calidad, autoría identificable y política de versionado. Es decir: **este punto solo es viable después de resolver el punto 1**, no antes.
- **BioPortal**: estrictamente biomédico, no aplica. Existen otras instancias hermanas bajo la [OntoPortal Alliance](https://ontoportal.org/about/) (AgroPortal, EcoPortal, MatPortal...), pero la investigación no encontró ninguna específica de patrimonio cultural/humanidades digitales — no hay, hoy, un catálogo "natural" de ese tipo al que sumar CAO_CRM.
- **El propio consorcio CIDOC-CRM (CRM-SIG)**: es, con diferencia, el catálogo más pertinente, porque CAO_CRM compone directamente CIDOC-CRM/LRMoo/CRMdig. Existe un proceso de dos niveles: primero como **"Compatible Ontology"** (listada, pero mantenida externamente — el sitio del CRM-SIG solo enlaza), y si hay colaboración sostenida en el tiempo, puede evolucionar a **"Harmonized Extension"** (alojada bajo el propio `cidoc-crm.org`). El sitio del CRM-SIG devolvió error 500 varias veces durante la investigación de hoy (parece una caída temporal del servidor, no que el sitio haya desaparecido — hay una copia archivada accesible en Wayback Machine) — recomendable reintentar en unos días y, en paralelo, contactar directamente a la lista de correo del CRM-SIG (`crm-sig@ics.forth.gr`, confirmada activa).

---

## 3. DOI y archivado permanente — para que se pueda *citar*

Un DOI es lo que permite que el próximo artículo académico del equipo (o de terceros) cite "CAO_CRM v2.0" de forma estable, con un enlace que nunca se rompe, en vez de citar "un archivo en un repositorio Git que puede moverse o desaparecer".

**Ruta estándar:** [integración GitHub–Zenodo](https://help.zenodo.org/docs/github/) — se activa el repositorio en Zenodo, y cada *release* de GitHub genera automáticamente un registro con DOI propio. Como este repositorio vive en GitLab (no GitHub), hay dos caminos: (a) espejar o mover el repositorio a GitHub para aprovechar la integración automática, o (b) subir manualmente cada versión a Zenodo (Zenodo también acepta subida directa de archivos, sin necesidad de GitHub).

En cualquiera de los dos casos, conviene añadir un **[`CITATION.cff`](https://citation-file-format.github.io/)** en la raíz del repositorio — es el formato que Zenodo (y GitHub) leen automáticamente para completar título, versión, licencia, autores con su ORCID y afiliación. Esto es, en la práctica, trabajo menor: `ADR-003-autoria-y-procedencia.md` ya documenta con precisión quién es autor de qué (el modelo conceptual de Mélanie Bouland, la codificación RDF/OWL de Andrés Echavarría, los contribuyentes) — solo falta trasladar esa misma información, ya decidida, al formato `CITATION.cff`.

---

## 4. Principios FAIR — un checklist ya operacional, verificado en vivo

Existe una checklist concreta (no genérica) específicamente para vocabularios/ontologías, documentada en Garijo & Poveda-Villalón, *"Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web"* ([arXiv:2003.13084](https://arxiv.org/abs/2003.13084)), y convertida en herramienta automática por el propio servicio **FOOPS!**, confirmado accesible hoy en `https://foops.linkeddata.es/FAIR_validator.html` (acepta subir un archivo directamente, sin necesidad de que la URI ya resuelva en la web — así que **este chequeo se puede correr desde ya**, sin esperar a resolver el punto 1). Evalúa 24 verificaciones agrupadas en Findable/Accessible/Interoperable/Reusable: resolución real de la URI, metadatos Dublin Core/DCAT mínimos, licencia declarada dentro del propio RDF (no solo en un README), `versionIRI` presente, presencia en registros como LOV, disponibilidad en varios formatos de serialización, y documentación humana enlazada desde la propia URI.

**Nota importante para no repetir un error ya cometido en este proyecto:** el intento anterior de usar FOOPS! (documentado en `validation/08-fair/README.md`) fracasó porque se buscó el endpoint equivocado — ahora se confirma que el endpoint real y funcional es `https://foops.linkeddata.es/FAIR_validator.html`, y que además existe un identificador w3id (`https://w3id.org/foops/`) apuntando ahí. Vale la pena actualizar `validation/08-fair/` con esta URL verificada y quitar el bloqueo que arrastra ese punto desde hace meses.

---

## 5. Metadatos para que buscadores y agregadores encuentren la ontología

- **[VoID](https://www.w3.org/TR/void/)** (*Vocabulary of Interlinked Datasets*): una descripción — enlazada desde la propia URI base — de cuántas clases/propiedades tiene el dataset, su licencia, su punto de acceso. Es lo que permite a un programa "seguir el rastro" (*follow-your-nose*) desde la URI hasta entender qué es todo el conjunto.
- **Marcado `schema.org/Dataset`** (JSON-LD) en la página de aterrizaje — es, específicamente, lo que **[Google Dataset Search](https://developers.google.com/search/docs/appearance/structured-data/dataset)** necesita para indexar la ontología. Sin este marcado, Google Dataset Search no la mostrará aunque el HTML ya exista y sea perfecto.
- Un sitemap XML apuntando a la página de aterrizaje y, si se quiere ir más allá, a cada término individual.
- El propio registro en LOV (punto 2) funciona también como canal de descubribilidad, porque LOV expone su catálogo consultable vía SPARQL.

---

## 6. Qué debe contener, como mínimo, la página de aterrizaje ("landing page")

Según el documento de referencia clásico del W3C, [Best Practice Recipes for Publishing RDF Vocabularies](https://www.w3.org/TR/swbp-vocab-pub/) (sigue siendo la fuente citada por trabajos posteriores, aunque no se ha actualizado formalmente desde 2008): la URI del vocabulario debe resolver, vía GET, a una descripción RDF "autoritativa", sin ambigüedad sobre si esa URI identifica una clase, una propiedad o el vocabulario entero, con negociación HTML/RDF y redirecciones 303 consistentes.

**La buena noticia para CAO_CRM: casi todo esto ya existe**, generado por Widoco (`docs/site/index-{en,fr,es}.html`) — tabla de clases/propiedades con enlaces, licencia visible, ejemplos, contacto, estado de mantenimiento. **Lo único que falta no es contenido, es publicarlo en una URI que de verdad resuelva** (punto 1) — el trabajo de redacción y generación ya está hecho.

---

## 7. Mantenimiento y sostenibilidad — el punto que ningún archivo `.rdf` puede resolver por sí solo

No hay un estándar único, pero la convergencia entre OBO Foundry, LOV y las guías FAIR-para-ontologías pide, de forma consistente:

- **Política de versionado explícita** — el [Principio 4 de OBO Foundry sobre versionado](http://obofoundry.org/principles/fp-004-versioning.html) recomienda un `versionIRI` con fecha o semver, y prohíbe modificar un release ya publicado (las correcciones van en un release nuevo, nunca sobre uno existente). CAO_CRM ya tiene `owl:versionIRI` — falta documentar explícitamente la política ("nunca se edita `2.0` una vez publicada, la siguiente corrección es `2.1`").
- **Canal de reporte de problemas** público y activo, enlazado desde la propia página de aterrizaje (el *issue tracker* de GitLab ya sirve para esto, solo falta enlazarlo visiblemente).
- **Declaración de compromiso de mantenimiento a largo plazo** — quién es responsable de CAO_CRM una vez termine la financiación de AMIS/OSCARS. Este es, en la práctica, el punto más delicado: LOV específicamente penaliza la falta de un "publicador identificable y confiable a largo plazo", y es exactamente el riesgo que corren los proyectos financiados con fecha de fin fija. Vale la pena que el Consorcio Ariane decida, explícitamente, quién mantiene esto después de AMIS.

---

## 8. Plan de acción, priorizado

No todo depende de lo mismo — así es como se desbloquea cada cosa:

| Orden | Acción | Depende de | Bloqueador |
|---|---|---|---|
| 1 | Correr FOOPS! ya mismo contra el `.rdf` actual (`https://foops.linkeddata.es/FAIR_validator.html`) | Nada — se puede hacer hoy | Ninguno |
| 2 | Escribir `CITATION.cff` a partir de lo ya decidido en ADR-003 | Nada — es solo trasladar información ya existente | Ninguno |
| 3 | Documentar explícitamente la política de versionado | Nada | Ninguno |
| 4 | Decidir si Huma-Num ofrece hosting con dominio propio, o si se usa w3id + Pages | Respuesta de Huma-Num | Depende de un tercero |
| 5 | Solicitar el identificador en w3id.org (PR a `perma-id/w3id.org`) | Punto 4 resuelto | — |
| 6 | Publicar el sitio estático (Widoco ya genera casi todo el contenido) | Punto 5 | — |
| 7 | Añadir VoID + `schema.org/Dataset` a la landing page | Punto 6 | — |
| 8 | Solicitar inclusión en LOV | Puntos 5-7 resueltos | — |
| 9 | Contactar al CRM-SIG para registrar CAO_CRM como "Compatible Ontology" | Nada técnico, solo redactar el contacto — el sitio del CRM-SIG está caído ahora mismo (error 500), reintentar en unos días | Temporalmente bloqueado (externo) |
| 10 | DOI en Zenodo | Decidir si se espeja a GitHub, o subida manual | Decisión del equipo |
| 11 | Declaración de mantenimiento a largo plazo tras AMIS | Decisión del Consorcio Ariane, no técnica | Decisión externa a este equipo |

**Los tres primeros pasos no dependen de nada — se pueden hacer esta misma semana, sin esperar ninguna decisión de modelado ni ninguna respuesta externa.**

---

## Fuentes citadas

- [Cool URIs for the Semantic Web](https://www.w3.org/TR/cooluris/) — W3C Interest Group Note.
- [Best Practice Recipes for Publishing RDF Vocabularies](https://www.w3.org/TR/swbp-vocab-pub/) — W3C Working Group Note.
- [w3id.org](https://w3id.org/) y su repositorio de solicitudes, [github.com/perma-id/w3id.org](https://github.com/perma-id/w3id.org).
- [purl.org](https://purl.org/) — servicio gestionado por Internet Archive.
- [LOV — Linked Open Vocabularies](https://lov.linkeddata.es/), formulario de sugerencia y página "About".
- [OntoPortal Alliance](https://ontoportal.org/about/).
- Consorcio CIDOC-CRM, página de extensiones (`cidoc-crm.org/Issue/ID-161-extensions-of-the-crm`, verificar cuando el sitio se recupere del error 500 actual).
- [Zenodo — integración con GitHub](https://help.zenodo.org/docs/github/) y [guía de `CITATION.cff`](https://help.zenodo.org/docs/github/describe-software/citation-file/).
- [citation-file-format.github.io](https://citation-file-format.github.io/).
- Garijo & Poveda-Villalón, ["Best Practices for Implementing FAIR Vocabularies and Ontologies on the Web"](https://arxiv.org/abs/2003.13084) (arXiv:2003.13084).
- **FOOPS!**, endpoint verificado hoy: `https://foops.linkeddata.es/FAIR_validator.html` (y su alias `https://w3id.org/foops/`).
- [W3C VoID](https://www.w3.org/TR/void/).
- [Google Dataset Search — structured data requirements](https://developers.google.com/search/docs/appearance/structured-data/dataset).
- [OBO Foundry, Principio 4 — Versionado](http://obofoundry.org/principles/fp-004-versioning.html).
