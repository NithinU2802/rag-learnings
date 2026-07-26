from rag_utils.fetch import load_pdf_data
from rag_utils.preprocessing import preprocess
from rag_utils.chunking import chunk_text
from dotenv import load_dotenv
import os

load_dotenv()

pdf_path = os.getenv("PDF_PATH")

def main():

    # 1. Load the PDF data
    text = load_pdf_data(pdf_path)
    # print(text)

    # 2. Preprocess the text data
    cleaned_text = preprocess(text)
    # print(cleaned_text)

    # 3. Chunking the text data
    chunks = chunk_text(cleaned_text)
    print("Total Chunks Created: ", len(chunks))
    for i, chunk in enumerate(chunks):
        print(f"\n-- Chunk {i+1} ---\n")
        print(chunk)

if __name__ == "__main__":
    main()