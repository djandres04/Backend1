from werkzeug.security import check_password_hash #, generate_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, fullname="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.fullname = fullname

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
#print(generate_password_hash("admin")) #pbkdf2:sha256:600000$WgxpvrORpFSD9vWE$236d473845940d880ff516854fe4a1f2f194f4bc04cd08d21a9b73d6ced8b71d