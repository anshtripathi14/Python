import speech_recognition as sr
from googletrans import Translator, LANGUAGES

def voice_to_text_translator():
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

if __name__ == "__main__":
    voice_to_text_translator()
    