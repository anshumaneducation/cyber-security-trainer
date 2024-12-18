import tkinter as tk
from tkinter import ttk
import os
import hashlib

# Path to store the keys
path_to_keys = "DSAkeys.txt"

# Function to save the keys to a file
def save_keys():
    key1 = key1_entry.get()
    key2 = key2_entry.get()
    ## hash values of keys
    key1_hash = hashlib.md5(key1.encode()).hexdigest()
    key2_hash = hashlib.md5(key2.encode()).hexdigest()
    if key1 and key2:
        with open(path_to_keys, "w") as file:
            file.write(f"Key 1: {key1_hash}\n")
            file.write(f"Key 2: {key2_hash}\n")
        status_label.config(text="Keys saved successfully!", foreground="green")
    else:
        status_label.config(text="Please enter both keys.", foreground="red")

# Create the main Tkinter window
root = tk.Tk()
root.title("Key Storage GUI")
root.geometry("300x200")

# Key 1 label and entry
key1_label = ttk.Label(root, text="Enter Key 1:")
key1_label.pack(pady=5)
key1_entry = ttk.Entry(root, width=30)
key1_entry.pack(pady=5)

# Key 2 label and entry
key2_label = ttk.Label(root, text="Enter Key 2:")
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
