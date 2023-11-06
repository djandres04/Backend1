from flask import Blueprint, request, jsonify
from flask_cors import CORS

from models import ModelUser
from utils.AuthenticateJWT import authentication_jwt
from utils.token import token_required
from utils import JsonMessage

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
            data = {'access_token': '', 'message': 'bad credentials'}
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


@main.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    try:
        return ModelUser.get_users()
    except Exception as ex:
        print(str(ex))
        return str(ex)


@main.route('/users', methods=['PUT'], strict_slashes=False)
def edit_users():
    try:
        id_user = request.json["id_user"]
        data = request.json
        name = data.get("name")
        lastname = data.get("lastname")
        email = data.get("email")

        return ModelUser.edit_user(id_user, name, lastname, email)
    except Exception as ex:
        print(str(ex))
        return str(ex)


@main.route('/users/<id_user>', methods=['DELETE'], strict_slashes=False)
def delete_users(id_user):
    try:
        return ModelUser.delete_user(id_user)
    except Exception as ex:
        print(str(ex))
        return str(ex)
