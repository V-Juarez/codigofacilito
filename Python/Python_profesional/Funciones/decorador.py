# a, b, c
#a(b) -> c

def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Podemos agragar codigo antes")
        resultado = funcion(*args, **kwargs)
        print("Podemos agregar codigo despues")
        return resultado
    return nueva_funcion


@decorador
def funcion_a_decorar():
    print("Este es una funcion a decorar")

@decorador
def suma(val1, val2):
    return val1 + val2

funcion_a_decorar()

print("\n")


resultado = suma(10, 20)
print(resultado)
#funcion_a_decorar()
