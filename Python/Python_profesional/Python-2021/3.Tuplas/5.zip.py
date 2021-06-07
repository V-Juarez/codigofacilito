#!/usr/bin/env python
# -*- coding: utf-8 -*-

lista = [1, 2, 3, 4, 5, 6, 7, 8]

tupla = (10, 20, 30, 40, 50)

lista_2 = [100, 200, 300, 400, 500]

tupla_2 = [1000, 2000, 3000, 4000, 5000]

resultado = zip(tupla, lista, lista_2, tupla_2) # -> zip
resultado = tuple(resultado)

print(resultado)
