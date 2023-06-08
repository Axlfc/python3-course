import hashlib


def convertir_password(password):
    # Verificar la longitud del password
    if len(password) < 6 or len(password) > 12:
        print("El password debe tener entre 6 y 12 caracteres.")
        return None

    # Calcular el hash del password
    hash_object = hashlib.md5(password.encode())
    hash_password = hash_object.hexdigest()

    # Devolver el resultado
    return hash_password


def main():
    # Ejemplo de uso
    password = input("Ingresa tu password: ")
    converted_password = convertir_password(password)
    if converted_password:
        print("Password convertido:", converted_password)


if __name__ == '__main__':
    main()
