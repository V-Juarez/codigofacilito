#!/usr/bin/env python
# -*- coding: utf-8 -*-



"""
a -> La funcion principal (Decorador)
b -> La funcion de decoarar
c - > La funcion decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        #  print('Nos, encontramos en la funcion c.')
        print('<<< antes del llamado')
        resultado = funcion_b(*args, **kwargs)
        print('>>> Despues del llamdado')

        return resultado

    return funcion_c


@funcion_a
def saludar():
    print('Hola, nos encontramos en una funcion')

@funcion_a
def suma(numero_1, numero_2):
    return numero_1 + numero_2
    #  print(10 + 30)

saludar()
resultado = suma(20, 30)
print(resultado)
