class Usuario:
    #pass

    def _init_(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saluda(self):                    #parametro self, y no es palabra resercada
        return "Hola, soy un usuario " + self.nombre

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

codi = Usuario("codi", "codigofacilito@gmail.com", "codigo")
facilito = Usuario()

resultado = codi.saluda()
print(resultado)


    #def crear_nombre(self, nombre):
    #    self.nombre = nombre


#codi = Usuario()
#codi.username = 'codi'
#codi.correo = 'codi@gmail.com'

#facilito = Usuario()
#facilito.username = 'facilito'
#facilito.correo = 'facilito@gmail.com'

#codi.mostrar_username()
#facilito.mostrar_username()

#codi.crear_nombre("codigo") #codigo que le pertenece al def mostrar_nombre
#codi.mostrar_nombre()

#print(type(codi))
#print(type(facilito))
#codi.saluda("codi")
#facilito.saluda("facilito")
