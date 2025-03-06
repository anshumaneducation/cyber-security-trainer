import hashlib
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

# Store the hashed password
stored_password_hash = hashlib.sha256("Anshuman1234".encode()).hexdigest()

# Encryption key (You should store this securely)
key = Fernet.generate_key()
cipher = Fernet(key)

# File path
file_path = "/etc/encrypted_file.enc"

def verify_password():
    entered_password = entry_pw.get()
    entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()
    
    if entered_password_hash == stored_password_hash:
        messagebox.showinfo("Success", "Password is correct!")
        encrypt_and_store_file()
    else:
        messagebox.showerror("Error", "Incorrect password!")

def encrypt_and_store_file():
    try:
        data = b"This is a secured encrypted file."

        # Encrypt the data
        encrypted_data = cipher.encrypt(data)

        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Store the encrypted file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

        # Make it unreadable & unwritable (but still executable if needed)
        os.chmod(file_path, 0o400)  # Read-only permission
    except Exception:
        print("Gone...")  # Generic error message without details

# Create GUI
root = tk.Tk()
root.title("Password Verification")

tk.Label(root, text="Enter Password:").pack(pady=5)

entry_pw = tk.Entry(root, show="*")  # Mask input
entry_pw.pack(pady=5)

validate_button = tk.Button(root, text="Verify", command=verify_password)
validate_button.pack(pady=10)

root.mainloop()
