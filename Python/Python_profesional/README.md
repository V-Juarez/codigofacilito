<h1>Python</h1>

<h2>Eduardo Garcia</h2>

<h1>Tabla de Contenido</h1>

- [1. Introducción](#1-introducción)
  - [Presentación del curso](#presentación-del-curso)
  - [Instalar Python en Windows](#instalar-python-en-windows)
  - [Editores de Texto](#editores-de-texto)
  - [Ejecutar scripts](#ejecutar-scripts)
  - [Variables](#variables)
  - [Constantes](#constantes)
  - [Palabras reservadas en Python](#palabras-reservadas-en-python)
  - [Comentarios](#comentarios)
  - [Tipos de datos](#tipos-de-datos)
  - [Tipado dínamico](#tipado-dínamico)
  - [Operadores relacionales](#operadores-relacionales)
  - [Operadores lógicos](#operadores-lógicos)
  - [Conocer tipos de datos](#conocer-tipos-de-datos)
  - [Leer valores por teclado](#leer-valores-por-teclado)
  - [Convertir tipos de datos](#convertir-tipos-de-datos)
  - [Crear múltiples variables](#crear-múltiples-variables)
- [2. Listas](#2-listas)
  - [¿Qué son las listas?](#qué-son-las-listas)
  - [Listas](#listas)
  - [Actualizar elementos](#actualizar-elementos)
  - [Sublistas](#sublistas)
  - [Modificar listas](#modificar-listas)
  - [Métodos de listas](#métodos-de-listas)
  - [Index](#index)
  - [Matrices](#matrices)
- [3. Tuplas](#3-tuplas)
  - [¿Qué son las tuplas?](#qué-son-las-tuplas)
  - [Índices de tuplas](#índices-de-tuplas)
  - [Listas y tuplas](#listas-y-tuplas)
  - [Desempaquetado](#desempaquetado)
  - [Zip](#zip)
- [4. Strings](#4-strings)
  - [Strings con listados](#strings-con-listados)
  - [Concatenar pt1](#concatenar-pt1)
  - [Concatenar pt2](#concatenar-pt2)
  - [Validar/50 sub strings](#validar-sub-strings)
  - [Función print](#función-print)
  - [FString](#fstring)
  - [Justificar texto](#justificar-texto)
- [5. Diccionarios](#5-diccionarios)
  - [¿Qué son los diccionarios?](#qué-son-los-diccionarios)
  - [Diccionarios](#diccionarios)
  - [Obtener elementos](#obtener-elementos)
  - [Llaves, Items y valores](#llaves-items-y-valores)
  - [Eliminar elementos](#eliminar-elementos)
- [6. Ciclos y condiciones](#6-ciclos-y-condiciones)
  - [Tipo None](#tipo-none)
  - [Valores falsos](#valores-falsos)
  - [Condiciones](#condiciones)
  - [elif](#elif)
  - [Ternario](#ternario)
  - [Ciclo While](#ciclo-while)
  - [Foreach](#foreach)
  - [Función enumerate](#función-enumerate)
  - [break and continue](#break-and-continue)
- [7. Funciones](#7-funciones)
  - [Funciones](#funciones)
  - [Argumentos](#argumentos)
  - [Retornar valores](#retornar-valores)
  - [Parámetros opcionales](#parámetros-opcionales)
  - [Args](#args)
  - [Args pt2](#args-pt2)
  - [Kwargs](#kwargs)
  - [Scopes](#scopes)
  - [Funciones anidadas](#funciones-anidadas)
  - [Ciudadanos de primera clase](#ciudadanos-de-primera-clase)
  - [Funciones lambda](#funciones-lambda)
  - [Callbacks](#callbacks)
  - [Variables no locales](#variables-no-locales)
  - [Retornar funciones](#retornar-funciones)
  - [Closures](#closures)
  - [Decoradores](#decoradores)
  - [Decoradores pt2](#decoradores-pt2)
  - [Documentar funciones](#documentar-funciones)
  - [Testear funciones](#testear-funciones)
- [8. Clases](#8-clases)
  - [Clases](#clases)
  - [Atributos de clase](#atributos-de-clase)
  - [Atributos de instancia](#atributos-de-instancia)
  - [Atributos dinámicos](#atributos-dinámicos)
  - [Métodos](#métodos)


# 1. Introducción

## Presentación del curso

Curso de python Profesional

## Instalar Python en Windows

- [python](https://www.python.org/)

```py
print('Hola Mundo')
```

## Editores de Texto

- [Code](https://code.visualstudio.com/)

## Ejecutar scripts

```bash
python3 main.py
```

## Variables

Variables ver como etiquetas.

```bash
titulo_curso = 'Profesional de Python' # Variable

curso = 'Curso Python'

print(titulo_curso)
```

- [Palabras Reservadas en Python](https://clases.codigofacilito.com/articulos/palabras_reservadas_python)

## Constantes

```py
TITULO_CURSO = 'Curso Profesional de Python'

print(TITULO_CURSO)
```

## Palabras reservadas en Python

Cómo menciamos en vídes anteriores, existen ciertas palabras las cuales no podemos utilizar para nombrar a nuestras variables, funciones o clases. A este tipo de palabras las conoceremos como palabras reservadas. Y estan diseñadas para realizar tareas especificar por parte del lenguajes.

Aquí el listado de todas ellas:

|     |       |        |      |
| ------- | ------- | ------------ | -------------- |
| False	| class	| is	| return |
| None	| continue	| lambda	| try |
| True	| def	| nonlocal	| while |
| and	| del	| not	| with |
| as	| elif	| or	| yield |
| assert	| else	| pass	| * |
| break	| except	| raise	| * |

- [List of Keywords in Python](https://www.programiz.com/python-programming/keyword-list)

## Comentarios

```py
# Comentario de linea
print('Hola Mundo')

"""
Este es un comentario que
posee saltos
de linea
"""
```

## Tipos de datos

```py
# string

titulo_curso = 'Curso Profesional de Python'
print(titulo_curso)

nombre_completo = "Eduardo Ismael"
print(nombre_completo)

mensaje = "'CodigoFacilito'"
print(mensaje)

mensaje_one = '''Te encuentas 
en el curso de Python.
En codigofacilito'''

print(mensaje_one)

# int

numero_uno = - 10   # Podemos realizar operaciones -> suma, resta, multipliacion y division
                    # Al dividir con / Obtenemos un tipo de dato flotante
                    # Al dividir con // Otenemos un tipo de dato entero
print(numero_uno)

# float

numero_dos = 3.14
print(numero_dos)

# bool

valor = True
valor1 = False

print(valor)
print(valor1)
```

## Tipado dínamico

```py
valor = 'Eduardo'
valor = 2
valor = 3.1
valor = True

print(valor)


valor = 'Eduardo'
print(valor)
valor = 2
print(valor)
valor = 3.1
print(valor)
valor = True
print(valor)
valor = 'CodigoFacilito'
print(valor)
```

## Operadores relacionales

```py
"""
>
<
<=
>=
== 
!=
"""


numero_uno = 10
numero_dos = 20


resultado = numero_uno > numero_dos
print(resultado)
```

## Operadores lógicos

```py
and, or y not
```

## Conocer tipos de datos



## Leer valores por teclado



## Convertir tipos de datos



## Crear múltiples variables



# 2. Listas

## ¿Qué son las listas?



## Listas



## Actualizar elementos



## Sublistas



## Modificar listas



## Métodos de listas



## Index



## Matrices



# 3. Tuplas

## ¿Qué son las tuplas?



## Índices de tuplas



## Listas y tuplas



## Desempaquetado



## Zip



# 4. Strings

## Strings con listados



## Concatenar pt1



## Concatenar pt2



## Validar sub strings



## Función print



## FString



## Justificar texto



# 5. Diccionarios

## ¿Qué son los diccionarios?



## Diccionarios



## Obtener elementos



## Llaves, Items y valores



## Eliminar elementos



# 6. Ciclos y condiciones

## Tipo None



## Valores falsos



## Condiciones



## elif



## Ternario



## Ciclo While



## Foreach



## Función enumerate



## break and continue



# 7. Funciones

## Funciones



## Argumentos



## Retornar valores



## Parámetros opcionales



## Args



## Args pt2



## Kwargs



## Scopes



## Funciones anidadas



## Ciudadanos de primera clase



## Funciones lambda



## Callbacks



## Variables no locales



## Retornar funciones



## Closures



## Decoradores



## Decoradores pt2



## Documentar funciones



## Testear funciones



# 8. Clases

## Clases



## Atributos de clase



## Atributos de instancia



## Atributos dinámicos



## Métodos



Método init
Herencia
Herencia múltiple
Sobre escritura de métodos
Sobre escritura de métodos pt2
Métodos de clase

