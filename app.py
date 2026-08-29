"""UAAS Chatbot - Streamlit entry point.
Run:  streamlit run app.py      (defaults to port 8599 via .streamlit/config.toml)
"""
import streamlit as st
from config import settings
from state import get_history, init_session_state
from ui.banner import render_banner
from ui.chat import render_chat_history
from ui.chat_input import render_chat_input
from ui.sidebar import render_sidebar
from ui.styles import inject_custom_css
# Must be the first Streamlit command
st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="\U0001F4AC",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject_custom_css()
init_session_state()
render_sidebar()                 # quick actions may append new messages
render_banner()                  # compact blue "UAAS Chatbot" banner
render_chat_history(get_history())  # bot/user bubbles from session state
render_chat_input()              # pinned "Type a message..." input
