# 💬 CHAI DOCS — Gemini 2.5 Chatbot (by bm9avan)

An elegant chatbot interface powered by Google's Gemini 2.5 Flash model, built using Streamlit. This project includes custom persona injection via a system prompt, real-time chat memory, and an auto-scrolling UI with a sidebar for persona visibility.

---

## 🚀 Features

- ✨ Gemini 2.5 Flash model integration using `google.genai`
- 🧠 Persona Prompt loaded from JSON
- 🪟 Sticky sidebar showing current system prompt
- 💬 Conversation history with roles (user & assistant)
- ⬇️ Input box pinned at the bottom for continuous chat flow
- 🔄 Auto-scrolls to the latest message automatically
- 🧼 Clean layout with custom CSS for enhanced UX

---

## 📁 Project Structure

```

hcBot/
├── main.py                    # Streamlit app logic
├── Persona\_prompt.json       # Contains the system persona instruction
├── requirements.txt          # Python dependencies
└── .streamlit/
└── secrets.toml          # Gemini API key config

```

---

## 🛠 Setup & Run

### 1. Clone the repo

```bash
git clone https://github.com/bm9avan/gemini-chatbot.git
cd gemini-chatbot
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\\Scripts\\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Gemini API key

Create a file at `.streamlit/secrets.toml` and add:

```toml
[genai]
api_key = "your-gemini-api-key-here"
```

### 5. Customize Persona Prompt

Edit `Persona_prompt.json`:

```json
{
  "system_instruction": "You are a helpful, knowledgeable AI that speaks like a software engineer and explains concepts clearly using analogies."
}
```

---

## ▶ Run the App

```bash
streamlit run main.py
```

---

## ✏️ Customization

- 💡 Want to change the assistant tone? Just modify `Persona_prompt.json`.
- 📜 Need markdown/code formatting? You can enhance output rendering using `st.markdown(..., unsafe_allow_html=True)` or with custom syntax highlighting.

---

## 📄 License

MIT — feel free to fork and remix.

---

## 👤 Author

Made by [bm9avan](https://github.com/bm9avan) with 💙 using Streamlit + Gemini AI
