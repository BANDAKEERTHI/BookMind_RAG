# 📚 BookMind RAG

BookMind RAG is an AI-powered Retrieval-Augmented Generation (RAG) application that enables users to upload PDF documents, build a searchable knowledge base, and ask natural language questions grounded in document content.

The application combines document retrieval, vector search, and Large Language Models (LLMs) to generate accurate, context-aware answers from uploaded books, notes, research papers, and PDFs.

---

# ✨ Features

| Feature | Description |
|----------|-------------|
| 📄 PDF Upload | Upload and process PDF documents |
| 🔍 Semantic Search | Retrieve relevant document chunks |
| 🧠 Retrieval-Augmented Generation (RAG) | Generate context-aware answers |
| 🖥️ Ollama Support | Local AI inference without cloud dependency |
| 🔑 Gemini BYOK | Bring Your Own Gemini API Key |
| ⚡ Vector Search | Fast retrieval using embeddings |
| 🧪 Testing Support | Automated testing with Pytest |
| 🔒 Secure Configuration | Environment-based API key management |

---

# ✅ Compliance Highlights

- 🤖 AI-powered Retrieval-Augmented Generation (RAG)
- 🖥️ Local AI Inference with Ollama
- 🔑 Bring Your Own Key (BYOK) support for Gemini
- 🔒 Secure environment-based API key management
- 📄 PDF document processing and retrieval
- 🧠 Context-aware question answering
- 🧪 Automated testing with Pytest
- 🎯 Code quality enforcement using Black, Flake8, and MyPy
- 📂 Modular and maintainable project structure
- 🌍 Open-source development workflow using Git and GitHub

---

# 🏗️ Architecture

```text
                ┌─────────────────┐
                │   User Uploads  │
                │      PDF        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   PDF Loader    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Splitter   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Vector Store    │
                │ (Embeddings)    │
                └────────┬────────┘
                         │
─────────────────────────┼─────────────────────────
                         │
                         ▼
                ┌─────────────────┐
                │  User Question  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Retrieval Agent │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Relevant Chunks │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Answer Agent   │
                └────────┬────────┘
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
   ┌────────────┐                ┌────────────┐
   │   Ollama   │                │   Gemini   │
   │  (Local)   │                │   (BYOK)   │
   └─────┬──────┘                └─────┬──────┘
          │                             │
          └──────────────┬──────────────┘
                         ▼
                ┌─────────────────┐
                │ AI Generated    │
                │    Response     │
                └─────────────────┘
```

---

# 🛠️ Tech Stack

| Layer | Technology |
|---------|------------|
| Programming Language | Python |
| Local LLM | Ollama |
| Cloud LLM | Google Gemini |
| Document Processing | PDF Processing Utilities |
| Vector Storage | Local Vector Store |
| Testing | Pytest |
| Code Quality | Black, Flake8, MyPy |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
BookMind_RAG/
│
├── agents/
│   ├── answer_agent.py
│   └── retrieval_agent.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── translator.py
│   └── vector_store.py
│
├── uploads/
├── vectorstore/
│
├── app.py
├── llm_ollama.py
├── gemini_api_demo.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/BANDAKEERTHI/BookMind_RAG.git
cd BookMind_RAG
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

# ▶️ Running the Application

```bash
python app.py
```

---

# 🧪 Running Tests

```bash
pytest
```

---

# 🎯 Example Workflow

1. Upload a PDF document.
2. The system extracts and processes the text.
3. Text chunks are converted into embeddings and stored.
4. Ask a question about the uploaded document.
5. Relevant document chunks are retrieved.
6. The LLM generates an answer using retrieved context.
7. Receive accurate, document-grounded responses.

---

# 🔒 Security

- API keys are stored using environment variables.
- Sensitive credentials are excluded through `.gitignore`.
- No secrets are hard-coded in source files.
- Supports secure BYOK integration.

---

# 📚 Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- Large Language Models (LLMs)
- Local AI Inference
- Prompt Engineering
- Software Engineering Best Practices
- Secure API Key Management

---

# 🚀 Future Enhancements

- Support for additional document formats
- Advanced vector retrieval techniques
- Chat history and conversation memory
- Web deployment
- User authentication
- Performance optimization for large document collections

---

# 👩‍💻 Author

**Banda Keerthi**

B.Tech Computer Science and Engineering

Aspiring Software Engineer | AI & Machine Learning Enthusiast

GitHub: https://github.com/BANDAKEERTHI

---

# 📜 License

This project is licensed under the MIT License.