import socket
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def attempt_connection():
    target_ip = ip.get()
    target_port = int(port.get())
    protocol = protocol_type.get().lower()

    try:
        if protocol == "tcp":
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)  # Set timeout to 3 seconds
            s.connect((target_ip, target_port))
            messagebox.showinfo("Result", f"TCP connection to {target_ip}:{target_port} successful!")
        elif protocol == "udp":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"Test", (target_ip, target_port))
            s.settimeout(3)
            try:
                data, _ = s.recvfrom(1024)
                messagebox.showinfo("Result", f"UDP connection to {target_ip}:{target_port} received response!")
            except socket.timeout:
                messagebox.showinfo("Result", f"UDP connection to {target_ip}:{target_port} sent, no response received.")
        else:
            messagebox.showerror("Error", "Unsupported protocol")
    except socket.error as e:
        messagebox.showerror("Connection Failed", f"Could not connect to {target_ip}:{target_port}. Error: {str(e)}")
    finally:
        s.close()

# GUI setup for Attack Simulation
root = Tk()
root.title("Firewall Attack Simulation")

# Variables to hold user inputs
ip = StringVar()
port = StringVar()
protocol_type = StringVar()

# GUI Components
Label(root, text="Target IP:").pack()
Entry(root, textvariable=ip).pack()

Label(root, text="Target Port:").pack()
Entry(root, textvariable=port).pack()

Label(root, text="Protocol (tcp/udp):").pack()
Entry(root, textvariable=protocol_type).pack()

Button(root, text="Attempt Connection", command=attempt_connection).pack()

root.mainloop()
