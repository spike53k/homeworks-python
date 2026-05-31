import tkinter as tk

def calculate(_):
    bill = float(entry.get())
    percent = scale.get()

    tips = bill * (percent / 100)
    total = bill + tips

    label_result.config(text=f"Чаевые: {tips:}\nИтого: {total:}")

window = tk.Tk()
window.title("Личный кассир")
window.geometry("300x300")

tk.Label(window, text="Сумма счета:").pack(pady=5)
entry = tk.Entry(window)
entry.pack(pady=5)

scale = tk.Scale(window, from_=5, to=25, orient="horizontal", command=calculate)
scale.pack(pady=10)

label_result = tk.Label(window, text="Результат", font=("Arial", 12))
label_result.pack(pady=10)

window.mainloop()