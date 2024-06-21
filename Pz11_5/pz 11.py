#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Сумма элементов:
#Элементы, умноженные на минимальный элемент:
import random

# Генерируем последовательность целых чисел
with open('new_text.txt', 'w') as file:
    sequence = [random.randint(-100, 100) for _ in range(10)]
    file.write(str(sequence))
# Находим минимальный элемент
min_element = min(sequence)

# Выполняем требуемую обработку
processed_sequence = [element * min_element for element in sequence]

# Записываем данные в текстовый файл
with open('original_data.txt', 'w') as file:
    file.write("Исходные данные:\n")
    file.write(f"Количество элементов: {len(sequence)}\n")
    file.write(f"Сумма элементов: {sum(sequence)}\n")
    file.write("Элементы, умноженные на минимальный элемент:\n")
    for element in processed_sequence:
        file.write(f"{element}\n")
with open('original_data.txt', 'r') as file:
    print(file.read())
with open('new_text.txt', 'r') as file:
    print(file.read())