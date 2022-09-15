import json
import socket
from threading import Thread

BACKLOG = 5

class MailBox:

    def __init__(self, port, max_size, handler):
        self.port = port
        self.max_size = max_size
        self.handler = handler
        self.message = None
    
    def start_server(self):
        host = 'localhost'

        server_socket = socket.socket()
        server_socket.bind((host, self.port))

        print(f"Server started on port {self.port}")

        server_socket.listen(BACKLOG)

        while True:
            connection, address = server_socket.accept()
            t = Thread(target=self.new_client, args=(connection, address))
            t.setDaemon(True)
            t.start()

    def new_client(self, connection, address):
        while True:
            print(f"Incoming request from host {address}")
            data = connection.recv(self.max_size).decode()
            if not data:
                break
            message = self.handler(data)
            connection.send(message.encode())

        connection.close()
    
    def store_message(self, message, client_socket):
        client_socket.send(message.encode())

        data = self.client_socket.recv(self.max_size).decode()
        if not data:
            return '-'
        return data
    
    def retrieve_message(self, message, client_socket):
        client_socket.send(message.encode())

        data = client_socket.recv(self.max_size).decode()
        if not data:
            return '-'
        return data



def handler(data):
    request = json.loads(data)

    if request['type'] == 'PROD':
        return 'Message stored'
    elif request['type'] == 'CONS':
        return 'Message consumed'

server = MailBox(3001, 1024, handler)
server.start_server()
