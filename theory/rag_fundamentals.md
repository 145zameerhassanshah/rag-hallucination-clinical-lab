# RAG Fundamentals

## What is RAG?
RAG stands for Retrieval-Augmented Generation.

It combines:
- Retrieval: find relevant external information.
- Generation: use an LLM to answer using that information.

## Why external knowledge?
LLMs may not know:
- private documents
- latest policies
- organization-specific rules
- newly published guidelines
- internal reports

## Pipeline

### 1. Ingest
Bring documents into the system.

### 2. Chunk
Split large documents into smaller pieces for better retrieval.

### 3. Embed
Convert text into vectors that represent semantic meaning.

### 4. Retrieve
Find the chunks most similar to the user's question.

### 5. Generate
Send question + retrieved context to the LLM.

## Two Pipelines

Indexing:
ingest → chunk → embed → store

Query:
question → embed → retrieve → generate

## Key Point
RAG can reduce hallucination risk, but it does not guarantee truth. Bad retrieval or bad interpretation can still produce a poor answer.
