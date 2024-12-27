import tkinter as tk
from tkinter import ttk, filedialog
import socket
import RC4
import RSA
import sDES
import TDES
import threading
import hashlib
import subprocess
import verification
import random
import re  # Added for regex

client_socket = None


# Function to validate IP address
def is_valid_ip(ip):
    pattern = r"^\d{1,3}(\.\d{1,3}){3}$"
    return re.match(pattern, ip)


def received_Messages(ciphertext):
    hash_and_message = ciphertext.split('|')
    received_hash = hash_and_message[0]
    received_key_hash = hash_and_message[1]
    encrypted_message = hash_and_message[2]


    # Calculate MD5 hashes for each algorithm
    hash_rc4 = hashlib.md5(b'RC4').hexdigest()
    hash_RSA = hashlib.md5(b'RSA').hexdigest()
    hash_sDES = hashlib.md5(b'sDES').hexdigest()
    hash_TDES = hashlib.md5(b'TDES').hexdigest()
    hash_AES = hashlib.md5(b'AES').hexdigest()

    # Compare received hash with computed hashes to identify the algorithm
    if received_hash == hash_rc4:
        identified_algorithm = 'RC4'
    elif received_hash == hash_RSA:
        identified_algorithm = 'RSA'
    elif received_hash == hash_sDES:
        identified_algorithm = 'sDES'
    elif received_hash == hash_TDES:
        identified_algorithm = 'TDES'
    elif received_hash == hash_AES:
        identified_algorithm = 'AES'
    else:
        identified_algorithm = 'Unknown'


    key = "123456789012345678901234"
    md5_key_hash = hashlib.md5(key.encode()).hexdigest()

    plaintext = ""

    if md5_key_hash == received_key_hash:
        key = "123456789012345678901234"
    private_key = (10609, 14017)

    if identified_algorithm == "RC4":
        plaintext = RC4.RC4(encrypted_message, key)
    if identified_algorithm == "sDES":
        plaintext = sDES.sdes_decrypt(encrypted_message, key)
    if identified_algorithm == "TDES":
        plaintext = TDES.tdes_decrypt(encrypted_message, key)
    if identified_algorithm == "RSA":
        plaintext = RSA.rsa_decrypt(encrypted_message, private_key)
    if identified_algorithm == "AES":
        plaintext = TDES.tdes_decrypt(encrypted_message, key)

    return plaintext


def receive_messages():
    while True:
        try:
            message_received = client_socket.recv(1024).decode('utf-8')
            plaintext = received_Messages(message_received)
            if plaintext:
                received_textarea.config(state=tk.NORMAL)
                received_textarea.insert(tk.END, f"{plaintext}\n")
                received_textarea.config(state=tk.DISABLED)
                received_textarea.yview(tk.END)
            else:
                break
        except:
            break


import os


def on_button_click_connect():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = ip_address_server_entry.get()  # Get the server IP from the entry box

    if not is_valid_ip(server_ip):
        return

    port = 8080
    try:
        client_socket.connect((server_ip, port))
        threading.Thread(target=receive_messages, daemon=True).start()

        # Change button text to "Connected" and disable it
        button.config(text="Connected", state=tk.DISABLED)

    except Exception as e:
        print(f"Error: {e}")


# Create the main window
root = tk.Tk()
root.title(f"Cyber Security Receiver")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Connect to server
connect_label = ttk.Label(frame, text="Connect to server: ")
connect_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

# Entry box for IP address
ip_address_server_entry = ttk.Entry(frame)
ip_address_server_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# Button for starting connection
button = ttk.Button(frame, text="Connect", command=on_button_click_connect)
button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

# Label for received messages
received_label = ttk.Label(frame, text="Received messages from server:")
received_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

# Create a frame for the TextArea and its scrollbar
text_frame = ttk.Frame(frame)
text_frame.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=(tk.W, tk.E))

# Scrollbar
scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# TextArea for received messages
received_textarea = tk.Text(text_frame, height=10, width=40, yscrollcommand=scrollbar.set)
received_textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
received_textarea.config(state=tk.DISABLED)

# Configure the scrollbar to work with the TextArea
scrollbar.config(command=received_textarea.yview)

# Run the main event loop
root.mainloop()
