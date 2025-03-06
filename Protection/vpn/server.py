import socket
from threading import Thread
import tkinter as tk
from time import sleep
import re

# File path
file_path = "/etc/encrypted_file.enc"

# Check if the encrypted file exists before opening the app
if not os.path.exists(file_path):
    exit()

def is_valid_ip(ip):
    """Validate the entered IP address."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if pattern.match(ip):
        segments = ip.split(".")
        return all(0 <= int(seg) <= 255 for seg in segments)
    return False

def start_server():
    try:
        server_ip = "0.0.0.0"
        server_port = 12345

        # Validate Client 2 IP address
        client2_ip = client2_ip_entry.get()
        if not is_valid_ip(client2_ip):
            logs.insert(tk.END, "Error: Invalid IP address entered for Client 2.")
            return

        client2_port = 12346

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((server_ip, server_port))
        server_socket.listen(1)
        logs.insert(tk.END, f"Server is listening on {server_ip}:{server_port}...")

        while True:
            conn, addr = server_socket.accept()
            logs.insert(tk.END, f"Connection from {addr}")

            data = conn.recv(1024)
            logs.insert(tk.END, f"Encrypted Data Received: {data.decode()}")
            visualize_flow(data, client2_ip)

            # Forward data to Client 2
            forward_to_client2(data, client2_ip, client2_port)
            conn.close()
    except Exception as e:
        logs.insert(tk.END, f"Error: {e}")

def forward_to_client2(data, ip, port):
    try:
        client2_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2_socket.connect((ip, port))
        logs.insert(tk.END, f"Forwarding data to Client 2 at {ip}:{port}...")
        client2_socket.sendall(data)
        logs.insert(tk.END, "Data successfully forwarded to Client 2.")
        client2_socket.close()
    except Exception as e:
        logs.insert(tk.END, f"Error forwarding to Client 2: {e}")

def visualize_flow(encrypted_data, client2_ip):
    canvas.delete("all")
    canvas.create_text(150, 50, text=f"Encrypted Data: {encrypted_data.decode()}", fill="blue", font=("Arial", 12))
    canvas.create_text(150, 100, text=f"Forwarding to {client2_ip}", fill="red", font=("Arial", 12))
    canvas.update()
    sleep(1)

# GUI setup
root = tk.Tk()
root.title("Server - VPN Simulation")

logs = tk.Listbox(root, width=60, height=10)
logs.pack(pady=5)

canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(pady=10)

# Entry for Client 2 IP
tk.Label(root, text="Enter Client 2 IP Address:").pack(pady=5)
client2_ip_entry = tk.Entry(root, width=30)
client2_ip_entry.pack(pady=5)

start_button = tk.Button(root, text="Start Server", command=lambda: Thread(target=start_server).start())
start_button.pack(pady=10)

root.mainloop()
