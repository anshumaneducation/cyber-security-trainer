import socket

# Configuration: Set up the listener
LISTENER_IP = '0.0.0.0'  # Listen on all interfaces
LISTENER_PORT = 4444
LOG_FILE = 'logs.txt'

def start_listener():
    # Set up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((LISTENER_IP, LISTENER_PORT))
    sock.listen(5)
    print(f"Listening on port {LISTENER_PORT}...")

    while True:
        # Accept incoming connections
        client, addr = sock.accept()
        print(f"Connection from {addr}")

        # Receive data from the client
        data = client.recv(4096).decode()
        if data:
            print(f"Received:\n{data}\n")
            
            # Save the received data to logs.txt
            with open(LOG_FILE, 'a') as log_file:
                log_file.write(f"Connection from {addr}\n")
                log_file.write(f"{data}\n")
                log_file.write("=" * 50 + "\n")
        
        client.close()

if __name__ == "__main__":
    start_listener()
