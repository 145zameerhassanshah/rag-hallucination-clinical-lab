# RAG Grounding Comparison

## Main Guideline Question Comparison

| Question | Without Context | With Context | Ground Truth | Observation |
|---|---|---|---|---|
| Clinic target under 80 | below 140/90 mmHg | below 140/90 mmHg | below 140/90 mmHg | Both answers were correct, but the with-context response was explicitly grounded in supplied evidence. |
| Clinic target age 80+ | below 150/90 mmHg | below 150/90 mmHg | below 150/90 mmHg | Both answers were correct; with-context response provided supporting text. |
| HBPM/ABPM under 80 | below 135/85 mmHg | below 135/85 mmHg | below 135/85 mmHg | No-context answer relied on internal model knowledge; with-context answer was source-supported. |
| HBPM/ABPM age 80+ | below 145/85 mmHg | below 145/85 mmHg | below 145/85 mmHg | Both were correct, but context improved traceability and grounding. |

## Hallucination / False-Premise Test

### Without Context
The model did not blindly accept the false premise. It stated that it did not believe NICE NG136 gives a separate target specifically for age 65. It correctly placed age 65 in the broader under-80 category and avoided inventing an exact quotation.

### With Context
The model explicitly stated:

"Not stated in the provided guideline context."

It correctly identified that the supplied context does not define a special age-65 blood-pressure target and only supports the broader under-80 recommendations.

## Key Findings

1. The LLM can sometimes answer correctly from internal knowledge without external context.
2. Correctness alone is not enough; without source context, the answer is harder to verify.
3. Supplying guideline context improves grounding, traceability, and confidence.
4. The false-premise test showed that good prompting can reduce fabrication.
5. RAG is useful not only for correcting wrong answers, but also for grounding answers in external evidence.
6. RAG does not completely eliminate hallucination; retrieval quality and prompt instructions still matter.

## Final Conclusion

This experiment demonstrated the core idea behind Retrieval-Augmented Generation. Without external context, the LLM relied on its internal knowledge and expressed uncertainty about the exact guideline wording. With guideline context supplied, the model produced answers that were directly supported by evidence and could identify the exact supporting statements.

In the false-premise test, the model avoided fabricating a special age-65 recommendation. The grounded version was even more reliable because it could explicitly state that the requested information was not present in the supplied context.

The experiment therefore shows that RAG improves source grounding, transparency, and verifiability. It is especially valuable when working with private, recent, domain-specific, or high-stakes information.