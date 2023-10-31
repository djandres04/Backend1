from flask import Blueprint, request, jsonify
from flask_cors import CORS

from src.models import ModelUser
from src.utils.AuthenticateJWT import authentication_jwt
from src.utils.token import token_required
from src.utils import  JsonMessage

main = Blueprint('home_blueprint', __name__)
CORS(main)


@main.route('/login', methods=['POST'], strict_slashes=False)
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]

        user = ModelUser.login(email, password)

        if user:
            access_token = authentication_jwt(user)
            data = {'access_token': access_token}
            response = jsonify(data)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            data = {'access_token': '','message':'bad credentials'}
            response = jsonify(data)
            response.headers['Content-Type'] = 'application/json'
            return response

    except Exception as ex:
        print(str(ex))
        return str(ex)


@main.route('/register', methods=['POST'], strict_slashes=False)
def register():
    try:
        email = request.json["email"]
        password = request.json["password"]
        first_name = request.json["first_name"]
        last_name = request.json["last_name"]

        temp = ModelUser.register(email, password, first_name, last_name)
        return temp

    except Exception as ex:
        print(str(ex))
        return str(ex)