import jwt
from decouple import config


def token_required(headers):
    authorization = headers['Authorization']
    encoded_token = authorization.split(" ")[1]
    print(encoded_token)
    try:
        if 'Authorization' in headers.keys():
            authorization = headers['Authorization']
            encoded_token = authorization.split(" ")[1]

            try:
                payload = jwt.decode(encoded_token, config('JWT_KEY'), algorithms=['HS256'])
                return True, payload
            except jwt.ExpiredSignatureError as ex:
                return False, str(ex)
            except jwt.InvalidSignatureError as ex:
                return False, str(ex)
            except Exception as ex:
                return False, str(ex)
    except Exception as ex:
        return False, str(ex)
