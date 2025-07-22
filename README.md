# Pizza AI Agent 🍕🤖

Welcome to the **Pizza AI Agent**! This project is an AI-powered assistant that helps you analyze and answer questions about restaurant reviews, with a special focus on pizza places. Built using LangChain, Ollama, and Chroma, it leverages the power of large language models and vector search to provide insightful, context-aware answers to your queries.

---

## 🚀 What does it do?

- **Reads and embeds restaurant review data** for fast, semantic search.
- **Answers natural language questions** about menu items, best dishes, and customer experiences using an LLM.
- **Retrieves the most relevant reviews** to support its answers, making responses more accurate and grounded in real data.

---

## 🛠️ Tech Stack
- **Python**
- **LangChain** (for chaining LLMs and retrieval)
- **Ollama** (for running local LLMs)
- **Chroma** (for vector database and semantic search)
- **Pandas** (for data handling)

---

## 📦 Project Structure

```
.
├── main.py                  # Main entry point for the AI agent
├── vector.py                # Handles vector database and retrieval logic
├── requirements.txt         # Python dependencies
├── restaurant_reviews.csv   # Sample dataset of restaurant reviews
└── README.md                # This file
```

---

## ⚡ Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Revanthinfosec/Pizza-AI-Agent.git
   cd Pizza-AI-Agent
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the agent:**
   ```bash
   python3 main.py
   ```

---

## 💡 How it Works
- The agent loads restaurant reviews from a CSV file.
- It creates vector embeddings for each review using Ollama's embedding model.
- When you ask a question, it retrieves the most relevant reviews using Chroma's vector search.
- The selected reviews and your question are sent to a language model (LLM) to generate a helpful, context-aware answer.

---

## 📝 Example Usage

```
Enter a question (type 'exit' to quit): What is the best pizza in the restaurant?

AI: Based on customer reviews, the Margherita Pizza is highly recommended for its fresh ingredients and crispy crust!
```

---

## 🤔 Why use this?
- **For restaurant owners:** Get insights from real customer feedback.
- **For foodies:** Discover the best dishes and experiences at a glance.
- **For developers:** Learn how to build retrieval-augmented generation (RAG) systems with modern AI tools.

---

## 📬 Contributing
Pull requests are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a PR.

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE). 