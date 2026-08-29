"""Pinned bottom chat input (Type a message...) handling."""
from __future__ import annotations
import streamlit as st
from bot import engine
from config import settings
from state import append_assistant, append_user
def render_chat_input() -> None:
    """Render the chat input; on submit, append user + bot messages."""
    prompt = st.chat_input(settings.CHAT_PLACEHOLDER)
    if prompt:
        append_user(prompt)
        append_assistant(engine.respond_to_text(prompt))
        st.rerun()  # re-render so the new messages appear immediately
