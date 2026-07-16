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
# graph/ — grafo interactivo del modelo CAO_CRM

**Qué es:** una visualización de red navegable del módulo `ontology/CAO_CRM-1.0.rdf` (el archivo final —
ver sección 1 del `README.md` principal), generada con `pyvis` (Python) — un único archivo HTML
autocontenido, sin necesidad de instalar ni levantar un servidor de base de datos en grafo (Neo4j u
otro). Se abre directamente en cualquier navegador.

**Cómo generarlo:**
```bash
python3 -m venv .venv && source .venv/bin/activate   # si no existe ya
pip install rdflib pyvis networkx
python3 build_graph.py ../ontology/CAO_CRM-1.0.rdf CAO_CRM-1.0-graph.html
```

**Cómo leerlo:**
- **Óvalos** = clases. Color según la ontología de origen: **azul** = CIDOC-CRM, **naranja** = LRMoo,
  **morado** = CRMdig.
- **Rectángulos grises pequeños** = propiedades (de objeto y de datos).
- **Aristas grises "subClassOf"** = jerarquía de clases.
- **Aristas verdes "domain"** = de una clase hacia la propiedad que la tiene como dominio.
- **Aristas rojas "range"** = de una propiedad hacia la clase que es su rango.
- Pasar el cursor sobre cualquier nodo muestra su etiqueta en inglés y su IRI completa.
- Arrastrar, hacer zoom (rueda del ratón) y usar los botones de navegación en la esquina inferior
  izquierda para explorar.
- Sobre la cobertura de dominios y rangos dentro del módulo acotado, ver
  `../decisions/es/informe-completitud-labels-domain-range.md`.

**Nota:** este grafo visualiza únicamente la estructura de clases y propiedades del módulo (TBox);
no incluye las instancias de ejemplo del grafo de datos real que sí existe en `../test-data/`,
usado por las categorías de validación `shacl`/`cq` (ver `../test-data/README.md`) — visualizar
instancias sería una extensión posible de esta herramienta, no implementada por ahora.
