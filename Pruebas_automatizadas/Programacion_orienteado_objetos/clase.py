class Usuario:
    nombre = "Victor"
    def saludar(self, saludo):
        #print("Hola mi nombre es " + self.nombre)
        print(saludo + self.nombre)

victor = Usuario()
#victor.email = "mytacam78@gmail.com"
victor.nombre = "Emilio"

victor.saludar("Aloja! Mi nombre es ")
#victor.saludar()

cody = Usuario()
cody.nombre = "Cody"

print(victor.nombre)
print(cody.nombre)
