import streamlit as st
import google.generativeai as genai

# 🔑 API Key
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Page config
st.set_page_config(page_title="Do Your Thing", page_icon="🤖", layout="centered")

# 🌗 Theme toggle
theme = st.sidebar.selectbox("🌗 Theme", ["Dark", "Light"])

# 🎨 Modern UI CSS
if theme == "Dark":
    st.markdown("""
    <style>
    .stApp {
        background-color: #0f172a;
        color: #f1f5f9;
    }

    .block-container {
        max-width: 700px;
        margin: auto;
    }

    .stTextInput > div > div > input {
        background-color: #1e293b;
        color: white;
        border-radius: 10px;
        padding: 12px;
        border: 1px solid #334155;
    }

    .stButton button {
        background-color: #3b82f6;
        color: white;
        border-radius: 10px;
        padding: 10px 16px;
        font-weight: bold;
        border: none;
    }

    .stButton button:hover {
        background-color: #2563eb;
    }

    .chat-user {
        background-color: #2563eb;
        padding: 10px;
        border-radius: 10px;
        margin: 6px 0;
        color: white;
    }

    .chat-bot {
        background-color: #334155;
        padding: 10px;
        border-radius: 10px;
        margin: 6px 0;
        color: white;
    }

    @media (max-width: 768px) {
        .block-container {
            padding: 10px !important;
        }

        h1 {
            font-size: 24px !important;
        }

        .stButton button {
            width: 100%;
            margin-top: 5px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }

    .block-container {
        max-width: 700px;
        margin: auto;
    }

    .stTextInput > div > div > input {
        background-color: white;
        color: black;
        border-radius: 10px;
        padding: 12px;
        border: 1px solid #cbd5e1;
    }

    .stButton button {
        background-color: #3b82f6;
        color: white;
        border-radius: 10px;
        padding: 10px 16px;
        font-weight: bold;
        border: none;
    }

    .chat-user {
        background-color: #3b82f6;
        padding: 10px;
        border-radius: 10px;
        margin: 6px 0;
        color: white;
    }

    .chat-bot {
        background-color: #e2e8f0;
        padding: 10px;
        border-radius: 10px;
        margin: 6px 0;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)

# 🎨 Header
st.image("logo.png", width=80)

st.markdown("""
<div style='text-align: center;'>
    <h1>🤖 Do Your Thing</h1>
    <h4>Your Personal AI Assistant</h4>
</div>
""", unsafe_allow_html=True)

# 🤖 Auto-select model
models = genai.list_models()
MODEL_NAME = None

for m in models:
    if "generateContent" in m.supported_generation_methods:
        MODEL_NAME = m.name
        break

model = genai.GenerativeModel(MODEL_NAME)

# 💬 Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "history" not in st.session_state:
    st.session_state.history = []

# 💬 Input
user_input = st.text_input("💬 Type your message:")

col1, col2 = st.columns(2)
send = col1.button("🚀 Send")
clear = col2.button("❌ Clear")

# 🚀 Send
if send and user_input:
    response = st.session_state.chat.send_message(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response.text))

# ❌ Clear
if clear:
    st.session_state.history = []
    st.session_state.chat = model.start_chat(history=[])

# 💬 Chat display (BUBBLES)
for role, msg in st.session_state.history:
    if role == "You":
        st.markdown(f"<div class='chat-user'>🧑 {msg}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bot'>🤖 {msg}</div>", unsafe_allow_html=True)

# ❤️ Footer
st.markdown("""
<hr>
<div style='text-align: center;'>

<p style="font-size:18px;">Made with ❤️ by <b>DWKR</b></p>

<a href="https://www.linkedin.com/in/diwakar-jha-064130229/" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="35" style="margin:10px;">
</a>

<a href="https://github.com/Stfu-diwakar" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="35" style="margin:10px;">
</a>

</div>
""", unsafe_allow_html=True)
