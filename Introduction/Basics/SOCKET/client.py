import socket

def main():
    server_ip = '192.168.x.x'  # Replace with the server's IP address
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, 9999))

    while True:
        command = input("Enter command (or 'exit' to quit): ")
        client_socket.send(command.encode())

        if command.lower() == 'exit':
            break

        # Receive response from server
        response = client_socket.recv(4096).decode()
        print("Response from server:\n", response)

    client_socket.close()

if __name__ == "__main__":
    main()
