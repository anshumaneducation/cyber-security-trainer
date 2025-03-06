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

private_key_path="private_key.pem"
# digital encryptor generator

def decrypt_file():
        global private_key_path
        file_path=file_path_var.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file to decrypt.")
            return

        if not file_path.endswith(".enc"):
            messagebox.showerror("Error", "Selected file is not an encrypted file.")
            return

        try:
            with open(private_key_path, "rb") as key_file:
                private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

            with open(file_path, "rb") as encrypted_file:
                iv = encrypted_file.read(16)
                encrypted_key = encrypted_file.read(256)
                encrypted_data = encrypted_file.read()

            aes_key = private_key.decrypt(
                encrypted_key,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )

            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

            unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
            decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

            encrypted_file_path=file_path
            print(encrypted_file_path)
            decrypted_file_path = file_path.rstrip(".enc")
            with open(decrypted_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)

            messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {decrypted_file_path}")
            os.remove(encrypted_file_path)

        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
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
node_text = "Node 1: Digital Signature Decryptor"


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
sign_btn = tk.Button(frame, text="Decrypt File", command=decrypt_file)
sign_btn.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

# Run the main event loop
root.mainloop()