from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
import shutil

VECTOR_PATH = "vectorstore"

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    if os.path.exists(VECTOR_PATH):
        shutil.rmtree(VECTOR_PATH)

    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local(VECTOR_PATH)

    return vectorstore


def load_vectorstore():
    if not os.path.exists(VECTOR_PATH):
        return None

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    return FAISS.load_local(
        VECTOR_PATH, embeddings, allow_dangerous_deserialization=True
    )
