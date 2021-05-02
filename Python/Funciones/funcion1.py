def crear_mensaje(nombre):
    return "Hola {}, bienvenido al curso de python  3".format(nombre)
    #return mensaje
def suma(val1, val2, val3):
    return val1 + val2 + val3

def obtener_curso():
    return "Curso de Python", "Basico", 3.6

nuevo_mensaje = crear_mensaje("Eduardo")
print(nuevo_mensaje)

resultado = suma(10, 20, 30)
print(resultado)

curso, nivel, version = obtener_curso()
print(curso, nivel, version)
