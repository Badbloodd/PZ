#Дана строка-предложение на русском языке и число K (0 < K < 10). Зашифровать
#строку, выполнив циклическую замену каждой буквы на букву того же регистра,
#расположенную в алфавите на K-й позиции после шифруемой буквы (например, для
#K = 2 «А» перейдет в «В», «а» — в «в», «Б» — в «Г», «я» — в «б» и т. д.). Букву «ё»
#в алфавите не учитывать, знаки препинания и пробелы не изменять.
def encrypt_sentence(sentence, k):
    encrypted_sentence = ""
    for char in sentence:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            offset = (ord(char) - base + k) % 26
            encrypted_char = chr(base + offset)
            encrypted_sentence += encrypted_char
        else:
            encrypted_sentence += char
    return encrypted_sentence

input_sentence = input("Введите предложение на русском языке: ")
k = int(input("Введите число K (0 < K < 10): "))

if 0 < k < 10:
    encrypted_result = encrypt_sentence(input_sentence, k)
    print("Зашифрованное предложение:", encrypted_result)
else:
    print("Пожалуйста, введите число K в допустимом диапазоне.")
