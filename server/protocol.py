import json


def encode_message(message_dict):
    return json.dumps(message_dict).encode()


def decode_message(message_bytes):
    return json.loads(message_bytes.decode())