#!/usr/bin/env python
# -*- coding: utf-8 -*-

elementos = {}

elementos['nombre'] = 'Cody'
elementos['nombre'] = 'CodigoFacilito'  # actualiza la llave
print(elementos)

elementos[(1, 2, 3)] = 'La llave es una tupla'
print(elementos)

elementos = {'a':1, 'b':2, 'c':3, 'a':4}
print(elementos)
