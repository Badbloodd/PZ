#Дано целое число N (1 < N < 26). Вывести N последних строчных (то есть маленьких)
#букв латинского алфавита в обратном порядке (начиная с буквы «z»).
def print_last_n_lowercase_letters_reversed(n):
    start = ord('z')
    for i in range(n):
        print(chr(start - i), end=' ')

n = int(input("Введите целое число N: "))
if 1 < n < 26:
    print_last_n_lowercase_letters_reversed(n)
else:
    print("Пожалуйста, введите целое число N от 2 до 25.")
