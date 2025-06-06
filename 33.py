import tkinter as tk

root = tk.Tk()
root.title("Программа 33")
root.configure(bg="blue")
root.geometry("400x300")

label = tk.Label(root, text="Обновление применено!", bg="blue", fg="white", font=("Arial", 16))
label.pack(expand=True)

root.mainloop()

