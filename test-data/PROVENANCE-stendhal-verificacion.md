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

# Verificación de datos reales — Stendhal, *Le Rouge et le Noir* (para test-data de CAO_CRM)

**Fecha:** 2026-07-10. **Investigación inicial:** agente con modelo Haiku (WebSearch/WebFetch).
**Verificación cruzada:** sesión principal (Sonnet), spot-check de los identificadores más
sensibles antes de usarlos en `test-data/stendhal-le-rouge-et-le-noir.ttl`.

## Por qué existe este archivo

El ejemplo de *Le Rouge et le Noir* ya estaba presente en el proyecto (página "exemple" del
diagrama `CRM_V8.json`, y en los propios `rdfs:comment` de las subpropiedades `P14_has_*` del
módulo RDF). Para escribir datos de instancia (ABox) reales — no sintéticos — que ejerzan de verdad
las categorías de validación `shacl` y `cq`, se investigaron los hechos bibliográficos reales de
esta obra y de la edición crítica de Henri Martineau (Le Divan, 1927) ya mencionada en el propio
módulo.

## Verificación cruzada realizada por la sesión principal

Los identificadores ARK de Gallica reportados por el agente Haiku no pudieron confirmarse por
`curl`/`WebFetch` directos (Gallica devuelve HTTP 403 ante tráfico no-navegador — protección
anti-bot conocida del dominio `gallica.bnf.fr`, no evidencia de que el recurso no exista). Se
verificaron en su lugar por búsqueda cruzada: el título exacto de la página de Gallica para
`ark:/12148/bpt6k6212441w` aparece indexado en Google como *"Le rouge et le noir : chronique du
dix-neuvième siècle. 1 / Stendhal ; [révision du texte et préf. par Henri Martineau] | Gallica"* —
coincide exactamente con lo reportado por el agente. El ARK del catálogo general de la BnF
(`ark:/12148/cb11987967z`) sí devolvió HTTP 200 directamente.

## Resumen de los datos usados en `test-data/stendhal-le-rouge-et-le-noir.ttl`

| Dato | Valor usado | Fuente | Confianza |
|---|---|---|---|
| Autor | Stendhal (Marie-Henri Beyle), 1783-01-23 / 1842-03-23 | Wikipedia EN/FR, Britannica | Alta (hecho ampliamente documentado) |
| Concepción de la obra | Octubre de 1829 – mayo de 1830 | Wikipedia FR, BnF Essentiels | Media-alta (fuentes secundarias consistentes entre sí) |
| Primera publicación (expresión) | 13 de noviembre de 1830, Levasseur, París | Wikipedia EN/FR | Alta |
| Edición Martineau/Le Divan | 1927, 2 tomos, 2525 ejemplares (25 + 2500) | Wikisource (prefacio de la propia edición) | Alta (fuente primaria: el propio prefacio digitalizado) |
| Henri Martineau | 1882-04-26 / 1958-04-21 | Wikipedia FR, BnF Catalogue, Babelio | Alta |
| Le Divan (editorial) | París, activa 1921-1958 | Open Library, Wikidata, Hotel Moderniste | Media (fuentes secundarias, sin verificación primaria adicional) |
| ARK BnF (obra) | `ark:/12148/cb11987967z` | BnF Catalogue — **HTTP 200 verificado directamente** | Alta |
| ARK Gallica Tomo I | `ark:/12148/bpt6k6212441w` | Gallica — **verificado por título indexado en búsqueda cruzada**, no por fetch directo (403 anti-bot) | Media-alta |
| ARK Gallica Tomo II | `ark:/12148/bpt6k69039` | Gallica — mismo método, no verificado por fetch directo | Media (no se hizo la búsqueda cruzada específica para este segundo ARK; usar con la misma cautela) |
| Dominio público | Vigente desde 1912 en la UE (70 años tras 1842) | Cálculo directo + política de Gallica | Alta |
| Signatura/cota exacta del ejemplar físico en BnF | No encontrada | — | Ninguna: se documenta explícitamente como no verificada en el propio `P3_has_note` del `F5_Item` |

## Limitación reconocida explícitamente

No se verificó independientemente el ARK de Gallica del Tomo II
(`ark:/12148/bpt6k69039`) con el mismo rigor que el del Tomo I — no se incluyó en el grafo de
instancia por esta razón (el grafo solo usa el Tomo I). Si se quiere ampliar el ejemplo al Tomo II,
repetir la verificación cruzada antes de darlo por bueno.
