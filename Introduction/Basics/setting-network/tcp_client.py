import socket

def start_client():
    # Step 1: Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Connect to the server
    host = 'localhost'
    port = 12345
    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")
    except ConnectionRefusedError:
        print("Unable to connect to the server.")
        return

    while True:
        try:
            # Step 3: Send a message to the server
            message = input("Client: ")
            if not message:
                break
            client_socket.send(message.encode('utf-8'))

            # Step 4: Receive a response from the server
            response = client_socket.recv(1024).decode('utf-8')
            if not response:
                break
            print(f"Server: {response}")

        except ConnectionResetError:
            print("Server disconnected abruptly.")
            break

    # Step 5: Close the connection
    client_socket.close()
    print("Connection closed.")

if __name__ == "__main__":
    start_client()
