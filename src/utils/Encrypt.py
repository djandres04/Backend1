import bcrypt


# Función para hashear una contraseña
def hash_password(password):
    # Genera un salt aleatorio
    salt = bcrypt.gensalt()
    # Hashea la contraseña con el salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


# Función para verificar una contraseña
def verify_password(input_password, hashed_password):
    # Verifica si la contraseña ingresada coincide con el hash almacenado
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)
