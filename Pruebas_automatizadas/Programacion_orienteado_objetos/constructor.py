class Usuario:
    nombre = "Victor"

    def __init__(self):
        #Metodo constructor
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)

victor = Usuario()
victor.nombre = "Juarez"


victor.saludar("Aloja! Mi nombre es ")


class Contador:
    def __init__(self):
        self.conteo = 0
