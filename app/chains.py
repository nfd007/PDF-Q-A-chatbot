from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.vectorstore import get_vectorstore
from app.config import settings

from langchain.chains import RetrievalQA
from langchain.chains.question_answering import load_qa_chain

def build_qa_chain():
    llm = Ollama(model=settings.model_name, temperature=0.1)
    vectordb = get_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are a helpful assistant. Use the provided context to answer.\n"
            "If you don't know, say you don't know.\n\n"
            "Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        ),
    )

    # Use the prompt with a simple chain
    qa_chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    return RetrievalQA(
        retriever=retriever,
        combine_documents_chain=qa_chain,
        return_source_documents=True,
    )
