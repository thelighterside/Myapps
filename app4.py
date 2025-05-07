from gtts import gTTS
from io import BytesIO
import streamlit as st  # Add this if not already included

st.title("🔊 Pronunciation Practice")

word = st.text_input("Enter a word to hear it:")

if word:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)  # ← Minimal necessary change
    st.audio(audio_fp.getvalue(), format="audio/mp3")
