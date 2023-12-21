def DigitCountSum(K):
    str_K = str(K)
    C = len(str_K)
    S = sum(int(digit) for digit in str_K)

    return C, S

input_numbers = input("Введите пять целых чисел через пробел: ")
numbers = list(map(int, input_numbers.split()))

for number in numbers:
    count, total_sum = DigitCountSum(number)
    print(f"Число: {number}, количество цифр: {count}, сумма цифр: {total_sum}")
