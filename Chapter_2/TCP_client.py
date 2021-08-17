import socket


if __name__ == "__main__":

    target_host = "0.0.0.0"
    target_port = 9998

    # Create the socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the client
    client.connect((target_host, target_port))

    # Send some data
    send_string = b"This is a test, what do you think?"
    client.send(send_string)

    # Receive some data
    response = client.recv(4096)
    print(response.decode())

    client.close()

