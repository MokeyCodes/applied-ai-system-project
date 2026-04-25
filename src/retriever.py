from pathlib import Path

DATA_DIR = Path("data/knowledge_base")

def load_documents():
    docs = []
    for path in DATA_DIR.glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        docs.append({"source": path.name, "text": text})
    return docs

def retrieve_relevant_docs(query: str, top_k: int = 2):
    docs = load_documents()
    query_terms = set(query.lower().split())

    scored = []
    for doc in docs:
        doc_terms = set(doc["text"].lower().split())
        overlap = len(query_terms.intersection(doc_terms))
        scored.append((overlap, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored[:top_k] if score > 0]