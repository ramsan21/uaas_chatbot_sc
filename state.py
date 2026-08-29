"""Session-state management.
All conversation history lives in ``st.session_state`` so the chat survives
Streamlit reruns (quick-action clicks, chat-input submits, expander toggles).
"""
from __future__ import annotations
import streamlit as st
from config import settings
MESSAGES_KEY = "uaas.messages"
Message = dict  # {"role": "user" | "assistant", "content": str, "avatar": str}
def init_session_state() -> None:
    """Create default keys exactly once per browser session."""
    if MESSAGES_KEY not in st.session_state:
        st.session_state[MESSAGES_KEY] = [
            {
                "role": "assistant",
                "avatar": "\U0001F916",
                "content": (
                    f"\U0001F44B Hello! I'm the **{settings.APP_NAME}**.\n\n"
                    f"{settings.WELCOME_BODY}"
                ),
            }
        ]
def get_history() -> list[Message]:
    """Return the full chat history."""
    return st.session_state[MESSAGES_KEY]
def append_user(content: str) -> None:
    """Append a user message to the history."""
    st.session_state[MESSAGES_KEY].append(
        {"role": "user", "avatar": "\U0001F9D1", "content": content}
    )
def append_assistant(content: str, avatar: str = "\U0001F916") -> None:
    """Append a bot message to the history."""
    st.session_state[MESSAGES_KEY].append(
        {"role": "assistant", "avatar": avatar, "content": content}
    )
