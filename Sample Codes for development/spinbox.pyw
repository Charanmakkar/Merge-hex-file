import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Integer Roller")

# Set window size (optional)
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Select an integer:")
label.pack(pady=10)

# Create a Spinbox for integer input
int_spinbox = ttk.Spinbox(root, from_=0, to=100, increment=1)
int_spinbox.pack(pady=10)

# Function to display the selected value
def show_value():
    selected_value = int_spinbox.get()
    result_label.config(text=f"Selected Value: {selected_value}")

# Create a button to confirm the selection
confirm_button = tk.Button(root, text="Confirm", command=show_value)
confirm_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
