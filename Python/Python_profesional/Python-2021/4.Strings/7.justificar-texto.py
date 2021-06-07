#!/usr/bin/env python
# -*- coding: utf-8 -*-

mensaje = 'Hola Mundo'


#  ljust -> justificar a la Izquierda
#  rjust -> justificar a la derecha
#  center -> center

mensaje = mensaje.ljust(20)
print(mensaje)
mensaje1 = mensaje.rjust(50)
print(mensaje1)
mensaje2 = mensaje.center(40)
print(mensaje2)

