#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  #  Attrs de clases
#  Attrs de instancias

class Usuario:
    
    def inicializar(self, username, password):
        # Anadiendo attrs al objeto
        #  self.username = ''
        self.username = username
        self.password = password
        #  self.password = ''

user1 = Usuario()
user2 = Usuario()


user1.inicializar('User1', 'password1')
user2.inicializar('User2', 'password2')


print(user1.__dict__)
print(user2.__dict__)
