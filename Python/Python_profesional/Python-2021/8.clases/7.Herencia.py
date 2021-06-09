#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Mascota: # Clase Padre
    
    def comer(self):
        print('La mascota come.')

    def dormir(self):
        print('La mascota duerme.')

class Perro(Mascota): # Clase HIja
    pass


class Gato(Mascota):
    pass

ducke = Perro()

ducke.comer()
ducke.dormir()

patricio = Gato()

patricio.comer()
patricio.dormir()
