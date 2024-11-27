import socket
import threading
from tkinter import *

# List to store received OTPs
received_otps = []

# Function to handle communication with a client
def handle_client(client_socket, client_address):
    global received_otps
    print(f"New connection from {client_address}")
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode()
            if not data:  # Connection closed by the client
                print(f"Client {client_address} disconnected")
                break

            print(f"Received from {client_address}: {data}")
            
            # Append the OTP to the list and update the GUI
            received_otps.append(data)
            update_gui(data)
    except Exception as e:
        print(f"Error with client {client_address}: {e}")
    finally:
        client_socket.close()

# Function to update the GUI with a received OTP
def update_gui(otp):
    otp_listbox.insert(END, otp)

# Function to start the server
def start_server(host="0.0.0.0", port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Listen for up to 5 pending connections
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # Accept a new client connection
            client_socket, client_address = server_socket.accept()
            # Handle the client connection in a separate thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
            client_thread.start()
    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()

# Function to run the server in a separate thread
def run_server():
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

# Start the server when the script is run
if __name__ == "__main__":
    # Start the server in a separate thread
    run_server()

    # GUI Setup
    root = Tk()
    root.title("OTP Server")
    root.geometry("400x400")

    # OTP Listbox
    Label(root, text="Received OTPs:").pack(pady=5)
    otp_listbox = Listbox(root, width=50, height=20)
    otp_listbox.pack(pady=5)

    # Run the Tkinter event loop
    root.mainloop()
