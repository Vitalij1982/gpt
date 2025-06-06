import tkinter as tk

root = tk.Tk()
root.title("Программа 33")
root.geometry("800x600")  # Увеличим размер, чтобы было видно

# Создаём фрейм на весь экран с синим фоном
frame = tk.Frame(root, bg="blue")
frame.pack(fill="both", expand=True)

# Надпись по центру
label = tk.Label(frame, text="Обновление применено!", bg="blue", fg="white", font=("Arial", 24))
label.pack(expand=True)

root.mainloop()
