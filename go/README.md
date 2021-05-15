<h1>Go</h1>

<h3>Eduardo Perez</h3>

<h1>Tabla de Contenido</h1>


# 1. Introduccion

## Introducción al curso



## ¿Qué es Go?

- [Go](https://devhints.io/go?fbclid=IwAR1WAcFKHTZwlLHH2crxqjqnnG32R2TukgQxPv9mOIb8C21ykU7zZb14m0Y)

## Instalación

- [golang](https://golang.org/)

## Hola mundo

Estructura de escritura de go

```go
package main

import "fmt"

// go build maing.go -> Crea un archivo ejecutable
//  go run main.go ejecuta el archivo sin compilar

func main() {
	fmt.Println("Hola mundo! desde el curso profesional de Go")
}
```

## Declarar variables

```go
package main

import "fmt"


func main() {

	var nombre  string = "Eduardo Ismael"
	
	var edad int

	// nombre = "Eduardo Isamel"
	edad = 26

	fmt.Println(nombre)
	fmt.Println(edad)
}
```

## Declaración de variables pt2

la declaración corta o inferida solo aplica en el cuerpo de funciones/métodos y su declaración agrupada en inline

la declaración tipada o definida aplica para constantes y variables dentro y fuera de funciones/métodos siendo estas consideradas globales dentro del paquete y se pueden exportar fuera del mismo nombrándola en mayúsculas o con inicial mayúscula

## Función Println

Es un ejemplo de función variadica o de parámetros variables que se apoya en interfaz genérica

```go
fmt.Println("El nombre es:", nombre, "la edad es:", edad, "la altura es:", altura)
```


## Declarar múltiples variables

la declaración puede agruparse y combinarse

```go
var (
nombre bool
apellido = 10
pais string
)

		var nombre, apellido, pais string

		fmt.Println(nombre, apellido, pais)
```

## Constantes

```go
package main

import "fmt"

const Curso string =  "Curso Profesional de Go!"

func main() {
	
	fmt.Println(Curso)
}
```

## Operadores relacionales

	Operadores relacionales
		>
		<
		>=
		<=
		==
		!=

## Operadores lógicos

	Operadores logicos

	&&
	||
	!

## Secuencia de valores

```go
package main 

import "fmt"

const {
  Domingo int = 0
  Lunes int = 1
  Martes int = 2
  Miercoles int = 3
  Jueves int = 4
  Viernes int = 5
  Sabado int = 6
}

const (
    Domingo int = iota + 0  // 0
    Lunes 
    Martes 
    Miercoles 
    Jueves 
    Viernes 
    Sabado 
)

func main() {
	
	fmt.Println(Domingo)
	fmt.Println(Lunes)
	fmt.Println(Martes)
	fmt.Println(Miercoles)
	fmt.Println(Jueves)
	fmt.Println(Viernes)
	fmt.Println(Sabado)
}
```

## Strings

```go
package main

import "fmt"
import "reflect"

func main() {

	// var curso string = "Curso Profesional de Go!"  1

	// var curso = "Curso Profesional de Goo!"  2

	curso := "Cruso profesional de Go!"				//3

	longitud := len(curso)

	fmt.Println(curso, longitud)

	primerCaracter := curso[0]  // char => uint*
	ultimoCaracter := curso [ len(curso) - 1 ]

	fmt.Println(primerCaracter)
	fmt.Println(reflect.TypeOf(primerCaracter))

	fmt.Printf("%c\n", primerCaracter)
	fmt.Printf("%c\n", ultimoCaracter)

}
```

## Lectura de valores

```go
package main

import "fmt"

func main() {

	var nombre string
	var edad int
	var altura float32

	fmt.Print("Ingresa tu nombre: ")
	fmt.Scanf("%s", &nombre)

	fmt.Print("Ingresa tu edad: ")
	fmt.Scanf("%d", &edad)

	fmt.Print("Ingresa tu altura: ")
	fmt.Scanf("%f", &altura)

	fmt.Printf("Hola %s con a edad %d y una altura %.2f\n", nombre, edad, altura)
}
```

# 2. Estucturas de datos

## Arreglos

```go
package main

import "fmt"

func main() {


	var numeros[6] int 

	numeros[0] = 100
	numeros[1] = 200
	numeros[2] = 300
	numeros[3] = 400
	numeros[4] = 500
	numeros[5] = 600

	fmt.Println(numeros)
}
```

## Arreglos pt2



## Slice



## Sclice pt2



## Resumen Slice

```go
package main 

import "fmt"

func main() {

	numeros := []int {1, 2, 3, 4, 5, 6}

	numeros[0] = 100
	numeros[5] = 600

	inicio := numeros[0:3]
	final := numeros[3:6]

	fmt.Println(numeros)
	fmt.Println(inicio)
	fmt.Println(final)
}
```

## Función Make

```go
package main

import "fmt"

func main() {

	slice := make([]int, 3, 3)

	slice[0] = 100
	slice[1] = 200
	slice[2] = 300 

	slice = append(slice, 400)

	fmt.Println(slice)
	fmt.Println(len(slice))
	fmt.Println(cap(slice))
}
```

## Mapas

```go
package main

import "fmt"

func main() {

	dias := make(map[int]string)

	dias[0] = "Domingo"
	dias[1] = "Lunes"
	dias[2] = "Mates"
	dias[3] = "Miercoles"
	dias[4] = "Jueves"
	dias[5] = "Viernes"
	dias[6] = "Sabado"

	dias[4] = "JUEVES"
	// eliminar la llave

	delete(dias, 4)
	fmt.Println(dias)
	fmt.Println(dias[4])
	// fmt.Println(cap(slice))
}
```
## Iterar sobre mapas

```go
package main

import "fmt"

func main() {

	usuarios := map[int] string {}

	usuarios[1] = "Usuario 1"
	usuarios[2] = "Usuario 2"
	usuarios[3] = "Usuario 3"
	usuarios[4] = "Usuario 4"

	for id, valor := range usuarios {
		fmt.Println(id, valor)
	}
}
```

# 3. Controles de flujos

## Condicionales

```bash
package main

import "fmt"

func main() {

	var edad int
	fmt.Print("Ingresa tu edad: ")
	fmt.Scanf("%d", &edad)

	if edad >= 18 {
		fmt.Println("El usuario es mayor de edad")
	} else {
		fmt.Println("El usuario es menor de edad!")
	}
}
```
## Múltiples condiciones

```bash
package main

import "fmt"

func main() {

	// else if
	// 10 - 8/9 - 6/7 -5

	var calificacion int

	fmt.Print("Ingresa una calificacion: ")
	fmt.Scanf("%d", &calificacion)

/* 	if calificacion == 10 {
		fmt.Println("Felicidades, obtuviste una calificacion perfecta!")
	} else {
		if calificacion == 8 || calificacion == 9 {
			fmt.Println("Aprobaste la materia")
		} else {
			if calificacion == 6 || calificacion == 7 {
				fmt.Println("Aprobaste la materai, pero necesitas estudiar mas")
			} else {
				if calificacion >= 0 && calificacion <= 5 {
					fmt.Println("No aprobaste la materia")
				} else {
					fmt.Println("Calificacion no valida")
				}
			}
		}
	} */
	if calificacion == 10 {
		fmt.Println("Felicidades, obtuvistes una calificacion perfecta!")
	} else if calificacion == 8 || calificacion == 9 {
		fmt.Println("Aprobaste la materia")
	} else if calificacion == 6 || calificacion == 7 {
		fmt.Println("Aprobaste la materia, pero necesitas estudiar mas")
	} else if calificacion >= 0 && calificacion <= 5 {
		fmt.Println("No aprebaste la materia")
	} else {
		fmt.Println("Calificacion no valida")
	}
}
```
## Declaración de variable en condiciones

```bash
package main

import "fmt"

func main() {

	if nombre, edad := "Cody", 7; nombre == "Cody " {
		fmt.Println("Hola", nombre, "te damos la bienvenido al curso de Go!")
	} else {
		fmt.Println("Los valores son: ", nombre, edad)
	}
	
}
```
## Switch

```bash
	package main

import "fmt"

func main() {

	// else if
	// 10 - 8/9 - 6/7 -5

	var calificacion int

	fmt.Print("Ingresa una calificacion: ")
	fmt.Scanf("%d", &calificacion)

	switch {
	case calificacion == 10:
		fmt.Println("Felicidades, obtuvistes una calificacion perfecta!")
	case calificacion == 8 || calificacion == 9:
		fmt.Println("Aprobaste la materia")
	case calificacion == 6 || calificacion == 7:
		fmt.Println("Aprobaste la materia, pero necesitas estudiar mas")
	case calificacion >= 0 && calificacion <= 5:
		fmt.Println("No aprebaste la materia")
	default:
			fmt.Println("Calificacion no valida")
	}

  	switch calificacion {
	  case 10:
	  	fmt.Println("Felicidades, obtuvistes una calificacion perfecta!")
	  case 8, 9:
	  	fmt.Println("Aprobaste la materia")
	  case 6, 7:
	  	fmt.Println("Aprobaste la materia, pero necesitas estudiar mas")
	  case 1, 2, 3, 4, 5:
	  	fmt.Println("No aprebaste la materia")
	  default:
	  	fmt.Println("Calificacion no valida")
	}

}
```
## Obtener valores de un mapa

```bash

```
## Ciclo for

```bash

```
## For como While

```bash

```
## Foreach

```bash

```
## Continue and Break

```bash

```
## Función panic

```bash

```
## For como Do while

```bash

```
## For como ciclo infinito

```bash

```

# 4. Funciones

## Definición de funciones
## Retornar valores
## Funciones anonimas
## Funciones como argumentos
## Retornar funciones
## Bloques y alcances
## Variables y scopes
## Variadic functions
## Punteros
## Funciones recursivas
## Funciones como valores
## Manejo de errores
## Variables globales
## Programar funciones
## Programar funciones pt2
## función recover


# 5. Tipos de Estructuras

## Crear estructuras
## Métodos
## Relación uno a uno
## Relación uno a muchos
## Enums
## Interfaces
## Múltiples interfaces
## Interfaces vacías
## Creación de paquetes
## Modificadores de acceso

# 6. Proyecto

## Introducción
## Leer valores del teclado
## Refactor
## Crear usuario
## Listar usuarios
## Limpiar consola
## Eliminar usuarios



