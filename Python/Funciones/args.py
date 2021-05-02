#def suma(val1, val2, val3):
def suma(parametro_requerido,*args):
    total = 0
    print(parametro_requerido)
    for valor in args:
        total+=valor
    return total

def usuarios_autenticados(**kwargs):
    print(kwargs)
    #return val1 + val2 + val3

resultado = suma("Este es un argumento parametro requerido", 10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(resultado)

def combinacion(requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)
combinacion("valor requerido", 10, 20, valor_uno=True, valor_dos=False)

usuarios_autenticados(codi=True, facilito=False)
