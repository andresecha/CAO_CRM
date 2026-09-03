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

# Retomar: publicación del italiano (revisión de Simone Rebora)

> Documento autosuficiente. Dárselo entero a Claude como primer mensaje de una sesión nueva.
> **Independiente del portugués:** no supone que el portugués se haya hecho antes ni después, y
> los números de dataset de Nakala están fijados por idioma, no por orden de llegada.

## 0. Dónde lanzar Claude

```
cd /home/andres/Documentos/GitHub/CAO_CRM
```

Repositorio de software (GitHub, `andresecha/CAO_CRM`), el **primario**. El trabajo toca además una
segunda carpeta, que **no es un repositorio git** y no hay que clonar ni commitear:

```
/home/andres/Documentos/GitLab/data-publication/
```

Colección de datasets preparados para depositar en Nakala, hermana del repo y fuera de él.

**No tocar** `~/Documentos/GitLab/cao_crm` (espejo institucional congelado el 2026-07-11) ni
`~/Documentos/GitLab/OLD_CAO_CRM` ni `~/Documentos/GitLab/Ontologie` (fase anterior, sin cambios
desde julio de 2026).

Entorno: `make validate` y `make docs` necesitan dependencias Python que **no** están en el Python
del sistema. En cada sesión:

```bash
export PATH="/home/andres/Documentos/GitLab/cao_crm/.venv/bin:$PATH"
```

`.tools/jena` y `.tools/robot` ya están instalados. Chrome y WeasyPrint están disponibles, así que
`make docs` produce también los PDF.

---

## 1. Situación exacta de la que se parte

El italiano existe entero desde el 2026-07-13 pero está **deliberadamente apartado**: es una
traducción asistida por IA sin revisar, no está cableada en el build y está en `.gitignore`. Lo que
hay, sin versionar:

| Archivo | Qué es |
|---|---|
| `docs/i18n/translations-it/*.yaml` | Los 130 términos en italiano, en 8 lotes temáticos |
| `docs/i18n/glossary_crosswalk-it.yaml` | Glosario puente de los conceptos ancla de CIDOC-CRM |
| `docs/i18n/CAO_CRM-1.0-i18n-it.ttl` | El overlay compilado a partir de los lotes |
| `docs/config-it.properties` | Título, resumen, descripción, estado y cita, en italiano |
| `docs/intro-it.html` | Introducción y "Stato di questo documento" |
| `documentation/it/` | Las 10 fichas pedagógicas en italiano |
| `PARAGRAPHS["it"]` en `docs/postprocess_acknowledgments.py` | Los agradecimientos en italiano (este sí está en el repo, ya versionado) |

**Diferencia capital con el rumano, que ahorra la mitad del trabajo:** Widoco 1.4.25 **sí** trae
`widoco/it.properties` y LODE **sí** trae `lode/it.xml`. Los títulos de sección, las etiquetas de
referencias cruzadas, la navegación y la leyenda salen ya en italiano de la propia herramienta. El
italiano **no necesita** nada equivalente a `docs/i18n/chrome-ro.yaml` ni a
`docs/postprocess_ro_chrome.py`, que existen solo porque para el rumano no hay paquete de idioma.
No crear un `chrome-it.yaml`.

Lo que sí comparte con el rumano: ninguno de los 130 términos tiene etiqueta oficial en italiano en
CIDOC-CRM/LRMoo/CRMdig, así que todas las etiquetas y definiciones italianas las aporta la capa de
traducción del proyecto y llevarán la daga (†) en la documentación generada.

Antes de empezar, mirar `git status` y `git log --oneline -15` para ver en qué estado está el
repositorio: puede haber trabajo rumano o portugués sin commitear, que **no hay que tocar ni
commitear junto con esto**.

---

## 2. Qué se recibe y dónde va

Simone Rebora devuelve **`review-it.md`** corregido (probablemente por correo; suele acabar en
`~/Descargas/`). Es un único documento con cuatro secciones: **A** agradecimientos, **B**
introducción / estado del documento, **C** resumen y descripción de la ontología, **D** los 130
términos uno a uno. Cada bloque muestra el inglés oficial, el francés de referencia y el italiano a
corregir bajo «PLEASE REVIEW / CORRECT BELOW».

Archivarlo en `docs/i18n/review/review-it.md` (sobrescribiendo el enviado). Ese directorio está en
`.gitignore` a propósito: es material de trabajo, no un artefacto publicado.

Comprobar primero que es de verdad la revisión devuelta y no la copia que se envió —ya ocurrió una
vez que el archivo entregado era, byte a byte, el mismo que ya estaba archivado—:

```bash
cmp -s ~/Descargas/review-it.md docs/i18n/review/review-it.md \
  && echo "IDÉNTICO al enviado: NO trae correcciones, preguntar a Andrés" \
  || echo "difiere del enviado: tiene correcciones, seguir"
```

Si es idéntico, **parar y decírselo a Andrés**.

---

## 3. Incorporar las correcciones: las cuatro secciones y sus destinos

Está documentado en `docs/i18n/README.md`, sección *Where a review lands*:

| Sección del documento | Destino real |
|---|---|
| A. Acknowledgments | `PARAGRAPHS["it"]` en `docs/postprocess_acknowledgments.py` |
| B. Introduction / Stato di questo documento | `docs/intro-it.html` |
| C. Abstract & description | `abstract=` / `description=` (y `status=` si lo corrigió) en `docs/config-it.properties` |
| D. Term-by-term glossary | `label` / `comment` en `docs/i18n/translations-it/*.yaml` |

Reglas al trasladar:

- **Solo se toca el italiano.** El inglés y el francés de cada bloque son referencia y no se editan.
- Si una etiqueta de la sección D cambió, revisar si su concepto está en
  `docs/i18n/glossary_crosswalk-it.yaml`: si la revisión impuso otra palabra para un concepto ancla,
  actualizar también esa entrada y marcarla **`source: native_review`**, que es la convención del
  proyecto para distinguir lo que fijó el hablante nativo de lo que decidió el equipo (así se hizo
  con las 6 entradas que fijó la revisión rumana). Si no se hace, `check_consistency.py` reportará
  deriva en la siguiente ejecución.
- Si Simone dejó una nota tipo `[NOT SURE]` o una duda, **no resolverla por cuenta propia**:
  recogerla y preguntársela a Andrés al final, dejando entretanto la propuesta actual.
- `config-it.properties` es un `.properties` de Java: los acentos pueden ir en UTF-8 literal, pero
  respetar la convención que ya usen los demás `config-*.properties` del proyecto.

Recompilar el overlay y pasar el control de coherencia:

```bash
cd docs/i18n
python3 scripts/compile_i18n_overlay.py translations-it CAO_CRM-1.0-i18n-it.ttl it
python3 scripts/check_consistency.py translations-it glossary_crosswalk-it.yaml term_inventory.json
cd ../..
```

`check_consistency.py` es heurístico: leer su salida, no tratarla como una barrera automática.

Comprobación de que no se perdió nada por el camino — el round-trip que recomienda el propio
`docs/i18n/README.md`: regenerar el documento de revisión desde el estado ya corregido y comparar
con el que devolvió Simone. Deben coincidir en la parte italiana.

```bash
python3 docs/i18n/scripts/build_review_doc.py it /tmp/roundtrip-it.md
```

---

## 4. Cablear el italiano en el build

Cinco puntos en tres archivos. Todos son necesarios; olvidar uno da una página a medio hacer.

### 4.1 `docs/build.sh`

1. **La lista de idiomas** (busca `LANGS=`): `LANGS="en fr es ro it"`. Todo lo que viene después
   —prefijos de código, bibliografía, agradecimientos, portada, dagas i18n, PDF, landing page—
   itera sobre esta lista, así que el idioma se declara aquí una sola vez.
2. **El overlay propio.** Dentro del bucle `for lang in $LANGS` hay un bloque `if [ "$lang" = ro ]`
   que funde el overlay rumano en una copia temporal del RDF, aparte de la fusión fr/es. El italiano
   necesita lo mismo, por la misma razón: que las pasadas en/fr/es sigan recibiendo exactamente la
   misma entrada que recibían antes, de modo que añadir un idioma no pueda perturbar las páginas ya
   publicadas. Extender ese bloque (o añadir uno paralelo) para `it`, con
   `i18n/CAO_CRM-1.0-i18n-it.ttl`, `config-it.properties` e `intro-it.html`, incluida la guarda que
   salta la pasada si falta alguno de los tres.
3. **La selección de overlay del marcador de dagas.** Más abajo hay
   `[ "$lang" = ro ] && overlay="i18n/CAO_CRM-1.0-i18n-ro.ttl"`. Añadir la línea equivalente para
   `it`; si no, el italiano se compararía contra el overlay fr/es y no marcaría ninguna daga.
4. **La landing page.** En el bloque `cat > site/index.html`, añadir la entrada italiana
   (`🇮🇹 Italiano`, enlace a `index-it.html`) con su `<p class="subtitle">`, que es la misma frase
   del subtítulo de portada del punto 4.2: las dos copias no pueden divergir.

### 4.2 Los diccionarios por idioma

| Archivo | Clave a añadir | De dónde sale |
|---|---|---|
| `docs/postprocess_titlepage.py` | `SUBTITLES["it"]` | La traducción italiana de la frase que ya está en `SUBTITLES["en"]`. Si la sección C de la revisión la incluía, usar la versión corregida; si no, decírselo a Andrés antes de inventarla |
| `docs/postprocess_i18n_marker.py` | `TOOLTIP["it"]` | El texto del tooltip de la daga, en italiano, siguiendo el de las otras lenguas |
| `docs/postprocess_acknowledgments.py` | `ANCHORS["it"]` | **Ver 4.3: no se adivina, se observa** |

### 4.3 `ANCHORS["it"]`: hay que observarlo, no deducirlo

`postprocess_acknowledgments.py` inserta los agradecimientos del proyecto justo antes del párrafo
fijo de créditos que escribe Widoco (el que agradece a los autores de LODE y Widoco), y localiza ese
punto por sus primeras palabras. Como Widoco **sí** trae paquete italiano, ese párrafo saldrá
traducido al italiano por la propia herramienta, y su redacción exacta **nunca se ha observado en
este proyecto**. El comentario del propio script lo advierte: copiarla de una página realmente
generada, no adivinarla.

Procedimiento exacto:

1. Hacer los cambios de 4.1 y las dos primeras filas de 4.2.
2. Ejecutar `make docs`. Abortará —`build.sh` corre con `set -euo pipefail`— con
   `postprocess_acknowledgments.py: unknown language 'it'`. **Es lo esperado**: para entonces
   Widoco ya ha escrito `docs/site/index-it.html` en disco.
3. Sacar de ahí las primeras palabras del párrafo:

   ```bash
   grep -o '<p>[^<]\{0,80\}' docs/site/index-it.html | grep -iE 'autor|ringrazia|LODE' | head -3
   ```

   Buscar el párrafo que menciona a Silvio Peroni / LODE / Daniel Garijo / Widoco y copiar
   literalmente sus primeras palabras (unas seis o siete, suficientes para ser inequívocas).
4. Añadir `ANCHORS["it"]` con ese texto exacto y volver a ejecutar `make docs` entero.

Como el build abortado deja `site/` a medio procesar, la comprobación del invariante del punto 6
solo vale después de una ejecución **completa y correcta**.

### 4.4 `.gitignore`

Quitar del bloque «Italian and Portuguese» las cinco entradas italianas, que dejan de ser trabajo
apartado y pasan a ser contenido publicado:

```
docs/intro-it.html
docs/config-it.properties
docs/i18n/translations-it/
docs/i18n/glossary_crosswalk-it.yaml
docs/i18n/CAO_CRM-1.0-i18n-it.ttl
```

**`documentation/it/` se queda ignorado.** Las 10 fichas pedagógicas italianas **no** forman parte
de `review-it.md` —que cubre solo las secciones A-D— y siguen siendo un borrador asistido por IA sin
revisar. Es exactamente el mismo criterio que se aplicó a `documentation/ro/`. Reescribir el
comentario del bloque para que quede claro qué sigue apartado y por qué, y dejar las entradas
portuguesas intactas.

---

## 5. Regenerar

```bash
cd /home/andres/Documentos/GitHub/CAO_CRM
export PATH="/home/andres/Documentos/GitLab/cao_crm/.venv/bin:$PATH"
make docs
```

Debe terminar con `Documentation built -> docs/site/index.html (landing) + index-{en,fr,es,ro,it}.html`
y cinco PDF generados.

---

## 6. Verificación (no saltarse ninguna)

### 6.1 Las otras cuatro lenguas no se movieron

Es el invariante del proyecto: añadir un idioma **no puede** alterar los ya publicados.

```bash
git diff --stat docs/site/index-en.html docs/site/index-fr.html docs/site/index-es.html docs/site/index-ro.html
```

Debe salir **vacío** (si el rumano aún estuviera sin commitear, compararlo contra la copia previa en
vez de contra HEAD). Si algo se movió, el cableado del punto 4 está tocando archivos que no le
corresponden.

Los PDF de esas lenguas cambian de bytes en cada build (fecha de creación incrustada) pero su
**texto** debe ser idéntico; si lo es, revertirlos para dejar el diff limpio:

```bash
for l in en es fr ro; do git show HEAD:docs/site/CAO_CRM-1.0-$l.pdf > /tmp/o-$l.pdf 2>/dev/null || continue
  pdftotext -q /tmp/o-$l.pdf /tmp/o-$l.txt; pdftotext -q docs/site/CAO_CRM-1.0-$l.pdf /tmp/n-$l.txt
  printf "%s: " $l; cmp -s /tmp/o-$l.txt /tmp/n-$l.txt && echo IDÉNTICO || echo DIFIERE; done
```

### 6.2 La página italiana está realmente en italiano

Widoco debería haber puesto la interfaz en italiano por su cuenta. Confirmarlo en vez de suponerlo:

```bash
grep -c 'Language file not found for it' /tmp/make-docs.log 2>/dev/null   # 0 esperado (guardar la salida si hace falta)
python3 -c "
from bs4 import BeautifulSoup
s=BeautifulSoup(open('docs/site/index-it.html',encoding='utf-8').read(),'html.parser')
print('Títulos:', [' '.join(h.get_text().split())[:45] for h in s.find_all(['h2','h4'])[:10]])
print('Etiquetas de referencia cruzada:', sorted({dt.get_text().strip() for dl in s.select('dl.description') for dt in dl.find_all('dt')}))"
```

Los títulos deben leerse en italiano (*Sommario*, *Panoramica*, *Classi*, *Proprietà*…) y las
etiquetas de referencia cruzada también. **Si salieran en inglés**, significa que el paquete de
idioma no se cargó: pararse a averiguar por qué y decírselo a Andrés — no improvisar un
post-proceso al estilo del rumano sin hablarlo antes.

Comprobar además que las dagas se aplicaron: la salida de `make docs` debe decir
`postprocess_i18n_marker.py: marked 130 entities in site/index-it.html` (130, porque ningún término
tiene etiqueta oficial en italiano).

### 6.3 La página y el PDF se ven bien

```bash
pdftoppm -png -r 50 -f 1 -l 1 docs/site/CAO_CRM-1.0-it.pdf /tmp/cover-it
xdg-open docs/site/index-it.html
```

Mirar de verdad: portada (título, subtítulo italiano, autor, logo ARIANE), índice, una ficha de
término, la leyenda, los agradecimientos y la página de procedencia.

### 6.4 Cadena de validación y marca de agua

```bash
make validate
```

Las 8 categorías más `cq` deben pasar, incluida `watermark`: todo archivo `.md`/`.sh`/`.py`/`.rq`/
`.ttl`/`.nt`/`.rdf`/`.owx` debe llevar su cabecera de copyright. Los archivos italianos que dejan
de estar ignorados pasan ahora a ser revisados por ese control — si falta alguna cabecera,
`make watermark-fix` la inserta.

`make docs` reserializa `ontology/CAO_CRM-1.0.nt` y `.jsonld` en cada ejecución y rdflib no garantiza
el orden, así que aparecerán modificados sin haber cambiado. Comprobarlo y revertirlos:

```bash
python3 - <<'EOF'
import subprocess, rdflib
for f,fmt in (("ontology/CAO_CRM-1.0.nt","nt"),("ontology/CAO_CRM-1.0.jsonld","json-ld")):
    old=subprocess.run(["git","show",f"HEAD:{f}"],capture_output=True,text=True).stdout
    print(f, "isomorfa=", rdflib.Graph().parse(data=old,format=fmt).isomorphic(rdflib.Graph().parse(f,format=fmt)))
EOF
git checkout -- ontology/CAO_CRM-1.0.nt ontology/CAO_CRM-1.0.jsonld   # solo si isomorfa=True
```

---

## 7. Actualizar la documentación del repositorio

- **`docs/i18n/README.md`** — la entrada `translations-it/` está en la línea de «Italian and
  Portuguese drafts, not yet reviewed, not wired into `docs/build.sh`, gitignored». El italiano sale
  de ahí: darle su propia entrada, con la fecha de la revisión, el alcance (cuántas etiquetas y
  definiciones corrigió) y el crédito a Simone Rebora con su enlace.
- **`docs/README.md`** — la sección *Multi-language build* dice «en/fr/es/ro, four separate files»:
  pasan a ser cinco. Añadir la pasada `-lang it` a la lista numerada y una nota que deje dicho que
  el italiano, a diferencia del rumano, no necesita post-proceso de interfaz porque Widoco y LODE sí
  traen su paquete de idioma. Ajustar también las menciones a `index-{en,fr,es,ro}.html` y a los PDF.
- **`README.md`** (raíz, en francés) — la arborescencia del repositorio, las menciones a
  `config-{en,es,fr,ro}.properties`, `intro{-en,-es,-ro,}.html`, `translations-ro/`, y la fila de
  badges `Docs-FR / Docs-ES / Docs-EN`, a la que conviene añadir `Docs-IT` enlazando a
  <https://www.cao-crm.eu/index-it.html>. Añadir la nota de que las correcciones del italiano las
  hizo Simone Rebora, con su enlace.

El enlace de Simone Rebora es el que ya usa el proyecto en las documentaciones públicas
(`docs/postprocess_people_links.py`): **<https://www.dlls.univr.it/?ent=persona&id=19903>**
(Verona University, Verona, Italia).

---

## 8. Commit

**Reglas absolutas:**

- **Nunca `git push`.** Los commits son locales; empujar es decisión de Andrés.
- **Ningún commit lleva atribución a Claude**: sin `Co-Authored-By`, sin `Claude-Session`, sin
  ninguna otra mención. Es una publicación científica firmada con autoría única declarada en el
  propio RDF (`dc:creator`) y DOI Nakala.
- Mensajes en español, descriptivos, explicando **por qué** además de qué; mirar `git log` antes de
  escribir el primero.
- Un commit por asunto (incorporación de la revisión / cableado del idioma / regeneración de la
  documentación / actualización de los README), no uno gigante.
- **No commitear de paso trabajo pendiente de otro idioma** que estuviera en el árbol sin commitear.

```bash
git log -8 --format='%an <%ae>%n  %s'
git log -8 --format='%B' | grep -iE 'claude|co-authored|anthropic' || echo "sin atribución: correcto"
```

---

## 9. Nakala: qué se deposita y qué se actualiza

En `/home/andres/Documentos/GitLab/data-publication/`, que **no es un repositorio git**: los
archivos se dejan en disco listos para que Andrés los suba. Cada carpeta lleva su
`METADATA-nakala.md`, ficha completa para transcribir al formulario de Nakala o usar como payload de
su API.

### 9.1 Dataset 07 — capa de traducción italiana (ya existe, privado)

`07-capa-traduccion-i18n-it/`, pre-depósito privado con DOI **`10.34847/NKL.DAA5AO51`**.

Su carga útil es la anterior a la revisión: **refrescarla** desde el repositorio y verificarlo.

```bash
D=/home/andres/Documentos/GitLab/data-publication/07-capa-traduccion-i18n-it
G=/home/andres/Documentos/GitHub/CAO_CRM/docs/i18n
cp $G/CAO_CRM-1.0-i18n-it.ttl $G/glossary_crosswalk-it.yaml $G/term_inventory.json $D/
cp $G/translations-it/*.yaml $D/translations/
for f in CAO_CRM-1.0-i18n-it.ttl glossary_crosswalk-it.yaml term_inventory.json; do
  cmp -s $D/$f $G/$f && echo "OK $f" || echo "FALLO $f"; done
for f in $D/translations/*.yaml; do cmp -s "$f" "$G/translations-it/$(basename $f)" \
  && echo "OK $(basename $f)" || echo "FALLO $(basename $f)"; done
```

(No tocar `CAO_CRM-1.0-i18n-fr-referencia.ttl`: es el overlay francés de referencia, idéntico al del
dataset 09, y no cambia.)

Después, reescribir su `METADATA-nakala.md`. Tomar como modelo el del dataset 06
(`06-capa-traduccion-i18n-ro/METADATA-nakala.md`), que ya pasó por exactamente esta transición:

- Sustituir el bloque **ESTADO: PRE-DEPÓSITO PRIVADO — NO HACER PÚBLICO TODAVÍA** por el estado real
  (revisión completada, listo para publicar), incluyendo la acción pendiente: sustituir la carga
  útil en Nakala y cambiar la visibilidad.
- **Simone Rebora es coautor** (`dcterms:creator` y `dcterms:rightsHolder`), con su afiliación
  (Verona University, Verona, Italia) y su enlace. Ya figura previsto en la ficha: mantenerlo.
- Rellenar `Date / created`, `dcterms:created`, `dcterms:modified`, `dcterms:dateAccepted`,
  `dcterms:available`, y quitar de `dcterms:accessRights` la advertencia de no depositar.
- `dcterms:extent`: recontar sobre el archivo real, no copiar la cifra anterior:
  ```bash
  python3 -c "
  import rdflib; from rdflib.namespace import RDFS
  g=rdflib.Graph().parse('docs/i18n/CAO_CRM-1.0-i18n-it.ttl',format='turtle')
  L=sum(1 for _,_,o in g.triples((None,RDFS.label,None)) if getattr(o,'language',None)=='it')
  C=sum(1 for _,_,o in g.triples((None,RDFS.comment,None)) if getattr(o,'language',None)=='it')
  print(f'{L} etiquetas + {C} definiciones = {len(g)} triples')"
  ```
- `dcterms:provenance`: contar el ciclo real —borrador asistido por IA, pre-depósito privado del
  2026-07-14, envío a revisión, devolución e incorporación— con el alcance cuantificado (cuántas
  etiquetas y definiciones cambió la revisión, cuántas entradas del glosario quedaron
  `source: native_review`).
- `dcterms:isReferencedBy` e `isRequiredBy`: enlazar al nuevo dataset 11 (documentación generada en
  italiano) y a <https://www.cao-crm.eu/index-it.html>.

### 9.2 Dataset 11 — documentación generada en italiano (nuevo)

**El número es 11 por ser italiano, no por orden de llegada.** El portugués es siempre el 12, llegue
antes o después. Crear:

```
/home/andres/Documentos/GitLab/data-publication/11-documentacion-generada-it/
```

Copiar el modelo completo del dataset 10 (`10-documentacion-generada-ro/`), que es exactamente el
mismo tipo de "data" para el rumano, y adaptarlo:

```bash
D=/home/andres/Documentos/GitLab/data-publication/11-documentacion-generada-it
G=/home/andres/Documentos/GitHub/CAO_CRM
mkdir -p $D/provenance $D/resources $D/logos $D/fuentes
cp $G/docs/site/index-it.html $G/docs/site/CAO_CRM-1.0-it.pdf $D/
cp $G/docs/site/provenance/provenance-it.{html,ttl} $D/provenance/
cp -r $G/docs/site/resources/. $D/resources/
cp $G/docs/site/logos/*.svg $D/logos/
cp $G/docs/config-it.properties $G/docs/intro-it.html $D/fuentes/
```

`fuentes/` lleva solo dos archivos, no tres: el italiano no tiene equivalente de `chrome-ro.yaml`.

Verificar que el conjunto es consultable tal cual se descargue:

```bash
cd $D
grep -rl '/home/andres' . || echo "sin rutas locales: correcto"
grep -o 'href="[^"]*index-it[^"]*"' provenance/provenance-it.html   # debe ser ../index-it.html
python3 -c "
from bs4 import BeautifulSoup; import os
s=BeautifulSoup(open('index-it.html',encoding='utf-8').read(),'html.parser')
refs={e.get(a).split('#')[0] for t,a in (('img','src'),('script','src'),('link','href'),('a','href'))
      for e in s.find_all(t) if e.get(a) and not e.get(a).startswith(('http','#','mailto','data:'))}
print('faltantes:', [r for r in sorted(refs) if r and not os.path.exists(r)] or 'ninguno')"
```

Las dos correcciones de ruta (logo como `data:` URI, enlace de procedencia con `../`) ya están
resueltas aguas arriba en el repositorio, así que estas comprobaciones deberían pasar sin parchear
nada. Si alguna fallara, corregirla en el repositorio y regenerar, no parchear la copia depositada.

Escribir su `METADATA-nakala.md` con la ficha del 10 como plantilla, cambiando lo que de verdad
cambia:

- **Tipo COAR** `texte` — `http://purl.org/coar/resource_type/c_18cf` (igual que el 04 y el 10).
- **Autoría:** Echavarría Peláez, Andrés Felipe ; Rebora, Simone.
- **Recuentos reales**, no copiados: número de fichas por sección y páginas del PDF.
  ```bash
  python3 -c "
  from bs4 import BeautifulSoup
  s=BeautifulSoup(open('$G/docs/site/index-it.html',encoding='utf-8').read(),'html.parser')
  for d in ('classes','objectproperties','dataproperties','annotationproperties'):
      div=s.find(id=d); print(d, len(div.select('div.entity')) if div else 0)"
  pdfinfo $G/docs/site/CAO_CRM-1.0-it.pdf | grep -i pages
  ```
- **La sección «Por qué Simone Rebora figura como coautor» hay que reescribirla, no copiarla.** El
  argumento del rumano se apoya en dos hechos acumulados —ni etiquetas oficiales ni paquete de
  idioma— y para el italiano **solo se cumple el primero**: Widoco y LODE sí traen paquete italiano,
  así que la interfaz de la página no es aportación del proyecto. El argumento correcto es que
  ninguno de los 130 términos tiene etiqueta ni definición oficial en italiano, de modo que todo el
  contenido terminológico que el lector lee es traducción del proyecto revisada por él. Afirmar lo
  otro sería falso y contradiría lo que la propia página muestra.
- Descripciones para humanos en **fr / it / en** (el 10 las tiene en fr/ro/en).
- `dcterms:language`: `it`. `dcterms:requires`: el módulo RDF (dataset 02) y la capa italiana
  (dataset 07, `10.34847/NKL.DAA5AO51`).
- Adaptar la nota final sobre rutas: decir que los archivos son copia exacta del repositorio y que
  las dos correcciones de ruta ya están resueltas aguas arriba.

### 9.3 Los dos archivos de la colección

- **`data-publication/README.md`** — la colección pasa de diez a once "data": actualizar los
  recuentos («las diez carpetas»), el párrafo sobre el estado de 06/07/08, la fila 7 de la tabla y
  añadir la fila 11.
- **`data-publication/COLLECTION-METADATA-nakala.md`** — el párrafo de estado del principio, el
  campo `Statut`, el recuento en `Licence predominante`, el título de la sección de composición, la
  fila 7 y la nueva fila 11. Cuando existan los DOI reales, sustituir los `[pendiente]` y completar
  los `dcterms:relation`/`isReferencedBy` cruzados.

---

## 10. Al terminar, decirle a Andrés

- Qué cambió la revisión, cuantificado (etiquetas, definiciones, entradas del glosario).
- Cuál resultó ser el `ANCHORS["it"]` observado en la página real.
- Si la interfaz italiana de Widoco/LODE salió correcta o hubo alguna sorpresa.
- Cualquier `[NOT SURE]` o duda que Simone dejara sin resolver.
- Que los commits están hechos **en local y sin empujar**, y cuáles son.
- Las acciones que solo puede hacer él en Nakala: sustituir la carga útil del 07 y publicarlo, y
  crear el 11.
