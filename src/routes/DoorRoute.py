from flask import Blueprint, request
from flask_cors import CORS
import requests

import json

from src.utils.token import token_required
from src.utils import JsonMessage

from decouple import config

main = Blueprint('devdoor_blueprint', __name__)
CORS(main)

topic = 'door'


@main.route('/add', methods=['POST'], strict_slashes=False)
def add_door():
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        try:
            headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}
            return "hi"

        except Exception as ex:
            print(str(ex))
            return JsonMessage.message_error(ex)

    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)


@main.route('/edit', methods=['PUT'], strict_slashes=False)
def edit_door():
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        try:
            headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}
            data = request.json

            response = requests.put(config('SERVER_REST') + '/door/', data=data, headers=headers)
            return response.json()

        except Exception as ex:
            print(str(ex))
            return JsonMessage.message_error(ex)

    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)


@main.route('/delete/<id>', methods=['DELETE'], strict_slashes=False)
def delete_door(id):
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        try:
            headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}
            database_id = request.json['database_id']
            data = json.dumps({'id': id, 'topic': topic, 'database_id': database_id})
            response = requests.delete(config('SERVER_REST') + '/door/', data=data, headers=headers)

            return response.json()

        except Exception as ex:
            print(str(ex))
            return JsonMessage.message_error(ex)

    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)
