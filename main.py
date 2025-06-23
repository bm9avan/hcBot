import streamlit as st
import json
from google import genai
from google.genai import types


# Load persona prompt from JSON file
with open("Persona_prompt.json", "r", encoding="utf-8") as f:
    Persona_Prompt = json.load(f)["system_instruction"]

# Configure your Gemini API key in Streamlit secrets (e.g., ["genai"]["api_key"]) or set here directly
# Example: genai.configure(api_key="YOUR_GEMINI_API_KEY")
genai.configure(api_key=st.secrets["genai"]["api_key"] if "genai" in st.secrets else "YOUR_GEMINI_API_KEY")

# Initialize chat history in session state
def init_chat():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

init_chat()

st.title("💬 Streamlit Chatbot (Gemini 2.0 Flash)")
st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 1rem;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Display chat messages
def display_chat():
    for msg in st.session_state.chat_history:
        role = msg.get("role")
        content = msg.get("content")
        with st.chat_message(role):
            st.markdown(content)

# User input and send button
with st.container():
    user_input = st.chat_input("Type your message...")

    if user_input:
        # Append user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Create a chat session with persona prompt config
        chat = genai.client.chats.create(
            model="gemini-2.0-flash",
            config=GenerateContentConfig(
                system_instruction=Persona_Prompt
            )
        )

        # Send all messages in chat history
        for msg in st.session_state.chat_history:
            chat.send_message(msg["content"])

        # Get assistant response
        assistant_text = chat.last.text

        # Append assistant response
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_text})

# Display the chat
display_chat()