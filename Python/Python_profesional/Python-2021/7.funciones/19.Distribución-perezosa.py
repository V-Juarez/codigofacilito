#!/usr/bin/env python
# -*- coding: utf-8 -*-


def pares():   # Generador -> Lazy iterator
    for numero in range(0, 8, 2):
        #  print(numero)
        yield numero # La funcion suspende su ejecucuion

        print('Se reanuda la ejecucion')


generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print('El generador finalizo')
        break
