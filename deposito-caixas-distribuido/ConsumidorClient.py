import socket


class ConsumidorClient:

    def __init__(self, port, box):
        self.port = port
        self.box = box
        self.host = socket.gethostname() # obter o host, como ambos os códigos estão sendo executados localmente
        self.client_socket = socket.socket()  # obter socket

        self.client_socket.connect((self.host, self.port))  # conectar ao servidor
    
    def consume_box(self, box):
        self.client_socket.send(self.box - box).encode()  # enviar mensagem

        data = self.client_socket.recv(self.box).decode() # obter mensagem
        if not data:
            return '-'
        return data
    
    def close_connection(self):
        self.client_socket.close()  # encerrar conexão
