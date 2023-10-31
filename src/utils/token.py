import jwt
from decouple import config


def token_required(headers):
    try:
        if 'Token' in headers.keys():
            authorization = headers['Token']
            #encoded_token = authorization.split(" ")[1]
            encoded_token = authorization
            try:
                payload = jwt.decode(encoded_token, config('JWT_KEY'), algorithms=['HS256'])
                return True, payload
            except jwt.ExpiredSignatureError as ex:
                return False, str(ex)
            except jwt.InvalidSignatureError as ex:
                return False, str(ex)
            except Exception as ex:
                return False, str(ex)
        else:
            return False, "token doesn't exist"
    except Exception as ex:
        return False, str(ex)
