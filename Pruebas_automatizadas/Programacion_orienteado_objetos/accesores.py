class Usuario:
    __edad = 0
    def __init__(self,nombre):
        # Metodo constructor
        self._nombre = nombre                       # _

    def saludar(self, saludo):
        print(saludo + self.nombre)

    @property
    def edad(self):             #getter
        return self.__edad


    @edad.setter
    def edad(self,valor):
        if(valor < 0):
            raise ValueError('Edad no puede ser menor que 0')
        self.__edad = valor

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
empleado.edad = 26
print(empleado.edad)
