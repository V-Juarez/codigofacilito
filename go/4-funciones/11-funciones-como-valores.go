package main

import "fmt"

func factorial(numero int) int {

	if numero == 1 {
		return 1
	}

	return factorial(numero - 1) * numero
}

type customeFunction func(n int) int

func main() {

	// resultado := factorial(2)
	// fmt.Println("El factorial es: ", resultado)

	// var miFuncion = factorial
	var miFuncion customeFunction

	if miFuncion == nil {
		miFuncion = factorial
	}

	// miFuncion = factorial
	resultado := miFuncion(3)

	fmt.Println(resultado)
	

}