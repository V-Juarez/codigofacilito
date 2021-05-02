class Usuario:
    def __init__(self,nombre):
        # Metodo constructor
        self.nombre = nombre

    def saludar(self, saludo):
        print(saludo + self.nombre)

class Empleado(Usuario):
    salario = 0

    def modificar_salario(self,salario):
        self.salario = salario

    def ver_salario(self):
        print(self.salario)

    def saludar(self):
        super().saludar("Hola!")
        print("Mi nombre es: " + self.nombre + " y gano: " + str(self.salario) )

empleado = Empleado("Victor")
empleado.saludar()

class Pagina:
    def imprimir_pie_pagina(self):
        print(self.pie_pagina)

class PaginaLegal(Pagina):
    def imprimir_pie_pagina(self):
        print("Derechos reservados")
        super().imprimir_pie_pagina()

html = PaginaLegal()
html.pie_pagina = "<p>Hola</p>"

html.imprimir_pie_pagina()


#empleado.modificar_salario(1000)
#empleado.ver_salario()
