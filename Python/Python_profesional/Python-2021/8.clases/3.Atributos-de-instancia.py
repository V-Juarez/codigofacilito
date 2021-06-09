#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__

user1 = Usuario()
# 1. cerifica si el attr existen dentro del objeto
# 2. Verifica si el attrs existe dentro de la clase -> Lectura
# 3. Lanzar un error

print(user1.username)

print(user1.__dict__) # Dict


