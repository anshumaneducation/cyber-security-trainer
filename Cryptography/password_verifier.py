import tkinter as tk
from tkinter import ttk
import hashlib
import os
import importlib

# Path to the keys file (relative path)
path_to_keys = "DSAkeys.txt"

# Variables for hashed passwords
encryptor_pass = None
decryptor_pass = None

# Function to load hashed keys from the file
def load_keys():
    global encryptor_pass, decryptor_pass
    try:
        with open(path_to_keys, "r") as file:
            lines = file.readlines()
            if len(lines) < 2:
                print("Error: Keys file must have at least two hashed keys.")
                return False
            # Extract hashed keys
            encryptor_pass = lines[0].split(":")[1].strip()
            decryptor_pass = lines[1].split(":")[1].strip()
        return True
    except FileNotFoundError:
        print(f"Error: Keys file '{path_to_keys}' not found.")
        return False
    except Exception as e:
        print(f"Error loading keys: {e}")
        return False

# Function to check password and load the appropriate module
def check_password():
    if not load_keys():
        return
    
    password = textarea.get()
    input_pass = hashlib.md5(password.encode()).hexdigest()
    
    if input_pass == encryptor_pass:
        try:
            import digital_signer
            print("Digital Signer module loaded successfully.")
        except ImportError:
            print("Error: Unable to load 'digital_signer' module.")
    elif input_pass == decryptor_pass:
        try:
            import digital_verifier
            print("Digital Verifier module loaded successfully.")
        except ImportError:
            print("Error: Unable to load 'digital_verifier' module.")
    else:
        print("Error: Invalid password.")

# Create the main window
root = tk.Tk()

screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Set the title of the window
title_text = "Cyber Security Trainer"
node_text = "Input Password to Enter"
root.title(node_text)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input field for the password
textarea = tk.Entry(frame, show="*")  # Hide password input
textarea.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Create a button that checks the password
pass_button = tk.Button(frame, text="Check", command=check_password)
pass_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Run the main event loop
root.mainloop()
