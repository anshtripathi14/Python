import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator, LANGUAGES
from playsound import playsound
import os

def voice_to_voice_translator():
    translator = Translator()
    print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))
    
    # Validate language code
    target_language = input("Enter target language code (e.g., 'en', 'hi'): ").strip()
    while target_language not in LANGUAGES:
        target_language = input("Invalid code. Try again (e.g., 'en', 'hi'): ").strip()

    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Say something...")
            audio = recognizer.listen(source, timeout=10)
        input_text = recognizer.recognize_google(audio)
        print(f"Input: {input_text}")

        translated_text = translator.translate(input_text, dest=target_language).text
        print(f"Translated: {translated_text}")

        tts = gTTS(text=translated_text, lang=target_language)
        tts.save("translated_speech.mp3")
        playsound("translated_speech.mp3")
        os.remove("translated_speech.mp3")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    voice_to_voice_translator()
    