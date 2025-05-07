import streamlit as st
from document_handler import extract_text
from vector_store import text_to_docs, save_to_faiss
from qa_chain import get_qa_chain
# Header
st.title("🔎 Ask your documents with AI")
st.divider()

uploaded_file = st.file_uploader("Upload or drag and drop a document", type=["pdf", "docx", "txt"], accept_multiple_files=False)

if uploaded_file is not None:
    with st.spinner("Reading file..."):
        text = extract_text(uploaded_file)
        
    if text:
        st.success("Done!")
        st.text_area("📄 Extracted Text", text, height=400)

        if st.button("📌 Embed & Start QA"):
            with st.spinner("Chunking & Embedding..."):
                docs = text_to_docs(text)
                vector_store = save_to_faiss(docs)
                st.session_state.qa_chain = get_qa_chain(vector_store)
                st.session_state.chat_ready = True
                st.success("💡 Ask your first question below!")

# Q&A section
if st.session_state.get("chat_ready"):
    question = st.text_input("❓ Ask a question about the document:")
    if question:
        with st.spinner("Thinking..."):
            response = st.session_state.qa_chain({"question": question})
            st.markdown("🧠 **Answer:**")
            st.write(response["answer"])
        
else:
    st.warning("No file uploaded yet!")

# Footer
st.divider()
st.markdown("Made with ❤️ and ☕ by [A.I. Bit-by-Bit](https://github.com/ai-bit-by-bit)")
st.markdown("Like this project? [Buy me a coffee](https://buymeacoffee.com/ai_bit_by_bit)")