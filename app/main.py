import streamlit as st
from document_handler import extract_text

# Header
st.title("🔎 Ask your documents with AI")
st.divider()

uploaded_file = st.file_uploader("Upload or drag and drop a document", type=["pdf", "docx", "txt"], accept_multiple_files=False)

if uploaded_file is not None:
    with st.spinner("Reading file..."):
        text = extract_text(uploaded_file)
        st.success("Done!")
        st.text_area("📄 Extracted Text", text, height=400)
else:
    st.warning("No file uploaded yet!")