"""Chat-history rendering: bot/user bubbles built from HTML + injected CSS."""
from __future__ import annotations
import html
import re
import streamlit as st
def _inline(text: str) -> str:
    """Escape HTML, then apply a tiny Markdown subset (**bold**, `code`)."""
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    return escaped
def _to_html(content: str) -> str:
    """Convert message text (with optional ``` blocks) into bubble HTML."""
    parts = content.split("```")
    rendered = []
    for index, part in enumerate(parts):
        if index % 2 == 0:
            rendered.append(_inline(part).replace("\n", "<br>"))
        else:
            code = part.strip("\n")
            # drop a leading language identifier line (e.g. ``` json)
            if "\n" in code:
                first, rest = code.split("\n", 1)
                if first.strip().isalpha() and len(first.strip()) <= 12:
                    code = rest
            # Use a <div> (Streamlit rewrites <pre> and drops custom classes)
            # with explicit <br> so line breaks survive whitespace collapse.
            rendered.append(
                "<div class='uaas-pre'>"
                + html.escape(code).replace("\n", "<br>")
                + "</div>"
            )
    return "".join(rendered)
def render_chat_history(messages: list[dict]) -> None:
    """Render every message in the session history."""
    for message in messages:
        render_message(message)
def render_message(message: dict) -> None:
    """Render a single bot or user chat bubble with avatar."""
    role = message["role"]
    avatar = message.get("avatar", "\U0001F916" if role == "assistant" else "\U0001F9D1")
    body = _to_html(message["content"])
    # NOTE: flush-left, newline-free HTML so Streamlit's markdown does not
    # treat the indented block as a code block (which flattens <pre>).
    if role == "assistant":
        block = (
            "<div class='uaas-row uaas-row-bot'>"
            f"<div class='uaas-avatar'>{avatar}</div>"
            f"<div class='uaas-bubble uaas-bubble-bot'>{body}</div>"
            "</div>"
        )
    else:
        block = (
            "<div class='uaas-row uaas-row-user'>"
            f"<div class='uaas-bubble uaas-bubble-user'>{body}</div>"
            f"<div class='uaas-avatar'>{avatar}</div>"
            "</div>"
        )
    st.markdown(block, unsafe_allow_html=True)
