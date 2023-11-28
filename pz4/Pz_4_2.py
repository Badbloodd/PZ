try:
    N = int(input("Введите целое число больше нуля: "))

    count = 0
    total = 0

    for i in range(1, N+1):
        if N % i == 0:
            count += 1
            total += i

    print(f"Количество делителей: {count}")
    print(f"Сумма делителей: {total}")
except:
    print('Проверьте правильность введеных данных')