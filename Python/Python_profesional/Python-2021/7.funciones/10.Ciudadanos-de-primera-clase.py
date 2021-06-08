#!/usr/bin/env python
# -*- coding: utf-8 -*-

def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

#  print(centigrados_a_farhenheit(10))
#  print(centigrados_a_farhenheit(-1))
#  print(centigrados_a_farhenheit(8))


mi_funcion = centigrados_a_farhenheit

print(type(mi_funcion))

print(mi_funcion(20))
