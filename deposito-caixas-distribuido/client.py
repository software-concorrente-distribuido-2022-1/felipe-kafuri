from ConsumidorClient import ConsumidorClient
from ProdutorClient import ProdutorClient


def start():
    port = 5000
    produtor = ProdutorClient(port)

    produtor.make_box()

    produtor.close_connection()


start()
