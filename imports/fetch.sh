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
cd "$(dirname "$0")"
mkdir -p vendor
: > vendor/CHECKSUMS.txt

fetch() {
  local name="$1" url="$2" out="vendor/$3"
  if [ -z "$url" ]; then
    echo "SKIP $name: no URL configured yet — set it in fetch.sh"
    return
  fi
  curl -L -o "$out" "$url"
  sha256sum "$out" >> vendor/CHECKSUMS.txt
  echo "fetched $name -> $out"
}

CIDOC_CRM_URL="https://cidoc-crm.org/rdfs/7.1.3/CIDOC_CRM_v7.1.3.rdfs"
LRMOO_URL="http://www.cidoc-crm.org/extensions/lrmoo/rdfs/1.1.1/LRMoo_v1.1.1.rdf"
CRMDIG_URL="http://www.cidoc-crm.org/extensions/crmdig/rdfs/5.0/CRMdig_v5.0.rdf"
SKOS_URL="https://www.w3.org/2004/02/skos/core.rdf"

fetch "CIDOC-CRM 7.1.3" "$CIDOC_CRM_URL" "cidoc-crm-7.1.3.rdf"
fetch "LRMoo 1.1.1"     "$LRMOO_URL"     "lrmoo-1.1.1.rdf"
fetch "CRMdig 5.0"      "$CRMDIG_URL"    "crmdig-5.0.rdf"
fetch "SKOS core"       "$SKOS_URL"      "skos.rdf"
