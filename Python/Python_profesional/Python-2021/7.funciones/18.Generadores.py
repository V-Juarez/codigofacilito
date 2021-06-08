#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pares():   # Generador -> Lazy iterator
    for numero in range(0, 100, 2):
        #  print(numero)
        yield numero # La funcion suspende su ejecucuion

        print('Se reanuda la ejecucion')

for par in pares():
    print(par)

