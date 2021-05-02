from abc import ABC, abstractmethod

#clase abstract
class EstructuraAbstracta(ABC):
    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass


class Hash(EstructuraAbstracta):
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def agregar(self,llave,valor):
        datos[llave] = valor

class Queve(EstructuraAbstracta):
    datos = {}

    def obtener(self,llave):
        datos[0]

    def agregar(self,llave,valr):
        datos[len(datos)-1] = valor


class FilaBanco:
    #usuarios = Queve()
    #usuarios = Hash{}

    def __init__(self,almacen_usuarios):
        if not isinstance(almacen_usuarios, EstructuraAbstracta):
            raise ValueError('Store is not supported')

        self.usuarios = almacen_usuarios

    def siguiente_usuario(self, numero):
        # Implementacion
        return usuarios.obtener(numero)

    def formar_usuario(self,numero,usuario):
        self.usuarios.agregar[numero,usuario]


FilaBanco(Queve())
