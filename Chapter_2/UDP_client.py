import socket


if __name__ == "__main__":

    target_host = "127.0.0.1"
    target_port = 9997

    # Create the socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send some data
    send_string = b"AAABBBCCC"
    client.sendto(send_string, (target_host, target_port))

    # Receive some data
    data, addr = client.recvfrom(4096)
    print(data.decode())

    client.close()

