import gTTS as gtts
import BytesIO as io

io.title("🔊 Pronunciation Practice")

word = io.text_input("Enter a word to hear it:")

if word:
    tts = gTTS(word)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    io.audio(audio_fp.getvalue(), format="audio/mp3")
