import json
import socket
from http import client

from P3.ex01.mail_box import MailBox, server


class Producer:

    def __init__(self, port, message_max_size, mail_box: MailBox):
        self.port = port
        self.message_max_size = message_max_size
        self.host = socket.gethostname()
        self.client_socket = socket.socket()
        self.mail_box = mail_box

        self.client_socket.connect((self.host, self.port))
    
    def store_message(self, message):
      self.mail_box.store_message(message, self.client_socket)
    
    def close_connection(self):
        self.client_socket.close() 

producer = Producer(3001, 1024, server)
response = producer.store_message(json.dumps({ 'message': 'test', 'type': 'PROD'}))
print(response)
