#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = [8, 90, 5, 44, 132, 600, 3, 2]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#  Menor o mayor
lista.sort()
print(lista[0]) #min
print(lista[-1]) # max

#  Funciones de numero menor y mayor
print(min(lista))
print(max(lista))

#  Conocer que la expresion este en la lista
print(10 in lista)
print(5 in lista)
print(11 not in lista)
