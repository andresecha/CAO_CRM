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

# `docs/prompts/` — instrucciones para retomar cada revisión pendiente

Tres trabajos del proyecto están detenidos a la espera de que un colega devuelva una revisión.
Pueden llegar en cualquier orden, con meses de diferencia, y cada uno se retoma en una sesión
nueva que no recordará nada de las anteriores. Este directorio contiene, para cada uno, un
documento autosuficiente: qué se recibe, dónde va, qué hay que tocar, cómo se verifica, qué se
deposita y qué no se debe hacer nunca.

| Archivo | Se activa cuando | Quién revisa | Qué desbloquea |
|---|---|---|---|
| [`RETOMAR-ro-revision-chrome.md`](RETOMAR-ro-revision-chrome.md) | Roxana Patras devuelve `review-chrome-ro.md` | Roxana Patras | Publicar la documentación rumana ya generada, y su dataset Nakala (10) |
| [`RETOMAR-it-publicacion.md`](RETOMAR-it-publicacion.md) | Simone Rebora devuelve `review-it.md` | Simone Rebora | Incorporar el italiano al build, generar su documentación, publicar los datasets 07 y 11 |
| [`RETOMAR-pt-publicacion.md`](RETOMAR-pt-publicacion.md) | Ana Salgado confirma su participación **y** devuelve `review-pt.md` | Ana Salgado (participación **no confirmada**) | Incorporar el portugués al build, generar su documentación, publicar los datasets 08 y 12 |

**Los tres son independientes entre sí.** Ninguno supone que otro se haya ejecutado antes, y los
números de dataset de Nakala están fijados **por idioma y no por orden de llegada** (italiano → 11,
portugués → 12), precisamente para que el que llegue primero no condicione al otro.

## Cómo se usan

Abrir el archivo que corresponda y dárselo entero a Claude como primer mensaje de una sesión nueva,
lanzada desde el directorio que el propio archivo indica en su primera sección. Están escritos para
leerse sin ningún contexto previo: cada uno repite los datos que necesita (rutas, DOI, nombres,
comandos, invariantes) en vez de remitir a los otros dos.

## Reglas que valen para los tres

Están repetidas dentro de cada archivo, porque cada uno tiene que poder leerse solo, pero conviene
tenerlas presentes también aquí:

1. **Nunca se hace `git push`.** Los commits son locales; empujar es decisión de Andrés.
2. **Ningún commit lleva atribución a Claude**: sin `Co-Authored-By`, sin `Claude-Session`.
3. **No se commitea contenido sin revisar.** Es la regla que mantiene todo esto detenido; romperla
   para "ir avanzando" anula el sentido del proceso entero.
4. **No se toca el espejo GitLab** (`~/Documentos/GitLab/cao_crm`), congelado desde el 2026-07-11.
