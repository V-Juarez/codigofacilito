#!/usr/bin/env python
# -*- coding: utf-8 -*-

e = 'e' # variables globales

def funcion_principal():
    a = 'a'   # Variables locales
    b = 'b'

    def funcion_anidada():
        c = 'c'  # variable locales
        nonlocal b
        b = 'Cambion de valor'

        print(a)
        #  print(b)
        print(b)

        print(e)

    funcion_anidada()
    #  print(c)

funcion_principal()
