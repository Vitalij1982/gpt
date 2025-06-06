import tkinter as tk

root = tk.Tk()
root.title("Обновление")
root.geometry("800x600")
root.configure(bg="blue")  # Устанавливаем синий фон

label = tk.Label(root, text="Программа обновлена", font=("Arial", 28), fg="white", bg="blue")
label.pack(expand=True)

root.mainloop()
