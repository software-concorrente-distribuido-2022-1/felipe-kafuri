from CaixaServer import CaixaServer
from ConsumidorClient import ConsumidorClient
from ProdutorClient import ProdutorClient


def handle_server(message, box):
    if message['message'] == 'Armazenar':
        box += 1
        return 'Armazenado'
    if message == 'Consumir' and box > 0:
        box -= 1
        return 'Consumido'


def start_server():
    caixa = 0
    port = 5001
    server = CaixaServer(port, 1024,caixa)
    server.start_server(handle_server)


if __name__ == '__main__':
    start_server()
