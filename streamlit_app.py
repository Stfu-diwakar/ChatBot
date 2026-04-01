import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyClaj3aY-GnFVj_k4XC1_gjpMgCgNqw5II")

st.set_page_config(page_title="Do Your Thing", page_icon="🤖", layout="centered")

theme = st.sidebar.selectbox("🌗 Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
        <style>
        .stApp {
            background-color: #0e1117;
            color: white;
        }
        .stTextInput > div > div > input {
            background-color: #262730;
            color: white;
        }
        .stButton button {
            background-color: #262730;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
        <style>
        .stApp {
            background-color: white;
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

# Auto-select working model
models = genai.list_models()
MODEL_NAME = None

for m in models:
    if "generateContent" in m.supported_generation_methods:
        MODEL_NAME = m.name
        break

model = genai.GenerativeModel(MODEL_NAME)

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "history" not in st.session_state:
    st.session_state.history = []

# Input
user_input = st.text_input("💬 Type your message:")

col1, col2 = st.columns(2)

send = col1.button("Send 🚀")
clear = col2.button("Clear ❌")

# Send message
if send and user_input:
    response = st.session_state.chat.send_message(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("DYT Bot", response.text))

# Clear chat
if clear:
    st.session_state.history = []
    st.session_state.chat = model.start_chat(history=[])

# Chat display
for role, msg in st.session_state.history:
    if role == "You":
        st.markdown(f"**🧑 You:** {msg}")
    else:
        st.markdown(f"**🤖 DYT Bot:** {msg}")

# Footer
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
