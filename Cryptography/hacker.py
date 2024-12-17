import tkinter as tk
from tkinter import ttk, filedialog
import socket
import threading
import hashlib
import re  # Added for regex
import RC4
import RSA
import sDES
import TDES
import subprocess
import verification
import random

client_socket = None
algorithm_selected = ""
key_pair_1 = (0, 0)
public_key1 = ""
type_of = "Symmetric Encryption"


# Function to validate IP address
def is_valid_ip(ip):
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return re.match(pattern, ip)


# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                root.after(0, lambda msg=message: received_textarea.insert(tk.END, msg + "\n"))
                Decrypt_and_show(message)
            else:
                break
        except Exception as e:
            print(f"Connection closed: {e}")
            break


# Function to handle server connection
def on_button_click_connect():
    global client_socket
    server_ip = ip_address_server_entry.get()
    if not is_valid_ip(server_ip):
        print("Invalid IP address. Please enter a valid one.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 8080
    try:
        client_socket.connect((server_ip, port))
        threading.Thread(target=receive_messages, daemon=True).start()
        print("Connected to server!")
    except Exception as e:
        print(f"Error: {e}")


# Update the second ComboBox based on the first ComboBox selection
def update_combo2(event):
    selected_method = combo1.get()
    if selected_method == "Symmetric Encryption":
        combo2['values'] = ("SDES", "TDES", "RC4")
    elif selected_method == "Asymmetric Encryption":
        combo2['values'] = ("RSA")
    else:
        combo2['values'] = ()


# Function to decrypt and display messages
def Decrypt_and_show(ciphertext):
    hash_and_message = ciphertext.split('|')
    if len(hash_and_message) != 3:
        print("Invalid message format")
        return

    received_hash = hash_and_message[0]
    received_key_hash = hash_and_message[1]
    encrypted_message = hash_and_message[2]

    algorithm = algorithm_selected
    key = public_key1

    try:
        if algorithm == "RC4":
            plaintext = RC4.rc4_decrypt(encrypted_message, key)
        elif algorithm == "TDES":
            plaintext = TDES.tdes_decrypt(encrypted_message, key)
        elif algorithm == "SDES":
            plaintext = sDES.sdes_decrypt(encrypted_message, key)
        elif algorithm == "RSA":
            print(key_pair_1)
            plaintext = RSA.rsa_decrypt(encrypted_message, key_pair_1)
        else:
            plaintext = "Unknown algorithm"
        
        received_textarea_decrypted.insert(tk.END, plaintext + "\n")
    except Exception as e:
        print(f"Decryption error: {e}")


# Function to handle decryption button click
def on_button_click_decrypt():
    global algorithm_selected, key_pair_1, public_key1, type_of

    algorithm_selected = combo2.get()
    hash_algorithm = hashlib.md5(algorithm_selected.encode()).hexdigest()

    public_key_get = public_key_entry.get()
    private_key_get = private_key_entry.get()

    key_hash = hashlib.md5(public_key_get.encode()).hexdigest()

    if combo1.get() == "Symmetric Encryption":
        type_of = "Symmetric Encryption"
        public_key1 = public_key_get
    else:
        type_of = "Asymmetric Encryption"
        key_pair_1 = (private_key_get, public_key_get)

    print(f"Decryption setup done: {algorithm_selected}, Hash: {hash_algorithm}")


# Main window setup
root = tk.Tk()
root.title("Cyber Security Hacker")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Create a frame for layout
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Connect to Server
connect_label = ttk.Label(frame, text="Connect to server:")
connect_label.pack(fill=tk.X, padx=5, pady=5)

ip_address_server_entry = ttk.Entry(frame)
ip_address_server_entry.pack(fill=tk.X, padx=10, pady=5)

connect_button = ttk.Button(frame, text="Connect", command=on_button_click_connect)
connect_button.pack(padx=10, pady=10)

# Step 1: Get Encrypted Messages
step_label1 = ttk.Label(frame, text="Step 1: Get the encrypted messages anyhow:")
step_label1.pack(fill=tk.X, padx=5, pady=5)

received_label = ttk.Label(frame, text="Received messages from server in encrypted format:")
received_label.pack(fill=tk.X, padx=5, pady=5)

received_textarea = tk.Text(frame, height=10, width=40)
received_textarea.pack(fill=tk.X, padx=10, pady=5)

# Step 2: Detect Encryption Method
step_label2 = ttk.Label(frame, text="Step 2: Detect the encrypting method from the encryption style:")
step_label2.pack(fill=tk.X, padx=5, pady=5)

combo_label1 = ttk.Label(frame, text="Choose cryptography method:")
combo_label1.pack(anchor=tk.W, padx=5, pady=5)

combo1 = ttk.Combobox(frame)
combo1['values'] = ("Symmetric Encryption", "Asymmetric Encryption")
combo1.pack(fill=tk.X, padx=10, pady=5)
combo1.bind("<<ComboboxSelected>>", update_combo2)

combo_label2 = ttk.Label(frame, text="Choose algorithm:")
combo_label2.pack(anchor=tk.W, padx=5, pady=5)

combo2 = ttk.Combobox(frame)
combo2.pack(fill=tk.X, padx=10, pady=5)

# Step 3: Get Keys
step_label3 = ttk.Label(frame, text="Step 3: Get the public and/or private key:")
step_label3.pack(fill=tk.X, padx=5, pady=5)

public_key_label = ttk.Label(frame, text="Public Key:")
public_key_label.pack(anchor=tk.W, padx=5, pady=5)

public_key_entry = ttk.Entry(frame)
public_key_entry.pack(fill=tk.X, padx=10, pady=5)

private_key_label = ttk.Label(frame, text="Private Key:")
private_key_label.pack(anchor=tk.W, padx=5, pady=5)

private_key_entry = ttk.Entry(frame)
private_key_entry.pack(fill=tk.X, padx=10, pady=5)

# Step 4: Decrypt Messages
step_label4 = ttk.Label(frame, text="Step 4: Get the decrypted messages:")
step_label4.pack(fill=tk.X, padx=5, pady=5)

decrypt_button = ttk.Button(frame, text="Decrypt message", command=on_button_click_decrypt)
decrypt_button.pack(padx=10, pady=10)

received_textarea_decrypted = tk.Text(frame, height=10, width=40)
received_textarea_decrypted.pack(fill=tk.X, padx=10, pady=5)

# Run the main event loop
root.mainloop()
