from rag_utils.fetch import load_pdf_data
from dotenv import load_dotenv
import os

load_dotenv()

pdf_path = os.getenv("PDF_PATH")

def main():
    # 1. Load the PDF data
    text = load_pdf_data(pdf_path)
    print(text)

if __name__ == "__main__":
    main()