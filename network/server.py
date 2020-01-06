import socket
import sys
import threading

class TCPServer(object):
    def __init__(self, bind_ip, bind_port, timeout=5):
        self.bind_ip = bind_ip
        self.bind_port = int(bind_port)
        self.timeout = timeout
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.server.bind((self.bind_ip, self.bind_port))
        self.server.listen(self.timeout)
        print(f'[*] Listening on {self.bind_ip}:{self.bind_port}')

    def command_shell(self, client_socket):
        while True:
            message = input() or '\n'
            if message:
                client_socket.send(message.encode())
                response = client_socket.recv(1024).decode()
                print(response, end="")

    def run(self):
        self.start()
        client, addr = self.server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=self.command_shell, args=(client,))
        client_handler.start()