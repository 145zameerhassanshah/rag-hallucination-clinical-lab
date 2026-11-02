from pathlib import Path

base = Path(__file__).resolve().parents[1]

files = {
    "NORMAL QUESTION — WITHOUT CONTEXT":
        base / "experiment" / "response_without_context.txt",

    "NORMAL QUESTION — WITH CONTEXT":
        base / "experiment" / "response_with_context.txt",

    "FALSE-PREMISE TEST — WITHOUT CONTEXT":
        base / "experiment" / "hallucination_response_without_context.txt",

    "FALSE-PREMISE TEST — WITH CONTEXT":
        base / "experiment" / "hallucination_response_with_context.txt",
}

print("=" * 90)
print("RAG VS HALLUCINATION — FOUR-WAY COMPARISON LAB")
print("=" * 90)

for title, path in files.items():
    print(f"\n{title}\n")
    print("-" * 90)

    if path.exists():
        content = path.read_text(encoding="utf-8").strip()
        print(content if content else "[File is empty]")
    else:
        print(f"[Missing file: {path.name}]")

    print()

print("=" * 90)
print("ANALYSIS CHECKLIST")
print("=" * 90)
print("- factual accuracy")
print("- fabrication")
print("- false-premise acceptance")
print("- unsupported certainty")
print("- source grounding")
print("- traceability")
print("- source dependence")
print("- refusal to invent unsupported information")