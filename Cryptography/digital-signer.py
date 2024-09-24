import tkinter as tk
from tkinter import filedialog, messagebox,ttk
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import os
import traceback
import hashlib

public_key_path="public_key.pem"
# digital encryptor generator

def encrypt_file():
        global public_key_path
        file_path=file_path_var.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file to encrypt.")
            return

        try:
            # Generate a random AES key
            aes_key = os.urandom(32)
            iv = os.urandom(16)

            # Encrypt the file using AES
            with open(file_path, "rb") as file:
                file_data = file.read()

            padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(file_data) + padder.finalize()

            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

            # Encrypt the AES key using RSA
            with open(public_key_path, "rb") as key_file:
                public_key = serialization.load_pem_public_key(key_file.read(), backend=default_backend())

            encrypted_key = public_key.encrypt(
                aes_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            # Save the encrypted AES key and the encrypted file
            original_file_path=file_path
            print(original_file_path)
            encrypted_file_path = file_path + ".enc"
            with open(encrypted_file_path, "wb") as encrypted_file:
                encrypted_file.write(iv + encrypted_key + encrypted_data)

            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {encrypted_file_path}")
            os.remove(original_file_path)

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
            print(traceback.format_exc())



# Function to select a file
def select_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
    if file_path:
        file_path_var.set(file_path)  # Update the label or entry with the selected file path
## create widgets tkinter
            
# Create the main window
root = tk.Tk()

screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Set the title of the window
title_text = "Cyber Security Trainer"
node_text = "Node 1: Digital Signature Encryptor"


# Create the title string with calculated spaces
title = f"{title_text}{'      '}{node_text}"
root.title(node_text)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


# Create a label to show the selected file path
file_path_var = tk.StringVar()
file_path_label = ttk.Label(frame, textvariable=file_path_var, anchor='w', relief='sunken', width=50)
file_path_label.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Create a button that opens the file selector
file_button = tk.Button(frame, text="Select File", command=select_file)
file_button.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)


# Create a button that Signs the file selector
sign_btn = tk.Button(frame, text="Encrypt File", command=encrypt_file)
sign_btn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

# Run the main event loop
root.mainloop()