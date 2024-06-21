#2. Из предложенного текстового файла (text18-5.txt) вывести на экран его содержимое,
#количество символов в тексте. Сформировать новый файл, в который поместить текст в
#стихотворной форме предварительно заменив символы нижнего регистра на верхний.
with open('text18-5.txt', 'r') as file:
    content = file.read()
    num_characters = len(content)
    print(f"Содержимое файла:\n{content}")
    print(f"Количество символов в файле: {num_characters}")

uppercase_content = content.upper()

with open('poem.txt', 'w') as file:
    file.write(uppercase_content)
    print("Текст успешно преобразован и записан в файл poem.txt")