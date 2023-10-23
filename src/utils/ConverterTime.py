from datetime import datetime, timedelta
import pytz
import hashlib

time_zone = pytz.timezone('America/Bogota')


def convert_time(hour=0, minute=0, second=0):
    temp_time = datetime.now(time_zone) + timedelta(hours=hour, minutes=minute, seconds=second)

    return int(temp_time.timestamp())


def time_now(hour=0, minute=0, second=0):
    # Obtén la hora en la zona horaria deseada
    date_string = datetime.now(time_zone) + timedelta(hours=hour, minutes=minute, seconds=second)
    # Formatea la hora en el formato deseado (sin zona horaria)
    formatted_date = date_string.strftime('%Y-%m-%d %H:%M:%S')
    # Utiliza strptime() para analizar la cadena
    date_time_obj = datetime.strptime(formatted_date, '%Y-%m-%d %H:%M:%S')
    return date_time_obj
