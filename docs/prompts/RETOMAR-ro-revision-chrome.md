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

# Retomar: revisión rumana de las cadenas de interfaz (Roxana Patras)

> Documento autosuficiente. Dárselo entero a Claude como primer mensaje de una sesión nueva.

## 0. Dónde lanzar Claude

```
cd /home/andres/Documentos/GitHub/CAO_CRM
```

Ese es el repositorio de software (GitHub, `andresecha/CAO_CRM`), el **repositorio primario**. El
trabajo también toca una segunda carpeta, que **no es un repositorio git** y no hay que clonar ni
commitear:

```
/home/andres/Documentos/GitLab/data-publication/
```

Es la colección de datasets preparados para depositar en Nakala. Hermana del repo, fuera de él.

**No tocar** `~/Documentos/GitLab/cao_crm` (espejo institucional congelado el 2026-07-11) ni
`~/Documentos/GitLab/OLD_CAO_CRM` ni `~/Documentos/GitLab/Ontologie` (carpetas de trabajo de una
fase anterior, sin cambios desde julio de 2026).

Entorno: `make validate` y `make docs` necesitan las dependencias Python del proyecto, que **no
están** en el Python del sistema. Anteponer este venv al `PATH` en cada sesión:

```bash
export PATH="/home/andres/Documentos/GitLab/cao_crm/.venv/bin:$PATH"
```

`.tools/jena` y `.tools/robot` ya están instalados (`.tools/jena` es un symlink a
`~/Documentos/GitLab/Validation/.tools/jena`, Jena 6.1.0). Chrome y WeasyPrint están disponibles, así
que `make docs` produce también los PDF.

---

## 1. Situación exacta en la que quedó el trabajo

La documentación de CAO_CRM se genera en cuatro idiomas (en, fr, es, ro). El rumano es un caso
aparte por dos razones acumuladas:

- **Ningún término tiene etiqueta oficial en rumano.** Los 130 términos del módulo vienen de
  CIDOC-CRM 7.1.3, LRMoo 1.1.1 y CRMdig 5.0, y ninguno de los tres publica una sola `rdfs:label@ro`.
  Las etiquetas y definiciones rumanas las aporta la capa de traducción del proyecto
  (`docs/i18n/CAO_CRM-1.0-i18n-ro.ttl`).
- **Ni Widoco 1.4.25 ni LODE traen paquete de idioma rumano.** No existe `widoco/ro.properties` ni
  `lode/ro.xml`, ni en el jar ni en el código fuente de ambos proyectos (verificado el 2026-09-03,
  cuando 1.4.25 seguía siendo el último release). Por eso `-lang ro` sale con toda la interfaz en
  inglés y `docs/postprocess_ro_chrome.py` la sustituye después, a partir de
  `docs/i18n/chrome-ro.yaml`.

**Lo que ya está revisado y cerrado:** Roxana Patras devolvió el 2026-09-01 la revisión
terminológica (`docs/i18n/review/review2-ro.md`, archivado) y sus correcciones están íntegramente
incorporadas — verificado término a término: los 130 bloques rumanos del documento coinciden
exactamente con el estado del repositorio. Corrigió 34 etiquetas y 88 definiciones, y fijó 6 entradas
del glosario puente (las marcadas `source: native_review` en `glossary_crosswalk-ro.yaml`). **Esa
parte no hay que volver a tocarla.**

**Lo que falta y es el objeto de este documento:** las ~73 cadenas de interfaz, que no existían
cuando ella revisó. Se le enviaron aparte como `docs/i18n/review/review-chrome-ro.md`.

**Estado del árbol de trabajo:** el trabajo rumano está **escrito pero sin commitear**, a propósito,
esperando justamente esta revisión. Antes de tocar nada, mirar `git status` y `git diff` para ver con
qué se está trabajando. Debería haber, sin commitear:

- `docs/i18n/chrome-ro.yaml` (nuevo) — las cadenas
- `docs/postprocess_ro_chrome.py` (nuevo) — el script que las aplica
- `docs/i18n/scripts/build_chrome_review_doc.py` (nuevo) — genera la hoja de revisión
- `docs/build.sh` (modificado) — el paso que invoca el script, y los comentarios que lo explican
- `README.md`, `docs/README.md`, `docs/i18n/README.md` (modificados)

**Lo que NO está en el árbol y hay que rehacer: los tres acoplamientos.** Llegaron a commitearse el
2026-09-04 (`cd15c48`, `64b2a13`, `841d8ce`) y **se revirtieron el mismo día** en `692d38a`, porque
sin el script que los alimenta dejaban `make docs` roto en un clon limpio: Widoco generaba la página
rumana con marco inglés, `postprocess_acknowledgments.py` buscaba el ancla rumana, no la encontraba y
abortaba el build entero. Al aplicar esta revisión hay que volver a ponerlos, ahora sí junto con el
resto:

| Archivo | Qué hay que volver a poner |
|---|---|
| `docs/postprocess_acknowledgments.py` | `ANCHORS["ro"]` = primer fragmento rumano de `ackText` (hoy vuelve a ser la frase inglesa) |
| `docs/postprocess_i18n_marker.py` | `TOOLTIP["ro"]` en rumano (hoy en inglés) |
| `docs/postprocess_titlepage.py` | `SUBTITLES["ro"]` en rumano (hoy la frase inglesa) |
| `docs/build.sh` | el `<p class="subtitle">` de la entrada rumana de la landing page, hoy ausente |

Los textos de los cuatro están en `i18n/chrome-ro.yaml`: los tres primeros en la entrada `ackText` y
en `front_matter`, el cuarto es la misma frase que `SUBTITLES["ro"]`. Se pueden recuperar también con
`git show cd15c48`, `git show 64b2a13` y `git show 841d8ce`, pero **conviene tomarlos de la versión
revisada por Roxana, no de esos commits**, que llevan el borrador anterior.

**La lección, para no repetirla:** esos cuatro cambios y el paso de `docs/build.sh` son una sola
unidad. Commitear cualquiera de ellos sin los demás rompe el build. Van juntos o no van.

Si el árbol estuviera limpio, significa que alguien ya commiteó ese trabajo: en ese caso, seguir
igualmente los pasos de abajo, partiendo de lo que haya en `main`.

---

## 2. Qué se recibe y dónde va

Roxana devuelve **`review-chrome-ro.md`** corregido (probablemente por correo; suele acabar en
`~/Descargas/`). Es una tabla de tres columnas por sección: inglés de Widoco/LODE, francés de las
mismas herramientas, y rumano a corregir.

Primer paso: **archivar el documento devuelto** en `docs/i18n/review/review-chrome-ro.md`
(sobrescribiendo la versión enviada). Ese directorio está en `.gitignore` a propósito: es material
de trabajo, no un artefacto publicado.

Antes de nada, comprobar que el archivo recibido es realmente la revisión del chrome y no otra cosa
—ya ocurrió una vez que el archivo entregado era, byte a byte, la revisión terminológica anterior
que ya estaba incorporada—:

```bash
# ¿es idéntico a algo que ya tenemos?
for f in docs/i18n/review/*.md; do cmp -s ~/Descargas/review-chrome-ro.md "$f" && echo "IDÉNTICO a $f"; done
# ¿trae de verdad las cadenas de interfaz?
grep -c -E 'has super-classes|back to|Cross-reference for|Object Properties' ~/Descargas/review-chrome-ro.md
```

Si es idéntico a un archivo ya archivado, o si el segundo comando devuelve 0, **parar y decírselo a
Andrés**: no es el documento que se esperaba.

---

## 3. Incorporar las correcciones

### 3.1 Las cadenas de interfaz → `docs/i18n/chrome-ro.yaml`

Cada entrada del YAML tiene `en`, `fr` y `ro`. **Solo se edita `ro`.** El campo `en` es la clave de
búsqueda contra el HTML generado: si se toca, la sustitución deja de encontrar la cadena y el
resultado es una página a medio traducir sin ningún error visible. El `fr` es referencia para el
revisor y tampoco se toca.

Trasladar cada corrección de la columna «Română» del documento devuelto a su entrada por `key`.
Si Roxana dejó una nota tipo `[NOT SURE]` o una duda, **no resolverla por cuenta propia**:
recogerla y preguntársela a Andrés al final, dejando entretanto la propuesta actual.

Las entradas `use: prose` y `use: prov` tienen el `ro` partido en **fragmentos** que se
corresponden uno a uno con los del `en` (el texto va troceado por los `<a>` que Widoco incrusta, para
que los enlaces sobrevivan a la sustitución). Si una corrección reordena la frase, hay que repartir
el texto corregido entre los mismos fragmentos, manteniendo su número y su orden. Si eso resultara
imposible sin forzar el rumano, decírselo a Andrés en vez de inventar un reparto.

### 3.2 Las tres cadenas de `front_matter` → además, a su lugar en el código

La sección `front_matter` del YAML es documentación del envío: los scripts guardan su **propia**
copia y son esas copias las que se usan. Si Roxana corrigió alguna, hay que actualizar las dos:

| Entrada de `chrome-ro.yaml` | Copia real que hay que corregir también |
|---|---|
| `subtitle` | `SUBTITLES["ro"]` en `docs/postprocess_titlepage.py` **y** el `<p class="subtitle">` de la entrada rumana de la landing page, dentro de `docs/build.sh` (bloque `cat > site/index.html`). Son la misma frase en dos sitios: no pueden divergir |
| `overlay_marker_tooltip` | `TOOLTIP["ro"]` en `docs/postprocess_i18n_marker.py` |

Ojo con las entidades HTML: `postprocess_titlepage.py` y la landing page escriben las diacríticas
como entidades (`&#537;` para ș, `&#539;` para ț, `&bdquo;`/`&rdquo;` para las comillas rumanas),
mientras que `chrome-ro.yaml` las lleva en UTF-8 literal. Respetar la convención de cada archivo.

### 3.3 El acoplamiento que rompe el build si se olvida

`docs/postprocess_acknowledgments.py` inserta los agradecimientos del proyecto justo antes del
párrafo de créditos que escribe Widoco, y localiza ese punto por sus primeras palabras. Como en
rumano ese párrafo ya ha sido traducido por `postprocess_ro_chrome.py` cuando ese script corre,
`ANCHORS["ro"]` contiene el **texto rumano**, que es exactamente el primer fragmento de la entrada
`ackText` de `chrome-ro.yaml`.

**Si la revisión cambia ese primer fragmento, hay que actualizar `ANCHORS["ro"]` con el mismo
texto.** Si no, `make docs` aborta con `postprocess_acknowledgments.py: anchor not found` — que al
menos falla ruidosamente, pero conviene no llegar ahí.

---

## 4. Regenerar

```bash
cd /home/andres/Documentos/GitHub/CAO_CRM
export PATH="/home/andres/Documentos/GitLab/cao_crm/.venv/bin:$PATH"
make docs
```

Esto regenera los cuatro HTML, los cuatro PDF, las páginas de procedencia y la landing page.

En la salida debe aparecer `postprocess_ro_chrome.py: ~1795 replacement(s) in site/index-ro.html`
repartidas en las siete reglas, y `11 replacement(s) in site/provenance/provenance-ro.html`. Un
número muy distinto significa que algo dejó de casar: investigarlo antes de seguir.

También hay que regenerar la hoja de revisión, para que refleje el estado corregido:

```bash
python3 docs/i18n/scripts/build_chrome_review_doc.py
```

---

## 5. Verificación (no saltarse ninguna)

### 5.1 Las otras tres lenguas no se movieron

Es el invariante del proyecto: añadir o corregir rumano **no puede** alterar en/fr/es.

```bash
git diff --stat docs/site/index-en.html docs/site/index-fr.html docs/site/index-es.html
```

Debe salir **vacío**. Si no lo está, hay una regla del post-proceso rumano actuando sobre archivos
que no le corresponden: pararse a entenderlo.

Los PDF de esas tres lenguas sí cambian de bytes en cada build (llevan la fecha de creación
incrustada), pero su **texto** debe ser idéntico:

```bash
for l in en es fr; do git show HEAD:docs/site/CAO_CRM-1.0-$l.pdf > /tmp/o-$l.pdf
  pdftotext -q /tmp/o-$l.pdf /tmp/o-$l.txt; pdftotext -q docs/site/CAO_CRM-1.0-$l.pdf /tmp/n-$l.txt
  printf "%s: " $l; cmp -s /tmp/o-$l.txt /tmp/n-$l.txt && echo IDÉNTICO || echo DIFIERE; done
```

Si el texto es idéntico, **revertirlos** para que el diff quede limpio:
`git checkout -- docs/site/CAO_CRM-1.0-{en,es,fr}.pdf`

### 5.2 No queda inglés suelto en las páginas rumanas

```bash
python3 - <<'EOF'
import yaml
d=yaml.safe_load(open("docs/i18n/chrome-ro.yaml",encoding="utf-8"))
ens=[]
for e in d["strings"]:
    v=e["en"]; ens.extend(v if isinstance(v,list) else [v])
LEGIT={"documentation","Documentation","Revision:","Legend","class","or","Date","Source"}
for f in ("docs/site/index-ro.html","docs/site/provenance/provenance-ro.html"):
    raw=open(f,encoding="utf-8").read()
    bad=[en for en in set(ens) if len(en.strip())>=4 and en not in LEGIT and en in raw]
    print(f"  {f}: {'LIMPIO' if not bad else bad}")
EOF
```

Ambas líneas deben decir `LIMPIO`. Las excepciones de `LEGIT` son legítimas y deben quedarse:
`documentation/ro/` aparece como ruta dentro de la introducción rumana, "Live OWL Documentation
Environment" es un nombre propio, `Revision:` está dentro de la cita bibliográfica de la ontología
(contenido del modelo, en inglés a propósito), y `class`/`Legend` son atributos e `id` de HTML.

### 5.3 La página y el PDF se ven bien

```bash
pdftoppm -png -r 50 -f 1 -l 1 docs/site/CAO_CRM-1.0-ro.pdf /tmp/cover-ro   # portada
xdg-open docs/site/index-ro.html
```

Mirar de verdad: portada (título, subtítulo rumano, autor, logo ARIANE), cuprins, una ficha de
término con sus `are supraclase` / `este în domeniul lui`, la leyenda, y la página de procedencia.

### 5.4 Cadena de validación y marca de agua

```bash
make validate
```

Las 8 categorías más `cq` deben pasar, incluida `watermark` (todo archivo `.md`/`.sh`/`.py`/`.rq`/
`.ttl`/`.nt`/`.rdf`/`.owx` con su cabecera de copyright — si se creó algún archivo nuevo, corregir
con `make watermark-fix`).

`make docs` reserializa `ontology/CAO_CRM-1.0.nt` y `.jsonld` en cada ejecución y rdflib no garantiza
el orden, así que aparecerán como modificados sin haber cambiado. Comprobarlo y revertirlos:

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

## 6. Actualizar la documentación del propio repositorio

Con la revisión cerrada, tres textos dejan de ser verdad y hay que corregirlos:

1. **`docs/i18n/chrome-ro.yaml`**, cabecera — quitar el bloque `STATUS: PROPOSED TRANSLATION, NOT
   YET REVIEWED BY A NATIVE SPEAKER` y poner que Roxana Patras la revisó, con la fecha real de
   devolución. Actualizar también `meta.status` (de `pending-native-review` a `native-review-complete`)
   y añadir la fecha.
2. **`docs/i18n/README.md`**, entrada de `chrome-ro.yaml` en la sección *Layout* — sustituir
   «**Not yet reviewed by a native speaker** — out for review…» por la constatación de la revisión,
   con la fecha y el enlace de Roxana.
3. **`docs/README.md`**, sección *Romanian: a language pack neither tool ships*, párrafo **Review
   status** — ahora ambas revisiones (la terminológica del 2026-09-01 y la del chrome) están
   cerradas; reescribirlo en consecuencia.

En los tres, el enlace de Roxana Patras es el que ella misma pidió que se usara, el que ya figura en
las documentaciones públicas: **<https://dhl.uaic.ro/taqwa/elementor-page-2114/members-2/>**
(Universitatea „Alexandru Ioan Cuza”, Iaşi, Rumanía).

Opcional, coméntaselo a Andrés antes de hacerlo: el `README.md` de la raíz tiene una fila de badges
`Docs-FR / Docs-ES / Docs-EN` que nunca incluyó el rumano. Con la edición rumana ya cerrada, añadir
`Docs-RO` enlazando a <https://www.cao-crm.eu/index-ro.html> sería coherente.

---

## 7. Commit

**Reglas absolutas:**

- **Nunca `git push`.** Los commits son locales; empujar es decisión de Andrés.
- **Ningún commit lleva atribución a Claude**: sin `Co-Authored-By`, sin `Claude-Session`, sin
  ninguna otra mención. Es una publicación científica firmada con autoría única declarada en el
  propio RDF (`dc:creator`) y DOI Nakala; una coautoría de herramienta en el historial la
  contradice.
- Mensajes en español, descriptivos, explicando **por qué** además de qué — es el estilo del
  repositorio; mirar `git log` antes de escribir el primero.
- Un commit por asunto, no uno gigante.

Comprobación final antes de dar el trabajo por cerrado:

```bash
git log -6 --format='%an <%ae>%n  %s'
git log -6 --format='%B' | grep -iE 'claude|co-authored|anthropic' || echo "sin atribución: correcto"
```

---

## 8. Nakala: qué se deposita y qué se actualiza

Todo esto ocurre en `/home/andres/Documentos/GitLab/data-publication/`, que **no es un repositorio
git**: los archivos simplemente se dejan en disco, listos para que Andrés los suba. La colección
tiene diez datasets numerados; cada carpeta lleva su `METADATA-nakala.md`, que es la ficha completa
para transcribir campo a campo al formulario de Nakala o usar como payload de su API.

### 8.1 Dataset 06 — capa de traducción rumana (ya estaba listo)

`06-capa-traduccion-i18n-ro/`. **No depende de la revisión del chrome**: su contenido es la capa
terminológica, revisada el 2026-09-01, y su carga útil ya se refrescó con las correcciones de
Roxana. Existe como pre-depósito privado con DOI **`10.34847/NKL.7020N1BK`**.

Acción pendiente en Nakala (de Andrés, en la interfaz web): sustituir la carga útil del "data" por
la de esta carpeta —la depositada el 2026-07-14 es anterior a la revisión— y cambiar la visibilidad
a **pública**. Verificar antes que la carpeta sigue coincidiendo con el repositorio:

```bash
D=/home/andres/Documentos/GitLab/data-publication/06-capa-traduccion-i18n-ro
G=/home/andres/Documentos/GitHub/CAO_CRM/docs/i18n
for f in CAO_CRM-1.0-i18n-ro.ttl glossary_crosswalk-ro.yaml term_inventory.json; do
  cmp -s $D/$f $G/$f && echo "OK $f" || echo "DESACTUALIZADO $f"; done
for f in $D/translations/*.yaml; do cmp -s "$f" "$G/translations-ro/$(basename $f)" \
  && echo "OK $(basename $f)" || echo "DESACTUALIZADO $(basename $f)"; done
```

### 8.2 Dataset 10 — documentación generada en rumano (lo que esta revisión desbloquea)

`10-documentacion-generada-ro/`. **Todavía no existe en Nakala**: no tiene DOI y hay que crearlo.

Refrescar su carga útil con lo recién regenerado (deben quedar copias exactas del repositorio, sin
parches locales de ningún tipo):

```bash
D=/home/andres/Documentos/GitLab/data-publication/10-documentacion-generada-ro
G=/home/andres/Documentos/GitHub/CAO_CRM
cp $G/docs/site/index-ro.html $G/docs/site/CAO_CRM-1.0-ro.pdf $D/
cp $G/docs/site/provenance/provenance-ro.{html,ttl} $D/provenance/
cp -r $G/docs/site/resources/. $D/resources/
cp $G/docs/site/logos/*.svg $D/logos/
cp $G/docs/i18n/chrome-ro.yaml $G/docs/config-ro.properties $G/docs/intro-ro.html $D/fuentes/
```

Y verificar que el conjunto es consultable tal cual se descargue:

```bash
cd $D
grep -rl '/home/andres' . || echo "sin rutas locales: correcto"
grep -o 'href="[^"]*index-ro[^"]*"' provenance/provenance-ro.html   # debe ser ../index-ro.html
python3 -c "
from bs4 import BeautifulSoup; import os
s=BeautifulSoup(open('index-ro.html',encoding='utf-8').read(),'html.parser')
refs={e.get(a).split('#')[0] for t,a in (('img','src'),('script','src'),('link','href'),('a','href'))
      for e in s.find_all(t) if e.get(a) and not e.get(a).startswith(('http','#','mailto','data:'))}
print('faltantes:', [r for r in sorted(refs) if r and not os.path.exists(r)] or 'ninguno')"
```

Después, actualizar su `METADATA-nakala.md`:

- Quitar el bloque **ESTADO: PREPARADO, NO DEPOSITAR TODAVÍA** y sustituirlo por el estado real
  (listo para crear y publicar, con la fecha de cierre de la revisión).
- Rellenar `Date / created`, `dcterms:date`/`created`, `dcterms:issued`, `dcterms:modified`,
  `dcterms:available` y `dcterms:dateAccepted` (que hoy dice «Parcial»: pasa a completo).
- `dcterms:accessRights`: quitar la advertencia de no publicar.
- `dcterms:provenance`: la frase que dice que las cadenas de interfaz están pendientes de revisión
  pasa a decir que fueron revisadas, con la fecha.
- Cuando Nakala asigne el DOI, ponerlo en `dcterms:identifier` y en la
  `dcterms:bibliographicCitation` sugerida.

**Roxana Patras es coautora** (`dcterms:creator` y `dcterms:rightsHolder`) de los datasets 06 y 10,
con su afiliación y su enlace. Ya está así en ambas fichas: no quitarlo. El fundamento está escrito
en la sección «Por qué Roxana Patras figura como coautora» de la ficha del 10, y sigue siendo válido.

### 8.3 Los dos archivos de la colección

- **`data-publication/README.md`** — la fila 10 de la tabla y el párrafo que introduce el dataset 10
  dicen que está pendiente de revisión; actualizarlos.
- **`data-publication/COLLECTION-METADATA-nakala.md`** — el párrafo de estado del principio, el
  campo `Statut` y la fila 10 de la tabla de composición. Cuando existan los DOI reales, sustituir
  los `[pendiente]` y completar los `dcterms:relation`/`isReferencedBy` cruzados.

---

## 9. Al terminar, decirle a Andrés

- Qué cambió realmente la revisión (cuántas cadenas, si alguna obligó a tocar `ANCHORS["ro"]`).
- Cualquier `[NOT SURE]` o duda que Roxana dejara sin resolver.
- Que los commits están hechos **en local y sin empujar**, y cuáles son.
- Las dos acciones que solo puede hacer él en la interfaz de Nakala: publicar el 06 (sustituyendo
  antes su carga útil) y crear el 10.
