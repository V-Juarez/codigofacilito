#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal():

    def comer(self):
        print('La Animal come.')

    def dormir(self):
        print('La Animal duerme.')

class Mascota(Animal): # Clase Padre
    
    def comer(self):
        print('La mascota come')


class Felino:

    def cazar(self):
        print('El felino caza.')

class Gato(Mascota, Felino):
    
    def __init__(self, nombre):
        self.nombre = nombre


    def comer(self):
        print(f'{self.nombre} come.')

    def dormir(self):
        super().comer()
        print(f'{self.nombre} duerme')

patricio = Gato('Patricio')

patricio.comer()
patricio.dormir()




