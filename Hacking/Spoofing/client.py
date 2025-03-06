import socket
import tkinter as tk

server_port = 9999

def connect_to_server():
    """Connects to the server with a fake IP message."""
    fake_ip = fake_ip_entry.get()
    server_ip=victim_ip_entry.get()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((server_ip, server_port))
        client.send(fake_ip.encode())  # Send the fake IP
        status_label.config(text="Connected!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {e}", fg="red")
    finally:
        client.close()

# GUI Setup
root = tk.Tk()
root.title("Client - Spoof IP")
root.geometry("300x200")

tk.Label(root, text="Enter Fake IP:").pack()
fake_ip_entry = tk.Entry(root)
fake_ip_entry.pack()

tk.Label(root, text="Enter Victim IP:").pack()
victim_ip_entry = tk.Entry(root)
victim_ip_entry.pack()

connect_button = tk.Button(root, text="Connect", command=connect_to_server)
connect_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="black")
status_label.pack()

root.mainloop()
