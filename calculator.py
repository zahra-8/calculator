import tkinter as tk
from tkinter import ttk

def on_click(button_value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")

# Style for themed buttons
style = ttk.Style()
style.configure("TButton", padding=10, font=('Arial', 16))

# Entry widget for displaying input and result
entry = tk.Entry(root, width=15, font=('Arial', 24), bd=10, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(root, text=button, style="TButton", command=lambda button=button: on_click(button) if button != '=' else calculate_result()).grid(row=row_val, column=col_val, pady=5, padx=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
ttk.Button(root, text='C', style="TButton", command=clear_entry).grid(row=row_val, column=col_val, pady=5, padx=5)

# Run the application
root.mainloop()
