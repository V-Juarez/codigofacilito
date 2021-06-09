#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  #  Attrs de clases
#  Attrs de instancias

class Usuario:
    # Attrs de clase
    username = 'Username por default'
    email = ''

# __dict__

user1 = Usuario()
# 1. cerifica si el attr existen dentro del objeto
# 2. Verifica si el attrs existe dentro de la clase -> Lectura
# 3. Lanzar un error

user1.username = 'Cody' # Anadimos el attrs al objeto
user1.password = '1234'
print(user1.username) # De instancias

print(user1.username)

print(id(user1.username))
print(id(user1.username))
 
user1.password = 'password'
print(user1.__dict__) # Dict


