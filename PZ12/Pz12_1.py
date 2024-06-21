#1.Из последовательности на n целых чисел создать новую последовательность, в
#которой каждый последующий элемент равен квадрату суммы двух соседних элементов.
import random
def create_new_sequence(arr):
    calculate_new_value = lambda i: arr[i + 1] ** 2 if i == 0 else ((arr[i - 1] + arr[i + 1]) ** 2) if i < len(
        arr) - 1 else arr[i - 1] ** 2

    for i in range(len(arr)):
        yield calculate_new_value(i)

    return arr




original_sequence = [random.randint(0, 5) for i in range(5)]
print(f'{original_sequence} - сгенерированная последовательность')
new_sequence = create_new_sequence(original_sequence)
print(list(new_sequence))
