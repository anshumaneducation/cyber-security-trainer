import tkinter as tk
import socket
import threading
import os

def receive_payload():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5002))  # Listening for Worms
    server.listen(5)
    
    while True:  # Keep accepting connections in a loop
        conn, addr = server.accept()

        # Receive the payload type and installation path
        data = conn.recv(1024).decode()
        attack_type, install_path = data.split("|")

        # Check if the path exists
        if os.path.exists(install_path):
            path_status = f"Path exists: {install_path}"
            conn.sendall(f"{attack_type} received, path exists.".encode())
        else:
            path_status = f"Path not found: {install_path}"
            conn.sendall(f"{attack_type} received, but path not found.".encode())
            conn.close()
            continue  # Skip further action if the path is not found

        # Worm Attack Simulation
        if attack_type == "worm":
            info_label.config(text=f"Worm Payload Received!\nSimulating worm attack...\n{path_status}")
            execute_worm_attack(install_path)

        # Close the connection but keep the server running
        conn.close()

def execute_worm_attack(install_path):
    info_label.config(text="Worm Attack:\nSimulating network spread...")
    try:
        # Simulate worm attack by creating directories in the provided path
        for i in range(1, 6):
            os.makedirs(os.path.join(install_path, f"infected_dir_{i}"), exist_ok=True)

        explanation_text = (
            "A worm is a type of malware that spreads across networks, replicating itself without human action. "
            "It can consume bandwidth and cause significant harm."
        )
        theoretical_label.config(text=explanation_text)
    except Exception as e:
        info_label.config(text=f"Error creating directories: {e}")

# GUI setup
root = tk.Tk()
root.title("Worm Node - Malware Simulation")

info_label = tk.Label(root, text="Waiting for payload...")
info_label.pack(pady=10)

theoretical_label = tk.Label(root, text="", wraplength=400, justify="left")
theoretical_label.pack(pady=10)

# Start receiving payload in a new thread
threading.Thread(target=receive_payload, daemon=True).start()

root.mainloop()
