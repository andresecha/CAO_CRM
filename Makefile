ONTOLOGY := ontology/CAO_CRM-1.0.rdf
MERGED   := imports/merged.ttl

.PHONY: validate syntax imports reason metrics conformance cq shacl quality metadata fair watermark watermark-fix docs clean

validate: syntax imports reason metrics conformance metadata quality shacl cq fair watermark
	@echo "All validation categories passed, including shacl/cq (real test-data/stendhal-le-rouge-et-le-noir.ttl, see competency-questions/) and fair (real FOOPS! run, see validation/08-fair/README.md). 'docs' remains a separate target (needs network access for Widoco/Chrome, see README.md)."

syntax:
	bash validation/01-syntax/check.sh $(ONTOLOGY)

imports:
	bash imports/fetch.sh
	bash imports/merge.sh $(ONTOLOGY) $(MERGED)

reason: imports
	bash validation/02-reasoning/check.sh $(MERGED)

metrics:
	bash validation/05-metrics/check.sh $(ONTOLOGY)

conformance: imports
	bash validation/06-conformance/check.sh $(MERGED)

cq:
	bash scripts/run-competency-questions.sh

shacl:
	bash validation/03-shacl/check.sh

quality:
	bash validation/04-quality/check.sh $(ONTOLOGY)

metadata:
	bash validation/07-metadata/check.sh $(ONTOLOGY)

fair:
	bash validation/08-fair/check.sh $(ONTOLOGY)

watermark:
	bash scripts/check-watermark.sh

watermark-fix:
	bash scripts/check-watermark.sh --fix

docs:
	bash docs/build.sh $(ONTOLOGY)

clean:
	rm -rf imports/vendor imports/merged.ttl docs/site validation/*/out
