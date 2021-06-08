#!/usr/bin/env python
# -*- coding: utf-8 -*-




def suma(n1, n2):
    #  resultado = n1 + n2
    #  return resultado
    return n1 + n2, 'La funcion retorna 2 valores'

numero_dos = int(input('Ingresa el segundo numero entero: '))
numero_uno = int(input('Ingresa el primer numero entero: '))

#  resultado, mensaje = suma(numero_uno, numero_dos)
resultado, _ = suma(numero_uno, numero_dos)
print('El resultado es: ', resultado)
#  print(mensaje)
