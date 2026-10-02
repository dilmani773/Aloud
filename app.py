import streamlit as st

from src.prompts import MED_WARNING, RETAKE
from src.reader import read_image
from src.tts import speak
from src.ui import apply_style, show_text, show_warning

st.set_page_config(page_title="Aloud", page_icon="🔊", layout="centered")
apply_style()

# Voice picker for week-1 testing only. Remove before giving to users.
with st.sidebar:
    engine = st.radio("Voice (testing)", ["gtts", "mms"])


def play(text):
    audio, fmt = speak(text, engine)
    st.audio(audio, format=fmt, autoplay=True)


st.title("🔊 කියවන්න")
photo = st.camera_input("ලියුමේ photo එකක් ගන්න")

if photo and st.button("කියවන්න"):
    with st.spinner("කියවමින්..."):
        try:
            r = read_image(photo.getvalue(), photo.type or "image/jpeg",
                           st.secrets["ANTHROPIC_API_KEY"])
        except Exception as e:
            st.error(f"Error: {e}")
            st.stop()

    if not r.get("readable"):
        show_warning(RETAKE)
        play(RETAKE)
        st.stop()

    spoken = " ".join(p for p in [r.get("summary", ""), r.get("text", "")] if p)
    if r.get("is_medicine"):
        show_warning(MED_WARNING)
        spoken += " " + MED_WARNING

    show_text(r.get("summary", ""), r.get("text", ""))
    play(spoken)
