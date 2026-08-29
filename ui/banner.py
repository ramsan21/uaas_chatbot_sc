"""Compact blue banner shown at the top of the main area."""
from __future__ import annotations
import streamlit as st
from config import settings
def render_banner() -> None:
    """Render the centered UAAS Chatbot banner with logo dot."""
    st.markdown(
        f"""
        <div class="uaas-banner">
            <span class="uaas-banner-dot"></span>{settings.APP_NAME}
        </div>
        """,
        unsafe_allow_html=True,
    )
