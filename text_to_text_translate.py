from googletrans import LANGUAGES, Translator
print("Languages:", ", ".join([f"{k}: {v}" for k, v in LANGUAGES.items()]))
translator = Translator()
lan = input("Choose language code (e.g., 'en'): ").strip()
while lan not in LANGUAGES:
    lan = input("Invalid code. Try again (e.g., 'en'): ").strip()
while True:
    text = input("Enter text ('change' to switch language, 'stop' to exit): ").strip()
    if text.lower() == "stop":
        break
    if text.lower() == "change":
        lan = input("New language code (e.g., 'en'): ").strip()
        while lan not in LANGUAGES:
            lan = input("Invalid code. Try again (e.g., 'en'): ").strip()
    else:
        translated_text = translator.translate(text, dest=lan).text
        print(f"Translated ({LANGUAGES[lan].capitalize()}): {translated_text}")
        