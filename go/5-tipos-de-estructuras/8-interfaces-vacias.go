package main 

import "fmt"

func mostrarVariable(objeto interface{} ) {
	fmt.Printf("El valor de la variable es: %v\n", objeto)
}

func suma(numero1, numero2 int) int {
	return numero1 + numero2
}

type User struct {
	Nombre string
}

func main() { 

	usuario := User { Nombre: "Eduardo" }
	
	mostrarVariable(usuario)
}