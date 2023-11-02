from flask import Blueprint, request
from flask_cors import CORS
import requests

import json

from utils.token import token_required
from utils import JsonMessage

from decouple import config

main = Blueprint('devices_blueprint', __name__)
CORS(main)


@main.route('/', methods=['GET'], strict_slashes=False)
def devices():
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        try:
            headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}

            light = requests.get(config('SERVER_REST') + '/light', headers=headers)
            door = requests.get(config('SERVER_REST') + '/door', headers=headers)

            tempe = {"light": light.json(), "door": door.json()}
            return json.dumps(tempe)
        except Exception as ex:
            print(str(ex))
            return JsonMessage.message_error(ex)
    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)


@main.route('/light', methods=['POST'], strict_slashes=False)
def status_devices_light():
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        try:
            headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}

            topic = request.json['topic']
            id_temp = request.json['id']
            id_device = id_temp[0]

            data = json.dumps({'topic': topic, 'status': request.json['status']})
            response = requests.post(config('SERVER_REST') + '/light/' + id_device, data=data,
                                     headers=headers)

            temp = response.json()
            if temp["message"] != "Light dont exist":
                return JsonMessage.message("Dispositivo cambiado de estado")
            else:
                return JsonMessage.message("Dispositivo no existente")

        except Exception as ex:
            return JsonMessage.message_error(str(ex))
    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)


@main.route('/door', methods=['POST'], strict_slashes=False)
def status_devices_door():
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        try:
            headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}
            id_device = request.json['id'][0]
            topic = request.json['topic']
            data = json.dumps({'topic': topic, 'status': request.json['status']})
            response = requests.post(config('SERVER_REST') + '/door/' + id_device, data=data,
                                     headers=headers)

            temp = response.json()
            if temp["message"] != "Door dont exist":
                return JsonMessage.message("Dispositivo cambiado de estado")
            else:
                return JsonMessage.message("Dispositivo no existente")
        except Exception as ex:
            return JsonMessage.message_error(ex)

    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)


@main.route('/buzzer', methods=['POST'], strict_slashes=False)
def status_devices_buzzer():
    topic = "buzzer"
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        return "hi"

    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)


@main.route('/tempe', methods=['POST'], strict_slashes=False)
def status_devices_tempe():
    temp_bool, temp_payload = token_required(request.headers)
    if temp_bool:
        return "hi"

    else:
        print(temp_payload)
        return JsonMessage.message(temp_payload)
