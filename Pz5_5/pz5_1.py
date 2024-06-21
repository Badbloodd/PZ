#С помощью функций получить вертикальную и горизонтальную линии.
#Линия проводится многократной печатью символа. Заключить слово в рамку из полученных линий
def get_input(message):
    user_input = input(message)
    return user_input

def print_horizontal_line(length, symbol):
    print(symbol * length)

def print_vertical_line(length, symbol):
    for _ in range(length):
        print(symbol + " " + " " * (length - 4) + " " + symbol)

def print_word_in_frame():
    word = get_input("Введите слово для отображения в рамке: ")
    symbol = get_input("Введите символ для рамки: ")
    length = len(word) + 4

    print_horizontal_line(length, symbol)
    print_vertical_line(length, symbol)
    print(symbol + " " + word + " " + symbol)
    print_vertical_line(length, symbol)
    print_horizontal_line(length, symbol)

print_word_in_frame()
