#!/usr/bin/env python
# -*- coding: utf-8 -*-


nombre = 'Eduardo Ismaiel'
apellido = 'Garcia'

nombre_completo = 'Mr.' + ' ' + nombre + ' ' + apellido + '.'
print(nombre_completo)

nombre_completo = 'Mr. %s %s.' %(nombre, apellido)
print(nombre_completo)
