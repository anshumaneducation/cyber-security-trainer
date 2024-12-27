import socket
from cryptography.fernet import Fernet
import tkinter as tk
from threading import Thread
from time import sleep

# Load shared encryption key
with open('key.key', 'rb') as key_file:
    key = key_file.read()
cipher = Fernet(key)

def start_server():
    try:
        client_ip = "0.0.0.0"
        client_port = 12346

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((client_ip, client_port))
        server_socket.listen(1)
        logs.insert(tk.END, "Client 2 is waiting for data...")

        while True:
            conn, addr = server_socket.accept()
            logs.insert(tk.END, f"Connected to Server at {addr}")
            encrypted_data = conn.recv(1024)
            logs.insert(tk.END, f"Encrypted Data Received: {encrypted_data.decode()}")

            decrypted_data = cipher.decrypt(encrypted_data).decode()
            logs.insert(tk.END, f"Decrypted Data: {decrypted_data}")
            visualize_flow(encrypted_data, decrypted_data)
            conn.close()
    except Exception as e:
        logs.insert(tk.END, f"Error: {e}")

def visualize_flow(encrypted_data, decrypted_data):
    canvas.delete("all")
    canvas.create_text(150, 50, text=f"Encrypted Data: {encrypted_data.decode()}", fill="blue", font=("Arial", 12))
    canvas.create_text(150, 100, text="Decrypting...", fill="green", font=("Arial", 12))
    canvas.update()
    sleep(1)

    canvas.create_text(150, 150, text=f"Decrypted: {decrypted_data}", fill="purple", font=("Arial", 12))
    canvas.update()



# GUI setup
root = tk.Tk()
root.title("Client 2 - VPN Simulation")

logs = tk.Listbox(root, width=60, height=10)
logs.pack(pady=5)

Thread(target=start_server).start()

canvas = tk.Canvas(root, width=300, height=250, bg="white")
canvas.pack(pady=10)


root.mainloop()
