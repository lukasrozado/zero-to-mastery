from translate import Translator

translator = Translator(to_lang="pt")

try:
    with open("./test.txt", mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open("./test-pt.txt", mode="w") as my_translation:
            my_translation.write(translation)
except FileNotFoundError as e:
    print("Check your file path")

print(translation)
