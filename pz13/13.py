#1. В матрице элементы второго столбца возвести в квадрат.
#2. Сгенерировать матрицу, в которой нечетные элементы заменяются на 0.
import random

# Создание случайной матрицы
create_random_matrix = lambda rows, cols, min_val, max_val: [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

# Возводит элементы второго столбца в квадрат
square_second_column = lambda matrix: [[row[i] ** 2 if i == 1 else row[i] for i in range(len(row))] for row in matrix]

# Заменяет нечетные на 0
replace_odd_elements = lambda matrix: [[0 if element % 2 != 0 else element for element in row] for row in matrix]

# Функция вывода матрицы
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Создаю матрицу
def main():
    rows = 4
    cols = 4
    min_val = 1
    max_val = 9

    matrix = create_random_matrix(rows, cols, min_val, max_val)
    print("Исходная матрица:")
    print_matrix(matrix)

    matrix = square_second_column(matrix)
    print("\nМатрица после возведения в квадрат элементов второго столбца:")
    print_matrix(matrix)

    matrix = replace_odd_elements(matrix)
    print("\nМатрица после замены нечетных элементов на 0:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()
