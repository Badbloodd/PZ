try:
    price = float(input("Введите цену 1 кг конфет: "))

    for i in range(2, 21, 2):
        cost = price * (i / 10)
        print(f"Стоимость {i/10} кг конфет: {cost}")
except:
    print("Проверьте правильность введеных данных")
