#!/usr/bin/env python
# -*- coding: utf-8 -*-

def saludar(username):
    mensaje = f'Hola {username}' # Variable Local

    def mostrar_mensaje(): # anidada
        print(mensaje)

    return mostrar_mensaje

username = 'Cody'
respuesta = saludar(username)
respuesta()
respuesta()
respuesta()
respuesta()
