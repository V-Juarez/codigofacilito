lenguaje = "Python; java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separador = ("; ")

resultados = lenguaje.split("separador")    #resultados es una lista

nuevo_string = separador.join(resultados)

print(resultados)
print(nuevo_string)


texto = """ Este es un texto
con
saltos de
linea"""

resultado = texto.splitlines()
print(resultado)
