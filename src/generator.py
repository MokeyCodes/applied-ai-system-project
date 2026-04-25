def generate_answer(question: str, retrieved_docs):
    if not retrieved_docs:
        return {
            "answer": "I don't have enough context to answer that.",
            "sources": [],
        }

    question_lower = question.lower()

    matched_chunks = []
    for doc in retrieved_docs:
        sentences = doc["text"].split(".")
        for sentence in sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            overlap = sum(
                1 for word in question_lower.split()
                if word in sentence.lower()
            )
            if overlap > 0:
                matched_chunks.append((overlap, sentence, doc["source"]))

    matched_chunks.sort(key=lambda x: x[0], reverse=True)

    if matched_chunks:
        best_sentences = matched_chunks[:2]
        answer_parts = [item[1] for item in best_sentences]
        used_sources = list(dict.fromkeys(item[2] for item in best_sentences))
        answer = ". ".join(answer_parts).strip()
        if not answer.endswith("."):
            answer += "."
    else:
        return {
        "answer": "I don't have enough relevant context to answer this question.",
        "sources": [],
    }
    answer += f" Sources used: {', '.join(used_sources)}."

    return {
        "answer": answer,
        "sources": used_sources,
    }