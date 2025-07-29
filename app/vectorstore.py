from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.config import settings

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=settings.embedding_model)

def get_vectorstore(persist_dir: str = settings.persist_dir):
    embeddings = get_embeddings()
    return Chroma(
        collection_name="docs",
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )