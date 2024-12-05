import hashlib

file_address = "virus4.txt"  # Specify the path to your file

try:
    # Open the file in binary read mode and compute its MD5 hash
    with open(file_address, 'rb') as file:
        file_hash = hashlib.md5(file.read()).hexdigest()
    print(file_hash)
except FileNotFoundError:
    print(f"File not found: {file_address}")
except Exception as e:
    print(f"Error: {e}")
