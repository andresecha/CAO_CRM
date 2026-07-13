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
# test-data/ — grafo de instancia real (no sintético)

`stendhal-le-rouge-et-le-noir.ttl` (124 triples) aplica los cinco niveles de CAO_CRM
(`F1_Work` → `F2_Expression` → `F3_Manifestation` → `F5_Item` → `D1_Digital_Object`) a *Le Rouge et
le Noir* de Stendhal — el mismo ejemplo ya usado en el diagrama conceptual `CRM_V8.json` ("page
exemple") y en los `rdfs:comment` de las cinco subpropiedades `P14_has_*` del propio módulo. Dos
casos reales:

1. La edición crítica francesa de Henri Martineau (Le Divan, 1927), digitalizada por la BnF en
   Gallica.
2. La traducción inglesa de C. K. Scott Moncrieff (Modern Library, 1929), digitalizada por Internet
   Archive — añadida específicamente para ejercer `P14_has_translator`.

Cada dato (fechas, identificadores ARK/Internet Archive, tirada de la edición Martineau, etc.) fue
investigado y verificado contra fuentes reales — ver `PROVENANCE-stendhal-verificacion.md` y
`PROVENANCE-stendhal-traduccion-internet-archive.md` para el detalle completo de cada fuente,
incluidas las limitaciones reconocidas explícitamente (p. ej. el ARK de Gallica del Tomo II no se
verificó con el mismo rigor que el del Tomo I y por eso no se usó en el grafo).

Este grafo es el que ejercen realmente las categorías `shacl` (`../validation/03-shacl/`) y `cq`
(`../competency-questions/`, `../sparql/`) — ver `make shacl` y `make cq`.
