import random

# Функция для создания случайной матрицы
def create_random_matrix(rows, cols, min_val, max_val):
    matrix = []
    for i in range(rows):
        row = [random.randint(min_val, max_val) for i in range(cols)]
        matrix.append(row)
    return matrix

# Функция для замены нечетных элементов на 0
def replace_odd_elements(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 != 0:
                matrix[i][j] = 0
    return matrix

# Функция для печати матрицы
def print_matrix(matrix):
    for row in matrix:
        print(row)

# Создаем случайную матрицу размером 4x4
rows = 4
cols = 4
min_val = 1
max_val = 9
matrix = create_random_matrix(rows, cols, min_val, max_val)
print("Исходная матрица:")
print_matrix(matrix)

# Заменяем нечетные элементы на 0
matrix = replace_odd_elements(matrix)

print("\nМатрица после замены нечетных элементов на 0:")
print_matrix(matrix)
