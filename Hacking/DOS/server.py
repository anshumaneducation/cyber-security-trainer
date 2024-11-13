import tkinter as tk
from tkinter import ttk
import socket
import threading
import time

# Global variable to control the server
server_thread = None
server_running = False
connection_count = 0

def on_button1_click():
    """Start Server button handler."""
    global server_thread, server_running
    if not server_running:
        server_running = True
        server_thread = threading.Thread(target=run_server)
        server_thread.start()

def on_button2_click():
    """Stop Server button handler."""
    global server_running
    server_running = False

def update_text_widget():
    """Update the text widget with the current number of connections."""
    while server_running:
        time.sleep(1)  # Update every second
        text_widget.delete('1.0', tk.END)  # Clear previous content
        text_widget.insert(tk.END, f"Total requests: {connection_count}\nRequests per minute: {connection_count_per_minute()}\n")
        text_widget.see(tk.END)  # Scroll to the end

def connection_count_per_minute():
    """Calculate requests per minute."""
    return connection_count  # Adjust as needed

def run_server():
    """Server function to handle incoming connections."""
    global connection_count
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.100.165', 8080))
    server_socket.listen(5)
    print("Server started on port 8080...")

    # Start the text widget updater
    threading.Thread(target=update_text_widget).start()

    while server_running:
        try:
            client_socket, addr = server_socket.accept()
            connection_count += 1
            print(f"Connection {connection_count} from {addr}")
            client_socket.close()
        except Exception as e:
            print(f"Server error: {e}")
            break

    server_socket.close()
    print("Server stopped.")

# GUI setup
root = tk.Tk()
root.title("DOS/DDOS Attack Server")

# Create two buttons
button1 = tk.Button(root, text="Start Server", command=on_button1_click)
button1.grid(row=0, column=2, padx=10, pady=10, sticky="NSEW")

button2 = tk.Button(root, text="Stop Server", command=on_button2_click)
button2.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Create a Text widget to show the number of requests
text_widget = tk.Text(root, height=5, width=30)
text_widget.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
