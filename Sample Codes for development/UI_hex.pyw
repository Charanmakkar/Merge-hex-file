import tkinter as tk
from tkinter import messagebox

def validate_hex_input(P):
    # Validate if the entered value is a valid hexadecimal string
    if all(c in '0123456789abcdefABCDEF' for c in P) or P == "":
        return True
    else:
        return False

def get_hex_value():
    hex_value = entry.get()
    if hex_value:
        try:
            # Convert hex string to integer to check validity
            int_value = int(hex_value, 16)
            result_label.config(text=f"Decimal Value: {int_value}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid hexadecimal value.")
    else:
        messagebox.showwarning("Input Missing", "Please enter a hexadecimal value.")

# Create the main window
root = tk.Tk()
root.title("Hexadecimal Input")

# Validation command setup
vcmd = (root.register(validate_hex_input), '%P')

# Label
label = tk.Label(root, text="Enter a hexadecimal value:")
label.pack(pady=10)

# Entry widget for hexadecimal input with validation
entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(pady=10)

# Button to process the input
process_button = tk.Button(root, text="Convert to Decimal", command=get_hex_value)
process_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
