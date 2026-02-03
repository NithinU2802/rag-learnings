RAG - Retrieval Augmented Generation
------------------------------------
Retrivel Augmented Generation(RAG) combines search and generation. First, it searches trusted
knowledge sources like databases or documents for relevant information. Then it passes this 
information to a language model to generate a grounded and accurate response. This approach 
minimizes incorrect answers and keeps responses up to date without retraining the model.

way to store data (Which is easy to understand by AI):
- Vector DB
- Knowledge Graph

Vector DB Pipline:
- Document Loader
- Text Splitting
- Embedding (Contextual Mathematics)
- Vector DB (Chroma DB, FAISS, Pg Vector to store chunks)

Knowledge Graph Pipline:
- Document Loader
- Entity Extraction (Named Entity Recognition)
- Relationship Extraction
- Graph Store (Neo4j, NetworkX)

 ```[Subjective] --> [Predictive] --> [Objective]```

Key points
----------
- Uses LLMs + External Knowledge
- Retrives relevent and up-to-date data
- Reduces hallucinations
- Improves accuracy
- Useful for enterprise and domain-specific applications
- Works without retraining the base model

Step-by-step RAG flow
---------------------
```
User Question
     ↓
Embedding (question → vector)
     ↓
Vector Database Search
     ↓
Relevant Documents
     ↓
Prompt = Question + Retrieved Docs
     ↓
LLM Answer
```
