import json

from database.db import get_connection

from utils import JsonMessage
from utils.Encrypt import verify_password
from utils.Encrypt import hash_password
from utils.ConverterTime import time_now

from models.entities.User import Users

import uuid


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
            id_uuid = uuid.uuid4().hex
            cur.execute(f"""INSERT INTO accounts (user_id ,email,password, name, lastname, created_on, last_login, role) 
                           VALUES ( '{id_uuid}','{email}','{hash_password(password)}', '{first_name}', 
                           '{last_name}', '{time_now()}','{time_now()}', 'user')""")

            temporal_out = JsonMessage.message("User created")

        # Cerrar el cursor y la conexión a la base de datos
        conn.commit()
        cur.close()
        conn.close()

        return temporal_out

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)


def get_users():
    try:
        conn = get_connection()

        cur = conn.cursor()

        cur.execute("""SELECT user_id, name, lastname, email FROM accounts WHERE role = 'user';""")

        row = cur.fetchall()

        if row is None:
            temporal_out = JsonMessage.message("")
        else:
            result = []
            for record in row:
                result.append({
                    'user_id': record[0],
                    'first_name': record[1],
                    'last_name': record[2],
                    'email': record[3],
                    'role': 'user'
                })

            temporal_out = json.dumps(result)

        # Cerrar el cursor y la conexión a la base de datos
        conn.commit()
        cur.close()
        conn.close()

        return temporal_out

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)


def edit_user(id_user, name=None, lastname=None, email=None):
    try:
        conn = get_connection()

        cur = conn.cursor()

        cur.execute(f"SELECT name, lastname, email FROM accounts WHERE user_id = '{id_user}'")

        row = cur.fetchone()

        if row is None:
            temporal_out = JsonMessage.message("User dont exist")
        else:
            if ((row[0] == name or name is None) and (row[1] == lastname or lastname is None) and
                    (row[2] == email or email is None)):
                temporal_out = JsonMessage.message("User dont changes")
            else:
                name_server = row[0] if row[0] == name or name is None else name
                lastname_server = row[1] if row[1] == lastname or lastname is None else lastname
                email_server = row[2] if row[2] == email or email is None else email

                cur.execute(f"""UPDATE accounts SET name = '{name_server}', lastname= '{lastname_server}', 
                                email= '{email_server}' WHERE user_id = '{id_user}'""")

                temporal_out = JsonMessage.message("User successful edit")

        # Cerrar el cursor y la conexión a la base de datos
        conn.commit()
        cur.close()
        conn.close()

        return temporal_out

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)


def delete_user(id_user):
    try:
        conn = get_connection()

        cur = conn.cursor()

        cur.execute(f"SELECT * FROM accounts WHERE user_id = '{id_user}'")

        row = cur.fetchone()

        if row is None:
            temporal_out = JsonMessage.message("User dont exist")
        else:
            cur.execute(f"DELETE FROM accounts WHERE user_id= '{id_user}'")
            temporal_out = JsonMessage.message("User successful delete")
        # Cerrar el cursor y la conexión a la base de datos
        conn.commit()
        cur.close()
        conn.close()

        return temporal_out

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)
