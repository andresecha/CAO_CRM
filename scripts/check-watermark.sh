#!/usr/bin/env bash
##
## CAO_CRM (Corpus Author Ontology CRM)
## Copyright (c) 2026 Andres Echavarria Pelaez
## Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)
## Encoding carried out under the scientific direction and support of Fatiha Idmhand
##
## This file is part of the CAO_CRM publication package, licensed under the
## Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
## License (CC BY-NC-SA 4.0). To view a copy of this license, visit
## https://creativecommons.org/licenses/by-nc-sa/4.0/
##
## Checks that every hand- or agent-authored source file in this repository carries the
## copyright/attribution header above. Exists because that header has gone missing twice
## already, silently: once when files were copied in from an external working directory,
## once when new .rq files were created without it, and once when ontology/CAO_CRM-1.0.rdf
## was regenerated via ROBOT/rdflib (tools that don't preserve comments -- see
## scripts/reserialize-ontology.py for how CAO_CRM-1.0.ttl/.nt cope with that).
##
## Run: bash scripts/check-watermark.sh            (report only, exit 1 if anything missing)
##      bash scripts/check-watermark.sh --fix       (also insert the missing header)
##
set -euo pipefail
cd "$(dirname "$0")/.."

FIX=0
[ "${1:-}" = "--fix" ] && FIX=1

# Deliberately NOT just "Fatiha Idmhand": that name also appears as ordinary metadata
# content (dcterms:contributor) inside ontology/CAO_CRM-1.0.ttl/.nt, which let a missing
# header silently pass this check once already (2026-07-11) after `make docs` regenerated
# those files without it. This phrase is unique to the header comment itself.
MARK="This file is part of the CAO_CRM publication package"

# File sets this project actually authors by hand (or has an agent author for it),
# where the header is expected. Deliberately excludes:
#  - imports/vendor/*        third-party CIDOC-CRM/LRMoo/CRMdig files, must NOT be touched
#  - imports/merged*.ttl     merge *output*, not authored source
#  - imports/module-terms.txt, docs/i18n/CAO_CRM-1.0-i18n.ttl, requirements.txt
#                            pre-existing exceptions: plain data/dependency lists with
#                            their own descriptive header instead, not this copyright block
#  - */out/*, docs/site/*, docs/.tools/*, .tools/*, __pycache__/*
#                            generated/build output, regenerated from real source anyway
#  - ontology/CAO_CRM-1.0.jsonld
#                            JSON has no comment syntax at all
#  - ontology/CAO_CRM-2.0.rdf, ontology/CAO_CRM-2.5.rdf (private working mirror only)
#                            frozen historical intermediate snapshots, same precedent as
#                            imports/merged-2.5.ttl -- not touched retroactively
FILES=$(find . \
  \( -path ./.venv -o -path ./.git -o -path ./.tools -o -path ./docs/.tools \
     -o -path ./docs/site -o -path ./imports/vendor \
     -o -name __pycache__ -o -name out \) -prune -o \
  -type f \( -name '*.md' -o -name '*.sh' -o -name '*.py' -o -name '*.rq' \
             -o -name '*.rdf' -o -name '*.ttl' -o -name '*.nt' \) -print \
  | grep -v -e '/imports/module-terms\.txt$' -e '/docs/i18n/CAO_CRM-1\.0-i18n\.ttl$' \
            -e '/imports/merged.*\.ttl$' -e '/ontology/CAO_CRM-2\.[05]\.rdf$' \
  | sort)

MISSING=()
while IFS= read -r f; do
  [ -z "$f" ] && continue
  if ! grep -q "$MARK" "$f" 2>/dev/null; then
    MISSING+=("$f")
  fi
done <<< "$FILES"

if [ "${#MISSING[@]}" -eq 0 ]; then
  echo "PASS: all $(echo "$FILES" | wc -l) checked files carry the watermark."
  exit 0
fi

echo "Missing watermark in ${#MISSING[@]} file(s):"
printf '  %s\n' "${MISSING[@]}"

if [ "$FIX" -eq 0 ]; then
  echo "Run 'bash scripts/check-watermark.sh --fix' to insert it automatically, or 'make watermark-fix'."
  exit 1
fi

echo "--- fixing ---"
for f in "${MISSING[@]}"; do
  case "$f" in
    *.md)
      { printf '<!--\nCAO_CRM (Corpus Author Ontology CRM)\nCopyright (c) 2026 Andres Echavarria Pelaez\nConsortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)\nEncoding carried out under the scientific direction and support of Fatiha Idmhand\n\nThis file is part of the CAO_CRM publication package, licensed under the\nCreative Commons Attribution-NonCommercial-ShareAlike 4.0 International\nLicense (CC BY-NC-SA 4.0). To view a copy of this license, visit\nhttps://creativecommons.org/licenses/by-nc-sa/4.0/\n-->\n\n'; cat "$f"; } > "$f.tmp" && mv "$f.tmp" "$f"
      ;;
    *.sh|*.py)
      { printf '##\n## CAO_CRM (Corpus Author Ontology CRM)\n## Copyright (c) 2026 Andres Echavarria Pelaez\n## Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)\n## Encoding carried out under the scientific direction and support of Fatiha Idmhand\n##\n## This file is part of the CAO_CRM publication package, licensed under the\n## Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International\n## License (CC BY-NC-SA 4.0). To view a copy of this license, visit\n## https://creativecommons.org/licenses/by-nc-sa/4.0/\n##\n'; cat "$f"; } > "$f.tmp" && mv "$f.tmp" "$f"
      ;;
    *.rq|*.ttl|*.nt)
      { printf '# CAO_CRM (Corpus Author Ontology CRM)\n# Copyright (c) 2026 Andres Echavarria Pelaez\n# Consortium Huma-Num ARIANE -- AMIS project (Advanced Metadata Intelligent System)\n# Encoding carried out under the scientific direction and support of Fatiha Idmhand\n#\n# This file is part of the CAO_CRM publication package, licensed under the\n# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International\n# License (CC BY-NC-SA 4.0). To view a copy of this license, visit\n# https://creativecommons.org/licenses/by-nc-sa/4.0/\n#\n\n'; cat "$f"; } > "$f.tmp" && mv "$f.tmp" "$f"
      ;;
    *.rdf)
      # XML comments forbid a literal "--" anywhere inside them (XML spec) -- use an
      # em dash here instead of the "--" used in every other file's header, or ROBOT/
      # rdflib's XML parser fails with a cryptic "not well-formed (invalid token)".
      python3 - "$f" <<'PYEOF'
import sys
path = sys.argv[1]
s = open(path, encoding="utf-8").read()
header = '''<!--
CAO_CRM (Corpus Author Ontology CRM)
Copyright (c) 2026 Andres Echavarria Pelaez
Consortium Huma-Num ARIANE — AMIS project (Advanced Metadata Intelligent System)
Encoding carried out under the scientific direction and support of Fatiha Idmhand

This file is part of the CAO_CRM publication package, licensed under the
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
License (CC BY-NC-SA 4.0). To view a copy of this license, visit
https://creativecommons.org/licenses/by-nc-sa/4.0/
-->
'''
marker = '<?xml version="1.0" encoding="utf-8"?>\n'
if s.startswith(marker):
    s = marker + header + s[len(marker):]
else:
    s = header + s
open(path, "w", encoding="utf-8").write(s)
PYEOF
      ;;
    *)
      echo "  SKIP (unknown extension, fix by hand): $f"
      continue
      ;;
  esac
  echo "  fixed: $f"
done
echo "done -- re-run without --fix to confirm."
