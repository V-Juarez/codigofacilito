class Usuario:
    def __init__(self,nombre):
        # Metodo constructor
        self._nombre = nombre                       # _

    def saludar(self, saludo):
        print(saludo + self.nombre)

class Empleado(Usuario):
    __salario = 0

    def modificar_salario(self,salario):
        self.__salario = salario

    def ver_salario(self):
        print(self.__salario)

    def saludar(self):
        super().saludar("Hola!")
        print("Mi nombre es: " + self._nombre + " y gano: " + str(self.__salario) )

empleado = Empleado("Victor")
empleado.modificar_salario(1000)
empleado.ver_salario()
print(empleado._Empleado__salario)


# _ Informacion Protegido -> 1 guion bajo    acceso de instancia.
# __ Informacion Privado -> 2 guion bajo

#print(empleado._nombre)         # de clara de esta manera No es recomendable utilizar lo heredado de clases
