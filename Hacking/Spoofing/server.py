import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

server_ip = "0.0.0.0"  # Listen on all interfaces
server_port = 9999
clients = []

def start_server():
    """Starts the server and listens for clients."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    log_text.insert(tk.END, f"Server listening on {server_ip}:{server_port}\n")

    while True:
        client_socket, addr = server.accept()
        clients.append((client_socket, addr))
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

def handle_client(client_socket, addr):
    """Handles incoming client messages."""
    try:
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            # Extract fake IP from received message
            log_text.insert(tk.END, f"Spoofed IP {data} → Connected from {addr[0]}\n")
    except:
        pass
    finally:
        client_socket.close()
        log_text.insert(tk.END, f"Client {addr[0]} disconnected\n")

# GUI Setup
root = tk.Tk()
root.title("Server - Connected Clients")
root.geometry("400x300")

log_text = scrolledtext.ScrolledText(root, width=50, height=15)
log_text.pack()

# Start server in a separate thread
threading.Thread(target=start_server, daemon=True).start()

root.mainloop()
