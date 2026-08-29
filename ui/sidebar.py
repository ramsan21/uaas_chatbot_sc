"""Sidebar Quick Actions panel: grouped expanders with action buttons."""
from __future__ import annotations
import streamlit as st
from bot import engine
from config import settings
from state import append_assistant, append_user
def render_sidebar() -> None:
    """Render Quick Actions; a button click appends user+bot messages."""
    with st.sidebar:
        st.markdown(
            f'<div class="uaas-side-title">{settings.SIDEBAR_HEADER}</div>',
            unsafe_allow_html=True,
        )
        for group in settings.ACTION_GROUPS:
            with st.expander(f"{group['icon']} **{group['title']}**", expanded=True):
                for action in group["actions"]:
                    if st.button(action["label"], key=f"qa-{action['id']}"):
                        append_user(action["label"])
                        append_assistant(engine.respond_to_action(action["id"]))
