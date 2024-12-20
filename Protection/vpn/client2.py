import socket
import tkinter as tk
from threading import Thread

def start_server():
    try:
        client_ip = "192.168.1.101"  # Replace with your IP
        client_port = 12346

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((client_ip, client_port))
        server_socket.listen(1)
        logs.insert(tk.END, "Client 2 is waiting for data...")

        while True:
            conn, addr = server_socket.accept()
            logs.insert(tk.END, f"Connected to Server at {addr}")
            data = conn.recv(1024).decode()
            visualize_flow(data)
            logs.insert(tk.END, f"Received Data: {data}")
            conn.close()
    except Exception as e:
        logs.insert(tk.END, f"Error: {e}")

def visualize_flow(data):
    canvas.delete("all")
    canvas.create_text(150, 50, text="Receiving Data...", fill="blue", font=("Arial", 12))
    canvas.update()
    sleep(1)

    canvas.create_text(150, 150, text=f"Received: {data}", fill="green", font=("Arial", 12))
    canvas.update()

# GUI setup
root = tk.Tk()
root.title("Client 2 - VPN Simulation")

logs = tk.Listbox(root, width=60, height=10)
logs.pack(pady=5)

canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=10)

start_button = tk.Button(root, text="Start Listening", command=lambda: Thread(target=start_server).start())
start_button.pack(pady=10)

root.mainloop()
