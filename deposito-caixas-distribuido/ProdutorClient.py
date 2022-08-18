import json
import socket


class ProdutorClient:

    def __init__(self, port):
        self.port = port
        self.host = socket.gethostname() # obter o host, como ambos os códigos estão sendo executados localmente
        self.client_socket = socket.socket()  # obter socket

        self.client_socket.connect((self.host, self.port))  # conectar ao servidor
    
    def make_box(self):
        self.client_socket.send(json.dumps(dict(
            message='Armazenar',
        )).encode())  # enviar mensagem

        data = self.client_socket.recv(1024) # obter mensagem
        if not data:
            return '-'
        return data
    
    def close_connection(self):
        self.client_socket.close()  # encerrar conexão
