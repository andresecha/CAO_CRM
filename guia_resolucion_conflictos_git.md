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

# Guía para resolver conflictos de Git priorizando la versión local

Dado que tu rama local (`main`) y la remota (`origin/main`) han divergido, al intentar unirlas (hacer un `git pull` o `git merge`) podrías encontrarte con conflictos en algunos documentos. 

Como solicitaste, aquí tienes las opciones exactas para que puedas tomar la decisión de cómo proceder y resolver los conflictos en favor de tu repositorio local sin que yo ejecute los comandos por ti.

## Opción 1: Resolver TODOS los conflictos automáticamente en favor de tu versión local al momento de unir

Si quieres hacer el `pull` y decirle a Git que, ante cualquier conflicto, conserve siempre tus cambios locales automáticamente, ejecuta:

```bash
git pull origin main -X ours
```
*(Si prefieres hacerlo con `merge` en lugar de `pull`: `git merge origin/main -X ours`)*

## Opción 2: Hacer la unión normal y decidir archivo por archivo (o carpeta por carpeta)

Si prefieres hacer la unión normal y luego, solo si hay conflictos, decirle a Git manualmente qué archivos deben mantener tu versión local:

1. **Inicia la unión (puede que marque conflictos):**
   ```bash
   git pull origin main
   ```

2. **Para cada documento o carpeta con conflicto donde quieras mantener tu versión local:**
   ```bash
   git checkout --ours -- <ruta/al/documento_o_carpeta>
   ```
   *Ejemplo: `git checkout --ours -- README.md` o `git checkout --ours -- docs/`*

3. **Marca esos archivos como resueltos:**
   ```bash
   git add <ruta/al/documento_o_carpeta>
   ```

4. **Finaliza la unión:**
   ```bash
   git commit
   ```
   *(Esto abrirá tu editor por defecto para confirmar el mensaje de merge, simplemente guárdalo y ciérralo).*

---
**Nota:** Actualmente, al hacer `git status`, no estás en medio de un proceso de fusión (merge). Tienes 3 commits locales que no están en el remoto, y el remoto tiene 1 commit que no tienes tú. Por lo tanto, tendrás que iniciar el `pull` o `merge` usando una de las opciones anteriores.
