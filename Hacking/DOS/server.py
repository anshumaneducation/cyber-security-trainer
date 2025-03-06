import tkinter as tk
import socket
import threading
import time

# Global variables
server_thread = None
server_running = False
connection_count = 0
server_ip='0.0.0.0'

# File path
file_path = "/etc/encrypted_file.enc"

# Check if the encrypted file exists before opening the app
if not os.path.exists(file_path):
    exit()

def log_server_message(message):
    """Log a message to the server's Text widget."""
    text_widget.config(state=tk.NORMAL)
    text_widget.insert(tk.END, message + "\n")
    text_widget.config(state=tk.DISABLED)
    text_widget.see(tk.END)

def on_button1_click():
    """Start Server button handler."""
    global server_thread, server_running
    if not server_running:
        server_running = True
        server_thread = threading.Thread(target=run_server)
        server_thread.start()
        log_server_message("Server started...")

def on_button2_click():
    """Stop Server button handler."""
    global server_running
    server_running = False
    log_server_message("Server stopped.")

def run_server():
    """Server function to handle incoming connections."""
    global connection_count
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 8080))
    server_socket.listen(5)

    while server_running:
        try:
            client_socket, addr = server_socket.accept()
            connection_count += 1
            log_server_message(f"Connection from {addr[0]}:{addr[1]} (Total connections: {connection_count})")
            client_socket.close()
        except Exception as e:
            log_server_message(f"Error: {e}")
            break

    server_socket.close()

# GUI setup
root = tk.Tk()
root.title("DOS/DDOS Attack Server")

# Create two buttons
button1 = tk.Button(root, text="Start Server", command=on_button1_click)
button1.grid(row=0, column=0, padx=10, pady=10)

button2 = tk.Button(root, text="Stop Server", command=on_button2_click)
button2.grid(row=0, column=1, padx=10, pady=10)

# Create a Text widget to log server messages
text_widget = tk.Text(root, height=10, width=50, state=tk.DISABLED)
text_widget.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
