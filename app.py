import warnings
warnings.filterwarnings('ignore')

import streamlit as st
import json
from llm_providers import run_llm

# Page Configuration
st.set_page_config(
    page_title="AI Chatbot Studio | GenAI Workspace",
    page_icon="🧠",
    layout="centered"
)

# Load config to display current active model in UI
try:
    with open("config.json", "r") as f:
        config = json.load(f)
    active_provider = config.get("provider", "Unknown").upper()
    active_model = config.get(config.get("provider", ""), {}).get("model", "N/A")
except Exception:
    active_provider = "LLM"
    active_model = "Active"

# --- SIDEBAR UI ---
with st.sidebar:
    st.header("⚙️ System Status")
    st.success(f"🟢 Active Provider: **{active_provider}**")
    st.caption(f"Model: `{active_model}`")
    
    st.markdown("---")
    
    st.write("### 🛠️ Features")
    st.markdown("""
    - Dynamic Provider Routing
    - Contextual Memory Retain
    - Session Parameter Control
    """)
    
    st.markdown("---")
    
    # Reset Conversation Button in Sidebar
    if st.button("🔄 Reset Conversation", use_container_width=True):
        st.session_state["history"] = [
            {"role": "assistant", "content": "Conversation reset. How can I assist you today?"}
        ]
        st.rerun()

# --- MAIN UI HEADER ---
st.title("🧠 Next-Gen AI Workspace")
st.markdown("Your intelligent conversational companion for instant problem solving & reasoning.")

# Collapsible Info Box
with st.expander("ℹ️ About this Application"):
    st.write("""
    - **Dynamic Routing:** Switches seamlessly between OpenAI & Google Gemini via backend configurations.
    - **Context Memory:** Maintains full session context for multi-turn conversations.
    - **Configurable LLM Params:** Fine-tuned `temperature`, `top_p`, and token limits.
    """)

st.markdown("---")

# Initialize conversation memory
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

# Display chat history with custom avatars
for msg in st.session_state["history"]:
    avatar = "🤖" if msg["role"] == "assistant" else "👤"
    st.chat_message(msg["role"], avatar=avatar).markdown(msg["content"])

# User input & Response Generation
if prompt := st.chat_input("Type your message..."):
    # Add user message
    st.session_state["history"].append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="👤").markdown(prompt)

    # Generate response with spinner
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner(f"Generating response via {active_provider}..."):
            reply = run_llm(st.session_state["history"])
            st.markdown(reply)

    # Append assistant response to history
    st.session_state["history"].append({"role": "assistant", "content": reply})