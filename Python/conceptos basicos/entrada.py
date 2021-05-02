nombre = input("Cual es tu nombre?\n")
edad = int(input("Cual es tu edad?\n"))
peso = float(input("cual es tu peso?\n"))

autorizado = input("Estas autorizado?(si/no)\n") == "si"

print("Hola", nombre)
print("edad", edad)
print("peso", peso)
print("autorizado", autorizado)
