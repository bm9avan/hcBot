import streamlit as st
import json
from google import genai
from google.genai import types


# Load persona prompt from JSON file
with open("Persona_prompt.json", "r", encoding="utf-8") as f:
    Persona_Prompt = json.load(f)["system_instruction"]

client = genai.Client(api_key=st.secrets["genai"]["api_key"] if "genai" in st.secrets else "")
def callModel(contents):
    # Create a system prompt entry
    print(contents)
    system_prompt = {
        "role": "system",
        "parts": [{"text": Persona_Prompt}]
    }

    # Convert user/assistant messages into Gemini-compatible format
    formatted_msgs = [
        {"role": msg["role"], "parts": [{"text": msg["content"]}]} for msg in contents
    ]

    # Prepend system instruction
    full_contents = [system_prompt] + formatted_msgs

    # Send to Gemini
    res = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=json.dumps(full_contents)
    )

    return res.text

# Initialize chat history in session state
def init_chat():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

init_chat()

# Page config
st.set_page_config(page_title="Gemini Chatbot", layout="centered")

st.title("💬 CHAI DOCS (AI Bot)")

# Sidebar for displaying persona prompt
with st.sidebar:
    st.title("🧠 System Prompt")
    st.write(Persona_Prompt)

st.markdown("""
<style>
    .main {
        display: flex;
        flex-direction: column;
        height: 90vh;
    }
    .chat-container {
        flex: 1;
        overflow-y: auto;
        padding-bottom: 60px;
    }
    .stTextInput > div > div > input {
        font-size: 1rem;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Auto-scroll JS
st.markdown("""
<script>
    window.addEventListener('load', function() {
        var chatContainer = window.parent.document.querySelector('.element-container div[data-testid=\"stVerticalBlock\"]');
        if (chatContainer) chatContainer.scrollTop = chatContainer.scrollHeight;
    });
</script>
""", unsafe_allow_html=True)

def chatDisplay():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    st.markdown('</div>', unsafe_allow_html=True)

# Chat display section
st.container()

# Input at the bottom
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    assistant_text = callModel(st.session_state.chat_history)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_text})
    chatDisplay()
    # Safely trigger rerun *before* next render
    # st.experimental_rerun()


