package main

import "fmt"

func suma(numero1, numero2 int) (int, string) {

	return numero1 + numero2, "Un mensaje desde la funcion suma"
}


func main() {
	

	resultado, mensaje := suma(10, 20)

	fmt.Println(resultado, mensaje)
}