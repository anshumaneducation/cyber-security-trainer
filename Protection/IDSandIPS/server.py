import socket
import threading
from tkinter import *
from tkinter import messagebox
import time
import os

# Global variables for server and connection tracking
server_running = False
server_socket = None
connection_attempts = 0
start_time = time.time()
IPS_MODE = True  # Enable IPS mode (True) or IDS mode (False)
detected_attack = False

# Function to start the server
def start_server():
    global server_running, server_socket, detected_attack
    server_ip = "0.0.0.0"
    server_port = 12345

    if not server_running:
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((server_ip, server_port))
            server_socket.listen(5)
            server_running = True
            threading.Thread(target=accept_connections).start()
            start_button.config(state=DISABLED)
            stop_button.config(state=NORMAL)
            messagebox.showinfo("Server", "Server started successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start server: {e}")
    else:
        messagebox.showwarning("Server", "Server is already running!")

# Function to stop the server
def stop_server():
    global server_running, server_socket
    if server_running:
        server_running = False
        server_socket.close()
        start_button.config(state=NORMAL)
        stop_button.config(state=DISABLED)
        messagebox.showinfo("Server", "Server stopped successfully!")
    else:
        messagebox.showwarning("Server", "Server is not running!")

# Function to accept connections and monitor traffic
def accept_connections():
    global connection_attempts, start_time, detected_attack
    while server_running:
        try:
            client_socket, client_address = server_socket.accept()
            connection_attempts += 1
            print(f"Connection attempt from {client_address}")

            # Detect attack based on the number of attempts
            if connection_attempts > 10:  # Threshold for detection
                detected_attack = True
                print(f"[ALERT] Attack detected from {client_address[0]}!")
                if IPS_MODE:
                    block_ip(client_address[0])
                    client_socket.close()
                    messagebox.showinfo("IPS", f"Blocked IP: {client_address[0]}")
                    stop_server()  # Stop the server to prevent further attacks
                    return
            threading.Thread(target=handle_client, args=(client_socket, client_address)).start()
        except socket.error:
            break

# Function to handle client connections
def handle_client(client_socket, client_address):
    try:
        client_socket.send(b"Hello from IDS/IPS Server\n")
        client_socket.close()
    except:
        pass

# Function to block IP (IPS mode)
def block_ip(ip_address):
    if os.name == 'posix':  # For Linux systems
        os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")
    elif os.name == 'nt':  # For Windows systems
        os.system(f"netsh advfirewall firewall add rule name='BlockIP' dir=in action=block remoteip={ip_address}")

# GUI Setup for IDS/IPS Management
root = Tk()
root.title("Server of IDS and IPS Simulation")
root.geometry("400x200")

# Labels for IDS/IPS status
status_label = Label(root, text="Server Status: Stopped", font=("Arial", 12))
status_label.pack(pady=10)

# Buttons to start and stop server
start_button = Button(root, text="Start Server", command=start_server, width=20)
start_button.pack(pady=10)

stop_button = Button(root, text="Stop Server", command=stop_server, state=DISABLED, width=20)
stop_button.pack(pady=10)

# Option to toggle between IDS and IPS modes
def toggle_ips():
    global IPS_MODE
    IPS_MODE = not IPS_MODE
    mode_label.config(text=f"Current Mode: {'IPS' if IPS_MODE else 'IDS'}")

mode_button = Button(root, text="Toggle IDS/IPS Mode", command=toggle_ips, width=20)
mode_button.pack(pady=10)

mode_label = Label(root, text="Current Mode: IPS", font=("Arial", 10))
mode_label.pack()

# Run the Tkinter event loop
root.mainloop()
