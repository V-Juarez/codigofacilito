#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  print('String', 10, 10.3, True)
def promedio(*args): # convencion y debe llamarse *args 
    #  print(args)
    #  print(type(args))

    return sum(args) / len(args)

#  resultado = promedio([10, 10, 5, 7, 10])
resultado = promedio(10, 10, 5, 7, 10)
print(resultado)
