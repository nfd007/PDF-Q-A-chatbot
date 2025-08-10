DocChain – Ask Your PDF
# 🤖 DocChain – Ask Your PDF



Upload a PDF. Ask questions. Get AI-generated answers using LangChain, ChromaDB, and Ollama – all running locally.



---



## 🧠 What is This?



DocChain is a local Retrieval-Augmented Generation (RAG) chatbot powered by:



- 🧩 LangChain for orchestrating RAG pipelines
- 🗂️ ChromaDB for vector storage
- 🧠 Ollama for local LLM inference (Mistral, LLaMA, etc.)
- 📄 Streamlit frontend for interaction
-    Backend	FastAPI


---



## 🌐 Architecture (PlantUML)

<img width="1336" height="968" alt="Pasted image (3)" src="https://github.com/user-attachments/assets/14c981cb-8c62-4169-b222-49bdccb60c64" />





---



## ⚙️ Getting Started



### 🧪 1. Create virtualenv
```bash
python3 -m venv .venv
source .venv/bin/activate
```



### 📦 2. Install dependencies
```bash
pip install -r requirements.txt
```



### 🧠 3. Run Ollama
Install Ollama and run a model (e.g., llama3):
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama run llama3
```



### 🚀 4. Start backend and UI
```bash
# Terminal 1 – Backend
uvicorn app.main:app --reload --port 8000



# Terminal 2 – Streamlit UI
streamlit run ui.py
```



---



## 🧪 Sample Questions



After uploading a PDF, try:
- “What is this document about?”
- “Summarize the section about health.”
- “What advice did the author give?”



---



## 🧰 Tech Stack



| Layer | Tool |
|------------|--------------------------|
| LLM | Ollama (e.g., Mistral) |
| Vector DB | ChromaDB |
| Embeddings | HuggingFace Transformers|
| RAG Engine | LangChain |
| Frontend | Streamlit |
| Backend | FastAPI |



---



## 📂 Project Structure



```
├── app/
│ ├── main.py # FastAPI backend
│ ├── chains.py # RAG pipeline
│ ├── vectorstore.py # ChromaDB interface
│ ├── config.py # Model/settings
│ └── loader.py # PDF ingestion
├── ui.py # Streamlit frontend
├── data/ # Uploaded PDFs + vector index
├── requirements.txt
└── README.md
```



---



## 📄 License



MIT License.
Feel free to modify, deploy, and use in your projects or freelance work.



---



## 💡 Ideas for Extensions



- [ ] Add multi-PDF support
- [ ] Source citation in answers
- [ ] Chat history with session memory
- [ ] Docker container for deployment
- [ ] Hugging Face Space / Streamlit Cloud integration

