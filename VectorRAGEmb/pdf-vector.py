import faiss 
import google.generativeai as genai
import numpy as np
import pickle
import PyPDF2
import os

# Set your Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please set it before running the script.")
genai.configure(api_key=api_key)

def pdf_to_vector(pdf_path):
    # To read pdf 
    print(f"Reading PDF: {pdf_path}")
    with open(pdf_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        total_pages = len(pdf_reader.pages)

        page_texts = []
        for page_num, page in enumerate(pdf_reader.pages):
            page_text = page.extract_text()
            page_texts.append({
                'text': page_text,
                'page_number': page_num + 1
            })

        text = ''.join([p['text'] for p in page_texts])
        print(f"Total pages: {total_pages}")
        print(f"Total text length: {len(text):,} characters")
        print(f"Average characters per page: {len(text)//total_pages:,}")

        chunks = []
        chunks_metadata = []

        for i in range(0, len(text), 400):
            chunk_text = text[i: i+500]
            chunks.append(chunk_text)

            # estimate page this chunk belongs to
            estimated_page = min((i//(len(text)//total_pages)) +1, total_pages)
            chunks_metadata.append({
                'start_pos': i,
                'estimated_page': estimated_page
            })

        print(f"Created {len(chunks)} chunks")

        # Get embedding from Gemini AI
        print("Getting embedding...")
        embeddings = []
        for idx, chunk in enumerate(chunks):
            print(f"Processing {idx+1}/{len(chunks)}")
            response = genai.embed_content(model="models/embedding-001",
                                           content=chunk,
                                           task_type="retrieval_document")
            embeddings.append(response['data'][0]['embedding'])

        # Create FAISS index
        print("Creating FAISS index...")
        embeddings = np.array(embeddings)
        index = faiss.IndexFlatIP(1536)
        index.add(embeddings.astype('float32'))

        # Save to files
        print("Saving to files...")
        faiss.write_index(index, "vectors.index")
        with open("chunks.pkl", "wb") as f:
            pickle.dump({
                'chunks': chunks,
                'metadata': chunks_metadata,
                'total_pages': total_pages
            }, f)

        print("Vector database created successfully")
        print("Files saved: vectors.index, chunks.pkl")
        print(f"Vector shape: {embeddings.shape}")
        print(f"Sample vector (first 5 dims): {embeddings[0][:5]}")

        return embeddings, chunks



if __name__ == "__main__":
    file = "ProjectReport.pdf"
    embeddings, chunks = pdf_to_vector(file)
    print("\nSetup completed! Now you can ask a question regarding your project report.")