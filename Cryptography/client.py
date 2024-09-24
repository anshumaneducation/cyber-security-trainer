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


# Get the hostname of the local machine
hostname = socket.gethostname()
# Get the IP address corresponding to the hostname
ip_address = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '192.168.2.130'  # Replace with the actual server IP address
port = 8080
client_socket.connect((server_ip, port))


def received_Messages(ciphertext):
    hash_and_message = ciphertext.split('|')
    received_hash = hash_and_message[0]
    received_key_hash = hash_and_message[1]
    encrypted_message = hash_and_message[2]

    print(f"Encrypted text: {encrypted_message}")

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

    print(f"Identified Algorithm: {identified_algorithm}")
    print(f"Received Key Hash: {received_key_hash}")
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
    print(f"key: {key} plaintext: {plaintext}")
    return plaintext


def receive_messages():
    while True:
        try:
            message_received = client_socket.recv(1024).decode('utf-8')
            plaintext = received_Messages(message_received)
            if plaintext:
                print(f"Server: {plaintext}")  # Print the message to the console
                received_textarea.config(state=tk.NORMAL)
                received_textarea.insert(tk.END, f"{plaintext}\n")
                received_textarea.config(state=tk.DISABLED)
                received_textarea.yview(tk.END)
            else:
                break
        except:
            break
        
import os

def receive_files():
    while True:
        try:
            # Receive and decode the data type (4 bytes)
            data_type = client_socket.recv(4).decode().strip()
            print(f"Received data type: {data_type}")
            
            if data_type == 'file':
                # Receive filename length (4 bytes)
                filename_length = int.from_bytes(client_socket.recv(4), 'big')
                # Receive filename
                filename = client_socket.recv(filename_length).decode().strip()
                if not filename:
                    break

                # Prepare to receive the file data
                with open(filename, 'wb') as fo:
                    print(f"Receiving file '{filename}' from server")
                    # Receive file data length (4 bytes)
                    file_data_length = int.from_bytes(client_socket.recv(4), 'big')
                    remaining = file_data_length
                    while remaining > 0:
                        data = client_socket.recv(min(1024, remaining))
                        if not data:
                            break
                        fo.write(data)
                        remaining -= len(data)
                
                print(f"File '{filename}' received successfully")
            else:
                break  # Handle other data types or exit loop
        except Exception as e:
            print(f"An error occurred: {e}")
            break


accept_thread1 = threading.Thread(target=receive_messages)
accept_thread1.daemon = True
accept_thread1.start()

accept_thread2 = threading.Thread(target=receive_files)
accept_thread2.daemon = True
accept_thread2.start()

def select_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
    if file_path:
        file_path_var.set(file_path)  # Update the label or entry with the selected file path


def verify_sign():
    text_get_path = file_path_var.get()
    # subprocess.Popen(['python3', 'verification.py', text_get_path])
    is_it_valid=verification.verification(text_get_path)
    print(is_it_valid)
    if(is_it_valid):
        file_path_var1.set("Valid Signature")
    else:
        file_path_var1.set("InValid Signature")



# Create the main window
root = tk.Tk()
root.title(f"Cyber Security Receiver ip={ip_address}")
screen_width = 780
screen_height = 780
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, True)

# Create a frame for layout purposes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a TextArea for received messages
received_label = ttk.Label(frame, text="Received messages from server:")
received_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

received_textarea = tk.Text(frame, height=10, width=40)
received_textarea.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E))
received_textarea.config(state=tk.DISABLED)

# Create a button that opens the file selector
file_button = tk.Button(frame, text="Select File", command=select_file)
file_button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Create a label to show the selected file path
file_path_var = tk.StringVar()
file_path_label = ttk.Label(frame, textvariable=file_path_var, anchor='w', relief='sunken', width=50)
file_path_label.grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Create a button that Signs the file selector
sign_btn = tk.Button(frame, text="Verify Signature", command=verify_sign)
sign_btn.grid(row=3, column=0, padx=5, pady=5,sticky=tk.W)

# Create a label to show the verified file 
file_path_var1 = tk.StringVar()
file_path_label1 = ttk.Label(frame, textvariable=file_path_var1, anchor='w', relief='sunken', width=50)
file_path_label1.grid(row=3, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))

# Run the main event loop
root.mainloop()
