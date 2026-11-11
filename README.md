# Do Your Thing — Gemini AI Chatbot

A clean, responsive conversational AI assistant built with **Python**, **Streamlit**, and Google's **Gemini API**.

## Live demo

https://chatbot-dyt.streamlit.app/

## Features

- Conversational AI responses powered by Gemini
- Chat-style interface with conversation history during the current session
- One-click conversation reset
- Responsive desktop and mobile layout
- Theme-aware styling that follows Streamlit's light or dark appearance
- Dedicated About section with developer profile links
- API credentials loaded through Streamlit secrets

## Tech stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | User interface |
| Google Generative AI SDK | Gemini API integration |

## Project structure

```text
.
├── DYT.png
├── logo.png
├── README.md
├── requirements.txt
└── streamlit_app.py
```

## Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Stfu-diwakar/ChatBot.git
   cd ChatBot
   ```

2. Create and activate a virtual environment:

   **Windows**
   ```bash
   python -m venv .venv
   .venv\\Scripts\\activate
   ```

   **macOS / Linux**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create `.streamlit/secrets.toml` and add your Gemini key:

   ```toml
   GEMINI_API_KEY = "your-gemini-api-key"
   ```

   Keep this file private. Never commit API keys to GitHub.

5. Run the app:

   ```bash
   streamlit run streamlit_app.py
   ```

## Deploy on Streamlit Community Cloud

1. Connect this GitHub repository.
2. Set the main file path to `streamlit_app.py`.
3. Under **Settings → Secrets**, add:

   ```toml
   GEMINI_API_KEY = "your-gemini-api-key"
   ```

4. Save and redeploy.

## About the developer

**Diwakar Jha** — MCA (AI/ML) student and AI application developer.

- [LinkedIn](https://www.linkedin.com/in/diwakar-jha-064130229/)
- [GitHub](https://github.com/Stfu-diwakar)

## Notes

- The Gemini API key is loaded through Streamlit secrets and is not hard-coded.
- Chat history is stored in session state, not in a permanent database.
- Available models depend on the Gemini account, SDK version, and API access.

---
Made with care by **DWKR**.
