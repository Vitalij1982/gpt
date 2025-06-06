import tkinter as tk

root = tk.Tk()
root.title("Программа 33")
root.geometry("400x300")

label = tk.Label(root, text="24", font=("Arial", 72), fg="black")
label.pack(expand=True)

root.mainloop()
