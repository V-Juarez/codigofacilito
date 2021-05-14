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
## Arreglos pt2
## Slice
## Sclice pt2
## Resumen Slice
## Función Make
## Mapas
## Iterar sobre mapas


# 3. Controles de flujos

## Condicionales
## Múltiples condiciones
## Declaración de variable en condiciones
## Switch
## Obtener valores de un mapa
## Ciclo for
## For como While
## Foreach
## Continue and Break
## Función panic
## For como Do while
## For como ciclo infinito

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



