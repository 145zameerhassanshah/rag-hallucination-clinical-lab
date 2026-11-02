# RAG vs Hallucination Clinical Guideline Lab

A learning-focused mini project that demonstrates why Retrieval-Augmented Generation (RAG) is useful for reducing unsupported LLM answers.

## Goal
Compare an LLM's answers to guideline-specific questions:
1. without external guideline context
2. with supplied guideline context
3. compare accuracy, uncertainty, grounding, and fabrication

This project is educational only and is not for clinical decision-making.

## RAG Pipeline
INGEST → CHUNK → EMBED → RETRIEVE → GENERATE

Today we manually simulate the retrieval stage by supplying relevant guideline context. Later this repo can be extended with real chunking, embeddings, vector search, and automatic retrieval.

## Structure
- theory/rag_fundamentals.md
- theory/hallucination_causes.md
- experiment/prompt_without_context.txt
- experiment/response_without_context.txt
- experiment/prompt_with_context.txt
- experiment/response_with_context.txt
- experiment/comparison.md
- app/compare_responses.py
- sources/guideline_reference.md
- SUBMISSION_NOTES.md

## Run
After pasting the actual LLM responses into the two response files:

```bash
python app/compare_responses.py
```

## Future Expansion
- sentence-transformers
- cosine similarity
- FAISS
- Chroma
- automatic retrieval
- source citations
- RAG evaluation
- FastAPI
- Docker
