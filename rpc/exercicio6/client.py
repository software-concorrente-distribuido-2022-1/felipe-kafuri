import xmlrpc.client
import json

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

message = proxy.consume(json.dumps({ 'name': 'Sergio', 'salary': 4000.00, 'level': 'A', 'dependents': 0 }))
print(message)