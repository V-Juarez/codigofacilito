#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal():

    def comer(self):
        print('La Animal come.')

    def dormir(self):
        print('La Animal duerme.')

class Mascota(Animal): # Clase Padre
    pass


class Felino:

    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino):
    pass



patricio = Gato()

patricio.comer()
patricio.dormir()
patricio.cazar()
