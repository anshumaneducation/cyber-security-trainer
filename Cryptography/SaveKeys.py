import tkinter as tk
from tkinter import ttk
import os
import hashlib

# Path to store the keys (relative to script location)
path_to_keys =  "DSAkeys.txt"
# File path for validation
file_path = "/home/an/CSEH Applications/Executables/Cryptography Apps/encrypted_file.enc"

# Check if the encrypted file exists before opening the app
if not os.path.exists(file_path):
    exit()

# Function to save the keys to a file
def save_keys():
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    
    # Ensure both keys are provided
    if not key1 or not key2:
        status_label.config(text="Please enter both keys.", foreground="red")
        return
    
    # Hash the values of keys
    key1_hash = hashlib.md5(key1.encode()).hexdigest()
    key2_hash = hashlib.md5(key2.encode()).hexdigest()
    
    # Save the hashed keys to the file
    try:
        with open(path_to_keys, "w") as file:
            file.write(f"Key 1: {key1_hash}\n")
            file.write(f"Key 2: {key2_hash}\n")
        status_label.config(text="Keys saved successfully!", foreground="green")
    except Exception as e:
        status_label.config(text=f"Error saving keys: {e}", foreground="red")

# Create the main Tkinter window
root = tk.Tk()
root.title("Key Storage GUI")
root.geometry("300x200")

# Key 1 label and entry
key1_label = ttk.Label(root, text="Encryptor Software Key:")
key1_label.pack(pady=5)
key1_entry = ttk.Entry(root, width=30)
key1_entry.pack(pady=5)

# Key 2 label and entry
key2_label = ttk.Label(root, text="Decryptor Software Key:")
key2_label.pack(pady=5)
key2_entry = ttk.Entry(root, width=30)
key2_entry.pack(pady=5)

# Save button
save_button = ttk.Button(root, text="Save Keys", command=save_keys)
save_button.pack(pady=10)

# Status label
status_label = ttk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
