# Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые
# маски» перенести в первый файл строки с нулевым четвертым октетом, а во второй
# – все остальные. Посчитать количество полученных строк в каждом файле
import re

# Открыть исходный файл
with open("ip_address.txt", "r") as f:
    lines = f.readlines()

# Создать два новых файла
with open("zero_fourth_octet.txt", "w") as f1, open("non_zero_fourth_octet.txt", "w") as f2:
    # Перебрать строки из исходного файла
    count1 = 0
    count2 = 0
    for line in lines:
        if re.match(r"^(?:\d{1,3}\.){3}0$", line):
            f1.write(line)
            count1 += 1
        else:
            f2.write(line)
            count2 += 1

# Вывести количество строк в каждом файле
print("Количество строк в zero_fourth_octet.txt:", count1)
print("Количество строк в non_zero_fourth_octet.txt:", count2)
