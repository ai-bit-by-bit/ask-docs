# vector_store.py (in-memory)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.docstore.document import Document

def text_to_docs(text: str) -> list[Document]:
    """
    Split the text into chunks of 1000 characters with 200 characters overlap
    Args:
        text: The text to split
    Returns:
        A list of documents
    """

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.create_documents([text])

def save_to_faiss(docs: list[Document]) -> FAISS:
    """
    Save the documents to a FAISS index
    Args:
        docs: The documents to save
    Returns:
        A FAISS index
    """
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embedding=embeddings)