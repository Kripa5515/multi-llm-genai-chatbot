# 🤖 Multi-LLM Interactive AI Chat Assistant

An interactive AI Chatbot built with Python and Streamlit that dynamically routes prompts to multiple Large Language Model (LLM) providers like OpenAI and Google Gemini based on dynamic JSON configurations.

## ✨ Features
- **Dynamic Provider Routing:** Switch between OpenAI and Google Gemini effortlessly via `config.json`.
- **Conversation Memory:** Retains chat history within the active Streamlit session.
- **Configurable Parameters:** Tailor `temperature`, `top_p`, and `max_tokens` per model provider.
- **Clean Chat Interface:** Streamlit-powered native messaging UI with a quick reset option.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Frontend UI:** Streamlit
- **LLMs / APIs:** OpenAI API (`gpt-4o-mini`), Google Gemini API (`gemini-3.6-flash`)
- **Config & Env:** `python-dotenv`, JSON-based dynamic routing

## 🚀 Quick Setup & Local Execution

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kripa5515/multi-llm-genai-chatbot.git](https://github.com/Kripa5515/multi-llm-genai-chatbot.git)
   cd multi-llm-genai-chatbot

2. Create & activate a virtual environment:
   python -m venv myenv
   # On Windows:
   myenv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Environment Configuration:
  Create a .env file in the root directory (refer to .env.example):

  OPENAI_API_KEY=your_openai_api_key
  
  GEMINI_API_KEY=your_gemini_api_key

6. Run the Streamlit App:
   streamlit run app.py
  
