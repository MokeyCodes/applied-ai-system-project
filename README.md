# Applied AI Study Assistant

## Project Overview

This project extends my Week 7 **Music Recommender System** into a more advanced applied AI system. The original project focused on building a scoring-based recommendation engine using structured data and explaining its behavior through a model card. It emphasized algorithmic reasoning, ranking logic, and evaluation of system bias.

In this final project, I expanded those ideas into a **retrieval-augmented AI assistant** that answers user questions using a document knowledge base. The system now integrates retrieval, answer generation, validation, and logging to create a more complete and reliable AI workflow.

---

## What This Project Does

The Applied AI Study Assistant allows users to ask questions about a set of documents. Instead of generating answers blindly, the system:

1. Retrieves relevant documents from a knowledge base
2. Extracts the most relevant information
3. Generates a grounded answer using retrieved content
4. Validates the response and assigns a confidence score
5. Logs the interaction for debugging and evaluation

This ensures that answers are **traceable, explainable, and more reliable**.

---

## Key Features

* Retrieval-Augmented Generation (RAG)
* Source-aware answers (shows which documents were used)
* Confidence scoring system
* Validation checks for reliability
* Logging of all interactions
* Automated tests for core components

---

## System Architecture

The system follows this pipeline:

**User Input → Retriever → Generator → Validator → Output + Logs**

* **Retriever**: Finds relevant documents from the knowledge base
* **Generator**: Constructs an answer using retrieved content
* **Validator**: Evaluates confidence and detects issues
* **Logger**: Records system behavior for debugging and analysis

See diagram in `/assets/system-diagram.png`.

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/MokeyCodes/applied-ai-system-project
cd applied-ai-system-project
```

2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python app.py
```

---

## Sample Interactions

### Example 1

**Input:** What is prompt engineering?
**Output:** Prompt engineering is the practice of designing inputs that guide large language models toward better outputs.
**Sources:** doc1.txt
**Confidence:** 0.7

### Example 2

**Input:** What is retrieval-augmented generation?
**Output:** Retrieval-augmented generation improves answer quality by using relevant external context before generating responses.
**Sources:** doc2.txt
**Confidence:** 0.7

### Example 3

**Input:** How can AI systems be more reliable?
**Output:** AI systems can be improved through testing, validation, logging, and guardrails.
**Sources:** doc3.txt
**Confidence:** 0.7

(Screenshots of these examples are included in the `/assets` folder.)

---

## Design Decisions

I chose a retrieval-based architecture to ensure that the AI system produces grounded and explainable outputs. Compared to my original recommender system, which relied on scoring logic, this project introduces external context as a key factor in decision-making.

I also implemented a simple keyword-based retrieval system to keep the system lightweight and reproducible. While more advanced approaches like embeddings could improve accuracy, this design prioritizes clarity and ease of understanding.

---

## Reliability and Testing

To ensure reliability, I implemented:

* Validation checks for missing sources
* Confidence scoring based on retrieved evidence
* Automated tests using `pytest`

### Testing Summary

* All core tests passed successfully
* System performs well on in-scope questions
* Performance drops when relevant context is missing

---

## Limitations

* Retrieval is keyword-based, not semantic
* Limited knowledge base size
* Cannot answer questions outside provided documents

---

## Reflection

This project showed me that building a useful AI system goes beyond generating good responses. The most important factors were:

* Providing relevant context (retrieval)
* Verifying outputs (validation)
* Making the system transparent (sources + logging)

One key insight was that even simple retrieval dramatically improves answer quality compared to raw generation. However, I also saw how easily systems fail when the context is incomplete, highlighting the importance of data coverage.

---

## Ethical Considerations

This system could be misused if users assume it is always correct. To mitigate this:

* The system displays sources
* It provides confidence scores
* It explicitly handles missing context

---

## Demo

Loom walkthrough: 

---

## Repository

GitHub link: https://github.com/MokeyCodes/applied-ai-system-project
