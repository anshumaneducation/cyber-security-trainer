import socket

def start_udp_client():
    # Step 1: Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Step 2: Set the server address
    host = 'localhost'
    port = 12345
    server_address = (host, port)

    try:
        while True:
            # Step 3: Send a message to the server
            message = input("Client: ")
            if not message:
                break
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Step 4: Receive a response from the server
            data, _ = client_socket.recvfrom(1024)
            print(f"Server: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nClient shutting down.")

    client_socket.close()

if __name__ == "__main__":
    start_udp_client()
