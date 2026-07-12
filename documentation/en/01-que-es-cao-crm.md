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
# What is CAO_CRM, and what is it for?

## The problem: a literary text is not a single thing

When a literature researcher sets out to describe a work — a novel, a collection of poems, an author's correspondence — they quickly discover that "describing it" can mean very different things. One can speak of the work as an idea or intellectual project (what Flaubert imagined before writing a single line of *Madame Bovary*), as a text with several versions (the manuscript, the variants, the corrected edition), as a physical object kept in a library, or as a digital file, whether produced by digitization or born directly in electronic format. These are not four ways of saying the same thing: each follows a distinct logic, involves different actors (author, publisher, librarian, archivist, technical team), and requires its own vocabulary.

The Ariane consortium's paper documenting CAO_CRM sums up the question this way: *"comment, dès lors, représenter, au sein d'un cadre sémantique cohérent, une entité qui relève simultanément de la création intellectuelle, de la matérialité documentaire, de l'herméneutique littéraire et de l'environnement numérique?"* — that is, how to represent, within a coherent framework of meaning, something that is at once intellectual creation, physical object, subject of literary interpretation, and digital resource, without reducing it to just one of these dimensions. That is the problem CAO_CRM (Corpus Author Ontology CRM) tries to solve: to offer a unified model — what is called, in this field, an **ontology**, a formal schema defining which "kinds of things" exist in a domain (work, edition, physical copy, digital file, person, creation event...) and how they relate to one another — capable of accompanying a literary corpus throughout its entire life cycle.

Without such a shared framework, each professional community describes the same object with its own categories: librarians, archivists, philologists, and textual geneticists each privilege different aspects. The result, the paper points out, is a fragmented description in which metadata — the data describing a resource, such as its author, date, or format — ends up incomplete and hard to cross-reference automatically.

## AMIS: an AI assistant that needed a conceptual "brain"

CAO_CRM was not born as an isolated theoretical exercise, but as the answer to a concrete need of the European project **AMIS** (Advanced Metadata Intelligent System), developed within Ariane with European funding (OSCARS, Open Science Clusters' Action for Research & Society). AMIS is a web application that helps create and enrich metadata for digital textual resources (PDF, images, XML/TEI) in a semi-assisted way: rather than leaving the researcher to fill in every field by hand — a task the paper calls "chronophage" (time-consuming) and idiosyncratic — an AI-backed "robot" (vision models that read a scanned page, and large language models, or LLMs) analyzes the document and proposes the data, which the researcher validates, corrects, or rejects.

During AMIS's development, a central obstacle emerged: language models reasonably well spot data such as the author, title, or date, but on their own they have no conceptual framework letting them tell at which "level" each piece of data belongs. Does this title describe the work in the abstract, this particular edition, or the PDF file currently being consulted? As the paper itself puts it, *"il lui manquait une base de connaissances qui lui permette d'organiser ces données"* — that is, the system lacked a knowledge base to organize that data. CAO_CRM is precisely that base: the conceptual structure indicating which entities exist (work, edition, physical copy, digital object, and the processes linking them) and which information belongs to each. Thanks to it, AMIS organizes what has been extracted coherently and uses the same structure to guide enrichment through RAG (Retrieval-Augmented Generation: an LLM that queries external sources to complete information).

## Why build a dedicated model instead of reusing an existing one

Before creating a new ontology, the Ariane consortium did the opposite: it systematically searched for existing resources that could, with reasonable adjustments, cover AMIS's needs, through an inventory of some forty ontologies from the art and culture domain. The result was telling: only nine specifically concerned the field of texts and fiction, and each covered only part of the problem — some favored bibliographic metadata, others the historical entities mentioned in texts, others still the linguistic or literary-genre dimensions. None, the paper concludes, allowed the whole literary process to be represented continuously, from the genetic traces of creation to the forms of dissemination and their digital reuses.

Ariane was aware of the risk of adding yet another ontology to an already scattered landscape; that is why the consortium did not start from scratch: it decided to build on international standards already well established in cultural heritage (covered in another section of this documentation) rather than invent a new vocabulary. But, having evaluated them, it concluded that none of them, even combined, fully resolved AMIS's needs: some were too general and did not precisely distinguish the work, its editions, and its digital objects; others described the technical aspects of digitization well but left in the shadows the scholarly work — that of a critical editor, for instance — of deciding which variants to keep. Hence the decision to build CAO_CRM: not as an alternative ignoring what already exists, but as an original articulation of these standards, completed where necessary, to accompany a literary corpus, coherently, from idea to digital file.

## In summary

CAO_CRM is an attempt to give the digital humanities something they did not yet have in a unified way: a common, formal language to describe literary corpora in all their dimensions — intellectual, material, editorial, and digital — without losing the precision that philological research demands, nor the ability of a system like AMIS to process that description coherently. It is not an end in itself, but a conceptual infrastructure supporting both the expert work of researchers and the assistance artificial intelligence can offer them.
