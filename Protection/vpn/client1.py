import socket
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from time import sleep
import re

# File path
file_path = "/etc/encrypted_file.enc"

# Check if the encrypted file exists before opening the app
if not os.path.exists(file_path):
    exit()

# Load shared encryption key
with open('key.key', 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)

def is_valid_ip(ip):
    """Validate the entered IP address."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        segments = ip.split(".")
        return all(0 <= int(seg) <= 255 for seg in segments)
    return False

def send_data():
    message = entry.get()
    if not message:
        messagebox.showerror("Error", "Message cannot be empty!")
        return

    server_ip = server_ip_entry.get()
    if not is_valid_ip(server_ip):
        messagebox.showerror("Error", "Invalid Server IP Address!")
        return

    encrypted_data = cipher.encrypt(message.encode())
    logs.insert(tk.END, f"Original: {message}")
    logs.insert(tk.END, f"Encrypted: {encrypted_data.decode()}")

    # Visualize data flow
    visualize_flow(message, encrypted_data)

    try:
        server_port = 12345

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        logs.insert(tk.END, "Connected to server.")
        client_socket.sendall(encrypted_data)
        logs.insert(tk.END, "Data sent to server.")
        client_socket.close()
    except Exception as e:
        logs.insert(tk.END, f"Error: {e}")

def visualize_flow(message, encrypted_data):
    canvas.delete("all")
    canvas.create_text(150, 50, text=f"Plain Text: {message}", fill="blue", font=("Arial", 12))
    canvas.create_text(150, 100, text="Encrypting...", fill="green", font=("Arial", 12))
    canvas.update()
    sleep(1)

    canvas.create_text(150, 150, text=f"Encrypted: {encrypted_data.decode()}", fill="purple", font=("Arial", 12))
    canvas.create_text(150, 200, text="Sending to Server...", fill="red", font=("Arial", 12))
    canvas.update()

# GUI setup
root = tk.Tk()
root.title("Client 1 - VPN Simulation")

# Entry for Server IP Address
tk.Label(root, text="Enter Server IP Address:").pack(pady=5)
server_ip_entry = tk.Entry(root, width=30)
server_ip_entry.pack(pady=5)

# Entry for Message
tk.Label(root, text="Enter Message:").pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send to Server", command=send_data)
send_button.pack(pady=10)

# Logs
logs = tk.Listbox(root, width=60, height=10)
logs.pack(pady=5)

# Visualization Canvas
canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(pady=10)

root.mainloop()
