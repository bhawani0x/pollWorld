import uuid
from flask import jsonify
from datetime import datetime


def generate_token():
    # Generate a UUID version 4 (random UUID)
    uuid_string = str(uuid.uuid4())
    uuid_string = uuid_string.split('-')
    uuid_string = ''.join(uuid_string)
    return uuid_string


def response(msg, code):
    return jsonify({"msg": msg}), code


def generate_log(level, reason):
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    log_message = f"{current_time} - Reason: {reason}"
    #
    # if level == 'INFO':
    #     app.logger.info(log_message)
    # elif level == 'WARNING':
    #     app.logger.warning(log_message)
    # elif level == 'ERROR':
    #     app.logger.error(log_message)
    # elif level == 'CRITICAL':
    #     app.logger.critical(log_message)
    # else:
    #     app.logger.error(f"Invalid log level: {level}")
