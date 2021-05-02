texto = " Curso de Python 3, Python basico "

resultado = texto.capitalize()  #Las iniciales son mayusculas

resultado1 = texto.swapcase()   #Las iniciales son minusculas

resultado2 = texto.upper()      #La frase es mayuscula

resultado3 = texto.lower()      #La frase es minuscula

print(resultado)
print(resultado1)
print(resultado2)
print(resultado3)

print(resultado2.isupper())     #retorna un valor boolean, falso o verdadero
print(resultado3.islower())


resultado4 = texto.title()      #cambia el titulo

print(resultado4)

resultado5 = texto.replace("Python", "Ruby", 1) #Remplaza un string

print(resultado5)

resultado6 = texto.strip()
print(resultado6)
