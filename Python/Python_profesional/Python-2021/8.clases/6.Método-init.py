#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Usuario:
    # Object
    def __init__(self, username='', password=''):
        #  print('Estamos creando un usuario')
        self.username = username
        self.password = password



user1 = Usuario('user1', 'password1')
user2 = Usuario('user2', 'password1')
user3 = Usuario('user3', 'password1')

user4 = Usuario()

print(user1.__dict__) # Dict 
print(user2.__dict__)
print(user3.__dict__)
print(user4.__dict__)
