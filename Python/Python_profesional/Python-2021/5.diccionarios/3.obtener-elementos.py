#!/usr/bin/env python
# -*- coding: utf-8 -*-

diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print('a' in diccionario)

# valor = diccionario['a']
# print(valor)

# geet
valor = diccionario.get('z', 'La llave no existe en el diccionario')
print(valor)

#  setdeafult
valor = diccionario.setdefault('e', 5)
print(valor)
