import tkinter as tk
import socket
import threading

def send_payload(target_ip, target_port, attack_type, install_path, status_label):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target_ip, target_port))
        # Send the payload type followed by the installation path
        s.sendall(f"{attack_type}|{install_path}".encode())
        status_label.config(text=f"Payload Type Sent: {attack_type}\nPath: {install_path}")
        
        # Receive feedback from the victim (path found or not)
        response = s.recv(1024).decode()
        status_label.config(text=f"Payload Sent: {attack_type}\nResponse: {response}")
    except Exception as e:
        status_label.config(text=f"Error: {e}")
    finally:
        s.close()

# GUI for Attacker Node
def start_gui():
    root = tk.Tk()
    root.title("Attacker Node - Malware Simulation")

    status_label = tk.Label(root, text="Idle", font=("Helvetica", 12))
    status_label.pack(pady=10)

    # Entry for target path
    path_entry_label = tk.Label(root, text="Enter Installation Path:", font=("Helvetica", 10))
    path_entry_label.pack(pady=5)
    
    path_entry = tk.Entry(root, width=40)
    path_entry.pack(pady=5)

    tk.Button(root, text="Send Virus", command=lambda: send_payload("127.0.0.1", 5001, "virus", path_entry.get(), status_label)).pack(pady=5)
    tk.Button(root, text="Send Worm", command=lambda: send_payload("127.0.0.1", 5002, "worm", path_entry.get(), status_label)).pack(pady=5)
    tk.Button(root, text="Send Trojan", command=lambda: send_payload("127.0.0.1", 5001, "trojan", path_entry.get(), status_label)).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
