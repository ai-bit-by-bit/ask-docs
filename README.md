# 🧠 AskDocs: AI-Powered Document Q&A App

AskDocs is a user-friendly web application that lets you **ask questions about your documents in natural language** — and get smart, accurate answers in real time. Powered by **RAG (Retrieval-Augmented Generation)**, LangChain, and cutting-edge LLMs, it's your personal document assistant.

> 📄 Upload PDFs, DOCX, or TXT files.  
> 💬 Ask any question.  
> ⚡️ Get instant, AI-powered responses based on your content.

---

## 🚀 Features

- 📁 Drag-and-drop document upload (PDF, DOCX, TXT)
- 🔍 Document chunking & embedding with LangChain
- 🧠 Smart Q&A using OpenAI or local models (via Ollama)
- 💃 Vector store with FAISS or ChromaDB
- 🧕 Multi-turn memory using LangChain's conversation memory
- 📌 Source reference display with similarity scores
- 📦 Modular codebase with simple UI (built with Streamlit)

---

## 🧠 Tech Stack

| Component            | Technology                    |
|----------------------|-------------------------------|
| Frontend             | Streamlit                     |
| AI / LLMs            | OpenAI / Local models (Ollama)|
| Document Handling    | LangChain TextSplitter        |
| Embedding            | OpenAI / HuggingFace models   |
| Vector Store         | FAISS or ChromaDB             |
| Memory Management    | LangChain Memory              |
| Backend Orchestration| Python                        |

---

## 👥 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/your-username/askdocs.git
cd ask-docs

# 2. Create environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

## 📂 File Structure

```
ask-docs/
│
├── app.py                 # Main Streamlit app
├── chains/                # LangChain pipelines
├── utils/                 # Helper functions
├── embeddings/            # Vector store logic
├── data/                  # Uploaded files
├── requirements.txt       # Python dependencies
└── README.md              # You are here
```

---

## 📌 TODOs / Roadmap

- [x] Multi-document upload support
- [ ] Downloadable Q&A chat history
- [ ] Add RAG evaluation and similarity visualization
- [ ] Deploy with Docker and Streamlit Cloud
- [ ] Switch between cloud and local LLMs via settings

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request with suggestions or improvements.

---

## 📜 License

MIT License. See [LICENSE](./LICENSE) for more details.

---

## 💡 Inspiration

Built as part of a portfolio AI project to explore the power of LLMs + RAG pipelines in real-world document interaction.

> _“AskDocs turns your documents into a searchable conversation.”_
