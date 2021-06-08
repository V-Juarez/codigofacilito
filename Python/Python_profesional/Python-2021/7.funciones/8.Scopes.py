#!/usr/bin/env python
# -*- coding: utf-8 -*-

animal = 'Leon' # variable global -> Funcion, condicion o ciclo


def imprimir_animal():
    global animal 

    animal = 'Ballena'  # variable local

    tipo = 'Mamifero'  # Variable local
    print(animal)
    print(tipo)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))
