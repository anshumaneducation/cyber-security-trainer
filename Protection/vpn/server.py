import socket
from threading import Thread
from cryptography.fernet import Fernet
import tkinter as tk
from time import sleep

# Encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

def start_server():
    try:
        server_ip = "127.0.0.1"  # Replace with your server's IP
        server_port = 12345
        client2_ip = "192.168.113.245"  # Replace with Client 2's IP
        client2_port = 12346

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)
        logs.insert(tk.END, f"Server is listening on {server_ip}:{server_port}...")

        while True:
            conn, addr = server_socket.accept()
            logs.insert(tk.END, f"Connection from {addr}")

            data = conn.recv(1024)
            logs.insert(tk.END, f"Encrypted Data: {data.decode()}")

            decrypted_data = cipher.decrypt(data).decode()
            logs.insert(tk.END, f"Decrypted Data: {decrypted_data}")

            visualize_flow(data, decrypted_data, client2_ip)

            # Forward data to Client 2
            forward_to_client2(decrypted_data, client2_ip, client2_port)
            conn.close()
    except Exception as e:
        logs.insert(tk.END, f"Error: {e}")

def forward_to_client2(data, ip, port):
    try:
        client2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2_socket.connect((ip, port))
        logs.insert(tk.END, f"Forwarding data to Client 2 at {ip}:{port}...")
        client2_socket.sendall(data.encode())
        logs.insert(tk.END, "Data successfully forwarded to Client 2.")
        client2_socket.close()
    except Exception as e:
        logs.insert(tk.END, f"Error forwarding to Client 2: {e}")

def visualize_flow(encrypted_data, decrypted_data, client2_ip):
    canvas.delete("all")
    canvas.create_text(150, 50, text=f"Received Encrypted: {encrypted_data.decode()}", fill="blue", font=("Arial", 12))
    canvas.create_text(150, 100, text=f"Decrypted: {decrypted_data}", fill="green", font=("Arial", 12))
    canvas.create_text(150, 150, text=f"Forwarding to {client2_ip}", fill="red", font=("Arial", 12))
    canvas.update()
    sleep(2)

# GUI setup
root = tk.Tk()
root.title("Server - VPN Simulation")

logs = tk.Listbox(root, width=60, height=10)
logs.pack(pady=5)

canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(pady=10)

start_button = tk.Button(root, text="Start Server", command=lambda: Thread(target=start_server).start())
start_button.pack(pady=10)

root.mainloop()
