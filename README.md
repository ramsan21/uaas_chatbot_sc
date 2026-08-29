# UAAS Chatbot (Streamlit) — Standard Chartered theme

A Streamlit UAAS Chatbot: a **Quick Actions** sidebar (User / Auth·Keys /
Group / Notifications), a compact banner, chat bubbles, and a chat input.
Themed with Standard Chartered brand colours — blue `#0473EA` (primary) and
green `#38D200` (accent). Runs end-to-end in demo mode (mocked responses).

## Tech stack
- **Python 3.x**
- **Streamlit ≥ 1.32.0** — chat UI, sidebar, buttons (no HTML/JS/React)
- **Custom CSS** injected via `st.markdown(unsafe_allow_html=True)`
- **`st.session_state`** for chat history across reruns
- Modular packages: `config/`, `bot/`, `ui/`, `state.py`
- `.streamlit/config.toml` for server + theme

## Project structure
```
uaas_chatbot_sc/
├── app.py                 # entry point — wires banner + sidebar + chat + input
├── state.py               # session-state helpers (chat history)
├── config/
│   ├── __init__.py
│   └── settings.py        # branding, texts, Quick Actions menu tree
├── bot/
│   ├── __init__.py
│   └── engine.py          # action + free-text response logic (mock)
├── ui/
│   ├── __init__.py
│   ├── styles.py          # all custom CSS (SC colour palette lives here)
│   ├── banner.py          # compact top banner
│   ├── sidebar.py         # Quick Actions groups + buttons
│   ├── chat.py            # chat bubbles (bot/user) + code blocks
│   └── chat_input.py      # bottom "Type a message..." input
├── .streamlit/config.toml
└── requirements.txt
```

## Run
```bash
cd uaas_chatbot_sc
python -m venv .venv && source .venv/bin/activate   # optional
pip install -r requirements.txt
streamlit run app.py
```
Opens on port 8599 (set in `.streamlit/config.toml`).

## Where the colours live
- **`ui/styles.py`** — SC blue `#0473EA` (banner, user bubble, links, focus,
  sidebar hover) and SC green `#38D200` (banner dot, send button, code-block
  accent stripe).
- **`.streamlit/config.toml`** — `primaryColor = "#0473EA"`.

## Add a new action
1. Add an entry under the right group in `config/settings.py` (`ACTION_GROUPS`).
2. Add its reply in `bot/engine.py` (`ACTION_RESPONSES`).
The sidebar renders it automatically.

## Wire up the real UAAS backend
Replace the mock payloads in `bot/engine.py` with real REST/gRPC calls — the
UI layer never changes.
