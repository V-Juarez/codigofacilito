#!/usr/bin/env python
# -*- coding: utf-8 -*-

promedio = lambda *args :  sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

print(promedio(10, 10, 9, 8, 7))
print(aprobatorio(6))


def es_aprobatorio(calificacion):
    return calificacion >= 90


def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}.')
    else:
        print('No aprobaste la materia.')

 
mostrar_mensaje(promedio, es_aprobatorio, 10, 10, 8, 7, 7)

