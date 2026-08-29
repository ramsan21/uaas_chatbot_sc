"""Custom CSS injected once per run via st.markdown(unsafe_allow_html=True).
Replicates the UAAS Chatbot look: compact banner, sidebar quick-action
buttons, chat bubbles, and hides Streamlit's default menu/whitespace.
"""
from __future__ import annotations
import streamlit as st
CSS = """
<style>
/* ================= 1. Hide Streamlit default chrome ================= */
#MainMenu { visibility: hidden !important; }
footer { visibility: hidden !important; }
header[data-testid="stHeader"] { display: none !important; }
div[data-testid="stDecoration"] { display: none !important; }
div[data-testid="stStatusWidget"] { visibility: hidden !important; }
/* ================= 2. Page layout / whitespace ================= */
.stApp { background: #ffffff; }
.stApp, .stApp button, .stApp input, .stApp textarea {
    font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
}
.block-container {
    padding-top: 1.1rem !important;
    padding-bottom: 7.5rem !important;   /* room for the pinned chat input */
    max-width: 1250px;
}
/* ================= 3. Compact blue banner ================= */
.uaas-banner {
    background: linear-gradient(180deg, #0473EA 0%, #045fc0 100%);
    color: #ffffff;
    font-size: 1.12rem;
    font-weight: 600;
    text-align: center;
    padding: 12px 16px;
    border-radius: 6px;
    margin-bottom: 14px;
    box-shadow: 0 2px 6px rgba(13, 60, 120, 0.25);
}
.uaas-banner .uaas-banner-dot {
    display: inline-block;
    width: 11px; height: 11px;
    border-radius: 50%;
    background: #38D200;
    margin-right: 9px;
    vertical-align: middle;
    box-shadow: 0 0 0 3px rgba(56, 210, 0, 0.35);
}
/* ================= 4. Chat bubbles ================= */
.uaas-row { display: flex; align-items: flex-start; gap: 10px; margin: 10px 0; }
.uaas-row-user { justify-content: flex-end; }
.uaas-avatar {
    flex: 0 0 auto;
    width: 40px; height: 40px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 21px;
    background: #eaf2ff;
    border: 1px solid #bcd8ff;
}
.uaas-bubble {
    padding: 12px 16px;
    border-radius: 14px;
    max-width: 80%;
    font-size: 0.98rem;
    line-height: 1.55;
    overflow-wrap: anywhere;
}
.uaas-bubble-bot {
    background: #f2f4f7;
    border: 1px solid #e4e8ee;
    color: #1f2430;
    border-top-left-radius: 4px;
}
.uaas-bubble-user {
    background: #0473EA;
    color: #ffffff;
    border-top-right-radius: 4px;
}
.uaas-bubble code {
    background: #ffffff;
    border: 1px solid #bcd8ff;
    border-radius: 5px;
    padding: 1px 5px;
    font-size: 0.86em;
    color: #0473EA;
    font-family: Consolas, "Courier New", monospace;
}
.uaas-bubble-user code {
    background: rgba(255, 255, 255, 0.16);
    border-color: rgba(255, 255, 255, 0.35);
    color: #ffffff;
}
.uaas-pre {
    background: #101828;
    color: #e6ebf2;
    border-left: 3px solid #38D200;
    padding: 10px 14px;
    border-radius: 10px;
    font-size: 0.85rem;
    overflow-x: auto;
    margin: 6px 0 2px 0;
    font-family: Consolas, "Courier New", monospace;
}
/* collapse the gaps Streamlit adds around our markdown message blocks */
div[data-testid="element-container"]:has(.uaas-row) { margin-bottom: 0 !important; }
/* ================= 5. Sidebar - Quick Actions ================= */
section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e7eaf0;
}
section[data-testid="stSidebar"] .block-container {
    padding-top: 0.6rem !important;
    padding-bottom: 2rem !important;
}
/* Streamlit reserves a 60px logo/collapse-button header row even when hidden;
   collapse it so the sidebar content starts right at the top. */
[data-testid="stSidebarHeader"] { display: none !important; }
.uaas-side-title {
    font-size: 1.18rem;
    font-weight: 700;
    color: #0f172a;
    margin: 0 0 12px 2px;
}
section[data-testid="stSidebar"] div[data-testid="stExpander"],
section[data-testid="stSidebar"] details[data-testid="stExpander"] {
    border: 1px solid #d8dee7 !important;
    border-left: 3px solid #0473EA !important;
    border-radius: 9px !important;
    background: #ffffff !important;
    box-shadow: 0 1px 2px rgba(16, 24, 40, 0.05);
    margin-bottom: 6px;
}
section[data-testid="stSidebar"] summary { font-size: 1rem; }
section[data-testid="stSidebar"] summary strong { color: #0473EA; }
/* tighten the gap Streamlit's flex layout inserts between stacked items */
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0 !important; }
section[data-testid="stSidebar"] [data-testid="stVerticalBlock"]:has(> [data-testid="stExpander"]) {
    gap: 6px !important;
}
section[data-testid="stSidebar"] .stButton > button {
    width: fit-content;
    border: none !important;
    background: #ffffff;
    color: #17202c;
    border-radius: 7px;
    padding: 4px 14px;
    font-size: 0.95rem;
    font-weight: 500;
    margin: 0 !important;
    box-shadow: 0 1px 1.5px rgba(16, 24, 40, 0.07);
}
section[data-testid="stSidebar"] .stButton > button:hover {
    color: #0473EA;
    background: #eef6ff;
}
section[data-testid="stSidebar"] .stButton > button:active,
section[data-testid="stSidebar"] .stButton > button:focus:not(:hover) {
    color: #1a8a00 !important;
    background: #eafcea !important;
}
/* hide the sidebar collapse chevron for exact-match look */
section[data-testid="stSidebar"] [data-testid="stSidebarCollapseButton"],
section[data-testid="stSidebar"] button[kind="header"] { display: none; }
/* ================= 6. Pinned chat input ================= */
div[data-testid="stBottom"] { background: transparent; }
div[data-testid="stBottom"] > div { max-width: 1250px; margin: 0 auto; }
[data-testid="stChatInput"] {
    border-radius: 999px;
    border: 1px solid #cfd6e0 !important;
    box-shadow: 0 3px 10px rgba(16, 24, 40, 0.08);
    background: #ffffff;
}
[data-testid="stChatInput"]:focus-within { border-color: #0473EA !important; }
[data-testid="stChatInput"] textarea { font-size: 1rem; }
[data-testid="stChatInput"] textarea::placeholder { color: #98a2b3; }
[data-testid="stChatInputSubmitButton"],
[data-testid="stChatInputSubmitButton"] button,
button[aria-label="Send"] {
    background: #38D200 !important;
    border-radius: 50% !important;
    color: #ffffff !important;
}
[data-testid="stChatInputSubmitButton"] svg,
button[aria-label="Send"] svg { fill: #ffffff !important; color: #ffffff !important; }
</style>
"""
def inject_custom_css() -> None:
    """Inject the global stylesheet (call once, right after set_page_config)."""
    st.markdown(CSS, unsafe_allow_html=True)
