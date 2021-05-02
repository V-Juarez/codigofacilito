animal = 'Leon'         #Animal es una variable Global

def mostrar_animal():
    global animal
    animal = 'Ballena'      #variable local
    print(animal)

mostrar_animal()
print(animal)
