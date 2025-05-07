from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS

def get_qa_chain(vector_store: FAISS) -> ConversationalRetrievalChain:
    """
    Get a ConversationalRetrievalChain
    Args:
        vector_store: The vector store to use
    Returns:
        A ConversationalRetrievalChain
    """
    llm = ChatOpenAI()
    retriever = vector_store.as_retriever()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory
    )
