#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
a -> La funcion principal (Decorador)
b -> La funcion de decoarar
c - > La funcion decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c():
        #  print('Nos, encontramos en la funcion c.')
        print('<<< antes del llamado')
        funcion_b()
        print('>>> Despues del llamdado')


    return funcion_c


@funcion_a
def saludar():
    print('Hola, nos encontramos en una funcion')

@funcion_a
def suma():
    print(10 + 30)

saludar()
suma()
