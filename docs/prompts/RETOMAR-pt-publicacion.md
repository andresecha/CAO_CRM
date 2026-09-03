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

# Retomar: publicación del portugués (revisión de Ana Salgado)

> Documento autosuficiente. Dárselo entero a Claude como primer mensaje de una sesión nueva.
> **Independiente del italiano:** no supone que el italiano se haya hecho antes ni después, y los
> números de dataset de Nakala están fijados por idioma, no por orden de llegada.

## 0. ANTES DE NADA: la condición que este idioma tiene y los otros no

**Ana Salgado no forma parte del equipo del proyecto.** Fue invitada a revisar las traducciones al
portugués y, a fecha de redacción de este documento, **no había confirmado si acepta participar**.
No figura entre los contribuidores declarados en el encabezado del RDF (`dc:contributor`), a
diferencia de Roxana Patras y Simone Rebora.

Por eso, antes de tocar nada:

1. **Confirmar con Andrés que Ana Salgado aceptó participar** y que lo que llega es su revisión.
2. Si llega una revisión pero **sin** confirmación explícita de participación, **parar** y
   preguntárselo. La ficha del dataset 08 dice literalmente que no debe hacerse público «bajo
   ninguna circunstancia» mientras eso no esté claro, y esa cautela es deliberada: publicar
   atribuyendo coautoría a alguien que no la ha aceptado es un problema real, no un formalismo.
3. **Si Ana Salgado declina participar**, este documento no aplica tal cual. En ese caso hay que ir
   a la sección 11 («Si declina») y preguntarle a Andrés qué quiere hacer, en vez de seguir los
   pasos normales.

También hace falta un dato que el proyecto **no tiene**: su afiliación exacta y el enlace personal
que quiera que se use. Roxana Patras y Simone Rebora tienen el suyo en
`docs/postprocess_people_links.py`; Ana Salgado no. **Pedírselo a Andrés y no inventarlo.**

---

## 1. Dónde lanzar Claude

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

## 2. Situación exacta de la que se parte

El portugués existe entero desde el 2026-07-13 pero está **deliberadamente apartado**: es una
traducción asistida por IA sin revisar, no está cableada en el build y está en `.gitignore`. Lo que
hay, sin versionar:

| Archivo | Qué es |
|---|---|
| `docs/i18n/translations-pt/*.yaml` | Los 130 términos en portugués, en 8 lotes temáticos |
| `docs/i18n/glossary_crosswalk-pt.yaml` | Glosario puente de los conceptos ancla de CIDOC-CRM |
| `docs/i18n/CAO_CRM-1.0-i18n-pt.ttl` | El overlay compilado a partir de los lotes |
| `docs/config-pt.properties` | Título, resumen, descripción, estado y cita, en portugués |
| `docs/intro-pt.html` | Introducción y "Estado deste documento" |
| `documentation/pt/` | Las 10 fichas pedagógicas en portugués |
| `PARAGRAPHS["pt"]` en `docs/postprocess_acknowledgments.py` | Los agradecimientos en portugués (este sí está en el repo, ya versionado) |

**Diferencia capital con el rumano, que ahorra la mitad del trabajo:** Widoco 1.4.25 **sí** trae
`widoco/pt.properties` y LODE **sí** trae `lode/pt.xml`. Los títulos de sección, las etiquetas de
referencias cruzadas, la navegación y la leyenda salen ya en portugués de la propia herramienta. El
portugués **no necesita** nada equivalente a `docs/i18n/chrome-ro.yaml` ni a
`docs/postprocess_ro_chrome.py`, que existen solo porque para el rumano no hay paquete de idioma.
No crear un `chrome-pt.yaml`.

Un matiz que conviene preguntar a Andrés: el paquete `pt` de Widoco es genérico y no distingue
variantes. Si la revisión de Ana Salgado se hace en português europeu, puede haber un desajuste
menor de registro entre la interfaz de la herramienta y el contenido traducido. No es un defecto que
haya que arreglar por cuenta propia; sí conviene mencionarlo.

**Y una diferencia con el rumano y el italiano que hay que tener presente todo el rato:** el
portugués **sí** es una de las siete lenguas en que CIDOC-CRM publica etiquetas oficiales. Medido
sobre `term_inventory.json` el 2026-09-03:

| Idioma | Términos con etiqueta oficial | Términos que la capa del proyecto tiene que aportar |
|---|---|---|
| ro | 0 | 130 |
| it | 0 | 130 |
| **pt** | **76** | **54** |

Es decir: en la página portuguesa, más de la mitad de las etiquetas son contenido oficial de
CIDOC-CRM y **no** llevan daga (†) ni proceden de la traducción del proyecto. Ninguna afirmación del
tipo «ninguno de los 130 términos tiene etiqueta oficial», válida para el rumano y el italiano, vale
aquí — ni en las fichas de Nakala, ni en los README, ni en el argumento de coautoría. Volver a medir
antes de escribir cualquier cifra:

```bash
python3 -c "
import json
inv=json.load(open('docs/i18n/term_inventory.json',encoding='utf-8'))
terms=inv if isinstance(inv,list) else inv.get('terms',inv)
n=sum(1 for t in (terms.values() if isinstance(terms,dict) else terms)
      if 'pt' in (t.get('official_languages_label') or []))
print('términos con etiqueta oficial en pt:', n)"
```

Antes de empezar, mirar `git status` y `git log --oneline -15`: puede haber trabajo rumano o
italiano sin commitear, que **no hay que tocar ni commitear junto con esto**.

---

## 3. Qué se recibe y dónde va

Ana Salgado devuelve **`review-pt.md`** corregido (probablemente por correo; suele acabar en
`~/Descargas/`). Es un único documento con cuatro secciones: **A** agradecimientos, **B**
introducción / estado del documento, **C** resumen y descripción de la ontología, **D** los 130
términos uno a uno. Cada bloque muestra el inglés oficial, el francés de referencia y el portugués a
corregir bajo «PLEASE REVIEW / CORRECT BELOW».

Archivarlo en `docs/i18n/review/review-pt.md` (sobrescribiendo el enviado). Ese directorio está en
`.gitignore` a propósito: es material de trabajo, no un artefacto publicado.

Comprobar primero que es de verdad la revisión devuelta y no la copia que se envió —ya ocurrió una
vez que el archivo entregado era, byte a byte, el mismo que ya estaba archivado—:

```bash
cmp -s ~/Descargas/review-pt.md docs/i18n/review/review-pt.md \
  && echo "IDÉNTICO al enviado: NO trae correcciones, preguntar a Andrés" \
  || echo "difiere del enviado: tiene correcciones, seguir"
```

Si es idéntico, **parar y decírselo a Andrés**.

---

## 4. Incorporar las correcciones: las cuatro secciones y sus destinos

Está documentado en `docs/i18n/README.md`, sección *Where a review lands*:

| Sección del documento | Destino real |
|---|---|
| A. Acknowledgments | `PARAGRAPHS["pt"]` en `docs/postprocess_acknowledgments.py` |
| B. Introduction / Estado deste documento | `docs/intro-pt.html` |
| C. Abstract & description | `abstract=` / `description=` (y `status=` si lo corrigió) en `docs/config-pt.properties` |
| D. Term-by-term glossary | `label` / `comment` en `docs/i18n/translations-pt/*.yaml` |

Reglas al trasladar:

- **Solo se toca el portugués.** El inglés y el francés de cada bloque son referencia y no se editan.
- Si una etiqueta de la sección D cambió, revisar si su concepto está en
  `docs/i18n/glossary_crosswalk-pt.yaml`: si la revisión impuso otra palabra para un concepto ancla,
  actualizar también esa entrada y marcarla **`source: native_review`**, que es la convención del
  proyecto para distinguir lo que fijó el hablante nativo de lo que decidió el equipo (así se hizo
  con las 6 entradas que fijó la revisión rumana). Si no se hace, `check_consistency.py` reportará
  deriva en la siguiente ejecución.
- Si Ana dejó una nota tipo `[NOT SURE]` o una duda, **no resolverla por cuenta propia**: recogerla
  y preguntársela a Andrés al final, dejando entretanto la propuesta actual.
- Si corrigió una etiqueta que **sí** tenía versión oficial de CIDOC-CRM en portugués, eso es un
  caso distinto y hay que señalarlo a Andrés: el proyecto no sobrescribe contenido oficial con
  traducción propia (es el principio de «composición pura» del ADR-002), así que esa corrección
  quizá no deba aplicarse tal cual.

Recompilar el overlay y pasar el control de coherencia:

```bash
cd docs/i18n
python3 scripts/compile_i18n_overlay.py translations-pt CAO_CRM-1.0-i18n-pt.ttl pt
python3 scripts/check_consistency.py translations-pt glossary_crosswalk-pt.yaml term_inventory.json
cd ../..
```

`check_consistency.py` es heurístico: leer su salida, no tratarla como una barrera automática.

Comprobación de que no se perdió nada — el round-trip que recomienda el propio
`docs/i18n/README.md`: regenerar el documento de revisión desde el estado ya corregido y comparar
con el que devolvió Ana. Deben coincidir en la parte portuguesa.

```bash
python3 docs/i18n/scripts/build_review_doc.py pt /tmp/roundtrip-pt.md
```

---

## 5. Cablear el portugués en el build

Cinco puntos en tres archivos. Todos son necesarios; olvidar uno da una página a medio hacer.

### 5.1 `docs/build.sh`

1. **La lista de idiomas** (busca `LANGS=`): añadir `pt`. Todo lo que viene después —prefijos de
   código, bibliografía, agradecimientos, portada, dagas i18n, PDF, landing page— itera sobre esta
   lista, así que el idioma se declara aquí una sola vez.
2. **El overlay propio.** Dentro del bucle `for lang in $LANGS` hay un bloque `if [ "$lang" = ro ]`
   que funde el overlay rumano en una copia temporal del RDF, aparte de la fusión fr/es. El
   portugués necesita lo mismo, por la misma razón: que las pasadas ya publicadas sigan recibiendo
   exactamente la misma entrada, de modo que añadir un idioma no pueda perturbarlas. Extender ese
   bloque (o añadir uno paralelo) para `pt`, con `i18n/CAO_CRM-1.0-i18n-pt.ttl`,
   `config-pt.properties` e `intro-pt.html`, incluida la guarda que salta la pasada si falta alguno.
3. **La selección de overlay del marcador de dagas.** Más abajo hay
   `[ "$lang" = ro ] && overlay="i18n/CAO_CRM-1.0-i18n-ro.ttl"`. Añadir la línea equivalente para
   `pt`; si no, el portugués se compararía contra el overlay fr/es y no marcaría las dagas correctas.
4. **La landing page.** En el bloque `cat > site/index.html`, añadir la entrada portuguesa
   (`🇵🇹 Português`, enlace a `index-pt.html`) con su `<p class="subtitle">`, que es la misma frase
   del subtítulo de portada del punto 5.2: las dos copias no pueden divergir.

### 5.2 Los diccionarios por idioma

| Archivo | Clave a añadir | De dónde sale |
|---|---|---|
| `docs/postprocess_titlepage.py` | `SUBTITLES["pt"]` | La traducción portuguesa de la frase que ya está en `SUBTITLES["en"]`. Si la sección C de la revisión la incluía, usar la versión corregida; si no, decírselo a Andrés antes de inventarla |
| `docs/postprocess_i18n_marker.py` | `TOOLTIP["pt"]` | El texto del tooltip de la daga, en portugués, siguiendo el de las otras lenguas |
| `docs/postprocess_acknowledgments.py` | `ANCHORS["pt"]` | **Ver 5.3: no se adivina, se observa** |

### 5.3 `ANCHORS["pt"]`: hay que observarlo, no deducirlo

`postprocess_acknowledgments.py` inserta los agradecimientos del proyecto justo antes del párrafo
fijo de créditos que escribe Widoco (el que agradece a los autores de LODE y Widoco), y localiza ese
punto por sus primeras palabras. Como Widoco **sí** trae paquete portugués, ese párrafo saldrá
traducido por la propia herramienta, y su redacción exacta **nunca se ha observado en este
proyecto**. El comentario del propio script lo advierte: copiarla de una página realmente generada,
no adivinarla.

Procedimiento exacto:

1. Hacer los cambios de 5.1 y las dos primeras filas de 5.2.
2. Ejecutar `make docs`. Abortará —`build.sh` corre con `set -euo pipefail`— con
   `postprocess_acknowledgments.py: unknown language 'pt'`. **Es lo esperado**: para entonces
   Widoco ya ha escrito `docs/site/index-pt.html` en disco.
3. Sacar de ahí las primeras palabras del párrafo:

   ```bash
   grep -o '<p>[^<]\{0,80\}' docs/site/index-pt.html | grep -iE 'autor|agradec|LODE' | head -3
   ```

   Buscar el párrafo que menciona a Silvio Peroni / LODE / Daniel Garijo / Widoco y copiar
   literalmente sus primeras palabras (unas seis o siete, suficientes para ser inequívocas).
4. Añadir `ANCHORS["pt"]` con ese texto exacto y volver a ejecutar `make docs` entero.

Como el build abortado deja `site/` a medio procesar, la comprobación del invariante del punto 7
solo vale después de una ejecución **completa y correcta**.

### 5.4 `.gitignore`

Quitar del bloque «Italian and Portuguese» las cinco entradas portuguesas, que dejan de ser trabajo
apartado y pasan a ser contenido publicado:

```
docs/intro-pt.html
docs/config-pt.properties
docs/i18n/translations-pt/
docs/i18n/glossary_crosswalk-pt.yaml
docs/i18n/CAO_CRM-1.0-i18n-pt.ttl
```

**`documentation/pt/` se queda ignorado.** Las 10 fichas pedagógicas portuguesas **no** forman parte
de `review-pt.md` —que cubre solo las secciones A-D— y siguen siendo un borrador asistido por IA sin
revisar. Es exactamente el mismo criterio que se aplicó a `documentation/ro/`. Reescribir el
comentario del bloque para que quede claro qué sigue apartado y por qué, y dejar las entradas
italianas intactas.

---

## 6. Regenerar

```bash
cd /home/andres/Documentos/GitHub/CAO_CRM
export PATH="/home/andres/Documentos/GitLab/cao_crm/.venv/bin:$PATH"
make docs
```

Debe terminar anunciando la landing page y todos los `index-*.html`, con un PDF por idioma.

---

## 7. Verificación (no saltarse ninguna)

### 7.1 Las otras lenguas no se movieron

Es el invariante del proyecto: añadir un idioma **no puede** alterar los ya publicados.

```bash
git diff --stat docs/site/index-en.html docs/site/index-fr.html docs/site/index-es.html docs/site/index-ro.html
```

Debe salir **vacío** (si el rumano o el italiano estuvieran aún sin commitear, compararlos contra su
copia previa en vez de contra HEAD). Si algo se movió, el cableado del punto 5 está tocando archivos
que no le corresponden.

Los PDF de esas lenguas cambian de bytes en cada build (fecha de creación incrustada) pero su
**texto** debe ser idéntico; si lo es, revertirlos para dejar el diff limpio:

```bash
for l in en es fr ro it; do git show HEAD:docs/site/CAO_CRM-1.0-$l.pdf > /tmp/o-$l.pdf 2>/dev/null || continue
  pdftotext -q /tmp/o-$l.pdf /tmp/o-$l.txt; pdftotext -q docs/site/CAO_CRM-1.0-$l.pdf /tmp/n-$l.txt
  printf "%s: " $l; cmp -s /tmp/o-$l.txt /tmp/n-$l.txt && echo IDÉNTICO || echo DIFIERE; done
```

### 7.2 La página portuguesa está realmente en portugués

Widoco debería haber puesto la interfaz en portugués por su cuenta. Confirmarlo en vez de suponerlo:

```bash
python3 -c "
from bs4 import BeautifulSoup
s=BeautifulSoup(open('docs/site/index-pt.html',encoding='utf-8').read(),'html.parser')
print('Títulos:', [' '.join(h.get_text().split())[:45] for h in s.find_all(['h2','h4'])[:10]])
print('Etiquetas de referencia cruzada:', sorted({dt.get_text().strip() for dl in s.select('dl.description') for dt in dl.find_all('dt')}))"
```

Los títulos y las etiquetas de referencia cruzada deben leerse en portugués. **Si salieran en
inglés**, significa que el paquete de idioma no se cargó: pararse a averiguar por qué y decírselo a
Andrés — no improvisar un post-proceso al estilo del rumano sin hablarlo antes.

Comprobar además cuántas dagas se aplicaron: la salida de `make docs` dirá
`postprocess_i18n_marker.py: marked N entities in site/index-pt.html`. Ese **N no será 130**, a
diferencia del italiano y el rumano, porque 76 términos ya traen etiqueta oficial de CIDOC-CRM en
portugués y esos no pasan por el overlay. El overlay portugués aporta hoy **54 etiquetas y 89
definiciones** (143 triples, frente a los 219 del rumano y del italiano, que son 130 + 89), así que
N reflejará eso. Usar el número real —nunca 130— en las fichas de Nakala y en los README.

### 7.3 La página y el PDF se ven bien

```bash
pdftoppm -png -r 50 -f 1 -l 1 docs/site/CAO_CRM-1.0-pt.pdf /tmp/cover-pt
xdg-open docs/site/index-pt.html
```

Mirar de verdad: portada (título, subtítulo portugués, autor, logo ARIANE), índice, una ficha de
término, la leyenda, los agradecimientos y la página de procedencia.

### 7.4 Cadena de validación y marca de agua

```bash
make validate
```

Las 8 categorías más `cq` deben pasar, incluida `watermark`: todo archivo `.md`/`.sh`/`.py`/`.rq`/
`.ttl`/`.nt`/`.rdf`/`.owx` debe llevar su cabecera de copyright. Los archivos portugueses que dejan
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

## 8. Actualizar la documentación del repositorio

- **`docs/i18n/README.md`** — la entrada `translations-pt/` está en la línea de «Italian and
  Portuguese drafts, not yet reviewed, not wired into `docs/build.sh`, gitignored». El portugués
  sale de ahí: darle su propia entrada, con la fecha de la revisión, el alcance y el crédito a Ana
  Salgado con el enlace que ella indique.
- **`docs/README.md`** — la sección *Multi-language build* enumera las pasadas de Widoco: añadir
  `-lang pt` y una nota que deje dicho que el portugués, a diferencia del rumano, no necesita
  post-proceso de interfaz porque Widoco y LODE sí traen su paquete de idioma. Ajustar las menciones
  a `index-{...}.html` y a los PDF.
- **`README.md`** (raíz, en francés) — la arborescencia del repositorio, las menciones a los
  `config-*.properties` e `intro-*.html`, y la fila de badges de documentación, a la que conviene
  añadir `Docs-PT` enlazando a <https://www.cao-crm.eu/index-pt.html>. Añadir la nota de que las
  correcciones del portugués las hizo Ana Salgado, con su enlace.

**Preguntar a Andrés antes de hacerlo:** si Ana Salgado pasa a ser coautora de dos datasets de
Nakala, ¿debe añadirse también como `dc:contributor` en el encabezado del RDF canónico, como están
Roxana Patras y Simone Rebora? Eso arrastraría `ontology/CAO_CRM-1.0.rdf` y sus cuatro
serializaciones, los cinco `config-*.properties`, los `intro-*.html` y `postprocess_people_links.py`
— es una decisión suya, no algo que deba hacerse de oficio.

---

## 9. Commit

**Reglas absolutas:**

- **Nunca `git push`.** Los commits son locales; empujar es decisión de Andrés.
- **Ningún commit lleva atribución a Claude**: sin `Co-Authored-By`, sin `Claude-Session`, sin
  ninguna otra mención. Es una publicación científica firmada con autoría única declarada en el
  propio RDF (`dc:creator`) y DOI Nakala.
- Mensajes en español, descriptivos, explicando **por qué** además de qué; mirar `git log` antes de
  escribir el primero.
- Un commit por asunto, no uno gigante.
- **No commitear de paso trabajo pendiente de otro idioma** que estuviera en el árbol sin commitear.

```bash
git log -8 --format='%an <%ae>%n  %s'
git log -8 --format='%B' | grep -iE 'claude|co-authored|anthropic' || echo "sin atribución: correcto"
```

---

## 10. Nakala: qué se deposita y qué se actualiza

En `/home/andres/Documentos/GitLab/data-publication/`, que **no es un repositorio git**: los
archivos se dejan en disco listos para que Andrés los suba.

### 10.1 Dataset 08 — capa de traducción portuguesa (ya existe, privado)

`08-capa-traduccion-i18n-pt/`, pre-depósito privado con DOI **`10.34847/NKL.D7DCF44B`**.

Su carga útil es la anterior a la revisión: **refrescarla** desde el repositorio y verificarlo.

```bash
D=/home/andres/Documentos/GitLab/data-publication/08-capa-traduccion-i18n-pt
G=/home/andres/Documentos/GitHub/CAO_CRM/docs/i18n
cp $G/CAO_CRM-1.0-i18n-pt.ttl $G/glossary_crosswalk-pt.yaml $G/term_inventory.json $D/
cp $G/translations-pt/*.yaml $D/translations/
for f in CAO_CRM-1.0-i18n-pt.ttl glossary_crosswalk-pt.yaml term_inventory.json; do
  cmp -s $D/$f $G/$f && echo "OK $f" || echo "FALLO $f"; done
for f in $D/translations/*.yaml; do cmp -s "$f" "$G/translations-pt/$(basename $f)" \
  && echo "OK $(basename $f)" || echo "FALLO $(basename $f)"; done
```

(No tocar `CAO_CRM-1.0-i18n-fr-referencia.ttl`: es el overlay francés de referencia, idéntico al del
dataset 09, y no cambia.)

Después, reescribir su `METADATA-nakala.md`. Tomar como modelo el del dataset 06
(`06-capa-traduccion-i18n-ro/METADATA-nakala.md`), que ya pasó por esta transición:

- Sustituir el bloque de estado —que hoy dice «NO HACER PÚBLICO BAJO NINGUNA CIRCUNSTANCIA
  TODAVÍA — participación aún no confirmada»— por el estado real, **dejando constancia explícita de
  que Ana Salgado confirmó su participación y en qué fecha**. Esa frase es el registro de que la
  condición se cumplió: no basta con borrar la advertencia.
- **Ana Salgado es coautora** (`dcterms:creator` y `dcterms:rightsHolder`), con la afiliación y el
  enlace que ella indique.
- Rellenar `Date / created`, `dcterms:created`, `dcterms:modified`, `dcterms:dateAccepted`,
  `dcterms:available`, y quitar de `dcterms:accessRights` la advertencia de no depositar.
- `dcterms:extent`: recontar sobre el archivo real, no copiar la cifra anterior:
  ```bash
  python3 -c "
  import rdflib; from rdflib.namespace import RDFS
  g=rdflib.Graph().parse('docs/i18n/CAO_CRM-1.0-i18n-pt.ttl',format='turtle')
  L=sum(1 for _,_,o in g.triples((None,RDFS.label,None)) if getattr(o,'language',None)=='pt')
  C=sum(1 for _,_,o in g.triples((None,RDFS.comment,None)) if getattr(o,'language',None)=='pt')
  print(f'{L} etiquetas + {C} definiciones = {len(g)} triples')"
  ```
  Y ajustar la descripción: la frase «ninguno tiene etiqueta oficial», que las fichas del rumano y
  del italiano usan con razón, **es falsa para el portugués** — 76 de los 130 términos sí la tienen.
  Describir lo que esta capa aporta de verdad: las etiquetas de los 54 términos que faltaban y las
  definiciones, que ninguna fuente oficial traduce en ninguna lengua.
- `dcterms:provenance`: contar el ciclo real —borrador asistido por IA, pre-depósito privado del
  2026-07-14, invitación, confirmación de participación, envío a revisión, devolución e
  incorporación— con el alcance cuantificado.
- `dcterms:isReferencedBy` e `isRequiredBy`: enlazar al nuevo dataset 12 y a
  <https://www.cao-crm.eu/index-pt.html>.

### 10.2 Dataset 12 — documentación generada en portugués (nuevo)

**El número es 12 por ser portugués, no por orden de llegada.** El italiano es siempre el 11, llegue
antes o después. Crear:

```
/home/andres/Documentos/GitLab/data-publication/12-documentacion-generada-pt/
```

Copiar el modelo completo del dataset 10 (`10-documentacion-generada-ro/`), que es el mismo tipo de
"data" para el rumano, y adaptarlo:

```bash
D=/home/andres/Documentos/GitLab/data-publication/12-documentacion-generada-pt
G=/home/andres/Documentos/GitHub/CAO_CRM
mkdir -p $D/provenance $D/resources $D/logos $D/fuentes
cp $G/docs/site/index-pt.html $G/docs/site/CAO_CRM-1.0-pt.pdf $D/
cp $G/docs/site/provenance/provenance-pt.{html,ttl} $D/provenance/
cp -r $G/docs/site/resources/. $D/resources/
cp $G/docs/site/logos/*.svg $D/logos/
cp $G/docs/config-pt.properties $G/docs/intro-pt.html $D/fuentes/
```

`fuentes/` lleva solo dos archivos, no tres: el portugués no tiene equivalente de `chrome-ro.yaml`.

Verificar que el conjunto es consultable tal cual se descargue:

```bash
cd $D
grep -rl '/home/andres' . || echo "sin rutas locales: correcto"
grep -o 'href="[^"]*index-pt[^"]*"' provenance/provenance-pt.html   # debe ser ../index-pt.html
python3 -c "
from bs4 import BeautifulSoup; import os
s=BeautifulSoup(open('index-pt.html',encoding='utf-8').read(),'html.parser')
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
- **Autoría:** Echavarría Peláez, Andrés Felipe ; Salgado, Ana.
- **Recuentos reales**, no copiados: fichas por sección y páginas del PDF.
  ```bash
  python3 -c "
  from bs4 import BeautifulSoup
  s=BeautifulSoup(open('$G/docs/site/index-pt.html',encoding='utf-8').read(),'html.parser')
  for d in ('classes','objectproperties','dataproperties','annotationproperties'):
      div=s.find(id=d); print(d, len(div.select('div.entity')) if div else 0)"
  pdfinfo $G/docs/site/CAO_CRM-1.0-pt.pdf | grep -i pages
  ```
- **La sección «Por qué … figura como coautora» hay que reescribirla, no copiarla.** El argumento
  del rumano se apoya en dos hechos acumulados —ni etiquetas oficiales ni paquete de idioma— y para
  el portugués **no se cumple ninguno de los dos**: Widoco y LODE sí traen paquete portugués, y
  CIDOC-CRM publica etiqueta oficial para 76 de los 130 términos. Copiar aquel argumento sería
  sencillamente falso, y lo desmentiría la propia página. Redactar el que corresponde: la revisión
  cubre las 54 etiquetas que ninguna fuente oficial daba, todas las definiciones (que ninguna fuente
  traduce en ninguna lengua) y la prosa de portada, introducción, resumen y agradecimientos.
- Descripciones para humanos en **fr / pt / en** (el 10 las tiene en fr/ro/en).
- `dcterms:language`: `pt`. `dcterms:requires`: el módulo RDF (dataset 02) y la capa portuguesa
  (dataset 08, `10.34847/NKL.D7DCF44B`).
- Adaptar la nota final sobre rutas: decir que los archivos son copia exacta del repositorio y que
  las dos correcciones de ruta ya están resueltas aguas arriba.

### 10.3 Los dos archivos de la colección

- **`data-publication/README.md`** — la colección crece en un "data": actualizar los recuentos, el
  párrafo sobre el estado de 06/07/08, la fila 8 de la tabla y añadir la fila 12.
- **`data-publication/COLLECTION-METADATA-nakala.md`** — el párrafo de estado del principio, el
  campo `Statut`, el recuento en `Licence predominante`, el título de la sección de composición, la
  fila 8 y la nueva fila 12. Cuando existan los DOI reales, sustituir los `[pendiente]` y completar
  los `dcterms:relation`/`isReferencedBy` cruzados.

---

## 11. Si Ana Salgado declina participar

No seguir los pasos anteriores. La ficha del dataset 08 ya prevé este caso y dice qué hay que
decidir; la decisión es de Andrés, no de quien ejecute esto. Plantearle las opciones:

1. **Retirar su nombre** de `dcterms:creator` y `dcterms:rightsHolder` del dataset 08 y decidir si
   el dataset se publica **sin revisión nativa confirmada** —dejándolo dicho con todas las letras en
   `dcterms:provenance` y en la descripción, para que quien lo reutilice sepa exactamente qué está
   reutilizando— o si se retira del depósito.
2. **Buscar otro revisor** lusófono y mantener el dataset privado mientras tanto. En ese caso, el
   documento a enviar sigue siendo `docs/i18n/review/review-pt.md`, y el correo modelo está en
   `docs/i18n/review/emails.md`, sección 3.
3. **No publicar el portugués**: dejar el dataset 08 en pre-depósito privado indefinidamente y el
   idioma fuera del build, como está hoy. Es una opción legítima y no cuesta nada mantenerla.

En cualquiera de los tres casos, **no cablear el portugués en `docs/build.sh`** ni sacarlo del
`.gitignore` sin que Andrés lo diga expresamente.

---

## 12. Al terminar, decirle a Andrés

- Que la confirmación de participación de Ana Salgado quedó registrada, y con qué fecha.
- Qué cambió la revisión, cuantificado (etiquetas, definiciones, entradas del glosario).
- Cuál resultó ser el `ANCHORS["pt"]` observado en la página real.
- Cuántos términos llevan daga en la página portuguesa y cuántos tenían etiqueta oficial de
  CIDOC-CRM, que es lo que distingue este idioma del rumano y el italiano.
- Cualquier `[NOT SURE]` o duda que Ana dejara sin resolver.
- La pregunta pendiente sobre añadirla o no como `dc:contributor` del RDF canónico.
- Que los commits están hechos **en local y sin empujar**, y cuáles son.
- Las acciones que solo puede hacer él en Nakala: sustituir la carga útil del 08 y publicarlo, y
  crear el 12.
