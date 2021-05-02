import os
import pprint

def clear_system(function):

    def wrap(*args, **kwargs):
        os.system('clear')
        result = function(*args, **kwargs)
        input('')
        os.system('clear')

    wrap.__doc__ = function.__doc__
    return wrap

def show_user(user):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(user)

@clear_system
def create_user(collection):
    """A) Crear un usuario """

    username = input('Username: ')
    edad = int(input('Edad: '))
    email = input('Email: ')

    # Dcumento -> Json -> dict
    user = dict(username=username, edad=edad, email=email)

    direccion = input('Desea ingresar su direccion? (S/N)').lower()

    if direccion == 's':
        user['direccion'] = get_address()

    collection.insert_one(user)
    print(user)

    return user

def get_address():
    calle = input('Calle')
    ciudad = input('Ciudad')
    estado = input('Estado')
    codigo_postal = input('codigo_postal')

    direccion = dict(calle=calle,
                        ciudad=ciudad,
                        estado=estado,
                        codigo_postal=codigo_postal)

    return direccion

@clear_system
def get_user():
    """B) Consultar usuario"""

    username = input('Username: ')

    user = collection.find_one(
            {'username': username},
            {'_id': false}
    )

    if user:
        print(user)
        return user
    else:
        print('No fue posible obtener documento alguno,')

def delete_user(collection):
    """C) Eliminar un usuario"""
    username = input('Username: ')

    return collection.remove(
        {'username': username}
    )

def update_user():
    """D) Actualizar usuario"""
    print('Actualizar usuario')

def default(*args, **kwargs):
    print('Opcion no valida')


#completar la funcion de actualizacion -> eduardo@codigofacilto.com
# Completar Trigger para elimiar un usuario, em -1
