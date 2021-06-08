#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Docstrisng
# __doc__ (Modulos, Clases, Metodos y Funciones)

def suma(numero_1, numero_2):

    """
    La funcion suma 2 numeros enteros.

    Argumentos:
    numero_1 (int)
    numero_2 (int)

    Se retorna la suma de los parametros.
    
    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    500

    """
    return numero_1 + numero_2

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#  print(suma.__doc__)
#  print(help(suma))
