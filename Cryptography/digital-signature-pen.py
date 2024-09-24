import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
import os
import traceback
import hashlib

class RSAEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RSA File Encryption/Decryption")

        self.file_path = ""
        self.public_key_path = "public_key.pem"
        self.private_key_path = "private_key.pem"

        self.create_widgets()
        # self.generate_keys()

    def create_widgets(self):
        self.select_file_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_file_button.pack(pady=5)

        self.encrypt_button = tk.Button(self.root, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(self.root, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            messagebox.showinfo("Selected File", f"Selected file: {self.file_path}")

    # def generate_keys(self):
    #     try:
    #         private_key = rsa.generate_private_key(
    #             public_exponent=65537,
    #             key_size=2048,
    #             backend=default_backend()
    #         )

    #         public_key = private_key.public_key()

    #         with open(self.private_key_path, "wb") as private_file:
    #             private_file.write(private_key.private_bytes(
    #                 encoding=serialization.Encoding.PEM,
    #                 format=serialization.PrivateFormat.PKCS8,
    #                 encryption_algorithm=serialization.NoEncryption()
    #             ))

    #         with open(self.public_key_path, "wb") as public_file:
    #             public_file.write(public_key.public_bytes(
    #                 encoding=serialization.Encoding.PEM,
    #                 format=serialization.PublicFormat.SubjectPublicKeyInfo
    #             ))
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Key generation failed: {str(e)}")
    #         print(traceback.format_exc())

    def encrypt_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file to encrypt.")
            return

        try:
            # Generate a random AES key
            aes_key = os.urandom(32)
            iv = os.urandom(16)

            # Encrypt the file using AES
            with open(self.file_path, "rb") as file:
                file_data = file.read()

            padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(file_data) + padder.finalize()

            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

            # Encrypt the AES key using RSA
            with open(self.public_key_path, "rb") as key_file:
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
            original_file_path=self.file_path
            print(original_file_path)
            encrypted_file_path = self.file_path + ".enc"
            with open(encrypted_file_path, "wb") as encrypted_file:
                encrypted_file.write(iv + encrypted_key + encrypted_data)

            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {encrypted_file_path}")
            os.remove(original_file_path)

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")
            print(traceback.format_exc())

    def decrypt_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file to decrypt.")
            return

        if not self.file_path.endswith(".enc"):
            messagebox.showerror("Error", "Selected file is not an encrypted file.")
            return

        try:
            with open(self.private_key_path, "rb") as key_file:
                private_key = serialization.load_pem_private_key(key_file.read(), password=None, backend=default_backend())

            with open(self.file_path, "rb") as encrypted_file:
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

            encrypted_file_path=self.file_path
            print(encrypted_file_path)
            decrypted_file_path = self.file_path.rstrip(".enc")
            with open(decrypted_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)

            messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {decrypted_file_path}")
            os.remove(encrypted_file_path)

        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")
            print(traceback.format_exc())

if __name__ == "__main__":
    root = tk.Tk()
    app = RSAEncryptionApp(root)
    root.mainloop()


