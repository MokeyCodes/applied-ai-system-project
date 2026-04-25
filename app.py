from dotenv import load_dotenv
load_dotenv()
from src.retriever import retrieve_relevant_docs
from src.generator import generate_answer
from src.validator import validate_response
from src.logger_utils import log_run

def main():
    print("Applied AI Study Assistant")
    print("Ask a question about the documents in /data/knowledge_base")
    question = input("\nQuestion: ").strip()

    docs = retrieve_relevant_docs(question)
    result = generate_answer(question, docs)
    validation = validate_response(result["answer"], result["sources"])
    log_run(question, result, validation)

    print("\nAnswer:")
    print(result["answer"])
    print(f"\nSources: {', '.join(result['sources']) if result['sources'] else 'None'}")
    print(f"Confidence: {validation['confidence']}")
    print(f"Validation passed: {validation['passed']}")
    if validation["issues"]:
        print("Issues:")
        for issue in validation["issues"]:
            print(f"- {issue}")

if __name__ == "__main__":
    main()