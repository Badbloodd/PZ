# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу (см. таблицу 1)
import tkinter as tk
from tkinter import ttk

# Инициализация окна
root = tk.Tk()
root.title("Order Form")
root.geometry("400x600")
root.configure(bg='#ccd27b')

# Установка стилей
style = ttk.Style()
style.configure('TFrame', background='#ccd27b')
style.configure('TLabel', background='#ccd27b', font=('Helvetica', 10))
style.configure('TEntry', font=('Helvetica', 10))
style.configure('TRadiobutton', background='#ccd27b', font=('Helvetica', 10))

# Создание фреймов для каждой секции
frame_details = ttk.Frame(root, padding=10)
frame_details.pack(pady=10, padx=10, fill='x')

frame_address = ttk.Frame(root, padding=10)
frame_address.pack(pady=10, padx=10, fill='x')

frame_card = ttk.Frame(root, padding=10)
frame_card.pack(pady=10, padx=10, fill='x')

# Добавление элементов в секцию "Ваши данные"
ttk.Label(frame_details, text="Step 1: Your details", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

ttk.Label(frame_details, text="Name").grid(row=1, column=0, sticky="w")
entry_name = ttk.Entry(frame_details, width=30)
entry_name.grid(row=1, column=1, pady=5)

ttk.Label(frame_details, text="Email").grid(row=2, column=0, sticky="w")
entry_email = ttk.Entry(frame_details, width=30)
entry_email.grid(row=2, column=1, pady=5)

ttk.Label(frame_details, text="Phone").grid(row=3, column=0, sticky="w")
entry_phone = ttk.Entry(frame_details, width=30)
entry_phone.grid(row=3, column=1, pady=5)

# Добавление элементов в секцию "Адрес доставки"
ttk.Label(frame_address, text="Step 2: Delivery address", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

ttk.Label(frame_address, text="Address").grid(row=1, column=0, sticky="w")
text_address = tk.Text(frame_address, width=30, height=4)
text_address.grid(row=1, column=1, pady=5)

ttk.Label(frame_address, text="Post code").grid(row=2, column=0, sticky="w")
entry_postcode = ttk.Entry(frame_address, width=30)
entry_postcode.grid(row=2, column=1, pady=5)

ttk.Label(frame_address, text="Country").grid(row=3, column=0, sticky="w")
entry_country = ttk.Entry(frame_address, width=30)
entry_country.grid(row=3, column=1, pady=5)

# Добавление элементов в секцию "Детали карты"
ttk.Label(frame_card, text="Step 3: Card details", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="w")

ttk.Label(frame_card, text="Card type").grid(row=1, column=0, sticky="w")
frame_card_type = ttk.Frame(frame_card)
frame_card_type.grid(row=1, column=1, pady=5, sticky="w")

card_type = tk.StringVar()
ttk.Radiobutton(frame_card_type, text="VISA", variable=card_type, value="VISA").pack(side='left')
ttk.Radiobutton(frame_card_type, text="AmEx", variable=card_type, value="AmEx").pack(side='left')
ttk.Radiobutton(frame_card_type, text="Mastercard", variable=card_type, value="Mastercard").pack(side='left')

ttk.Label(frame_card, text="Card number").grid(row=2, column=0, sticky="w")
entry_card_number = ttk.Entry(frame_card, width=30)
entry_card_number.grid(row=2, column=1, pady=5)

ttk.Label(frame_card, text="Security code").grid(row=3, column=0, sticky="w")
entry_security_code = ttk.Entry(frame_card, width=30)
entry_security_code.grid(row=3, column=1, pady=5)

ttk.Label(frame_card, text="Name on card").grid(row=4, column=0, sticky="w")
entry_card_name = ttk.Entry(frame_card, width=30)
entry_card_name.grid(row=4, column=1, pady=5)

# Кнопка "BUY IT!"
btn_buy = tk.Button(root, text="BUY IT!", font=('Helvetica', 12, 'bold'), bg='#a4a244', fg='white')
btn_buy.pack(pady=10)
root.mainloop()
