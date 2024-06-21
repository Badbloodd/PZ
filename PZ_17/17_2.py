# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 2 – 9
import tkinter as tk
from tkinter import messagebox


def calculate_distance():
    try:
        v1 = int(entry_v1.get())
        v2 = int(entry_v2.get())
        T = int(entry_T.get())
        S = int(entry_S.get())

        if v1 <= 0 or v2 <= 0 or T <= 0 or S <= 0:
            raise ValueError

        distance = (v1 + v2) * T - S
        result_label.config(text=f"Расстояние между автомобилями через {T} часов: {distance} км")
    except ValueError:
        messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные положительные числа.")


# Создание главного окна
root = tk.Tk()
root.title("Расчет расстояния между автомобилями")

# Создание и размещение виджетов
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Скорость первого автомобиля (км/ч):").grid(row=0, column=0, sticky='w')
entry_v1 = tk.Entry(frame)
entry_v1.grid(row=0, column=1)

tk.Label(frame, text="Скорость второго автомобиля (км/ч):").grid(row=1, column=0, sticky='w')
entry_v2 = tk.Entry(frame)
entry_v2.grid(row=1, column=1)

tk.Label(frame, text="Время (ч):").grid(row=2, column=0, sticky='w')
entry_T = tk.Entry(frame)
entry_T.grid(row=2, column=1)

tk.Label(frame, text="Начальное расстояние (км):").grid(row=3, column=0, sticky='w')
entry_S = tk.Entry(frame)
entry_S.grid(row=3, column=1)

tk.Button(frame, text="Рассчитать", command=calculate_distance).grid(row=4, columnspan=2)

result_label = tk.Label(frame, text="")
result_label.grid(row=5, columnspan=2)

# Запуск главного цикла приложения
root.mainloop()
