class Animal:
    def comer(self):
        print("Comiendo")

    def dormir(self):
        print("Durmiendo")

    def comun(self):
        print("Este es un metodo de Animal")

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print("Este es un metodo de Mascota")

class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("Ladrando")

    def dormir(self):
        print(self.nombre, "esta durmiendo!")
        Animal.dormir(self)
        print("No molestar")

    def comun(self):
        print("Este es un metodo de Perro")

class Gato(Animal):
    def ronroneo(self):
        print(ronroneo)

    def comun(self):
        print("Este es un metodo de Gato")



firulasis = Perro("Firulasis")
firulasis.comun()
firulasis.fecha_adopcion("hoy")
print(firulasis.fecha_de_adopcion)
firulasis.ladrar()
firulasis.comer()
firulasis.dormir()


bola_de_nieve = Gato()
bola_de_nieve.comer()
bola_de_nieve.dormir()
