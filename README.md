
# 🤖 AI Chatbot (LLaMA 3 + Streamlit)

This is a simple AI Assistant chatbot built using Streamlit and LangChain that uses the LLaMA 3 model running locally via Ollama. It allows you to have natural language conversations directly in your browser.

## 🧠 Features

- Chat interface powered by LLaMA 3 via Ollama
- Streamlit-based web UI with chat history
- Maintains conversation state during session
- Fully local (no OpenAI or cloud API required)
- Simple and lightweight

## 🛠️ Tech Stack

- Python 3.8+
- Streamlit
- LangChain
- LangChain Community Extensions
- Ollama (for running LLaMA locally)

## 🗂️ Project Structure

├── app.py # Streamlit frontend
├── chatbot_engine.py # LLM backend logic using LangChain
├── requirements.txt # Python dependencies
├── README.md # Project overview

## ⚙️ Installation & Setup

1. Clone or download the repository.

2. Install Ollama and download LLaMA 3 model:

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Run the Ollama service
ollama serve

# Pull the LLaMA 3 model
ollama pull llama3
Create a virtual environment and install Python dependencies:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows

pip install -r requirements.txt
Run the Streamlit app:

bash
Copy
Edit
streamlit run app.py
