# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 0.1, 0.2, ..., 1 кг конфет
try:
    price = int(input("Введите цену 1 кг конфет: "))

    if price <= 0:
        raise ValueError("Цена должна быть положительным числом")

    for i in range(1, 11):
        weight = i / 10
        price = price * weight
        print(f"Стоимость {weight} кг конфет: {price:.2f}")

except ValueError as error:
    print(f"Ошибка: {error}")
