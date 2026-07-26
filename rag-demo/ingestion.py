from rag_utils.fetch import load_pdf_data
from rag_utils.preprocessing import preprocess
from dotenv import load_dotenv
import os

load_dotenv()

pdf_path = os.getenv("PDF_PATH")

def main():

    # 1. Load the PDF data
    text = load_pdf_data(pdf_path)
    print(text)

    # 2. Preprocess the text data
    cleaned_text = preprocess(text)
    print(cleaned_text)

if __name__ == "__main__":
    main()