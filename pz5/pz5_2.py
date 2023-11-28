def DigitCountSum(K):
    C = len(str(K))
    S = sum(int(digit) for digit in str(K))
    return C, S


numbers = [123, 4567, 89012, 345678, 9012345]
for number in numbers:
    count, total = DigitCountSum(number)
    print(f"Число: {number}, количество цифр: {count}, сумма цифр: {total}")
