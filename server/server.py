import socket
import threading
import json
import sys

from protocol import encode_message, decode_message
from mailbox_manager import save_email
from router import send_to_remote_server


CONFIG_FILE = sys.argv[1]

with open(CONFIG_FILE, "r") as file:
    config = json.load(file)

DOMAIN = config["domain"]
HOST = config["host"]
PORT = config["port"]
ROUTES = config["routes"]


def handle_client(client_socket):

    try:
        data = client_socket.recv(4096)

        if not data:
            return

        message = decode_message(data)

        print(f"\n[{DOMAIN}] MESSAGE RECEIVED")
        print(message)

        sender = message["from"]
        recipients = message["to"]
        subject = message["subject"]
        body = message["body"]

        results = {}

        for recipient in recipients:

            if "@" not in recipient:
                results[recipient] = "INVALID_EMAIL"
                continue

            domain = recipient.split("@")[1]

            # LIVRARE LOCALA
            if domain == DOMAIN:

                save_email(
                    recipient,
                    sender,
                    subject,
                    body
                )

                results[recipient] = "DELIVERED_LOCAL"

            # LIVRARE SERVER EXTERN
            elif domain in ROUTES:

                remote_message = {
                    "from": sender,
                    "to": [recipient],
                    "subject": subject,
                    "body": body
                }

                response = send_to_remote_server(
                    ROUTES[domain],
                    remote_message
                )

                if response["status"] == "OK":
                    results[recipient] = "DELIVERED_REMOTE"

                else:
                    results[recipient] = "SERVER_UNAVAILABLE"

            # DOMENIU NECUNOSCUT
            else:

                results[recipient] = "UNKNOWN_DOMAIN"

        response = {
            "status": "OK",
            "results": results
        }

        client_socket.sendall(
            encode_message(response)
        )

    except Exception as e:

        error_response = {
            "status": "ERROR",
            "message": str(e)
        }

        client_socket.sendall(
            encode_message(error_response)
        )

    finally:
        client_socket.close()


def start_server():

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind((HOST, PORT))

    server.listen(5)

    print(f"\n[{DOMAIN}] SERVER STARTED ON {HOST}:{PORT}")

    while True:

        client_socket, address = server.accept()

        print(f"\n[{DOMAIN}] CONNECTION FROM {address}")

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket,)
        )

        thread.start()


start_server()