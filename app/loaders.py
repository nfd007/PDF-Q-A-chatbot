from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_docs_from_pdfs(pdf_paths):
    docs = []
    for p in pdf_paths:
        loader = PyPDFLoader(p)
        docs.extend(loader.load())
    return split_docs(docs)

def load_docs_from_urls(urls):
    docs = []
    for u in urls:
        loader = WebBaseLoader(u)
        docs.extend(loader.load())
    return split_docs(docs)

def split_docs(docs, chunk_size=800, chunk_overlap=80):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(docs)
