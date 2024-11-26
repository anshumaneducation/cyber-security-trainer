import socket
import hashlib
import tkinter as tk
from tkinter import messagebox

# Shared secret password (same as server)
shared_secret = "mypassword"

# Function to compute the hash (using MD5)
def compute_hash(challenge, password):
    return hashlib.md5((password + challenge).encode()).hexdigest()

# Function to connect to the server and authenticate
def authenticate():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    # Connect to the server
    server_host = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_host, server_port))
        
        # Receive challenge from server
        challenge = client_socket.recv(1024).decode()
        print(f"Received challenge: {challenge}")
        
        # Update the client GUI with the received challenge
        label_challenge.config(text=f"Challenge: {challenge}")

        # Compute response
        response = compute_hash(challenge, password)
        print(f"Sending response: {response}")

        # Send username and response to server
        client_socket.send(f"{username},{response}".encode())

        # Receive authentication result
        result = client_socket.recv(1024).decode()
        print(result)
        messagebox.showinfo("Authentication", result)

    except Exception as e:
        messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
    finally:
        client_socket.close()

# Create the GUI window for the client
window = tk.Tk()
window.title("CHAP Authentication Client")

# Username and password labels and inputs
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

# Label for showing the challenge
label_challenge = tk.Label(window, text="Challenge will appear here.")
label_challenge.pack(pady=5)

# Authentication button
auth_button = tk.Button(window, text="Authenticate", command=authenticate)
auth_button.pack(pady=20)

# Run the GUI loop
window.mainloop()
