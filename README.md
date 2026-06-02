# 🎓 SchoolIQ – Agentic AI Powered Educational Analytics System

SchoolIQ is an intelligent educational analytics assistant that combines **Agentic AI**, **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, **SQL-based analytics**, and **Vector Databases** to help teachers and school administrators interact with student data using natural language.

The system enables users to ask questions such as:

- How many students are there?
- What is the average final grade?
- Which students are high performers?
- What patterns can be observed in student performance?
- Explain trends in the dataset.

Instead of manually querying databases or analyzing spreadsheets, users can simply chat with the system.

---

# 🚀 Features

## 📊 Data Analytics

- Student count analysis
- Grade statistics
- Performance comparisons
- Aggregate calculations
- Dataset exploration
- SQL-powered analytics

---

## 🔍 Retrieval-Augmented Generation (RAG)

- Semantic search using vector embeddings
- Context retrieval from student records
- Intelligent knowledge retrieval
- Context-aware responses

---

## 🤖 Agentic AI Routing

The system automatically decides whether a question requires:

### SQL Analytics
Examples:
- How many students are there?
- What is the average grade?
- Which student has the highest score?

### RAG + LLM Reasoning
Examples:
- Explain the grading trends.
- Describe high-performing students.
- What insights can be derived from the dataset?

---

## 🧠 LLM Integration

- Natural language understanding
- Context-aware reasoning
- Dataset explanation
- Educational insights

---

# 🏗️ System Architecture

```text
                User Question
                       │
                       ▼
                Agent Router
                       │
        ┌──────────────┴──────────────┐
        │                             │
        ▼                             ▼
 SQL Analytics Engine         RAG Retrieval Engine
        │                             │
        ▼                             ▼
 SQLite Database          ChromaDB Vector Store
        │                             │
        └──────────────┬──────────────┘
                       ▼
                  LLM Layer
                       ▼
                Final Response
```

---

# 🛠️ Tech Stack

## Programming Language
- Python

## AI & LLM
- OpenAI API
- LangChain

## Retrieval-Augmented Generation
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers

## Database
- SQLite

## Data Processing
- Pandas
- NumPy

## Environment Management
- Python Dotenv

---

# 📂 Project Structure

```text
SchoolIQ-Agentic-RAG-System/
│
├── data/
│   └── school.csv
│
├── database/
│   ├── db_setup.py
│   ├── db_executor.py
│   ├── sql_analysis.py
│   ├── analysis_functions.py
│   └── school.db
│
├── rag/
│   ├── create_vector_db.py
│   ├── query_rag.py
│   ├── rag_utils.py
│   └── chroma_db/
│
├── llm/
│   ├── openai_llm.py
│   ├── llm_explainer.py
│   └── sql_generator.py
│
├── router/
│   └── router.py
│
├── chatbot.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/SchoolIQ-Agentic-RAG-System.git

cd SchoolIQ-Agentic-RAG-System
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
OPENAI_API_KEY=your_openai_api_key
```

---

# 🗄️ Create Database

Run:

```bash
python database/db_setup.py
```

This will:

- Create SQLite database
- Load school dataset
- Prepare tables for analytics

---

# 🧠 Create Vector Database

Run:

```bash
python rag/create_vector_db.py
```

This will:

- Generate embeddings
- Create ChromaDB vector store
- Enable semantic retrieval

---

# ▶️ Run Application

```bash
python main.py
```

---

# 💬 Example Queries

## SQL Analytics

```text
How many students are there?

What is the average final grade?

Which student has the highest score?

What is the maximum age?
```

---

## RAG + LLM

```text
Explain grading patterns.

Describe high-performing students.

What trends can be observed in student performance?

Provide insights about the dataset.
```

---

# 📈 Future Enhancements

- Multi-school support
- Dashboard integration
- Role-based authentication
- Fine-tuned local LLM deployment
- Real-time analytics
- Web-based interface
- Advanced educational insights
- Multi-dataset support

---

# 🔒 Security

- API keys stored using environment variables
- Sensitive files excluded through `.gitignore`
- Database isolation
- Secure configuration management

---

# 🎯 Learning Outcomes

This project demonstrates:

- Agentic AI Systems
- Retrieval-Augmented Generation (RAG)
- Vector Databases
- LLM Integration
- Natural Language Interfaces
- SQL Analytics
- Data Engineering
- AI Application Development

---

# 👨‍💻 Author

**Atharva Kotkar**

Computer Engineering Student | AI & Data Science Enthusiast

---

# ⭐ If You Like This Project

Consider giving the repository a star and sharing feedback for future improvements.
