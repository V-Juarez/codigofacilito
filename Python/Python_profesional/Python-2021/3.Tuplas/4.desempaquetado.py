#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  * => lista
# _ => omitir valor

numeros = (1, 2, 3, 4, 5, 6, 8, 9, 10)
#  uno, dos, tres, cuatro, *resto_valores = numeros
#  uno, dos, tres, cuatro, *_ = numeros
uno, _, tres, cuatro, *_, nueve, diez = numeros

print(uno)
#  print(dos)
print(tres)
print(cuatro)
#  print(resto_valores)
print(nueve)
print(diez)


