import sys
import socket
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Define server functions
def start_tcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(5)
    print("TCP Server started")
    while True:
        client_socket, addr = server_socket.accept()
        # Handle connection

def start_udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 8081))
    print("UDP Server started")
    while True:
        data, addr = server_socket.recvfrom(1024)
        # Handle data

def start_http_server():
    server = HTTPServer(('localhost', 8082), SimpleHTTPRequestHandler)
    print("HTTP Server started")
    server.serve_forever()

def start_ftp_server():
    # FTP server code using pyftpdlib
    print("FTP Server started")

def start_mqtt_server():
    # MQTT server code using paho-mqtt
    print("MQTT Server started")

# Define function to start server in a thread
def start_server():
    global server_thread
    server_type = server_combobox.get()
    
    if server_type == 'TCP':
        server_thread = threading.Thread(target=start_tcp_server, daemon=True)
    elif server_type == 'UDP':
        server_thread = threading.Thread(target=start_udp_server, daemon=True)
    elif server_type == 'HTTP':
        server_thread = threading.Thread(target=start_http_server, daemon=True)
    elif server_type == 'FTP':
        server_thread = threading.Thread(target=start_ftp_server, daemon=True)
    elif server_type == 'MQTT':
        server_thread = threading.Thread(target=start_mqtt_server, daemon=True)
    else:
        messagebox.showerror("Error", "Please select a valid server type.")
        return
    
    server_thread.start()
    status_label.config(text=f"{server_type} Server started.")

# Define function to stop server
def stop_server():
    global server_thread
    if server_thread:
        # A mechanism to stop the server gracefully should be implemented here.
        # Since Python's standard library does not support stopping threads,
        # the implementation depends on how servers are being stopped (e.g., setting a flag, etc.).
        # Placeholder implementation.
        status_label.config(text="Stopping server...")
        # Example: You might need to implement server-specific stop logic.
    else:
        messagebox.showwarning("Warning", "No server is running.")

# GUI Setup for Attacker Management
root = Tk()
root.title("Cyber Security Network Introduction Server")
root.geometry("400x300")

# Server Selection
Label(root, text="Select Server Type:").pack(pady=5)
server_combobox = ttk.Combobox(root, values=['TCP', 'UDP', 'HTTP', 'FTP', 'MQTT'])
server_combobox.pack(pady=5)

# Start and Stop Buttons
start_button = Button(root, text="Start Server", command=start_server)
start_button.pack(pady=5)
stop_button = Button(root, text="Stop Server", command=stop_server)
stop_button.pack(pady=5)

# Status Label
status_label = Label(root, text="Server not started.")
status_label.pack(pady=10)

# Initialize the server thread as None
server_thread = None

# Run the Tkinter event loop
root.mainloop()
