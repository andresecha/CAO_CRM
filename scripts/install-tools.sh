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
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== Java (needed for ROBOT, Jena riot) =="
java -version

echo "== ROBOT (OWL CLI: reasoning, reports, diff) =="
mkdir -p .tools
if [ ! -f .tools/robot.jar ]; then
  # -f (not just -L): without it curl happily writes an HTTP error page into the
  # target file and exits 0, so the failure only surfaces much later as a corrupt
  # artifact -- exactly how the Jena download below failed silently in CI.
  curl -fL -o .tools/robot.jar https://github.com/ontodev/robot/releases/latest/download/robot.jar
fi
cat > .tools/robot <<'EOF'
#!/usr/bin/env bash
exec java -jar "$(dirname "$0")/robot.jar" "$@"
EOF
chmod +x .tools/robot
.tools/robot --version

echo "== Apache Jena riot (RDF syntax + SHACL CLI) =="
if command -v riot >/dev/null 2>&1; then
  echo "riot already on PATH: $(command -v riot)"
elif [ -x .tools/jena/bin/riot ]; then
  echo "riot already installed at .tools/jena/bin/riot"
else
  # Pinned, not "latest": the validation reports committed under validation/*/out/
  # were produced with this exact riot, and a syntax/SHACL checker is precisely the
  # kind of tool whose output must not drift underneath a published result.
  JENA_VERSION="6.1.0"

  # Two mirrors, tried in order, because they serve different purposes:
  #   - dlcdn.apache.org carries ONLY the current release. It dropped 6.1.0 the
  #     moment 6.2.0 shipped, which broke this script in CI on 2026-09-01: curl
  #     without -f wrote Apache's 404 page into jena.tar.gz and tar then died with
  #     the entirely misleading "gzip: stdin: not in gzip format".
  #   - archive.apache.org keeps every past release permanently, so it is what
  #     actually makes a pinned version reproducible. It is the fallback rather
  #     than the primary only because Apache asks that the CDN absorb the traffic
  #     for whatever release is current.
  # -f on both, so a mirror that answers with an error page fails here, loudly,
  # instead of three lines down as a corrupt archive.
  echo "riot not found — downloading Apache Jena $JENA_VERSION into .tools/ (no sudo needed)"
  curl -fL -o .tools/jena.tar.gz "https://dlcdn.apache.org/jena/binaries/apache-jena-${JENA_VERSION}.tar.gz" \
    || {
      echo "  not on dlcdn (it only mirrors the current release) — falling back to archive.apache.org"
      curl -fL -o .tools/jena.tar.gz "https://archive.apache.org/dist/jena/binaries/apache-jena-${JENA_VERSION}.tar.gz"
    }
  rm -rf .tools/jena "apache-jena-${JENA_VERSION}"
  tar -xzf .tools/jena.tar.gz -C .tools
  mv ".tools/apache-jena-${JENA_VERSION}" .tools/jena
  rm .tools/jena.tar.gz
  echo "Installed. Add to PATH for this shell with: export PATH=\"$(pwd)/.tools/jena/bin:\$PATH\""
  echo "(all check.sh scripts also fall back to .tools/jena/bin automatically if riot isn't on PATH)"
fi

echo "== raptor/rapper (RDF/XML strict syntax check) =="
if ! command -v rapper >/dev/null 2>&1; then
  echo "rapper not found on PATH. Install raptor2-utils (e.g. apt install raptor2-utils)."
fi

echo "== Python packages =="
pip install -r requirements.txt

echo "Done. Re-run any 'not found' installs manually, then re-run this script to confirm."
