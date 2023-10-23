from flask import jsonify


def message_error(error):
    data = {'message': str(error)}
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response, 500


def message(message_send):
    data = {'message': message_send}
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response, 200
