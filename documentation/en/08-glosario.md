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
# Glossary of technical terms used in this project

This section gathers, in alphabetical order, the technical terms that keep recurring in CAO_CRM's
documentation and in the validation repository. There is no need to read it start to finish: it
serves as a quick reference for whenever a term appears, on some other page, without prior
explanation.

- **Class (`owl:Class`).** A category of things, not a concrete thing. In CAO_CRM, `E21_Person` is
  the class "all persons" and `F1_Work` is the class "all works." A class, on its own, carries no
  particular data (no name, no date); it only defines a type. See also **instance** and
  **subclass**.

- **Logical consistency.** An ontology is *consistent* when it contains no internal contradiction
  that would make it impossible to satisfy. A real case from `validation/02-reasoning/` illustrates
  the problem: in an intermediate version of the model, the **reasoner** found that, due to
  badly declared equivalences, a property inherited a text value even though its **range** required
  a URI — something impossible to satisfy. That single contradiction was enough to mark the entire
  ontology as inconsistent, because from a contradiction one can "derive" anything at all.

- **Disjointness (`owl:disjointWith`).** A statement asserting "these two classes can never have an
  instance in common" (for example, declaring `E67_Birth`/birth and `E69_Death`/death disjoint would
  prevent a single event from being recorded as both at once). This project's `ADR-001-disjointness.md`
  explains that CAO_CRM decided to add no disjointness, following the same deliberate choice CIDOC-CRM
  itself makes, preferring to leave that kind of restriction to each project's own judgment.

- **Domain (`rdfs:domain`) and range (`rdfs:range`).** When a **property** connects a thing A to a
  thing B, the domain states what kind of thing A may be, and the range what kind of thing B may be.
  For example, `P3_has_note` ("has note") has domain `E1 CRM Entity` (any entity) and, in the model's
  current version, range `rdfs:Literal` (any simple literal). A key nuance, explained in
  `decisions/fr/problemes-et-solutions.md` (Problem 1): in OWL this is not a validation that rejects faulty data
  (that is SHACL's job), but a rule from which the system *derives* things automatically.

- **Namespace / IRI.** A shared prefix that keeps two projects from accidentally using the same name
  for different things. It is implemented via an **IRI** (a URI/URL variant admitting any language),
  so that every class and property has a unique address, such as
  `http://www.cidoc-crm.org/cidoc-crm/P3_has_note`. When CAO_CRM reuses `P3_has_note`, it does not
  merely copy a name: it reuses that exact identifier, letting any program know unambiguously which
  property is meant.

- **Multilingual label (`rdfs:label`).** The "human-readable" name of a class or property in a given
  language, marked with a language tag (`@en`, `@fr`...); the technical identifier (the IRI) does not
  change with language, only how it is displayed does. `ADR-002-idiomas-LRMoo-CRMdig.md` documents
  that a number of LRMoo/CRMdig terms only have an official label in English, and that the team
  decided not to invent its own translations, so as not to attribute to those consortia content they
  never published.

- **Import (`owl:imports`) vs. merge.** `owl:imports` is a formal statement telling any tool "also
  load this other file to reason properly over this one." `CAO_CRM-1.0.rdf` declares no
  `owl:imports` at all: from CIDOC-CRM/LRMoo/CRMdig as from SKOS, it copies a trimmed version
  directly into its own file, with no formal `owl:imports` (see `imports/README.md`). That is why
  there is a separate **merge** step: `imports/merge.sh` combines CAO_CRM with the complete official
  files into `merged.ttl`, because the trimmed copy does not bring the full axiomatics of those
  ontologies.

- **Instance / individual.** A concrete example of a class, with its own data. If `E21_Person` is the
  class "all persons," an instance of it would be the real person "Stendhal." In OWL, "instance" and
  "individual" are synonyms.

- **Literal (`rdfs:Literal`) vs. XSD type.** A literal is any simple value (text, number, date) with
  no identity of its own. `rdfs:Literal` is the broadest possible category of literals; **XSD** types
  (from the XML Schema standard), such as `xsd:string` or `xsd:decimal`, are stricter subcategories.
  `decisions/fr/problemes-et-solutions.md` (Problem 1) documents why CAO_CRM chose `rdfs:Literal` for `P3_has_note`: it is the same convention
  the official CIDOC-CRM file uses for equivalent properties such as `P90_has_value`, even though the
  latter conceptually represents "a number."

- **Scope note.** The official paragraph defining a class or property, written by the relevant
  consortium, explaining what it means and what it does not cover. For example, the *scope note* for
  `E59 Primitive Value` in CIDOC-CRM states, verbatim, that *"the instances of E59 Primitive Value
  and its subclasses are not considered elements of the universe of discourse the CIDOC CRM aims to
  define and analyse"*: values such as numbers or text are not treated as "things" in the described
  world, but as the technical way of representing a simple datum. This is the kind of source cited
  verbatim whenever a doubt arises about how to treat a reused piece, as this project's ADRs show.

- **Ontology.** A formal schema defining which "kinds of things" exist in a knowledge domain (work,
  edition, physical copy, digital file, person, creation event...) and how they relate, so that both
  a person and a program can interpret it unambiguously. CAO_CRM is this repository's ontology: it
  invents no classes or properties of its own, but selects and assembles pieces from CIDOC-CRM,
  LRMoo, and CRMdig.

- **Data property (`owl:DatatypeProperty`).** A type of **property** connecting an **instance** to a
  **literal** (text, number, date), not to another instance. For example, "this work `has title`
  'Le Rouge et le Noir'": the title is just text. `P3_has_note` is another example: it connects any
  entity to a note in free text.

- **Object property (`owl:ObjectProperty`).** A type of **property** connecting an **instance** to
  **another instance**, that is, two entities each with its own identity. For example, "this work
  `was created by` this person": both are entities, unlike a literal.

- **Reasoner.** A program that applies OWL's logical rules to an ontology to check that it makes
  mathematical sense, derive implicit information, and detect contradictions. In this repository the
  reasoner used is HermiT, invoked via ROBOT (see `validation/02-reasoning/README.md`); its main
  output is whether the ontology is **consistent** and whether it has any unsatisfiable class (a
  class that could never possibly have any instance).

- **RDF/XML vs. Turtle (serialization formats).** The same set of RDF data can be written in
  different text formats, or *serializations*, without changing its meaning. RDF/XML is the format
  based on XML tags — the one `CAO_CRM-1.0.rdf` uses — and tends to be more verbose. Turtle (`.ttl`
  extension) is more compact and readable, used for instance in `imports/module/`. Converting from
  one to the other changes no class or relation, only how the content is written.

- **SHACL.** A language (Shapes Constraint Language) for defining validation rules that do actually
  reject data failing to meet them, unlike OWL's domain and range. For example, a rule could require
  every `E12_Production` instance to have exactly one associated date. In this repository,
  `validation/03-shacl/` applies such rules (via pySHACL) to `test-data/`, as a layer complementary
  to the reasoner's **logical consistency** check.

- **SPARQL.** The query language for querying RDF data, playing a role equivalent to SQL for
  relational databases. It is used here in two forms, aligned with the **competency questions** (the
  use cases the ontology should be able to answer): `ASK` queries (yes/no, in `sparql/ask/`) and
  `SELECT` queries (result lists, in `sparql/select/`).

- **Subclass (`rdfs:subClassOf`).** A relation between two classes meaning "everything belonging to
  this class also automatically belongs to this other, more general class." If `E21_Person` were
  declared a subclass of `E39_Actor`, the reasoner would infer that any person is also an
  `E39_Actor`, without needing to declare it separately for every individual.

Other concepts mentioned in this documentation — such as the AMIS project, the ROBOT tool, or the
ADRs (decision records) themselves — are explained in context, in the corresponding sections of this
folder, and are not repeated here since they are not technical terms specific to OWL/RDF.
