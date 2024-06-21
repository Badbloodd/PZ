# Мастям игральных карт присвоены порядковые номера: 1– пики, 2 – трефы, 3 –
# бубны, 4 – червы. Достоинству карт, старших десятки, присвоены номера: 11 – валет,
# 12 – дама, 13 – король, 14 – туз. Дано трехзначное число, в котором первая цифра
# указывает на масть, а вторые две на достоинство карты. Вывести соответствующее
# название карты вида «дама червей», «туз треф» и т.п
number = input("Введите трехзначное число: ")
card_value = int(number)
suit = card_value // 100
value = card_value % 100
if suit < 1 or suit > 4 or value < 1 or value > 14:
        print("Ошибка: введены недопустимые значения")
else:
        if value == 11:
            value_name = 'валет'
        elif value == 12:
            value_name = 'дама'
        elif value == 13:
            value_name = 'король'
        elif value == 14:
            value_name = 'туз'
        else:
            value_name = str(value)

        if suit == 1:
            suit_name = 'пики'
        elif suit == 2:
            suit_name = 'трефы'
        elif suit == 3:
            suit_name = 'бубны'
        elif suit == 4:
            suit_name = 'червы'

        print(f"Соответствующая карта: {value_name} {suit_name}")
