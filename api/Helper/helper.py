import uuid
from flask import jsonify


def generate_token():
    # Generate a UUID version 4 (random UUID)
    uuid_string = str(uuid.uuid4())
    uuid_string = uuid_string.split('-')
    uuid_string = ''.join(uuid_string)
    return uuid_string


def response(msg, code):
    return jsonify({"msg": msg}), code


