from fastapi import FastAPI, UploadFile, File, Form
from typing import List, Optional
import shutil, os
from app.vectorstore import get_vectorstore
from app.loaders import load_docs_from_pdfs, load_docs_from_urls
from app.chains import build_qa_chain

app = FastAPI(title="RAG QA Bot (LangChain + OSS LLM)")

qa_chain = build_qa_chain()
vectordb = get_vectorstore()

@app.post("/ingest/pdfs")
async def ingest_pdfs(files: List[UploadFile] = File(...)):
    paths = []
    os.makedirs("data/docs", exist_ok=True)
    for f in files:
        path = f"data/docs/{f.filename}"
        with open(path, "wb") as out:
            shutil.copyfileobj(f.file, out)
        paths.append(path)

    docs = load_docs_from_pdfs(paths)
    vectordb.add_documents(docs)
    vectordb.persist()
    return {"status": "ok", "num_chunks": len(docs)}

@app.post("/ingest/urls")
async def ingest_urls(urls: List[str]):
    docs = load_docs_from_urls(urls)
    vectordb.add_documents(docs)
    vectordb.persist()
    return {"status": "ok", "num_chunks": len(docs)}

@app.post("/ask")
async def ask(question: str = Form(...)):
    result = qa_chain({"query": question})
    answer = result["result"]
    sources = [doc.metadata for doc in result["source_documents"]]
    return {"answer": answer, "sources": sources}
