import jwt

from decouple import config
from utils.ConverterTime import convert_time


def authentication_jwt(user):
    payload = {
        'public_id': user.id,
        'fullname': user.first_name + " "+ user.last_name,
        'initial_time': convert_time(),
        'exp': convert_time(minute=30)
    }

    return jwt.encode(payload, config('JWT_KEY'), algorithm='HS256')
