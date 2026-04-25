# Model Card: Applied AI Study Assistant

## 1. Model Name

Applied AI Study Assistant

## 2. Goal / Task

This system answers user questions using a small document knowledge base. Its goal is to retrieve relevant information, generate a grounded answer, show which sources were used, and provide a simple confidence score.

## 3. Base Project Connection

This final project extends my Week 7 **Music Recommender Simulation** project. In that earlier project, I built a scoring-based system that ranked songs based on user preferences like genre, mood, and energy. It helped me learn how AI-style systems use structured logic, ranking, and evaluation to produce outputs.

For this final version, I expanded from recommendation logic into a fuller applied AI workflow that includes retrieval, answer generation, validation, and logging.

## 4. Data Used

This system uses a small local knowledge base made up of text files stored in `data/knowledge_base/`.

Current documents:

* `doc1.txt`
* `doc2.txt`
* `doc3.txt`

These files contain short factual notes about prompt engineering, retrieval-augmented generation, and AI reliability.

### Data limitations

* The dataset is very small
* The system can only answer questions related to the provided documents
* If the wording of the question does not overlap well with the document text, retrieval may miss useful content

## 5. System / Algorithm Summary

The system works in four main steps:

1. A user asks a question
2. The retriever searches the document set for relevant files using keyword overlap
3. The generator builds an answer from the most relevant retrieved text
4. The validator assigns a confidence score and checks whether supporting sources were found

The system also logs each run in JSON format so that outputs can be reviewed later.

## 6. Intended Use

This project is intended for:

* educational demos
* simple question answering over a small document set
* showing how retrieval, validation, and logging can work together in an AI system
* portfolio demonstration of applied AI engineering concepts

## 7. Non-Intended Use

This system should not be used for:

* high-stakes decisions
* legal, medical, or financial advice
* broad internet-scale question answering
* situations where users need guaranteed accuracy or comprehensive knowledge

## 8. Reliability Features

This system includes several reliability features:

* **Source display**: shows which document(s) were used
* **Confidence scoring**: gives a simple confidence estimate
* **Validation logic**: checks whether sources were found
* **Logging**: stores each run for debugging and evaluation
* **Automated tests**: basic tests verify retrieval and validation behavior
* **Fallback handling**: returns a safe response when no relevant context is found

These features help make the system more transparent and easier to debug.

## 9. Evaluation Process

I evaluated the system in three ways:

### Manual testing

I tested the system with at least three questions:

* What is prompt engineering?
* What is retrieval-augmented generation?
* How can AI systems be more reliable?

The system returned correct answers for all three because each question matched one of the available documents.

### Output inspection

I checked whether:

* the answer matched the document content
* the correct source file was shown
* the confidence score appeared
* the interaction was saved in the logs folder

### Automated testing

I used `pytest` to verify:

* validation with sources
* validation without sources
* retrieval returns the expected data type

## 10. Observed Behavior

The system performs well when the question closely matches the wording in the documents. It is fast, easy to inspect, and produces traceable outputs. The system now better detects out-of-scope queries and returns a fallback response instead of generating unrelated answers.

It performs less well when:

* the question is vague
* the user asks about a topic not in the knowledge base
* the wording does not strongly overlap with stored text

## 11. Limitations and Biases

This system has several limitations:

* It relies on keyword matching rather than semantic understanding
* It is biased toward documents that share exact words with the query
* It may miss relevant information if the question uses different wording
* It cannot reason deeply beyond the retrieved content
* Because the knowledge base is small, coverage is very limited
* It may still fail when relevant concepts are phrased very differently from the stored documents, even after improving keyword filtering.

A broader limitation is that users may trust confident-sounding answers too easily, even when the system only has partial context.

## 12. Misuse Risks and Safeguards

### Possible misuse

A user could treat the system like a general expert assistant and rely on it beyond its intended scope.

### Safeguards

To reduce this risk, the system:

* shows sources
* uses a confidence score
* falls back when context is weak
* keeps logs for inspection and debugging

These safeguards do not eliminate mistakes, but they make the system more transparent.

## 13. What Surprised Me

What surprised me most was how much retrieval quality affected the final answer. Even with a simple generator, the system produced good results when the right document was retrieved. That showed me that in many AI systems, context selection matters just as much as answer generation.

## 14. AI Collaboration Reflection

One helpful AI suggestion was the idea to organize the project into modular components such as retriever, generator, validator, and logger. That made the project easier to understand and test.

One flawed or incomplete AI suggestion was using an external model API for generation without accounting for quota and billing limits. I had to adapt the system so it would still work locally and remain demoable for the assignment. This reminded me that AI-generated solutions are only useful if they fit real project constraints.

## 15. Biggest Learning Moment

My biggest learning moment was realizing that a working AI system is more than just “getting an answer.” A strong system also needs explainability, validation, and reproducibility. Building those parts made the project feel much more like real AI engineering.

## 16. Ideas for Improvement

If I continued this project, I would improve it by:

* replacing keyword retrieval with embedding-based semantic search
* expanding the knowledge base with more documents and topics
* adding a better confidence model based on retrieval strength
* building a small web interface for easier interaction
* adding stronger automated tests for edge cases and out-of-scope questions

## 17. Final Reflection

This project reflects my growth from building a scoring-based recommender into building a more complete applied AI system. It shows that I can move beyond a single algorithm and think about full system behavior: how information is retrieved, how outputs are checked, how failures are logged, and how limitations are documented.

It also taught me that responsible AI engineering means being honest about what a system can and cannot do.
