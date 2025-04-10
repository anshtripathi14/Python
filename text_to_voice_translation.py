from gtts import gTTS
from googletrans import Translator, LANGUAGES
from playsound import playsound
import os

def text_to_voice_translator():
    translator = Translator()
    print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))

    target_language = input("Enter target language code (e.g., 'en', 'hi'): ").strip()
    while target_language not in LANGUAGES:
        target_language = input("Invalid code. Try again (e.g., 'en', 'hi'): ").strip()

    while True:
        text = input("Enter text to translate ('stop' to exit): ").strip()
        if text.lower() == "stop":
            break

        translated_text = translator.translate(text, dest=target_language).text
        print(f"Translated: {translated_text}")

        try:
            tts = gTTS(text=translated_text, lang=target_language)
            tts.save("translated_speech.mp3")
            playsound("translated_speech.mp3")
            os.remove("translated_speech.mp3")
        except Exception as e:
            print(f"Error generating speech: {e}")

if __name__ == "__main__":
    text_to_voice_translator()
    