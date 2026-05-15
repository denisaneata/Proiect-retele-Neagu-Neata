import socket

from protocol import encode_message, decode_message


def send_to_remote_server(server_info, email_data):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect(
            (server_info["host"], server_info["port"])
        )

        sock.sendall(
            encode_message(email_data)
        )

        response = sock.recv(4096)

        sock.close()

        return decode_message(response)

    except Exception as e:

        return {
            "status": "ERROR",
            "message": str(e)
        }