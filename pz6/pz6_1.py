#Дано целое число N (>2). Сформировать и вывести целочисленный список размера
#10, содержащий 10 первых элементов последовательности чисел Фибоначчи FK: F1
#= 1, F2 = 1, FK = FK-2 + FK-1, K = 3,4,... .
def fibonacci_sequence(n):
    fib_sequence = [1, 1]
    for k in range(2, n):
        next_fib = fib_sequence[k-1] + fib_sequence[k-2]
        fib_sequence.append(next_fib)
    return fib_sequence

N = int(input("Введите целое число N (> 2): "))
if N > 2:
    fib_list = fibonacci_sequence(10)
    print(fib_list)
else:
    print("Число N должно быть больше 2")
