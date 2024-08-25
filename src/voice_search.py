import speech_to_text as stt
import google_search as gsearch
import say
import time

# if __name__ == "__main__":
say.say_text("Hi there, Let me know what do you want me to search.")
recognized_text = stt.recognize_speech()
if recognized_text:
    results = gsearch.google_search(recognized_text)
    print("from top Google Search Results:")
    print(results)