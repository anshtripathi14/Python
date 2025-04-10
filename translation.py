import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
import os

def text_to_text_translation():
    translator = Translator()
    print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))
    target_language = input("Enter target language code (e.g., 'en', 'hi'): ").strip()
    while target_language not in LANGUAGES:
        target_language = input("Invalid code. Try again (e.g., 'en', 'hi'): ").strip()
    while True:
        text = input("Enter text ('stop' to exit): ").strip()
        if text.lower() == "stop":
            break
        translated_text = translator.translate(text, dest=target_language).text
        print(f"Translated ({LANGUAGES[target_language].capitalize()}): {translated_text}")

def text_to_voice_translation():
    translator = Translator()
    print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))
    target_language = input("Enter target language code (e.g., 'en', 'hi'): ").strip()
    while target_language not in LANGUAGES:
        target_language = input("Invalid code. Try again (e.g., 'en', 'hi'): ").strip()
    while True:
        text = input("Enter text ('stop' to exit): ").strip()
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

def voice_to_text_translation():
    translator = Translator()
    print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))
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
        print(f"Recognized: {input_text}")
        translated_text = translator.translate(input_text, dest=target_language).text
        print(f"Translated: {translated_text}")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except Exception as e:
        print(f"Error: {e}")

def voice_to_voice_translation():
    translator = Translator()
    print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))
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
    print("Translation Options:")
    print("1: Text to Text Translation")
    print("2: Text to Voice Translation")
    print("3: Voice to Text Translation")
    print("4: Voice to Voice Translation")

    choice = int(input("Enter your choice (1-4): ").strip())

    match choice:
        case 1:
            text_to_text_translation()
        case 2:
            text_to_voice_translation()
        case 3:
            voice_to_text_translation()
        case 4:
            voice_to_voice_translation()
        case _:
            print("Invalid choice. Exiting...")
