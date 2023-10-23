from flask import Blueprint, request
from flask_cors import CORS
import requests

import json

from src.utils.token import token_required
from src.utils import JsonMessage

from decouple import config

main = Blueprint('devices_blueprint', __name__)
CORS(main)


@main.route('/', methods=['POST', 'GET'], strict_slashes=False)
def devices():
    temp_bool, temp_payload = True, "holi"
    if temp_bool:
        headers = {'Client': 'smartHome', 'Content-Type': 'application/json'}
        if request.method == 'POST':
            try:
                topic = request.json['topic']
                if topic == 'light':
                    id_device = request.json['id']

                    data = json.dumps({'topic': topic, 'status': request.json['status']})
                    response = requests.post(config('SERVER_REST') + '/light/' + id_device, data=data,
                                             headers=headers)

                    temp = response.json()
                    if temp["message"] != "Light dont exist":
                        return JsonMessage.message("Dispositivo cambiado de estado")
                    else:
                        return JsonMessage.message_error("Dispositivo no existente")

                elif topic == 'door':
                    id_device = request.json['id']

                    data = json.dumps({'topic': topic, 'status': request.json['status']})
                    response = requests.post(config('SERVER_REST') + '/door/' + id_device, data=data,
                                             headers=headers)

                    temp = response.json()
                    if temp["message"] != "Door dont exist":
                        return JsonMessage.message("Dispositivo cambiado de estado")
                    else:
                        return JsonMessage.message_error("Dispositivo no existente")

                    return "hi"
                elif topic == 'buzzer':
                    return "hi"
                else:
                    return "hi"
            except Exception as ex:
                return JsonMessage.message_error(str(ex))
        else:
            lightserver = config('SERVER_REST') + '/light'
            light = requests.get(lightserver, headers=headers)
            doorserver = config('SERVER_REST') + '/door'
            door = requests.get(doorserver, headers=headers)
            return light.json(), door.json()
    else:
        print(temp_payload)
        return JsonMessage.message_error(temp_payload)


@main.route('/prueba', methods=['GET'], strict_slashes=False)
def prueba():
    try:
        temp_bool, temp_payload = token_required(request.headers)
        if temp_bool:
            return JsonMessage.message("szs pa")
        else:
            print("nada ")
            return JsonMessage.message("nada")
    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)
