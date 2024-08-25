from gtts import gTTS
import os

def say_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("afplay output.mp3")
    os.remove("output.mp3")