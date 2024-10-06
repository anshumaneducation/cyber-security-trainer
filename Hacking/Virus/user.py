import tkinter as tk
import socket
import threading
import os

def receive_payload():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5001))  # Listening for Virus and Trojan
    server.listen(1)
    
    while True:
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

        # Virus Attack Simulation
        if attack_type == "virus":
            info_label.config(text=f"Virus Payload Received!\nSimulating virus attack...\n{path_status}")
            execute_virus_attack(install_path)

        # Trojan Attack Simulation
        elif attack_type == "trojan":
            info_label.config(text=f"Trojan Payload Received!\nSimulating trojan attack...\n{path_status}")
            execute_trojan_attack(install_path)

        # Close the connection but keep server running
        conn.close()

def execute_virus_attack(install_path):
    info_label.config(text="Virus Attack:\nCreating infected files...")
    try:
        for i in range(1, 6):
            with open(os.path.join(install_path, f"infected_file_{i}.txt"), "w") as f:
                f.write("This file has been infected by a virus!\n")
        explanation_text = (
            "A virus is a malicious program that replicates itself and spreads by attaching itself "
            "to legitimate files or applications. It can corrupt or modify files and perform unauthorized actions."
        )
        theoretical_label.config(text=explanation_text)
    except Exception as e:
        info_label.config(text=f"Error creating files: {e}")

def execute_trojan_attack(install_path):
    info_label.config(text="Trojan Attack:\nSimulating backdoor creation...")
    try:
        with open(os.path.join(install_path, "backdoor_log.txt"), "w") as f:
            f.write("Backdoor created: This simulates a trojan attack.\n")

        explanation_text = (
            "A Trojan is disguised as legitimate software but performs malicious activities in the background."
            " It might open backdoors or log user data."
        )
        theoretical_label.config(text=explanation_text)
    except Exception as e:
        info_label.config(text=f"Error creating backdoor: {e}")

# GUI setup
root = tk.Tk()
root.title("User Node - Malware Simulation")

info_label = tk.Label(root, text="Waiting for payload...")
info_label.pack(pady=10)

theoretical_label = tk.Label(root, text="", wraplength=400, justify="left")
theoretical_label.pack(pady=10)

# Start receiving payload in a new thread
threading.Thread(target=receive_payload, daemon=True).start()

root.mainloop()
