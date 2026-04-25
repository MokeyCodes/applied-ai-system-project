from pathlib import Path

DATA_DIR = Path("data/knowledge_base")

STOPWORDS = {
    "what", "is", "the", "a", "an", "of", "how", "can", "be",
    "to", "and", "in", "for", "it", "this", "that", "are"
}

def load_documents():
    docs = []
    for path in DATA_DIR.glob("*.txt"):
        text = path.read_text(encoding="utf-8")
        docs.append({"source": path.name, "text": text})
    return docs

def retrieve_relevant_docs(query: str, top_k: int = 2):
    docs = load_documents()
    query_terms = {
        word.strip(".,?!").lower()
        for word in query.split()
        if word.strip(".,?!").lower() not in STOPWORDS
    }

    scored = []
    for doc in docs:
        doc_terms = {
            word.strip(".,?!").lower()
            for word in doc["text"].split()
        }
        overlap = len(query_terms.intersection(doc_terms))
        scored.append((overlap, doc))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored[:top_k] if score > 0]