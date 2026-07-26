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


Real Time Example - Consider you have a biology book, If I need to find "What is photosynthesis?" for this we will look on the index based on it we will find the content which is nearest relevance of it.

```bash
ASK Question -> Reterive (Check Index) -> Read Relevance Part -> Generate Answer
```

RAG is a way for AI to find the right info first, then answer the question accordingly instead of remember everything. AI will search index, Find correct page, Read only that part and give the answer, A smart process is called RAG,

```bash
Note: Incase of using LLM there will be cutoff for every LLM until then the model get trained.
```

Instead we provide a book to LLM in which the required content we have based on it answer get generated through relevent information.

### Two Phases of RAG:
- Ingestion (to load data into db)
- Retrieval (to fetch data from db)

## Ingestion Phase
```bash
Fetch the Data -> Pre-processing -> Chunking -> Embeddingb -> Vector Store
```

Fetch the Data - Collect data from different source like PDFs, website, database or APIs.

pre-processing - Clean and prepare the data by removing unnecessary content, extracting text and standardizing the format.

Chunking - Split the large document into smaller meaningful pieces so that AI can search efficiently.

Embedding - Convert each text chunk into a numerical vector that captures its sematic meaning.

Vector Store - Store these vectors in a vector database so similar information can be retrived quickly during search. Stored with metadata.

User: Tell me about photosynthesis?
AI: Will frame answer by vectors with nearest values.


### Types of Chunking
- Fixed size chunking (Split the doc into chunks of fixed size(based on char or tokens) without considering meaning)
- Semantic chunking (Split the doc based on meaning or topic changes. Each chunk contains a complete idea or topic)
- Recursive chunking (Recursively split text using a hierarchy of seperators until the chunk size fits the limit. Common order: paragraph -> sentence -> words)
- Sliding window chunking - (Creates overlapping chunks using a moving window. Each chunk shares some content with the previous chunk)
