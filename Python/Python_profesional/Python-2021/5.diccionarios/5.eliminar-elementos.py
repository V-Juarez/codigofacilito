#!/usr/bin/env python
# -*- coding: utf-8 -*-


diccionario = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

print(len(diccionario))

del diccionario['a']
print(diccionario)
print(len(diccionario))

valor = diccionario.pop('b')
print(valor)
print(len(diccionario))

diccionario.clear()
print(diccionario)
print(len(diccionario))
