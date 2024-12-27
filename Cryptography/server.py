import tkinter as tk
from tkinter import ttk, filedialog
import socket
import RC4
import RSA
import sDES
import TDES
import hashlib
import threading
import subprocess
import sign
import random
import string
import psutil

ciphertext = ""
p = 467
q = 23
g = 2
x = 15


# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8080  # Using a higher port number to avoid potential permission issues

server_ip = '0.0.0.0'  # Bind to all interfaces
server_socket.bind((server_ip, port))
server_socket.listen(5)
clients = []


def accept_clients():
    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)

def send_to_client(event=None):
    for client in clients:
        try:
            client.sendall(ciphertext.encode('utf-8'))
        except:
            clients.remove(client)

# Start accepting clients in a separate thread
accept_thread = threading.Thread(target=accept_clients)
accept_thread.daemon = True
accept_thread.start()


# Function to update the second ComboBox based on the first ComboBox selection
def update_combo1(event):
    selected_method = combo1.get()
    if selected_method == "Symmetric Encryption":
        combo2['values'] = ("sDES", "TDES", "RC4")
    elif selected_method == "Asymmetric Encryption":
        combo2['values'] = ("RSA")
    else:
        combo2['values'] = ()

def update_combo2(event):
    selected_method = combo2.get()
    if selected_method == "":
        textarea.delete('1.0', tk.END)
        textarea.config(state=tk.DISABLED)
    else:
        textarea.config(state=tk.NORMAL)

# Function to handle button clicks
def on_button_click():
    global ciphertext

    algorithm = combo2.get()
    cryptoType = combo1.get()
    public_key = "123456789012345678901234"
    type = True

    if cryptoType == "Symmetric Encryption":
        pass
    else:
        type = False
    md5_key_hash = hashlib.md5(public_key.encode()).hexdigest()  # Hash the key
    plaintext = textarea.get("1.0", tk.END).strip()  # Get and strip the plaintext


    if type:
        if algorithm == 'RC4':
            result = hashlib.md5(b'RC4').hexdigest()
            ciphertext = result + "|" + md5_key_hash + "|" + RC4.RC4(plaintext, public_key)
        elif algorithm == 'sDES':
            result = hashlib.md5(b'sDES').hexdigest()
            ciphertext = result + "|" + md5_key_hash + "|" + sDES.sdes_encrypt(plaintext, public_key)
        elif algorithm == 'TDES':
            result = hashlib.md5(b'TDES').hexdigest()
            ciphertext = result + "|" + md5_key_hash + "|" + TDES.tdes_encrypt(plaintext, public_key)
    else:
        if algorithm == 'RSA':
            public_key1 = (8009, 14017)
            result = hashlib.md5(b'RSA').hexdigest()
            ciphertext = result + "|" + md5_key_hash + "|" + RSA.rsa_encrypt(plaintext, public_key1)
        if algorithm == 'AES':
            result = hashlib.md5(b'rc4').hexdigest()
            ciphertext = result + "|" + DSA.RC4(plaintext, public_key1)

    send_to_client()

def on_closing():
    # Close all client sockets
    for client in clients:
        client.close()

    # Close the server socket
    server_socket.close()

    # Terminate the GUI window
    root.destroy()



# Create the main window
root = tk.Tk()

screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Set the title of the window
title_text = "Cyber Security Trainer"
node_text = "Node 1: Sender"


# Create the title string with calculated spaces
title = (f"Cyber Security Sender")
root.title(title)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the first ComboBox
combo_label1 = ttk.Label(frame, text="Choose cryptography method:")
combo_label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

combo1 = ttk.Combobox(frame)
combo1['values'] = ("Symmetric Encryption", "Asymmetric Encryption")
combo1.grid(row=0, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
combo1.bind("<<ComboboxSelected>>", update_combo1)

# Create the second ComboBox
combo_label2 = ttk.Label(frame, text="Choose algorithm:")
combo_label2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

combo2 = ttk.Combobox(frame)
combo2.grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
combo2.bind("<<ComboboxSelected>>", update_combo2)

# Create a TextArea
text_label = ttk.Label(frame, text="Enter text here:")
text_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

textarea = tk.Text(frame, height=10, width=40)
textarea.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
textarea.config(state=tk.DISABLED)

# Create a Button
send_button = ttk.Button(frame, text="Send", command=on_button_click)
send_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

# Bind the close event to the on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)



# Run the main event loop
root.mainloop()
