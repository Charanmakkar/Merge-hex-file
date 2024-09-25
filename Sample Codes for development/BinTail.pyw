def get_last_address(bin_file):
    with open(bin_file, 'rb') as f:
        # Seek to the end of the file
        f.seek(0, 2)  # 0 offset, 2 means "from the end"
        # Get the current position, which is the size of the file in bytes
        file_size = f.tell()
        
    # The last address will be file size - 1
    last_address = (file_size - 1)
    return hex(last_address)

# Example usage:
bin_file = "bootloader.bin"
last_address = get_last_address(bin_file)
print(f"The last address of the file is: (Decimal: {last_address})")
