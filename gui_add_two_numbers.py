import tkinter as tk
from tkinter import messagebox

def calculate_sum():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        total = num1 + num2
        result_label.config(text=f"The sum is: {total}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers.")

# Create the main window
root = tk.Tk()
root.title("Add Two Numbers")

# Create and place widgets
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="Calculate Sum", command=calculate_sum).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
