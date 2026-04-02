import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password

def on_generate():
    try:
        length = int(length_entry.get())

        password = generate_password(
            length,
            upper_var.get(),
            digit_var.get(),
            symbol_var.get()
        )

        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter valid number")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root, text="Password Generator", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Enter Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar()
digit_var = tk.BooleanVar()
symbol_var = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate", command=on_generate).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state='readonly').pack()

root.mainloop()