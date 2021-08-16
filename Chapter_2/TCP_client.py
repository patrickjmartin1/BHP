import socket


if __name__ == "__main__":

    target_host = "www.google.com"
    target_port = 80

    # Create the socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the client
    client.connect((target_host, target_port))

    # Send some data
    send_string = b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
    client.send(send_string)

    # Receive some data
    response = client.recv(4096)
    print(response.decode())

    client.close()

