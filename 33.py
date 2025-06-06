import tkinter as tk

root = tk.Tk()
root.title("Обновление")
root.geometry("800x600")
root.configure(bg="red")

label = tk.Label(root, text="Программа обновлена222", font=("Arial", 28), fg="white", bg="red")
label.pack(expand=True)

root.mainloop()
