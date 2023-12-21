#Дан список размера N. Обнулить все его локальные максимумы (то есть числа,большие своих соседей).
def zero_local_max(numbers):
    n = len(numbers)
    for i in range(1, n - 1):
        if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
            numbers[i] = 0
    return numbers

input_list = [1, 3, 2, 5, 4, 6, 8, 5, 7]
result = zero_local_max(input_list)
print(result)
