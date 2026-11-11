from pathlib import Path
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Do Your Thing | AI Assistant", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")
ROOT = Path(__file__).resolve().parent
LOGO_PATH = ROOT / "logo.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
.stApp { background: var(--background-color); color: var(--text-color); font-family: 'DM Sans', sans-serif; }
.block-container { max-width: 860px; padding-top: 2.2rem; padding-bottom: 3rem; }
h1,h2,h3 { font-family: 'Space Grotesk',sans-serif !important; letter-spacing: -.035em; }
.hero { text-align:center; padding:1.1rem 0 1.5rem; }
.hero-kicker { display:inline-block; padding:.35rem .75rem; border:1px solid var(--border-color); border-radius:999px; font-size:.78rem; font-weight:700; letter-spacing:.08em; text-transform:uppercase; opacity:.78; }
.hero h1 { font-size:clamp(2.2rem,6vw,3.5rem); line-height:1.08; margin:.85rem 0 .45rem; }
.hero p { opacity:.72; font-size:1.05rem; margin:0; }
.info-card { background:var(--secondary-background-color); border:1px solid var(--border-color); border-radius:18px; padding:1.1rem 1.25rem; margin:.5rem 0 1rem; }
[data-testid="stChatMessage"] { border:1px solid var(--border-color); border-radius:16px; padding:.9rem 1rem; margin-bottom:.75rem; }
[data-testid="stChatInput"] { border-radius:16px; }
[data-testid="stButton"] button { border-radius:12px; min-height:2.7rem; font-weight:650; transition:transform .15s ease; }
[data-testid="stButton"] button:hover { transform:translateY(-1px); }
a { color:var(--primary-color) !important; }
.footer { text-align:center; opacity:.72; font-size:.88rem; padding-top:1.5rem; }
@media(max-width:640px) { .block-container { padding:1.2rem 1rem 2rem; } .hero { padding-top:.5rem; } }
</style>
""", unsafe_allow_html=True)

_, center, _ = st.columns([1, 2, 1])
with center:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=104)

st.markdown("""
<div class="hero">
  <span class="hero-kicker">Your space to think</span>
  <h1>Do Your Thing</h1>
  <p>A simple, friendly AI assistant powered by Gemini.</p>
</div>
""", unsafe_allow_html=True)

chat_tab, about_tab = st.tabs(["💬  Chat", "👋  About"])
if "messages" not in st.session_state:
    st.session_state.messages = []
if "gemini_chat" not in st.session_state:
    st.session_state.gemini_chat = None

def get_model():
    """Configure Gemini and choose an available text-generation model."""
    api_key = st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing. Add it to Streamlit secrets.")
    genai.configure(api_key=api_key)
    available = [
        item.name for item in genai.list_models()
        if "generateContent" in getattr(item, "supported_generation_methods", [])
    ]
    if not available:
        raise RuntimeError("No Gemini model with generateContent access was found.")
    selected = next((name for name in available if "flash" in name.lower()), available[0])
    return genai.GenerativeModel(selected)

with chat_tab:
    st.markdown('<div class="info-card">Ask a question, explore an idea, or start a conversation. Your chat stays in this session.</div>', unsafe_allow_html=True)
    if st.button("🗑️ Clear conversation"):
        st.session_state.messages = []
        st.session_state.gemini_chat = None
        st.rerun()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Message Do Your Thing…")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Thinking…"):
                try:
                    if st.session_state.gemini_chat is None:
                        st.session_state.gemini_chat = get_model().start_chat(history=[])
                    response = st.session_state.gemini_chat.send_message(prompt)
                    answer = response.text or "I couldn't generate a text response. Please try again."
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as exc:
                    st.error(f"Sorry, I couldn't reach Gemini. {exc}")
                    st.caption("Check GEMINI_API_KEY in Streamlit secrets and confirm the key has access to a Gemini model.")

with about_tab:
    st.subheader("About this project")
    st.write("Do Your Thing is a lightweight conversational AI assistant built with Python and Streamlit. It uses Google's Gemini API to generate helpful responses in a clean, session-based chat experience.")
    st.markdown("#### What it offers")
    st.markdown("- Natural-language conversations powered by Gemini\n- Chat history maintained during the current app session\n- One-click conversation reset\n- Responsive layout that follows Streamlit's light or dark theme")
    st.markdown("#### Built with")
    st.write("Python  ·  Streamlit  ·  Google Gemini API")
    st.divider()
    st.markdown("#### Meet the developer")
    st.write("Built by **Diwakar Jha** — an MCA (AI/ML) student interested in building practical AI-powered applications.")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("LinkedIn ↗", "https://www.linkedin.com/in/diwakar-jha-064130229/", use_container_width=True)
    with col2:
        st.link_button("GitHub ↗", "https://github.com/Stfu-diwakar", use_container_width=True)

st.markdown('<div class="footer">Made with care by <strong>DWKR</strong> · Do Your Thing</div>', unsafe_allow_html=True)
