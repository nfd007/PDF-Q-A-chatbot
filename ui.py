import streamlit as st
import requests

st.title("📄 RAG Bot – Upload PDF & Ask Questions")

# Upload PDF
st.subheader("Step 1: Upload your PDF")
pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

if pdf_file:
    with st.spinner("Uploading and indexing..."):
        files = {"files": (pdf_file.name, pdf_file, "application/pdf")}
        r = requests.post("http://localhost:8000/ingest/pdfs", files=files)
        if r.ok:
            st.success(f"Uploaded! {r.json()['num_chunks']} chunks added.")
        else:
            st.error("Upload failed.")

# Ask questions
st.subheader("Step 2: Ask a question")
question = st.text_input("Enter your question")

if st.button("Ask") and question:
    r = requests.post("http://localhost:8000/ask", data={"question": question})
    print("Backend response:", r.text)  # 👈 Add this
    if r.ok:
        st.markdown("### 💬 Answer")
        st.write(r.json()["answer"])
    else:
        st.error("Error getting answer.")
