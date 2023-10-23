from src.database.db import get_connection

from src.utils import JsonMessage
from src.utils.Encrypt import verify_password
from src.utils.Encrypt import hash_password
from src.utils.ConverterTime import time_now

from src.models.entities.User import Users


def login(email, password):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM accounts WHERE email = '{email}'")

        row = cur.fetchone()
        if row is not None:
            hashed_password = bytes(row[1])

            if verify_password(password, hashed_password):
                cur.execute(f"UPDATE accounts SET last_login = '{time_now()}' WHERE email = '{email}'")
                temporal_out = Users(row[0], row[1], row[3], row[4], row[5])
            else:
                temporal_out = None

        else:
            temporal_out = None

        # Cerrar el cursor y la conexión a la base de datos
        cur.close()
        conn.commit()
        conn.close()

        return temporal_out

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)


def register(email, password, first_name, last_name):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM accounts WHERE email = '{email}'")

        row = cur.fetchone()

        if row is not None:
            temporal_out = JsonMessage.message("User exist")
        else:
            cur.execute(f"""INSERT INTO accounts ( email,password, name, lastname, created_on, last_login) 
                           VALUES ( '{email}','{hash_password(password)}', '{first_name}', 
                           '{last_name}', '{time_now()}','{time_now()}')""")

            temporal_out = JsonMessage.message("User created")

        # Cerrar el cursor y la conexión a la base de datos
        conn.commit()
        cur.close()
        conn.close()

        return temporal_out

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)
