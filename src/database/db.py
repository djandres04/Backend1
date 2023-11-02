import psycopg2

from decouple import config


def get_connection():
    try:
        conn = psycopg2.connect(host=config('DB_HOST'),
                                database=config('DB_DATABASE'),
                                port=config('DB_PORT'),
                                user=config('DB_USERNAME'),
                                password=config('DB_PASSWORD'))
        return conn
    except Exception as ex:
        return 'Connection Failed', 500
