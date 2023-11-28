def draw_horizontal_line(symbol, length):
    horizontal_line = symbol * length
    print(horizontal_line)


def draw_vertical_line(symbol, height):
    for _ in range(height):
        print(symbol)


def draw_word_in_box(word, symbol):
    word_length = len(word)
    horizontal_line = symbol * (word_length + 4)

    print(horizontal_line)
    print(f"{symbol} {word} {symbol}")
    print(horizontal_line)


symbol_h = input("Введите символ для горизонтальной линии: ")
length_h = int(input("Введите длину горизонтальной линии: "))
draw_horizontal_line(symbol_h, length_h)

symbol_v = input("Введите символ для вертикальной линии: ")
height_v = int(input("Введите высоту вертикальной линии: "))
draw_vertical_line(symbol_v, height_v)

word = input("Введите слово для отображения в рамке: ")
symbol_b = input("Введите символ для рамки: ")
draw_word_in_box(word, symbol_b)
