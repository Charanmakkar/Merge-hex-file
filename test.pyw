import tkinter as tk
from tkinter import filedialog
import os

def get_last_address(bin_file):
    with open(bin_file, 'rb') as f:
        # Seek to the end of the file
        f.seek(0, 2)  # 0 offset, 2 means "from the end"
        # Get the current position, which is the size of the file in bytes
        file_size = f.tell()
        
    # The last address will be file size - 1
    last_address = file_size - 1
    print(last_address, type(last_address))
    return last_address

def validate_hex_input(P):
    # Validate if the entered value is a valid hexadecimal string
    if all(c in '0123456789abcdefABCDEF' for c in P) or P == "":
        return True
    else:
        return False

def browseFiles(label):
    # Open file dialog and get the file path
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Binary files", "*.bin*"),
                                                     ("All files", "*.*")))
    label.config(text=filename)
    return filename

def merge_bin_files_with_padding():
    # Get the file paths from the labels
    file1 = label_file_explorer.cget("text")
    file2 = label_file_explorer2.cget("text")

    lastHexAddr = get_last_address(file1)

    print(lastHexAddr)

    padding_size = ((int(hex_value_input.get(), 16)) - lastHexAddr)-1

    print(padding_size)
    
    if not file1 or not file2:
        print("Please select both files before merging.")
        return
    
    print(f"File 1: {file1}")
    print(f"File 2: {file2}")

    # Read the contents of the first file
    with open(file1, 'rb') as f1:
        data1 = f1.read()
    
    # Read the contents of the second file
    with open(file2, 'rb') as f2:
        data2 = f2.read()
    
    # Create padding bytes (filled with 0x00)
    padding = bytes([0x00] * padding_size)

    # Define the output file path
    output_file = os.path.join(os.getcwd(), "outfile.bin")

    # Write the merged content to the output file
    with open(output_file, 'wb') as out:
        out.write(data1)      # Write the first file's content
        out.write(padding)    # Write the padding
        out.write(data2)      # Write the second file's content

    print(f"Files {file1} and {file2} have been merged into {output_file} with {padding_size} bytes of padding.")



def merge_files():
    # Get the file paths from the labels
    file1_path = label_file_explorer.cget("text")
    file2_path = label_file_explorer2.cget("text")
    
    if not file1_path or not file2_path:
        print("Please select both files before merging.")
        return
    
    print(f"File 1: {file1_path}")
    print(f"File 2: {file2_path}")

    lastHexAddr = get_last_address(file1_path)

    selected_value = int(hex_value_input.get())
    
    # result_label.config(text=f"Selected Value: {selected_value}")

    try:
        # Read the contents of the first file
        with open(file1_path, 'rb') as file1:
            file1_content = file1.read()


        # Read the contents of the second file
        with open(file2_path, 'rb') as file2:
            file2_content = file2.read()

        # Define the output file path
        output_file_path = os.path.join(os.getcwd(), "outfile.bin")

        
        # Merge the contents and write to a new file
        with open(output_file_path, 'wb') as outfile:
            outfile.write(file1_content)
            outfile.write(file2_content)

        print(f"Files merged successfully into {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Setting up the GUI
window = tk.Tk()
window.title('File Merger')
window.geometry("500x500")
window.config(background="white")
window.resizable(False, False)

# Validation command setup
vcmd = (window.register(validate_hex_input), '%P')

# File Explorer labels
label_file_explorer = tk.Label(window, text="Select File 1", width=100, height=4, fg="blue")
label_file_explorer.pack(pady=10)

# Entry widget for hexadecimal input with validation
hex_value_input = tk.Entry(window, validate="key", validatecommand=vcmd)
hex_value_input.pack(pady=10)

label_file_explorer2 = tk.Label(window, text="Select File 2", width=100, height=4, fg="blue")
label_file_explorer2.pack(pady=10)

# Buttons to browse files
button_explore1 = tk.Button(window, text="Browse File 1", command=lambda: browseFiles(label_file_explorer))
button_explore1.pack()

button_explore2 = tk.Button(window, text="Browse File 2", command=lambda: browseFiles(label_file_explorer2))
button_explore2.pack()

# Button to merge files
# button_merge = tk.Button(window, text="Merge Files", command=merge_files)
button_merge = tk.Button(window, text="Merge Files", command=merge_bin_files_with_padding)
button_merge.pack(pady=20)

# Button to exit the application
button_exit = tk.Button(window, text="Exit", command=window.quit)
button_exit.pack()

# Run the GUI loop
window.mainloop()
