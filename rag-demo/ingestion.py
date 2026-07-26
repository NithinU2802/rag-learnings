from rag_utils.fetch import load_pdf_data
from rag_utils.preprocessing import preprocess
from rag_utils.chunking import chunk_text
from rag_utils.embedding import generate_embeddings
from rag_utils.vector_store import setup_collection, ingest_chunks
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import yaml
import os

load_dotenv()

pdf_path = os.getenv("PDF_PATH")

def load_config():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config

def main():

    config = load_config()
    # print(config)

    # 1. Load the PDF data
    text = load_pdf_data(pdf_path)
    # print(text)

    # 2. Preprocess the text data
    cleaned_text = preprocess(text)
    # print(cleaned_text)

    # 3. Chunking the text data
    chunks = chunk_text(cleaned_text)
    print("Total Chunks Created: ", len(chunks))
    # for i, chunk in enumerate(chunks):
    #     print(f"\n-- Chunk {i+1} ---\n")
    #     print(chunk)

    # 4. Generate Embeddings
    embeddings = generate_embeddings(chunks, config["ollama"]["embedding_model"])
    print("Embedding for all chunks: ", embeddings[0][:5])

    # 5. Setup Qdrant collection and ingest data
    print("Connecting to Qdrant...")
    client = QdrantClient(
        host=config["qdrant"]["host"],
        port=config["qdrant"]["port"]
    )

    setup_collection(client, config["qdrant"]["collection_name"], config["qdrant"]["vector_size"])
    print("Ingesting vectors into Qdrant...")
    ingest_chunks(client, config["qdrant"]["collection_name"], chunks, embeddings)
    print("Data ingestion completed!")

if __name__ == "__main__":
    main()