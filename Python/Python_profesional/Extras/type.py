def saludo(nombre : str) -> None:
    print("Hola " + nombre)                 #str(nombre))

def suma(num1 : int, num2 : int = 100) -> int:
    return num1 + num2

nombre = "Eduardo"
saludo(nombre)

print(suma(56.7, 89.7))
