import socket
import json


HOST = "127.0.0.1"
PORT = 5001


message = {
    "from": "maria@alpha.ro",

    "to": [
        "ana@alpha.ro",
        "bob@beta.ro",
        "test@unknown.ro",
        "bianca@alpha.ro",
        "denisa@alpha.ro"

    ],

    "subject": "Salut",

    "body": "Acesta este proiectul nostru la retele"
}


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client.connect((HOST, PORT))

client.sendall(
    json.dumps(message).encode()
)

response = client.recv(4096)

print("\nSERVER RESPONSE:")
print(json.loads(response.decode()))

client.close()