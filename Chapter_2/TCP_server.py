"""
TCP Server

Let's create a TCP server class in accordance with that layed out in BHP.

Note that this was not implemented as a class originally, this was coded as such from scratch
"""

import socket
import threading


class TCP_server():
    def __init__(self):
        self.IP = "0.0.0.0"
        self.Port = 9998

    def main(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.IP, self.Port))
        server.listen(5)
        print("[*] Listening on {ip}:{port}".format(ip=self.IP, port=self.Port))

        while True:
            client, address = server.accept()
            print("[*] Accepted connection from {add_0}:{add_1}".format(add_0=address[0], add_1=address[1]))
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()

    def handle_client(self, client_socket):
        with client_socket as sock:
            request = sock.recv(1024)
            print("[*] Received: {decoded}".format(decoded=request.decode("utf-8")))
            sock.send(b"ACK")


if __name__ == "__main__":
    Server = TCP_server()
    Server.main()
