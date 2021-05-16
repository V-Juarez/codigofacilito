package main

import "fmt"


type Operacion func(balance, cantidad int) int

func suma(numero1, numero2 int) int {
	return numero1 + numero2
}

func resta(numero1, numero2 int) int {
	return numero1 - numero2
}

func ejecutarOperacion(funcion Operacion, balance, cantidad int) {

	fmt.Println("Antes de la operacion")

	resultado := funcion(balance, cantidad)
	fmt.Println("El reusltado es: ", resultado)

	fmt.Println("Despues de la operacion")
}

func main() {

	ejecutarOperacion(suma, 100, 50)
}