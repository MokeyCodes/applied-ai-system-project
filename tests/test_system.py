from src.retriever import retrieve_relevant_docs
from src.validator import validate_response

def test_validation_with_sources():
    result = validate_response("Valid answer", ["doc1.txt"])
    assert result["confidence"] >= 0.7

def test_validation_without_sources():
    result = validate_response("I don't have enough context to answer that.", [])
    assert result["confidence"] == 0.2

def test_retrieval_returns_list():
    docs = retrieve_relevant_docs("test")
    assert isinstance(docs, list)