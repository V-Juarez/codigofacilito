#!/usr/bin/env python
# -*- coding: utf-8 -*-


nombre = 'Eduardo Ismaiel'
apellido = 'Garcia'

#  nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'Perez')
nombre_completo = 'Mr. {nombre} {primer_apellido} {segundo_apellido}.'.format(
    nombre=nombre,
    primer_apellido=apellido,
    segundo_apellido='Perez'

)

print(nombre_completo)
