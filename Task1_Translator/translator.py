from googletrans import Translator

translator = Translator()

print("=== Language Translator ===")
text = input("Enter text: ")

translated = translator.translate(text, dest='ur')

print("Translated Text:", translated.text)
