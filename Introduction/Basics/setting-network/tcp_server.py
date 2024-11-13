import socket

def start_server():
    # Step 1: Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Step 2: Bind the socket to an address and port
    host = 'localhost'
    port = 12345
    server_socket.bind((host, port))

    # Step 3: Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}...")

    # Step 4: Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    while True:
        try:
            # Step 5: Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Client: {data}")

            # Step 6: Send a response to the client
            response = input("Server: ")
            client_socket.send(response.encode('utf-8'))

        except ConnectionResetError:
            print("Client disconnected abruptly.")
            break

    # Step 7: Close the connection
    client_socket.close()
    print("Connection closed.")
    server_socket.close()

if __name__ == "__main__":
    start_server()

