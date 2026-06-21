from utils.pdf_loader import load_pdf
from utils.text_splitter import split_text
from utils.vector_store import create_vectorstore

pdf_path = "uploads/computer network.pdf"

print("Loading PDF...")
text = load_pdf(pdf_path)

print("PDF Loaded Successfully!")
print("Text Length:", len(text))

print("Splitting Text...")
chunks = split_text(text)

print("Number of Chunks:", len(chunks))

print("Creating Vector Store...")
vectorstore = create_vectorstore(chunks)

print("Vector Store Created Successfully!")
