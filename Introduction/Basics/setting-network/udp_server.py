import socket

def start_udp_server():
    # Step 1: Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Step 2: Bind the socket to an address and port
    host = 'localhost'
    port = 12345
    server_socket.bind((host, port))
    print(f"UDP server is listening on {host}:{port}...")

    while True:
        try:
            # Step 3: Receive a message from the client
            data, client_address = server_socket.recvfrom(1024)  # Buffer size of 1024 bytes
            if not data:
                break
            print(f"Client [{client_address}]: {data.decode('utf-8')}")

            # Step 4: Send a response back to the client
            response = input("Server: ")
            server_socket.sendto(response.encode('utf-8'), client_address)

        except KeyboardInterrupt:
            print("\nServer shutting down.")
            break

    server_socket.close()

if __name__ == "__main__":
    start_udp_server()
