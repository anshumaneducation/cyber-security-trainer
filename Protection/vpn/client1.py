import socket
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
from time import sleep

# Encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

def send_data():
    message = entry.get()
    if not message:
        messagebox.showerror("Error", "Message cannot be empty!")
        return

    encrypted_data = cipher.encrypt(message.encode())
    logs.insert(tk.END, f"Original: {message}")
    logs.insert(tk.END, f"Encrypted: {encrypted_data.decode()}")

    # Visualize data flow
    visualize_flow(message, encrypted_data)

    try:
        server_ip = "192.168.1.100"  # Replace with server's IP
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

tk.Label(root, text="Enter Message:").pack()
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

send_button = tk.Button(root, text="Send to Server", command=send_data)
send_button.pack(pady=10)

logs = tk.Listbox(root, width=60, height=10)
logs.pack(pady=5)

canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(pady=10)

root.mainloop()
