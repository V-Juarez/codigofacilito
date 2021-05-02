class Numero:
    value = 0

    def __init__(self,value):
            self.value = value

    def compare(self,numero):
        if numero.value > self.value:
            return numero.value
        return self.value

class Cadena:
    value = ""

    def __init__(self,value):
        self.value = value

    def compare(self,cadena):
        palabras = [self.value,cadena.value]
        palabras.sort()
        return palabras[0]

class Lista:
    value = []

    def __init__(self,value):
        self.value = value

    def compare(self,lista):
        if len(self.value) > len(lista.value):
            return self.value
        return lista.value



def retornaElMayor(a,b):
    return a.compare(b)

numero_uno = Numero(10)
numero_dos = Numero(2)

cadena_uno = Cadena("Uriel")
cadena_dos = Cadena("Alenjandro")

lista_uno = Lista([1,2])
lista_dos = Lista([1,2,3,4])

print(retornaElMayor(numero_uno,numero_dos))
print(retornaElMayor(cadena_uno,cadena_dos))
print(retornaElMayor(lista_uno,lista_dos))


# cuando se comparan dos elementos y estas funciona entonces se le conoce como poliformismo
