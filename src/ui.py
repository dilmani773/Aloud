import streamlit as st

CSS = """
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;700&display=swap" rel="stylesheet">
<style>
html, body, .stApp { background:#FFF8E1; color:#000; font-family:'Noto Sans Sinhala', sans-serif; font-size:22px; }
h1 { font-size:48px !important; text-align:center; }
div.stButton > button { width:100%; height:110px; font-size:44px; font-weight:700;
  background:#0B3D91; color:#fff; border:none; border-radius:18px; }
div.stButton > button:focus { outline:6px solid #FFB300; }
.read-text { font-size:30px; line-height:1.7; background:#fff; padding:20px; border-radius:12px; }
.warn { font-size:28px; font-weight:700; background:#FFB300; color:#000; padding:18px; border-radius:12px; }
</style>
"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def show_warning(text: str):
    st.markdown(f'<div class="warn">⚠️ {text}</div>', unsafe_allow_html=True)


def show_text(summary: str, text: str):
    st.markdown(f'<div class="read-text">{summary}<br><br>{text}</div>', unsafe_allow_html=True)
