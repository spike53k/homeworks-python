import tkinter as tk


def show_price():
    price = size.get()

    if cheese.get():
        price += 30
    if mushrooms.get():
        price += 30
    if sausage.get():
        price += 30

    label_result.config(text=f"Цена: {price} руб")

window = tk.Tk()
window.geometry("300x300")
window.title("Пиццерия")

size = tk.IntVar(value=100)

tk.Radiobutton(window, text="Маленькая (100р)", variable=size, value=100).pack()
tk.Radiobutton(window, text="Средняя (200р)", variable=size, value=200).pack()
tk.Radiobutton(window, text="Большая (300р)", variable=size, value=300).pack()

cheese = tk.BooleanVar()
mushrooms = tk.BooleanVar()
sausage = tk.BooleanVar()

tk.Checkbutton(window, text="Сыр", variable=cheese).pack()
tk.Checkbutton(window, text="Грибы", variable=mushrooms).pack()
tk.Checkbutton(window, text="Колбаса", variable=sausage).pack()

tk.Button(window, text="Показать стоимость", command=show_price).pack(pady=10)

label_result = tk.Label(window, text="Цена", font=("Arial", 12))
label_result.pack()

window.mainloop()